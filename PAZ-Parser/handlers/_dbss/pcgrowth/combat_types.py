"""Combat type and combat resource labels of `pcgrowth.dbss`.

`global_newclass_data.luac` gives each class an `_attackType` of
`__eAttackTypeDirect`, `__eAttackTypeRange` or `__eAttackTypeMagical`, and
`panel_characterinfo_basic_all_1.luac` labels them with `GAME` sheet keys.
The same panel names each `CppEnums.CombatResourceType` (MP, FP, EP, BP) with
a `GAME` sheet key too. A key's text is LOC type 37 under its
`stringtable.bss` hash. The hash function is unknown but depends on the key
string alone, so the hashes are stored here, and a test checks them against
`stringtable.bss`.
"""

from __future__ import annotations

from typing import NamedTuple

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_key_text


class EnumLabel(NamedTuple):
    enum_name: str
    key: str
    key_hash: int


# combat_type value -> its `__eAttackType` name and the label key the character info panel shows.
COMBAT_TYPE_LABELS: dict[int, EnumLabel] = {
    0: EnumLabel("Direct", "LUA_WARRIOR_AWAKEN_COMBAT_TYPE", 2394625067),
    1: EnumLabel("Range", "LUA_RANGER_SUCCESSION_COMBAT_TYPE", 3755871217),
    2: EnumLabel("Magical", "LUA_ATKTYPE_MAGIC", 2290260056),
}

# combat_resource_type value -> its `CppEnums.CombatResourceType` name and the
# label key of the character info panel (English MP, WP, MP, SP).
RESOURCE_TYPE_LABELS: dict[int, EnumLabel] = {
    0: EnumLabel("MP", "LUA_CHARACTERINFO_TEXT_MP", 3542800959),
    1: EnumLabel("FP", "LUA_CHARACTERINFO_TEXT_FP_NEW", 4225389044),
    2: EnumLabel("EP", "LUA_CHARACTERINFO_TEXT_EP", 3157683541),
    3: EnumLabel("BP", "LUA_SELFCHARACTERINFO_BP", 3267555402),
}

_KEY_HASHES = {
    GAME_SHEET: {
        label.key: label.key_hash
        for label in (*COMBAT_TYPE_LABELS.values(), *RESOURCE_TYPE_LABELS.values())
    }
}


def _label(labels: dict[int, EnumLabel], value: int) -> str:
    label = labels.get(value)
    return ui_key_text(_KEY_HASHES, GAME_SHEET, label.key) if label else ""


def _text(labels: dict[int, EnumLabel], label_text: str, value: int) -> str:
    label = labels.get(value)
    return label_text or (label.enum_name if label else str(value))


def combat_type_label(combat_type: int) -> str:
    """The LOC text of a combat type, or '' for an unknown value or without LOC."""
    return _label(COMBAT_TYPE_LABELS, combat_type)


def combat_type_text(combat_type: int) -> str:
    """`Ranged`: the LOC label, else the enum name (`Range`), else the bare value."""
    return _text(COMBAT_TYPE_LABELS, combat_type_label(combat_type), combat_type)


def resource_type_label(resource_type: int) -> str:
    """The LOC text of a combat resource type, or '' for an unknown value or without LOC."""
    return _label(RESOURCE_TYPE_LABELS, resource_type)


def resource_type_text(resource_type: int) -> str:
    """`WP`: the LOC label, else the enum name (`FP`), else the bare value."""
    return _text(RESOURCE_TYPE_LABELS, resource_type_label(resource_type), resource_type)
