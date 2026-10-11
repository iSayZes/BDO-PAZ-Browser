from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.enchant_level import enchant_level_text
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import parse_cronenchant_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"

# Columns after Gear and Grade: (lang key, record field), all numbers.
_NUMBER_COLUMNS = (
    ("caphrasLevel", "caphras_level"),
    ("stones", "stones"),
    ("totalStones", "total_stones"),
    ("ap", "ap"),
    ("dp", "dp"),
    ("accuracy", "accuracy"),
    ("evasion", "evasion"),
    ("hiddenEvasion", "hidden_evasion"),
    ("damageReduction", "damage_reduction"),
    ("hiddenDamageReduction", "hidden_damage_reduction"),
    ("hp", "hp"),
    ("mp", "mp"),
)


class CronEnchantBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["category"], "num", sort_key="category"),
            Column(cols["gear"], sort_key="gear"),
            # Sorts by level so TRI, TET and PEN keep game order.
            Column(cols["grade"], sort_key="enchant_level"),
            *(Column(cols[key], "num", sort_key=field) for key, field in _NUMBER_COLUMNS),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        # The file has no category names; the lang files name them after the
        # Caphras cost tables they match (cronenchant_bss.md, Categories).
        gear = load_handler_strings(self.lang, _LANG_DIR)["gear"]
        return [
            {
                **record,
                "gear": gear.get(str(record["category"]), ""),
                "grade": enchant_level_text(record["enchant_level"]),
                # DP is evasion plus damage reduction, as the game and bdocodex show it.
                "dp": record["evasion"] + record["damage_reduction"],
            }
            for record in parse_cronenchant_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            categories=len({record["category"] for record in records}),
        )
        rows = [
            [
                e(r["category"]),
                e(r["gear"] or _EMPTY),
                e(r["grade"] or r["enchant_level"]),
                *(e(r[field]) for _, field in _NUMBER_COLUMNS),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
