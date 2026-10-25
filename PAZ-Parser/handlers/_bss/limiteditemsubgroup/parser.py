"""`limiteditemsubgroup.bss`: the purchase limits of the shop items in an item subgroup.

    PABR | u32 row_count | row_count x row | string table
    | u32 table_start | u32 0
    row: u32 entry_count | entry_count x entry (16 bytes)
    entry: u16 subgroup_key | u32 item_key | u8 purchase_subject
    | u32 purchase_count_limit | u8 reset_type | u32 unknown_0c

Every entry of one row holds the same `subgroup_key`. Layout 2 in
docs/file-formats/bss/limiteditemsubgroup_bss.md; clients 1348 and 1485 have
no `unknown_0c` (Layout 1), which this parser does not read.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_structs
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "limiteditemsubgroup.bss"
KEY_FIELD = "subgroup_key"

_U32 = struct.Struct("<I")
_ENTRY = struct.Struct("<HIBIBI")
_ENTRY_FIELDS = (
    KEY_FIELD,
    "item_key",
    "purchase_subject",
    "purchase_count_limit",
    "reset_type",
    "unknown_0c",
)


def parse_limiteditemsubgroup_records(data: bytes) -> list[dict]:
    """One record per entry, in file order.

    Raises ValueError on a bad magic or trailer, when a row runs past the
    string table, or when the rows do not end where it starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE - _U32.size, end, FILE_NAME)
    (row_count,) = reader.unpack(_U32)
    records = [
        entry
        for row in range(row_count)
        for entry in read_counted_structs(reader, _ENTRY, _ENTRY_FIELDS, f"{FILE_NAME} row {row}")
    ]
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return records
