from __future__ import annotations

from typing import TypedDict


class MentalThemeOffsetRecord(TypedDict):
    row: int
    theme_id: int
    payload_offset: int
    payload_size: int


class MentalThemeRecord(TypedDict):
    row: int
    theme_id: int
    offset_theme_id: int
    payload_offset: int
    payload_size: int
    name_ko: str
    name: str
    parent_id: int
    parent_name: str
    increase_wp: int
    need_count: int
    increase_wp_2: int
    need_count_2: int
    unknown_flag: int
    unknown_value: int
    entry_count: int
    entry_ids: str
    entry_names: str
    child_count: int
    child_ids: str
    terminator: int
