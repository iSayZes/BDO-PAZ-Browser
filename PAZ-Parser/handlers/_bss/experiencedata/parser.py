"""`experiencedata.bss`: the first-experience triggers of the Black Spirit guide.

    PABR | u32 row_count | row_count x 17-byte row | String Table
    | u32 string_table_start | u32 0
    row: u32 once_condition | u32 constant_condition | u32 execute | u8 repeat
         | u32 delete_condition

The four scripts are indexes into the string table
(`_bss/sequence_scripts/reader.py`). Layout 1 in
docs/file-formats/bss/experiencedata_bss.md.
"""

from __future__ import annotations

import struct

from _bss.sequence_scripts.reader import check_rows_end, open_table, read_string_refs


FILE_NAME = "experiencedata.bss"
# The script fields of a row, in file order around `repeat`.
HEAD_SCRIPTS = ("once_condition", "constant_condition", "execute")
TAIL_SCRIPTS = ("delete_condition",)

_REPEAT = struct.Struct("<B")


def parse_experiencedata_records(data: bytes) -> list[dict]:
    """Every row in file order, its scripts resolved.

    Raises ValueError on a bad magic, a string index past the table, or rows
    that do not end where the string table starts.
    """
    table = open_table(data, FILE_NAME)
    records: list[dict] = []
    for index in range(table.row_count):
        label = f"{FILE_NAME} row {index}"
        head = read_string_refs(table, HEAD_SCRIPTS, label)
        (repeat,) = table.reader.unpack(_REPEAT)
        tail = read_string_refs(table, TAIL_SCRIPTS, label)
        records.append({"row": index, **head, "repeat": repeat, **tail})
    check_rows_end(table, FILE_NAME)
    return records
