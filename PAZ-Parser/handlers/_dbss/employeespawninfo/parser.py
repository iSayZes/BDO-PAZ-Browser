"""`employeespawninfo.dbss`: hire data of the sailors in the port towns.

The main file is a u32 count and one variable-length row per sailor character:

    u16 character_key | u32 employee_key | u32 spawn_count
    | u32 spawn_position_keys[spawn_count]
    | 44-byte hire block (unknown u32s, u32 respawn_time_s, u32 hire_item_key,
      u64 hire_item_count)
    | u64-prefixed UTF-16 accept_text_ko | u64-prefixed UTF-16 refuse_text_ko
    | u32 terminator

`employeespawninfooffset.dbss` is a bare offset table of 10-byte
[u16 character_key][u32 offset][u32 size] rows. Full layout in
docs/file-formats/employeespawninfo_dbss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import parse_bare_offset_rows
from _common.record_reader import RecordReader


_HEAD = struct.Struct("<HII")
_U32 = struct.Struct("<I")
# Seven u32 (unknown_00 to unknown_18, respawn_time_s at +0x10), u32 hire_item_key,
# u64 hire_item_count, u32 unknown_28.
_HIRE_BLOCK = struct.Struct("<7IIQI")
_HIRE_FIELDS = (
    "unknown_00", "unknown_04", "unknown_08", "unknown_0c", "respawn_time_s", "unknown_14", "unknown_18",
    "hire_item_key", "hire_item_count", "unknown_28",
)


def parse_employeespawninfooffset_records(data: bytes) -> list[dict]:
    return [
        {"character_key": row.entry_id, "data_offset": row.offset, "data_size": row.size}
        for row in parse_bare_offset_rows(data)
    ]


def _sailor_record(data: bytes, offset_row: dict) -> dict:
    start = offset_row["data_offset"]
    label = f"sailor {offset_row['character_key']}"
    reader = RecordReader(data, start, start + offset_row["data_size"], label)

    character_key, employee_key, spawn_count = reader.unpack(_HEAD)
    if character_key != offset_row["character_key"]:
        raise ValueError(f"{label}: row holds key {character_key}")
    spawn_position_keys = [reader.unpack(_U32)[0] for _ in range(spawn_count)]
    hire = dict(zip(_HIRE_FIELDS, reader.unpack(_HIRE_BLOCK)))
    accept_text_ko = reader.text(wide=True)
    refuse_text_ko = reader.text(wide=True)
    (terminator,) = reader.unpack(_U32)
    if not reader.at_end():
        raise ValueError(f"{label}: {reader.remaining()} bytes left after the row")

    return {
        "character_key": character_key,
        "employee_key": employee_key,
        "spawn_position_keys": spawn_position_keys,
        **hire,
        "accept_text_ko": accept_text_ko,
        "refuse_text_ko": refuse_text_ko,
        "terminator": terminator,
    }


def parse_employeespawninfo_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Every sailor row the offset companion points at, in its order.

    Raises ValueError when a row lies outside the file, holds a key other
    than the offset row's, or does not end exactly at its recorded size.
    """
    return [_sailor_record(data, row) for row in parse_employeespawninfooffset_records(offset_data)]
