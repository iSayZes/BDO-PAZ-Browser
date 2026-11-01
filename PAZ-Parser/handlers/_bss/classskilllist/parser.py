"""`classskilllist.bss`: the Skill Guide skill list of each class.

    PABR | u32 class_count | class_count x row | string table
    | u32 string_table_start | u32 0

    row: u8 class_type | u64 skill_count | skill_count x u16 skill_no

The string table is present but empty. Full layout in
docs/file-formats/bss/classskilllist_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start

FILE_NAME = "classskilllist.bss"
_ROW_HEAD = struct.Struct("<BQ")
_SKILL_NO_SIZE = 2


@dataclass(frozen=True)
class ClassSkillList:
    class_type: int
    skill_nos: tuple[int, ...]


def parse_classskilllist_records(data: bytes) -> list[ClassSkillList]:
    """Every row in file order.

    Raises ValueError on a bad magic, a row that runs into the string table,
    or rows that do not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    pos = HEADER_SIZE
    rows: list[ClassSkillList] = []
    for _ in range(u32(data, 4)):
        if pos + _ROW_HEAD.size > end:
            raise ValueError(f"{FILE_NAME} row at 0x{pos:X} runs into the string table")
        class_type, skill_count = _ROW_HEAD.unpack_from(data, pos)
        first = pos + _ROW_HEAD.size
        pos = first + skill_count * _SKILL_NO_SIZE
        if pos > end:
            raise ValueError(f"{FILE_NAME} class type {class_type} holds {skill_count:,} skills, more than fit")
        rows.append(ClassSkillList(class_type, struct.unpack_from(f"<{skill_count}H", data, first)))
    check_rows_end(data, pos, f"{FILE_NAME} rows")
    return rows
