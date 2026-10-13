from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import parse_itemcouponreward_offset_records


_LANG_DIR = Path(__file__).parent / "lang"


class ItemCouponRewardOffsetHandler(PreviewHandler):
    """Raw u32 words of itemcouponrewardoffset.dbss; docs/file-formats/itemcouponreward_dbss.md."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["offset"], "num", sort_key="offset"),
            Column(cols["field"], sort_key="field"),
            Column(cols["value"], "num", sort_key="value"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_itemcouponreward_offset_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.words", count=len(records))
        rows = [
            [e(f"+0x{r['offset']:02X}"), e(r["field"]), e(r["value"])]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
