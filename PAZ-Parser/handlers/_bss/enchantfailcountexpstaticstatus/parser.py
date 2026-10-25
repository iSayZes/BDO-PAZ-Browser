"""`enchantfailcountexpstaticstatus.bss`: values per fail stack and feed entry.

    PABR | u32 count | count x (u32 group_count
    | group_count x (u16 fairy_feed_key | u32 entry_count
    | entry_count x (u8 enchant_level | u32 unknown_01)) | u64 stack)
    | empty string table | u32 end_of_records | u32 0

`stack` closes each record, after its groups. Full layout in
docs/file-formats/bss/enchantfailcountexpstaticstatus_bss.md (Layout 2).
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start
from _common.record_reader import RecordReader


_FILE = "enchantfailcountexpstaticstatus.bss"

_COUNT = struct.Struct("<I")
# u16 fairy_feed_key | u32 entry_count
_GROUP_HEAD = struct.Struct("<HI")
# u8 enchant_level | u32 unknown_01, unaligned
_ENTRY = struct.Struct("<BI")
_STACK = struct.Struct("<Q")


def _read_record(reader: RecordReader) -> list[dict]:
    """One flat row per entry, each carrying the record's `stack`."""
    (group_count,) = reader.unpack(_COUNT)
    entries: list[tuple[int, int, int]] = []
    for _ in range(group_count):
        fairy_feed_key, entry_count = reader.unpack(_GROUP_HEAD)
        for _ in range(entry_count):
            enchant_level, unknown_01 = reader.unpack(_ENTRY)
            entries.append((fairy_feed_key, enchant_level, unknown_01))
    (stack,) = reader.unpack(_STACK)
    return [
        {
            "stack": stack,
            "fairy_feed_key": fairy_feed_key,
            "enchant_level": enchant_level,
            "unknown_01": unknown_01,
        }
        for fairy_feed_key, enchant_level, unknown_01 in entries
    ]


def parse_enchantfailcountexp_rows(data: bytes) -> list[dict]:
    """Every entry in file order, one row each.

    Raises ValueError when a record runs past the string table or the walk
    does not end where it starts: then the layout has changed.
    """
    end = checked_string_table_start(data, _FILE)
    reader = RecordReader(data, HEADER_SIZE, end, _FILE)
    rows = [row for _ in range(u32(data, 4)) for row in _read_record(reader)]
    if not reader.at_end():
        raise ValueError(f"{_FILE} records do not end where its string table starts")
    return rows
