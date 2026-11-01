"""`houseinforeceipe.dbss`: the house uses (receipes) a node house can be set to.

A u32 row count, then the rows back to back with no `PABR` magic and no
string table. A row is the receipe key, the `houseinfoneeditem.dbss` key, a
u64-prefixed UTF-16LE Korean name, the use type, icon type and one unknown
byte, five counted u32 lists of item exchange keys (house levels 1 to 5), an
unknown u32 and a counted u8 list. `houseinforeceipeoffset.dbss` points at
each row's key. Layout in docs/file-formats/dbss/houseinforeceipe_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "houseinforeceipe.dbss"
OFFSET_FILE = "houseinforeceipeoffset.dbss"
LEVEL_COUNT = 5

_COUNT_SIZE = 4
_HEAD = struct.Struct("<IH")
_TYPES = struct.Struct("<BBB")
_U32 = struct.Struct("<I")
_KEY_SIZE = 4


def parse_houseinforeceipe_records(data: bytes) -> list[dict]:
    """Every receipe row, in file order.

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
    receipe_key, need_item_key = reader.unpack(_HEAD)
    name_kr = reader.text(wide=True)
    house_use_type, icon_type, unknown_tail_02 = reader.unpack(_TYPES)
    level_exchanges = [_read_list(reader, _KEY_SIZE, "I") for _ in range(LEVEL_COUNT)]
    (unknown_after_level_exchanges,) = reader.unpack(_U32)
    unknown_end = _read_list(reader, 1, "B")
    record = {
        "receipe_key": receipe_key,
        "need_item_key": need_item_key,
        "name_kr": name_kr,
        "house_use_type": house_use_type,
        "icon_type": icon_type,
        "unknown_tail_02": unknown_tail_02,
        "level_exchanges": level_exchanges,
        "unknown_after_level_exchanges": unknown_after_level_exchanges,
        "unknown_end": unknown_end,
    }
    return record, reader.pos


def _read_list(reader: RecordReader, item_size: int, code: str) -> list[int]:
    """A u32 count, then `count` values of `item_size` bytes.

    Raises ValueError when the count runs past the end of the file.
    """
    (count,) = reader.unpack(_U32)
    if count * item_size > reader.remaining():
        raise ValueError(f"list of {count:,} values runs past the end of {FILE_NAME}")
    return list(reader.unpack(struct.Struct(f"<{count}{code}")))
