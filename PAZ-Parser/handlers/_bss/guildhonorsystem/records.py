"""The table records of `guildhonorsystem.bss`: one per list entry, with the shown text joined.

Each record keeps the doc's fields of its list and adds the fields the
columns share: `description` (English text, else the Korean one),
`type_value` (`reason_type` or `benefit_type`) and `details_text` (the boss,
skills or mission range its parameters name). Kept apart from handler.py so
the tests can import it (see "Unit Tests" in docs/handler.md).
"""

from __future__ import annotations

import re
from collections.abc import Callable

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text
from _common.loc import loc_text
from _common.rate import RATE_PER_PERCENT
from _common.string_hash import key_hash
from .parser import GuildHonorSystem


# Record `section` values, one per list of the file.
CHANGE_REASON_SECTION = "change_reason"
BENEFIT_SECTION = "benefit"
DAILY_INCENTIVE_SECTION = "daily_incentive"

# `reason_type` values whose `reason_param` is a boss_spawn.bss key, or a skill key.
BOSS_REASON_TYPES = frozenset({1005, 1006})
SKILL_REASON_TYPES = frozenset({1007})

# `benefit_type` values: a guild mission range, or one or two skill keys.
MISSION_BENEFIT = 0
UNLOCK_SKILL_BENEFIT = 2
UPGRADE_SKILL_BENEFIT = 3

UPGRADE_ARROW = " → "
_RANGE_DASH = " - "

# LOC type of the English text, keyed by the row key.
LOC_CHANGE_REASON = 141
LOC_BENEFIT = 140
# The GAME sheet text the Lua fills with a daily pay step's bonus.
_DAILY_INCENTIVE_KEY_HASH = key_hash("LUA_GUILDHONOR_DAILYINCENTIVE_BENEFIT_GUIDE")
_PERCENT_PLACEHOLDER = "{percent}"

# The bold tags the stored and the LOC texts put around the amount.
_BOLD_TAG_RE = re.compile(r"</?b>")

LabelOf = Callable[[int], str]


def _plain(text: str) -> str:
    return _BOLD_TAG_RE.sub("", text).strip()


def bonus_percent_text(bonus_percent: int) -> str:
    """The `{percent}` the Lua fills in: `9000000` -> `900`."""
    return f"{bonus_percent / RATE_PER_PERCENT:g}"


def _reason_details(record: dict, boss_label: LabelOf, skill_label: LabelOf) -> str:
    param = record["reason_param"]
    if param and record["reason_type"] in BOSS_REASON_TYPES:
        return boss_label(param)
    if param and record["reason_type"] in SKILL_REASON_TYPES:
        return skill_label(param)
    return ""


def _benefit_details(record: dict, skill_label: LabelOf) -> str:
    benefit_type = record["benefit_type"]
    if benefit_type == MISSION_BENEFIT:
        return f"{record['param_1']}{_RANGE_DASH}{record['param_2']}"
    if benefit_type == UNLOCK_SKILL_BENEFIT:
        return skill_label(record["param_1"])
    if benefit_type == UPGRADE_SKILL_BENEFIT:
        return f"{skill_label(record['param_1'])}{UPGRADE_ARROW}{skill_label(record['param_2'])}"
    return ""


def _change_reason_record(record: dict, boss_label: LabelOf, skill_label: LabelOf) -> dict:
    return {
        "section": CHANGE_REASON_SECTION,
        **record,
        "description": _plain(loc_text(LOC_CHANGE_REASON, record["key"]) or record["description_kr"]),
        "type_value": record["reason_type"],
        "details_text": _reason_details(record, boss_label, skill_label),
    }


def _benefit_record(record: dict, skill_label: LabelOf) -> dict:
    return {
        "section": BENEFIT_SECTION,
        **record,
        "description": _plain(loc_text(LOC_BENEFIT, record["key"]) or record["description_kr"]),
        "type_value": record["benefit_type"],
        "details_text": _benefit_details(record, skill_label),
    }


def _daily_incentive_record(record: dict) -> dict:
    percent = bonus_percent_text(record["bonus_percent"])
    text = ui_hash_text(GAME_SHEET, _DAILY_INCENTIVE_KEY_HASH)
    return {
        "section": DAILY_INCENTIVE_SECTION,
        "key": None,
        **record,
        "description": text.replace(_PERCENT_PLACEHOLDER, percent),
        "type_value": None,
        "details_text": f"+{percent}%",
    }


def guild_honor_records(system: GuildHonorSystem, *, boss_label: LabelOf, skill_label: LabelOf) -> list[dict]:
    """Every list entry as one record, the change reasons first, each list in file order.

    `boss_label` names a boss_spawn.bss key and `skill_label` a skill key.
    """
    return [
        *(_change_reason_record(record, boss_label, skill_label) for record in system.change_reasons),
        *(_benefit_record(record, skill_label) for record in system.benefits),
        *(_daily_incentive_record(record) for record in system.daily_incentives),
    ]
