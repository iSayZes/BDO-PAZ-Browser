"""The castle name of an `__eEdaniaRegion` value, shared by the Edania tables."""

from __future__ import annotations

from _common.string_hash import key_hash
from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text
from .parser import EDANIA_REGION_NAMES


# The Edania window (panel_window_edania_contents_all.luac) names each region's
# castle with this GAME sheet key; Orbita and Tenebraum swap numbers 3 and 4.
_CASTLE_NAME_KEY = "LUA_EDANIA_SYSTEM_CASTLE_NAME_{}"
_CASTLE_NAME_NUMBERS = (1, 2, 4, 3, 5, 6, 7, 8, 9, 10)


def castle_name(edania_region: int) -> str:
    """The castle name the Edania window shows, else the enum name, else ''."""
    if not 0 <= edania_region < len(EDANIA_REGION_NAMES):
        return ""
    key = _CASTLE_NAME_KEY.format(_CASTLE_NAME_NUMBERS[edania_region])
    return ui_hash_text(GAME_SHEET, key_hash(key)) or EDANIA_REGION_NAMES[edania_region]
