"""`skillfusion.dbss`: the Skill Enhancement choices, a main skill and a sub skill per enhanced skill.

    u32 count | count x (u32 skill_fusion_key | u32 skill_fusion_key_dup
                         | u32 main_skill_key | u32 sub_skill_key
                         | u32 slot_no | u32 order_no)

The three keys are skill keys (`skill_no << 16 | level`, level 1 on every
row). `skillfusionoffset.dbss` (u32 count, then u32 skill key, offset and
size per row) points 4 bytes into a row, at `skill_fusion_key_dup`. Layout
1 in docs/file-formats/skillfusion_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows


FILE_NAME = "skillfusion.dbss"
OFFSET_FILE = "skillfusionoffset.dbss"
KEY_FIELD = "skill_fusion_key"

_ROW = struct.Struct("<6I")
_FIELDS = (KEY_FIELD, "skill_fusion_key_dup", "main_skill_key", "sub_skill_key", "slot_no", "order_no")


def parse_skillfusion_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, _ROW, _FIELDS, FILE_NAME)


def parse_skillfusionoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_u32_offset_rows(data)
