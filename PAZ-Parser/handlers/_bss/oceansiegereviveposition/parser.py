"""`oceansiegereviveposition.bss`: where Blue Battlefield (ocean siege) players revive, per territory.

    PABR | u32 row_count | row_count x Row | string table
    | u32 table_start | u32 0
    Row: u16 territory_key | u32 group_count | group_count x Group
    Group: u8 unknown_00 | u32 position_count | position_count x Position
    Position (17 bytes): f32 x | f32 y | f32 z | f32 unknown_0c | u8 unknown_10

Full layout in docs/file-formats/bss/oceansiegereviveposition_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import whole_float
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, check_rows_end
from _common.record_reader import RecordReader


FILE_NAME = "oceansiegereviveposition.bss"

_COUNT = struct.Struct("<I")
_TERRITORY_KEY = struct.Struct("<H")
_GROUP_KEY = struct.Struct("<B")
_POSITION = struct.Struct("<4fB")


def _read_positions(reader: RecordReader) -> list[dict]:
    (count,) = reader.unpack(_COUNT)
    if count * _POSITION.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} position count {count:,} runs past the string table")
    positions: list[dict] = []
    for _ in range(count):
        x, y, z, unknown_0c, unknown_10 = reader.unpack(_POSITION)
        positions.append(
            {
                "x": whole_float(x),
                "y": whole_float(y),
                "z": whole_float(z),
                "unknown_0c": whole_float(unknown_0c),
                "unknown_10": unknown_10,
            }
        )
    return positions


def _read_row(reader: RecordReader) -> list[dict]:
    """One record per position of one territory's groups."""
    (territory_key,) = reader.unpack(_TERRITORY_KEY)
    (group_count,) = reader.unpack(_COUNT)
    records: list[dict] = []
    for _ in range(group_count):
        (unknown_00,) = reader.unpack(_GROUP_KEY)
        records += [
            {"territory_key": territory_key, "unknown_00": unknown_00, **position}
            for position in _read_positions(reader)
        ]
    return records


def parse_revive_position_records(data: bytes) -> list[dict]:
    """One record per revive position, in file order, with its territory key and group key.

    Raises ValueError on a bad magic or trailer, or when the rows do not end
    where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE - _COUNT.size, end, FILE_NAME)
    (row_count,) = reader.unpack(_COUNT)
    records: list[dict] = []
    for _ in range(row_count):
        records += _read_row(reader)
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return records
