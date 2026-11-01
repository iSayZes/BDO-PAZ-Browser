"""`hardcorerandomspawncharacterstaticstatusmanager.bss`: the characters that spawn at random on the Hardcore channel.

    PABR | u32 row_count | row_count x Row (19 bytes)
    | u32 boss_count | boss_count x u16 boss_keys
    | u32 npc_count | npc_count x u16 npc_keys
    | u32 unknown_str_ref_count | unknown_str_ref_count x u32 unknown_str_refs
    | string table | u32 table_start | u32 0
    Row: u16 character_key | i16 x 5 string refs | u8 unknown_0c
    | u32 random_spawn_key | u16 unknown_11

A string ref is a string-table index, `-1` for none. Full layout in
docs/file-formats/bss/hardcorerandomspawncharacterstaticstatusmanager_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_strings import (
    HEADER_SIZE,
    check_rows_end,
    checked_string_table_start,
    read_string_table,
    string_at,
)
from _common.record_reader import RecordReader


FILE_NAME = "hardcorerandomspawncharacterstaticstatusmanager.bss"

_COUNT = struct.Struct("<I")
_ROW = struct.Struct("<H5hBIH")
_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")
# The five string refs of a row, in row order, each with the field its string goes to.
STRING_FIELDS: tuple[tuple[str, str], ...] = (
    ("world_map_icon_ref", "world_map_icon"),
    ("boss_icon_ref", "boss_icon"),
    ("notice_background_ref", "notice_background"),
    ("notice_ref", "notice_key"),
    ("reveal_notice_ref", "reveal_notice_key"),
)


@dataclass(frozen=True)
class RandomSpawnFile:
    """The rows and the three lists after them."""

    rows: list[dict]
    boss_keys: list[int]
    npc_keys: list[int]
    unknown_str_refs: list[int]


def _read_row(reader: RecordReader, strings: list[str]) -> dict:
    character_key, *refs, unknown_0c, random_spawn_key, unknown_11 = reader.unpack(_ROW)
    record: dict = {"random_spawn_key": random_spawn_key, "character_key": character_key}
    for (ref_field, text_field), ref in zip(STRING_FIELDS, refs):
        record[ref_field] = ref
        record[text_field] = string_at(strings, ref)
    record["unknown_0c"] = unknown_0c
    record["unknown_11"] = unknown_11
    return record


def _read_list(reader: RecordReader, entry: struct.Struct, name: str) -> list[int]:
    """A u32 count, then that many values of `entry`."""
    (count,) = reader.unpack(_COUNT)
    if count * entry.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} {name} count {count:,} runs past the string table")
    return [reader.unpack(entry)[0] for _ in range(count)]


def parse_random_spawn_file(data: bytes) -> RandomSpawnFile:
    """Every row in file order, with the strings its refs point to, and the lists after the rows.

    Raises ValueError on a bad magic or trailer, or when the lists do not end
    where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE - _COUNT.size, end, FILE_NAME)
    (row_count,) = reader.unpack(_COUNT)
    if row_count * _ROW.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} row count {row_count:,} runs past the string table")
    rows = [_read_row(reader, strings) for _ in range(row_count)]
    boss_keys = _read_list(reader, _U16, "boss_keys")
    npc_keys = _read_list(reader, _U16, "npc_keys")
    unknown_str_refs = _read_list(reader, _U32, "unknown_str_refs")
    check_rows_end(data, reader.pos, f"{FILE_NAME} lists")
    return RandomSpawnFile(rows, boss_keys, npc_keys, unknown_str_refs)
