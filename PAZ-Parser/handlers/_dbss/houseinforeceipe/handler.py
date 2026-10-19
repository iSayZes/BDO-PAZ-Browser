"""houseinforeceipe.dbss preview handler: house uses with their per-level item exchanges."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.enum_name import enum_name
from _common.html import Column, e, html_list_cell, record_link, sort_keys, table
from _common.item_exchange import exchange_list_cell, exchange_text
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_text
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_u32_offset_rows
from .house_enums import HOUSE_ICON_TYPE_NAMES, HOUSE_USE_TYPE_NAMES
from .parser import parse_houseinforeceipe_records


_LANG_DIR = Path(__file__).parent / "lang"
_LOC_TYPE_RECEIPE = 16
_EMPTY = "-"
_HOUSEINFONEEDITEM = "gamecommondata/binary/houseinfoneeditem.dbss"
_LINK_CLASS = "record-link"
# Exchanges shown per level line; the rest go behind a hoverable count.
_KEYS_PER_LEVEL = 4


def house_info_receipe_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("receipe_key", "receipeKey"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "receipe_key"),
    )


def _with_display_fields(record: dict) -> dict:
    """The record with its name in the user language (else Korean), its enum
    names, its filled level count, its exchange key count and its exchange names."""
    levels = record["level_exchanges"]
    exchange_count = sum(len(keys) for keys in levels)
    return {
        **record,
        "name": loc_text(_LOC_TYPE_RECEIPE, record["receipe_key"]) or record["name_kr"],
        "house_use_type_name": enum_name(HOUSE_USE_TYPE_NAMES, record["house_use_type"]),
        "icon_type_name": enum_name(HOUSE_ICON_TYPE_NAMES, record["icon_type"]),
        "level_count": sum(1 for keys in levels if keys),
        # None on a use with no exchanges, so its "-" cell sorts last.
        "exchange_count": exchange_count or None,
        # `Azwell Longsword (5026)` per key, level by level, so tab search and CSV export see them.
        "exchanges": [exchange_text(key) for keys in levels for key in keys],
    }


class HouseInfoReceipeHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["receipeKey"], "num", sort_key="receipe_key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["useType"], sort_key="house_use_type_name"),
            Column(cols["iconType"], sort_key="icon_type_name"),
            Column(cols["needItemKey"], "num", sort_key="need_item_key"),
            Column(cols["levels"], "num", sort_key="level_count"),
            Column(cols["exchanges"], sort_key="exchange_count"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [_with_display_fields(record) for record in parse_houseinforeceipe_records(data)]

    def _exchanges_cell(self, levels: list[list[int]]) -> str:
        """One line per filled level: its label and its exchanges, each linked to its row."""
        lines = [
            f"{e(handler_text(self.lang, _LANG_DIR, 'cells.level', level=level))} "
            f"{exchange_list_cell(keys, _KEYS_PER_LEVEL)}"
            for level, keys in enumerate(levels, start=1)
            if keys
        ]
        return html_list_cell(lines, separator="<br>") if lines else _EMPTY

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        rows = [
            [
                e(r["receipe_key"]),
                e(r["name"]),
                e(r["house_use_type_name"]),
                e(r["icon_type_name"]),
                record_link(str(r["need_item_key"]), _HOUSEINFONEEDITEM, "need_item_key", r["need_item_key"], _LINK_CLASS),
                e(r["level_count"]),
                self._exchanges_cell(r["level_exchanges"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            exchanges=len({key for r in records for keys in r["level_exchanges"] for key in keys}),
        )
        return table(meta, self._columns(), rows)
