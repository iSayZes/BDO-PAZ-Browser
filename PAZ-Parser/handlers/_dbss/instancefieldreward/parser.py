"""`instancefieldreward.dbss`: the rewards of an instance dungeon.

    u32 count | count x Row
    Row: u16 instance_dungeon_no | u16 instance_dungeon_no_dup | u32 learn_skill
         | u32 item_groups[5] | u32 push_item_count | push_item_count x 12 bytes
         | u32 related_region_count | u16 related_regions[related_region_count]

`instancefieldrewardoffset.dbss` (u32 count, then u16 key, offset and size per
row) points 2 bytes into each row, at `instance_dungeon_no_dup`. Layout 2 in
docs/file-formats/dbss/instancefieldreward_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "instancefieldreward.dbss"
OFFSET_FILE = "instancefieldrewardoffset.dbss"
KEY_FIELD = "instance_dungeon_no"

ITEM_GROUP_COUNT = 5
_COUNT_SIZE = 4
_HEAD = struct.Struct(f"<HHI{ITEM_GROUP_COUNT}I")
_U32 = struct.Struct("<I")
_PUSH_ITEM = struct.Struct("<Iq")
_REGION = struct.Struct("<H")


def _read_row(reader: RecordReader) -> dict:
    key, key_dup, learn_skill, *item_groups = reader.unpack(_HEAD)
    (push_item_count,) = reader.unpack(_U32)
    push_items = [list(reader.unpack(_PUSH_ITEM)) for _ in range(push_item_count)]
    (region_count,) = reader.unpack(_U32)
    regions = [reader.unpack(_REGION)[0] for _ in range(region_count)]
    return {
        KEY_FIELD: key,
        "instance_dungeon_no_dup": key_dup,
        "learn_skill": learn_skill,
        "item_groups": item_groups,
        "push_item_count": push_item_count,
        "push_items": push_items,
        "related_region_count": region_count,
        "related_regions": regions,
    }


def parse_instancefieldreward_records(data: bytes) -> list[dict]:
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


def parse_instancefieldrewardoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
