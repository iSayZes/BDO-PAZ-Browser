"""`guildquest.dbss`: the guild missions of the guild quest window.

A u32 row count, then rows back to back:

    u32 quest_no | str16 complete_condition | str16 complete_condition_text_kr
    | u16 quest_level | str16 title_kr | str16 description_kr | str16 icon_path
    | u32 limit_minute | u32 need_item_key | i64 need_item_count | u8 is_preoccupancy
    | u32 base_reward_count | 178-byte reward entries
    | u32 select_reward_count | reward entries | u32 | i64
    | u32 contents_group_count | u32 contents_group_hashes[] | u8 guild_quest_type
    | u32 unknown_value_count | u32 unknown_values[] | u32 | u32

The reward entries are read by `_common/quest/reward_entry.py`. Every row
carries its own counts, so the walk needs no index;
`guildquestoffset.dbss` lists (quest_no, row offset, row size). Layout 2 in
docs/file-formats/dbss/guildquest_dbss.md.
"""

from __future__ import annotations

import struct

# REWARD_ENTRY_SIZE stays importable from here for the tests.
from _common.quest.reward_entry import REWARD_ENTRY_SIZE, read_reward_list  # noqa: F401
from _common.record_reader import RecordReader


FILE_NAME = "guildquest.dbss"
OFFSET_FILE = "guildquestoffset.dbss"

_U8 = struct.Struct("<B")
_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")
# limit_minute, need_item_key, need_item_count, is_preoccupancy
_ACCEPT = struct.Struct("<IIqB")
# unknown_select_rewards_00, unknown_select_rewards_04
_AFTER_REWARDS = struct.Struct("<Iq")
# unknown_after_unknown_values, unknown_end
_END = struct.Struct("<II")


def _u32_list(reader: RecordReader) -> list[int]:
    (count,) = reader.unpack(_U32)
    return list(reader.unpack(struct.Struct(f"<{count}I")))


def _parse_row(reader: RecordReader) -> dict:
    (quest_no,) = reader.unpack(_U32)
    complete_condition = reader.text(wide=True)
    complete_condition_text_kr = reader.text(wide=True)
    (quest_level,) = reader.unpack(_U16)
    title_kr = reader.text(wide=True)
    description_kr = reader.text(wide=True)
    icon_path = reader.text(wide=True)
    limit_minute, need_item_key, need_item_count, is_preoccupancy = reader.unpack(_ACCEPT)
    base_rewards = read_reward_list(reader)
    select_rewards = read_reward_list(reader)
    after_00, after_04 = reader.unpack(_AFTER_REWARDS)
    contents_group_hashes = _u32_list(reader)
    (guild_quest_type,) = reader.unpack(_U8)
    unknown_values = _u32_list(reader)
    unknown_after_unknown_values, unknown_end = reader.unpack(_END)
    return {
        "quest_no": quest_no,
        "complete_condition": complete_condition,
        "complete_condition_text_kr": complete_condition_text_kr,
        "quest_level": quest_level,
        "title_kr": title_kr,
        "description_kr": description_kr,
        "icon_path": icon_path,
        "limit_minute": limit_minute,
        "need_item_key": need_item_key,
        "need_item_count": need_item_count,
        "is_preoccupancy": is_preoccupancy,
        "base_reward_count": len(base_rewards),
        "base_rewards": base_rewards,
        "select_reward_count": len(select_rewards),
        "select_rewards": select_rewards,
        "unknown_select_rewards_00": after_00,
        "unknown_select_rewards_04": after_04,
        "contents_group_count": len(contents_group_hashes),
        "contents_group_hashes": contents_group_hashes,
        "guild_quest_type": guild_quest_type,
        "unknown_value_count": len(unknown_values),
        "unknown_values": unknown_values,
        "unknown_after_unknown_values": unknown_after_unknown_values,
        "unknown_end": unknown_end,
    }


def parse_guildquest_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when a row runs past the file or bytes follow the last
    of the counted rows.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    (count,) = reader.unpack(_U32)
    records = [_parse_row(reader) for _ in range(count)]
    if not reader.at_end():
        raise ValueError(f"{reader.remaining():,} bytes follow the last of {count:,} rows")
    return records
