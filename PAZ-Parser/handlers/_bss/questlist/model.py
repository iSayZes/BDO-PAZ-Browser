from __future__ import annotations

from typing import TypedDict


class QuestListRecord(TypedDict):
    group: int
    group_key: int
    group_name_kr: str
    unknown_06: int
    event_start: str
    event_end: str
    row: int
    unknown_10: int
    quest_chain_id: int
    quest_id: int
    packed_quest_id: int
    condition_index: int
    condition_kr: str
    script_1_index: int
    script_1: str
    script_2_index: int
    script_2: str
