"""Gear Reform: `itemimprovement.dbss` and `itemimprovementsource.dbss`.

Both are a u32 count, then records back to back to the end of the file: a u32
key, a u64 count, that many u32 values and a fixed tail. The gear records hold
the result and input item IDs and a 13-byte tail with the reform group at
`+1`; the stone records hold five unknown values and a 10-byte tail of
category, group and the default display flag. Each `*offset.dbss` index points
4 bytes into a record, past the key, so the walk from the start needs no
index. Layouts in docs/file-formats/dbss/itemimprovement_dbss.md and
itemimprovementsource_dbss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Iterator
from typing import NamedTuple

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "itemimprovement.dbss"
OFFSET_FILE = "itemimprovementoffset.dbss"
SOURCE_FILE = "itemimprovementsource.dbss"
SOURCE_OFFSET_FILE = "itemimprovementsourceoffset.dbss"

KEY_SIZE = 4
_COUNT = struct.Struct("<I")
_LIST_HEAD = struct.Struct("<IQ")  # key, value count
_GEAR_TAIL = struct.Struct("<BB11s")  # unknown_tail_0, group, unknown_tail_2
_SOURCE_TAIL = struct.Struct("<IIH")  # category, group, is_default_display
# A gear record of five IDs is the result, then the input four times.
_RESULT_AND_INPUTS = 5


class _KeyedList(NamedTuple):
    start: int
    key: int
    values: tuple[int, ...]
    tail: tuple


def _keyed_lists(data: bytes, file_name: str, tail: struct.Struct) -> Iterator[_KeyedList]:
    """Every record of a keyed-list file, in file order.

    Raises ValueError when a record runs past the file or the records do not
    end where the file does.
    """
    if len(data) < _COUNT.size:
        raise ValueError(f"{file_name} is too short to hold its record count")

    count = u32(data, 0)
    pos = _COUNT.size
    for _ in range(count):
        reader = RecordReader(data, pos, len(data), f"{file_name} record at 0x{pos:X}")
        key, value_count = reader.unpack(_LIST_HEAD)
        values = reader.unpack(struct.Struct(f"<{value_count}I"))
        yield _KeyedList(pos, key, values, reader.unpack(tail))
        pos = reader.pos
    if pos != len(data):
        raise ValueError(f"{file_name} has {len(data) - pos:,} bytes after its {count:,} records")


def parse_itemimprovement_records(data: bytes) -> list[dict]:
    """Every gear reform record, in file order.

    A five-ID record names its result and input; a one-ID record names only
    the input gear. Raises ValueError on any other count, or four input
    slots that differ.
    """
    return [_gear_record(record) for record in _keyed_lists(data, FILE_NAME, _GEAR_TAIL)]


def _gear_record(record: _KeyedList) -> dict:
    unknown_tail_0, group, unknown_tail_2 = record.tail
    values = record.values
    if len(values) == _RESULT_AND_INPUTS:
        result_id, *inputs = values
        if len(set(inputs)) != 1:
            raise ValueError(f"{FILE_NAME} key {record.key} has differing inputs {inputs}")
    elif len(values) == 1:
        result_id, inputs = None, list(values)
    else:
        raise ValueError(f"{FILE_NAME} key {record.key} holds {len(values)} items, not 5 or 1")

    return {
        "key": record.key,
        "result_id": result_id,
        "input_id": inputs[0],
        "group": group,
        "offset": record.start,
        "unknown_tail_0": unknown_tail_0,
        "unknown_tail_2": unknown_tail_2.hex(),
    }


def parse_itemimprovementsource_records(data: bytes) -> list[dict]:
    """Every reform stone record, in file order."""
    return [_source_record(record) for record in _keyed_lists(data, SOURCE_FILE, _SOURCE_TAIL)]


def _source_record(record: _KeyedList) -> dict:
    category, group, is_default_display = record.tail
    return {
        "item_id": record.key,
        "category": category,
        "group": group,
        "is_default_display": bool(is_default_display),
        "offset": record.start,
        "results": list(record.values),
    }
