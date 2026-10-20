"""A character key as a link to its `characterstatic.dbss` row, or plain text when it has none.

Tables keyed by character (`collect.dbss`, `collectresourcename.dbss`) hold
keys with no `characterstatic.dbss` row; a link there would open nothing.
`characterstaticoffset.dbss` lists every key, so handlers load it as an
optional companion and store the answer on each record.
"""

from __future__ import annotations

from _common.html import e, record_link
from _common.lookup_builders import CHARACTERSTATIC
from _common.pabr_offset import parse_pabr_offset_rows

CHARACTERSTATIC_OFFSET_FILE = "characterstaticoffset.dbss"


def characterstatic_offset_companion(internal_path: str) -> str:
    """The `characterstaticoffset.dbss` path next to a file in the same folder."""
    folder = internal_path.rsplit("/", 1)[0]
    return f"{folder}/{CHARACTERSTATIC_OFFSET_FILE}"


def character_row_ids(companions: dict[str, bytes]) -> frozenset[int] | None:
    """Every `characterstatic.dbss` key, or None when the offset companion is missing.

    Raises ValueError, naming the companion, when its rows do not parse.
    """
    offset_raw = companions.get(CHARACTERSTATIC_OFFSET_FILE)
    if offset_raw is None:
        return None
    try:
        rows = parse_pabr_offset_rows(offset_raw)
    except ValueError as ex:
        raise ValueError(f"{CHARACTERSTATIC_OFFSET_FILE}: {ex}") from ex
    return frozenset(row.entry_id for row in rows)


def has_character_row(row_ids: frozenset[int] | None, character_key: int) -> bool:
    """Whether the key has a row; True when the keys are unknown, so the link stays."""
    return row_ids is None or character_key in row_ids


def character_key_cell(character_key: int, has_row: bool) -> str:
    """The key as a link to its `characterstatic.dbss` row, or plain text without one."""
    if not has_row:
        return e(character_key)
    return record_link(str(character_key), CHARACTERSTATIC, "character_id", character_key, "record-link")
