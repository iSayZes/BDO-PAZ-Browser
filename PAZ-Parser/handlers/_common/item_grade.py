"""Item grades and the colours the game draws item names in.

`itemenchant.dbss` stores the grade at `+0x06`, 0 to 5; tables other than
`itemenchant.dbss` read it from the `ITEM_GRADE` lookup index through
`item_grade()`. The colours come from
`PAGlobalFunc_SetItemTextColorByItemGrade` in the client Lua
(`include/global_util`), which also wraps a name in the grade's `<PAColor>`
tag (`PAGlobalFunc_ReturnAppliedItemColorTextForNewUI`). See
docs/file-formats/dbss/itemenchant_dbss.md.
"""

from __future__ import annotations

from _common.lookup_index import IndexKind, lookup

# ARGB name colour by grade: white, green, blue, yellow, orange, then purple
# (Sovereign, Kharazad, the Fiery Sovereign gear; purple confirmed in game).
ITEM_GRADE_COLORS = (0xFFC4C4C4, 0xFF83A543, 0xFF438DCC, 0xFFF5BA3A, 0xFFD05D48, 0xFFA070EF)


def item_grade(item_id: int) -> int | None:
    """Grade of a base item from the `ITEM_GRADE` index, or None when unknown."""
    grade = lookup(IndexKind.ITEM_GRADE, item_id)
    return grade if isinstance(grade, int) else None


def item_grade_tagged(name: str, grade: int | None) -> str:
    """`name` in its grade's `<PAColor>` tag, as the game writes it; plain for an unknown grade."""
    if not name or grade is None or not 0 <= grade < len(ITEM_GRADE_COLORS):
        return name
    return f"<PAColor0x{ITEM_GRADE_COLORS[grade]:08X}>{name}<PAOldColor>"
