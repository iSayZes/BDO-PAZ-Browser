"""houseinfoneeditem.dbss preview handler: the items and time each house level costs."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.duration import format_duration
from _common.html import Column, e, error, html_list_cell, icon_html_label_cell, sort_keys, table, text_list_cell
from _common.item_key import item_key_icon_path, item_key_text_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_html
from _common.pabr_offset import parse_bare_offset_rows
from _dbss.guildhousecraftskill.labels import house_use_name
from _dbss.houseinforeceipe.parser import FILE_NAME as RECEIPE_FILE
from _dbss.houseinforeceipe.parser import parse_houseinforeceipe_records
from .parser import FILE_NAME, parse_houseinfoneeditem_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_MS_PER_SECOND = 1000
# House use names shown per row; the rest go behind a hoverable count.
_HOUSE_USES_SHOWN = 6


def house_info_need_item_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("need_item_key", "needItemKey"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "need_item_key"),
    )


def receipes_by_group(receipe_data: bytes | None) -> dict[int, list[dict]]:
    """The `houseinforeceipe.dbss` rows of each `need_item_key`, in file order.

    Empty without the companion.
    """
    if receipe_data is None:
        return {}
    groups: dict[int, list[dict]] = {}
    for receipe in parse_houseinforeceipe_records(receipe_data):
        groups.setdefault(receipe["need_item_key"], []).append(receipe)
    return groups


def _house_uses(receipes: list[dict]) -> list[str]:
    """Each distinct house use name once: the LOC type 16 name in the user
    language, else the Korean name. Several towns share one name."""
    names = (house_use_name(receipe["receipe_key"]) or receipe["name_kr"] for receipe in receipes)
    return list(dict.fromkeys(names))


def _priced_levels(levels: list[dict]) -> list[dict]:
    return [level for level in levels if level["items"]]


def _with_display_fields(record: dict, receipes: list[dict]) -> dict:
    """The record with the receipe keys that use it, their house use names
    and its priced level count."""
    return {
        **record,
        "receipe_keys": [receipe["receipe_key"] for receipe in receipes],
        "house_uses": _house_uses(receipes),
        "level_count": len(_priced_levels(record["levels"])),
    }


class HouseInfoNeedItemHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["needItemKey"], "num", sort_key="need_item_key"),
            Column(cols["houseUses"]),
            Column(cols["levels"], "num", sort_key="level_count"),
            Column(cols["needItems"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{RECEIPE_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_houseinfoneeditem_records(data)
            receipes = receipes_by_group(companions.get(RECEIPE_FILE))
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [_with_display_fields(record, receipes.get(record["need_item_key"], [])) for record in records]

    def _level_line(self, level: dict) -> str:
        """`Lv 2: Silver x2,500 · 5s`: the level, each item with its icon, then the time."""
        label = e(handler_text(self.lang, _LANG_DIR, "cells.level", level=level["level"]))
        items = ", ".join(
            icon_html_label_cell(
                item_key_icon_path(item["item_key"]),
                f"{pa_html(item_key_text_tagged(item['item_key']))} x{item['count']:,}",
            )
            for item in level["items"]
        )
        time_text = format_duration(level["transfer_time"] * _MS_PER_SECOND)
        return f"{label} {items}" + (f" · {e(time_text)}" if time_text else "")

    def _need_items_cell(self, levels: list[dict]) -> str:
        lines = [self._level_line(level) for level in _priced_levels(levels)]
        return html_list_cell(lines, separator="<br>") if lines else _EMPTY

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        rows = [
            [
                e(r["need_item_key"]),
                text_list_cell(r["house_uses"], _HOUSE_USES_SHOWN) if r["house_uses"] else _EMPTY,
                e(r["level_count"]),
                self._need_items_cell(r["levels"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
