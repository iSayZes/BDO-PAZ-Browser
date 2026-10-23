"""`solareoptionstaticstatusmanager.bss`: the Arena of Solare rank tiers and equipment presets.

    PABR | 4 x Mode | common values | u64 count | u32[count] unknown_item_keys
    | bytes[3] | 48 x Preset | f32[8] | String Table | u32 table_start | u32 0
    Mode:   79-byte head (u8 game_mode first) | 8 x Group
    Group:  41-byte head (u8 rank_group first) | u64 tier_count | tier_count x Tier
    Tier:   u32 min_rating | u32 max_ranking | u16 rank_tier_key | 6 x u32 string index
            | 9 x Item List (u64 item_count | item_count x (u32 item_key, u32, u64 count))
    Preset: u8 class_type | f32 | f32 | u64 n | n x Preset Item | u64 m | m x Preset Item
    Preset Item: u32 item_key | i32 | u8 equip_slot_no | u8 index

Every array but the counted ones has a fixed length. Layout 4 (client 3474
and later) in docs/file-formats/solareoptionstaticstatusmanager_bss.md; older
clients store fixed item blocks per tier, which this parser does not read.
"""

from __future__ import annotations

import struct
from collections.abc import Sequence
from typing import Any, NamedTuple

from _common.pabr_strings import HEADER_SIZE, U32_SIZE, check_rows_end, checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "solareoptionstaticstatusmanager.bss"
MODE_COUNT = 4
GROUP_COUNT = 8
PRESET_COUNT = 48
ITEM_LIST_COUNT = 9

_U64 = struct.Struct("<Q")

_MODE_HEAD = struct.Struct("<BBIIBf8IfIIiIIII")
_MODE_FIELDS = (
    "game_mode", "unknown_01", "unknown_02", "unknown_06", "unknown_0a", "unknown_0b",
    "unknown_0f", "unknown_13", "unknown_17", "unknown_1b", "unknown_1f", "unknown_23", "unknown_27", "unknown_2b",
    "unknown_2f", "unknown_33", "unknown_37", "unknown_3b", "unknown_3f", "unknown_43", "unknown_47", "unknown_4b",
)
_GROUP_HEAD = struct.Struct("<BffHHHB3fB3fQ")
_TIER_HEAD = struct.Struct("<IIH6I")
_TIER_STRINGS = (
    "description",
    "icon_texture",
    "match_slot_right_frame",
    "match_slot_left_frame",
    "hp_widget_right_frame",
    "hp_widget_left_frame",
)
_LIST_ITEM = struct.Struct("<IIQ")
_LIST_ITEM_FIELDS = ("item_key", "unknown_04", "count")

_COMMON = struct.Struct("<fBf9Q6IQ")
_ITEM_KEYS_TAIL = struct.Struct("<3s")
# class_type, unknown_01, unknown_05; the u64 equip_count follows.
_PRESET_HEAD = struct.Struct("<Bff")
_PRESET_ITEM = struct.Struct("<IiBB")
_PRESET_ITEM_FIELDS = ("item_key", "unknown_04", "equip_slot_no", "index")
_TAIL = struct.Struct("<8f")


class SolareOptionFile(NamedTuple):
    modes: list[dict]
    # The values between the modes and the presets, by their doc names.
    common: dict
    equip_presets: list[dict]
    # The eight f32 after the presets.
    tail: list[float]


def _counted(reader: RecordReader, item: struct.Struct, fields: Sequence[str], what: str) -> list[dict]:
    """A u64 count, then that many `item` structs as `fields` -> values."""
    (count,) = reader.unpack(_U64)
    if count * item.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} {what} count {count:,} at 0x{reader.pos - _U64.size:X} runs past the end")
    return [dict(zip(fields, reader.unpack(item), strict=True)) for _ in range(count)]


def _read_tier(reader: RecordReader, strings: list[str]) -> dict:
    min_rating, max_ranking, rank_tier_key, *refs = reader.unpack(_TIER_HEAD)
    tier = {"min_rating": min_rating, "max_ranking": max_ranking, "rank_tier_key": rank_tier_key}
    for field, index in zip(_TIER_STRINGS, refs, strict=True):
        tier[field] = index
        tier[f"{field}_key"] = string_at(strings, index)
    tier["item_lists"] = [
        _counted(reader, _LIST_ITEM, _LIST_ITEM_FIELDS, "item list") for _ in range(ITEM_LIST_COUNT)
    ]
    return tier


