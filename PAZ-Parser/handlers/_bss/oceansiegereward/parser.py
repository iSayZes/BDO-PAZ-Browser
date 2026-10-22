"""`oceansiegereward.bss`: the Blue Battlefield (ocean siege) reward items.

    PABR | u32 row_count | row_count x Row | string table
    | u32 table_start | u32 0
    Row: u16 unknown_00 | 5 x Reward Set | Rewards unknown_rewards
         | u32 skill_key_1 | u32 skill_key_2
    Reward Set: 4 x Rewards (unknown_rewards_1 to unknown_rewards_4)
    Rewards: u64 count | count x Reward
    Reward (16 bytes): u32 item_id | bytes[4] unknown_04 | u64 count

Full layout in docs/file-formats/oceansiegereward_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, check_rows_end
from _common.record_reader import RecordReader


FILE_NAME = "oceansiegereward.bss"
REWARD_SET_COUNT = 5
# The reward lists of a Reward Set, in file order; the doc's field names.
SET_REWARD_LISTS: tuple[str, ...] = tuple(f"unknown_rewards_{number}" for number in range(1, 5))
# The list after the five sets.
ROW_REWARD_LIST = "unknown_rewards"

_ROW_COUNT = struct.Struct("<I")
_ROW_KEY = struct.Struct("<H")
_LIST_COUNT = struct.Struct("<Q")
_REWARD = struct.Struct("<I4sQ")
_SKILL_KEYS = struct.Struct("<II")


def _read_rewards(reader: RecordReader) -> list[dict]:
    (count,) = reader.unpack(_LIST_COUNT)
    if count * _REWARD.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} reward count {count:,} runs past the string table")
    rewards: list[dict] = []
    for _ in range(count):
        item_id, unknown_04, item_count = reader.unpack(_REWARD)
        rewards.append({"item_id": item_id, "unknown_04": unknown_04.hex(" "), "count": item_count})
    return rewards


def _read_row(reader: RecordReader) -> dict:
    (unknown_00,) = reader.unpack(_ROW_KEY)
    reward_sets = [{name: _read_rewards(reader) for name in SET_REWARD_LISTS} for _ in range(REWARD_SET_COUNT)]
    unknown_rewards = _read_rewards(reader)
    skill_key_1, skill_key_2 = reader.unpack(_SKILL_KEYS)
    return {
        "unknown_00": unknown_00,
        "reward_sets": reward_sets,
        ROW_REWARD_LIST: unknown_rewards,
        "skill_key_1": skill_key_1,
        "skill_key_2": skill_key_2,
    }


def parse_reward_rows(data: bytes) -> list[dict]:
    """Every row in file order: `unknown_00`, the five reward sets, the last list and the two skill keys.

    Raises ValueError on a bad magic or trailer, or when the rows do not end
    where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE - _ROW_COUNT.size, end, FILE_NAME)
    (row_count,) = reader.unpack(_ROW_COUNT)
    rows = [_read_row(reader) for _ in range(row_count)]
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return rows


def _row_fields(row: dict) -> dict:
    return {"unknown_00": row["unknown_00"], "skill_key_1": row["skill_key_1"], "skill_key_2": row["skill_key_2"]}


def parse_reward_records(data: bytes) -> list[dict]:
    """One record per reward item, in file order, with its row's fields.

    `reward_set` is the set's number (1 to 5) and `reward_list` the list's
    field name; an item of the list after the sets has `reward_set` None.
    Raises ValueError like `parse_reward_rows`.
    """
    records: list[dict] = []
    for row in parse_reward_rows(data):
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
