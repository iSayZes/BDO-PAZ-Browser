from __future__ import annotations

from typing import TypedDict


class TitleBuffRecord(TypedDict):
    buff_id: int
    offset: int
    raw_text: str
    debug_u32: dict[str, int]
