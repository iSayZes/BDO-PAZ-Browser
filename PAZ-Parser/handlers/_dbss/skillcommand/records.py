"""The display record of one `skillcommand.dbss` row: LOC texts, the classes and the Drakania form.

LOC type 2 holds this table's own text under `str_id1` = skill number:
`str_id4` 0 the name, 1 the command and 2 the console command. The inline
Korean text is the fallback. A command wraps each key binding in angle
brackets (`<{KeyBind:Jump}> [after other skills]`); `command_tagged()` drops
them so `pa_html()` draws each binding as a key chip.

The class comes from `classskilllist.bss`, which lists the skill numbers of
each class's Skill Guide; a number can sit in more than one class row
(Wizard and Witch share eight).

The old Shadow Arena rows `17051` to `17174` reuse numbers that `skill.dbss`
gives to Tamer and Valkyrie skills, so they get no `skill.dbss` link.
docs/file-formats/dbss/skillcommand_dbss.md.
"""

from __future__ import annotations

from collections.abc import Mapping

from _bss.classskilllist.parser import parse_classskilllist_records
from _bss.skillcomboguide.commands import command_tagged
from _common.class_type import class_name
from _common.icon_index import clean_stored_icon_path
from _common.loc import loc_tagged, loc_text
from _common.pa_text import pa_fields
from _common.ui_texture import UI_TEXTURE_ICON_ROOT, ui_texture_path
from .parser import KEY_FIELD

LOC_SKILL_COMMAND = 2
NAME_ID4 = 0
COMMAND_ID4 = 1
CONSOLE_COMMAND_ID4 = 2
_CLASS_SEPARATOR = ", "
SHADOW_ARENA_SKILL_NOS = range(17051, 17175)
# skillcommand.dbss commands hold no `[stringtable key]`, so command_tagged()
# gets no key hashes and only drops the brackets around each key binding.
_NO_KEY_HASHES: Mapping[str, int] = {}


def skill_classes(classskilllist: bytes | None) -> dict[int, tuple[int, ...]]:
    """Skill number -> the class types whose `classskilllist.bss` row lists it, in file order.

    Empty without the file. Raises ValueError when the file does not parse.
    """
    if classskilllist is None:
        return {}
    classes: dict[int, tuple[int, ...]] = {}
    for row in parse_classskilllist_records(classskilllist):
        for skill_no in dict.fromkeys(row.skill_nos):
            classes[skill_no] = (*classes.get(skill_no, ()), row.class_type)
    return classes


def _command(skill_no: int, id4: int, korean: str) -> str:
    """The LOC command text, else the inline Korean, with bare key bindings."""
    return command_tagged(loc_tagged(LOC_SKILL_COMMAND, skill_no, id4) or korean, _NO_KEY_HASHES)


def skill_command_record(
    row: dict,
    classes: Mapping[int, tuple[int, ...]],
    forms: Mapping[str, str],
) -> dict:
    """`row` with its name, commands, icon path, classes, form label and whether it links to `skill.dbss`."""
    skill_no = row[KEY_FIELD]
    class_types = classes.get(skill_no, ())
    return {
        **row,
        "has_skill_link": skill_no not in SHADOW_ARENA_SKILL_NOS,
        "name": loc_text(LOC_SKILL_COMMAND, skill_no, NAME_ID4) or row["name_kr"].strip(),
        "icon": ui_texture_path(clean_stored_icon_path(row["icon_path"]), UI_TEXTURE_ICON_ROOT),
        **pa_fields("command", _command(skill_no, COMMAND_ID4, row["command_kr"])),
        **pa_fields("console_command", _command(skill_no, CONSOLE_COMMAND_ID4, row["console_command_kr"])),
        "class_types": list(class_types),
        "classes": _CLASS_SEPARATOR.join(class_name(class_type) for class_type in class_types) or None,
        "form": forms.get(str(row["extra_param"])),
    }
