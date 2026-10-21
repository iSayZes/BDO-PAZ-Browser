"""barter_special.bss preview handler: one row per special barter offer."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.barter.category import category_names
from _bss.barter.display import exchange_cells, exchange_columns, exchange_text_fields
from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import FILE_NAME, parse_barter_special_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class BarterSpecialBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["index"], "num", sort_key="index"),
            Column(cols["regionKey"], "num", sort_key="barter_region_key"),
            Column(cols["selectRate"], "num", sort_key="select_rate"),
            *exchange_columns(self.lang),
            Column(cols["subGroup"], "num", sort_key="barter_sub_group"),
            Column(cols["category"], sort_key="category_names"),
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
            records = parse_barter_special_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [
            {
                **record,
                **exchange_text_fields(record),
                "category_names": category_names(record["barter_category"]),
            }
            for record in records
        ]

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
                e(r["index"]),
                e(r["barter_region_key"]),
                e(f"{r['select_rate']:,}"),
                *exchange_cells(r),
                e(r["barter_sub_group"]),
                e(r["category_names"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
