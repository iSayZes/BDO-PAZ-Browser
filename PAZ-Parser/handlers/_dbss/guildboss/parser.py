"""`guildboss.dbss`: skill EXP and guild funds per guild boss character.

    u32 count | count x (u16 character_key | u8 unknown_02 | u16 character_key_dup
                         | i32 skill_point_exp | i64 guild_money)

`guildbossoffset.dbss` points at each row's `unknown_02`, so the walk from
the start needs no index. Layout 1 in docs/file-formats/guildboss_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "guildboss.dbss"
OFFSET_FILE = "guildbossoffset.dbss"

_COUNT_SIZE = 4
# character_key, unknown_02, character_key_dup, skill_point_exp, guild_money
_ROW = struct.Struct("<HBHiq")


def parse_guildboss_records(data: bytes) -> list[dict]:
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
            "character_key": character_key,
            "unknown_02": unknown_02,
            "character_key_dup": character_key_dup,
            "skill_point_exp": skill_point_exp,
            "guild_money": guild_money,
        }
        for character_key, unknown_02, character_key_dup, skill_point_exp, guild_money in _ROW.iter_unpack(
            data[_COUNT_SIZE:end]
        )
    ]
