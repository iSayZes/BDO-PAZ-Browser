"""The 178-byte quest reward entry of `quest.dbss` and `guildquest.dbss`.

An entry opens with the 2016 `gc::QuestRewardElement` members, byte-packed
with the pointer dropped:

    u32 reward_type | i64 experience | i32 skill_experience
    | i32 product_experience | u8 life_experience_type | i32 life_experience
    | u32 item_key | i64 item_count | u16 intimacy_character | i32 intimacy_value

then 135 bytes the 2016 struct has no member for. `reward_type` picks the
member that holds the reward. Both files store a list as a u32 count and the
entries back to back. "Reward Entry" in docs/file-formats/quest_dbss.md and
guildquest_dbss.md.
"""

from __future__ import annotations

import struct
from typing import TypedDict

from _common.record_reader import RecordReader


REWARD_ENTRY_SIZE = 178

# gc::RewardType of the 2016 client. Later clients add more types (5 to 18),
# whose values sit in the tail.
REWARD_EXP = 0
REWARD_SKILL_EXP = 1
REWARD_LIFE_EXP = 2
REWARD_ITEM = 3
REWARD_INTIMACY = 4
REWARD_TYPE_NAMES = {
    REWARD_EXP: "eRewardExp",
    REWARD_SKILL_EXP: "eRewardSkillExp",
    REWARD_LIFE_EXP: "eRewardLifeExp",
    REWARD_ITEM: "eRewardItem",
    REWARD_INTIMACY: "eRewardIntimacy",
}

# Start of the Family Stat Union inside the tail (`quest.dbss`).
FAMILY_STAT_OFFSET = 0x67

_HEAD = struct.Struct("<IqiiBiIqHi")
_TAIL = struct.Struct(f"<{REWARD_ENTRY_SIZE - _HEAD.size}s")
_U32 = struct.Struct("<I")


class RewardEntry(TypedDict):
    reward_type: int
    experience: int
    skill_experience: int
    product_experience: int
    life_experience_type: int
    life_experience: int
    item_key: int
    item_count: int
    intimacy_character: int
    intimacy_value: int
    # The 135 bytes after intimacy_value, as hex.
    unknown_2b: str


def read_reward_entry(reader: RecordReader) -> RewardEntry:
    """One entry at the reader's position."""
    (
        reward_type,
        experience,
        skill_experience,
        product_experience,
        life_experience_type,
        life_experience,
        item_key,
        item_count,
        intimacy_character,
        intimacy_value,
    ) = reader.unpack(_HEAD)
    (tail,) = reader.unpack(_TAIL)
    return RewardEntry(
        reward_type=reward_type,
        experience=experience,
        skill_experience=skill_experience,
        product_experience=product_experience,
        life_experience_type=life_experience_type,
        life_experience=life_experience,
        item_key=item_key,
        item_count=item_count,
        intimacy_character=intimacy_character,
        intimacy_value=intimacy_value,
        unknown_2b=tail.hex(),
    )


def read_reward_list(reader: RecordReader) -> list[RewardEntry]:
    """A u32 count, then that many entries."""
    (count,) = reader.unpack(_U32)
    return [read_reward_entry(reader) for _ in range(count)]
