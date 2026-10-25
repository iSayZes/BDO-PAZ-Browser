"""`charactersimply.bss`: one fixed row per character template.

    PABR | u32 count | count x 119-byte row | string table | u32 string_table_start | u32 0

Each row repeats a subset of the character's `characterstatic.dbss` fields
in another order and points into the string table for the model path, the
voice bank, the Korean name and title and the two scripts. Full layout in
docs/file-formats/bss/charactersimply_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import whole_float
from _common.knowledge_script import knowledge_id_of
from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at

# (record key, struct code) in row order; None skips bytes that are always 0.
# A key ending in `_ref` is a string-table index, stored as the text under
# the key without `_ref`.
_FIELDS: tuple[tuple[str | None, str], ...] = (
    ("character_id", "H"),
    ("is_giant", "B"),
    ("spawn_start_hour", "h"),
    ("spawn_end_hour", "h"),
    ("is_fixed", "B"),
    ("collect_drop_id", "H"),
    ("unknown_0a", "B"),
    ("unknown_0b", "B"),
    ("is_client_ai", "B"),
    ("model_path_ref", "I"),
    ("model_path_hash", "I"),
    ("npc_kind", "B"),
    ("class_type", "B"),
    ("body_height", "f"),
    ("body_size", "f"),
    ("max_hp", "f"),
    ("attribute_type_mask", "Q"),
    ("unknown_2b", "B"),
    ("unknown_2c", "B"),
    ("is_tamable", "B"),
    ("is_opti_monster", "B"),
    (None, "3x"),
    ("is_render_shadow", "B"),
    ("use_default_audio", "B"),
    ("voice_bank_ref", "I"),
    ("unknown_38", "B"),
    ("is_carrier", "B"),
    ("vehicle_type", "B"),
    ("team_no", "h"),
    ("unknown_3d", "B"),
    ("is_hidden_name", "B"),
    ("is_live_collect", "i"),
    ("unknown_43", "B"),
    ("name_kr_ref", "I"),
    ("title_kr_ref", "I"),
    ("unknown_4c", "B"),
    ("grade", "B"),
    ("is_hidden_hp", "B"),
    ("level", "I"),
    ("character_group", "h"),
    ("fusion_group_key", "I"),
    ("unknown_59", "B"),
    ("unknown_5a", "B"),
    ("unknown_5b", "B"),
    ("unknown_5c", "B"),
    ("action_script_ref", "I"),
    ("steal_drop_id", "H"),
    (None, "2x"),
    ("inventory_max", "B"),
    ("absolute_interaction", "B"),
    ("is_attacked_pvp_mode_only", "B"),
    ("vehicle_driver_ridable", "B"),
    ("vehicle_seat_count", "B"),
    ("condition_script_ref", "I"),
    ("vehicle_sub_type", "B"),
    ("is_guild_vehicle", "B"),
    ("unknown_70", "B"),
    ("carriage_type", "B"),
    (None, "4x"),
    ("unknown_76", "B"),
)
_ROW = struct.Struct("<" + "".join(code for _, code in _FIELDS))
_KEYS = tuple(key for key, _ in _FIELDS if key is not None)
ROW_SIZE = 119
assert _ROW.size == ROW_SIZE

_REF_SUFFIX = "_ref"
_FLOAT_KEYS = frozenset({"body_height", "body_size", "max_hp"})


def _record(values: tuple, strings: list[str]) -> dict:
    record: dict = {}
    for key, value in zip(_KEYS, values):
        if key.endswith(_REF_SUFFIX):
            record[key.removesuffix(_REF_SUFFIX)] = string_at(strings, value)
        elif key in _FLOAT_KEYS:
            record[key] = whole_float(value)
        else:
            record[key] = value
    record["knowledge_id"] = knowledge_id_of(record["action_script"])
    return record


def parse_charactersimply_records(data: bytes) -> list[dict]:
    """Every row in file order, its string-table indexes resolved to text.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    offsets = fixed_row_offsets(data, ROW_SIZE, "charactersimply.bss")
    strings = read_string_table(data)
    return [_record(_ROW.unpack_from(data, offset), strings) for offset in offsets]
