"""`pcgrowth.dbss`: the class selection record of every class type.

The main file is a u32 count and one variable-length row per class type, each
after a u8 copy of its class type:

    u8 class_type | u16 character_key | 3 x u16 + u32 + u8 unknown
    | u32 starter_count | u32 starter_weapons[starter_count]
    | 99-byte block | u64-prefixed UTF-16 name_kr, description_kr, select_movie
    | u8 gender | 4 x u64-prefixed ASCII consume_actions
    | presentation block (71 bytes + 8 per extra pair)
    | 2 x (u32 count | count x (u8 slot | u64-prefixed ASCII model path))

`pcgrowthoffset.dbss` is a bare offset table of 9-byte
[u8 class_type][u32 offset][u32 size] rows; the offset points just past the
u8 copy. Full layout in docs/file-formats/pcgrowth_dbss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import parse_bare_u8_offset_rows
from _common.record_reader import RecordReader


# Each offset points just past a u8 copy of the class type.
_KEY_PREFIX_SIZE = 1
_HEAD = struct.Struct("<BHHHHIB")
_HEAD_FIELDS = (
    "class_type", "character_key", "unknown_03", "unknown_05", "unknown_07", "unknown_09", "unknown_0d",
)
_U8 = struct.Struct("<B")
_U32 = struct.Struct("<I")
# Same bytes in every row of client 3464 except the u8 at +0x5E.
_SETUP_BLOCK = struct.Struct("<99s")
_SETUP_VARYING = 0x5E
_CONSUME_ACTION_COUNT = 4
# f32[6] | u8 unknown_18 | u32 class_weapons[3] | u16 unknown_25 | f32[6] | u32 pair_count
_PRESENTATION_HEAD = struct.Struct("<24sB3IH24sI")
_PAIR_SIZE = 8


def parse_pcgrowthoffset_records(data: bytes) -> list[dict]:
    return [
        {"class_type": row.entry_id, "data_offset": row.offset, "data_size": row.size}
        for row in parse_bare_u8_offset_rows(data)
    ]


def _model_paths(reader: RecordReader) -> list[str]:
    (count,) = reader.unpack(_U32)
    paths: list[str] = []
    for _ in range(count):
        reader.skip(_U8.size)  # slot 1, 2, 3: main, sub, awakening
        paths.append(reader.text(wide=False))
    return paths


def _presentation(reader: RecordReader) -> dict:
    _, unknown_18, main, sub, awakening, unknown_25, _, pair_count = reader.unpack(_PRESENTATION_HEAD)
    reader.skip(pair_count * _PAIR_SIZE + _U32.size)
    return {
        "unknown_18": unknown_18,
        "class_weapons": [main, sub, awakening],
        "unknown_25": unknown_25,
    }


def _class_record(data: bytes, offset_row: dict) -> dict:
    start = offset_row["data_offset"]
    label = f"class type {offset_row['class_type']}"
    if start < _KEY_PREFIX_SIZE or data[start - _KEY_PREFIX_SIZE] != offset_row["class_type"]:
        raise ValueError(f"{label}: no class type copy before 0x{start:X}")
    reader = RecordReader(data, start, start + offset_row["data_size"], label)

    head = dict(zip(_HEAD_FIELDS, reader.unpack(_HEAD)))
    if head["class_type"] != offset_row["class_type"]:
        raise ValueError(f"{label}: row holds class type {head['class_type']}")
    (starter_count,) = reader.unpack(_U32)
    starter_weapons = [reader.unpack(_U32)[0] for _ in range(starter_count)]
    (setup,) = reader.unpack(_SETUP_BLOCK)
    name_kr = reader.text(wide=True)
    description_kr = reader.text(wide=True)
    select_movie = reader.text(wide=True)
    (gender,) = reader.unpack(_U8)
    consume_actions = [reader.text(wide=False) for _ in range(_CONSUME_ACTION_COUNT)]
    presentation = _presentation(reader)
    weapon_models = _model_paths(reader)
    _model_paths(reader)  # the second list repeats the first on client 3464
    if not reader.at_end():
        raise ValueError(f"{label}: {reader.remaining()} bytes left after the row")

    return {
        **head,
        "starter_weapons": starter_weapons,
        "unknown_5e": setup[_SETUP_VARYING],
        "name_kr": name_kr,
        "description_kr": description_kr,
        "select_movie": select_movie,
        "gender": gender,
        "consume_actions": consume_actions,
        **presentation,
        "weapon_models": weapon_models,
    }


def parse_pcgrowth_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Every class row the offset companion points at, in its order.

    Raises ValueError when a row lies outside the file, holds a class type
    other than the offset row's, or does not end exactly at its recorded size.
    """
    return [_class_record(data, row) for row in parse_pcgrowthoffset_records(offset_data)]
