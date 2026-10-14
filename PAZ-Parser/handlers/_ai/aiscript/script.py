"""An `.ai` script read as states: the `<state>` and `<handler>` elements under `<root>`.

A state runs its `<start>` children once on entry, its other children every
`CallCycleTime` ms, and its `<end>` children on leaving. A child with a
`state` attribute (`changeState`, `findTarget`, ...) is a transition to that
state; its own children are the conditions that must all hold. A handler
(`HandleTakeDamage`, ...) runs its children when the event happens.

Under `<root>` next to them: `<macro_value_define>` names expressions that a
`compute expr` can use (`Protected_Check="0 == (...)"`), and `<import
filepath="/Summon/Horse.ai"/>` pulls in the states of another script.
"""
from __future__ import annotations

from dataclasses import dataclass

from _ai.sections import section_and_note
from _ai.xml_tree import XmlNode, parse_xml

KIND_STATE = "state"
KIND_HANDLER = "handler"
_MACROS = "macro_value_define"
_IMPORT = "import"

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


@dataclass(frozen=True)
class AiScript:
    states: tuple[AiState, ...]
    # (name, expression) of every `<macro_value_define>` attribute, in file order.
    macros: tuple[tuple[str, str], ...]
    # `filepath` of every `<import>`, as written.
    imports: tuple[str, ...]


def is_transition(node: XmlNode) -> bool:
    return node.has_attr("state")


def parse_script(text: str) -> AiScript:
    """States and handlers of the script in file order, with its macros and imports."""
    document = parse_xml(text)
    root = next((node for node in document.children if node.name == "root"), document)
    states: list[AiState] = []
    section = ""
    for node in root.children:
        section, note = section_and_note(node.comments, section)
        if node.name in (KIND_STATE, KIND_HANDLER):
            states.append(_state(node, section, note))
    return AiScript(
        states=tuple(states),
        macros=tuple(
            (key, value) for node in root.children if node.name == _MACROS for key, value in node.attrs.items()
        ),
        imports=tuple(node.attr("filepath") for node in root.children if node.name == _IMPORT),
    )


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
