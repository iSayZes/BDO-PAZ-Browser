"""itemtrade.dbss preview handler."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name, character_title
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_offset_rows
from .parser import parse_itemtrade_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def item_trade_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_id", "characterId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "character_id"),
    )


class ItemTradeHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["name"], sort_key="name"),
            Column(cols["title"], sort_key="title"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {
                **record,
                "name": character_name(record["character_id"]),
                "title": character_title(record["character_id"]),
            }
            for record in parse_itemtrade_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["character_id"]),
                e(r["name"] or _EMPTY),
                e(r["title"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
