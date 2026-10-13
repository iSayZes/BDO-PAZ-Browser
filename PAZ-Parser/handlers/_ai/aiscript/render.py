"""HTML of the AI Script view: the summary over the table, and the table cells.

State names are buttons with `data-action="goto-record"` and the target's
record index; ui/js/features/preview-views.js pages to that row and marks it.
Styles: ui/css/26-ai-script.css.
"""
from __future__ import annotations

from ui_text import fill_placeholders

from _common.html import e

from .records import is_run_step
from .script import KIND_HANDLER, PHASE_END, PHASE_START, PHASE_TICK
from .steps import STEP_TRANSITION, VARIABLE_PREFIX

_INITIAL_STATE = "InitialState"
_EMPTY = '<span class="ai-dim">-</span>'
_PHASES = (PHASE_START, PHASE_TICK, PHASE_END)


def record_index(records: list[dict]) -> dict[str, int]:
    """State name -> its record's index; the first record wins a repeated name."""
    index: dict[str, int] = {}
    for position, record in enumerate(records):
        index.setdefault(record["state"], position)
    return index


class ScriptRenderer:
    """Cells and summary of one script, with its name index and strings."""

    def __init__(self, records: list[dict], strings: dict) -> None:
        self._records = records
        self._strings = strings
        self._index = record_index(records)

    # ── Links and chips ──────────────────────────────────────────────────────

    def state_link(self, name: str) -> str:
        position = self._index.get(name)
        if position is None:
            title = e(self._strings["missingState"])
            return f'<span class="ai-state-link missing" title="{title}">{e(name) or "-"}</span>'
        return (
            f'<button type="button" class="ai-state-link" data-action="goto-record" '
            f'data-record="{position}">{e(name)}</button>'
        )

    @staticmethod
    def _chip(text: str, is_hp: bool = False) -> str:
        return f'<span class="ai-cond{" hp" if is_hp else ""}">{e(text)}</span>'

    def _transition_line(self, step: dict) -> str:
        parts = ['<span class="ai-arrow">→</span>', self.state_link(step["to"])]
        if step["tag"]:
            parts.append(f'<span class="ai-kind">{e(step["tag"])}</span>')
        if step["dice"]:
            parts.append(f'<span class="ai-dice">dice {e(step["dice"])}</span>')
        if step["extra"]:
            parts.append(self._chip(step["extra"]))
        parts += [self._chip(c["text"], c["hp"]) for c in step["conditions"]]
        return f'<div class="ai-transition">{"".join(parts)}</div>'

    def _step_line(self, step: dict) -> str:
        if step["type"] == STEP_TRANSITION:
            return self._transition_line(step)
        return f'<div class="ai-action{" hp" if step["hp"] else ""}">{e(step["text"])}</div>'

    # ── Cells ────────────────────────────────────────────────────────────────

    def id_cell(self, record: dict, section: str) -> str:
        head = f'<div class="ai-section">{e(section)}</div>' if section else ""
        note = f'<div class="ai-note">{e(record["note"])}</div>' if record["note"] else ""
        return f'{head}<div class="ai-name">{e(record["state"])}</div>{note}'

    def behavior_cell(self, record: dict) -> str:
        is_handler = record["kind"] == KIND_HANDLER
        behavior = self._strings["handler"] if is_handler else record["behavior"]
        lines = [f"<div>{e(behavior)}</div>" if behavior else ""]
        lines += [f'<div class="ai-detail">{e(text)}</div>' for text in (record["action"], record["attributes"]) if text]
        return "".join(lines) or _EMPTY

    def runs_cell(self, record: dict) -> str:
        labels = self._strings["phases"]
        blocks = []
        for phase in _PHASES:
            steps = [step for step in record["_steps"] if step["phase"] == phase and is_run_step(step)]
            if steps:
                lines = "".join(self._step_line(step) for step in steps)
                blocks.append(f'<div class="ai-block"><div class="ai-phase">{e(labels[phase])}</div>{lines}</div>')
        return "".join(blocks) or _EMPTY

    def transitions_cell(self, record: dict) -> str:
        lines = [self._transition_line(step) for step in record["_steps"] if not is_run_step(step)]
        lines += [
            f'<div class="ai-transition"><span class="ai-edge">{e(key)}</span>'
            f'<span class="ai-arrow">→</span>{self.state_link(target)}</div>'
            for key, target in record["_edges"]
        ]
        return "".join(lines) or _EMPTY

    def reached_from_cell(self, record: dict) -> str:
        sources = record["_reached_from"]
        if not sources:
            text = self._strings["event"] if record["kind"] == KIND_HANDLER else "-"
            return f'<span class="ai-dim">{e(text)}</span>'
        return f'<div class="ai-links">{"".join(self.state_link(name) for name in sources)}</div>'

    # ── Summary ──────────────────────────────────────────────────────────────

    def summary(self) -> str:
        labels = self._strings["summary"]
        return (
            '<div class="ai-summary">'
            f'{self._box(labels["script"], self._counts())}'
            f'{self._box(labels["hpGates"], self._hp_gates())}'
            f'{self._box(labels["variables"], self._variables())}'
            '</div>'
        )

    @staticmethod
    def _box(title: str, body: str) -> str:
        return f'<div class="ai-box"><div class="ai-box-title">{e(title)}</div>{body}</div>'

    def _counts(self) -> str:
        labels = self._strings["summary"]
        handlers = sum(1 for r in self._records if r["kind"] == KIND_HANDLER)
        transitions = sum(
            sum(1 for step in r["_steps"] if step["type"] == STEP_TRANSITION) + len(r["_edges"])
            for r in self._records
        )
        counts = [
            (len(self._records) - handlers, labels["states"]),
            (handlers, labels["handlers"]),
            (transitions, labels["transitions"]),
        ]
        items = "".join(f'<div class="ai-count"><b>{count:,}</b><span>{e(label)}</span></div>' for count, label in counts)
        return f'<div class="ai-counts">{items}</div>'

    def _hp_gates(self) -> str:
        """Transitions behind an HP condition, one line per (condition, target)."""
        gates: dict[tuple[str, str], dict[str, None]] = {}
        for record in self._records:
            for step in record["_steps"]:
                if step["type"] != STEP_TRANSITION:
                    continue
                for condition in step["conditions"]:
                    if condition["gate"]:
                        gates.setdefault((condition["text"], step["to"]), {})[record["state"]] = None
        if not gates:
            return f'<div class="ai-dim">{e(self._strings["summary"]["none"])}</div>'
        from_text = self._strings["summary"]["from"]
        lines = "".join(
            f'<li>{self._chip(text, True)}<span class="ai-arrow">→</span>{self.state_link(target)}'
            f'<span class="ai-from">{e(fill_placeholders(from_text, names=", ".join(sources)))}</span></li>'
            for (text, target), sources in gates.items()
        )
        return f'<ul class="ai-gates">{lines}</ul>'

    def _variables(self) -> str:
        initial = next((r for r in self._records if r["state"] == _INITIAL_STATE), None)
        steps = [] if initial is None else [
            step for step in initial["_steps"] if step["type"] != STEP_TRANSITION and step["tag"].lower() == "variable"
        ]
        if not steps:
            return f'<div class="ai-dim">{e(self._strings["summary"]["none"])}</div>'
        chips = "".join(self._chip(step["text"].removeprefix(f"{VARIABLE_PREFIX} "), step["hp"]) for step in steps)
        return f'<div class="ai-vars">{chips}</div>'
