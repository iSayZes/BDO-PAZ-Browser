"""Names and cell text of the Hardcore channel tables in `hardcore_tables.py`."""

from __future__ import annotations

from _common.class_type import class_name
from _common.string_hash import key_hash
from _bss.stringtable.parser import RESOURCE_SHEET
from _bss.stringtable.text import ui_hash_text


_LIST_SEPARATOR = ", "
# The ranking window (panel_widget_ranking_hardcore_1.luac, initTierList)
# names grade keys 1 to 3 PANEL_HARDCOE_RANKING_TIER_0_<key>, grade keys 4 to
# 9 PANEL_HARDCOE_RANKING_TIERNAME_<key - 3> and grade key 0 TIERNAME_7; its
# _totalGradeCount is 10.
_TOP_GRADE_KEY = "PANEL_HARDCOE_RANKING_TIER_0_{}"
_TIER_GRADE_KEY = "PANEL_HARDCOE_RANKING_TIERNAME_{}"
_NO_GRADE_KEY = "PANEL_HARDCOE_RANKING_TIERNAME_7"
_TOP_GRADE_COUNT = 3
_GRADE_COUNT = 10
# The tier names take the player's rank as a {rank} prefix; the table has none.
_RANK_PARAMETER = "{rank}"


def _grade_string_key(grade_key: int) -> str:
    """The RESOURCE sheet key of a grade's name, or '' outside the ranking window's grades."""
    if grade_key == 0:
        return _NO_GRADE_KEY
    if 0 < grade_key <= _TOP_GRADE_COUNT:
        return _TOP_GRADE_KEY.format(grade_key)
    if _TOP_GRADE_COUNT < grade_key < _GRADE_COUNT:
        return _TIER_GRADE_KEY.format(grade_key - _TOP_GRADE_COUNT)
    return ""


def grade_name(grade_key: int) -> str:
    """The tier name the ranking window shows for a grade key (`1` Transcendent), or ''."""
    key = _grade_string_key(grade_key)
    if not key:
        return ""
    return ui_hash_text(RESOURCE_SHEET, key_hash(key)).replace(_RANK_PARAMETER, "").strip()


def class_list_text(class_types: list[int]) -> str:
    """`Warrior, Hashashin, ...`: the LOC type 21 name of each class type, in list order."""
    return _LIST_SEPARATOR.join(class_name(class_type) for class_type in class_types)
