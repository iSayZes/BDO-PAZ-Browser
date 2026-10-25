"""`publicskill.bss`: the level 1 key of every item and event skill.

    PABR | u32 unknown_04 | u32 skill_count | skill_count x u32 skill_key
    | string table | u32 table_start | u32 0

`unknown_04` is `0` on every checked client; with no rows behind it its row
size is unknown, so any other value is rejected. Layout 1 in
docs/file-formats/bss/publicskill_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_u32s
from _common.pabr_offset import PABR_MAGIC
from _common.pabr_strings import checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "publicskill.bss"
KEY_FIELD = "skill_key"

_U32 = struct.Struct("<I")


def parse_publicskill_keys(data: bytes) -> list[int]:
    """Every skill key in file order.

    Raises ValueError on a bad PABR magic or trailer, a non-zero
    `unknown_04`, or keys that do not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, len(PABR_MAGIC), end, FILE_NAME)
    (unknown_04,) = reader.unpack(_U32)
    if unknown_04:
        raise ValueError(f"{FILE_NAME} unknown_04 is {unknown_04:,}; only 0 is known, so the keys cannot be found")
    keys = read_counted_u32s(reader, f"{FILE_NAME} skill_count")
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} keys end at 0x{reader.pos:X}, the string table starts at 0x{end:X}")
    return keys
