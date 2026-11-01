"""`minigamefindpattern.dbss`: the tile patterns of the Lakiaro digging minigame.

    u32 group_count | group_count x (u8 slot_index | u32 row_count | row_count x Pattern Row)

    Pattern Row: u16 pattern_index | u16 pattern_index_dup | u16 change_pattern
        | u16 root_begin_no | u8 root_size | str8 image_file | str8 image_file2
        | u16[4] slot_coordinate | u8 next_pattern_end_direction
        | u8[4] root_begin_direction | u64 count | u16[count] next_pattern_indexes

`minigamefindpatternoffset.dbss` has the same groups, with (u16 key, u32
offset, u32 size) rows that point 2 bytes into a row, at `pattern_index_dup`.
Layout 1 in docs/file-formats/dbss/minigamefindpattern_dbss.md.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _common.record_reader import RecordReader


FILE_NAME = "minigamefindpattern.dbss"
OFFSET_FILE = "minigamefindpatternoffset.dbss"

# `next_pattern_end_direction` of a row with no end direction.
NO_DIRECTION = 4
# The direction values in order; `root_begin_direction` holds one flag per value.
DIRECTION_COUNT = 4

_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
_GROUP_HEAD = struct.Struct("<BI")
# pattern_index | pattern_index_dup | change_pattern | root_begin_no | root_size
_ROW_HEAD = struct.Struct("<HHHHB")
_COORDINATES = struct.Struct("<4H")
# next_pattern_end_direction | root_begin_direction[4]
_DIRECTIONS = struct.Struct(f"<B{DIRECTION_COUNT}B")
_INDEX_ROW = struct.Struct("<HII")


class PatternIndexRow(NamedTuple):
    slot_index: int
    pattern_index: int
    data_offset: int
    data_size: int


def parse_minigamefindpattern(data: bytes) -> list[dict]:
    """Every pattern in file order, with its group's `slot_index`.

    `change_pattern` and `root_begin_no` are None where the file stores `0`,
    and `next_pattern_end_direction` where it stores `NO_DIRECTION`. Raises
    ValueError when a group or row runs past the file or bytes are left after
    the last group.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    (group_count,) = reader.unpack(_U32)
    records: list[dict] = []
    for _ in range(group_count):
        slot_index, row_count = reader.unpack(_GROUP_HEAD)
        records.extend(_read_row(reader, slot_index) for _ in range(row_count))
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME}: {reader.remaining():,} bytes left after the last group")
    return records


def _read_row(reader: RecordReader, slot_index: int) -> dict:
    pattern_index, pattern_index_dup, change_pattern, root_begin_no, root_size = reader.unpack(_ROW_HEAD)
    image_file = reader.text(wide=False)
    image_file2 = reader.text(wide=False)
    slot_coordinate = list(reader.unpack(_COORDINATES))
    end_direction, *root_begin_direction = reader.unpack(_DIRECTIONS)
    (next_count,) = reader.unpack(_U64)
    next_patterns = list(reader.unpack(struct.Struct(f"<{next_count}H")))
    return {
        "slot_index": slot_index,
        "pattern_index": pattern_index,
        "pattern_index_dup": pattern_index_dup,
        "change_pattern": change_pattern or None,
        "root_begin_no": root_begin_no or None,
        "root_size": root_size,
        "image_file": image_file,
        "image_file2": image_file2,
        "slot_coordinate": slot_coordinate,
        "next_pattern_end_direction": None if end_direction == NO_DIRECTION else end_direction,
        "root_begin_direction": root_begin_direction,
        "next_pattern_indexes": next_patterns,
    }


def parse_minigamefindpatternoffset(data: bytes) -> list[PatternIndexRow]:
    """Every index row in file order. Raises ValueError like `parse_minigamefindpattern()`."""
    reader = RecordReader(data, 0, len(data), OFFSET_FILE)
    (group_count,) = reader.unpack(_U32)
    rows: list[PatternIndexRow] = []
    for _ in range(group_count):
        slot_index, row_count = reader.unpack(_GROUP_HEAD)
        rows.extend(PatternIndexRow(slot_index, *reader.unpack(_INDEX_ROW)) for _ in range(row_count))
    if not reader.at_end():
        raise ValueError(f"{OFFSET_FILE}: {reader.remaining():,} bytes left after the last group")
    return rows
