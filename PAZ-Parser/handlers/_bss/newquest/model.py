from __future__ import annotations

from typing import TypedDict


class NewQuestRecord(TypedDict):
    group: int
    row: int
    flags: int
    quest_chain_id: int
    quest_id: int
    packed_quest_id: int
    sequence_a: int
    sequence_b: int
    sequence_c: int
