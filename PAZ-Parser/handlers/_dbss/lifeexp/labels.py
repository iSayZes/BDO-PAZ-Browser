"""Life skill names and rank names from the client Lua.

`global_define_cpp_enum.luac` numbers the life skills in
`CppEnums.LifeExperienceType` (`gather` 0 to `temp4` 14, `Type_Count` 15) and
names them in `CppEnums.LifeExperienceString` with `GAME` sheet keys
(`LUA_SELFCHARACTERINFO_GATHER`); the spare slots `temp1` to `temp4` get no key.

`PaGlobalFunc_Util_CraftLevelReplace` in `global_util.luac` turns a level into
its rank: levels 1 to 10 read `LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_1` (Beginner)
plus the level, up to group 7 (Guru) for levels 81 to 180, shown as level - 80.

The key's text is LOC type 37 under its `stringtable.bss` hash. The hash
function is unknown but depends on the key string alone, so the hashes are
stored here, and a test checks them against `stringtable.bss`.
"""

from __future__ import annotations

from typing import NamedTuple

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_key_text


class LifeSkillLabel(NamedTuple):
    enum_name: str
    key: str | None = None
    key_hash: int | None = None


class RankGroup(NamedTuple):
    first_level: int
    last_level: int
    key: str
    key_hash: int


# LifeExperienceType value -> its enum name and name key, in the Lua's order.
LIFE_SKILLS: dict[int, LifeSkillLabel] = {
    0: LifeSkillLabel("gather", "LUA_SELFCHARACTERINFO_GATHER", 313477045),
    1: LifeSkillLabel("fishing", "LUA_SELFCHARACTERINFO_FISH", 216983509),
    2: LifeSkillLabel("hunting", "LUA_SELFCHARACTERINFO_HUNT", 4003364020),
    3: LifeSkillLabel("cooking", "LUA_SELFCHARACTERINFO_COOK", 1307088205),
    4: LifeSkillLabel("alchemy", "LUA_SELFCHARACTERINFO_ALCHEMY", 551531861),
    5: LifeSkillLabel("manufacture", "LUA_SELFCHARACTERINFO_MANUFACTURE", 1909319174),
    6: LifeSkillLabel("training", "LUA_SELFCHARACTERINFO_OBEDIENCE", 1245402146),
    7: LifeSkillLabel("trade", "LUA_SELFCHARACTERINFO_TRADE", 840542349),
    8: LifeSkillLabel("growth", "LUA_SELFCHARACTERINFO_GROWTH", 759374495),
    9: LifeSkillLabel("sail", "LUA_SELFCHARACTERINFO_SAIL", 2861791965),
    10: LifeSkillLabel("temp1"),
    11: LifeSkillLabel("barter", "LUA_SELFCHARACTERINFO_BARTER", 375791083),
    12: LifeSkillLabel("temp2"),
    13: LifeSkillLabel("temp3"),
    14: LifeSkillLabel("temp4"),
}

# Beginner, Apprentice, Skilled, Professional, Artisan, Master, Guru.
RANK_GROUPS: tuple[RankGroup, ...] = (
    RankGroup(1, 10, "LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_1", 1594363795),
    RankGroup(11, 20, "LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_2", 3364130715),
    RankGroup(21, 30, "LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_3", 2625546170),
    RankGroup(31, 40, "LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_4", 3576975617),
    RankGroup(41, 50, "LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_5", 2104237919),
    RankGroup(51, 80, "LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_6", 4119818460),
    RankGroup(81, 180, "LUA_CHARACTERINFO_CRAFTLEVEL_GROUP_7", 3746834287),
)

KEY_HASHES = {
    GAME_SHEET: {
        **{label.key: label.key_hash for label in LIFE_SKILLS.values() if label.key and label.key_hash},
        **{group.key: group.key_hash for group in RANK_GROUPS},
    }
}


def life_skill_name(life_skill: int) -> str:
    """The LOC name of a life skill (`Gathering`), else its enum name (`temp1`),
    else its number."""
    label = LIFE_SKILLS.get(life_skill)
    if label is None:
        return str(life_skill)
    text = ui_key_text(KEY_HASHES, GAME_SHEET, label.key) if label.key else ""
    return text or label.enum_name


def rank_text(level: int) -> str | None:
    """`Guru 12` for level 92, as the client shows it; None outside levels
    1 to 180 or without LOC."""
    for group in RANK_GROUPS:
        if group.first_level <= level <= group.last_level:
            name = ui_key_text(KEY_HASHES, GAME_SHEET, group.key)
            return f"{name} {level - group.first_level + 1}" if name else None
    return None
