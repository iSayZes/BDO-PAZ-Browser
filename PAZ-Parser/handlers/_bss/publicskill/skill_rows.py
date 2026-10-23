"""Record fields and cells of one skill key, shared by `publicskill.bss` and `privateskill.bss`.

Both files list level 1 skill keys; each row shows the skill number linked
to its `skill.dbss` row, then the skill icon and LOC type 10 name.
"""

from __future__ import annotations

from _common.html import icon_html_label_cell
from _common.icon_index import IconKind, icon_path
from _common.pa_text import pa_cell, pa_fields
from _common.skill import skill_name_tagged, split_skill_key
from _common.skill_cells import skill_link


SKILL_NO_FIELD = "skill_no"
SKILL_FIELD = "skill"


def skill_key_fields(skill_key: int) -> dict:
    """`skill_key`, its `skill_no` and `level`, and the skill name as `pa_fields`."""
    skill_no, level = split_skill_key(skill_key)
    return {
        "skill_key": skill_key,
        SKILL_NO_FIELD: skill_no,
        "level": level,
        **pa_fields(SKILL_FIELD, skill_name_tagged(skill_no)),
    }


def skill_no_cell(record: dict) -> str:
    """The skill number as a link to its first `skill.dbss` row."""
    skill_no = record[SKILL_NO_FIELD]
    return skill_link(skill_no, str(skill_no))


def skill_name_cell(record: dict) -> str:
    """The skill icon and its name in game colours."""
    return icon_html_label_cell(icon_path(IconKind.SKILL, record[SKILL_NO_FIELD]), pa_cell(record, SKILL_FIELD))
