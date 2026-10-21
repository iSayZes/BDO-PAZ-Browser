"""Barter categories: the `barter_category` bit mask and the Barter window's filter names.

Bit N of the mask is category N, the `__eBarterCategory_*` value whose label
the Barter information window (`panel_window_barterinfosearch.luac`) reads
from the GAME sheet key below. See docs/file-formats/bartersubgroup_bss.md,
"Barter Categories".
"""

from __future__ import annotations

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text
from _common.string_hash import key_hash

# Category value -> GAME sheet key of its filter label (Ocean, 8, takes filter 9).
_CATEGORY_KEYS = {
    1: "LUA_BARTER_NEW_FILTER_1",
    2: "LUA_BARTER_NEW_FILTER_2",
    3: "LUA_BARTER_NEW_FILTER_3",
    4: "LUA_BARTER_NEW_FILTER_4",
    5: "LUA_BARTER_NEW_FILTER_5",
    6: "LUA_BARTER_NEW_FILTER_6",
    7: "LUA_BARTER_NEW_FILTER_7",
    8: "LUA_BARTER_NEW_FILTER_9",
    9: "LUA_BARTER_NEW_FILTER_10",
    10: "LUA_BARTER_NEW_FILTER_11",
}
# A u32 mask holds bits 0 to 31.
_MASK_BITS = 32
_NAME_SEPARATOR = ", "


def category_numbers(mask: int) -> list[int]:
    """The categories whose bit is set in `mask`, lowest first."""
    return [bit for bit in range(_MASK_BITS) if mask >> bit & 1]


def category_name(category: int) -> str:
    """The LOC type 37 filter label of a category (`Crow Coin`), else its number."""
    key = _CATEGORY_KEYS.get(category)
    name = ui_hash_text(GAME_SHEET, key_hash(key)) if key else ""
    return name or str(category)


def category_names(mask: int) -> str | None:
    """`Lv. 4 -> Lv. 5, Ocean Barter` for a mask, None when no bit is set."""
    names = [category_name(category) for category in category_numbers(mask)]
    return _NAME_SEPARATOR.join(names) or None
