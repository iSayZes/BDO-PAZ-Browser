"""Tables that are a u32 row count followed by the rows.

Most `.dbss` tables with an `*offset.dbss` index have this shape; the index
only says where each row sits, so the rows can be read from the count.
`parse_counted_rows()` reads rows of one fixed size, `read_counted_records()`
rows with lists in them. `read_counted_structs()` and `read_counted_u32s()`
read such a list inside a row or after the rows.
"""

from __future__ import annotations

import struct
from collections.abc import Callable, Sequence

from _common.binary import u32
from _common.record_reader import RecordReader

COUNT_SIZE = 4
_U32 = struct.Struct("<I")


def counted_row_values(data: bytes, row: struct.Struct, file_name: str) -> list[tuple]:
    """The values `row` unpacks from every row, in file order.

    Raises ValueError when the rows do not end at the last byte of the file.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{file_name} is too short to hold its row count")

    count = u32(data, 0)
    expected = COUNT_SIZE + count * row.size
    if len(data) != expected:
        raise ValueError(f"{file_name} is {len(data):,} bytes, {count:,} rows of {row.size} need {expected:,}")
    return list(row.iter_unpack(data[COUNT_SIZE:]))


def parse_counted_rows(data: bytes, row: struct.Struct, fields: Sequence[str], file_name: str) -> list[dict]:
    """Every row in file order, as `fields` -> the values `row` unpacks.

    Raises ValueError like `counted_row_values()`.
    """
    return [dict(zip(fields, values, strict=True)) for values in counted_row_values(data, row, file_name)]


def read_counted_records(data: bytes, read_row: Callable[[RecordReader], dict], file_name: str) -> list[dict]:
    """Every row in file order, each read by `read_row` from one reader over the whole file.

    Raises ValueError when a row runs past the file or the rows end before it.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{file_name} is too short to hold its row count")
    reader = RecordReader(data, COUNT_SIZE, len(data), file_name)
    records = [read_row(reader) for _ in range(u32(data, 0))]
    if not reader.at_end():
        raise ValueError(f"{file_name} rows end at 0x{reader.pos:X}, the file at 0x{len(data):X}")
    return records


def read_counted_structs(reader: RecordReader, item: struct.Struct, fields: Sequence[str], what: str) -> list[dict]:
    """A u32 count, then that many `item` structs, each as `fields` -> the values it unpacks.

    Raises ValueError naming `what` when the count runs past the reader's end.
    """
    (count,) = reader.unpack(_U32)
    if count * item.size > reader.remaining():
        raise ValueError(f"{what} count {count:,} at 0x{reader.pos - _U32.size:X} runs past the end")
    return [dict(zip(fields, reader.unpack(item), strict=True)) for _ in range(count)]


def read_counted_u32s(reader: RecordReader, what: str) -> list[int]:
    """A u32 count, then that many u32 values. Raises ValueError like `read_counted_structs()`."""
    (count,) = reader.unpack(_U32)
    if count * _U32.size > reader.remaining():
        raise ValueError(f"{what} count {count:,} at 0x{reader.pos - _U32.size:X} runs past the end")
    return list(reader.unpack(struct.Struct(f"<{count}I")))
