"""Display text for guild house uses and their guild skills.

`guildhousecraftskill.dbss` and `guildhousecraftskillreverselinklist.bss`
both show a receipe key with its house use name and a skill number with its
skill name.
"""
from __future__ import annotations

from _common.loc import loc_text
from _common.skill import skill_name


GUILD_HOUSE_CRAFT_SKILL = "gamecommondata/binary/guildhousecraftskill.dbss"
# LOC type 16, str_id1 = receipe key: the house use name (houseinforeceipe_dbss.md).
_LOC_TYPE_RECEIPE = 16


def house_use_name(receipe_key: int) -> str:
    """The house use name of a receipe key, or '' without one."""
    return loc_text(_LOC_TYPE_RECEIPE, receipe_key)


def skill_label(skill_no: int) -> str:
    """`65042 Building Boat Lv. 1`, or the bare number without a name."""
    return f"{skill_no} {skill_name(skill_no)}".strip()


def house_use_label(receipe_key: int) -> str:
    """`1601 Guild Shipyard`, or the bare key without a name."""
    return f"{receipe_key} {house_use_name(receipe_key)}".strip()
