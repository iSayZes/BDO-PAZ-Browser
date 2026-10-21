"""The Black Shrine window's names for a part and a difficulty (LOC type 37).

The keys are the ones `panel_window_morningland_boss_all_1.luac` and its
UI XML show. `part_name` and `difficulty_name` return '' when the text is
not loaded; `part_label` and `difficulty_label` then fall back to the
handler's own labels. `elementalmonsterreward.bss` shows its bosses with
the same labels.
"""

from __future__ import annotations

from pathlib import Path

from _bss.stringtable.parser import GAME_SHEET, RESOURCE_SHEET
from _bss.stringtable.text import ui_hash_text
from _common.lang import load_handler_strings
from _common.string_hash import key_hash


# `monster_part` values: `__eMorningLandMosterPart1` and `...Part2`.
PART_SOLO = 1
PART_PARTY = 2

_PART_NAME_KEYS = {
    PART_SOLO: "PANEL_BLACKTEMPLE_SINGLE",
    PART_PARTY: "PANEL_BLACKTEMPLE_PARTY",
}
# Hwanghae (Party) levels: the Normal and Hard radio buttons pass 0 and 1.
_PARTY_DIFFICULTY_KEYS = ("PANEL_MORNING2_EASY", "PANEL_MORNING2_HARD")
_SOLO_DIFFICULTY_KEY = "LUA_MORNING_ATTRBOSS_DIFFICULTY_{level}"
# The handler's own labels, by Hwanghae (Party) level, for a client without the text.
_PARTY_LEVEL_LABELS = ("normal", "hard")
_LANG_DIR = Path(__file__).parent / "lang"


def part_name(monster_part: int) -> str:
    """`Donghae (Solo)` or `Hwanghae (Party)`."""
    key = _PART_NAME_KEYS.get(monster_part)
    return ui_hash_text(RESOURCE_SHEET, key_hash(key)) if key else ""


def difficulty_name(monster_part: int, level: int) -> str:
    """`Calamity 7` for a Donghae (Solo) level, `Normal` or `Hard` for a Hwanghae (Party) one."""
    if monster_part == PART_SOLO:
        return ui_hash_text(GAME_SHEET, key_hash(_SOLO_DIFFICULTY_KEY.format(level=level)))
    if monster_part == PART_PARTY and 0 <= level < len(_PARTY_DIFFICULTY_KEYS):
        return ui_hash_text(RESOURCE_SHEET, key_hash(_PARTY_DIFFICULTY_KEYS[level]))
    return ""


def part_label(lang: str, monster_part: int) -> str:
    """The window's part name, else the handler's label, else the bare value."""
    if name := part_name(monster_part):
        return name
    labels = load_handler_strings(lang, _LANG_DIR)["parts"]
    if monster_part == PART_SOLO:
        return labels["solo"]
    if monster_part == PART_PARTY:
        return labels["party"]
    return str(monster_part)


def difficulty_label(lang: str, monster_part: int, level: int) -> str:
    """The window's difficulty name (`Calamity 7`, `Hard`), else the handler's label."""
    if name := difficulty_name(monster_part, level):
        return name
    labels = load_handler_strings(lang, _LANG_DIR)["difficulties"]
    if monster_part == PART_PARTY and 0 <= level < len(_PARTY_LEVEL_LABELS):
        return labels[_PARTY_LEVEL_LABELS[level]]
    return labels["calamity"].format(number=level + 1)
