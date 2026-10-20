"""petleaderbuff.bss preview handler."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.rate import rate_percent
from .parser import parse_petleaderbuff_records


_LANG_DIR = Path(__file__).parent / "lang"


class PetLeaderBuffBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["petTier"], "num", sort_key="pet_tier"),
            Column(cols["lootCooldown"], "num", sort_key="leader_buff_rate"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_petleaderbuff_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        # The client shows the value as a cut: "Loot cooldown -15%".
        rows = [
            [e(r["pet_tier"]), e(f"-{rate_percent(r['leader_buff_rate'])}")]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
