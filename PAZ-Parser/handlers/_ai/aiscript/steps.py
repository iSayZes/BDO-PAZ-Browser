"""The children of a state as plain dicts: actions, transitions and their conditions.

The dicts go into the records (display-only `_steps`), so the table and the
text columns that search and CSV read are built from the same values.
"""
from __future__ import annotations

import re
from collections.abc import Iterable, Sequence

from _ai.xml_tree import XmlNode
from _common.character import character_name
from .script import AiState, is_transition

STEP_ACTION = "action"
STEP_TRANSITION = "transition"
# Starts the text of a `<variable>` action: `var _HP = 100`.
VARIABLE_PREFIX = "var"

# The tag a plain transition uses; others (`findTarget`, ...) are named on the line.
_CHANGE_STATE = "changestate"
_HP_EXPRESSION = "gethprate()"
_OPS = {"<=": "≤", ">=": "≥", "==": "=", "!=": "≠"}
# A lower bound as read from the left of a range: `distance > 300` is `300 < distance`.
_LOWER_BOUNDS = {">": "<", ">=": "≤"}
_UPPER_BOUNDS = frozenset({"<", "<="})
# Attributes and condition tags that end in this hold character IDs
# (`summonCharacter characterKey`, `target_characterKey`), several joined by `|`.
_CHARACTER_KEY = "characterkey"
_LIST_SEPARATOR = "|"
_NUMBER = re.compile(r"-?\d+(?:\.\d+)?")
# Transition attributes not repeated on the line: the target, the dice chip,
# and the animation blend time.
_TRANSITION_SHOWN_APART = frozenset({"state", "dice", "blendtime"})
_CONDITION_SHOWN_APART = frozenset({"cmp", "value", "min", "max"})
_VARIABLE_CONDITION_SHOWN_APART = _CONDITION_SHOWN_APART | {"name"}
_VARIABLE_SHOWN_APART = frozenset({"name", "value"})


def hp_variables(states: Iterable[AiState]) -> frozenset[str]:
    """Variables a `compute` fills with `getHpRate()`.

    A condition on one of them compares percent of max HP, so it shows as
    `HP ≤ 70%`.
    """
    return frozenset(
        node.attr("dest")
        for state in states
        for _, node in state.steps
        if node.name == "compute" and node.attr("expr").replace(" ", "").lower() == _HP_EXPRESSION
    )


def step_dicts(state: AiState, hp_vars: frozenset[str], hp_label: str) -> list[dict]:
    return [
        _transition(phase, node, hp_vars, hp_label) if is_transition(node) else _action(phase, node, hp_vars)
        for phase, node in state.steps
    ]


def _is_character_key(name: str) -> bool:
    return name.lower().endswith(_CHARACTER_KEY)


def character_ids_text(value: str) -> str:
    """Character IDs with their names: `28494 (Kzarka)`, several joined by ` | `.

    An ID without a name in the loaded LOC, or any value that is not a whole
    number, stays as written.
    """
    parts = []
    for part in value.split(_LIST_SEPARATOR):
        name = character_name(int(part)) if part.strip().isdigit() else ""
        parts.append(f"{part} ({name})" if name else part)
    return f" {_LIST_SEPARATOR} ".join(parts)


def _attr_text(node: XmlNode, skip: frozenset[str] = frozenset()) -> list[str]:
    return [
        f"{key}={character_ids_text(value) if _is_character_key(key) else value}"
        for key, value in node.attrs.items()
        if key.lower() not in skip
    ]


def _action(phase: str, node: XmlNode, hp_vars: frozenset[str]) -> dict:
    """`{"text": "_HP = getHpRate()", "hp": True, ...}`; `hp` marks an HP variable."""
    variable = ""
    if node.name == "compute" and node.has_attr("dest"):
        variable = node.attr("dest")
        text = f"{variable} = {node.attr('expr')}"
    elif node.name == "variable" and node.has_attr("name"):
        variable = node.attr("name")
        value = [f"= {node.attr('value')}"] if node.has_attr("value") else []
        text = " ".join([VARIABLE_PREFIX, variable, *value, *_attr_text(node, _VARIABLE_SHOWN_APART)])
    else:
        text = " ".join([node.tag, *_attr_text(node)])
    return {"phase": phase, "type": STEP_ACTION, "tag": node.tag, "text": text, "hp": variable in hp_vars}


def _transition(phase: str, node: XmlNode, hp_vars: frozenset[str], hp_label: str) -> dict:
    extra = " ".join(_attr_text(node, _TRANSITION_SHOWN_APART))
    return {
        "phase": phase,
        "type": STEP_TRANSITION,
        "tag": "" if node.name == _CHANGE_STATE else node.tag,
        "to": node.attr("state"),
        "dice": node.attr("dice"),
        "extra": extra,
        "conditions": condition_dicts(node.children, hp_vars, hp_label),
    }


def _is_variable(node: XmlNode) -> bool:
    return node.name == "variable" and node.has_attr("name")


def _is_hp(node: XmlNode, hp_vars: frozenset[str]) -> bool:
    return _is_variable(node) and node.attr("name") in hp_vars


