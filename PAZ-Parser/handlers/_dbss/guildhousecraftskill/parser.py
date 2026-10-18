"""`guildhousecraftskill.dbss`: the guild skills each guild house use grants.

A u32 row count, then 20-byte rows: the i32 `houseinforeceipe.dbss` key, the
same key again, an unknown u16 and five u16 skill numbers (`0` in an unused
slot). `guildhousecraftskilloffset.dbss` points 4 bytes into a row, at the
second key, so the walk from the start needs no index. Layout 1 in
docs/file-formats/guildhousecraftskill_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "guildhousecraftskill.dbss"
OFFSET_FILE = "guildhousecraftskilloffset.dbss"

SKILL_SLOT_COUNT = 5
_COUNT_SIZE = 4
# receipe_key, receipe_key_dup, unknown_08, skill_nos[5]
_ROW = struct.Struct(f"<iiH{SKILL_SLOT_COUNT}H")
ROW_SIZE = _ROW.size


def _parse_row(data: bytes, offset: int) -> dict:
    receipe_key, receipe_key_dup, unknown_08, *skill_nos = _ROW.unpack_from(data, offset)
    return {
        "receipe_key": receipe_key,
        "receipe_key_dup": receipe_key_dup,
        "unknown_08": unknown_08,
        "skill_nos": skill_nos,
    }


def parse_guildhousecraftskill_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not the row count followed by exactly
    that many rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    expected = _COUNT_SIZE + count * ROW_SIZE
    if expected != len(data):
        raise ValueError(f"{count:,} rows of {ROW_SIZE} bytes need {expected:,} bytes, the file is {len(data):,}")
    return [_parse_row(data, _COUNT_SIZE + index * ROW_SIZE) for index in range(count)]
