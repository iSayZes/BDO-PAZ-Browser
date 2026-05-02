from __future__ import annotations

from typing import TypedDict


class TitleRecord(TypedDict):
    layout: str
    title_id: int
    style_value: int
    style_offset: int
    pa_colors: list[str]
    debug_u32: dict[str, int]
    first_pa_color_offset: int | None
