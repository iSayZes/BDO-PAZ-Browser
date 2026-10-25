"""`itemenchantpuzzle.dbss`: the inventory puzzles of each first piece.

    u32 record_count | record_count x Record
    Record: u32 start_puzzle_item_key | u64 puzzle_key_count | u16[puzzle_key_count] puzzle_keys

No offset index and no PABR magic. Each puzzle key is an `itempuzzle.dbss`
row whose `start_puzzle_item_key` is the record's item. Layout 1 in
docs/file-formats/dbss/itemenchantpuzzle_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "itemenchantpuzzle.dbss"
KEY_FIELD = "start_puzzle_item_key"

_HEAD = struct.Struct("<IQ")
_PUZZLE_KEY_SIZE = 2


def _read_record(reader: RecordReader) -> dict:
    item_key, count = reader.unpack(_HEAD)
    if count * _PUZZLE_KEY_SIZE > reader.remaining():
        raise ValueError(f"{FILE_NAME} item {item_key} puzzle count {count:,} runs past the end")
    puzzle_keys = list(reader.unpack(struct.Struct(f"<{count}H")))
    return {KEY_FIELD: item_key, "puzzle_key_count": count, "puzzle_keys": puzzle_keys}


def parse_itemenchantpuzzle_records(data: bytes) -> list[dict]:
    """Every record in file order.

    Raises ValueError when a record runs past the file or the records end before it.
    """
    return read_counted_records(data, _read_record, FILE_NAME)
