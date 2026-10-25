"""`extractblackstone.bss`: what Black Stone extraction gives per difficulty, gear kind and level.

    u32 count | count x Group
    Group: u32 difficulty | u32 weapon_count | u32 armor_count
           | weapon_count x Entry | armor_count x Entry
    Entry: u8 enchant_level | u32 result_item_key | u64 unknown_05 | u64 unknown_0d

Layout 1 in docs/file-formats/bss/extractblackstone_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "extractblackstone.bss"

_COUNT_SIZE = 4
_GROUP_HEAD = struct.Struct("<III")
_ENTRY = struct.Struct("<BIQQ")
_ENTRY_FIELDS = ("enchant_level", "result_item_key", "unknown_05", "unknown_0d")


def _entries(reader: RecordReader, count: int, difficulty: int, is_weapon: bool) -> list[dict]:
    return [
        {
            "difficulty": difficulty,
            "is_weapon": is_weapon,
            **dict(zip(_ENTRY_FIELDS, reader.unpack(_ENTRY), strict=True)),
        }
        for _ in range(count)
    ]


def parse_extractblackstone_records(data: bytes) -> list[dict]:
    """One record per entry, weapons before armor within each group, in file order.

    Each record carries its group's `difficulty` and `is_weapon` (which list
    it came from). Raises ValueError when the groups do not end at the last
    byte of the file.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its group count")

    reader = RecordReader(data, _COUNT_SIZE, len(data), FILE_NAME)
    records = []
    for _ in range(u32(data, 0)):
        difficulty, weapon_count, armor_count = reader.unpack(_GROUP_HEAD)
        records += _entries(reader, weapon_count, difficulty, is_weapon=True)
        records += _entries(reader, armor_count, difficulty, is_weapon=False)
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} has {reader.remaining():,} bytes after its last group")
    return records
