"""`instancedungeoninfo.dbss`: the entry point of each instance dungeon.

    u32 count | count x (u32 key | u16 field_no | f32 enter_x, enter_y, enter_z | f32 enter_rotation)

`field_no` is a `Field_Table` key and `enter_rotation` is in radians.
`instancedungeoninfooffset.dbss` holds bare u32-keyed index rows (key,
absolute offset, size 22). Layout in docs/file-formats/dbss/instancedungeoninfo_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "instancedungeoninfo.dbss"
OFFSET_FILE = "instancedungeoninfooffset.dbss"

COUNT_SIZE = 4
_ROW = struct.Struct("<IH4f")
ROW_SIZE = _ROW.size
_FIELDS = ("key", "field_no", "enter_x", "enter_y", "enter_z", "enter_rotation")


def parse_instancedungeoninfo_records(data: bytes) -> list[dict]:
    """Every record in file order.

    Raises ValueError when the file does not hold exactly its count of 22-byte rows.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its record count")
    count = u32(data, 0)
    expected = COUNT_SIZE + count * ROW_SIZE
    if len(data) != expected:
        raise ValueError(f"{FILE_NAME} declares {count} rows ({expected:,} bytes) but holds {len(data):,} bytes")
    return [
        dict(zip(_FIELDS, _ROW.unpack_from(data, COUNT_SIZE + index * ROW_SIZE)))
        for index in range(count)
    ]
