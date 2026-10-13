"""An `.ai` script read as states: the `<state>` and `<handler>` elements under `<root>`.

A state runs its `<start>` children once on entry, its other children every
`CallCycleTime` ms, and its `<end>` children on leaving. A child with a
`state` attribute (`changeState`, `findTarget`, ...) is a transition to that
state; its own children are the conditions that must all hold. A handler
(`HandleTakeDamage`, ...) runs its children when the event happens.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

from _ai.xml_tree import XmlNode, parse_xml

KIND_STATE = "state"
KIND_HANDLER = "handler"

PHASE_START = "start"
PHASE_TICK = "tick"
PHASE_END = "end"

# State attributes whose value names the state to go to when the action ends
# (`exit`) or on an event, compared without case.
EDGE_ATTRS = frozenset({
    "exit", "complete", "targetlost", "targethit",
    "failfindpath", "failbycurvedpath", "failbyrestrict",
})
# Attributes a state row shows in their own columns.
_OWN_ATTRS = frozenset({"name", "behavior", "action", "callcycletime"})

# A comment with a run of these is a section title such as
# `<!-- ■■■ 비전투 상태 ■■■ -->` or `<!-- 비 전투 상태 ----- -->`.
_DECORATION = re.compile(r"■|[-=*#~]{3,}")
_DECORATION_CHARS = "■□◆◇●○★☆▶▷◀◁-=*#~ "


@dataclass(frozen=True)
class AiState:
    kind: str
    name: str
    # The last section title comment above it, and the plain comment right above it.
    section: str
    note: str
    behavior: str
    action: str
    cycle: str
    # Other attributes, as written.
    attrs: tuple[tuple[str, str], ...]
    # (attribute as written, target state) for the EDGE_ATTRS.
    edges: tuple[tuple[str, str], ...]
    # (phase, node) in file order within each phase: start, tick, end.
    steps: tuple[tuple[str, XmlNode], ...]


def is_transition(node: XmlNode) -> bool:
    return node.has_attr("state")


def parse_script(text: str) -> list[AiState]:
    """States and handlers of the script, in file order."""
    document = parse_xml(text)
    root = next((node for node in document.children if node.name == "root"), document)
    states: list[AiState] = []
    section = ""
    for node in root.children:
        section, note = _section_and_note(node.comments, section)
        if node.name in (KIND_STATE, KIND_HANDLER):
            states.append(_state(node, section, note))
    return states


def _section_and_note(comments: tuple[str, ...], section: str) -> tuple[str, str]:
    note = ""
    for comment in comments:
        if _DECORATION.search(comment):
            title = comment.strip(_DECORATION_CHARS)
            if title:
                section, note = title, ""
        else:
            note = comment
    return section, note


def _state(node: XmlNode, section: str, note: str) -> AiState:
    edges = tuple((key, value) for key, value in node.attrs.items() if key.lower() in EDGE_ATTRS)
    attrs = tuple(
        (key, value) for key, value in node.attrs.items()
        if key.lower() not in EDGE_ATTRS and key.lower() not in _OWN_ATTRS
    )
    return AiState(
        kind=node.name,
        name=node.attr("name"),
        section=section,
        note=note,
        behavior=node.attr("behavior"),
        action=node.attr("action"),
        cycle=node.attr("callcycletime"),
        attrs=attrs,
        edges=edges,
        steps=_steps(node),
    )


def _steps(node: XmlNode) -> tuple[tuple[str, XmlNode], ...]:
    """The children by phase: `<start>` ones, then every-cycle ones, then `<end>` ones."""
    phases: dict[str, list[XmlNode]] = {PHASE_START: [], PHASE_TICK: [], PHASE_END: []}
    for child in node.children:
        if child.name in (PHASE_START, PHASE_END):
            phases[child.name].extend(child.children)
        else:
            phases[PHASE_TICK].append(child)
    return tuple((phase, child) for phase, children in phases.items() for child in children)
