"""`itembuildkit.bss`: the structures each siege build kit item places.

    PABR | u32 kit_count | kit_count x Kit | String Table | u32 table_start | u32 0
    Kit: u32 entry_count | entry_count x 35-byte Entry
    Entry: u32 item_key | u16 character_key | u32 use_condition
    | u32 contents_event_type | u32 contents_event_param1 | u32 icon_image_file
    | u32 description | u32 unknown_1a | u32 unknown_1e | u8 unknown_22

`use_condition`, `icon_image_file` and `description` index the string table.
Layout 3 in docs/file-formats/bss/itembuildkit_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_structs
from _common.pabr_strings import (
    HEADER_SIZE,
    U32_SIZE,
    check_rows_end,
    checked_string_table_start,
    read_string_table,
    string_at,
)
from _common.record_reader import RecordReader


FILE_NAME = "itembuildkit.bss"

_COUNT = struct.Struct("<I")
_ENTRY = struct.Struct("<IHIIIIIIIB")
_ENTRY_FIELDS = (
    "item_key",
    "character_key",
    "use_condition",
    "contents_event_type",
    "contents_event_param1",
    "icon_image_file",
    "description",
    "unknown_1a",
    "unknown_1e",
    "unknown_22",
)
# Each string index field and the record field that holds its text.
STRING_FIELDS = (
    ("use_condition", "use_condition_text"),
    ("icon_image_file", "icon_image_file_text"),
    ("description", "description_kr"),
)


def parse_itembuildkit_entries(data: bytes) -> list[dict]:
    """Every entry of every kit in file order, with the texts its string indexes name.

    Raises ValueError on a bad magic or trailer, when a kit runs past the
    string table, or when the kits do not end where it starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE - U32_SIZE, end, FILE_NAME)
    (kit_count,) = reader.unpack(_COUNT)
    entries = [
        entry
        for _ in range(kit_count)
        for entry in read_counted_structs(reader, _ENTRY, _ENTRY_FIELDS, f"{FILE_NAME} kit")
    ]
    check_rows_end(data, reader.pos, f"{FILE_NAME} kits")
    return [
        {**entry, **{text: string_at(strings, entry[index]) for index, text in STRING_FIELDS}}
        for entry in entries
    ]
