"""UI string keys that label slots, with their `stringtable.bss` hashes.

The client Lua names a label by sheet and key; LOC type 37 holds its text
under the key's hash. The hash function is unknown but depends on the key
string alone, so each module stores the hashes of its keys, and a test checks
them against `stringtable.bss`.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import NamedTuple

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import KeyHashes, ui_key_text


class UiKeyLabel(NamedTuple):
    key: str
    key_hash: int
    sheet: str = GAME_SHEET


def key_hashes(labels: Iterable[UiKeyLabel]) -> dict[str, dict[str, int]]:
    """sheet -> {key -> key_hash} of `labels`."""
    hashes: dict[str, dict[str, int]] = {}
    for label in labels:
        hashes.setdefault(label.sheet, {})[label.key] = label.key_hash
    return hashes


def label_text(hashes: KeyHashes, label: UiKeyLabel) -> str:
    """The label's LOC text in the app language; '' when LOC lacks it."""
    return ui_key_text(hashes, label.sheet, label.key)
