"""`buildingbuff.dbss`: the villa buffs and their silver cost.

The file and its `buildingbuffoffset.dbss` index use the grouped walk in
`_common/grouped_rows.py`: a u32 list count, then per list a u32 row
count and that many rows. List `i` holds the rows whose `Count_Villa` is
`i + 1`.

    Row:        u16 buff_index | u16 skill_no | i64 cost
    Offset Row: u16 buff_index | u32 offset | u32 size

Layout in docs/file-formats/dbss/buildingbuff_dbss.md.
"""

from __future__ import annotations

import struct

from _common.grouped_rows import parse_grouped_rows

FILE_NAME = "buildingbuff.dbss"
OFFSET_FILE = "buildingbuffoffset.dbss"

ROW = struct.Struct("<HHq")
OFFSET_ROW = struct.Struct("<HII")
# The bytes an offset row skips: it points at `skill_no`, past `buff_index`.
BUFF_INDEX_SIZE = 2
# List `i` holds `Count_Villa` `i + 1`.
_VILLA_COUNT_BASE = 1


def parse_buildingbuff_records(data: bytes) -> list[dict]:
    """Every villa buff, in file order.

    Raises ValueError when a list runs past the end of the file or bytes are
    left after the last list.
    """
    return [
        {
            "villa_count": group + _VILLA_COUNT_BASE,
            "buff_index": buff_index,
            "skill_no": skill_no,
            "cost": cost,
        }
        for group, (buff_index, skill_no, cost) in parse_grouped_rows(data, FILE_NAME, ROW)
    ]


def parse_buildingbuffoffset_records(data: bytes) -> list[dict]:
    """Every index row, in file order, with the `villa_count` of its list."""
    return [
        {
            "villa_count": group + _VILLA_COUNT_BASE,
            "buff_index": buff_index,
            "offset": offset,
            "size": size,
        }
        for group, (buff_index, offset, size) in parse_grouped_rows(data, OFFSET_FILE, OFFSET_ROW)
    ]
