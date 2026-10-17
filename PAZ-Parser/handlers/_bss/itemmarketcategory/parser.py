"""`itemmarketcategory.bss`: the Central Market category tree.

    PABR | u32 count | count x row | string table
    | u32 string_table_start | u32 0

    row: u8 key | category value main_category
         | u32 count, count x category value   sub_categories
         | u32 count, count x category value   filter1_values
         | u32 count, count x category value   filter2_values
         | u32 unknown_filter2_values_00
    category value: u8 category_no | u32 name_ref (string table index)

Layout in docs/file-formats/itemmarketcategory_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import (
    HEADER_SIZE,
    check_rows_end,
    checked_string_table_start,
    read_string_table,
    string_at,
)
from _common.record_reader import RecordReader


FILE_NAME = "itemmarketcategory.bss"
# The three counted lists of a row, in file order.
LIST_FIELDS = ("sub_categories", "filter1_values", "filter2_values")

_U8 = struct.Struct("<B")
_U32 = struct.Struct("<I")
# u8 category_no | u32 name_ref
_VALUE = struct.Struct("<BI")


def _value(reader: RecordReader, strings: list[str]) -> dict:
    category_no, name_ref = reader.unpack(_VALUE)
    return {"category_no": category_no, "name_kr": string_at(strings, name_ref)}


def _value_list(reader: RecordReader, strings: list[str]) -> list[dict]:
    (count,) = reader.unpack(_U32)
    return [_value(reader, strings) for _ in range(count)]


def _parse_row(reader: RecordReader, strings: list[str]) -> dict:
    (key,) = reader.unpack(_U8)
    record: dict = {"key": key, "main_category": _value(reader, strings)}
    for field in LIST_FIELDS:
        record[field] = _value_list(reader, strings)
    (record["unknown_filter2_values_00"],) = reader.unpack(_U32)
    return record


def parse_itemmarketcategory_records(data: bytes) -> list[dict]:
    """Every main category row in file order, its Korean names resolved.

    Raises ValueError on a bad magic, when a row runs into the string table,
    or when the rows end anywhere but where the string table starts: then
    the row layout has changed and every later field is suspect.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)

    records: list[dict] = []
    pos = HEADER_SIZE
    for index in range(u32(data, 4)):
        reader = RecordReader(data, pos, rows_end, f"{FILE_NAME} row {index}")
        records.append(_parse_row(reader, strings))
        pos = reader.pos
    check_rows_end(data, pos, f"{FILE_NAME} rows")
    return records
