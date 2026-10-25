"""`challenge.dbss`: the challenges of the character window, keyed by challenge key.

    u32 count | count x (u16 key_prefix | row)
    row: u16 challenge_key | u32 challenge_type | str16 title_kr
         | str16 description_kr | str16 progress_condition | str16 reward_condition
         | u32 complete_condition_type | i32 condition_param1 | i32 condition_param2
         | u32 reset_type | i32 reset_value
         | u32 base_reward_count | 178-byte reward entries
         | u32 select_reward_count | 178-byte reward entries
         | u32 unknown_select_rewards_00 | i64 unknown_select_rewards_04
         | u8 is_reward_overlapable | u8 is_save_repository | u32 optional_type
         | u8 unknown_select_rewards_12 | u8 is_show_icon | u32 unknown_select_rewards_14

`key_prefix` repeats `challenge_key`. `challengeoffset.dbss` (u32 count, then
u16 key, u32 offset and u32 size per row, no PABR magic) points past the key
prefix. The reward entries are read by `_common/quest/reward_entry.py`.
Layout 2 in docs/file-formats/dbss/challenge_dbss.md; the client 1784 rows with
188-byte entries and `expected_price` (Layout 1) are not read.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.quest.reward_entry import read_reward_list
from _common.record_reader import RecordReader


FILE_NAME = "challenge.dbss"
OFFSET_FILE = "challengeoffset.dbss"
KEY_FIELD = "challenge_key"

_HEAD = struct.Struct("<HHI")
# complete_condition_type, condition_param1, condition_param2, reset_type, reset_value
_CONDITION = struct.Struct("<IiiIi")
# unknown_select_rewards_00, unknown_select_rewards_04, is_reward_overlapable,
# is_save_repository, optional_type, unknown_select_rewards_12, is_show_icon,
# unknown_select_rewards_14
_TAIL = struct.Struct("<IqBBIBBI")


def _read_row(reader: RecordReader) -> dict:
    key_prefix, challenge_key, challenge_type = reader.unpack(_HEAD)
    if key_prefix != challenge_key:
        raise ValueError(f"{FILE_NAME} row {challenge_key} follows the key prefix {key_prefix}")
    title_kr = reader.text(wide=True)
    description_kr = reader.text(wide=True)
    progress_condition = reader.text(wide=True)
    reward_condition = reader.text(wide=True)
    (
        complete_condition_type,
        condition_param1,
        condition_param2,
        reset_type,
        reset_value,
    ) = reader.unpack(_CONDITION)
    base_rewards = read_reward_list(reader)
    select_rewards = read_reward_list(reader)
    (
        unknown_select_rewards_00,
        unknown_select_rewards_04,
        is_reward_overlapable,
        is_save_repository,
        optional_type,
        unknown_select_rewards_12,
        is_show_icon,
        unknown_select_rewards_14,
    ) = reader.unpack(_TAIL)
    return {
        KEY_FIELD: challenge_key,
        "challenge_type": challenge_type,
        "title_kr": title_kr,
        "description_kr": description_kr,
        "progress_condition": progress_condition,
        "reward_condition": reward_condition,
        "complete_condition_type": complete_condition_type,
        "condition_param1": condition_param1,
        "condition_param2": condition_param2,
        "reset_type": reset_type,
        "reset_value": reset_value,
        "base_reward_count": len(base_rewards),
        "base_rewards": base_rewards,
        "select_reward_count": len(select_rewards),
        "select_rewards": select_rewards,
        "unknown_select_rewards_00": unknown_select_rewards_00,
        "unknown_select_rewards_04": unknown_select_rewards_04,
        "is_reward_overlapable": is_reward_overlapable,
        "is_save_repository": is_save_repository,
        "optional_type": optional_type,
        "unknown_select_rewards_12": unknown_select_rewards_12,
        "is_show_icon": is_show_icon,
        "unknown_select_rewards_14": unknown_select_rewards_14,
    }


def parse_challenge_records(data: bytes) -> list[dict]:
    """Every challenge row in file order.

    Raises ValueError when a row runs past the file, its key prefix differs
    from its key, or the rows end before the last byte.
    """
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_challengeoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row: challenge key, row offset and row size. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)
