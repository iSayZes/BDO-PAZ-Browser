"""`rosewarrevivepositionstaticstatus.bss`: where Rose War players revive.

    PABR | u32 team_count | team_count x Team Point
    | u32 sanctum_count | sanctum_count x Sanctum Point | string table
    | u32 table_start | u32 0
    Team Point: u8 respawn_position_type | Points
    Sanctum Point: u16 fierce_battle_key | Points
    Points: u32 position_count | position_count x (f32 x, y, z) | f32 unknown_positions_00

Full layout in docs/file-formats/bss/rosewarrevivepositionstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import whole_float
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, check_rows_end
from _common.record_reader import RecordReader


FILE_NAME = "rosewarrevivepositionstaticstatus.bss"

_COUNT = struct.Struct("<I")
_RESPAWN_POSITION_TYPE = struct.Struct("<B")
_FIERCE_BATTLE_KEY = struct.Struct("<H")
_POSITION = struct.Struct("<3f")
_UNKNOWN_FLOAT = struct.Struct("<f")


def _read_points(reader: RecordReader) -> dict:
    """The positions of one revive point and the f32 after them."""
    (count,) = reader.unpack(_COUNT)
    if count * _POSITION.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} position count {count:,} runs past the string table")
    positions = [list(reader.unpack(_POSITION)) for _ in range(count)]
    (unknown,) = reader.unpack(_UNKNOWN_FLOAT)
    return {"positions": positions, "unknown_positions_00": whole_float(unknown)}


def _read_group(reader: RecordReader, key: struct.Struct, field: str, other: str) -> list[dict]:
    """One counted group of revive points; `other` is the key field the group lacks."""
    (count,) = reader.unpack(_COUNT)
    records: list[dict] = []
    for _ in range(count):
        (value,) = reader.unpack(key)
        records.append({field: value, other: None, **_read_points(reader)})
    return records


def parse_revive_position_records(data: bytes) -> list[dict]:
    """The team revive points, then the sanctum revive points, in file order.

    A team point has `respawn_position_type` and `fierce_battle_key` None; a
    sanctum point the other way round. Raises ValueError on a bad magic or
    trailer, or when the points do not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE - _COUNT.size, end, FILE_NAME)
    records = _read_group(reader, _RESPAWN_POSITION_TYPE, "respawn_position_type", "fierce_battle_key")
    records += _read_group(reader, _FIERCE_BATTLE_KEY, "fierce_battle_key", "respawn_position_type")
    check_rows_end(data, reader.pos, f"{FILE_NAME} revive points")
    return records
