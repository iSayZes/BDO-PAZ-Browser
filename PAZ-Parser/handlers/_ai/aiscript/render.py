"""HTML of the AI Script view: the table cells and the behavior filter.

State names are buttons with `data-action="goto-record"` and the target's
record index; ui/js/features/preview-views.js pages to that row and marks it.
The behavior chips (`data-action="ai-filter"`) hide the rows of the shown page
whose state name carries another `data-behavior`. The boxes over the table are
in summary.py. Styles: ui/css/26-ai-script.css.
"""
from __future__ import annotations

from collections import Counter

from _common.html import e

from .records import is_run_step
from .script import KIND_HANDLER, PHASE_END, PHASE_START, PHASE_TICK
from .steps import STEP_TRANSITION

_EMPTY = '<span class="ai-dim">-</span>'
_PHASES = (PHASE_START, PHASE_TICK, PHASE_END)
# The filter value of a state without a `behavior` attribute.
_NO_BEHAVIOR = "-"


def record_index(records: list[dict]) -> dict[str, int]:
    """State name -> its record's index; the first record wins a repeated name."""
    index: dict[str, int] = {}
    for position, record in enumerate(records):
        index.setdefault(record["state"], position)
    return index


def behavior_key(record: dict) -> str:
    """The filter value of a row: `handler`, or the state's behavior in lower case."""
    if record["kind"] == KIND_HANDLER:
        return KIND_HANDLER
    return record["behavior"].lower() or _NO_BEHAVIOR


class ScriptRenderer:
    """Cells of one script, with its name index and strings."""

    def __init__(self, records: list[dict], strings: dict) -> None:
        self.records = records
        self.strings = strings
        self._index = record_index(records)

    # ── Links and chips ──────────────────────────────────────────────────────

    def state_link(self, name: str) -> str:
        position = self._index.get(name)
        if position is None:
            title = e(self.strings["missingState"])
            return f'<span class="ai-state-link missing" title="{title}">{e(name) or "-"}</span>'
        return (
            f'<button type="button" class="ai-state-link" data-action="goto-record" '
            f'data-record="{position}">{e(name)}</button>'
        )

    @staticmethod
    def chip(text: str, is_hp: bool = False, is_wrapped: bool = False) -> str:
        classes = "ai-cond" + (" hp" if is_hp else "") + (" wrap" if is_wrapped else "")
        return f'<span class="{classes}">{e(text)}</span>'

    def _transition_line(self, step: dict) -> str:
        parts = ['<span class="ai-arrow">→</span>', self.state_link(step["to"])]
        if step["tag"]:
            parts.append(f'<span class="ai-kind">{e(step["tag"])}</span>')
        if step["dice"]:
            parts.append(f'<span class="ai-dice">dice {e(step["dice"])}</span>')
        if step["extra"]:
            parts.append(self.chip(step["extra"]))
        parts += [self.chip(c["text"], c["hp"], c["wrap"]) for c in step["conditions"]]
        return f'<div class="ai-transition">{"".join(parts)}</div>'

    def _step_line(self, step: dict) -> str:
        if step["type"] == STEP_TRANSITION:
            return self._transition_line(step)
        return f'<div class="ai-action{" hp" if step["hp"] else ""}">{e(step["text"])}</div>'

    # ── Behavior filter ──────────────────────────────────────────────────────

    def filter_bar(self) -> str:
        """One chip per behavior with its row count in the whole script; '' for one behavior."""
        counts = Counter(behavior_key(record) for record in self.records)
        if len(counts) < 2:
            return ""
        labels = self.strings["filter"]
        chips = "".join(
            f'<button type="button" class="ai-chip" data-action="ai-filter" data-value="{e(key)}" '
            f'aria-pressed="false">{e(self.strings["handler"] if key == KIND_HANDLER else key)}'
            f'<span class="ai-chip-count">{count:,}</span></button>'
            for key, count in sorted(counts.items())
        )
        return (
            f'<div class="ai-filter" data-shown="{e(labels["shown"])}">'
            f'<span class="ai-filter-label">{e(labels["label"])}</span>{chips}'
            '<span class="ai-filter-count" aria-live="polite"></span></div>'
        )

    # ── Cells ────────────────────────────────────────────────────────────────

    def id_cell(self, record: dict, section: str) -> str:
        head = f'<div class="ai-section">{e(section)}</div>' if section else ""
        note = f'<div class="ai-note">{e(record["note"])}</div>' if record["note"] else ""
        name = f'<div class="ai-name" data-behavior="{e(behavior_key(record))}">{e(record["state"])}</div>'
        return f"{head}{name}{note}"

    def behavior_cell(self, record: dict) -> str:
        is_handler = record["kind"] == KIND_HANDLER
        behavior = self.strings["handler"] if is_handler else record["behavior"]
        lines = [f"<div>{e(behavior)}</div>" if behavior else ""]
        lines += [f'<div class="ai-detail">{e(text)}</div>' for text in (record["action"], record["attributes"]) if text]
        return "".join(lines) or _EMPTY

    def runs_cell(self, record: dict) -> str:
        labels = self.strings["phases"]
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
            text = self.strings["event"] if record["kind"] == KIND_HANDLER else "-"
            return f'<span class="ai-dim">{e(text)}</span>'
        return f'<div class="ai-links">{"".join(self.state_link(name) for name in sources)}</div>'
