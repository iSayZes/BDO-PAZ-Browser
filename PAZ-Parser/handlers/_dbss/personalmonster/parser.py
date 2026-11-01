"""`personalmonster.dbss`: the Dark Rift bosses.

    u32 count | count x Row
    Row: u16 character_key | str16 description_kr | u32 difficulty
         | str8 monster_image | u32 drop_item_count | u32 drop_item_keys[drop_item_count]
         | u32 unknown_drop_item_keys_00

`personalmonsteroffset.dbss` (u32 count, then u16 key, offset and size per
row) points at each row start. Layout 1 in
docs/file-formats/dbss/personalmonster_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "personalmonster.dbss"
OFFSET_FILE = "personalmonsteroffset.dbss"
KEY_FIELD = "character_key"

_COUNT_SIZE = 4
_KEY = struct.Struct("<H")
_U32 = struct.Struct("<I")


def _read_row(reader: RecordReader) -> dict:
    (character_key,) = reader.unpack(_KEY)
    description_kr = reader.text(wide=True)
    (difficulty,) = reader.unpack(_U32)
    monster_image = reader.text(wide=False)
    (drop_item_count,) = reader.unpack(_U32)
    drop_item_keys = [reader.unpack(_U32)[0] for _ in range(drop_item_count)]
    (unknown_drop_item_keys_00,) = reader.unpack(_U32)
    return {
        KEY_FIELD: character_key,
        "description_kr": description_kr,
        "difficulty": difficulty,
        "monster_image": monster_image,
        "drop_item_count": drop_item_count,
        "drop_item_keys": drop_item_keys,
        "unknown_drop_item_keys_00": unknown_drop_item_keys_00,
    }


def parse_personalmonster_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError when a row runs past the file or the rows do not end at
    its last byte.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    reader = RecordReader(data, _COUNT_SIZE, len(data), FILE_NAME)
    records = [_read_row(reader) for _ in range(u32(data, 0))]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} has {reader.remaining():,} bytes after its last row")
    return records


def parse_personalmonsteroffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
