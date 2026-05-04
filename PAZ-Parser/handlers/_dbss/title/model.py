from __future__ import annotations

from typing import TypedDict


class TitleRecord(TypedDict):
    layout: str
    key_count: int
    key_values: list[int]
    title_id: int
    style_value: int
    style_offset: int
    title_text_ko: str
    requirement_text_ko: str
    requirement_length: int
    category_id: int
    title_color_argb: str
    title_color_css: str
    title_effect_name: str
    extra_payload_size: int
    header_field_meaning: str
    pa_colors: list[str]
    debug_u32: dict[str, int]
    first_pa_color_offset: int | None
