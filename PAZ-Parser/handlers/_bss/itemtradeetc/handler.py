"""itemtradeetc.bss preview handler: the desert trade buff per trade group pair."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.trade_group import trade_group_text, trade_group_tooltip
from .parser import FILE_NAME, parse_itemtradeetc


_LANG_DIR = Path(__file__).parent / "lang"


class ItemTradeEtcBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        guess = f'title="{e(trade_group_tooltip(self.lang))}"'
        return [
            Column(cols["fromGroup"], extra_attrs=guess, sort_key="from_group"),
            Column(cols["toGroup"], extra_attrs=guess, sort_key="to_group"),
            Column(cols["distance"], "num", sort_key="distance"),
            Column(cols["addRate"], "num", sort_key="add_rate"),
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
            parsed = parse_itemtradeetc(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        # The 12-byte rows after the pairs are unknown and stay out of the table.
        return [
            {
                **pair,
                "from_group_text": trade_group_text(self.lang, pair["from_group"]),
                "to_group_text": trade_group_text(self.lang, pair["to_group"]),
            }
            for pair in parsed.pairs
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
                e(r["from_group_text"]),
                e(r["to_group_text"]),
                e(f"{r['distance']:,.0f}"),
                e(f"{r['add_rate']:,}"),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
