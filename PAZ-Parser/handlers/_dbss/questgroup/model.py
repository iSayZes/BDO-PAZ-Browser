from __future__ import annotations

from typing import TypedDict


class QuestGroupLink(TypedDict):
    group_id: int
    quest_no: int
    quest_id: int


class QuestGroupRecord(TypedDict):
    row: int
    offset: int
    size: int
    group_id: int
    name_kr: str
    quest_count: int
    quests: list[QuestGroupLink]
