from __future__ import annotations

from ..common.binary import debug_u32_fields, u32
from ..common.pa_color import extract_pa_colors, first_pa_color_offset
from .model import TitleRecord


def detect_layout(block: bytes, title_id: int) -> str:
    if u32(block, 8) == title_id:
        return "A"

    if u32(block, 12) == title_id:
        return "B"

    if u32(block, 16) == title_id:
        return "C"

    return "?"


def style_offset_for_layout(layout: str) -> int:
    offsets: dict[str, int] = {
        "A": 12,
        "B": 16,
        "C": 20,
    }

    return offsets.get(layout, 0)


def extract_title_records(
    data: bytes,
    offset_map: dict[int, tuple[int, int]],
) -> list[TitleRecord]:
    records: list[TitleRecord] = []

    for title_id, (offset, size) in sorted(offset_map.items()):
        if offset + size > len(data):
            continue

        block = data[offset:offset + size]
        layout = detect_layout(block, title_id)
        style_offset = style_offset_for_layout(layout)
        style_value = u32(block, style_offset) if style_offset else 0

        records.append(TitleRecord(
            layout=layout,
            title_id=title_id,
            style_value=style_value,
            style_offset=style_offset,
            pa_colors=extract_pa_colors(block),
            debug_u32=debug_u32_fields(block),
            first_pa_color_offset=first_pa_color_offset(block),
        ))

    return records
