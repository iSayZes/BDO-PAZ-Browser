"""Slot labels of Life Skill gear (`item_type` 20, `__eItemType_LifeEquip`).

Life Skill gear stores `equip_slot` 46: the equipment window finds its slot
in the Life Skill tab from `life_equip_type` and `life_restrict_type`
(`ToClient_getEquipableSlotLifeEquipItem`, `panel_window_equipment_all_3.luac`).
That window's empty-slot tooltip labels the slots with
`CppEnums.LifeEquipSlotString` (`global_define_cpp_enum.luac`), and the
clothes slots with `PANEL_TOOLTIP_EQUIP_UPPERBODY`. The Lua never gives the
type values, so `LIFE_SLOT_LABELS` keys them by the items that store them
(itemenchant_dbss.md, After the icon).
"""

from __future__ import annotations

from .ui_key_labels import UiKeyLabel, key_hashes, label_text

# `life_equip_type` of every item that is not Life Skill gear.
NO_LIFE_EQUIP_TYPE = 37

_ARMOR = UiKeyLabel("PANEL_TOOLTIP_EQUIP_UPPERBODY", 1217446112)
_TOOL = UiKeyLabel("LUA_EQUIPMENT_GATHERTOOLS", 2362700627)
_KNOT = UiKeyLabel("LUA_LIFEEQUIPMENT_TOOLTIP_KNOT", 1972743129)

# life_equip_type -> label key. Clothes of Gathering (7), Fishing (8),
# Hunting (10), Cooking (12), Alchemy (14), Processing (16), Training (18),
# Trading (20), Sailing (21) and Farming (24) go in a clothes slot; Fishing
# Chair (9), Hunting Bag (11), Ladle (13), Flask (15), Processing Stone (17),
# Riding Crop (19) and Sailing Log (22) in a tool slot; one knot each for
# Hunting, Farming, Processing, Cooking, Alchemy and Training (30 to 35).
LIFE_SLOT_LABELS: dict[int, UiKeyLabel] = {
    0: UiKeyLabel("LUA_LIFEEQUIP_TOOLTIP_01", 2633093508),
    1: UiKeyLabel("LUA_LIFEEQUIP_TOOLTIP_02", 1192846262),
    2: UiKeyLabel("LUA_LIFEEQUIP_TOOLTIP_03", 2533163170),
    3: UiKeyLabel("LUA_LIFEEQUIP_TOOLTIP_04", 528051736),
    4: UiKeyLabel("LUA_LIFEEQUIP_TOOLTIP_05", 114951100),
    5: UiKeyLabel("LUA_LIFEEQUIP_TOOLTIP_06", 2651740551),
    6: UiKeyLabel("LUA_TOOLTIP_EQUIP_RELIC", 496561071),
    7: _ARMOR,
    8: _ARMOR,
    9: _TOOL,
    10: _ARMOR,
    11: _TOOL,
    12: _ARMOR,
    13: _TOOL,
    14: _ARMOR,
    15: _TOOL,
    16: _ARMOR,
    17: _TOOL,
    18: _ARMOR,
    19: _TOOL,
    20: _ARMOR,
    21: _ARMOR,
    22: _TOOL,
    24: _ARMOR,
    25: UiKeyLabel("PANEL_TOOLTIP_EQUIP_NECKLACE", 2231640483),
    26: UiKeyLabel("PANEL_TOOLTIP_EQUIP_WAISTBAND", 492747648),
    27: UiKeyLabel("PANEL_TOOLTIP_EQUIP_RING", 737837115),
    28: UiKeyLabel("PANEL_TOOLTIP_EQUIP_EARRING", 1286384132),
    29: UiKeyLabel("Lua_EquipSlotNo_String_alchemyStone", 2335748712),
    30: _KNOT,
    31: _KNOT,
    32: _KNOT,
    33: _KNOT,
    34: _KNOT,
    35: _KNOT,
    36: UiKeyLabel("LUA_LIFEEQUIPMENT_TOOLTIP_MARBLE", 3134062465),
}

_KEY_HASHES = key_hashes(LIFE_SLOT_LABELS.values())


def life_slot_label(life_equip_type: int) -> str:
    """The Life Skill tab's label for the gear's slot; '' for a type without one."""
    label = LIFE_SLOT_LABELS.get(life_equip_type)
    return "" if label is None else label_text(_KEY_HASHES, label)
