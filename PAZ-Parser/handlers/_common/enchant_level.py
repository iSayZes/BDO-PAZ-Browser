"""Names of item enhancement levels: `+1` to `+15`, then PRI to DEC.

Levels 16 to 25 are drawn as grades in game; the LOC type 79 level names
confirm them (docs/file-formats/bss/specialenchantitem_bss.md).
"""

from __future__ import annotations


_FIRST_GRADE_LEVEL = 16
_GRADES = ("PRI", "DUO", "TRI", "TET", "PEN", "HEX", "SEP", "OCT", "NOV", "DEC")


def enchant_level_text(level: int) -> str:
    """`+7`, `PEN` or `DEC` for an enhancement level; '' for 0 or a value past DEC."""
    if level <= 0:
        return ""
    if level < _FIRST_GRADE_LEVEL:
        return f"+{level}"

    grade = level - _FIRST_GRADE_LEVEL
    return _GRADES[grade] if grade < len(_GRADES) else ""
