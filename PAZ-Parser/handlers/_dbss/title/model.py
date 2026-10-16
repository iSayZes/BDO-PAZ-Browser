from __future__ import annotations

from typing import TypedDict


class TitleRecord(TypedDict):
    key_count: int
    key_values: list[int]
    title_id: int
    title_text_kr: str
    requirement_text_kr: str
    # The title names itself in PAColor tags ("MASTER ..." gradients).
    is_styled_title: bool
    category_id: int
    unknown_tail_1c: int
    unknown_tail_24: int
    title_color_argb: str
    title_color_css: str
    title_effect_name: str