def _read_group(reader: RecordReader, strings: list[str]) -> dict:
    values = reader.unpack(_GROUP_HEAD)
    group = {
        "rank_group": values[0],
        "unknown_01": values[1],
        "unknown_05": values[2],
        "unknown_09": values[3],
        "unknown_0b": values[4],
        "unknown_0d": values[5],
        "unknown_0f": values[6],
        "unknown_10": list(values[7:10]),
        "unknown_1c": values[10],
        "unknown_1d": list(values[11:14]),
        "tier_count": values[14],
    }
    group["tiers"] = [_read_tier(reader, strings) for _ in range(group["tier_count"])]
    return group


def _read_mode(reader: RecordReader, strings: list[str]) -> dict:
    mode: dict[str, Any] = dict(zip(_MODE_FIELDS, reader.unpack(_MODE_HEAD), strict=True))
    mode["groups"] = [_read_group(reader, strings) for _ in range(GROUP_COUNT)]
    return mode


def _read_common(reader: RecordReader, strings: list[str]) -> dict:
    values = reader.unpack(_COMMON)
    common = {
        "unknown_modes_00": values[0],
        "unknown_modes_04": values[1],
        "unknown_modes_05": values[2],
        "unknown_modes_09": list(values[3:12]),
        "unknown_win_str_ref": values[12],
        "unknown_draw_str_ref": values[13],
        "unknown_lose_str_ref": values[14],
        "unknown_modes_5d": values[15],
        "unknown_modes_61": values[16],
        "unknown_modes_65": values[17],
        "unknown_item_count": values[18],
    }
    for field in ("unknown_win_str_ref", "unknown_draw_str_ref", "unknown_lose_str_ref"):
        common[f"{field}_text"] = string_at(strings, common[field])
    count = common["unknown_item_count"]
    if count * U32_SIZE > reader.remaining():
        raise ValueError(f"{FILE_NAME} item key count {count:,} runs past the end")
    common["unknown_item_keys"] = list(reader.unpack(struct.Struct(f"<{count}I")))
    common["unknown_item_keys_00"] = reader.unpack(_ITEM_KEYS_TAIL)[0].hex(" ")
    return common


def _read_preset(reader: RecordReader) -> dict:
    class_type, unknown_01, unknown_05 = reader.unpack(_PRESET_HEAD)
    equip_items = _counted(reader, _PRESET_ITEM, _PRESET_ITEM_FIELDS, "equip item")
    jewel_items = _counted(reader, _PRESET_ITEM, _PRESET_ITEM_FIELDS, "jewel item")
    return {
        "class_type": class_type,
        "unknown_01": unknown_01,
        "unknown_05": unknown_05,
        "equip_count": len(equip_items),
        "equip_items": equip_items,
        "jewel_count": len(jewel_items),
        "jewel_items": jewel_items,
    }


def parse_solareoption_file(data: bytes) -> SolareOptionFile:
    """The modes, common values, presets and tail values.

    Raises ValueError on a bad magic or trailer, a count that runs past the
    string table, or values that do not end where it starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE - U32_SIZE, end, FILE_NAME)
    modes = [_read_mode(reader, strings) for _ in range(MODE_COUNT)]
    common = _read_common(reader, strings)
    presets = [_read_preset(reader) for _ in range(PRESET_COUNT)]
    tail = list(reader.unpack(_TAIL))
    check_rows_end(data, reader.pos, f"{FILE_NAME} values")
    return SolareOptionFile(modes, common, presets, tail)


def tier_records(parsed: SolareOptionFile) -> list[dict]:
    """One record per tier, in file order, with its game mode and rank group.

    The unused modes have no tiers, so they add no record.
    """
    return [
        {"game_mode": mode["game_mode"], "rank_group": group["rank_group"], **tier}
        for mode in parsed.modes
        for group in mode["groups"]
        for tier in group["tiers"]
    ]
