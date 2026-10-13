"""One record per combo, in file order.

The plain fields (`learn_check`, `steps`, ...) are text for tab search and
CSV; the `_` fields hold the same values as lists and dicts for the table.
`_file` is one dict shared by every record with the file's skill command
count, so the summary reads it on any page.
Skill numbers carry their names (LOC type 10, then the Korean `skilltype.dbss`
name), and each step the keys of every `<skill_command>` of its name.
"""
from __future__ import annotations

from _common.skill import skill_name

from .combolist import Attrs, Combo, ComboList, ComboStep, SkillCommand

_TRUE = "true"
_FALSE = "false"


def combo_records(combo_list: ComboList, strings: dict) -> list[dict]:
    commands = commands_by_name(combo_list.commands)
    shared = {"commands": len(combo_list.commands)}
    return [{**_record(combo, commands, strings), "_file": shared} for combo in combo_list.combos]


def commands_by_name(commands: tuple[SkillCommand, ...]) -> dict[str, list[SkillCommand]]:
    """Action name in lower case -> its skill commands, in file order."""
    by_name: dict[str, list[SkillCommand]] = {}
    for command in commands:
        by_name.setdefault(command.name.lower(), []).append(command)
    return by_name


def _attrs_text(attrs: Attrs) -> str:
    return " ".join(f"{key}={value}" for key, value in attrs)


def _skills(numbers: tuple[str, ...]) -> list[list[str]]:
    """[number, name] per skill number; the name is '' when there is none."""
    return [[number, skill_name(int(number)) if number.isdigit() else ""] for number in numbers]


def skills_text(skills: list[list[str]]) -> str:
    return ", ".join(f"{number} {name}".strip() for number, name in skills)


def _console_only(value: str) -> bool | None:
    text = value.strip().lower()
    return True if text == _TRUE else False if text == _FALSE else None


def keys_text(keys: tuple[tuple[str, str, str], ...]) -> str:
    """`Shift 0-300 + W 100-300`: each key with the milliseconds it is held."""
    return " + ".join(f"{key} {start}-{end}" for key, start, end in keys)


def _command_dict(command: SkillCommand, strings: dict) -> dict:
    return {
        "awakening": command.awakening_type,
        "awakening_text": strings["awakening"].get(command.awakening_type, command.awakening_type),
        "keys": keys_text(command.keys),
        "attrs": _attrs_text(command.attrs),
    }


def _step_dict(step: ComboStep, commands: dict[str, list[SkillCommand]], strings: dict) -> dict:
    return {
        "kind": step.kind,
        "name": step.name,
        "skills": _skills(step.skill_nos),
        "pad_key": step.pad_key,
        "attrs": _attrs_text(step.attrs),
        "commands": [_command_dict(command, strings) for command in commands.get(step.name.lower(), [])],
    }


def step_text(step: dict) -> str:
    """`BT_ATTACK_S1_1 349 Forward Slash I LT 0 X call_cycle_time=1000 [C 0-200]`."""
    parts = [step["name"], skills_text(step["skills"]), step["pad_key"], step["attrs"]]
    parts += [f"[{command['keys']}]" for command in step["commands"]]
    return " ".join(part for part in parts if part)


def _record(combo: Combo, commands: dict[str, list[SkillCommand]], strings: dict) -> dict:
    learn = _skills(combo.learn_check)
    cool = _skills(combo.cool_check)
    steps = [_step_dict(step, commands, strings) for step in combo.steps]
    weapon = combo.weapon.strip()
    return {
        "combo": combo.name,
        "section": combo.section,
        "note": combo.note,
        "weapon": int(weapon) if weapon.isdigit() else None,
        "weapon_text": strings["weapons"].get(weapon, weapon),
        "console_only": _console_only(combo.console_only),
        "learn_check": skills_text(learn),
        "cool_check": skills_text(cool),
        "attributes": _attrs_text(combo.attrs),
        "steps": "; ".join(step_text(step) for step in steps),
        "_learn": learn,
        "_cool": cool,
        "_steps": steps,
    }
