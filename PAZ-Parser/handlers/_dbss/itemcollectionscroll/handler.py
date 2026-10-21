"""itemcollectionscroll.dbss preview handler: the bonuses and time use of each Item Collection Increase gauge level."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.rate import rate_percent
from .parser import FILE_NAME, parse_itemcollectionscroll_records


_LANG_DIR = Path(__file__).parent / "lang"


def item_collection_scroll_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("grade", "grade"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "grade", "data_offset", "data_size"),
    )


class ItemCollectionScrollHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["grade"], "num", sort_key="grade"),
            Column(cols["dropRate"], "num", sort_key="drop_rate"),
            Column(cols["countRate"], "num", sort_key="count_rate"),
            Column(cols["costPercent"], "num", sort_key="cost_percent"),
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
            return parse_itemcollectionscroll_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

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
                e(r["grade"]),
                e(rate_percent(r["drop_rate"])),
                e(rate_percent(r["count_rate"])),
                e(rate_percent(r["cost_percent"])),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
