"""`boss_spawnlevel.bss`: the difficulty levels of the Guild Boss Summon window.

    PABR | u32 count | count x group | string table | u32 table_start | u32 0
    group: u32 entry_count | entry_count x 21-byte entry
    entry: u32 boss_key | u8 level | u16 | u16 | u32 reward_item_id
           | u32 image (string index) | u16 | u16 character_id

`boss_key` is the key of `boss_spawn.bss`. Full layout in
docs/file-formats/boss_spawnlevel_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import (
    HEADER_SIZE,
    check_rows_end,
    checked_string_table_start,
    read_string_table,
    string_at,
)
from _common.record_reader import RecordReader
from _common.ui_texture import ui_texture_path


FILE_NAME = "boss_spawnlevel.bss"

_COUNT = struct.Struct("<I")
_ENTRY = struct.Struct("<IBHHIIHH")


def _read_entry(reader: RecordReader, strings: list[str]) -> dict:
    (
        boss_key, level, unknown_05, unknown_07,
        reward_item_id, image, unknown_11, character_id,
    ) = reader.unpack(_ENTRY)
    return {
        "boss_key": boss_key,
        "level": level,
        "character_id": character_id,
        "reward_item_id": reward_item_id,
        "image_path": ui_texture_path(string_at(strings, image)),
        "unknown_05": unknown_05,
        "unknown_07": unknown_07,
        "unknown_11": unknown_11,
    }


def parse_boss_spawnlevel_records(data: bytes) -> list[dict]:
    """Every entry of every group, in file order.

    Raises ValueError on a bad magic, an entry running past the string table
    or groups that do not end where the string table starts.
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE, table_start, FILE_NAME)
    records: list[dict] = []
    for _ in range(u32(data, 4)):
        (entry_count,) = reader.unpack(_COUNT)
        records.extend(_read_entry(reader, strings) for _ in range(entry_count))
    check_rows_end(data, reader.pos, f"{FILE_NAME} groups")
    return records


def boss_characters(data: bytes) -> dict[int, int]:
    """Boss key -> the boss character of its lowest level.

    Raises ValueError as `parse_boss_spawnlevel_records` does.
    """
    characters: dict[int, int] = {}
    for record in sorted(parse_boss_spawnlevel_records(data), key=lambda r: r["level"]):
        characters.setdefault(record["boss_key"], record["character_id"])
    return characters


def optional_boss_characters(data: bytes | None) -> dict[int, int]:
    """`boss_characters` of an optional companion; empty when it is missing or
    unreadable, for tables that show the boss names only as a convenience."""
    if data is None:
        return {}
    try:
        return boss_characters(data)
    except ValueError:
        return {}
