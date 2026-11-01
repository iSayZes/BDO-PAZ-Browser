"""`guildmanufacture.dbss`: the Guild Crafting recipes, one per product item.

A u32 row count, then variable rows: the u32 product item key (the key
`guildmanufactureoffset.dbss` stores), the u32 `itemexchangesource.bss` key,
the product item key again, three u64 values (time, price, product limit),
six u32 required item keys and their six u64 counts, a u8 category, a u32
count of u16 guild house character keys, and a u32 guild skill key.
`guildmanufactureoffset.dbss` points 4 bytes into a row, at the exchange
key, so the walk from the start needs no index. Layout 2 in
docs/file-formats/dbss/guildmanufacture_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "guildmanufacture.dbss"
OFFSET_FILE = "guildmanufactureoffset.dbss"

# The slots the Guild Crafting window shows (`__eGuildManufactureRequiredItemCount`
# in panel_guild_manufacture_all_1.luac); an empty slot holds key 0.
REQUIRED_ITEM_SLOTS = 6

_COUNT_SIZE = 4
# product_item_key, exchange_item_key, product_item_key_dup, time, price, product_item_limit
_HEAD = struct.Struct("<IIIQQQ")
_REQUIRED_KEYS = struct.Struct(f"<{REQUIRED_ITEM_SLOTS}I")
_REQUIRED_COUNTS = struct.Struct(f"<{REQUIRED_ITEM_SLOTS}Q")
# category, guild_house_count
_HOUSE_HEAD = struct.Struct("<BI")
_HOUSE_KEY_SIZE = 2
_SKILL_KEY = struct.Struct("<I")


def _parse_row(data: bytes, offset: int) -> tuple[dict, int]:
    """One row at `offset` and the offset after it.

    Raises ValueError when the row runs past the end of the file.
    """
    houses_offset = offset + _HEAD.size + _REQUIRED_KEYS.size + _REQUIRED_COUNTS.size + _HOUSE_HEAD.size
    if houses_offset > len(data):
        raise ValueError(f"row at 0x{offset:X} runs past the end of the file")
    product_item_key, exchange_item_key, product_item_key_dup, time, price, product_item_limit = (
        _HEAD.unpack_from(data, offset)
    )
    keys_offset = offset + _HEAD.size
    counts_offset = keys_offset + _REQUIRED_KEYS.size
    required_item_keys = list(_REQUIRED_KEYS.unpack_from(data, keys_offset))
    required_item_counts = list(_REQUIRED_COUNTS.unpack_from(data, counts_offset))
    category, guild_house_count = _HOUSE_HEAD.unpack_from(data, counts_offset + _REQUIRED_COUNTS.size)

    skill_offset = houses_offset + guild_house_count * _HOUSE_KEY_SIZE
    end = skill_offset + _SKILL_KEY.size
    if end > len(data):
        raise ValueError(
            f"row at 0x{offset:X} lists {guild_house_count:,} guild houses and runs past the end of the file"
        )
    guild_house_keys = list(struct.unpack_from(f"<{guild_house_count}H", data, houses_offset))
    (skill_key,) = _SKILL_KEY.unpack_from(data, skill_offset)
    record = {
        "product_item_key": product_item_key,
        "exchange_item_key": exchange_item_key,
        "product_item_key_dup": product_item_key_dup,
        "time": time,
        "price": price,
        "product_item_limit": product_item_limit,
        "required_item_keys": required_item_keys,
        "required_item_counts": required_item_counts,
        "category": category,
        "guild_house_count": guild_house_count,
        "guild_house_keys": guild_house_keys,
        "skill_key": skill_key,
    }
    return record, end


def parse_guildmanufacture_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not the row count followed by exactly
    that many rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    records = []
    offset = _COUNT_SIZE
    for _ in range(count):
        record, offset = _parse_row(data, offset)
        records.append(record)
    if offset != len(data):
        raise ValueError(f"{count:,} rows end at 0x{offset:X}, the file is {len(data):,} bytes")
    return records
