"""`skillclasstypelist.bss`: one row per non-guild skill.

    PABR | u32 skill_count | skill_count x (u32 skill_key, u64 unknown_04)
    | string table | u32 table_start | u32 0

The keys are the level 1 keys of `publicskill.bss` and `privateskill.bss`
together; `unknown_04` is the `skillsimply.dbss` every-class mask on every
row. Layout 2 in docs/file-formats/bss/skillclasstypelist_bss.md; the 36-byte
rows of Layout 1 (clients before 1267) are not read.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "skillclasstypelist.bss"

_ROW = struct.Struct("<IQ")
_ROW_FIELDS = ("skill_key", "unknown_04")


def parse_skillclasstypelist_rows(data: bytes) -> list[dict]:
    """Every row in file order, as `skill_key` and `unknown_04`.

    Raises ValueError on a bad PABR magic or rows that do not end where the
    string table starts.
    """
    return [
        dict(zip(_ROW_FIELDS, _ROW.unpack_from(data, pos), strict=True))
        for pos in fixed_row_offsets(data, _ROW.size, FILE_NAME)
    ]
