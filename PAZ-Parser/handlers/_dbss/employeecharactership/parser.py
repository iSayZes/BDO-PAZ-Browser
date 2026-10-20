"""`employeecharactership.dbss`: ship settings per boat character.

A u32 row count, then rows back to back to the end of the file: the u16
character key, sailor limit and positions, rations, the cannon setup, the
ration and cannonball recovery prices, the restoration cost, 8 unknown
bytes, the cannon and ship skill flags, the manual cannon fire values and a
u64-prefixed UTF-16 condition script. `employeecharactershipoffset.dbss`
points at each row start, so the walk from the start needs no index.
Layout 2 in docs/file-formats/employeecharactership_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_offset import parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "employeecharactership.dbss"
OFFSET_FILE = "employeecharactershipoffset.dbss"

_COUNT_SIZE = 4
# The 68 fixed bytes from character_key to manual_cannon_fire_decrease_cool_time.
_FIXED = struct.Struct("<HIIIIfffIIBBBfBBffffIB")
_FIXED_FIELDS = (
    "character_key",
    "employee_max",
    "employee_spawn_count",
    "food_max",
    "ocean_ship_cannon_setup",
    "ship_food_recovery",
    "ship_cannon_recovery",
    "damage_diagram_restoration_cost",
    "unknown_1e",
    "unknown_22",
    "is_summon_full",
    "new_cannon_ship_ui",
    "new_cannon_count",
    "new_cannon_speed",
    "ocean_ship_skill_ui",
    "manual_cannon_fire",
    "manual_cannon_fire_min_length",
    "manual_cannon_fire_max_length",
    "manual_cannon_fire_random_dist",
    "manual_cannon_fire_random_pos",
    "manual_cannon_fire_max_angle",
    "manual_cannon_fire_decrease_cool_time",
)
_FLOAT_FIELDS = frozenset(
    name for name, code in zip(_FIXED_FIELDS, _FIXED.format.lstrip("<")) if code == "f"
)
# f32 values hold at most 7 significant digits; more only shows rounding noise.
_F32_DIGITS = 7


def _f32_value(value: float) -> float:
    """An f32 as the decimal it was written as: 0.6 instead of 0.6000000238418579."""
    return float(f"{value:.{_F32_DIGITS}g}")


def parse_employeecharactership_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when a row runs past the file or the rows do not end
    where the file does.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    pos = _COUNT_SIZE
    records = []
    for _ in range(count):
        reader = RecordReader(data, pos, len(data), f"{FILE_NAME} row at 0x{pos:X}")
        records.append(_read_row(reader))
        pos = reader.pos
    if pos != len(data):
        raise ValueError(f"{FILE_NAME} has {len(data) - pos:,} bytes after its {count:,} rows")
    return records


def _read_row(reader: RecordReader) -> dict:
    fixed = {
        name: _f32_value(value) if name in _FLOAT_FIELDS else value
        for name, value in zip(_FIXED_FIELDS, reader.unpack(_FIXED))
    }
    return {
        **fixed,
        "manual_cannon_fire_decrease_cool_time_condition": reader.text(wide=True),
    }


def parse_employeecharactershipoffset_records(data: bytes) -> list[dict]:
    return [
        {"character_key": row.entry_id, "data_offset": row.offset, "data_size": row.size}
        for row in parse_bare_offset_rows(data)
    ]
