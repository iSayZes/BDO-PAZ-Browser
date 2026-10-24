"""Links between `tutorial.bss` steps and the `tutorial_startevent.bss` rows they start.

A step lists start event keys (`start_event_keys`); each opens its
`tutorial_startevent.bss` row by `key`. A start event row links back to every
step that lists it, by the step's `step` text (`1.4`: tutorial type, then
step index).
"""

from __future__ import annotations

from collections.abc import Iterable

from _common.html import record_link


FOLDER = "gamecommondata/binary"
TUTORIAL_FILE = "tutorial.bss"
START_EVENT_FILE = "tutorial_startevent.bss"
STEP_FIELD = "step"
START_EVENT_KEY_FIELD = "key"
_LINK_CLASS = "record-link"


def step_text(tutorial_type: int, tutorial_index: int) -> str:
    """`1.4`: the tutorial type and the step index, the `step` field of a `tutorial.bss` record."""
    return f"{tutorial_type}.{tutorial_index}"


def start_event_link(key: int) -> str:
    """A button showing the key that opens its `tutorial_startevent.bss` row."""
    return record_link(str(key), f"{FOLDER}/{START_EVENT_FILE}", START_EVENT_KEY_FIELD, key, _LINK_CLASS)


def step_link(step: str) -> str:
    """A button showing the step that opens its `tutorial.bss` row."""
    return record_link(step, f"{FOLDER}/{TUTORIAL_FILE}", STEP_FIELD, step, _LINK_CLASS)


def steps_by_start_event(steps: Iterable[dict]) -> dict[int, list[str]]:
    """Start event key -> the `step` texts of the `tutorial.bss` rows that list it, in step order."""
    found: dict[int, list[str]] = {}
    ordered = sorted(steps, key=lambda row: (row["tutorial_type"], row["tutorial_index"]))
    for row in ordered:
        step = step_text(row["tutorial_type"], row["tutorial_index"])
        for key in row["start_event_keys"]:
            found.setdefault(key, []).append(step)
    return found
