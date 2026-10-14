"""One record per state or handler, in file order.

The plain fields (`runs`, `transitions`, `reached_from`, ...) are text for tab
search and CSV; the `_` fields hold the same steps as dicts for the table.
`_script` is one dict shared by every record, with what belongs to the whole
script (macros, imports, the characters that run it), so the summary reads it
on any page.
"""
from __future__ import annotations

from .script import PHASE_END, PHASE_START, PHASE_TICK, AiScript, AiState
from .steps import STEP_TRANSITION, hp_variables, step_dicts, step_text

_PHASES = (PHASE_START, PHASE_TICK, PHASE_END)


def script_records(script: AiScript, strings: dict, users: list[tuple[int, str]]) -> list[dict]:
    """`users` are the (character ID, name) pairs that run the script."""
    states = script.states
    hp_vars = hp_variables(states)
    incoming = reached_from(states)
    shared = {
        "macros": [list(macro) for macro in script.macros],
        "imports": list(script.imports),
        "users": [list(user) for user in users],
    }
    records = []
    for state in states:
        steps = step_dicts(state, hp_vars, strings["hp"])
        sources = incoming.get(state.name, [])
        records.append({
            "state": state.name,
            "kind": state.kind,
            "section": state.section,
            "note": state.note,
            "behavior": state.behavior,
            "action": state.action,
            "cycle_ms": _milliseconds(state.cycle),
            "attributes": " ".join(f"{key}={value}" for key, value in state.attrs),
            "runs": _runs_text(steps, strings["phases"]),
            "transitions": _transitions_text(steps, state.edges),
            "reached_from": ", ".join(sources),
            "_steps": steps,
            "_edges": [list(edge) for edge in state.edges],
            "_reached_from": sources,
            "_script": shared,
        })
    return records


def _milliseconds(value: str) -> int | None:
    """`CallCycleTime` as a number, None when it is missing or not a whole number."""
    text = value.strip()
    return int(text) if text.isdigit() else None


def is_run_step(step: dict) -> bool:
    """True for a step the Runs column shows: every `start` and `end` step,
    and the every-cycle steps that are not transitions."""
    return step["phase"] != PHASE_TICK or step["type"] != STEP_TRANSITION


def reached_from(states: tuple[AiState, ...]) -> dict[str, list[str]]:
    """Target state -> the states and handlers that lead to it, in file order, itself left out."""
    sources: dict[str, dict[str, None]] = {}
    for state in states:
        targets = [node.attr("state") for _, node in state.steps if node.has_attr("state")]
        targets += [target for _, target in state.edges]
        for target in targets:
            if target != state.name:
                sources.setdefault(target, {})[state.name] = None
    return {target: list(names) for target, names in sources.items()}


def _runs_text(steps: list[dict], labels: dict[str, str]) -> str:
    blocks = []
    for phase in _PHASES:
        texts = [step_text(step) for step in steps if step["phase"] == phase and is_run_step(step)]
        if texts:
            blocks.append(f"{labels[phase]}: " + "; ".join(texts))
    return " | ".join(blocks)


def _transitions_text(steps: list[dict], edges: tuple[tuple[str, str], ...]) -> str:
    texts = [step_text(step) for step in steps if not is_run_step(step)]
    texts += [f"{key} → {target}" for key, target in edges]
    return "; ".join(texts)
