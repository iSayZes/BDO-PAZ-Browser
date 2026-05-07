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
