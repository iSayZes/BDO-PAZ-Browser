"""Monster species labels of the drop item window, for `tribe_type` values.

`dropuihuntinggroundinfo.bss` zones and `characterstatic.dbss` characters store
a `__eNewTribeType_*` value. `panel_window_renewdropitem_all_1.luac` labels each
with a `GAME` sheet key, `LUA_DROPITEM_<name>_TOOLTIP_NAME`. The key's text is
LOC type 37 under its `stringtable.bss` hash. The hash function is unknown but
depends on the key string alone, so the hashes are stored here, and a test
checks them against `stringtable.bss`.
"""

from __future__ import annotations

from typing import NamedTuple

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_key_text


class TribeLabel(NamedTuple):
    enum_name: str
    key: str
    key_hash: int


# tribe_type value -> its enum name and label key, in the Lua's order.
TRIBE_LABELS: dict[int, TribeLabel] = {
    0: TribeLabel("Human", "LUA_DROPITEM_HUMAN_TOOLTIP_NAME", 3710921208),
    1: TribeLabel("NonHuman", "LUA_DROPITEM_AIN_TOOLTIP_NAME", 3472837012),
    2: TribeLabel("Others", "LUA_DROPITEM_NORMAL_TOOLTIP_NAME", 1849078063),
    3: TribeLabel("Kamasilvia", "LUA_DROPITEM_KAMASILVIA_TOOLTIP_NAME", 894034231),
    4: TribeLabel("Edania", "LUA_DROPITEM_EDANIA_TOOLTIP_NAME", 207013860),
}

_KEY_HASHES = {GAME_SHEET: {label.key: label.key_hash for label in TRIBE_LABELS.values()}}


def tribe_label(tribe_type: int) -> str:
    """The LOC text of a species label, or '' for an unknown value or without LOC."""
    label = TRIBE_LABELS.get(tribe_type)
    return ui_key_text(_KEY_HASHES, GAME_SHEET, label.key) if label else ""


def tribe_text(tribe_type: int) -> str:
    """`1 Demihumans`: the value, then its label, else its enum name (`1 NonHuman`)."""
    label = TRIBE_LABELS.get(tribe_type)
    name = tribe_label(tribe_type) or (label.enum_name if label else "")
    return f"{tribe_type} {name}" if name else str(tribe_type)
