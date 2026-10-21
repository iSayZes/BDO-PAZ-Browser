"""elementalmonsterstat.bss preview handler: the Black Shrine bosses and the monsters of their fights."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.pabr_values.names import aura_name
from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e, error, flag_cell, sort_keys, table
from _common.item_key import item_count_list_cell, item_count_text
from _common.knowledge import knowledge_name
from _common.lang import handler_text, load_handler_strings
from .parser import FILE_NAME, parse_elementalmonsterstat_records
from .text import difficulty_label, part_label


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_SEPARATOR = ", "


def _reward_items(record: dict) -> list[tuple[int, int]]:
    return [(item["item_key"], item["count"]) for item in record["show_rewards"]]


def _unlock_boss_name(key: int | None, difficulties: dict[int, str]) -> str | None:
    """`Gumiho (Calamity 6)`: the boss to defeat first, with its difficulty when it has a row."""
    if not key:
        return None
    name = character_name(key) or str(key)
    difficulty = difficulties.get(key)
    return f"{name} ({difficulty})" if difficulty else name


class ElementalMonsterStatBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterKey"], "num", sort_key="character_key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["unlockBoss"], sort_key="unlock_character_name"),
            Column(cols["unlockKnowledge"], sort_key="unlock_mental_card_name"),
            Column(cols["offence"], "num", sort_key="offence_stat"),
            Column(cols["defence"], "num", sort_key="defence_stat"),
            Column(cols["weakAura"], sort_key="weak_aura"),
            Column(cols["difficulty"], sort_key="level"),
            Column(cols["group"], "num", sort_key="group"),
            Column(cols["boss"], sort_key="is_boss"),
            Column(cols["part"], sort_key="part"),
            Column(cols["showRewards"]),
            Column(cols["position"]),
            Column(cols["minAp"], "num", sort_key="min_ap"),
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
        try:
            records = parse_elementalmonsterstat_records(data)
            row_ids = character_row_ids(companions)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        rows = [self._record(record, row_ids) for record in records]
        difficulties = {r["character_key"]: r["difficulty"] for r in rows}
        return [
            {**r, "unlock_character_name": _unlock_boss_name(r["unlock_character_key"], difficulties)}
            for r in rows
        ]

    def _record(self, record: dict, row_ids: frozenset[int] | None) -> dict:
        mental_card_key = record["unlock_mental_card_key"]
        part = record["monster_part"]
        return {
            **record,
            "unlock_character_key": record["unlock_character_key"] or None,
            "unlock_mental_card_key": mental_card_key or None,
            "min_ap": record["min_ap"] or None,
            "name": character_name(record["character_key"]),
            "has_character_row": has_character_row(row_ids, record["character_key"]),
            "unlock_mental_card_name": (knowledge_name(mental_card_key) or str(mental_card_key)) if mental_card_key else None,
            "weak_aura": aura_name(record["element_type"]),
            "part": part_label(self.lang, part),
            "difficulty": difficulty_label(self.lang, part, record["level"]),
            "show_rewards_text": _LIST_SEPARATOR.join(
                item_count_text(key, count) for key, count in _reward_items(record)
            ),
        }

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        rows = [self._row(r) for r in records[start : start + page_size]]
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            bosses=sum(1 for r in records if r["is_boss"]),
        )
        return table(meta, self._columns(), rows)

    @staticmethod
    def _row(r: dict) -> list[str]:
        has_position = r["position_x"] or r["position_y"] or r["position_z"]
        return [
            character_key_cell(r["character_key"], r["has_character_row"]),
            e(r["name"] or _EMPTY),
            e(r["unlock_character_name"] or _EMPTY),
            e(r["unlock_mental_card_name"] or _EMPTY),
            e(r["offence_stat"]),
            e(r["defence_stat"]),
            e(r["weak_aura"]),
            e(r["difficulty"]),
            e(r["group"]),
            flag_cell(r["is_boss"]),
            e(r["part"]),
            item_count_list_cell(_reward_items(r)) if r["show_rewards"] else _EMPTY,
            e(f"{r['position_x']:,.0f}, {r['position_y']:,.0f}, {r['position_z']:,.0f}") if has_position else _EMPTY,
            e(r["min_ap"] if r["min_ap"] is not None else _EMPTY),
        ]
