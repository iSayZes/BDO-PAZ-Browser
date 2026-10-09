"""Combat type labels of `pcgrowth.dbss`.

`global_newclass_data.luac` gives each class an `_attackType` of
`__eAttackTypeDirect`, `__eAttackTypeRange` or `__eAttackTypeMagical`, and
`panel_characterinfo_basic_all_1.luac` labels them with `GAME` sheet keys.
The key's text is LOC type 37 under its `stringtable.bss` hash. The hash
function is unknown but depends on the key string alone, so the hashes are
stored here, and a test checks them against `stringtable.bss`.
"""

from __future__ import annotations

from typing import NamedTuple

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_key_text


class CombatTypeLabel(NamedTuple):
    enum_name: str
    key: str
    key_hash: int


# combat_type value -> its `__eAttackType` name and the label key the character info panel shows.
COMBAT_TYPE_LABELS: dict[int, CombatTypeLabel] = {
    0: CombatTypeLabel("Direct", "LUA_WARRIOR_AWAKEN_COMBAT_TYPE", 2394625067),
    1: CombatTypeLabel("Range", "LUA_RANGER_SUCCESSION_COMBAT_TYPE", 3755871217),
    2: CombatTypeLabel("Magical", "LUA_ATKTYPE_MAGIC", 2290260056),
}

_KEY_HASHES = {GAME_SHEET: {label.key: label.key_hash for label in COMBAT_TYPE_LABELS.values()}}


def combat_type_label(combat_type: int) -> str:
    """The LOC text of a combat type, or '' for an unknown value or without LOC."""
    label = COMBAT_TYPE_LABELS.get(combat_type)
    return ui_key_text(_KEY_HASHES, GAME_SHEET, label.key) if label else ""


def combat_type_text(combat_type: int) -> str:
    """`Ranged`: the LOC label, else the enum name (`Range`), else the bare value."""
    label = COMBAT_TYPE_LABELS.get(combat_type)
    return combat_type_label(combat_type) or (label.enum_name if label else str(combat_type))
