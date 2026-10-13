"""`bossinfostaicstatusmanager.bss`: the bosses of the Boss Info window.

    PABR | u32 count | count x record | string table | u32 table_start | u32 0
    record: groups spawn_times | groups unknown_ids | u32 n, u32[n] rewards
            | u32 main_texture | u32 list_texture | u16 character_id
            | u8 has_reinforced [| u16 character_id | u32 main | u32 list
            | u32 n, u32[n] rewards] | f32[3] position | u8 type | u8 | u8
    groups: u32 count, count x (u8 group key, u32 n, u32[n] values)

The textures are string table indexes holding texture keys. Full layout in
docs/file-formats/bossinfostaicstatusmanager_bss.md.
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


FILE_NAME = "bossinfostaicstatusmanager.bss"

_U8 = struct.Struct("<B")
_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")
_TEXTURES = struct.Struct("<II")
_POSITION = struct.Struct("<3f")
_FLAGS = struct.Struct("<BBB")


def _u32_list(reader: RecordReader) -> list[int]:
    (count,) = reader.unpack(_U32)
    return [reader.unpack(_U32)[0] for _ in range(count)]


def _groups(reader: RecordReader) -> list[dict]:
    (count,) = reader.unpack(_U32)
    groups = []
    for _ in range(count):
        (group,) = reader.unpack(_U8)
        groups.append({"group": group, "values": _u32_list(reader)})
    return groups


def _textures(reader: RecordReader, strings: list[str]) -> tuple[str, str]:
    main, listed = reader.unpack(_TEXTURES)
    return string_at(strings, main), string_at(strings, listed)


def _reinforced(reader: RecordReader, strings: list[str]) -> dict:
    """The reinforced form, which stores its textures before its rewards."""
    (character_id,) = reader.unpack(_U16)
    main_texture, list_texture = _textures(reader, strings)
    return {
        "reinforced_character_id": character_id,
        "reinforced_main_texture": main_texture,
        "reinforced_list_texture": list_texture,
        "reinforced_reward_items": _u32_list(reader),
    }


def _no_reinforced() -> dict:
    return {
        "reinforced_character_id": None,
        "reinforced_main_texture": "",
        "reinforced_list_texture": "",
        "reinforced_reward_items": [],
    }


def _read_record(reader: RecordReader, strings: list[str]) -> dict:
    spawn_times = _groups(reader)
    unknown_ids = _groups(reader)
    reward_items = _u32_list(reader)
    main_texture, list_texture = _textures(reader, strings)
    (character_id,) = reader.unpack(_U16)
    (has_reinforced,) = reader.unpack(_U8)
    reinforced = _reinforced(reader, strings) if has_reinforced else _no_reinforced()
    x, y, z = reader.unpack(_POSITION)
    boss_info_type, unknown_flag, is_event_boss = reader.unpack(_FLAGS)
    return {
        "character_id": character_id,
        "boss_info_type": boss_info_type,
        "reward_items": reward_items,
        "main_texture": main_texture,
        "list_texture": list_texture,
        **reinforced,
        "x": x,
        "y": y,
        "z": z,
        "spawn_times": spawn_times,
        "is_event_boss": bool(is_event_boss),
        "unknown_ids": unknown_ids,
        "unknown_flag": unknown_flag,
    }


def parse_bossinfo_records(data: bytes) -> list[dict]:
    """Every record in file order, with its texture keys resolved.

    Raises ValueError on a bad magic, a record running past the string table
    or records that do not end where the string table starts.
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE, table_start, FILE_NAME)
    records = [_read_record(reader, strings) for _ in range(u32(data, 4))]
    check_rows_end(data, reader.pos, f"{FILE_NAME} records")
    return records
