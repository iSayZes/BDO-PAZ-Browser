"""`lifeactionexperience.dbss`: life skill EXP per item.

A u32 row count, then 26-byte rows: the u32 item key, the key again, two u8
life skill types and two i64 EXP amounts. `lifeactionexperienceoffset.dbss`
points 4 bytes into a row, at the second key, so the walk from the start
needs no index. Layout 1 in docs/file-formats/lifeactionexperience_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "lifeactionexperience.dbss"
OFFSET_FILE = "lifeactionexperienceoffset.dbss"
SLOT_COUNT = 2
# `CppEnums.LifeExperienceType.Type_Count`, the type of an empty slot.
EMPTY_LIFE_ACTION_TYPE = 15

_COUNT_SIZE = 4
# item_key, item_key_dup, life_action_types[2], experiences[2]
_ROW = struct.Struct(f"<II{SLOT_COUNT}B{SLOT_COUNT}q")


def parse_lifeactionexperience_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not the row count followed by exactly
    that many rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    expected_size = _COUNT_SIZE + count * _ROW.size
    if len(data) != expected_size:
        raise ValueError(f"{FILE_NAME} is {len(data):,} bytes, {count:,} rows need {expected_size:,}")

    records = []
    for item_key, item_key_dup, *slots in _ROW.iter_unpack(data[_COUNT_SIZE:]):
        records.append({
            "item_key": item_key,
            "item_key_dup": item_key_dup,
            "life_action_types": slots[:SLOT_COUNT],
            "experiences": slots[SLOT_COUNT:],
        })
    return records
