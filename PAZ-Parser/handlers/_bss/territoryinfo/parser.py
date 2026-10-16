"""`territoryinfo.bss`: the world's territories, one row per LOC type 12 ID.

    PABR | u32 count | count x row (88 + 4 x list_count bytes) | string table
    | u32 string_table_start | u32 0

Rows are byte-packed and grow by one u32 per entry of a short trailing list,
so they are walked in order and must end exactly where the string table
starts. Full layout in docs/file-formats/territoryinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import checked_string_table_start, read_string_table, string_at, string_table_start
from _common.record_reader import RecordReader
from _common.ui_texture import ui_texture_path


_HEADER_SIZE = 8

# u16 territory_key | u8 unknown_02 | u8 is_autonomous | 3 x f32 vec3 position
_HEAD = struct.Struct("<HBB9f")
# u32 nation_hash | nation_ref | name_ref | icon_large_ref | icon_small_ref
# | unknown_3c | unknown_40 | crown_item_id | armor_item_id | list_count | unknown_50
_BODY = struct.Struct("<11I")
_U32 = struct.Struct("<I")

_AXES = 3


def _rows_end(data: bytes) -> int:
    """Where the rows stop. Raises ValueError on a bad magic or trailer."""
    return checked_string_table_start(data, "territoryinfo.bss")


def _positions(coords: list[float]) -> list[list[float]]:
    """The three stored vec3 values as `[x, y, z]`, in file order."""
    return [coords[i : i + _AXES] for i in range(0, len(coords), _AXES)]


def _read_row(reader: RecordReader, strings: list[str]) -> dict:
    key, unknown_02, is_autonomous, *coords = reader.unpack(_HEAD)
    (
        nation_hash, nation_ref, name_ref, icon_large_ref, icon_small_ref,
        unknown_3c, unknown_40, crown_item_id, armor_item_id, list_count, unknown_50,
    ) = reader.unpack(_BODY)
    unknown_54 = [reader.unpack(_U32)[0] for _ in range(list_count)]
    (unknown_tail,) = reader.unpack(_U32)
    return {
        "territory_key": key,
        "nation_kr": string_at(strings, nation_ref),
        "name_kr": string_at(strings, name_ref),
        "is_autonomous": bool(is_autonomous),
        "positions": _positions(coords),
        "nation_hash": nation_hash,
        "icon_large_path": ui_texture_path(string_at(strings, icon_large_ref)),
        "icon_small_path": ui_texture_path(string_at(strings, icon_small_ref)),
        "crown_item_id": crown_item_id,
        "armor_item_id": armor_item_id,
        "unknown_02": unknown_02,
        "unknown_3c": unknown_3c,
        "unknown_40": unknown_40,
        "unknown_50": unknown_50,
        "unknown_54": unknown_54,
        "unknown_tail": unknown_tail,
    }


def parse_territoryinfo_records(data: bytes) -> list[dict]:
    """Every territory row in file order, with its strings resolved.

    Raises ValueError on a bad magic, when a row runs past the string table,
    or when the declared rows do not end exactly where it starts: then the row
    layout has changed and every field is suspect.
    """
    end = _rows_end(data)
    strings = read_string_table(data)
    reader = RecordReader(data, _HEADER_SIZE, end, "territoryinfo.bss rows")
    records = [_read_row(reader, strings) for _ in range(u32(data, 4))]
    if not reader.at_end():
        raise ValueError(
            f"territoryinfo.bss rows end at 0x{reader.pos:X} but its string "
            f"table starts at 0x{end:X}"
        )
    return records
