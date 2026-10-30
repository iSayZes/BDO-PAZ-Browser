"""The two quest count files: their enum, the record keys and the names the
quest window shows for each value.

The enum names come from the client Lua (`CppEnums.QuestRegionType` in
`global_define_cpp_enum.luac`, the `__eQuestType_*` order of
`panel_window_quest_all.luac`). The GAME sheet keys are the `_regionString`
and `_typeString` tables of `panel_window_quest_all.luac`; values the Lua
gives no key (the three Olvia Academy types) show their enum name.
"""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Mapping


_HISTORY_REGION = "LUA_QUESTLIST_HISTORY_TXT_REGION_{}"
_HISTORY_TYPE = "LUA_QUESTLIST_HISTORY_TXT_TYPE_{}"
_ETC = _HISTORY_REGION.format(99)


@dataclass(frozen=True)
class QuestCountTable:
    """One quest count file and how its values are named."""

    file_name: str
    key_field: str
    name_field: str
    enum_names: tuple[str, ...]
    name_keys: Mapping[int, str]
    # Keys of the handler's lang/*.json.
    key_column: str
    name_column: str
    count_meta: str


QUEST_REGION_NAMES: tuple[str, ...] = (
    "None", "Balenos", "Serendia", "NorthCalpheon", "CalpheonBigCity", "Keplan",
    "SouthWestCalpheon", "Media", "Valencia", "Kamasylvia", "Drigan", "Odilita",
    "MountainOfEternalWinter", "AbyssOne", "MorningLand", "Ulukita", "Edania_1", "Edania_2",
)

QUEST_TYPE_NAMES: tuple[str, ...] = (
    "BlackSpirit", "Main", "Sub", "Repeat", "Adventure", "BaseLife", "OceanLife",
    "CraftLife", "Contents", "Event", "Guild", "DirectAccept", "Sudden", "SeasonPass",
    "GrowthPass", "DirectClear", "Journal", "OlviaAcademyPass", "OlviaAcademyReward",
    "OlviaAcademyCurriculum",
)

# Region 0 (no region) shows "Etc."; AbyssOne uses the Abyss One server title.
# Regions 1 to 12 use their own number, the later ones skip numbers.
_REGION_KEYS: dict[int, str] = {
    0: _ETC,
    **{region: _HISTORY_REGION.format(region) for region in range(1, 13)},
    13: "LUA_ABYSSONE_MSG_SERVERSELECT_TITLE",
    14: _HISTORY_REGION.format(13),
    15: _HISTORY_REGION.format(14),
    16: _HISTORY_REGION.format(17),
    17: _HISTORY_REGION.format(20),
}

# Type N uses TYPE_(N+1), except DirectClear, which the Lua names "Etc.".
_DIRECT_CLEAR = QUEST_TYPE_NAMES.index("DirectClear")
_JOURNAL = QUEST_TYPE_NAMES.index("Journal")
_TYPE_KEYS: dict[int, str] = {
    quest_type: _ETC if quest_type == _DIRECT_CLEAR else _HISTORY_TYPE.format(quest_type + 1)
    for quest_type in range(_JOURNAL + 1)
}

QUEST_REGION_TABLE = QuestCountTable(
    file_name="totalquestcountregion.bss",
    key_field="quest_region",
    name_field="quest_region_name",
    enum_names=QUEST_REGION_NAMES,
    name_keys=MappingProxyType(_REGION_KEYS),
    key_column="questRegionId",
    name_column="questRegion",
    count_meta="regionCount",
)

QUEST_TYPE_TABLE = QuestCountTable(
    file_name="totalquestcounttype.bss",
    key_field="quest_type",
    name_field="quest_type_name",
    enum_names=QUEST_TYPE_NAMES,
    name_keys=MappingProxyType(_TYPE_KEYS),
    key_column="questTypeId",
    name_column="questType",
    count_meta="typeCount",
)

QUEST_COUNT_TABLES: tuple[QuestCountTable, ...] = (QUEST_REGION_TABLE, QUEST_TYPE_TABLE)

# quest.dbss Layout 1 (clients 1717 to 2000) numbers quest types in
# `CppEnums.QuestType` of global_define_cpp_enum.luac (read on client 1784), with
# gaps. The data also holds 13 and 16 (the season pass and Growth Pass quest
# lists), which that enum does not name.
_CPP_QUEST_TYPES: dict[int, str] = {
    0: "BlackSpirit", 1: "Story", 2: "Town", 3: "Adventure", 4: "Trade", 5: "Craft",
    6: "Repetition", 7: "Guild", 10: "Special", 11: "RegionMonsterKill", 15: "Production",
}
# The _typeString table of that client's panel_window_quest_all.luac: value N
# reads TYPE_(N+1) up to Guild, then Special TYPE_10 and RegionMonsterKill TYPE_11.
_CPP_TYPE_KEYS: dict[int, str] = {
    **{quest_type: _HISTORY_TYPE.format(quest_type + 1) for quest_type in range(8)},
    10: _HISTORY_TYPE.format(10),
    11: _HISTORY_TYPE.format(11),
}

CPP_ENUMS_QUEST_TYPE_TABLE = QuestCountTable(
    file_name="totalquestcounttype.bss",
    key_field="quest_type",
    name_field="quest_type_name",
    enum_names=tuple(_CPP_QUEST_TYPES.get(value, "") for value in range(max(_CPP_QUEST_TYPES) + 1)),
    name_keys=MappingProxyType(_CPP_TYPE_KEYS),
    key_column="questTypeId",
    name_column="questType",
    count_meta="typeCount",
)
