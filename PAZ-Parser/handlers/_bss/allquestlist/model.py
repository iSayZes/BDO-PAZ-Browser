from __future__ import annotations

from typing import TypedDict


class AllQuestListRecord(TypedDict):
    slot: int
    packed_quest_id: int
    quest_chain_id: int
    quest_id: int
