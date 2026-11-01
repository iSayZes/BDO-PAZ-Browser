"""`fieldinfo.bss`: one fixed row per field (`Field_Table`), the world and its instance copies.

    PABR | u32 count | count x 157-byte row | string table | u32 string_table_start | u32 0

Each row holds the field number that `instancefield.dbss` and
`instancedungeoninfo.dbss` store as `field_no`, string-table indexes for the
field and resource names, a spawn point, the field's sector box in three
units, its type, the keys of the `regionmapinfo.bss` maps it uses and the
entry rules. Full layout in docs/file-formats/bss/fieldinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import whole_float
from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at

# (record key, struct code) in row order. A key ending in `_ref` is a
# string-table index, stored as the text under the key without `_ref`.
_FIELDS: tuple[tuple[str, str], ...] = (
    ("field_no", "H"),
    ("field_name_ref", "I"),
    ("resource_name_ref", "I"),
    ("display_name_ref", "I"),
    ("spawn_x", "f"),
    ("spawn_y", "f"),
    ("spawn_z", "f"),
    ("sector_start_x", "i"),
    ("sector_start_y", "i"),
    ("sector_start_z", "i"),
    ("sector_end_x", "i"),
    ("sector_end_y", "i"),
    ("sector_end_z", "i"),
    ("world_start_x", "f"),
    ("world_start_y", "f"),
    ("world_start_z", "f"),
    ("world_end_x", "f"),
    ("world_end_y", "f"),
    ("world_end_z", "f"),
    ("obstacle_precision", "i"),
    ("server_sector_start_x", "i"),
    ("server_sector_start_y", "i"),
    ("server_sector_start_z", "i"),
    ("server_sector_end_x", "i"),
    ("server_sector_end_y", "i"),
    ("server_sector_end_z", "i"),
    ("field_type", "B"),
    ("region_map_index", "H"),
    ("fishing_map_index", "H"),
    ("water_info_map_index", "H"),
    ("siege_info_map_index", "H"),
    ("village_siege_info_map_index", "H"),
    ("village_siege_info_map_index_new", "H"),
    ("unknown_73", "H"),
    ("underground_map_index", "H"),
    ("audio_map_index", "H"),
    ("is_save_complete", "B"),
    ("field_level", "I"),
    ("is_ridable", "B"),
    ("enter_enable_user_count", "H"),
    ("use_range_spawn", "B"),
    ("use_return_position", "B"),
    ("item_drop_rate", "i"),
    ("bank_no_music", "I"),
    ("bank_no_environment", "I"),
    ("great_sea_map_index", "H"),
    ("horse_race_course_map_index", "H"),
    ("unknown_93", "H"),
    ("unknown_95", "H"),
    ("unknown_97", "H"),
    ("unknown_99", "H"),
    ("unknown_9b", "H"),
)
_ROW = struct.Struct("<" + "".join(code for _, code in _FIELDS))
_KEYS = tuple(key for key, _ in _FIELDS)
ROW_SIZE = 157
assert _ROW.size == ROW_SIZE

_REF_SUFFIX = "_ref"
_FLOAT_KEYS = frozenset(key for key, code in _FIELDS if code == "f")


def _record(values: tuple, strings: list[str]) -> dict:
    record: dict = {}
    for key, value in zip(_KEYS, values):
        if key.endswith(_REF_SUFFIX):
            record[key.removesuffix(_REF_SUFFIX)] = string_at(strings, value)
        elif key in _FLOAT_KEYS:
            record[key] = whole_float(value)
        else:
            record[key] = value
    return record


def parse_fieldinfo_records(data: bytes) -> list[dict]:
    """Every row in file order (not sorted), its string-table indexes resolved to text.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    offsets = fixed_row_offsets(data, ROW_SIZE, "fieldinfo.bss")
    strings = read_string_table(data)
    return [_record(_ROW.unpack_from(data, offset), strings) for offset in offsets]


def build_field_name_index(data: bytes) -> dict[int, str]:
    """FIELD_NAME: field number -> the field's name as the file writes it (`월드`, `A1_001`)."""
    return {record["field_no"]: record["field_name"] for record in parse_fieldinfo_records(data)}
