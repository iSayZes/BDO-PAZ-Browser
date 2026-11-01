"""`rosewarrewardstaticstatus.bss`: the Rose War reward items, one row without and one with a guild.

    PABR | u32 row_count | row_count x Row | string table
    | u32 table_start | u32 0
    Row: 4 x (u64 count | count x Reward) | u8 is_guild
    Reward (16 bytes): u32 item_id | bytes[4] unknown_04 | u64 count

The four lists are the victory, defeat and liberation rewards and a fourth
list. Full layout in docs/file-formats/bss/rosewarrewardstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, check_rows_end
from _common.record_reader import RecordReader
from _common.reward_items import read_reward_items


FILE_NAME = "rosewarrewardstaticstatus.bss"
# The reward lists of a row, in file order; the doc's field names.
REWARD_LISTS: tuple[str, ...] = ("win_rewards", "lose_rewards", "draw_rewards", "unknown_rewards")

_ROW_COUNT = struct.Struct("<I")
_IS_GUILD = struct.Struct("<B")


def parse_reward_rows(data: bytes) -> list[dict]:
    """Every row in file order: `is_guild` and the four reward lists.

    Raises ValueError on a bad magic or trailer, or when the rows do not end
    where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE - _ROW_COUNT.size, end, FILE_NAME)
    (row_count,) = reader.unpack(_ROW_COUNT)
    rows: list[dict] = []
    for _ in range(row_count):
        lists = {name: read_reward_items(reader, FILE_NAME) for name in REWARD_LISTS}
        (is_guild,) = reader.unpack(_IS_GUILD)
        rows.append({**lists, "is_guild": is_guild})
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return rows


def parse_reward_records(data: bytes) -> list[dict]:
    """One record per reward item: its row's `is_guild`, its list and the item.

    Raises ValueError like `parse_reward_rows`.
    """
    return [
        {"is_guild": row["is_guild"], "reward_list": name, **reward}
        for row in parse_reward_rows(data)
        for name in REWARD_LISTS
        for reward in row[name]
    ]
