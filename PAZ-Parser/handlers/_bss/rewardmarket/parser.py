"""`rewardmarket.bss`: the pet exchange, the items a pet trades for.

    PABR | u32 row_count | row_count x row | string table | u32 table_start | u32 0
    row: u16 trade_key | u32 pet_key | bytes[11] unknown_06 | u32 reward_count
         | reward_count x (u32 item_key, u64 item_count)

`pet_key` is a `pet.dbss` pet ID. Layout 1 in
docs/file-formats/bss/rewardmarket_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.counted_rows import read_counted_structs
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "rewardmarket.bss"
KEY_FIELD = "trade_key"

_HEAD = struct.Struct("<HI11s")
_REWARD = struct.Struct("<IQ")
_REWARD_FIELDS = ("item_key", "item_count")
_COUNT_SIZE = 4


def _read_row(reader: RecordReader) -> dict:
    trade_key, pet_key, unknown_06 = reader.unpack(_HEAD)
    rewards = read_counted_structs(reader, _REWARD, _REWARD_FIELDS, f"{FILE_NAME} trade {trade_key} rewards")
    return {
        KEY_FIELD: trade_key,
        "pet_key": pet_key,
        "unknown_06": unknown_06.hex(),
        "reward_count": len(rewards),
        "rewards": rewards,
    }


def parse_rewardmarket_records(data: bytes) -> list[dict]:
    """Every trade in file order.

    Raises ValueError on a bad PABR magic or trailer, or when the rows do not
    end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE, end, FILE_NAME)
    records = [_read_row(reader) for _ in range(u32(data, HEADER_SIZE - _COUNT_SIZE))]
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} rows end at 0x{reader.pos:X}, the string table starts at 0x{end:X}")
    return records
