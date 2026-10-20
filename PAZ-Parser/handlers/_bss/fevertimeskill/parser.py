"""`fevertimeskill.bss`: the Agris Fever drop skills and their drop bonus.

    PABR | u32 count | u16 unknown_08 | count x 10-byte row | string table
    | u32 string_table_start | u32 0

    row: u16 index | u16 skill_level | u16 skill_no | u32 description

`skill_level` and `skill_no` are one gc::SkillKey. The string table is empty.
Layout in docs/file-formats/fevertimeskill_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_pabr, check_rows_end
from _common.skill import skill_key


FILE_NAME = "fevertimeskill.bss"

# The u16 `unknown_08` sits between the PABR count and the first row.
_ROWS_START = HEADER_SIZE + 2
_ROW = struct.Struct("<HHHI")


def parse_fevertimeskill_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    check_pabr(data, FILE_NAME)
    rows_end = _ROWS_START + u32(data, 4) * _ROW.size
    check_rows_end(data, rows_end, f"{FILE_NAME} rows")

    records: list[dict] = []
    for offset in range(_ROWS_START, rows_end, _ROW.size):
        index, skill_level, skill_no, description = _ROW.unpack_from(data, offset)
        records.append({
            "index": index,
            "skill_level": skill_level,
            "skill_no": skill_no,
            "skill_key": skill_key(skill_no, skill_level),
            "description": description,
        })
    return records
