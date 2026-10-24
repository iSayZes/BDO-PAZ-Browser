"""The `eventmanagement.bss` view rows: the events, then the event contents, each linked to the other.

An event lists the contents rows it sets (`setted_event`); a contents row
lists the events that set it. Both kinds share the view fields `key`,
`section`, `name`, `details`, the period of the event's condition, the
characters a spawn row names and `linked_keys`, and keep every parser field
for search and export. `row_ref` (`event:3050`, `contents:1001`) tells the
two key ranges apart for links, since an event and a contents row can share
a number.
"""

from __future__ import annotations

import re
from collections.abc import Callable

from .parser import EventManagementTables, setted_contents_keys


EVENT_SECTION = "event"
CONTENTS_SECTION = "contents"
ROW_REF_FIELD = "row_ref"

# Functions whose `param_1` holds character keys joined by `,`.
_CHARACTER_FUNCTIONS = frozenset({"s_spawncharacter", "s_spawnrandomfieldboss", "s_changeselectrate"})
_CHARACTER_SEPARATOR = ","
_PARAM_FIELDS = ("param_1", "param_2", "param_3", "param_4")
# Parameters hold commas of their own (`DayTime-5, 30, 32`).
_PARAM_SEPARATOR = " | "

# `checkPeriod(start, end)` or `checkPeriodbyGMT(n, start, end)`: the last
# two arguments are the period.
_PERIOD_CALL_RE = re.compile(r"checkperiod(?:bygmt)?\(([^)]*)\)", re.IGNORECASE)
_TIME_RE = re.compile(r"^(\d{4})/(\d{1,2})/(\d{1,2})-(\d{1,2}):(\d{2})$")
_PERIOD_ARG_COUNT = 2

# A character key as the text a row shows, `Dastard Bheg (28922)`.
CharacterLabel = Callable[[int], str]


def row_ref(section: str, key: int) -> str:
    """`event:3050` or `contents:1001`: the section and key of one view row."""
    return f"{section}:{key}"


def eventmanagement_records(tables: EventManagementTables, character_label: CharacterLabel) -> list[dict]:
    """The events by `event_no`, then the event contents by `event_contents_no`.

    Raises ValueError on a `setted_event` that is not a list of numbers.
    """
    contents_by_key = {row["event_contents_no"]: row for row in tables.contents}
    characters = {key: _character_keys(row) for key, row in contents_by_key.items()}
    setted = {event["event_no"]: setted_contents_keys(event["setted_event"]) for event in tables.events}

    setters: dict[int, list[int]] = {}
    for event_no in sorted(setted):
        for contents_key in setted[event_no]:
            setters.setdefault(contents_key, []).append(event_no)

    events = [
        _event_record(event, setted[event["event_no"]], characters, character_label)
        for event in sorted(tables.events, key=lambda row: row["event_no"])
    ]
    contents = [
        _contents_record(row, setters.get(row["event_contents_no"], []), characters, character_label)
        for row in sorted(tables.contents, key=lambda row: row["event_contents_no"])
    ]
    return events + contents


def period(condition: str) -> tuple[str | None, str | None]:
    """The start and end of the first period call, as `2026-09-17 09:00`; None without one.

    A time not written as `2026/09/17-09:00` stays as written.
    """
    match = _PERIOD_CALL_RE.search(condition)
    if match is None:
        return None, None
    args = [arg.strip() for arg in match.group(1).split(",")]
    if len(args) < _PERIOD_ARG_COUNT:
        return None, None
    start, end = args[-_PERIOD_ARG_COUNT:]
    return _time_text(start), _time_text(end)


def _time_text(value: str) -> str:
    match = _TIME_RE.match(value)
    if match is None:
        return value
    year, month, day, hour, minute = (int(part) for part in match.groups())
    return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}"


def _character_keys(row: dict) -> list[int]:
    if row["function"] not in _CHARACTER_FUNCTIONS:
        return []
    entries = [entry.strip() for entry in row["param_1"].split(_CHARACTER_SEPARATOR)]
    return [int(entry) for entry in entries if entry.isdigit() and int(entry)]


def _event_record(
    event: dict,
    contents_keys: list[int],
    characters: dict[int, list[int]],
    character_label: CharacterLabel,
) -> dict:
    start, end = period(event["condition"])
    character_keys = list(dict.fromkeys(key for contents_key in contents_keys for key in characters.get(contents_key, [])))
    key = event["event_no"]
    return {
        **event,
        "section": EVENT_SECTION,
        ROW_REF_FIELD: row_ref(EVENT_SECTION, key),
        "key": key,
        "name": event["event_name"],
        "details": event["condition"],
        "period_start": start,
        "period_end": end,
        "character_keys": character_keys,
        "character_names": [character_label(character) for character in character_keys],
        "linked_keys": contents_keys,
    }


def _contents_record(
    row: dict,
    event_keys: list[int],
    characters: dict[int, list[int]],
    character_label: CharacterLabel,
) -> dict:
    key = row["event_contents_no"]
    character_keys = characters[key]
    return {
        **row,
        "section": CONTENTS_SECTION,
        ROW_REF_FIELD: row_ref(CONTENTS_SECTION, key),
        "key": key,
        "name": row["function"],
        "details": _PARAM_SEPARATOR.join(row[field] for field in _PARAM_FIELDS),
        "period_start": None,
        "period_end": None,
        "character_keys": character_keys,
        "character_names": [character_label(character) for character in character_keys],
        "linked_keys": event_keys,
    }
