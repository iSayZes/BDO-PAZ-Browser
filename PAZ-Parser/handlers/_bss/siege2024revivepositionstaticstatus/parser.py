"""`siege2024revivepositionstaticstatus.bss`: where Node War players revive, per territory.

    PABR | u32 row_count | row_count x Row | string table
    | u32 table_start | u32 0
    Row: u32 position_count | u16 territory_key | position_count x Position
    Position (16 bytes): f32 x | f32 y | f32 z | f32 unknown_0c

The count comes before the territory key. Full layout in
docs/file-formats/siege2024revivepositionstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import whole_float
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, check_rows_end
from _common.record_reader import RecordReader


FILE_NAME = "siege2024revivepositionstaticstatus.bss"

_ROW_COUNT = struct.Struct("<I")
_ROW_HEAD = struct.Struct("<IH")
_POSITION = struct.Struct("<4f")


def _read_row(reader: RecordReader) -> list[dict]:
    """One record per position of one territory."""
    position_count, territory_key = reader.unpack(_ROW_HEAD)
    if position_count * _POSITION.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} position count {position_count:,} runs past the string table")
    records: list[dict] = []
    for _ in range(position_count):
        x, y, z, unknown_0c = reader.unpack(_POSITION)
        records.append(
            {
                "territory_key": territory_key,
                "x": whole_float(x),
                "y": whole_float(y),
                "z": whole_float(z),
                "unknown_0c": whole_float(unknown_0c),
            }
        )
    return records


def parse_revive_position_records(data: bytes) -> list[dict]:
    """One record per revive position, in file order, with its territory key.

    Raises ValueError on a bad magic or trailer, or when the rows do not end
    where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE - _ROW_COUNT.size, end, FILE_NAME)
    (row_count,) = reader.unpack(_ROW_COUNT)
    records: list[dict] = []
    for _ in range(row_count):
        records += _read_row(reader)
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return records
