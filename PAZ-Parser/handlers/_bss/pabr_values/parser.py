"""Reads the small option tables of `tables.py`.

A `Framing.PABR` file:

    PABR | values (+0x04 up to table_start) | u32 string_count | strings
    | u32 table_start | u32 0

A `Framing.BARE` file is the values alone, from +0x00 to the end of the file.

The values end where the string table starts or the file ends; values that
do not fill that space exactly raise ValueError, since every field would
then be read from the wrong place. A string-table index field (`TextRef`)
also stores the string it points to. Head fields, read once before the row
count, and tail fields, read once after the last row, go on every record. `parse_value_rows` also gives each row's bytes
as hex text, for the files with no named field.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_strings import TRAILER_SIZE, U32_SIZE, check_pabr, read_string_table, string_at, string_table_start
from .layout import Framing, RowCount, ValueField, ValueTable


PABR_VALUES_START = 0x04
_COUNT_FORMAT = "I"


@dataclass(frozen=True)
class _Row:
    """One row's record and where its bytes start and stop."""

    record: dict
    start: int
    stop: int


def _end_name(table: ValueTable) -> str:
    return "the string table starts" if table.framing is Framing.PABR else "the file ends"


def _values_span(data: bytes, table: ValueTable) -> tuple[int, int]:
    """Where the values start and stop; for PABR, checked against the magic and trailer."""
    if table.framing is Framing.BARE:
        return 0, len(data)
    check_pabr(data, table.file_name)
    end = string_table_start(data)
    if not PABR_VALUES_START <= end <= len(data) - TRAILER_SIZE - U32_SIZE:
        raise ValueError(f"{table.file_name} string table offset 0x{end:X} is outside the file")
    return PABR_VALUES_START, end


def _unpack(data: bytes, fmt: str, offset: int, end: int, table: ValueTable) -> tuple[tuple, int]:
    """The values of `fmt` at `offset` and the offset after them, which must not pass `end`."""
    stop = offset + struct.calcsize("<" + fmt)
    if stop > end:
        raise ValueError(f"{table.file_name} values run past 0x{end:X}, where {_end_name(table)}")
    return struct.unpack_from("<" + fmt, data, offset), stop


def _value(raw: object) -> object:
    """A byte run as `01 0a` hex text; numbers as read."""
    return raw.hex(" ") if isinstance(raw, bytes) else raw


def _entries(raws: tuple, fmt: str) -> list[object]:
    """The values of a counted list; an entry of several values (`B3I`) as a list."""
    per_entry = len(struct.unpack("<" + fmt, bytes(struct.calcsize("<" + fmt))))
    if per_entry == 1:
        return [_value(raw) for raw in raws]
    return [[_value(raw) for raw in raws[i : i + per_entry]] for i in range(0, len(raws), per_entry)]


def _field_value(data: bytes, field: ValueField, offset: int, end: int, table: ValueTable) -> tuple[object, int]:
    """One field's value (a list for a counted list) and the offset after it."""
    if not field.is_counted_list:
        (raw,), stop = _unpack(data, field.fmt, offset, end, table)
        return _value(raw), stop
    (count,), start = _unpack(data, field.count_fmt, offset, end, table)
    if start + count * struct.calcsize("<" + field.fmt) > end:
        raise ValueError(f"{table.file_name} {field.name} count {count:,} runs past 0x{end:X}, where {_end_name(table)}")
    raws, stop = _unpack(data, field.fmt * count, start, end, table)
    return _entries(raws, field.fmt), stop


def _read_values(
    data: bytes,
    table: ValueTable,
    fields: tuple[ValueField, ...],
    offset: int,
    end: int,
    strings: list[str],
) -> _Row:
    """The values of `fields` from `offset`, with the string of each string-table index."""
    values: dict[str, object] = {}
    stop = offset
    for field in fields:
        value, stop = _field_value(data, field, stop, end, table)
        values[field.name] = value
        if field.text is not None and isinstance(value, int):
            values[field.text.field] = string_at(strings, value)
    return _Row(values, offset, stop)


def _first_row_and_count(data: bytes, table: ValueTable, start: int, end: int) -> tuple[int, int]:
    """The first row's offset and the row count of `table`."""
    if table.rows is RowCount.COUNTED:
        (count,), first = _unpack(data, _COUNT_FORMAT, start, end, table)
        return first, count
    if table.rows is RowCount.TO_TABLE_START:
        row_size = struct.calcsize("<" + "".join(field.fmt for field in table.fields))
        if (end - start) % row_size:
            raise ValueError(
                f"{table.file_name} values from 0x{start:X} to 0x{end:X}, where {_end_name(table)}, "
                f"are not whole {row_size}-byte rows"
            )
        return start, (end - start) // row_size
    return start, 1


def _read_rows(data: bytes, table: ValueTable) -> list[_Row]:
    """Every row of `table`, checked to end exactly where the values stop."""
    start, end = _values_span(data, table)
    strings = read_string_table(data) if table.has_text else []
    head = _read_values(data, table, table.head, start, end, strings)
    offset, count = _first_row_and_count(data, table, head.stop, end)
    rows: list[_Row] = []
    for _ in range(count):
        row = _read_values(data, table, table.fields, offset, end, strings)
        rows.append(row)
        offset = row.stop
    tail = _read_values(data, table, table.tail, offset, end, strings)
    offset = tail.stop
    rows = [_Row({**row.record, **head.record, **tail.record}, row.start, row.stop) for row in rows]
    if offset != end:
        raise ValueError(f"{table.file_name} values end at 0x{offset:X}, but {_end_name(table)} at 0x{end:X}")
    return rows


def parse_value_table(data: bytes, table: ValueTable) -> list[dict]:
    """One record per row of `table`, keyed by the doc's field names.

    Raises ValueError on a bad PABR magic or trailer, or when the rows do not
    end where the string table starts (PABR) or the file ends (BARE).
    """
    return [row.record for row in _read_rows(data, table)]


def parse_value_rows(data: bytes, table: ValueTable) -> list[tuple[dict, str]]:
    """Each row's record with its bytes as hex text, from one read, in row order.

    A `RowCount.ONE` row holds every value byte. Raises as `parse_value_table`.
    """
    return [(row.record, data[row.start : row.stop].hex(" ")) for row in _read_rows(data, table)]
