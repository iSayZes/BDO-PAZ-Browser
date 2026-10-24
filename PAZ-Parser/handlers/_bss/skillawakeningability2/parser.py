"""`skillawakeningability2.bss`: the Skill Add-on options each skill offers.

    PABR | u32 row_count | row_count x Row | string table | u32 table_start | u32 0
    Row: u16 skill_no | u16 skill_no_dup | u64 ability_count
         | ability_count x u32 ability_indexes

`ability_indexes` are `skillawakeningability.dbss` ability indexes, in the
order the Skill Add-on window lists them. Layout 1 in
docs/file-formats/skillawakeningability2_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, U32_SIZE, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "skillawakeningability2.bss"
KEY_FIELD = "skill_no"

_HEAD = struct.Struct("<HHQ")


def _read_row(reader: RecordReader) -> dict:
    skill_no, skill_no_dup, ability_count = reader.unpack(_HEAD)
    if ability_count * U32_SIZE > reader.remaining():
        raise ValueError(f"{FILE_NAME} skill {skill_no} declares {ability_count:,} ability indexes past the rows")
    ability_indexes = list(reader.unpack(struct.Struct(f"<{ability_count}I")))
    return {
        KEY_FIELD: skill_no,
        "skill_no_dup": skill_no_dup,
        "ability_count": ability_count,
        "ability_indexes": ability_indexes,
    }


def parse_skillawakeningability2_records(data: bytes) -> list[dict]:
    """Every skill row in file order.

    Raises ValueError on a bad PABR magic or trailer, or when the rows do not
    end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE, end, FILE_NAME)
    records = [_read_row(reader) for _ in range(u32(data, HEADER_SIZE - U32_SIZE))]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} rows end at 0x{reader.pos:X}, the string table starts at 0x{end:X}")
    return records
