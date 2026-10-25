"""`cashproductcategory.dbss`: the Pearl Shop category tree (main, middle and small categories).

    str16 all_name_kr | u32 unknown_all_name_kr_00 | u8 unknown_all_name_kr_04
    | u32 count | count x category
    category: u16 category_key | str16 name_kr | u8 is_useable | u8 price_type
              | u8 special_category_type | u8 tag_type | u8 tag_order
              | bytes[3] unknown_name_kr_05 | u32 unique_no | u32 child_count
              | child_count x category | u16 unknown_children_00
              | u32 unknown_children_02

The top-level categories are the main categories (`CppEnums.CashProductCategory`),
their children the middle ones and theirs the small ones.
`cashproductcategoryoffset.dbss` (PABR, u16 main key, u32 offset, u32 size)
points at each main category. Layout 1 in
docs/file-formats/dbss/cashproductcategory_dbss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import PabrOffsetRow, parse_pabr_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "cashproductcategory.dbss"
OFFSET_FILE = "cashproductcategoryoffset.dbss"
KEY_FIELD = "main_key"
# A category level the record does not reach, as the LOC type 51 key writes it.
NO_MIDDLE = 0xFFFF
NO_SMALL = 0xFF
# Main, middle and small: the deepest category level the client 3482 tree has.
MAX_DEPTH = 3

_HEAD_TAIL = struct.Struct("<IB")
_COUNT = struct.Struct("<I")
_KEY = struct.Struct("<H")
_FLAGS = struct.Struct("<BBBBB3sII")
_TAIL = struct.Struct("<HI")


def _read_category(reader: RecordReader, path: tuple[int, ...]) -> list[dict]:
    """The category at `reader`, then its children, depth first."""
    (category_key,) = reader.unpack(_KEY)
    name_kr = reader.text(wide=True)
    (
        is_useable, price_type, special_category_type, tag_type, tag_order,
        unknown_05, unique_no, child_count,
    ) = reader.unpack(_FLAGS)
    keys = (*path, category_key)
    if len(keys) > MAX_DEPTH:
        raise ValueError(f"category {keys} is nested deeper than {MAX_DEPTH} levels")
    children = [record for _ in range(child_count) for record in _read_category(reader, keys)]
    unknown_children_00, unknown_children_02 = reader.unpack(_TAIL)
    category = {
        "main_key": keys[0],
        "middle_key": keys[1] if len(keys) > 1 else None,
        "small_key": keys[2] if len(keys) > 2 else None,
        "category_key": category_key,
        "depth": len(keys),
        "name_kr": name_kr,
        "is_useable": is_useable,
        "price_type": price_type,
        "special_category_type": special_category_type,
        "tag_type": tag_type,
        "tag_order": tag_order,
        "unknown_name_kr_05": unknown_05.hex(),
        "unique_no": unique_no,
        "child_count": child_count,
        "unknown_children_00": unknown_children_00,
        "unknown_children_02": unknown_children_02,
    }
    return [category, *children]


def parse_cashproductcategory(data: bytes) -> tuple[dict, list[dict]]:
    """The head (the all-categories name and its two unknown fields) and every category, depth first.

    Raises ValueError when a category runs past the file or the categories end before it.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    all_name_kr = reader.text(wide=True)
    unknown_00, unknown_04 = reader.unpack(_HEAD_TAIL)
    head = {
        "all_name_kr": all_name_kr,
        "unknown_all_name_kr_00": unknown_00,
        "unknown_all_name_kr_04": unknown_04,
    }
    (count,) = reader.unpack(_COUNT)
    records = [record for _ in range(count) for record in _read_category(reader, ())]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} categories end at 0x{reader.pos:X}, the file at 0x{len(data):X}")
    return head, records


def parse_cashproductcategory_records(data: bytes) -> list[dict]:
    """Every category, main ones followed by their children. Raises ValueError like `parse_cashproductcategory()`."""
    return parse_cashproductcategory(data)[1]


def parse_cashproductcategoryoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row: main category key, offset of its category and its size with the children."""
    return parse_pabr_offset_rows(data)
