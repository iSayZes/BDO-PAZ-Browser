from __future__ import annotations

from typing import TypedDict


class ZodiacSignOffsetRecord(TypedDict):
    row: int
    zodiac_id: int
    data_offset: int
    data_size: int


class ZodiacSignOrderRecord(TypedDict):
    row: int
    personality_type: int
    zodiac_id: int
    trigger_count: int
    trigger_order: list


class ZodiacSignOrderOffsetRecord(TypedDict):
    row: int
    personality_type: int
    data_offset: int
    data_size: int
    padding: int
