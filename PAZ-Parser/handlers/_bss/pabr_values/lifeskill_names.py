"""Cell text of the fishing tables (`lifeskill_tables.py`)."""

from __future__ import annotations

from _common.string_hash import key_hash
from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text
from _dbss.lifeexp.labels import rank_text


# The auto-fishing discard window (panel_widget_fishing_all_2.luac, client
# 3482) names its choices `LUA_FISHING_DISCARD_ITEM_GRADE_0` ("Do not
# discard") to `_4` ("Yellow") and lets the player pick choice `grade + 1`
# at most, so a stored grade names its choice under this key with `grade + 1`.
_DISCARD_CHOICE_KEY = "LUA_FISHING_DISCARD_ITEM_GRADE_{choice}"


def fishing_level_text(level: int) -> str:
    """`Professional 1` for level 31, as the client shows it; else the level."""
    return rank_text(level) or str(level)


def discard_grade_text(grade: int) -> str:
    """`1 Green`: a stored grade and the colour of the highest choice it opens."""
    text = ui_hash_text(GAME_SHEET, key_hash(_DISCARD_CHOICE_KEY.format(choice=grade + 1)))
    return f"{grade} {text}" if text else str(grade)
