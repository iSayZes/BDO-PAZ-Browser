"""`territoryinfo.bss`: the world's territories, one row per LOC type 12 ID.

    PABR | u32 count | count x row (80 bytes + two u64-counted u32 lists)
    | string table | u32 string_table_start | u32 0

Rows are byte-packed and grow with their booty item and territory supply key
lists, so they are walked in order and must end exactly where the string
table starts. Full layout in docs/file-formats/territoryinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader
from _common.ui_texture import ui_texture_path


_HEADER_SIZE = 8

# u16 territory_key | u8 is_king_territory_only | u8 is_lord_territory_only | 3 x f32 vec3 position
_HEAD = struct.Struct("<HBB9f")
# u32 national_key | nation_ref | name_ref | icon_large_ref | icon_small_ref
_REFS = struct.Struct("<5I")
_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")

_AXES = 3
# The three stored vec3 values in file order (Territory_Table column names).
POSITION_FIELDS = (
    "occupying_tent_position",
    "volunteer_attack_position",
    "volunteer_defense_position",
)


def _rows_end(data: bytes) -> int:
    """Where the rows stop. Raises ValueError on a bad magic or trailer."""
    return checked_string_table_start(data, "territoryinfo.bss")


def _positions(coords: list[float]) -> dict[str, list[float]]:
    """Each stored vec3 value as `[x, y, z]` under its field name."""
    return {
        field: coords[i * _AXES : (i + 1) * _AXES]
        for i, field in enumerate(POSITION_FIELDS)
    }


def _u32_list(reader: RecordReader) -> list[int]:
    """A u64 count, then that many u32 values."""
    (count,) = reader.unpack(_U64)
    if count * _U32.size > reader.remaining():
        raise ValueError(f"territoryinfo.bss list of {count} runs past its row at 0x{reader.pos:X}")
    return list(reader.unpack(struct.Struct(f"<{count}I")))


def _read_row(reader: RecordReader, strings: list[str]) -> dict:
    key, is_king_territory_only, is_lord_territory_only, *coords = reader.unpack(_HEAD)
    national_key, nation_ref, name_ref, icon_large_ref, icon_small_ref = reader.unpack(_REFS)
    booty_item_ids = _u32_list(reader)
    territory_supply_keys = _u32_list(reader)
    (unknown_tail,) = reader.unpack(_U32)
    return {
        "territory_key": key,
        "nation_kr": string_at(strings, nation_ref),
        "name_kr": string_at(strings, name_ref),
        "is_king_territory_only": bool(is_king_territory_only),
        "is_lord_territory_only": bool(is_lord_territory_only),
        **_positions(coords),
        "national_key": national_key,
        "icon_large_path": ui_texture_path(string_at(strings, icon_large_ref)),
        "icon_small_path": ui_texture_path(string_at(strings, icon_small_ref)),
        "booty_item_ids": booty_item_ids,
        "territory_supply_keys": territory_supply_keys,
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
