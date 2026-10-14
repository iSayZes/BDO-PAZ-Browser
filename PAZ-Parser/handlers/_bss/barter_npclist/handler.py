from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.town import town_name
from .parser import parse_barter_npclist_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class BarterNpcListBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["regionKey"], "num", sort_key="barter_region_key"),
            Column(cols["region"], sort_key="region_name"),
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["npc"], sort_key="npc_name"),
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
                # LOC type 17 names regions; the barter regions are regions.
                "region_name": town_name(record["barter_region_key"]),
                "npc_name": character_name(record["character_id"]),
            }
            for record in parse_barter_npclist_records(data)
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
                e(r["barter_region_key"]),
                e(r["region_name"] or _EMPTY),
                e(r["character_id"]),
                e(r["npc_name"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
