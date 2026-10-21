"""`exptoskillexprate.dbss`: an EXP to skill EXP rate per character level, 0 in the client.

    u32 count | count x (u32 level | u32 level_dup | u32 exp_to_skill_exp_rate)

`level_dup` and `exp_to_skill_exp_rate` are the 2016
`gc::ExpToSkillExpRateStaticStatus`; the rate is a server-only column, so the
client file holds `0`. `exptoskillexprateoffset.dbss` (u32 count, then u32
level, offset and size per row) points 4 bytes into a row, at `level_dup`.
Layout 1 in docs/file-formats/exptoskillexprate_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows


FILE_NAME = "exptoskillexprate.dbss"
OFFSET_FILE = "exptoskillexprateoffset.dbss"
KEY_FIELD = "level"

_ROW = struct.Struct("<III")
_FIELDS = (KEY_FIELD, "level_dup", "exp_to_skill_exp_rate")


def parse_exptoskillexprate_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, _ROW, _FIELDS, FILE_NAME)


def parse_exptoskillexprateoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_u32_offset_rows(data)
