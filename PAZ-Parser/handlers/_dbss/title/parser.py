from __future__ import annotations

import re
import string

from ..common.binary import debug_u32_fields, u32
from ..common.pa_color import extract_pa_colors, first_pa_color_offset
from .model import TitleRecord

_PA_TAG_START = "<PA".encode("utf-16-le")
_PA_TAG_RE = re.compile(r"<PA[^>]+>")
_HEX_BYTES = set(bytes(string.hexdigits, "ascii"))


def detect_layout(block: bytes, title_id: int) -> str:
    key_count = u32(block, 0)
    title_offset = title_offset_for_key_count(key_count)
    if u32(block, title_offset) == title_id:
        return {
            1: "A",
            2: "B",
            3: "C",
        }.get(key_count, f"K{key_count}")

    if u32(block, 8) == title_id:
        return "A"

    if u32(block, 12) == title_id:
        return "B"

    if u32(block, 16) == title_id:
        return "C"

    return "?"


def title_offset_for_key_count(key_count: int) -> int:
    return 4 + key_count * 4


def style_offset_for_layout(layout: str) -> int:
    offsets: dict[str, int] = {
        "A": 12,
        "B": 16,
        "C": 20,
    }

    if layout.startswith("K") and layout[1:].isdigit():
        return title_offset_for_key_count(int(layout[1:])) + 4

    return offsets.get(layout, 0)


def _u16(data: bytes, offset: int) -> int:
    if offset < 0 or offset + 2 > len(data):
        return 0

    return int.from_bytes(data[offset:offset + 2], "little")


def _decode_utf16(data: bytes, start: int, end: int) -> str:
    if end <= start:
        return ""

    return data[start:end].decode("utf-16-le", errors="replace")


def _read_utf16z(data: bytes, start: int) -> tuple[str, int]:
    end = start

    while end + 1 < len(data):
        if data[end] == 0 and data[end + 1] == 0:
            break
        end += 2

    return _decode_utf16(data, start, end), end


def _strip_pa_tags(text: str) -> str:
    return _PA_TAG_RE.sub("", text)


def _decode_ascii(data: bytes) -> str:
    return data.decode("ascii", errors="ignore").rstrip("\x00")


def _extract_title_color(extra_payload: bytes) -> tuple[str, str]:
    payload = extra_payload.rstrip(b"\x00")

    for offset in range(max(0, len(payload) - 64), max(0, len(payload) - 11)):
        raw = payload[offset:offset + 8]
        if len(raw) != 8 or any(byte not in _HEX_BYTES for byte in raw):
            continue

        packed = payload[offset + 8:offset + 12]
        if len(packed) != 4:
            continue

        argb = raw.decode("ascii").upper()
        if int.from_bytes(packed, "little") != int(argb, 16):
            continue

        return f"0x{argb}", f"#{argb[2:]}"

    return "", ""


def _extract_title_effect(extra_payload: bytes) -> str:
    payload = extra_payload.rstrip(b"\x00")

    for offset in range(0, max(0, len(payload) - 7)):
        length = u32(payload, offset)
        if not length or length <= 8 or length > 128:
            continue

        text_start = offset + 8
        text_end = text_start + length
        if text_end > len(payload):
            continue

        raw = payload[text_start:text_end]
        if all(32 <= byte < 127 for byte in raw):
            return _decode_ascii(raw)

    return ""


def _extract_text_fields(
    block: bytes,
    text_start: int,
    style_value: int,
) -> tuple[str, str, int, int, str, str, int, str, str]:
    if text_start >= len(block):
        return "", "", 0, 0, "", "", 0, "", "style"

    is_styled_title = block.startswith(_PA_TAG_START, text_start)
    if is_styled_title:
        title_end = text_start + (style_value + 1) * 2
        title_text = _strip_pa_tags(_decode_utf16(block, text_start, title_end - 2))
        requirement_length = _u16(block, title_end - 2)
        requirement_start = title_end + 6
        header_field_meaning = "styled title length"
    else:
        requirement_start = block.find(_PA_TAG_START, text_start)
        if requirement_start < 0:
            return (
                _decode_utf16(block, text_start, len(block)).rstrip("\x00"),
                "",
                0,
                0,
                "",
                "",
                0,
                "",
                "style",
            )

        title_text = _decode_utf16(block, text_start, requirement_start - 8)
        requirement_length = _u16(block, requirement_start - 8)
        header_field_meaning = "style"

    requirement_text, requirement_end = _read_utf16z(block, requirement_start)
    category_id = u32(block, requirement_end + 4)
    extra_payload = block[requirement_end + 8:]
    title_color_argb, title_color_css = _extract_title_color(extra_payload)

    return (
        title_text.rstrip("\x00"),
        _strip_pa_tags(requirement_text),
        requirement_length,
        category_id,
        title_color_argb,
        title_color_css,
        len(extra_payload.rstrip(b"\x00")),
        _extract_title_effect(extra_payload),
        header_field_meaning,
    )


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
        key_count = u32(block, 0)
        key_values = [u32(block, 4 + index * 4) for index in range(key_count)]
        style_offset = style_offset_for_layout(layout)
        style_value = u32(block, style_offset) if style_offset else 0
        text_start = style_offset + 8 if style_offset else 0
        (
            title_text_ko,
            requirement_text_ko,
            requirement_length,
            category_id,
            title_color_argb,
            title_color_css,
            extra_payload_size,
            title_effect_name,
            header_field_meaning,
        ) = _extract_text_fields(block, text_start, style_value)

        records.append(TitleRecord(
            layout=layout,
            key_count=key_count,
            key_values=key_values,
            title_id=title_id,
            style_value=style_value,
            style_offset=style_offset,
            title_text_ko=title_text_ko,
            requirement_text_ko=requirement_text_ko,
            requirement_length=requirement_length,
            category_id=category_id,
            title_color_argb=title_color_argb,
            title_color_css=title_color_css,
            title_effect_name=title_effect_name,
            extra_payload_size=extra_payload_size,
            header_field_meaning=header_field_meaning,
            pa_colors=extract_pa_colors(block),
            debug_u32=debug_u32_fields(block),
            first_pa_color_offset=first_pa_color_offset(block),
        ))

    return records
