"""`petdetectposition.dbss`: the world positions behind the pet Location Find skill.

    u32 count | count x (u16 pet_detect_position_key | f32 pos_x | f32 pos_y | f32 pos_z
                         | u8 pet_detect_position_type)

The rows are the 2016 `gc::PetDetectPositionStaticStatus` packed with no
padding. `petdetectpositionoffset.dbss` points at each row's key, so the
walk from the start needs no index. Layout 1 in
docs/file-formats/petdetectposition_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "petdetectposition.dbss"
OFFSET_FILE = "petdetectpositionoffset.dbss"

_COUNT_SIZE = 4
# pet_detect_position_key, pos_x, pos_y, pos_z, pet_detect_position_type
_ROW = struct.Struct("<HfffB")


def parse_petdetectposition_records(data: bytes) -> list[dict]:
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
        {
            "pet_detect_position_key": key,
            "pos_x": pos_x,
            "pos_y": pos_y,
            "pos_z": pos_z,
            "pet_detect_position_type": position_type,
        }
        for key, pos_x, pos_y, pos_z, position_type in _ROW.iter_unpack(data[_COUNT_SIZE:end])
    ]
