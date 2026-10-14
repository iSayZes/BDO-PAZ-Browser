"""A `.cl` combo list read as combos and skill commands.

`<combolist>` holds `<combo>` elements, each a sequence of `<skill>` and
`<move>` steps; `<skill_command_list>` holds the keyboard and mouse input of
each action name (`<skill_command>` with `<command key starttime endtime>`).
Two files use an older layout with capitalized names (`<Combo Name
StartWeaponType>`, `<Skill SkillNo Command>`); both spellings are read. See
docs/file-formats/combolist_cl.md.
"""
from __future__ import annotations

from dataclasses import dataclass

from _ai.sections import section_and_note
from _ai.xml_tree import XmlNode, parse_xml

_COMBO_LIST = "combolist"
_COMBO = "combo"
_COMMAND_LIST = "skill_command_list"
_COMMAND = "skill_command"
_KEY = "command"
STEP_SKILL = "skill"
STEP_MOVE = "move"

# Each field and its attribute names: the current layout first, then the older one.
_NAME = ("name",)
_WEAPON = ("start_weapon_type", "StartWeaponType")
_CONSOLE_ONLY = ("is_only_console",)
_LEARN_CHECK = ("learn_check_skill",)
_COOL_CHECK = ("cool_check_skill",)
_SKILL_NO = ("skill_no", "SkillNo")
_PAD_KEY = ("console_key", "Command")
_AWAKENING = ("awakening_type",)

_COMBO_OWN = _NAME + _WEAPON + _CONSOLE_ONLY + _LEARN_CHECK + _COOL_CHECK
_STEP_OWN = _NAME + _SKILL_NO + _PAD_KEY
_COMMAND_OWN = _NAME + _AWAKENING

Attrs = tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class ComboStep:
    kind: str
    name: str
    # Skill numbers as written; the older layout lists several to try.
    skill_nos: tuple[str, ...]
    # `console_key` (`LT 0 X`), or the older `Command` (`1` to `4`).
    pad_key: str
    # Other attributes, as written (`call_cycle_time`, `require_mp`, ...).
    attrs: Attrs


@dataclass(frozen=True)
class Combo:
    name: str
    # The last section title comment above it, and the plain comment right above it.
    section: str
    note: str
    weapon: str
    console_only: str
    learn_check: tuple[str, ...]
    cool_check: tuple[str, ...]
    attrs: Attrs
    steps: tuple[ComboStep, ...]


@dataclass(frozen=True)
class SkillCommand:
    name: str
    awakening_type: str
    attrs: Attrs
    # (key, starttime, endtime) of each `<command>`, in file order.
    keys: tuple[tuple[str, str, str], ...]


@dataclass(frozen=True)
class ComboList:
    combos: tuple[Combo, ...]
    commands: tuple[SkillCommand, ...]


def _attr(node: XmlNode, names: tuple[str, ...]) -> str:
    return next((node.attr(name) for name in names if node.has_attr(name)), "")


def _other_attrs(node: XmlNode, own: tuple[str, ...]) -> Attrs:
    skip = {name.lower() for name in own}
    return tuple((key, value) for key, value in node.attrs.items() if key.lower() not in skip)


def _numbers(value: str) -> tuple[str, ...]:
    return tuple(value.split())


def _children(document: XmlNode, list_name: str, item_name: str) -> list[XmlNode]:
    return [
        child
        for node in document.children if node.name == list_name
        for child in node.children if child.name == item_name
    ]


def parse_combo_list(text: str) -> ComboList:
    """Combos and skill commands of the file, in file order."""
    document = parse_xml(text)
    combos: list[Combo] = []
    section = ""
    for node in (child for root in document.children if root.name == _COMBO_LIST for child in root.children):
        section, note = section_and_note(node.comments, section)
        if node.name == _COMBO:
            combos.append(_combo(node, section, note))
    return ComboList(
        combos=tuple(combos),
        commands=tuple(_command(node) for node in _children(document, _COMMAND_LIST, _COMMAND)),
    )


def _combo(node: XmlNode, section: str, note: str) -> Combo:
    return Combo(
        name=_attr(node, _NAME),
        section=section,
        note=note,
        weapon=_attr(node, _WEAPON),
        console_only=_attr(node, _CONSOLE_ONLY),
        learn_check=_numbers(_attr(node, _LEARN_CHECK)),
        cool_check=_numbers(_attr(node, _COOL_CHECK)),
        attrs=_other_attrs(node, _COMBO_OWN),
        steps=tuple(_step(child) for child in node.children if child.name in (STEP_SKILL, STEP_MOVE)),
    )


def _step(node: XmlNode) -> ComboStep:
    return ComboStep(
        kind=node.name,
        name=_attr(node, _NAME),
        skill_nos=_numbers(_attr(node, _SKILL_NO)),
        pad_key=_attr(node, _PAD_KEY),
        attrs=_other_attrs(node, _STEP_OWN),
    )


def _command(node: XmlNode) -> SkillCommand:
    return SkillCommand(
        name=_attr(node, _NAME),
        awakening_type=_attr(node, _AWAKENING),
        attrs=_other_attrs(node, _COMMAND_OWN),
        keys=tuple(
            (child.attr("key"), child.attr("starttime"), child.attr("endtime"))
            for child in node.children if child.name == _KEY
        ),
    )
