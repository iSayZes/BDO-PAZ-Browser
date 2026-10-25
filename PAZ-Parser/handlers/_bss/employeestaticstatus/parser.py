"""`employeestaticstatus.bss`: sailor and First Mate rows, one per level.

    PABR | u32 sailor_count | sailor_count x 130-byte row
    | u32 first_mate_count | first_mate_count x 130-byte row
    | 64-byte block | string table | u32 string_table_start | u32 0

Each row is one employee key at one level, with 19 (ability type, value)
slots and the character whose name, title and icon the sailor uses. Full
layout in docs/file-formats/bss/employeestaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import TRAILER_SIZE, check_rows_end, read_string_table, string_at, string_table_start


_MAGIC = b"PABR"
_COUNT_SIZE = 4
_LIST_COUNT = 2
# The block between the second list and the string table; its fields are not decoded.
_UNKNOWN_BLOCK_SIZE = 64

# u8 job | u16 level | u16 employee_key | 19 x (u8 ability type | u32 value)
_ROW_HEAD = struct.Struct("<BHH")
_ABILITY = struct.Struct("<BI")
_ABILITY_SLOTS = 19
# u32 weight | u32 cabin_cost | u32 appetite | u32 max_condition | u32 unknown_74
# | u32 icon_index | u16 character_id | u16 employee_key | u16 padding
_ROW_TAIL = struct.Struct("<IIIIIIHHH")
_ROW_SIZE = 130
_TAIL_OFFSET = _ROW_HEAD.size + _ABILITY_SLOTS * _ABILITY.size
assert _TAIL_OFFSET + _ROW_TAIL.size == _ROW_SIZE

# Three of the 19 slots carry this type, one past the highest used type, with value 0.
_UNUSED_ABILITY_TYPE = 19

# Ability types with a name in the Manage Sailors window, in the window's order
# (PANEL_SAILORMANAGER_SPEED to _SIGHT). Values are percent x 10,000.
STAT_FIELDS: dict[int, str] = {
    6: "endurance",
    7: "wits",
    8: "awareness",
    9: "strength",
    13: "patience",
    14: "focus",
    15: "force",
    16: "vision",
}


def _abilities(data: bytes, row_at: int) -> list[tuple[int, int]]:
    """Non-zero `(type, value)` pairs in slot order; unused and zero slots are left out."""
    pairs: list[tuple[int, int]] = []
    for slot in range(_ABILITY_SLOTS):
        kind, value = _ABILITY.unpack_from(data, row_at + _ROW_HEAD.size + slot * _ABILITY.size)
        if kind != _UNUSED_ABILITY_TYPE and value:
            pairs.append((kind, value))
    return pairs


def _pairs_text(pairs: list[tuple[int, int]]) -> str:
    return ", ".join(f"{kind}: {value}" for kind, value in pairs)


def _ability_fields(pairs: list[tuple[int, int]]) -> dict:
    """One field per named stat (0 when the row lacks it), plus the raw text of all and of the unnamed types.

    `abilities` keeps every pair for export; `other_abilities` holds the types
    without a column, such as the First Mate skills 17 and 18.
    """
    values = dict(pairs)
    return {
        **{field: values.get(kind, 0) for kind, field in STAT_FIELDS.items()},
        "abilities": _pairs_text(pairs),
        "other_abilities": _pairs_text([(kind, value) for kind, value in pairs if kind not in STAT_FIELDS]),
    }


def _parse_row(data: bytes, row_at: int, strings: list[str]) -> dict:
    job, level, employee_key = _ROW_HEAD.unpack_from(data, row_at)
    (
        weight, cabin_cost, appetite, max_condition, unknown_74,
        icon_index, character_id, tail_employee_key, _padding,
    ) = _ROW_TAIL.unpack_from(data, row_at + _TAIL_OFFSET)
    if tail_employee_key != employee_key:
        raise ValueError(
            f"employeestaticstatus.bss row at 0x{row_at:X} repeats key "
            f"{tail_employee_key}, expected {employee_key}"
        )
    return {
        "employee_key": employee_key,
        "level": level,
        "job": job,
        "character_id": character_id,
        "icon_index": icon_index,
        "icon_path": string_at(strings, icon_index),
        **_ability_fields(_abilities(data, row_at)),
        "weight": weight,
        "cabin_cost": cabin_cost,
        "appetite": appetite,
        "max_condition": max_condition,
        "unknown_74": unknown_74,
    }


def parse_employeestaticstatus_records(data: bytes) -> list[dict]:
    """Every row of both lists in file order, icons resolved.

    Raises ValueError on a bad magic, or when the lists plus the 64-byte block
    do not end where the string table starts: then the row size has changed
    and every field is suspect.
    """
    if len(data) < len(_MAGIC) + _COUNT_SIZE + TRAILER_SIZE or data[:4] != _MAGIC:
        raise ValueError("employeestaticstatus.bss has invalid magic.")

    strings = read_string_table(data)
    records: list[dict] = []
    pos = len(_MAGIC)
    for _ in range(_LIST_COUNT):
        count = u32(data, pos)
        pos += _COUNT_SIZE
        rows_end = pos + count * _ROW_SIZE
        if rows_end > len(data):
            raise ValueError(f"employeestaticstatus.bss declares {count} rows past the end of the file")
        records.extend(_parse_row(data, row_at, strings) for row_at in range(pos, rows_end, _ROW_SIZE))
        pos = rows_end

    check_rows_end(data, pos + _UNKNOWN_BLOCK_SIZE, "employeestaticstatus.bss rows")
    return records
