"""HTML of the Combo List view: the summary over the table, and the table cells.

Shares the `ai-*` classes of the AI Script view (ui/css/26-ai-script.css).
A skill number links to its first `skill.dbss` row (`data-action="open-record"`).
"""
from __future__ import annotations

from collections import Counter

from _common.html import e, flag_cell, record_link
from _common.lookup_builders import SKILL

from .combolist import STEP_MOVE

_EMPTY = '<span class="ai-dim">-</span>'


def _chip(text: str) -> str:
    return f'<span class="ai-cond">{e(text)}</span>'


def _skill_chip(number: str, name: str) -> str:
    text = f"{number} {name}".strip()
    return record_link(text, SKILL, "skill_no", number, "ai-state-link") if number.isdigit() else _chip(text)


def _skill_chips(skills: list[list[str]]) -> str:
    return "".join(_skill_chip(number, name) for number, name in skills)


class ComboRenderer:
    def __init__(self, records: list[dict], strings: dict) -> None:
        self.records = records
        self.strings = strings

    # ── Cells ────────────────────────────────────────────────────────────────

    def id_cell(self, record: dict, section: str) -> str:
        head = f'<div class="ai-section">{e(section)}</div>' if section else ""
        note = f'<div class="ai-note">{e(record["note"])}</div>' if record["note"] else ""
        return f'{head}<div class="ai-name">{e(record["combo"])}</div>{note}'

    @staticmethod
    def weapon_cell(record: dict) -> str:
        return e(record["weapon_text"]) if record["weapon_text"] else _EMPTY

    @staticmethod
    def console_only_cell(record: dict) -> str:
        return _EMPTY if record["console_only"] is None else flag_cell(record["console_only"])

    def checks_cell(self, record: dict) -> str:
        """The learned and cooldown skills; one line when the lists are the same."""
        labels = self.strings["checks"]
        learn, cool = record["_learn"], record["_cool"]
        if learn and learn == cool:
            lines = [(labels["both"], learn)]
        else:
            lines = [(label, skills) for label, skills in ((labels["learned"], learn), (labels["cooldown"], cool)) if skills]
        if not lines:
            return _EMPTY
        return "".join(
            f'<div class="ai-transition"><span class="ai-edge">{e(label)}</span>{_skill_chips(skills)}</div>'
            for label, skills in lines
        )

    def steps_cell(self, record: dict) -> str:
        return "".join(self._step(step) for step in record["_steps"]) or _EMPTY

    def _step(self, step: dict) -> str:
        head = [f'<span class="ai-name">{e(step["name"])}</span>']
        if step["kind"] == STEP_MOVE:
            head.append(f'<span class="ai-kind">{e(step["kind"])}</span>')
        head.append(_skill_chips(step["skills"]))
        if step["pad_key"]:
            head.append(f'<span class="ai-dice">{e(step["pad_key"])}</span>')
        lines = [f'<div class="ai-transition">{"".join(head)}</div>']
        if step["attrs"]:
            lines.append(f'<div class="ai-detail">{e(step["attrs"])}</div>')
        is_several = len(step["commands"]) > 1
        for command in step["commands"]:
            awakening = f'<span class="ai-edge">{e(command["awakening_text"])}</span>' if is_several else ""
            lines.append(f'<div class="ai-transition">{awakening}<span class="ai-action">{e(command["keys"])}</span></div>')
        return f'<div class="ai-block">{"".join(lines)}</div>'

    # ── Summary ──────────────────────────────────────────────────────────────

    def summary(self, command_count: int) -> str:
        labels = self.strings["summary"]
        counts = [
            (len(self.records), labels["combos"]),
            (sum(len(r["_steps"]) for r in self.records), labels["steps"]),
            (command_count, labels["commands"]),
        ]
        items = "".join(f'<div class="ai-count"><b>{count:,}</b><span>{e(label)}</span></div>' for count, label in counts)
        weapons = Counter(r["weapon_text"] or "-" for r in self.records)
        chips = "".join(_chip(f"{label} {count:,}") for label, count in weapons.items())
        return (
            '<div class="ai-summary">'
            f'<div class="ai-box"><div class="ai-box-title">{e(labels["list"])}</div><div class="ai-counts">{items}</div></div>'
            f'<div class="ai-box"><div class="ai-box-title">{e(labels["weapons"])}</div><div class="ai-vars">{chips}</div></div>'
            '</div>'
        )
