"""`itemviewstackenchantgroupss.bss`: groups of `enchantstaticstatus.dbss` enchant keys.

    u32 count | count x (u32 enchant_key | u32 unknown_04 | u64 group_count
                         | u32[group_count] group_enchant_keys)

Every key of a group has its own row with the whole group. Layout in
docs/file-formats/itemviewstackenchantgroupss_bss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader


FILE_NAME = "itemviewstackenchantgroupss.bss"

_COUNT = struct.Struct("<I")
# enchant_key | unknown_04 | group_count
_ROW_HEAD = struct.Struct("<IIQ")
_KEY_SIZE = 4


def parse_itemviewstackenchantgroupss_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError when a row runs past the file or bytes are left after
    the last row: then the layout has changed and every field is suspect.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    (count,) = reader.unpack(_COUNT)
    records = [_read_row(reader, index) for index in range(count)]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME}: {reader.remaining():,} bytes left after {count:,} rows")
    return records


def _read_row(reader: RecordReader, index: int) -> dict:
    enchant_key, unknown_04, group_count = reader.unpack(_ROW_HEAD)
    if group_count * _KEY_SIZE > reader.remaining():
        raise ValueError(f"{FILE_NAME}: row {index} lists {group_count:,} keys, past the end of the file")
    group_enchant_keys = reader.unpack(struct.Struct(f"<{group_count}I"))
    return {
        "enchant_key": enchant_key,
        "unknown_04": unknown_04,
        "group_count": group_count,
        "group_enchant_keys": list(group_enchant_keys),
    }
