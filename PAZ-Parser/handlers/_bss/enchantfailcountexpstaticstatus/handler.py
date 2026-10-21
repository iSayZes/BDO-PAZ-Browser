"""enchantfailcountexpstaticstatus.bss parsed preview handler."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.enchant_level import enchant_level_text
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import parse_enchantfailcountexp_rows


_LANG_DIR = Path(__file__).parent / "lang"


class EnchantFailCountExpBssHandler(PreviewHandler):
    """One row per (stack, feed key, enchant level).

    `unknown_01`, the only value, stays on the record for search and export
    but gets no column until it is named.
    """

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["stack"], "num", sort_key="stack"),
            Column(cols["fairyFeedKey"], "num", sort_key="fairy_feed_key"),
            # Sorts by level so TET and PEN keep game order.
            Column(cols["enchantLevel"], sort_key="enchant_level"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_enchantfailcountexp_rows(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        stack_count = len({record["stack"] for record in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), stack_count=stack_count)

        rows = [
            [
                e(f"{record['stack']:,}"),
                e(record["fairy_feed_key"]),
                e(enchant_level_text(record["enchant_level"]) or record["enchant_level"]),
            ]
            for record in slice_
        ]

        return table(meta, self._columns(), rows)
