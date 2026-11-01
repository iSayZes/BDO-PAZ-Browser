"""`servantexperience.dbss`: one record per servant (mount or ship) and level.

`servantexperienceoffset.dbss` keys each record by `level << 16 | character_id`
and points at its first byte. A record is a fixed head with the
`experience.bss` stat body from `+0x0A`, three inline `1D1` strings, six
level-up dice strings and a zero tail. Layout in
docs/file-formats/dbss/servantexperience_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32, whole_float
from _common.pabr_offset import PabrOffsetRow, parse_bare_u32_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "servantexperience.dbss"
OFFSET_FILE = "servantexperienceoffset.dbss"

_KEY_LEVEL_SHIFT = 16
_KEY_ID_MASK = 0xFFFF
# character_id, level (i32, as the 2016 _level), exp.
_HEAD = struct.Struct("<HiQ")
# The stat body fields, read in order from +0x0E. Every skipped byte is 0 on
# client 3464.
_F32 = struct.Struct("<f")
_U32 = struct.Struct("<I")
_I64 = struct.Struct("<q")  # +0x52 max_weight, the possessableWeight column
_HP_MP = struct.Struct("<fI")  # +0x0E max_hp, +0x12 max_mp
# +0x42 MaxCriticalRate, MaxDropItemLuck, MaxFishingLuck, MaxCollectionLuck.
_MAX_LUCKS = struct.Struct("<4I")
_MAX_VARIED_SPEED = struct.Struct("<3I")  # +0x6E MaxAttackSpeed, MaxMoveSpeed, MaxCastingSpeed
_STATS = struct.Struct("<8I")  # +0x8A stats, by ServantStatType
_GAP_TO_2A = 20
_GAP_TO_42 = 20
_GAP_TO_6E = 16
_GAP_TO_8A = 12
_BODY_STRING_COUNT = 3
_MIDDLE_RESERVED_SIZE = 48
_DICE_COUNT = 6
_TAIL_RESERVED_SIZE = 32
_MOVE_STAT_COUNT = 4
_HP_DICE_SLOT = 0
_STAMINA_DICE_SLOT = 1
_MOVE_DICE_SLOTS = slice(2, 6)


def split_servant_key(key: int) -> tuple[int, int]:
    """`(character_id, level)` of an offset key."""
    return key & _KEY_ID_MASK, key >> _KEY_LEVEL_SHIFT


def parse_servantexperience_offset_records(data: bytes) -> list[dict]:
    """One dict per `servantexperienceoffset.dbss` row, in file order."""
    return [_offset_record(row) for row in parse_bare_u32_offset_rows(data)]


def _offset_record(row: PabrOffsetRow) -> dict:
    character_id, level = split_servant_key(row.entry_id)
    return {
        "servant_key": row.entry_id,
        "character_id": character_id,
        "level": level,
        "offset": row.offset,
        "size": row.size,
    }


def parse_servantexperience_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Every level record, in file order.

    Raises ValueError when the counts disagree, a record runs past its size or
    the file, or its first bytes do not repeat its offset key.
    """
    rows = sorted(parse_bare_u32_offset_rows(offset_data), key=lambda row: row.offset)
    if len(data) < _U32.size or u32(data, 0) != len(rows):
        raise ValueError(f"{FILE_NAME} count does not match the {len(rows):,} rows of {OFFSET_FILE}")
    return [_parse_record(data, row) for row in rows]


def _parse_record(data: bytes, row: PabrOffsetRow) -> dict:
    character_id, level = split_servant_key(row.entry_id)
    label = f"servant {character_id} level {level}"
    reader = RecordReader(data, row.offset, row.offset + row.size, label)
    head_id, head_level, exp = reader.unpack(_HEAD)
    if (head_id, head_level) != (character_id, level):
        raise ValueError(f"{label} record starts with servant {head_id} level {head_level}")

    max_hp, max_mp = reader.unpack(_HP_MP)
    reader.skip(_GAP_TO_2A)
    (unknown_2a,) = reader.unpack(_F32)
    reader.skip(_GAP_TO_42)
    max_critical_rate, max_drop_item_luck, max_fishing_luck, max_collection_luck = reader.unpack(_MAX_LUCKS)
    (max_weight,) = reader.unpack(_I64)
    (unknown_5a,) = reader.unpack(_F32)
    reader.skip(_GAP_TO_6E)
    max_varied_speed = list(reader.unpack(_MAX_VARIED_SPEED))
    (unknown_7a,) = reader.unpack(_F32)
    reader.skip(_GAP_TO_8A)
    stats = list(reader.unpack(_STATS))

    body_strings: list[str] = []
    body_values: list[int] = []
    for _ in range(_BODY_STRING_COUNT):
        body_strings.append(reader.text(wide=True))
        body_values.append(reader.unpack(_U32)[0])
    reader.skip(_MIDDLE_RESERVED_SIZE)
    growth_dice = [reader.text(wide=True) for _ in range(_DICE_COUNT)]
    reader.skip(_TAIL_RESERVED_SIZE)
    if not reader.at_end():
        raise ValueError(f"{label} has {reader.remaining()} bytes after its tail")

    return {
        "servant_key": row.entry_id,
        "character_id": character_id,
        "level": level,
        "exp": exp,
        "max_hp": whole_float(max_hp),
        "max_mp": max_mp,
        "max_weight": max_weight,
        "acceleration": stats[0],
        "speed": stats[1],
        "turn": stats[2],
        "brake": stats[3],
        "cannon_stats": stats[_MOVE_STAT_COUNT:],
        "growth_dice": growth_dice,
        "max_critical_rate": max_critical_rate,
        "max_drop_item_luck": max_drop_item_luck,
        "max_fishing_luck": max_fishing_luck,
        "max_collection_luck": max_collection_luck,
        "max_varied_speed": max_varied_speed,
        "unknown_2a": whole_float(unknown_2a),
        "unknown_5a": whole_float(unknown_5a),
        "unknown_7a": whole_float(unknown_7a),
        "unknown_aa": body_strings,
        "unknown_aa_values": body_values,
    }


def hp_dice(growth_dice: list[str]) -> str:
    return growth_dice[_HP_DICE_SLOT]


def stamina_dice(growth_dice: list[str]) -> str:
    return growth_dice[_STAMINA_DICE_SLOT]


def move_dice(growth_dice: list[str]) -> str:
    """The movement die, or the four joined when they differ."""
    dice = growth_dice[_MOVE_DICE_SLOTS]
    return dice[0] if len(set(dice)) == 1 else ", ".join(dice)
