"""Display text of a guild mission: LOC type 27 strings and the mission type names."""

from __future__ import annotations

from _bss.stringtable.parser import RESOURCE_SHEET
from _bss.stringtable.text import ui_hash_text
from _common.loc import loc_tagged, resolve_text_binds
from _common.string_hash import key_hash


# LOC type 27: `str_id1` = quest_no; `str_id4` 0 title, 1 description,
# 2 objective (the translated complete_condition_text_kr).
LOC_GUILD_QUEST = 27
LOC_TITLE = 0
LOC_DESCRIPTION = 1
LOC_OBJECTIVE = 2

# guild_quest_type -> the RESOURCE sheet key of its tab tooltip in the guild
# mission list (HandleEventOnOut_GuildQuest_Type_ShowSimpleTooltip in
# panel_guildquestlist_all_2.luac). Type 3 has no tab.
_TYPE_KEYS = {
    0: "PANEL_GUILDQUEST_QUESTTYPE_BATTLE",
    1: "PANEL_GUILDQUEST_QUESTTYPE_LIFE",
    2: "PANEL_GUILDQUEST_QUESTTYPE_TRADE",
    4: "PANEL_GUILDQUEST_QUESTTYPE_BOSSBATTLE",
}


def guild_quest_type_name(guild_quest_type: int) -> str:
    """The tab name of a mission type (`Subjugation`), else the number."""
    key = _TYPE_KEYS.get(guild_quest_type)
    name = ui_hash_text(RESOURCE_SHEET, key_hash(key)) if key is not None else ""
    return name or str(guild_quest_type)


def guild_quest_tagged(quest_no: int, role: int, fallback_kr: str) -> str:
    """LOC type 27 text of one role with its PA tags, else the inline Korean text."""
    return loc_tagged(LOC_GUILD_QUEST, quest_no, role) or resolve_text_binds(fallback_kr).strip()
