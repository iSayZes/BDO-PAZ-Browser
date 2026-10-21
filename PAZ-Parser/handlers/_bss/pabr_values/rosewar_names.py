"""Names and cell text of the Rose War tables in `tables.py`.

The enum names come from the client Lua; the Lua holds no values, so each
value mapping below names the data that fixes it.
"""

from __future__ import annotations

from _common.enum_name import enum_name
from _common.string_hash import key_hash
from _common.town import town_name
from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text


# __eRoseWarSkillType_* in the order of the skill list in
# panel_rosewar_teamskill.luac, from 1. Each value's skill text matches its
# name (rosewarskillstaticstatus_bss.md, Skill Types).
ROSE_WAR_SKILL_TYPES: tuple[str, ...] = (
    "Scan",
    "Recall",
    "Bombard",
    "Summon",
    "Conceal",
    "Zonya",
    "FixedResurrection",
)
_FIRST_SKILL_TYPE = 1
# __eRoseWarTeam_* by team number: rosewarteamnostaticstatus.bss puts the
# Lemoria characters on 0 and the Ahib characters on 1.
ROSE_WAR_TEAMS: tuple[str, ...] = ("Kamasylvia", "Odyllita")
# One schedule entry: a u8, then (day, hour, minute) triples.
_SCHEDULE_TIME_SIZE = 3


def _value_and_name(value: int, name: str) -> str:
    return f"{value} {name}" if name else str(value)


def _enum_text(names: tuple[str, ...], value: int, first: int = 0) -> str:
    """The value and its member name, or the bare value outside the enum."""
    index = value - first
    return _value_and_name(value, enum_name(names, index) if 0 <= index < len(names) else "")


def skill_type_text(skill_type: int) -> str:
    """`3 Bombard`: the value and its `__eRoseWarSkillType_*` name."""
    return _enum_text(ROSE_WAR_SKILL_TYPES, skill_type, _FIRST_SKILL_TYPE)


def team_text(team_no: int) -> str:
    """`1 Odyllita`: the value and its `__eRoseWarTeam_*` name."""
    return _enum_text(ROSE_WAR_TEAMS, team_no)


def region_text(region_key: int) -> str:
    """`735 Grana`: a region key and its LOC type 17 name."""
    return _value_and_name(region_key, town_name(region_key))


def game_key_text(key: str) -> str:
    """LOC text of a GAME sheet key (`LUA_ROSEWAR_CHARTITLE_RANK_6`), or ''."""
    return ui_hash_text(GAME_SHEET, key_hash(key)) if key else ""


def argb_hex(argb: int) -> str:
    """An ARGB colour as `0xFFABFF79`."""
    return f"0x{argb:08X}"


def schedule_text(entry: list[int]) -> str:
    """One schedule entry as `0: 0 22:00, 1 00:00, ...`: its u8, then each day and time."""
    head, times = entry[0], entry[1:]
    slots = [times[i : i + _SCHEDULE_TIME_SIZE] for i in range(0, len(times), _SCHEDULE_TIME_SIZE)]
    return f"{head}: " + ", ".join(f"{day} {hour:02d}:{minute:02d}" for day, hour, minute in slots)
