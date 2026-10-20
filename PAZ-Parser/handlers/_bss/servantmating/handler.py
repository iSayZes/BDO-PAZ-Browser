from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.rate import rate_percent
from .parser import parse_servantmating_records


_LANG_DIR = Path(__file__).parent / "lang"


class ServantMatingBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["averageGrade"], "num", sort_key="average_grade"),
            Column(cols["resultMaxGrade"], "num", sort_key="result_max_grade"),
            Column(cols["resultMinGrade"], "num", sort_key="result_min_grade"),
            Column(cols["imperialSteedCharacterId"], "num", sort_key="imperial_steed_character_id"),
            Column(cols["imperialSteed"], sort_key="imperial_steed_name"),
            Column(cols["imperialSteedRate"], "num", sort_key="imperial_steed_rate"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        row_ids = character_row_ids(companions)
        return [
            {
                **record,
                # The shown name: LOC in the user's language, else the character ID.
                "imperial_steed_name": (
                    character_name(record["imperial_steed_character_id"])
                    or str(record["imperial_steed_character_id"])
                ),
                "has_character_row": has_character_row(row_ids, record["imperial_steed_character_id"]),
            }
            for record in parse_servantmating_records(data)
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
                e(r["key"]),
                e(r["average_grade"]),
                e(r["result_max_grade"]),
                e(r["result_min_grade"]),
                character_key_cell(r["imperial_steed_character_id"], r["has_character_row"]),
                e(r["imperial_steed_name"]),
                e(rate_percent(r["imperial_steed_rate"])),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
