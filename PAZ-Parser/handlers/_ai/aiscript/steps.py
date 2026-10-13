"""The children of a state as plain dicts: actions, transitions and their conditions.

The dicts go into the records (display-only `_steps`), so the table and the
text columns that search and CSV read are built from the same values.
"""
from __future__ import annotations

from collections.abc import Iterable

from _ai.xml_tree import XmlNode
from .script import AiState, is_transition

STEP_ACTION = "action"
STEP_TRANSITION = "transition"
# Starts the text of a `<variable>` action: `var _HP = 100`.
VARIABLE_PREFIX = "var"

# The tag a plain transition uses; others (`findTarget`, ...) are named on the line.
_CHANGE_STATE = "changestate"
_HP_EXPRESSION = "gethprate()"
_OPS = {"<=": "≤", ">=": "≥", "==": "=", "!=": "≠"}
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


def _attr_text(node: XmlNode, skip: frozenset[str] = frozenset()) -> list[str]:
    return [f"{key}={value}" for key, value in node.attrs.items() if key.lower() not in skip]


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
        "conditions": [condition_dict(child, hp_vars, hp_label) for child in node.children],
    }


def condition_dict(node: XmlNode, hp_vars: frozenset[str], hp_label: str) -> dict:
    """`{"text": "HP ≤ 70%", "hp": True, "gate": True}`.

    `hp` marks a condition on an HP variable; `gate` leaves out `HP ≤ 100%`,
    which always holds.
    """
    is_variable = node.name == "variable" and node.has_attr("name")
    is_hp = is_variable and node.attr("name") in hp_vars
    subject = hp_label if is_hp else node.attr("name") if is_variable else node.tag
    unit = "%" if is_hp else ""
    cmp, value = node.attr("cmp"), node.attr("value")

    parts = [subject]
    if node.has_attr("cmp"):
        parts.append(f"{_OPS.get(cmp, cmp)} {value}{unit}")
    elif node.has_attr("min") or node.has_attr("max"):
        parts.append(f"{node.attr('min')}…{node.attr('max')}{unit}")
    elif node.has_attr("value"):
        parts.append(f"= {value}{unit}")
    parts += _attr_text(node, _VARIABLE_CONDITION_SHOWN_APART if is_variable else _CONDITION_SHOWN_APART)

    is_always = cmp == "<=" and value == "100"
    return {"text": " ".join(parts), "hp": is_hp, "gate": is_hp and not is_always}


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
