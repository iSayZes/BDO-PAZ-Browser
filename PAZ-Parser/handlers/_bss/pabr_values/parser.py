"""Reads the small PABR option tables of `tables.py`.

    PABR | values (+0x04 up to table_start) | u32 string_count | strings
    | u32 table_start | u32 0

The values end where the string table starts; a file whose values do not
fill that space exactly raises ValueError, since every field would then be
read from the wrong place.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import TRAILER_SIZE, U32_SIZE, check_pabr, check_rows_end, string_table_start
from .tables import RowCount, ValueField, ValueTable


VALUES_START = 0x04


def _values_end(data: bytes, file_name: str) -> int:
    """Where the values stop: the trailer's `table_start`, checked against the file."""
    check_pabr(data, file_name)
    end = string_table_start(data)
    if not VALUES_START <= end <= len(data) - TRAILER_SIZE - U32_SIZE:
        raise ValueError(f"{file_name} string table offset 0x{end:X} is outside the file")
    return end


def _rows(data: bytes, table: ValueTable, row_size: int, end: int) -> tuple[int, int]:
    """The first row's offset and the row count of `table`."""
    if table.rows is RowCount.COUNTED:
        return VALUES_START + U32_SIZE, u32(data, VALUES_START)
    if table.rows is RowCount.TO_TABLE_START:
        span = end - VALUES_START
        if span % row_size:
            raise ValueError(
                f"{table.file_name} string table starts at 0x{end:X}, "
                f"not after whole {row_size}-byte rows from 0x{VALUES_START:X}"
            )
        return VALUES_START, span // row_size
    return VALUES_START, 1


def _value(raw: object) -> object:
    """A byte run as `01 0a` hex text; numbers as read."""
    return raw.hex(" ") if isinstance(raw, bytes) else raw


def _record(fields: tuple[ValueField, ...], values: tuple[object, ...]) -> dict:
    return {field.name: _value(raw) for field, raw in zip(fields, values, strict=True)}


def parse_value_table(data: bytes, table: ValueTable) -> list[dict]:
    """One record per row of `table`, keyed by the doc's field names.

    Raises ValueError on a bad magic or trailer, or when the rows do not end
    at the string table.
    """
    end = _values_end(data, table.file_name)
    row = struct.Struct("<" + "".join(field.fmt for field in table.fields))
    start, count = _rows(data, table, row.size, end)
    check_rows_end(data, start + count * row.size, f"{table.file_name} values")
    return [_record(table.fields, row.unpack_from(data, start + index * row.size)) for index in range(count)]


def value_bytes(data: bytes, file_name: str) -> str:
    """Every byte between the magic and the string table, as hex text."""
    return data[VALUES_START : _values_end(data, file_name)].hex(" ")
