"""The boxes over the AI Script table: counts, HP gates, variables, and what
belongs to the whole script (the characters that run it, macros, imports).

The last three show only when the script has them. A character that runs the
script links to its `characterstatic.dbss` row (`data-action="open-record"`,
ui/js/features/preview-views.js). Styles: ui/css/26-ai-script.css.
"""
from __future__ import annotations

from ui_text import fill_placeholders

from _common.html import e, hidden_slice, html_list_cell, record_link, truncate
from _common.lookup_builders import CHARACTERSTATIC

from .render import ScriptRenderer
from .script import KIND_HANDLER
from .steps import STEP_TRANSITION, VARIABLE_PREFIX

_INITIAL_STATE = "InitialState"
# Characters listed before the `... (+N)` marker; `9999` runs on thousands.
_MAX_USERS = 40
# A macro expression is one long line; the box shows its start, the tooltip all of it.
_MAX_EXPRESSION_CHARS = 160


def summary_html(renderer: ScriptRenderer) -> str:
    labels = renderer.strings["summary"]
    shared = renderer.records[0]["_script"] if renderer.records else {}
    boxes = [
        _box(labels["script"], _counts(renderer)),
        _box(labels["hpGates"], _hp_gates(renderer)),
        _box(labels["variables"], _variables(renderer)),
    ]
    if shared.get("users"):
        boxes.append(_box(labels["usedBy"], _users(shared["users"])))
    if shared.get("macros"):
        boxes.append(_box(labels["macros"], _macros(shared["macros"])))
    if shared.get("imports"):
        boxes.append(_box(labels["imports"], _imports(shared["imports"])))
    return f'<div class="ai-summary">{"".join(boxes)}</div>'


def _box(title: str, body: str) -> str:
    return f'<div class="ai-box"><div class="ai-box-title">{e(title)}</div>{body}</div>'


def _none(renderer: ScriptRenderer) -> str:
    return f'<div class="ai-dim">{e(renderer.strings["summary"]["none"])}</div>'


def _counts(renderer: ScriptRenderer) -> str:
    labels = renderer.strings["summary"]
    records = renderer.records
    handlers = sum(1 for r in records if r["kind"] == KIND_HANDLER)
    transitions = sum(
        sum(1 for step in r["_steps"] if step["type"] == STEP_TRANSITION) + len(r["_edges"])
        for r in records
    )
    counts = [
        (len(records) - handlers, labels["states"]),
        (handlers, labels["handlers"]),
        (transitions, labels["transitions"]),
    ]
    items = "".join(f'<div class="ai-count"><b>{count:,}</b><span>{e(label)}</span></div>' for count, label in counts)
    return f'<div class="ai-counts">{items}</div>'


def _hp_gates(renderer: ScriptRenderer) -> str:
    """Transitions behind an HP condition, one line per (condition, target)."""
    gates: dict[tuple[str, str], dict[str, None]] = {}
    for record in renderer.records:
        for step in record["_steps"]:
            if step["type"] != STEP_TRANSITION:
                continue
            for condition in step["conditions"]:
                if condition["gate"]:
                    gates.setdefault((condition["text"], step["to"]), {})[record["state"]] = None
    if not gates:
        return _none(renderer)
    from_text = renderer.strings["summary"]["from"]
    lines = "".join(
        f'<li>{renderer.chip(text, is_hp=True)}<span class="ai-arrow">→</span>{renderer.state_link(target)}'
        f'<span class="ai-from">{e(fill_placeholders(from_text, names=", ".join(sources)))}</span></li>'
        for (text, target), sources in gates.items()
    )
    return f'<ul class="ai-gates">{lines}</ul>'


def _variables(renderer: ScriptRenderer) -> str:
    initial = next((r for r in renderer.records if r["state"] == _INITIAL_STATE), None)
    steps = [] if initial is None else [
        step for step in initial["_steps"] if step["type"] != STEP_TRANSITION and step["tag"].lower() == "variable"
    ]
    if not steps:
        return _none(renderer)
    chips = "".join(renderer.chip(step["text"].removeprefix(f"{VARIABLE_PREFIX} "), step["hp"]) for step in steps)
    return f'<div class="ai-vars">{chips}</div>'


def _user_text(character_id: int, name: str) -> str:
    return f"{name} ({character_id})" if name else str(character_id)


def _users(users: list[list]) -> str:
    texts = [_user_text(character_id, name) for character_id, name in users]
    chips = [
        record_link(text, CHARACTERSTATIC, "character_id", character_id, "ai-state-link")
        for (character_id, _), text in zip(users[:_MAX_USERS], texts)
    ]
    hidden_count = len(texts) - len(chips)
    cell = html_list_cell(chips, hidden_count, hidden_slice(texts, _MAX_USERS), separator="")
    return f'<div class="ai-vars">{cell}</div>'


def _macros(macros: list[list[str]]) -> str:
    lines = "".join(
        f'<li><span class="ai-cond">{e(name)}</span>'
        f'<span class="ai-expr" title="{e(expression)}">{e(truncate(expression, _MAX_EXPRESSION_CHARS))}</span></li>'
        for name, expression in macros
    )
    return f'<ul class="ai-gates">{lines}</ul>'


def _imports(imports: list[str]) -> str:
    lines = "".join(f'<li class="ai-action">{e(path)}</li>' for path in imports)
    return f'<ul class="ai-gates">{lines}</ul>'
