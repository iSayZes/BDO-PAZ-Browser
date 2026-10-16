"""`blizzardregioninfo.bss`: the snow regions of the Mountain of Eternal Winter and Ulukita.

    PABR | u32 count | count x 26-byte row | u32 0 (empty string table)
    | u32 string_table_start | u32 0

Each row joins one `regioninfo.bss` region by its region key and holds the
blizzard effect's spawn chance range (1,000,000 = 100%) and a wind vector.
Full layout in docs/file-formats/blizzardregioninfo_bss.md.
"""

from __future__ import annotations

from _common.binary import f32, u16, u32
from _common.pabr_strings import fixed_row_offsets, string_table_start


ROW_SIZE = 26

# Row field offsets.
_KEY = 0x00
_REGION_KEY = 0x04
_EFFECT_SPAWN_PERCENT_MIN = 0x06
_EFFECT_SPAWN_PERCENT_MAX = 0x0A
_WIND_X = 0x0E
_WIND_Y = 0x12
_WIND_Z = 0x16


def _parse_row(data: bytes, pos: int) -> dict:
    return {
        "key": u32(data, pos + _KEY),
        "region_key": u16(data, pos + _REGION_KEY),
        "effect_spawn_percent_min": u32(data, pos + _EFFECT_SPAWN_PERCENT_MIN),
        "effect_spawn_percent_max": u32(data, pos + _EFFECT_SPAWN_PERCENT_MAX),
        "wind_x": f32(data, pos + _WIND_X),
        "wind_y": f32(data, pos + _WIND_Y),
        "wind_z": f32(data, pos + _WIND_Z),
    }


def parse_blizzardregioninfo_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a missing magic or a row count that does not end
    where the trailer says the string table starts.
    """
    return [_parse_row(data, pos) for pos in fixed_row_offsets(data, ROW_SIZE, "blizzardregioninfo.bss")]
