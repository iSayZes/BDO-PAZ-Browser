"""`minigamefindtool.dbss`: the hoe values of the Lakiaro digging minigame per item grade and enhancement level.

    grade blocks back to back to the end of the file, block i = item grade i:
    u8 unknown_00 | 21 x (u32 r_click_count | u8 open_slot_count | u32 decrease_damage_rate)

The file stores no count and no key. `minigamefindtooloffset.dbss` holds the
same blocks as a u32 row count and (u8 enchant_level, u32 offset, u32 size)
rows. Layout 2 in docs/file-formats/minigamefindtool_dbss.md.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _common.record_reader import RecordReader


FILE_NAME = "minigamefindtool.dbss"
OFFSET_FILE = "minigamefindtooloffset.dbss"

# Enhancement levels +0 to PEN.
LEVEL_COUNT = 21

_BLOCK_HEAD = struct.Struct("<B")
# r_click_count | open_slot_count | decrease_damage_rate
LEVEL_ROW = struct.Struct("<IBI")
GRADE_BLOCK_SIZE = _BLOCK_HEAD.size + LEVEL_COUNT * LEVEL_ROW.size

_U32 = struct.Struct("<I")
_INDEX_ROW = struct.Struct("<BII")


class ToolIndexRow(NamedTuple):
    item_grade: int
    enchant_level: int
    data_offset: int
    data_size: int


def parse_minigamefindtool(data: bytes) -> list[dict]:
    """Every row in file order, keyed by its block (item grade) and place (enhancement level).

    Raises ValueError when the file is not a whole number of grade blocks.
    """
    if len(data) % GRADE_BLOCK_SIZE:
        raise ValueError(f"{FILE_NAME} is {len(data):,} bytes, not a whole number of {GRADE_BLOCK_SIZE}-byte grade blocks")

    records: list[dict] = []
    for item_grade, block_start in enumerate(range(0, len(data), GRADE_BLOCK_SIZE)):
        (unknown_00,) = _BLOCK_HEAD.unpack_from(data, block_start)
        rows_start = block_start + _BLOCK_HEAD.size
        for enchant_level in range(LEVEL_COUNT):
            r_click_count, open_slot_count, decrease_damage_rate = LEVEL_ROW.unpack_from(
                data, rows_start + enchant_level * LEVEL_ROW.size
            )
            records.append({
                "item_grade": item_grade,
                "enchant_level": enchant_level,
                "unknown_00": unknown_00,
                "r_click_count": r_click_count,
                "open_slot_count": open_slot_count,
                "decrease_damage_rate": decrease_damage_rate,
            })
    return records


def parse_minigamefindtooloffset(data: bytes) -> list[ToolIndexRow]:
    """Every index row in file order; group i is item grade i.

    Raises ValueError when a group runs past the end of the file.
    """
    reader = RecordReader(data, 0, len(data), OFFSET_FILE)
    rows: list[ToolIndexRow] = []
    item_grade = 0
    while not reader.at_end():
        (row_count,) = reader.unpack(_U32)
        rows.extend(ToolIndexRow(item_grade, *reader.unpack(_INDEX_ROW)) for _ in range(row_count))
        item_grade += 1
    return rows
