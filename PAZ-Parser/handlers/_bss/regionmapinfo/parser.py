"""`regionmapinfo.bss`: one fixed row per map bitmap (`RegionMap_Table`).

    PABR | u32 count | count x 25-byte row | string table | u32 string_table_start | u32 0

    row: u16 map_index | u8 map_type | u16 map_index_dup
         | i32 sector_start_x, sector_end_y, sector_end_x, sector_start_y
         | u32 image_path_ref

The rectangle is the 2016 `CRect` order (left, top, right, bottom); the
map's Y axis is world Z. `fieldinfo.bss` stores `map_index` in its
`*_map_index` fields. Full layout in docs/file-formats/bss/regionmapinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at

FILE_NAME = "regionmapinfo.bss"
KEY_FIELD = "map_index"

_ROW = struct.Struct("<HBHiiiiI")
ROW_SIZE = 25
assert _ROW.size == ROW_SIZE


def _record(offset: int, values: tuple, strings: list[str]) -> dict:
    map_index, map_type, map_index_dup, start_x, end_y, end_x, start_y, image_ref = values
    if map_index_dup != map_index:
        raise ValueError(f"row at 0x{offset:X} repeats key {map_index} as {map_index_dup}")
    return {
        KEY_FIELD: map_index,
        "map_type": map_type,
        "map_index_dup": map_index_dup,
        "sector_start_x": start_x,
        "sector_end_y": end_y,
        "sector_end_x": end_x,
        "sector_start_y": start_y,
        "image_path": string_at(strings, image_ref),
    }


def parse_regionmapinfo_records(data: bytes) -> list[dict]:
    """Every row in file order (not sorted), the image name resolved to text.

    Raises ValueError on a bad magic, when the rows do not end where the
    string table starts, or when a row's key copy differs from its key.
    """
    offsets = fixed_row_offsets(data, ROW_SIZE, FILE_NAME)
    strings = read_string_table(data)
    return [_record(offset, _ROW.unpack_from(data, offset), strings) for offset in offsets]


def map_images(data: bytes) -> dict[int, str]:
    """Map key -> image file name (`1` -> `RegionMap_New.bmp`)."""
    return {record[KEY_FIELD]: record["image_path"] for record in parse_regionmapinfo_records(data)}
