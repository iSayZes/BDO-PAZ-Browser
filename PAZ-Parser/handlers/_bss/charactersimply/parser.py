"""`charactersimply.bss`: one fixed row per character template.

    PABR | u32 count | count x row | string table | u32 string_table_start | u32 0

Each row repeats a subset of the character's `characterstatic.dbss` fields
in another order and points into the string table for the model path, the
voice bank, the Korean name and title and the two scripts. Rows are 119
bytes in Layout 2 (client 3464 on) and 121 in Layout 1 (clients 1762 to
2553); a file is read with the first layout, in client order, whose rows end
where the string table starts. Full layout in
docs/file-formats/bss/charactersimply_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import whole_float
from _common.client_versions import ClientRange, client_order
from _common.knowledge_script import knowledge_id_of
from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at
from _common.vehicle_type import NO_VEHICLE_TYPE, NO_VEHICLE_TYPE_OLD

FILE_NAME = "charactersimply.bss"

# (record key, struct code) in Layout 2 row order; None skips bytes that are
# always 0. A key ending in `_ref` is a string-table index, stored as the text
# under the key without `_ref`.
_LAYOUT_2_FIELDS: tuple[tuple[str | None, str], ...] = (
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
    # unknown_63
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
# Layout 2 fields that Layout 1 rows do not store; their records hold None.
_LAYOUT_2_ONLY = ("unknown_76",)


def _layout_1_fields() -> tuple[tuple[str | None, str], ...]:
    """Layout 2 with a u32 after model_path_hash, no `unknown_63` after
    steal_drop_id, a zero byte after absolute_interaction and no `unknown_76`."""
    fields: list[tuple[str | None, str]] = []
    for key, code in _LAYOUT_2_FIELDS:
        follows_steal_drop_id = bool(fields) and fields[-1][0] == "steal_drop_id"
        if key in _LAYOUT_2_ONLY or (key is None and follows_steal_drop_id):
            continue
        fields.append((key, code))
        if key == "model_path_hash":
            fields.append(("unknown_after_model_path_hash", "I"))
        elif key == "absolute_interaction":
            fields.append((None, "x"))
    return tuple(fields)


@dataclass(frozen=True)
class RowLayout:
    """One documented Row shape; `number` is its Layout N in the doc."""

    number: int
    row: struct.Struct
    keys: tuple[str, ...]
    # vehicle_type of a character that is not a vehicle (`_common/vehicle_type.py`).
    no_vehicle_type: int
    # Test clients this layout reads (the doc's Versions table, written by
    # check_docs); they only order the tries (`client_versions.py`).
    clients: tuple[ClientRange, ...] = ()


def _row_layout(
    number: int,
    fields: tuple[tuple[str | None, str], ...],
    no_vehicle_type: int,
    clients: tuple[ClientRange, ...],
) -> RowLayout:
    return RowLayout(
        number,
        struct.Struct("<" + "".join(code for _, code in fields)),
        tuple(key for key, _ in fields if key is not None),
        no_vehicle_type,
        clients,
    )


# Newest first.
LAYOUTS = (
    _row_layout(2, _LAYOUT_2_FIELDS, NO_VEHICLE_TYPE, (ClientRange(3464),)),
    _row_layout(1, _layout_1_fields(), NO_VEHICLE_TYPE_OLD, (ClientRange(1762, 2553),)),
)
assert [layout.row.size for layout in LAYOUTS] == [119, 121]

_REF_SUFFIX = "_ref"
_FLOAT_KEYS = frozenset({"body_height", "body_size", "max_hp"})


def _record(values: tuple, strings: list[str], layout: RowLayout) -> dict:
    record: dict = dict.fromkeys(_LAYOUT_2_ONLY)
    for key, value in zip(layout.keys, values):
        if key.endswith(_REF_SUFFIX):
            record[key.removesuffix(_REF_SUFFIX)] = string_at(strings, value)
        elif key in _FLOAT_KEYS:
            record[key] = whole_float(value)
        else:
            record[key] = value
    # None where the layout's value means "not a vehicle".
    if record["vehicle_type"] == layout.no_vehicle_type:
        record["vehicle_type"] = None
    record["knowledge_id"] = knowledge_id_of(record["action_script"])
    return record


def _layout_offsets(data: bytes) -> tuple[RowLayout, range]:
    """The first layout, in client order, whose rows end where the string table starts."""
    breaks: list[str] = []
    for layout in client_order(LAYOUTS, lambda layout: layout.clients):
        try:
            return layout, fixed_row_offsets(data, layout.row.size, FILE_NAME)
        except ValueError as error:
            breaks.append(f"Layout {layout.number}: {error}")
    raise ValueError(f"{FILE_NAME} fits no known layout ({'; '.join(breaks)})")


def parse_charactersimply_records(data: bytes) -> list[dict]:
    """Every row in file order, its string-table indexes resolved to text.

    Raises ValueError on a bad magic, or when no layout's rows end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    layout, offsets = _layout_offsets(data)
    strings = read_string_table(data)
    return [_record(layout.row.unpack_from(data, offset), strings, layout) for offset in offsets]
