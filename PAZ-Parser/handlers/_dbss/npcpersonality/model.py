from __future__ import annotations

from typing import TypedDict


class NpcPersonalityRecord(TypedDict):
    row: int
    personality_id: int
    group_a_id: int
    group_a_need_count: int
    group_b_id: int
    group_b_need_count: int
    group_c_id: int
    group_c_need_count: int
    interest_min: float
    interest_max: float
    favor_min: float
    favor_max: float
    personality_type: int


class NpcPersonalityOffsetRecord(TypedDict):
    row: int
    personality_id: int
    data_offset: int
    data_size: int
