"""`sequencedatatable.bss`: where and when each cutscene starts, and what it runs.

    PABR | u32 row_count | row_count x 27-byte row | String Table
    | u32 string_table_start | u32 0
    row: u16 region_key | u32 file_name_hash | u32 cutscene_file_name
         | u32 start_condition | u32 start_execute | u32 end_execute
         | u32 unknown_16 | u8 unknown_1a

The four text fields are indexes into the string table
(`_bss/sequence_scripts/reader.py`). Layout 2 (the live client) in
docs/file-formats/bss/sequencedatatable_bss.md.
"""

from __future__ import annotations

import struct

from _bss.sequence_scripts.reader import SCRIPT_FIELDS, check_rows_end, open_table, read_string_refs


FILE_NAME = "sequencedatatable.bss"

_HEAD = struct.Struct("<HI")
_TAIL = struct.Struct("<IB")
_TEXT_FIELDS = ("cutscene_file_name", *SCRIPT_FIELDS)


def parse_sequencedatatable_records(data: bytes) -> list[dict]:
    """Every row in file order, its text fields resolved.

    Raises ValueError on a bad magic, a string index past the table, or rows
    that do not end where the string table starts.
    """
    table = open_table(data, FILE_NAME)
    records: list[dict] = []
    for index in range(table.row_count):
        region_key, file_name_hash = table.reader.unpack(_HEAD)
        texts = read_string_refs(table, _TEXT_FIELDS, f"{FILE_NAME} row {index}")
        unknown_16, unknown_1a = table.reader.unpack(_TAIL)
        records.append({
            "region_key": region_key,
            "file_name_hash": file_name_hash,
            **texts,
            "unknown_16": unknown_16,
            "unknown_1a": unknown_1a,
        })
    check_rows_end(table, FILE_NAME)
    return records
