"""`trainingvehicle.dbss`: the grade of each training dummy character.

    u32 count | count x (u16 character_key | u16 character_key_dup | i32 grade)

`trainingvehicleoffset.dbss` points at each row's `character_key_dup`, so
the walk from the start needs no index. Layout 1 in
docs/file-formats/dbss/trainingvehicle_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "trainingvehicle.dbss"
OFFSET_FILE = "trainingvehicleoffset.dbss"

_COUNT_SIZE = 4
# character_key, character_key_dup, grade
_ROW = struct.Struct("<HHi")


def parse_trainingvehicle_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not the row count followed by exactly
    that many rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    end = _COUNT_SIZE + count * _ROW.size
    if end != len(data):
        raise ValueError(f"{count:,} rows of {_ROW.size} bytes end at 0x{end:X}, the file is {len(data):,} bytes")

    return [
        {"character_key": character_key, "character_key_dup": character_key_dup, "grade": grade}
        for character_key, character_key_dup, grade in _ROW.iter_unpack(data[_COUNT_SIZE:end])
    ]
