"""`oceansiegereward.bss`: the Blue Battlefield (ocean siege) reward items.

    PABR | u32 row_count | row_count x Row | string table
    | u32 table_start | u32 0
    Row: u16 unknown_00 | 5 x Reward Set | Rewards unknown_rewards
         | u32 skill_key_1 | u32 skill_key_2
    Reward Set: 4 x Rewards (unknown_rewards_1 to unknown_rewards_4)
    Rewards: u64 count | count x Reward
    Reward (16 bytes): u32 item_id | bytes[4] unknown_04 | u64 count

`siege2024rewardstaticstatus.bss` has the same rows; the parse functions take
its name. Full layout in docs/file-formats/oceansiegereward_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, check_rows_end
from _common.record_reader import RecordReader
from _common.reward_items import read_reward_items


FILE_NAME = "oceansiegereward.bss"
REWARD_SET_COUNT = 5
# The reward lists of a Reward Set, in file order; the doc's field names.
SET_REWARD_LISTS: tuple[str, ...] = tuple(f"unknown_rewards_{number}" for number in range(1, 5))
# The list after the five sets.
ROW_REWARD_LIST = "unknown_rewards"

_ROW_COUNT = struct.Struct("<I")
_ROW_KEY = struct.Struct("<H")
_SKILL_KEYS = struct.Struct("<II")


def _read_row(reader: RecordReader, file_name: str) -> dict:
    (unknown_00,) = reader.unpack(_ROW_KEY)
    reward_sets = [
        {name: read_reward_items(reader, file_name) for name in SET_REWARD_LISTS} for _ in range(REWARD_SET_COUNT)
    ]
    unknown_rewards = read_reward_items(reader, file_name)
    skill_key_1, skill_key_2 = reader.unpack(_SKILL_KEYS)
    return {
        "unknown_00": unknown_00,
        "reward_sets": reward_sets,
        ROW_REWARD_LIST: unknown_rewards,
        "skill_key_1": skill_key_1,
        "skill_key_2": skill_key_2,
    }


def parse_reward_rows(data: bytes, file_name: str = FILE_NAME) -> list[dict]:
    """Every row in file order: `unknown_00`, the five reward sets, the last list and the two skill keys.

    `file_name` names the file in error messages. Raises ValueError on a bad
    magic or trailer, or when the rows do not end where the string table starts.
    """
    end = checked_string_table_start(data, file_name)
    reader = RecordReader(data, HEADER_SIZE - _ROW_COUNT.size, end, file_name)
    (row_count,) = reader.unpack(_ROW_COUNT)
    rows = [_read_row(reader, file_name) for _ in range(row_count)]
    check_rows_end(data, reader.pos, f"{file_name} rows")
    return rows


def _row_fields(row: dict) -> dict:
    return {"unknown_00": row["unknown_00"], "skill_key_1": row["skill_key_1"], "skill_key_2": row["skill_key_2"]}


def parse_reward_records(data: bytes, file_name: str = FILE_NAME) -> list[dict]:
    """One record per reward item, in file order, with its row's fields.

    `reward_set` is the set's number (1 to 5) and `reward_list` the list's
    field name; an item of the list after the sets has `reward_set` None.
    Raises ValueError like `parse_reward_rows`.
    """
    records: list[dict] = []
    for row in parse_reward_rows(data, file_name):
        for set_number, reward_set in enumerate(row["reward_sets"], start=1):
            for name in SET_REWARD_LISTS:
                records += [
                    {**_row_fields(row), "reward_set": set_number, "reward_list": name, **reward}
                    for reward in reward_set[name]
                ]
        records += [
            {**_row_fields(row), "reward_set": None, "reward_list": ROW_REWARD_LIST, **reward}
            for reward in row[ROW_REWARD_LIST]
        ]
    return records
