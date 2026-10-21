"""`exceptionskillcooltimewidget.dbss`: skills the skill cooldown window lists under another skill.

A `PABR` table of 20-byte rows with an empty string table:

    Row: u32 skill_key_from | u64 class_mask | u32 skill_key_to | u32 skill_learn_check_key

Each key is `skill_no << 16 | 1`. `exceptionskillcooltimewidgetoffset.dbss`
is a bare index (u32 count, then u32 key, u32 offset, u32 size per row) that
points at each row's start, so reading the rows in order needs no index.
Layout in docs/file-formats/exceptionskillcooltimewidget_dbss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "exceptionskillcooltimewidget.dbss"
OFFSET_FILE = "exceptionskillcooltimewidgetoffset.dbss"

ROW = struct.Struct("<IQII")


def parse_exceptionskillcooltimewidget_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError on a missing magic or rows that do not end where the
    string table starts.
    """
    return [_record(*ROW.unpack_from(data, start)) for start in fixed_row_offsets(data, ROW.size, FILE_NAME)]


def _record(skill_key_from: int, class_mask: int, skill_key_to: int, skill_learn_check_key: int) -> dict:
    return {
        "skill_key_from": skill_key_from,
        "class_mask": class_mask,
        "skill_key_to": skill_key_to,
        "skill_learn_check_key": skill_learn_check_key,
    }
