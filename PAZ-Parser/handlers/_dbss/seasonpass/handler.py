"""seasonpass.dbss preview handler: one row per Black Spirit Pass row with its free and premium quest."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.quest.quest import quest_title, split_packed_quest_id
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_seasonpass_file


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# The packed quest fields of a row and the record field that shows each.
_QUEST_FIELDS = (
    ("base_reward_quest", "base_reward_quest_text"),
    ("premium_reward_quest", "premium_reward_quest_text"),
    ("condition_quest", "condition_quest_text"),
)


def quest_text(packed_quest_id: int) -> str:
    """`50000/1 Title`, the chain and quest without a title, or '' for no quest."""
    if not packed_quest_id:
        return ""
    chain, quest = split_packed_quest_id(packed_quest_id)
    return f"{chain}/{quest} {quest_title(chain, quest)}".strip()


def _text_cell(text: str) -> str:
    return e(text) if text else _EMPTY


class SeasonPassHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["passNo"], "num", sort_key=KEY_FIELD),
            Column(labels["freeQuest"], sort_key="base_reward_quest_text"),
            Column(labels["premiumQuest"], sort_key="premium_reward_quest_text"),
            Column(labels["seasonType"], "num", sort_key="season_type"),
            Column(labels["conditionQuest"], sort_key="condition_quest_text"),
            Column(labels["changedTitle"], sort_key="changed_title_kr"),
            Column(labels["changedDescription"], sort_key="changed_desc_kr"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**row, **{text: quest_text(row[field]) for field, text in _QUEST_FIELDS}}
            for row in parse_seasonpass_file(data).rows
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            _text_cell(record["base_reward_quest_text"]),
            _text_cell(record["premium_reward_quest_text"]),
            e(record["season_type"]),
            _text_cell(record["condition_quest_text"]),
            _text_cell(record["changed_title_kr"]),
            _text_cell(record["changed_desc_kr"]),
        ]
