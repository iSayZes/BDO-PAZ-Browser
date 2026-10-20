"""Name, icon and cell text functions the layouts of `tables.py` point to."""

from __future__ import annotations

from _common.duration import format_duration
from _common.enum_name import enum_name
from _common.icon_index import IconKind, icon_path
from _common.loc import loc_text
from _common.quest.quest import quest_title, split_packed_quest_id
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


_MS_PER_SECOND = 1000


def duration_seconds(seconds: int) -> str:
    """A duration in seconds as `3h`, `1h 30m`; empty for zero."""
    return format_duration(seconds * _MS_PER_SECOND)


def rate_bonus(rate: int) -> str:
    """A rate as the client shows a bonus: `200000` -> `+20%` ("Item Drop Rate +20%")."""
    return f"+{rate_percent(rate)}"


_SECONDS_PER_DAY = 86_400
_SECONDS_PER_HOUR = 3_600
_SECONDS_PER_MINUTE = 60
# Days from 0000-03-01 to 1970-01-01, and per 400-year era, in the proleptic Gregorian calendar.
_EPOCH_SHIFT_DAYS = 719_468
_DAYS_PER_ERA = 146_097


def _civil_date(days: int) -> tuple[int, int, int]:
    """(year, month, day) of a day count from 1970-01-01 (H. Hinnant's `civil_from_days`).

    `datetime` is not in the modules the exe bundles (handler_api.py).
    """
    shifted = days + _EPOCH_SHIFT_DAYS
    era, day_of_era = divmod(shifted, _DAYS_PER_ERA)
    year_of_era = (day_of_era - day_of_era // 1460 + day_of_era // 36524 - day_of_era // 146096) // 365
    day_of_year = day_of_era - (365 * year_of_era + year_of_era // 4 - year_of_era // 100)
    month_index = (5 * day_of_year + 2) // 153
    day = day_of_year - (153 * month_index + 2) // 5 + 1
    month = month_index + 3 if month_index < 10 else month_index - 9
    year = year_of_era + era * 400 + (1 if month <= 2 else 0)
    return year, month, day


def utc_time(seconds: int) -> str:
    """Unix seconds as UTC date and time: `1785402000` -> `2026-07-30 09:00 UTC`."""
    days, second_of_day = divmod(seconds, _SECONDS_PER_DAY)
    year, month, day = _civil_date(days)
    hour, rest = divmod(second_of_day, _SECONDS_PER_HOUR)
    return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{rest // _SECONDS_PER_MINUTE:02d} UTC"


def packed_quest_text(packed_quest_id: int) -> str:
    """A packed quest ID as `chain/quest`: `0x00010904` -> `2308/1`."""
    chain, quest = split_packed_quest_id(packed_quest_id)
    return f"{chain}/{quest}"


def packed_quest_title(packed_quest_id: int) -> str:
    """LOC type 18 title of a packed quest ID, or ''."""
    return quest_title(*split_packed_quest_id(packed_quest_id))
