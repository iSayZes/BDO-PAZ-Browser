"""fairyfeedenchantfailcount.bss parsed preview handler."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.enchant_level import enchant_level_text
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import parse_fairyfeedenchantfailcount_records


_LANG_DIR = Path(__file__).parent / "lang"


class FairyFeedEnchantFailCountBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["fairyFeedKey"], "num", sort_key="fairy_feed_key"),
            # Sorts by level so TET and PEN keep game order.
            Column(cols["enchantLevel"], sort_key="enchant_level"),
            Column(cols["feedValue"], "num", sort_key="feed_value"),
            Column(cols["equipExp"], "num", sort_key="equip_exp"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_fairyfeedenchantfailcount_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        record_count = len({record["record"] for record in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), record_count=record_count)

        rows = [
            [
                e(record["fairy_feed_key"]),
                e(enchant_level_text(record["enchant_level"]) or record["enchant_level"]),
                e(f"{record['feed_value']:,}"),
                e(f"{record['equip_exp']:,}"),
            ]
            for record in slice_
        ]

        return table(meta, self._columns(), rows)
