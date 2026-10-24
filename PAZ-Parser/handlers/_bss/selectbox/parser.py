"""`selectbox.bss`: the items of each choose-your-item box, per type.

    PABR | u32 box_count | box_count x Box | String Table | u32 table_start | u32 0
    Box: 5 x Type List (type 0 to 4 in order)
    Type List: u32 entry_count | entry_count x 21-byte Entry
    Entry: u32 key | u8 type | u32 item_key | u64 item_count | u32 texture_name

The box stores no key of its own; every entry repeats it. `texture_name`
indexes the string table (`Combine_Tab_Icon_Daily`). Layout 1 in
docs/file-formats/selectbox_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import (
    HEADER_SIZE,
    U32_SIZE,
    check_rows_end,
    checked_string_table_start,
    read_string_table,
    string_at,
)
from _common.record_reader import RecordReader


FILE_NAME = "selectbox.bss"
KEY_FIELD = "key"
# `__eSelectBoxTypeCount`: every box stores this many type lists.
TYPE_COUNT = 5

_COUNT = struct.Struct("<I")
_ENTRY = struct.Struct("<IBIQI")
_ENTRY_FIELDS = (KEY_FIELD, "type", "item_key", "item_count", "texture_name")


def _read_type_list(reader: RecordReader, strings: list[str]) -> list[dict]:
    (count,) = reader.unpack(_COUNT)
    if count * _ENTRY.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} type list count {count:,} at 0x{reader.pos - _COUNT.size:X} runs past the boxes")
    entries = []
    for _ in range(count):
        entry = dict(zip(_ENTRY_FIELDS, reader.unpack(_ENTRY), strict=True))
        entries.append({**entry, "texture_name_text": string_at(strings, entry["texture_name"])})
    return entries


def parse_selectbox_boxes(data: bytes) -> list[dict]:
    """Every box in file order: its key and its `type_lists` (one entry list per type).

    The key is the one its entries repeat, None for a box with no entry.
    Raises ValueError on a bad magic or trailer, when a list runs past the
    string table, or when the boxes do not end where it starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE - U32_SIZE, end, FILE_NAME)
    (box_count,) = reader.unpack(_COUNT)
    boxes = []
    for _ in range(box_count):
        type_lists = [_read_type_list(reader, strings) for _ in range(TYPE_COUNT)]
        keys = [entry[KEY_FIELD] for entries in type_lists for entry in entries]
        boxes.append({KEY_FIELD: keys[0] if keys else None, "type_lists": type_lists})
    check_rows_end(data, reader.pos, f"{FILE_NAME} boxes")
    return boxes
