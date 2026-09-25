"""`buff.dbss` records, located through `buffoffset.dbss`.

Each record chains fixed blocks and length-prefixed strings:

    u16 buff_id | name | 133-byte stats block | unknown_str | icon_path
    | u8 is_shown | u32 apply_rate | description | 27-byte tail block

Full layout in docs/file-formats/buff_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u16, u32
from _common.pabr_offset import PabrOffsetRow
from _common.prefixed_string import read_prefixed_at


STATS_BLOCK_SIZE = 133
TAIL_BLOCK_SIZE = 27
PARAM_COUNT = 10

# Stored paths start at "New_Icon/", which lives under ui_texture/icon/.
ICON_ROOT = "ui_texture/icon/"
# 221 records store this literal instead of leaving the path empty.
_ICON_PLACEHOLDER = "unknown"

# Field offsets inside the stats block.
_LEVEL = 0x00
_UNKNOWN_04 = 0x04
_EFFECT_TYPE = 0x08
_PARAMS = 0x13
_DURATION_MS = 0x68

_PARAMS_STRUCT = struct.Struct(f"<{PARAM_COUNT}q")


def _icon_paz_path(stored: str) -> str:
    """PAZ path for a stored icon, or an empty string when there is none."""
    path = stored.strip().replace("\\", "/").lower()
    if not path or path == _ICON_PLACEHOLDER:
        return ""
    return f"{ICON_ROOT}{path}"


def _parse_record(data: bytes, row: PabrOffsetRow) -> dict:
    start = row.offset
    end = start + row.size
    if end > len(data):
        raise ValueError(f"buff {row.entry_id} runs past the end of buff.dbss")
    if u16(data, start) != row.entry_id:
        raise ValueError(f"buff {row.entry_id} record does not start with its own ID")

    name, stats = read_prefixed_at(data, start + 2, end, wide=True)
    unknown_str, pos = read_prefixed_at(data, stats + STATS_BLOCK_SIZE, end, wide=True)
    icon, pos = read_prefixed_at(data, pos, end, wide=False)

    is_shown = data[pos]
    apply_rate = u32(data, pos + 1)
    description, pos = read_prefixed_at(data, pos + 5, end, wide=True)

    if pos + TAIL_BLOCK_SIZE != end:
        raise ValueError(
            f"buff {row.entry_id} tail is {end - pos} bytes, expected {TAIL_BLOCK_SIZE}"
        )

    params = _PARAMS_STRUCT.unpack_from(data, stats + _PARAMS)
    record = {
        "buff_id": row.entry_id,
        "name": name,
        "level": u32(data, stats + _LEVEL),
        "effect_type": data[stats + _EFFECT_TYPE],
        "unknown_04": u32(data, stats + _UNKNOWN_04),
        "duration_ms": u32(data, stats + _DURATION_MS),
        "unknown_str": unknown_str,
        "icon_path": _icon_paz_path(icon),
        "is_shown": bool(is_shown),
        "apply_rate": apply_rate,
        "description_kr": description,
    }
    record.update({f"param_{index}": value for index, value in enumerate(params, 1)})
    return record


def parse_buff_records(data: bytes, offset_rows: list[PabrOffsetRow]) -> list[dict]:
    """Parse every record the offset table points at, in offset-table order.

    Raises ValueError on the first malformed record: the layout has no resync
    point, so a bad length would silently misread every field after it.
    """
    return [_parse_record(data, row) for row in offset_rows]