def _subject(node: XmlNode, hp_vars: frozenset[str], hp_label: str) -> str:
    """What a condition tests: `HP` for an HP variable, a variable's name, else the tag."""
    if _is_hp(node, hp_vars):
        return hp_label
    return node.attr("name") if _is_variable(node) else node.tag


def condition_dicts(nodes: Sequence[XmlNode], hp_vars: frozenset[str], hp_label: str) -> list[dict]:
    """The conditions of one transition, in file order.

    A subject with exactly two conditions, a lower and an upper bound, reads as
    one range in the place of the first: `300 < distance ≤ 500`.
    """
    by_subject: dict[str, list[int]] = {}
    for position, node in enumerate(nodes):
        by_subject.setdefault(_subject(node, hp_vars, hp_label).lower(), []).append(position)

    ranges: dict[int, dict] = {}
    for positions in by_subject.values():
        bounds = _range_bounds([nodes[position] for position in positions])
        if bounds is not None:
            ranges[positions[0]] = _range_dict(*bounds, hp_vars, hp_label)
    merged_away = {positions[1] for positions in by_subject.values() if positions[0] in ranges}
    return [
        ranges.get(position) or condition_dict(node, hp_vars, hp_label)
        for position, node in enumerate(nodes)
        if position not in merged_away
    ]


def _is_plain_comparison(node: XmlNode) -> bool:
    """Only `cmp` and `value` (and a variable's `name`), so nothing is lost in a range."""
    shown_apart = _VARIABLE_CONDITION_SHOWN_APART if _is_variable(node) else _CONDITION_SHOWN_APART
    return node.has_attr("cmp") and node.has_attr("value") and not _attr_text(node, shown_apart)


def _range_bounds(nodes: list[XmlNode]) -> tuple[XmlNode, XmlNode] | None:
    """(lower, upper) when the two conditions on one subject bound it from both sides."""
    if len(nodes) != 2 or not all(_is_plain_comparison(node) for node in nodes):
        return None
    lower = next((node for node in nodes if node.attr("cmp") in _LOWER_BOUNDS), None)
    upper = next((node for node in nodes if node.attr("cmp") in _UPPER_BOUNDS), None)
    return None if lower is None or upper is None else (lower, upper)


def _with_unit(value: str, is_hp: bool) -> str:
    """`70%` for a number compared with HP; a variable name (`AI_Warp_HP`) stays as written."""
    return f"{value}%" if is_hp and _NUMBER.fullmatch(value.strip()) else value


def _range_dict(lower: XmlNode, upper: XmlNode, hp_vars: frozenset[str], hp_label: str) -> dict:
    is_hp = _is_hp(lower, hp_vars)
    low_cmp, high_cmp = lower.attr("cmp"), upper.attr("cmp")
    text = (
        f"{_with_unit(lower.attr('value'), is_hp)} {_LOWER_BOUNDS[low_cmp]} {_subject(lower, hp_vars, hp_label)} "
        f"{_OPS.get(high_cmp, high_cmp)} {_with_unit(upper.attr('value'), is_hp)}"
    )
    return {"text": text, "hp": is_hp, "gate": is_hp, "wrap": False}


def condition_dict(node: XmlNode, hp_vars: frozenset[str], hp_label: str) -> dict:
    """`{"text": "HP ≤ 70%", "hp": True, "gate": True, "wrap": False}`.

    `hp` marks a condition on an HP variable; `gate` leaves out `HP ≤ 100%`,
    which always holds. `wrap` marks a list value (`Wait|Move_Random`), which
    may break across lines.
    """
    is_variable = _is_variable(node)
    is_hp = _is_hp(node, hp_vars)
    cmp, value = node.attr("cmp"), node.attr("value")
    if _is_character_key(node.tag):
        value = character_ids_text(value)

    parts = [_subject(node, hp_vars, hp_label)]
    if node.has_attr("cmp"):
        parts.append(f"{_OPS.get(cmp, cmp)} {_with_unit(value, is_hp)}")
    elif node.has_attr("min") or node.has_attr("max"):
        parts.append(f"{node.attr('min')}…{_with_unit(node.attr('max'), is_hp)}")
    elif node.has_attr("value"):
        parts.append(f"= {_with_unit(value, is_hp)}")
    parts += _attr_text(node, _VARIABLE_CONDITION_SHOWN_APART if is_variable else _CONDITION_SHOWN_APART)

    is_always = cmp == "<=" and value == "100"
    return {
        "text": " ".join(parts),
        "hp": is_hp,
        "gate": is_hp and not is_always,
        "wrap": _LIST_SEPARATOR in value,
    }


def transition_text(step: dict) -> str:
    """One transition as text: `Attack_SwingL findTarget dice 30 (distance ≤ 450, HP ≤ 70%)`."""
    parts = [f"→ {step['to']}"]
    if step["tag"]:
        parts.append(step["tag"])
    if step["dice"]:
        parts.append(f"dice {step['dice']}")
    if step["extra"]:
        parts.append(step["extra"])
    if step["conditions"]:
        parts.append("(" + ", ".join(c["text"] for c in step["conditions"]) + ")")
    return " ".join(parts)


def step_text(step: dict) -> str:
    return transition_text(step) if step["type"] == STEP_TRANSITION else step["text"]
