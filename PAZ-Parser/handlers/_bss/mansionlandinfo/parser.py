"""`mansionlandinfo.bss`: the rentable manors, one 93-byte row per manor land.

    PABR | u32 count | count x row | string table | u32 table_start | u32 0
    row: u16 land_character_key | u16 building_character_key | u16 need_point
         | u16 region_key | i32[3] sector_start | i32[3] sector_end
         | i32[3] unknown_20 | i32[3] unknown_2c
         | u16 condition_quest_chain_id | u16 condition_quest_id | u32 day_pay
         | f32 unknown_40 | f32 unknown_44 | f32 unknown_48 | f32 unknown_4c
         | u8 unknown_50 | f32[3] unknown_51

Full layout in docs/file-formats/mansionlandinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import whole_float
from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "mansionlandinfo.bss"

_ROW = struct.Struct("<HHHH3i3i3i3iHHIffffB3f")
_ROW_SIZE = 93
assert _ROW.size == _ROW_SIZE


def _floats(values: tuple[float, ...]) -> list[float | int]:
    return [whole_float(value) for value in values]


def _record(values: tuple) -> dict:
    land, building, need_point, region_key = values[0:4]
    sector_start, sector_end, unknown_20, unknown_2c = (list(values[i : i + 3]) for i in range(4, 16, 3))
    quest_chain_id, quest_id, day_pay = values[16:19]
    unknown_40, unknown_44, unknown_48, unknown_4c, unknown_50 = values[19:24]
    return {
        "land_character_key": land,
        "building_character_key": building,
        "need_point": need_point,
        "region_key": region_key,
        "sector_start": sector_start,
        "sector_end": sector_end,
        "unknown_20": unknown_20,
        "unknown_2c": unknown_2c,
        "condition_quest_chain_id": quest_chain_id,
        "condition_quest_id": quest_id,
        "day_pay": day_pay,
        "unknown_40": whole_float(unknown_40),
        "unknown_44": whole_float(unknown_44),
        "unknown_48": whole_float(unknown_48),
        "unknown_4c": whole_float(unknown_4c),
        "unknown_50": unknown_50,
        "unknown_51": _floats(values[24:27]),
    }


def parse_mansionlandinfo_records(data: bytes) -> list[dict]:
    """Every manor land row in file order.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    return [_record(_ROW.unpack_from(data, offset)) for offset in fixed_row_offsets(data, _ROW_SIZE, FILE_NAME)]
