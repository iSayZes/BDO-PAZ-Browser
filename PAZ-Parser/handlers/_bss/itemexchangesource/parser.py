"""`itemexchangesource.bss`: item exchanges, the recipes of workers, houses, guilds and boxes.

    PABR | u32 count | count x row | string table | u32 string_table_start | u32 0

    row:  u32 key | u32 key_dup | u8 unknown_08 | u8 exchange_type | 36 zero bytes
          | u32 material_count | material_count x material
          | material source_item (copy of the first) | u8 product_category | 12 zero bytes
          | u64 product_time | i16 unknown_materials_21 | u32 product_drop_key
          | u32 luck_drop_key | u16 craft_character_key | u32 icon_ref
          | u32 description_ref | u32 detail_description_ref | 60 zero bytes
          | u8 work_ani_type | i32 unknown_materials_76
          | u32 unknown_list_count | unknown_list_count x u16
          | u16 unknown_list_00 | u16 repeat_group_key | i32 daily_working_count
          | i32 first_working_index | u32 contents_group_count
          | contents_group_count x u32 hash | u32 unknown_end
    material: u32 item_key | u64 count

The `*_ref` fields index the string table; string 0 is empty. The always-zero
byte blocks are skipped. Full layout in docs/file-formats/bss/itemexchangesource_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_strings import (
    HEADER_SIZE,
    check_rows_end,
    checked_string_table_start,
    read_string_table,
)
from _common.record_reader import RecordReader

FILE_NAME = "itemexchangesource.bss"
_HEAD = struct.Struct("<IIBB36xI")
_MATERIAL = struct.Struct("<IQ")
# From source_item (skipped, it repeats the first material) to unknown_list_count.
_BODY = struct.Struct("<12xB12xQhIIHIII60xBiI")
_TAIL = struct.Struct("<HHiiI")
_U32 = struct.Struct("<I")


@dataclass(frozen=True)
class Material:
    # enchant_level << 24 | item_id
    item_key: int
    count: int


@dataclass(frozen=True)
class ItemExchange:
    key: int
    exchange_type: int
    materials: tuple[Material, ...]
    product_category: int
    # Milliseconds; the worker windows show it divided by 1,000 as the workload.
    product_time: int
    product_drop_key: int
    luck_drop_key: int
    craft_character_key: int
    icon_path: str
    description_kr: str
    detail_description_kr: str
    work_ani_type: int
    repeat_group_key: int
    daily_working_count: int
    first_working_index: int
    contents_group_hashes: tuple[int, ...]
    unknown_08: int
    unknown_materials_21: int
    unknown_materials_76: int
    unknown_list: tuple[int, ...]
    unknown_list_00: int
    unknown_end: int


def parse_itemexchangesource_records(data: bytes) -> list[ItemExchange]:
    """Every row in file order.

    Raises ValueError on a bad magic, a row that runs into the string table,
    a `key_dup` that differs from `key`, a string index past the table, or
    when the rows do not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    pos = HEADER_SIZE
    rows: list[ItemExchange] = []
    for _ in range(u32(data, 4)):
        reader = RecordReader(data, pos, end, f"{FILE_NAME} row at 0x{pos:X}")
        rows.append(_read_row(reader, strings))
        pos = reader.pos
    check_rows_end(data, pos, f"{FILE_NAME} rows")
    return rows


def build_exchange_name_kr_index(data: bytes) -> dict[int, str]:
    """The `EXCHANGE_NAME_KR` index: every exchange key to its Korean name, '' when it has none.

    Every row is kept, so the index also tells which keys have a row to link to.
    Read it through `_common/item_exchange.py`.
    """
    return {exchange.key: exchange.description_kr for exchange in parse_itemexchangesource_records(data)}


def _read_row(reader: RecordReader, strings: list[str]) -> ItemExchange:
    key, key_dup, unknown_08, exchange_type, material_count = reader.unpack(_HEAD)
    if key_dup != key:
        raise ValueError(f"{FILE_NAME} row {key} repeats its key as {key_dup}")
    materials = tuple(Material(*reader.unpack(_MATERIAL)) for _ in range(material_count))
    (
        product_category, product_time, unknown_materials_21, product_drop_key, luck_drop_key,
        craft_character_key, icon_ref, description_ref, detail_description_ref,
        work_ani_type, unknown_materials_76, list_count,
    ) = reader.unpack(_BODY)
    unknown_list = reader.unpack(struct.Struct(f"<{list_count}H"))
    unknown_list_00, repeat_group_key, daily_working_count, first_working_index, hash_count = reader.unpack(_TAIL)
    contents_group_hashes = reader.unpack(struct.Struct(f"<{hash_count}I"))
    (unknown_end,) = reader.unpack(_U32)
    return ItemExchange(
        key=key,
        exchange_type=exchange_type,
        materials=materials,
        product_category=product_category,
        product_time=product_time,
        product_drop_key=product_drop_key,
        luck_drop_key=luck_drop_key,
        craft_character_key=craft_character_key,
        icon_path=_string(strings, icon_ref, key),
        description_kr=_string(strings, description_ref, key),
        detail_description_kr=_string(strings, detail_description_ref, key),
        work_ani_type=work_ani_type,
        repeat_group_key=repeat_group_key,
        daily_working_count=daily_working_count,
        first_working_index=first_working_index,
        contents_group_hashes=contents_group_hashes,
        unknown_08=unknown_08,
        unknown_materials_21=unknown_materials_21,
        unknown_materials_76=unknown_materials_76,
        unknown_list=unknown_list,
        unknown_list_00=unknown_list_00,
        unknown_end=unknown_end,
    )


def _string(strings: list[str], index: int, key: int) -> str:
    if index >= len(strings):
        raise ValueError(f"{FILE_NAME} row {key} points at string {index}, past the string table")
    return strings[index]
