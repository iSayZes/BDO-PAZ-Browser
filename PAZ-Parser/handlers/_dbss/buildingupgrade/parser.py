"""`buildingupgrade.dbss`: what a placed siege building upgrades into and the items it takes.

    PABR | u32 count | count x row | u32 0 | u32 table_start | u32 0

A row is a u16 character key, a u32 upgrade time, an i32 upgrade level, the
u16 character key it becomes and a u32-counted list of (u32 item key, i64
count) pairs. The rows end where the empty PABR string table starts.
`buildingupgradeoffset.dbss` points at each row's key. Layout in
docs/file-formats/dbss/buildingupgrade_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "buildingupgrade.dbss"
OFFSET_FILE = "buildingupgradeoffset.dbss"
COUNT_OFFSET = 4

# character_key, upgrade_time, upgrade_level, target_character_key, item_count
_HEAD = struct.Struct("<HIiHI")
# item_key, count
_SOURCE_ITEM = struct.Struct("<Iq")


def parse_buildingupgrade_records(data: bytes) -> list[dict]:
    """Every upgrade row, in file order.

    Raises ValueError on a bad magic or trailer, a row that runs past the
    string table, or rows that end before it.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    count = u32(data, COUNT_OFFSET)
    reader = RecordReader(data, HEADER_SIZE, rows_end, FILE_NAME)
    records = [_read_row(reader) for _ in range(count)]
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return records


def _read_row(reader: RecordReader) -> dict:
    character_key, upgrade_time, upgrade_level, target_character_key, item_count = reader.unpack(_HEAD)
    if item_count * _SOURCE_ITEM.size > reader.remaining():
        raise ValueError(f"list of {item_count:,} source items runs past the rows of {FILE_NAME}")
    items = [
        {"item_key": item_key, "count": count}
        for item_key, count in (reader.unpack(_SOURCE_ITEM) for _ in range(item_count))
    ]
    return {
        "character_key": character_key,
        "upgrade_time": upgrade_time,
        "upgrade_level": upgrade_level,
        "target_character_key": target_character_key,
        "item_count": item_count,
        "items": items,
    }
