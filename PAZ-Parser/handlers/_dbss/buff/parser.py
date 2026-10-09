"""`buff.dbss` records, located through `buffoffset.dbss`.

Each record chains fixed blocks and length-prefixed strings:

    u32 buff_id | name | 133-byte stats block | unknown_str | icon_path
    | u8 is_shown | u32 apply_rate | description | 27-byte tail block

Full layout in docs/file-formats/buff_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u16, u32
from _common.buff import buff_icon_path
from _common.inline_text import decode_inline_text
from _common.pabr_offset import PabrOffsetRow, parse_pabr_u32_offset_rows
from _common.prefixed_string import read_prefixed_at
from _common.teleport import TELEPORT_EFFECT_TYPE, teleport_point_id


_ID_SIZE = 4
STATS_BLOCK_SIZE = 133
TAIL_BLOCK_SIZE = 27
PARAM_COUNT = 10

# Field offsets inside the stats block.
_LEVEL = 0x00
_GROUP = 0x04
_CONDITION_TYPE = 0x06
_EFFECT_TYPE = 0x08
_PARAMS = 0x13
_DURATION_MS = 0x68
_TICK_MS = 0x6C

# Tail block offset of the broad family byte (food, elixir, perfume, ...).
_STACKING_CATEGORY = 0x18
# Tail block flag: applying the buff ends the others of its stacking category.
_IS_EXCLUSIVE = 0x19

_I16 = struct.Struct("<h")
_PARAMS_STRUCT = struct.Struct(f"<{PARAM_COUNT}q")


def _parse_record(data: bytes, row: PabrOffsetRow) -> dict:
    start = row.offset
    end = start + row.size
    if end > len(data):
        raise ValueError(f"buff {row.entry_id} runs past the end of buff.dbss")
    if u32(data, start) != row.entry_id:
        raise ValueError(f"buff {row.entry_id} record does not start with its own ID")

    name, stats = read_prefixed_at(data, start + _ID_SIZE, end, wide=True)
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
        "level": _I16.unpack_from(data, stats + _LEVEL)[0],
        "effect_type": data[stats + _EFFECT_TYPE],
        # A u16: keys from 40001 up read negative as an i16.
        "group": u16(data, stats + _GROUP),
        "condition_type": _I16.unpack_from(data, stats + _CONDITION_TYPE)[0],
        "duration_ms": u32(data, stats + _DURATION_MS),
        # Tick interval of a periodic effect; 0 on everything else.
        "tick_ms": u32(data, stats + _TICK_MS),
        "unknown_str": unknown_str,
        "icon_path": buff_icon_path(icon),
        "is_shown": bool(is_shown),
        "apply_rate": apply_rate,
        "description_kr": decode_inline_text(description),
        "stacking_category": data[pos + _STACKING_CATEGORY],
        "is_exclusive": bool(data[pos + _IS_EXCLUSIVE]),
    }
    record.update({f"param_{index}": value for index, value in enumerate(params, 1)})
    return record


def parse_buff_records(data: bytes, offset_rows: list[PabrOffsetRow]) -> list[dict]:
    """Parse every record the offset table points at, in offset-table order.

    Raises ValueError on the first malformed record: the layout has no resync
    point, so a bad length would silently misread every field after it.
    """
    return [_parse_record(data, row) for row in offset_rows]


def _teleport_buffs(data: bytes, offset_data: bytes) -> list[dict]:
    """The effect type 23 buffs, which name a teleport.dbss section and key."""
    records = parse_buff_records(data, parse_pabr_u32_offset_rows(offset_data))
    return [record for record in records if record["effect_type"] == TELEPORT_EFFECT_TYPE]


def build_teleport_buff_index(data: bytes, offset_data: bytes) -> dict[int, tuple[int, ...]]:
    """The `TELEPORT_BUFFS` index: each teleport point to the buffs that go there, by buff ID."""
    points: dict[int, list[int]] = {}
    for record in _teleport_buffs(data, offset_data):
        point_id = teleport_point_id(record["param_1"], record["param_2"])
        points.setdefault(point_id, []).append(record["buff_id"])
    return {point_id: tuple(sorted(buff_ids)) for point_id, buff_ids in points.items()}


def build_teleport_buff_name_index(data: bytes, offset_data: bytes) -> dict[int, str]:
    """The `TELEPORT_BUFF_NAME_KR` index: each teleport buff to its Korean name."""
    return {
        record["buff_id"]: record["name"].strip()
        for record in _teleport_buffs(data, offset_data)
        if record["name"].strip()
    }
