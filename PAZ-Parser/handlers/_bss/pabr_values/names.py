"""Name, icon and cell text functions the layouts of `tables.py` point to."""

from __future__ import annotations

from _common.enum_name import enum_name
from _common.icon_index import IconKind, icon_path
from _common.loc import loc_text
from _common.rate import rate_percent
from _common.skill import skill_name, split_skill_key
from _common.string_hash import key_hash
from _common.vehicle_skill import LOC_VEHICLE_SKILL
from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text


# The client Lua's __eElementalStat_* names in value order, without the prefix.
ELEMENT_TYPE_NAMES: tuple[str, ...] = ("Sun", "Moon", "Land")
# The Black Shrine window (panel_window_morningland_boss_all.luac,
# _attributeDesc) names each aura with these GAME sheet keys, by element_type.
_AURA_NAME_KEYS: tuple[str, ...] = (
    "LUA_MORNING_ATTRBOSS_SUN",
    "LUA_MORNING_ATTRBOSS_MOON",
    "LUA_MORNING_ATTRBOSS_SOIL",
)


def vehicle_skill_name(key: int) -> str:
    return loc_text(LOC_VEHICLE_SKILL, key)


def skill_key_name(key: int) -> str:
    skill_no, _level = split_skill_key(key)
    return skill_name(skill_no)


def aura_name(element_type: int) -> str:
    """The aura name the Black Shrine window shows, else the enum name."""
    if 0 <= element_type < len(_AURA_NAME_KEYS):
        text = ui_hash_text(GAME_SHEET, key_hash(_AURA_NAME_KEYS[element_type]))
        if text:
            return text
    return enum_name(ELEMENT_TYPE_NAMES, element_type)


def item_icon_path(item_id: int) -> str:
    return icon_path(IconKind.ITEM, item_id)


def cooldown_cut(rate: int) -> str:
    """A rate as the client shows a cut: `150000` -> `-15%` ("Loot cooldown -15%")."""
    return f"-{rate_percent(rate)}"
