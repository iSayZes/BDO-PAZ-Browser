"""Skill cells of the skill list tables: icon, number and name, linked to `skill.dbss`.

`skillcomboguide.bss`, `skillquickslotinfo.bss`, `skillfusionslotlist.bss`,
`uipracticeskilltreelayout.bss` and `instancedungeonskillinfo.bss` list skill
numbers; each shows them the same way. A click opens the first `skill.dbss`
row of the skill.
"""

from __future__ import annotations

from collections.abc import Sequence

from _common.html import IconEntry, hidden_slice, icon_html_list_cell, record_link
from _common.icon_index import IconKind, icon_path
from _common.lookup_builders import SKILL
from _common.skill import skill_name

SKILL_LINK_CLASS = "record-link"
_EMPTY = "-"


def skill_label(skill_no: int) -> str:
    """`1022 Charging Thrust I`, or the bare number without a name."""
    return f"{skill_no} {skill_name(skill_no)}".strip()


def skill_link(skill_no: int, text: str | None = None) -> str:
    """A button that opens the skill's first `skill.dbss` row; `text` defaults to `skill_label`."""
    return record_link(text if text is not None else skill_label(skill_no), SKILL, "skill_no", skill_no, SKILL_LINK_CLASS)


def skill_entry(skill_no: int) -> IconEntry:
    """The skill's icon path and its linked label, for the icon list cells."""
    return icon_path(IconKind.SKILL, skill_no), skill_link(skill_no)


def skill_list_cell(skill_nos: Sequence[int], max_items: int) -> str:
    """The first `max_items` skills with icons and links, the rest counted, or a dash."""
    if not skill_nos:
        return _EMPTY
    shown = [skill_entry(skill_no) for skill_no in skill_nos[:max_items]]
    hidden = [skill_label(skill_no) for skill_no in hidden_slice(skill_nos, max_items)]
    return icon_html_list_cell(shown, len(skill_nos) - len(shown), hidden_names=hidden)
