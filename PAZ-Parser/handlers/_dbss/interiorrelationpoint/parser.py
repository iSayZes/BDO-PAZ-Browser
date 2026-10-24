"""`interiorrelationpoint.dbss`: the placement points of each furniture character.

    PABR | u32 count | count x row | u32 string_count (0) | u32 table_start | u32 0
    row: u16 character_key | u16 character_key_dup | u16 matching_character_key
         | i32 matching_character_point | 14 x i32 relation points

The 14 relation points are, in order, the `RELATION_FIELDS` below.
`interiorrelationpointoffset.dbss` (PABR, u16 key, offset, size 0) points 2
bytes into a row, at `character_key_dup`. Layout 1 in
docs/file-formats/interiorrelationpoint_dbss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import PabrOffsetRow, parse_pabr_offset_rows
from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "interiorrelationpoint.dbss"
OFFSET_FILE = "interiorrelationpointoffset.dbss"
KEY_FIELD = "character_key"

# The relation points in file order: the columns of the InteriorRelationPoint_Table sheet.
RELATION_FIELDS = (
    "on_dresser",
    "on_bed_side_cabinet",
    "on_wardrobe",
    "on_dining_table",
    "on_table",
    "on_chair",
    "on_sofa",
    "on_bed",
    "on_book_case",
    "on_shelf",
    "is_empty_in_front",
    "is_empty_in_back",
    "is_empty_in_left",
    "is_empty_in_right",
)
_FIELDS = (KEY_FIELD, "character_key_dup", "matching_character_key", "matching_character_point", *RELATION_FIELDS)
_ROW = struct.Struct(f"<HHHi{len(RELATION_FIELDS)}i")


def parse_interiorrelationpoint_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a missing magic or rows that do not end where the
    string table starts.
    """
    return [
        dict(zip(_FIELDS, _ROW.unpack_from(data, start), strict=True))
        for start in fixed_row_offsets(data, _ROW.size, FILE_NAME)
    ]


def parse_interiorrelationpointoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row. Raises ValueError on a missing magic or a count the file cannot hold."""
    return parse_pabr_offset_rows(data)
