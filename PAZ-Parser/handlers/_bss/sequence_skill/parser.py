"""`sequence_skill.bss` and `cutscene_skill.bss`: the skills each class gets
listed for a tutorial sequence or cutscene.

    PABR | u32 row_count | row_count x row | String Table (0 strings)
    | u32 string_table_start | u32 0
    row: u32 file_name_hash | u32 class_count | class_count x class
    class: u8 class_type | u64 skill_count | u16 skill_nos[skill_count]

A row stores only the hash of its file name (`_bss/sequence_scripts/reader.py`).
Layout 1 in docs/file-formats/bss/sequence_skill_bss.md.
"""

from __future__ import annotations

import struct

from _bss.sequence_scripts.reader import check_rows_end, open_table, read_class_entries
from _common.record_reader import RecordReader


SEQUENCE_FILE_NAME = "sequence_skill.bss"
CUTSCENE_FILE_NAME = "cutscene_skill.bss"

_HASH = struct.Struct("<I")
_CLASS_HEAD = struct.Struct("<BQ")
_SKILL_NO_SIZE = 2


def _read_class(reader: RecordReader) -> dict:
    class_type, skill_count = reader.unpack(_CLASS_HEAD)
    # Checked before the count sizes a struct: a misread u64 would not fit in memory.
    if skill_count * _SKILL_NO_SIZE > reader.remaining():
        raise ValueError(f"class {class_type} lists {skill_count:,} skills, past the rows")
    skill_nos = reader.unpack(struct.Struct(f"<{skill_count}H"))
    return {"class_type": class_type, "skill_count": skill_count, "skill_nos": list(skill_nos)}


def parse_sequence_skill_rows(data: bytes, file_name: str) -> list[dict]:
    """Every row in file order: its file name hash and its class entries.

    Raises ValueError on a bad magic, a skill list past the rows, or rows
    that do not end where the string table starts.
    """
    table = open_table(data, file_name)
    rows: list[dict] = []
    for _ in range(table.row_count):
        (file_name_hash,) = table.reader.unpack(_HASH)
        rows.append({"file_name_hash": file_name_hash, "classes": read_class_entries(table.reader, _read_class)})
    check_rows_end(table, file_name)
    return rows
