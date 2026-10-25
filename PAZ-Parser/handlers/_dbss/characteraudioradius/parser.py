"""`characteraudioradius.dbss`: the sound radius of a few characters.

    u32 count | count x (u16 character_key | f32 sound_radius)

`characteraudioradiusoffset.dbss` points at each row's `character_key`, so
the walk from the start needs no index. Layout 1 in
docs/file-formats/dbss/characteraudioradius_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32, whole_float


FILE_NAME = "characteraudioradius.dbss"
OFFSET_FILE = "characteraudioradiusoffset.dbss"

_COUNT_SIZE = 4
# character_key, sound_radius
_ROW = struct.Struct("<Hf")


def parse_characteraudioradius_records(data: bytes) -> list[dict]:
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
        {"character_key": character_key, "sound_radius": whole_float(sound_radius)}
        for character_key, sound_radius in _ROW.iter_unpack(data[_COUNT_SIZE:end])
    ]
