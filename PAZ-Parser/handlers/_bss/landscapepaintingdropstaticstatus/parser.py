"""`landscapepaintingdropstaticstatus.bss`: one row per landscape painting of the landscape painting window.

    PABR | u32 row_count | row_count x row | string table
    | u32 table_start | u32 0
    row: u8 landscape_painting_type | u32 unknown_01 | u32 name_index
    | u32 unknown_09 | unknown_09 x u32 unknown_0d | u32 drop_item_key

`name_index` points into the string table (the Korean name). Layout 2 in
docs/file-formats/bss/landscapepaintingdropstaticstatus_bss.md; client 3251
has no `drop_item_key` (Layout 1), which this parser does not read.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_u32s
from _common.pabr_strings import (
    HEADER_SIZE,
    check_rows_end,
    checked_string_table_start,
    read_string_table,
    string_at,
)
from _common.record_reader import RecordReader


FILE_NAME = "landscapepaintingdropstaticstatus.bss"
KEY_FIELD = "landscape_painting_type"

_U32 = struct.Struct("<I")
_HEAD = struct.Struct("<BII")
_HEAD_FIELDS = (KEY_FIELD, "unknown_01", "name_index")


def _read_row(reader: RecordReader, strings: list[str]) -> dict:
    head = dict(zip(_HEAD_FIELDS, reader.unpack(_HEAD), strict=True))
    unknown_list = read_counted_u32s(reader, f"{FILE_NAME} type {head[KEY_FIELD]} list")
    (drop_item_key,) = reader.unpack(_U32)
    return {
        **head,
        "name_kr": string_at(strings, head["name_index"]),
        "unknown_09": len(unknown_list),
        "unknown_0d": unknown_list,
        "drop_item_key": drop_item_key,
    }


def parse_landscapepaintingdrop_records(data: bytes) -> list[dict]:
    """Every row in file order, with its Korean name read from the string table.

    Raises ValueError on a bad magic or trailer, when a list runs past the
    string table, or when the rows do not end where it starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE - _U32.size, end, FILE_NAME)
    (row_count,) = reader.unpack(_U32)
    records = [_read_row(reader, strings) for _ in range(row_count)]
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return records
