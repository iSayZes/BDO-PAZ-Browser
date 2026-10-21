"""buildingsource.bss preview handler: guild building kits, their build time and repair materials."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.enum_name import enum_name
from _common.html import Column, e, error, icon_html_label_cell, sort_keys, table
from _common.item_key import item_count_list_cell, item_count_text, item_key_icon_path, item_key_text, item_key_text_tagged
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_html
from _common.work_ani_type import WORK_ANI_TYPE_NAMES
from .parser import FILE_NAME, parse_buildingsource_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _repair_items(record: dict) -> list[tuple[int, int]]:
    """`(item_key, count)` of each repair item; the key and count lists run in step."""
    return list(zip(record["repair_item_keys"], record["repair_item_counts"]))


def _with_display_fields(record: dict) -> dict:
    """The record with the kit name, the work animation name and the repair
    items as plain text for tab search and CSV export."""
    return {
        **record,
        "name": item_key_text(record["item_key"]),
        "work_ani_type_name": enum_name(WORK_ANI_TYPE_NAMES, record["work_ani_type"]),
        "repair_items": [item_count_text(key, count) for key, count in _repair_items(record)],
    }


def _kit_cell(item_key: int) -> str:
    return icon_html_label_cell(item_key_icon_path(item_key), pa_html(item_key_text_tagged(item_key)))


def _percents_text(percents: list[int]) -> str:
    return ", ".join(f"{value:,}" for value in percents) or _EMPTY


class BuildingSourceBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemId"], "num", sort_key="item_key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["buildTime"], "num", sort_key="build_time"),
            Column(cols["workAnimation"], sort_key="work_ani_type_name"),
            # List columns: they would only sort by their string form.
            Column(cols["repairItems"]),
            Column(cols["repairPercents"], "num"),
            Column(cols["repairTime"], "num", sort_key="repair_time"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_buildingsource_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [_with_display_fields(record) for record in records]

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
                e(r["item_key"]),
                _kit_cell(r["item_key"]),
                e(f"{r['build_time']:,}"),
                e(r["work_ani_type_name"]),
                item_count_list_cell(_repair_items(r)) or _EMPTY,
                e(_percents_text(r["repair_percents"])),
                e(f"{r['repair_time']:,}"),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
