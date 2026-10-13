"""`alchemystonechange.dbss`: the Growth recipe of each item that grows a tier.

A u32 row count, then the rows back to back with no `PABR` magic and no
string table. A row is a fixed head (key, item, material and count), a
u64-prefixed UTF-16LE condition script and a 12-byte tail (result item and
two unknown u32). `alchemystonechangeoffset.dbss` points at each row's
`item_id`, 4 bytes past its key. Layout in
docs/file-formats/alchemystonechange_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "alchemystonechange.dbss"
OFFSET_FILE = "alchemystonechangeoffset.dbss"

_COUNT_SIZE = 4
_HEAD = struct.Struct("<IIIII")
_UNKNOWN_14_SIZE = 16
_TAIL = struct.Struct("<III")


def parse_alchemystonechange_records(data: bytes) -> list[dict]:
    """Every Growth row, in file order.

    Raises ValueError when a row runs past the end of the file or bytes are
    left after the last row.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    cursor = _COUNT_SIZE
    records: list[dict] = []
    for index in range(count):
        record, cursor = _read_row(data, cursor, f"{FILE_NAME} row {index}")
        records.append(record)

    if cursor != len(data):
        raise ValueError(f"{FILE_NAME}: {len(data) - cursor} bytes left after row {count - 1}")
    return records


def _read_row(data: bytes, start: int, label: str) -> tuple[dict, int]:
    """The row at `start` and where the next row starts."""
    reader = RecordReader(data, start, len(data), label)
    key, item_id, unknown_08, material_item_id, material_count = reader.unpack(_HEAD)
    unknown_14 = data[reader.pos : reader.pos + _UNKNOWN_14_SIZE]
    reader.skip(_UNKNOWN_14_SIZE)
    condition = reader.text(wide=True)
    result_item_id, unknown_tail_04, unknown_tail_08 = reader.unpack(_TAIL)
    record = {
        "key": key,
        "item_id": item_id,
        "unknown_08": unknown_08,
        "material_item_id": material_item_id,
        "material_count": material_count,
        "unknown_14": unknown_14.hex(),
        "condition": condition,
        "result_item_id": result_item_id,
        "unknown_tail_04": unknown_tail_04,
        "unknown_tail_08": unknown_tail_08,
    }
    return record, reader.pos
