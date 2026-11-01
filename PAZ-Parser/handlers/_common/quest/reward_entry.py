"""The 178-byte quest reward entry of `quest.dbss` and `guildquest.dbss`.

An entry opens with the 2016 `gc::QuestRewardElement` members, byte-packed
with the pointer dropped:

    u32 reward_type | i64 experience | i32 skill_experience
    | i32 product_experience | u8 life_experience_type | i32 life_experience
    | u32 item_key | i64 item_count | u16 intimacy_character | i32 intimacy_value

then 135 bytes for the reward types the 2016 enum does not have:

    i32 mental_card_key | u8[2] | u8 exp_grade | u8[4] | u8[49]
    | u8[53] family_stat | u8[4] | u32 max_fever_point | u32 add_fever_point
    | u8 | u8 season_no | i64 explore_exp

`reward_type` picks the member that holds the reward. Both files store a list
as a u32 count and the entries back to back. "Reward Entry" in
docs/file-formats/dbss/quest_dbss.md and guildquest_dbss.md.

Client 1784 entries are 188 bytes (`REWARD_ENTRY_LAYOUT_1`): `unknown_9c` is
10 bytes long and 4 zero bytes follow `season_no`. "Reward Entry (188 bytes)"
in guildquest_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass
from typing import TypedDict

from _common.record_reader import RecordReader


REWARD_ENTRY_SIZE = 178

# gc::RewardType of the 2016 client.
REWARD_EXP = 0
REWARD_SKILL_EXP = 1
REWARD_LIFE_EXP = 2
REWARD_ITEM = 3
REWARD_INTIMACY = 4
# Later types: the client Lua enum names, matched to their values by the
# Quest_Table script calls of client 1784 (Reward Types in quest_dbss.md).
REWARD_KNOWLEDGE = 5
REWARD_EXP_GRADE = 7
REWARD_SKILL_EXP_GRADE = 8
REWARD_EXPLORE_EXP = 9
REWARD_FAMILY_STAT = 12
REWARD_FEVER_POINT = 17
REWARD_SEASON_REWARD = 18
REWARD_TYPE_NAMES = {
    REWARD_EXP: "eRewardExp",
    REWARD_SKILL_EXP: "eRewardSkillExp",
    REWARD_LIFE_EXP: "eRewardLifeExp",
    REWARD_ITEM: "eRewardItem",
    REWARD_INTIMACY: "eRewardIntimacy",
    REWARD_KNOWLEDGE: "eRewardKnowledge",
    REWARD_EXP_GRADE: "eRewardExpGrade",
    REWARD_SKILL_EXP_GRADE: "eRewardSkillExpGrade",
    REWARD_EXPLORE_EXP: "eRewardExploreExp",
    REWARD_FAMILY_STAT: "eRewardFamilyStat",
    # The client Lua spells this one `__eeRewardFeverPoint`.
    REWARD_FEVER_POINT: "eeRewardFeverPoint",
    REWARD_SEASON_REWARD: "eRewardSeasonReward",
}

# Start of the Family Stat Union (`quest.dbss`).
FAMILY_STAT_OFFSET = 0x67

_HEAD = struct.Struct("<IqiiBiIqHi")
# mental_card_key, unknown_2f, exp_grade, unknown_32, unknown_36, family_stat,
# unknown_9c, max_fever_point, add_fever_point, unknown_a8, season_no, explore_exp
_TAIL = struct.Struct("<i2sB4s49s53s4sIIBBq")
# The same members with the 10-byte unknown_9c; the 4 zero bytes after
# season_no are skipped.
_TAIL_LAYOUT_1 = struct.Struct("<i2sB4s49s53s10sIIBB4xq")
_U32 = struct.Struct("<I")


@dataclass(frozen=True)
class RewardEntryLayout:
    """One documented Reward Entry shape: the 2016 head, then `tail`."""

    tail: struct.Struct

    @property
    def size(self) -> int:
        return _HEAD.size + self.tail.size


REWARD_ENTRY_LAYOUT_2 = RewardEntryLayout(_TAIL)
REWARD_ENTRY_LAYOUT_1 = RewardEntryLayout(_TAIL_LAYOUT_1)


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
    # Knowledge (mentalcard.dbss card) of type 5.
    mental_card_key: int
    unknown_2f: str
    # expgrade() argument of type 7.
    exp_grade: int
    unknown_32: str
    unknown_36: str
    # The Family Stat Union as hex; quest.dbss decodes it.
    family_stat: str
    unknown_9c: str
    # Agris Fever points of type 17.
    max_fever_point: int
    add_fever_point: int
    unknown_a8: int
    # Season of type 18.
    season_no: int
    # Contribution EXP of type 9.
    explore_exp: int


def read_reward_entry(reader: RecordReader, layout: RewardEntryLayout = REWARD_ENTRY_LAYOUT_2) -> RewardEntry:
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
    (
        mental_card_key,
        unknown_2f,
        exp_grade,
        unknown_32,
        unknown_36,
        family_stat,
        unknown_9c,
        max_fever_point,
        add_fever_point,
        unknown_a8,
        season_no,
        explore_exp,
    ) = reader.unpack(layout.tail)
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
        mental_card_key=mental_card_key,
        unknown_2f=unknown_2f.hex(),
        exp_grade=exp_grade,
        unknown_32=unknown_32.hex(),
        unknown_36=unknown_36.hex(),
        family_stat=family_stat.hex(),
        unknown_9c=unknown_9c.hex(),
        max_fever_point=max_fever_point,
        add_fever_point=add_fever_point,
        unknown_a8=unknown_a8,
        season_no=season_no,
        explore_exp=explore_exp,
    )


def read_reward_list(reader: RecordReader, layout: RewardEntryLayout = REWARD_ENTRY_LAYOUT_2) -> list[RewardEntry]:
    """A u32 count, then that many entries."""
    (count,) = reader.unpack(_U32)
    return [read_reward_entry(reader, layout) for _ in range(count)]
