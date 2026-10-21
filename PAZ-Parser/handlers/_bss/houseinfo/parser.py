"""`houseinfo.bss`: the node houses, their uses and the items each house can make.

    PABR | u32 count | count x house row | u32 product_count | product_count x product
    | string table | u32 table_start | u32 0
    house row: i16 need_explore_point | u16 affiliated_town | u32 parent_node_key
               | u16 character_key | u16 unknown_0a | u32 house_group | i32 house_floor
               | u64 need_house_count | need_house_count x u16
               | u32 craft_count | craft_count x (u32 receipe_key, u32 level)
               | u8 unknown_after_crafts
    product:   u32 item_key | u64 house_count | house_count x u16

The product list maps an item to the houses whose uses make it. Full layout
in docs/file-formats/houseinfo_bss.md.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "houseinfo.bss"

_U8 = struct.Struct("<B")
_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
_HOUSE_HEAD = struct.Struct("<hHIHHIi")
_CRAFT = struct.Struct("<II")
_PRODUCT_HEAD = struct.Struct("<IQ")
_HOUSE_KEY_SIZE = 2


class HouseInfo(NamedTuple):
    """The house rows and the product list, each in file order."""

    houses: list[dict]
    products: list[dict]


def _read_house_keys(reader: RecordReader, count: int) -> list[int]:
    """`count` u16 house keys. Raises ValueError when they run past the rows."""
    if count * _HOUSE_KEY_SIZE > reader.remaining():
        raise ValueError(f"{FILE_NAME}: list of {count:,} house keys runs past the rows")
    return list(reader.unpack(struct.Struct(f"<{count}H")))


def _read_house(reader: RecordReader) -> dict:
    (
        need_explore_point, affiliated_town, parent_node_key, character_key,
        unknown_0a, house_group, house_floor,
    ) = reader.unpack(_HOUSE_HEAD)
    (need_house_count,) = reader.unpack(_U64)
    need_house_keys = _read_house_keys(reader, need_house_count)
    (craft_count,) = reader.unpack(_U32)
    crafts = [
        dict(zip(("receipe_key", "level"), reader.unpack(_CRAFT)))
        for _ in range(craft_count)
    ]
    (unknown_after_crafts,) = reader.unpack(_U8)
    return {
        "character_key": character_key,
        "need_explore_point": need_explore_point,
        "affiliated_town": affiliated_town,
        "parent_node_key": parent_node_key,
        "unknown_0a": unknown_0a,
        "house_group": house_group,
        "house_floor": house_floor,
        "need_house_keys": need_house_keys,
        "crafts": crafts,
        "unknown_after_crafts": unknown_after_crafts,
    }


def _read_product(reader: RecordReader) -> dict:
    item_key, house_count = reader.unpack(_PRODUCT_HEAD)
    return {"item_key": item_key, "house_keys": _read_house_keys(reader, house_count)}


def parse_houseinfo(data: bytes) -> HouseInfo:
    """Every house row and every product entry.

    Raises ValueError on a bad magic, when a row runs past the string table,
    or when the product list does not end where the string table starts.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE, rows_end, FILE_NAME)
    count = struct.unpack_from("<I", data, 4)[0]
    houses = [_read_house(reader) for _ in range(count)]
    (product_count,) = reader.unpack(_U32)
    products = [_read_product(reader) for _ in range(product_count)]
    check_rows_end(data, reader.pos, f"{FILE_NAME} products")
    return HouseInfo(houses, products)


def products_by_house(products: list[dict]) -> dict[int, list[int]]:
    """House key -> the item keys the product list names for it, each once, in file order."""
    items: dict[int, dict[int, None]] = {}
    for product in products:
        for house_key in product["house_keys"]:
            items.setdefault(house_key, {})[product["item_key"]] = None
    return {house_key: list(keys) for house_key, keys in items.items()}
