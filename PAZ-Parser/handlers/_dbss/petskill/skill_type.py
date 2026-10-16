"""Display names of the pet skill types, the `skill_type` byte of `petskill.dbss`.

The pet info window (`setPetSkillType` in `panel_window_petinfo_all_1.luac`)
picks one GAME sheet key per type; the 2016 client names types 1 to 10 in
`gc::PetSkillParam::PetSkillType` (`ePetSkill_Looting` to `ePetSkill_CollectingBoost`).
"""

from __future__ import annotations

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import KeyHashes, ui_key_text


_KEY_PREFIX = "LUA_PETINFO_PETSKILLTYPE_"
PET_SKILL_TYPE_KEYS: dict[int, str] = {
    1: "ITEMGETTIME",
    2: "FINDGATHER",
    3: "FINDPK",
    4: "FINDPLACE",
    5: "MOBAGGRO",
    6: "FINDRAREMONSTER",
    7: "REDUCEAUTOFISHINGTIME",
    8: "REGISTILL",
    9: "AUTOGETHERING",
    10: "GETHERINGINCREASE",
    11: "HPRECOVERY",
    12: "MPRECOVERY",
    13: "FINDLOSTNORMALITEM",
    14: "FINDLOSTSPECIALITEM",
}
# The loot text carries the pickup time the client computes in
# ToClient_getPetLootingCoolTime; the browser cannot reproduce it.
_LOOT_TIME_PARAM = "{itemGetTime}"
_UNKNOWN_VALUE = "?"


def pet_skill_type_name(hashes: KeyHashes, skill_type: int) -> str:
    """The pet window's text for a skill type, or '' for an unknown type or without LOC."""
    key = PET_SKILL_TYPE_KEYS.get(skill_type)
    if key is None:
        return ""
    return ui_key_text(hashes, GAME_SHEET, _KEY_PREFIX + key).replace(_LOOT_TIME_PARAM, _UNKNOWN_VALUE)


def pet_skill_types(records: list[dict]) -> dict[int, int]:
    """`pet_skill_id -> skill_type` from parsed `petskill.dbss` level rows."""
    return {record["pet_skill_id"]: record["skill_type"] for record in records}
