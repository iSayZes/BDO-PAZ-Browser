"""`customizeditem.dbss`: the item each condition gives out of a per-character box.

    u32 count | count x record
    record: u16 customized_item_key | u32 item_count
            | item_count x (str16 condition | u32 item_key) | u16 customized_item_key_dup

`item_key` packs `enchant_level << 24 | item_id`. `customizeditemoffset.dbss`
(u32 count, then u16 key, u32 offset and u32 size per row) points 2 bytes
into a record, at `item_count`. Layout 1 in
docs/file-formats/customizeditem_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "customizeditem.dbss"
OFFSET_FILE = "customizeditemoffset.dbss"
KEY_FIELD = "customized_item_key"

_KEY = struct.Struct("<H")
_COUNT = struct.Struct("<I")
_ITEM_KEY = struct.Struct("<I")
# The u64 length of an empty condition and the item key.
_MIN_ITEM_SIZE = 12


def _read_item(reader: RecordReader) -> dict:
    condition = reader.text(wide=True)
    (item_key,) = reader.unpack(_ITEM_KEY)
    return {"condition": condition, "item_key": item_key}


def _read_record(reader: RecordReader) -> dict:
    (key,) = reader.unpack(_KEY)
    (item_count,) = reader.unpack(_COUNT)
    if item_count * _MIN_ITEM_SIZE > reader.remaining():
        raise ValueError(f"{FILE_NAME}: key {key} lists {item_count:,} items, more than the file holds")
    items = [_read_item(reader) for _ in range(item_count)]
    (key_dup,) = reader.unpack(_KEY)
    return {
        KEY_FIELD: key,
        "item_count": item_count,
        "items": items,
        "customized_item_key_dup": key_dup,
    }


def parse_customizeditem_records(data: bytes) -> list[dict]:
    """Every record in file order. Raises ValueError when a record runs past the file or the records end early."""
    return read_counted_records(data, _read_record, FILE_NAME)


def parse_customizeditemoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
