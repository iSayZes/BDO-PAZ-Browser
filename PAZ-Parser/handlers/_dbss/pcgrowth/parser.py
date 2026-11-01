"""`pcgrowth.dbss`: the class selection record of every class type.

The main file is a u32 count and one variable-length row per class type, each
after a u8 copy of its class type (Layout 2 shown):

    u8 class_type | u16 character_key | u16 background, alter ego and worker
    character keys | u32 unknown_09 | u8 unknown_0d
    | u32 starter_count | u32 starter_weapons[starter_count]
    | 99-byte setup block | u64-prefixed UTF-16 name_kr, description_kr,
    select_movie | u8 gender | 4 x u64-prefixed ASCII consume_actions
    | presentation block (u8 is_open, start angles, life skill pairs)
    | 2 x (u32 count | count x (u8 slot | u64-prefixed ASCII model path))

Layout 1 (clients 1759 to 1862) has no `unknown_09`, a 63-byte setup block
(one start position instead of four) and no `unknown_37` in the presentation
block. Nothing in the file names its layout, so it is read with the first
layout, in client order, that reads every row.

`pcgrowthoffset.dbss` is a bare offset table of 9-byte
[u8 class_type][u32 offset][u32 size] rows; the offset points just past the
u8 copy. Full layout in docs/file-formats/dbss/pcgrowth_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.client_versions import ClientRange, client_order
from _common.pabr_offset import parse_bare_u8_offset_rows
from _common.record_reader import RecordReader


# Each offset points just past a u8 copy of the class type.
_KEY_PREFIX_SIZE = 1
_KEYS = struct.Struct("<BHHHH")
_KEY_FIELDS = (
    "class_type",
    "character_key",
    "background_character_key",
    "alterego_character_key",
    "worker_character_key",
)
_U8 = struct.Struct("<B")
_U32 = struct.Struct("<I")
_CONSUME_ACTION_COUNT = 4
# f32[3] combo_color | f32[3] awaken_combo_color | u8 combat_type
# | u32 class_weapons[3] | u8 is_open | u8 unknown_26
# | f32[3] start_character_angle | f32 start_character_angle_y
_PRESENTATION_HEAD = struct.Struct("<3f3fB3IBB3ff")
_COLOR_SCALE = 255


@dataclass(frozen=True)
class PcGrowthLayout:
    """One documented Class Record shape; `number` is its Layout N in the doc."""

    number: int
    # Layout 2 only: u32 unknown_09 after the worker character key.
    has_unknown_09: bool
    # The setup block, and in it the u8 combat_resource_type.
    setup_size: int
    combat_resource_type: int
    # Layout 2 only: u32 unknown_37 after the start angles.
    has_unknown_37: bool
    # Test clients this layout reads (the doc's Versions table, written by
    # check_docs); they only order the tries (`client_versions.py`).
    clients: tuple[ClientRange, ...] = ()


# Newest first.
LAYOUTS = (
    PcGrowthLayout(
        2, has_unknown_09=True, setup_size=99, combat_resource_type=0x5E, has_unknown_37=True,
        clients=(ClientRange(3314),),
    ),
    PcGrowthLayout(
        1, has_unknown_09=False, setup_size=63, combat_resource_type=0x3A, has_unknown_37=False,
        clients=(ClientRange(1759, 1862),),
    ),
)


def parse_pcgrowthoffset_records(data: bytes) -> list[dict]:
    return [
        {"class_type": row.entry_id, "data_offset": row.offset, "data_size": row.size}
        for row in parse_bare_u8_offset_rows(data)
    ]


def _u32_list(reader: RecordReader) -> tuple[int, ...]:
    (count,) = reader.unpack(_U32)
    return reader.unpack(struct.Struct(f"<{count}I"))


def _model_paths(reader: RecordReader) -> list[str]:
    (count,) = reader.unpack(_U32)
    paths: list[str] = []
    for _ in range(count):
        reader.skip(_U8.size)  # slot 1, 2, 3: main, sub, awakening
        paths.append(reader.text(wide=False))
    return paths


def _rgb_hex(channels: tuple[float, ...]) -> str:
    """Three 0.0 to 1.0 channels as `rrggbb`."""
    return bytes(round(channel * _COLOR_SCALE) for channel in channels).hex()


def _presentation(reader: RecordReader, layout: PcGrowthLayout) -> dict:
    values = reader.unpack(_PRESENTATION_HEAD)
    combo, awaken_combo = values[0:3], values[3:6]
    combat_type, main, sub, awakening, is_open = values[6:11]
    if layout.has_unknown_37:
        reader.skip(_U32.size)
    _u32_list(reader)  # unknown_list, empty on every client read
    (pair_count,) = reader.unpack(_U32)
    pairs = reader.unpack(struct.Struct(f"<{2 * pair_count}I"))
    reader.skip(_U32.size)  # unknown_end
    return {
        "combo_color": _rgb_hex(combo),
        "awaken_combo_color": _rgb_hex(awaken_combo),
        "combat_type": combat_type,
        "class_weapons": [main, sub, awakening],
        "is_open": bool(is_open),
        # (life skill, level): the sheet's DefaultLifeType and DefaultLifeLevel.
        "default_life_skills": [tuple(pairs[index : index + 2]) for index in range(0, len(pairs), 2)],
    }


def _class_record(data: bytes, offset_row: dict, layout: PcGrowthLayout) -> dict:
    start = offset_row["data_offset"]
    label = f"class type {offset_row['class_type']}"
    if start < _KEY_PREFIX_SIZE or data[start - _KEY_PREFIX_SIZE] != offset_row["class_type"]:
        raise ValueError(f"{label}: no class type copy before 0x{start:X}")
    reader = RecordReader(data, start, start + offset_row["data_size"], label)

    keys = dict(zip(_KEY_FIELDS, reader.unpack(_KEYS)))
    if keys["class_type"] != offset_row["class_type"]:
        raise ValueError(f"{label}: row holds class type {keys['class_type']}")
    unknown_09 = reader.unpack(_U32)[0] if layout.has_unknown_09 else None
    (unknown_0d,) = reader.unpack(_U8)
    starter_weapons = list(_u32_list(reader))
    setup = reader.unpack(struct.Struct(f"<{layout.setup_size}s"))[0]
    name_kr = reader.text(wide=True)
    description_kr = reader.text(wide=True)
    select_movie = reader.text(wide=True)
    (gender,) = reader.unpack(_U8)
    consume_actions = [reader.text(wide=False) for _ in range(_CONSUME_ACTION_COUNT)]
    presentation = _presentation(reader, layout)
    weapon_models = _model_paths(reader)
    _model_paths(reader)  # the second list repeats the first on every client read
    if not reader.at_end():
        raise ValueError(f"{label}: {reader.remaining()} bytes left after the row")

    return {
        **keys,
        # None in Layout 1, which does not have it.
        "unknown_09": unknown_09,
        "unknown_0d": unknown_0d,
        "starter_weapons": starter_weapons,
        "combat_resource_type": setup[layout.combat_resource_type],
        "name_kr": name_kr,
        "description_kr": description_kr,
        "select_movie": select_movie,
        "gender": gender,
        "consume_actions": consume_actions,
        **presentation,
        "weapon_models": weapon_models,
    }


def parse_pcgrowth_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Every class row the offset companion points at, in its order, read with
    the first layout (in client order) under which every row ends at its size.

    Raises ValueError, naming where each layout broke, when none fits: a row
    outside the file, a class type other than the offset row's, or a row that
    does not end exactly at its recorded size.
    """
    rows = parse_pcgrowthoffset_records(offset_data)
    breaks: list[str] = []
    for layout in client_order(LAYOUTS, lambda layout: layout.clients):
        try:
            return [_class_record(data, row, layout) for row in rows]
        except ValueError as error:
            breaks.append(f"Layout {layout.number}: {error}")
    raise ValueError(f"pcgrowth.dbss fits no known layout ({'; '.join(breaks)})")
