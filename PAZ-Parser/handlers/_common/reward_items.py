"""The u64-counted reward item lists of the siege and Rose War reward tables.

    u64 count | count x Reward
    Reward (16 bytes): u32 item_id | bytes[4] unknown_04 | u64 count

`oceansiegereward.bss`, `rosewarrewardstaticstatus.bss`,
`siege2024rewardstaticstatus.bss` and `majorsiegerewardstaticstatus.bss`
store their rewards this way (rosewarrewardstaticstatus_bss.md, Reward).
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader

_LIST_COUNT = struct.Struct("<Q")
_REWARD = struct.Struct("<I4sQ")


def read_reward_items(reader: RecordReader, file_name: str) -> list[dict]:
    """One reward list: each item as `item_id`, `unknown_04` (hex text) and `count`.

    Raises ValueError naming `file_name` when the count runs past the reader's
    end, where the rows of a PABR table stop and its string table starts.
    """
    (count,) = reader.unpack(_LIST_COUNT)
    if count * _REWARD.size > reader.remaining():
        raise ValueError(f"{file_name} reward count {count:,} runs past the string table")
    rewards: list[dict] = []
    for _ in range(count):
        item_id, unknown_04, item_count = reader.unpack(_REWARD)
        rewards.append({"item_id": item_id, "unknown_04": unknown_04.hex(" "), "count": item_count})
    return rewards
