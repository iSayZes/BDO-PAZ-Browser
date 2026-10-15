from __future__ import annotations

from typing import TypedDict


class QuestListRecord(TypedDict):
    group: int
    group_key: int
    group_name_kr: str
    group_type: int
    event_start: str
    event_end: str
    row: int
    is_sub_quest: bool
    quest_chain_id: int
    quest_id: int
    packed_quest_id: int
    condition_index: int
    condition_kr: str
    hide_conditions_index: int
    hide_conditions: str
    visible_conditions_index: int
    visible_conditions: str
