"""Names of the UI panels and controls the tutorial tables store as hashes.

`tutorial.bss` and `tutorial_startevent.bss` store a panel or control name
as its `ascii_key_hash()`. The step scripts of `tutorial.bss` name most of
them (`uiinputevent(Panel_Window_PetList_All, Button_AllUnSeal, Mouse_LUp)`);
`_EXTRA_NAMES` holds the client UI names that no step script mentions, each
matching a `tutorial_startevent.bss` hash. See
docs/file-formats/bss/tutorial_startevent_bss.md.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from _common.string_hash import ascii_key_hash


_NAME_RE = re.compile(r"\b(?:Panel|Button|Static|Edit|Template)_\w+")
_EXTRA_NAMES = ("Panel_Widget_ServantIcon", "Button_Icon_10", "Static_FeedingBg", "Static_IconBg0")


def ui_names_by_hash(strings: Iterable[str]) -> dict[int, str]:
    """`ascii_key_hash` -> name of every UI name the strings mention, plus `_EXTRA_NAMES`."""
    names = [name for text in strings for name in _NAME_RE.findall(text)]
    return {ascii_key_hash(name): name for name in (*names, *_EXTRA_NAMES)}


def ui_name(names: dict[int, str], name_hash: int) -> str:
    """The name behind `name_hash`, its 8-digit hex when no name fits, or '' for `0` (none)."""
    if not name_hash:
        return ""
    return names.get(name_hash, f"0x{name_hash:08X}")
