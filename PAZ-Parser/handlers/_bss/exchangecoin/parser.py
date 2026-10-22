"""`exchangecoin.bss`: the coin exchange, the items each coin item buys.

    u32 coin_count | coin_count x coin | u32 unknown_order_count
    | unknown_order_count x u32 unknown_order_keys
    coin: u8 unknown_00 | u32 coin_item_key | u8 info_category | i64 unknown_06
          | u64 accumulated_level_count | accumulated_level_count x u64 accumulated_need_counts
          | u32 reward_count | reward_count x reward
    reward (35 bytes): u32 exchange_no | u64 need_coin_count | u32 item_key
          | u64 item_count | u8 exchange_type | u8 limit_count | i64 unknown_1a
          | u8 accumulated_need_level

No PABR magic and no string table. `unknown_order_keys` lists the coin item
keys of the coins in another order. Layout 3 in
docs/file-formats/exchangecoin_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import COUNT_SIZE, read_counted_structs, read_counted_u32s
from _common.record_reader import RecordReader


FILE_NAME = "exchangecoin.bss"
KEY_FIELD = "exchange_no"
# `accumulated_need_level` of a reward that needs no accumulated coin level.
NO_LEVEL = 0xFF

_COIN_HEAD = struct.Struct("<BIBqQ")
_U64 = struct.Struct("<Q")
_REWARD = struct.Struct("<IqIqBBqB")
_REWARD_FIELDS = (
    KEY_FIELD, "need_coin_count", "item_key", "item_count", "exchange_type",
    "limit_count", "unknown_1a", "accumulated_need_level",
)


def _read_coin(reader: RecordReader) -> dict:
    unknown_00, coin_item_key, info_category, unknown_06, level_count = reader.unpack(_COIN_HEAD)
    if level_count * _U64.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} coin {coin_item_key} declares {level_count:,} levels past the end")
    need_counts = [reader.unpack(_U64)[0] for _ in range(level_count)]
    rewards = read_counted_structs(reader, _REWARD, _REWARD_FIELDS, f"{FILE_NAME} coin {coin_item_key} rewards")
    return {
        "unknown_00": unknown_00,
        "coin_item_key": coin_item_key,
        "info_category": info_category,
        "unknown_06": unknown_06,
        "accumulated_need_counts": need_counts,
        "rewards": rewards,
    }


def parse_exchangecoin(data: bytes) -> tuple[list[dict], list[int]]:
    """Every coin in file order with its rewards, and the coin key list after them.

    Raises ValueError when a coin or the key list runs past the file or the
    list ends before it.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its coin count")
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    (coin_count,) = reader.unpack(struct.Struct("<I"))
    coins = [_read_coin(reader) for _ in range(coin_count)]
    order_keys = read_counted_u32s(reader, f"{FILE_NAME} coin key list")
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} ends at 0x{len(data):X}, past the coin key list at 0x{reader.pos:X}")
    return coins, order_keys


def parse_exchangecoin_records(data: bytes) -> list[dict]:
    """One record per reward, coin by coin, each with its coin's fields. Raises ValueError like `parse_exchangecoin()`."""
    coins, _order_keys = parse_exchangecoin(data)
    return [
        {**{field: value for field, value in coin.items() if field != "rewards"}, **reward}
        for coin in coins
        for reward in coin["rewards"]
    ]
