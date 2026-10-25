"""Drop item window hunting grounds by key.

`dropuihuntinggroundinfo.bss` holds one row per hunting ground, and
`worldmapmonster.dbss` points at its keys from the hunting zone markers. LOC
type 116 names a hunting ground by key; the `HUNTING_GROUND_NAME_KR` lookup
index holds the Korean name for the keys LOC leaves out. The
`CHARACTER_HUNTING_GROUNDS` index lists the hunting grounds whose monster list
holds a character, so tables keyed by monster need no companion for it. See
docs/file-formats/bss/dropuihuntinggroundinfo_bss.md.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence

from _common.html import hidden_slice, html_list_cell, record_link
from _common.loc import loc_text
from _common.lookup_index import IndexKind, lookup

DROPUIHUNTINGGROUNDINFO_PATH = "gamecommondata/binary/dropuihuntinggroundinfo.bss"
LOC_HUNTING_GROUND_NAME = 116


def hunting_ground_name(key: int) -> str:
    """LOC type 116 name of a hunting ground, else its Korean name, else ''."""
    name_kr = lookup(IndexKind.HUNTING_GROUND_NAME_KR, key)
    return loc_text(LOC_HUNTING_GROUND_NAME, key) or (name_kr if isinstance(name_kr, str) else "")


def hunting_ground_text(key: int) -> str:
    """`hunting_ground_name()`, or the bare key when the hunting ground has no name."""
    return hunting_ground_name(key) or str(key)


def character_hunting_grounds(character_keys: Iterable[int]) -> tuple[int, ...]:
    """Keys of every hunting ground that lists at least one of the characters, ascending.

    Empty when the `CHARACTER_HUNTING_GROUNDS` index is not loaded.
    """
    keys: set[int] = set()
    for character_key in character_keys:
        grounds = lookup(IndexKind.CHARACTER_HUNTING_GROUNDS, character_key)
        if isinstance(grounds, tuple):
            keys.update(grounds)
    return tuple(sorted(keys))


def hunting_ground_link(key: int, text: str) -> str:
    """`text` as a link to the hunting ground's `dropuihuntinggroundinfo.bss` row."""
    return record_link(text, DROPUIHUNTINGGROUNDINFO_PATH, "key", key, "record-link")


def hunting_ground_list_cell(keys: Sequence[int], names: Sequence[str], max_items: int) -> str:
    """The first `max_items` hunting grounds as row links and a hoverable count of the rest, or ''.

    `names` holds the text of each key in the same order, as the record stores it.
    """
    return html_list_cell(
        [hunting_ground_link(key, name) for key, name in zip(keys[:max_items], names[:max_items])],
        len(keys) - max_items,
        hidden_slice(names, max_items),
    )
