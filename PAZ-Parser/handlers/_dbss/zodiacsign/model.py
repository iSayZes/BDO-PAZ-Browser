from __future__ import annotations

from typing import TypedDict


class ZodiacSignRecord(TypedDict):
    row: int
    zodiac_id: int
    float_count: int
    pairs_count: int
    constellation_name: str
    trait_text: str
    icon_small: str
    icon_large: str
    next_zodiac_id: int


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


class ZodiacSignIndexRecord(TypedDict):
    slot: int
    zodiac_id: int
