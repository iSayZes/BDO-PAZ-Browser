"""`yachthandrank.bss`: the hand ranks (scoring combinations) of Yar!.

    PABR | u32 count | count x 49-byte row | string table | u32 string_table_start | u32 0

    row: u32 hand_rank_key | bytes[9] unknown_04 | u32 unknown_0d | bytes[4] unknown_11
         | u8 target_eye | u32 target_count | u32 straight_count | u8 is_full_house
         | u8 is_two_pair | u32 made_point | u8 is_sum_point
         | u32 icon_texture_index | u32 name_kr_index | u32 desc_kr_index

The three indexes point into the string table. Layout in
docs/file-formats/yachthandrank_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at


FILE_NAME = "yachthandrank.bss"

_ROW = struct.Struct("<I9sI4sBIIBBIBIII")


def parse_yachthandrank_records(data: bytes) -> list[dict]:
    """Every hand rank in file order, its strings read from the string table.

    Raises ValueError on a bad magic, rows that do not end where the string
    table starts, or a string that runs past the table.
    """
    starts = fixed_row_offsets(data, _ROW.size, FILE_NAME)
    strings = read_string_table(data)
    records: list[dict] = []
    for start in starts:
        (
            key, unknown_04, unknown_0d, unknown_11, target_eye, target_count, straight_count,
            is_full_house, is_two_pair, made_point, is_sum_point,
            icon_texture_index, name_kr_index, desc_kr_index,
        ) = _ROW.unpack_from(data, start)
        records.append({
            "hand_rank_key": key,
            "unknown_04": unknown_04.hex(),
            "unknown_0d": unknown_0d,
            "unknown_11": unknown_11.hex(),
            "target_eye": target_eye,
            "target_count": target_count,
            "straight_count": straight_count,
            "is_full_house": is_full_house,
            "is_two_pair": is_two_pair,
            "made_point": made_point,
            "is_sum_point": is_sum_point,
            "icon_texture_index": icon_texture_index,
            "icon_texture": string_at(strings, icon_texture_index),
            "name_kr_index": name_kr_index,
            "name_kr": string_at(strings, name_kr_index),
            "desc_kr_index": desc_kr_index,
            "desc_kr": string_at(strings, desc_kr_index),
        })
    return records
