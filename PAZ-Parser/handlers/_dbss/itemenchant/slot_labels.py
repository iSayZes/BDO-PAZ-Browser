"""Equipment slot labels, as the item tooltip names the slots.

`include/global_define_cpp_enum.luac` labels each `__eEquipSlotNo*` value in
`CppEnums.SlotNoIdToString` with a `GAME` sheet key. The numbers of
`rightHand` (0) to `Fishing` (40) come from `CppEnums.EquipSlotNo`; that table
ends with `Hunting = 41` and a count of 42, older than the client's slots 41
to 45, which follow from the items that store them and the equipment type
the tooltip names (itemenchant_dbss.md, `equip_slot`). Body, Avatar Body and
Installation 4 are not in the tooltip table, so they use their
`CppEnums.EquipSlotNoString` key. The key's text is LOC type 37 under its
`stringtable.bss` hash. The hash function is unknown but depends on the key
string alone, so the hashes are stored here, and a test checks them against
`stringtable.bss`.
"""

from __future__ import annotations

from typing import NamedTuple

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_key_text


class SlotLabel(NamedTuple):
    enum_name: str
    key: str
    key_hash: int


# The value of items that go in no slot.
NO_SLOT = 46

# equip_slot value -> its `__eEquipSlotNo*` name and label key.
SLOT_LABELS: dict[int, SlotLabel] = {
    0: SlotLabel("RightHand", "PANEL_TOOLTIP_EQUIP_MAINHAND", 3481145065),
    1: SlotLabel("LeftHand", "PANEL_TOOLTIP_EQUIP_SUBHAND", 2640149767),
    2: SlotLabel("SubTool", "LUA_EQUIPMENT_GATHERTOOLS", 2362700627),
    3: SlotLabel("Chest", "PANEL_TOOLTIP_EQUIP_UPPERBODY", 1217446112),
    4: SlotLabel("Glove", "PANEL_TOOLTIP_EQUIP_GLOVES", 2540096254),
    5: SlotLabel("Boots", "PANEL_TOOLTIP_EQUIP_BOOTS", 3667269328),
    6: SlotLabel("Helm", "PANEL_TOOLTIP_EQUIP_HELM", 3176887170),
    7: SlotLabel("Necklace", "PANEL_TOOLTIP_EQUIP_NECKLACE", 2231640483),
    8: SlotLabel("Ring1", "PANEL_TOOLTIP_EQUIP_RING", 737837115),
    9: SlotLabel("Ring2", "PANEL_TOOLTIP_EQUIP_RING", 737837115),
    10: SlotLabel("Earing1", "PANEL_TOOLTIP_EQUIP_EARRING", 1286384132),
    11: SlotLabel("Earing2", "PANEL_TOOLTIP_EQUIP_EARRING", 1286384132),
    12: SlotLabel("Belt", "PANEL_TOOLTIP_EQUIP_WAISTBAND", 492747648),
    13: SlotLabel("Lantern", "PANEL_TOOLTIP_EQUIP_LANTERN", 2307158504),
    14: SlotLabel("AvatarChest", "LUA_EQUIPMENT_AVATAR_BODY", 1487951390),
    15: SlotLabel("AvatarGlove", "LUA_EQUIPMENT_AVATAR_HANDS", 1992007751),
    16: SlotLabel("AvatarBoots", "LUA_EQUIPMENT_AVATAR_BOOTS", 2498387158),
    17: SlotLabel("AvatarHelm", "LUA_EQUIPMENT_AVATAR_HELM", 3987920073),
    18: SlotLabel("AvatarWeapon", "LUA_EQUIPMENT_AVATAR_MAIN", 339052271),
    19: SlotLabel("AvatarSubWeapon", "LUA_EQUIPMENT_AVATAR_SUB", 4202048287),
    20: SlotLabel("AvatarUnderwear", "LUA_EQUIPMENT_AVATAR_UNDERWEAR", 1566105806),
    21: SlotLabel("FaceDecoration1", "LUA_EQUIPMENT_AVATAR_HEAD", 1506474875),
    22: SlotLabel("FaceDecoration2", "LUA_EQUIPMENT_AVATAR_EYES", 150176573),
    23: SlotLabel("FaceDecoration3", "LUA_EQUIPMENT_AVATAR_MOUSE", 1114592465),
    24: SlotLabel("Installation4", "Lua_EquipSlotNo_String_Installation4", 1389637314),
    25: SlotLabel("Body", "Lua_EquipSlotNo_String_body", 3655224765),
    26: SlotLabel("AvatarBody", "Lua_EquipSlotNo_String_avatarBody", 2765519076),
    27: SlotLabel("AlchemyStone", "Lua_EquipSlotNo_String_alchemyStone", 2335748712),
    29: SlotLabel("AwakenWeapon", "Lua_EquipSlotNo_String_awakenWeapon", 386673943),
    30: SlotLabel("AvatarAwakenWeapon", "Lua_EquipSlotNo_String_avatarAwakenWeapon", 3502607328),
    31: SlotLabel("QuestBook", "LUA_EQUIPMENT_QUESTBOOK", 1995191830),
    32: SlotLabel("Artifact1", "LUA_TOOLTIP_EQUIP_RELIC", 496561071),
    33: SlotLabel("Artifact2", "LUA_TOOLTIP_EQUIP_RELIC", 496561071),
    34: SlotLabel("Axe", "LUA_LIFEEQUIP_TOOLTIP_01", 2633093508),
    35: SlotLabel("Syringe", "LUA_LIFEEQUIP_TOOLTIP_02", 1192846262),
    36: SlotLabel("Hoe", "LUA_LIFEEQUIP_TOOLTIP_03", 2533163170),
    37: SlotLabel("ButcheryKnife", "LUA_LIFEEQUIP_TOOLTIP_04", 528051736),
    38: SlotLabel("SkinKnife", "LUA_LIFEEQUIP_TOOLTIP_05", 114951100),
    39: SlotLabel("PickAx", "LUA_LIFEEQUIP_TOOLTIP_06", 2651740551),
    40: SlotLabel("FishingRod", "LUA_LIFEEQUIP_TOOLTIP_07", 2927776078),
    41: SlotLabel("Bobber", "LUA_LIFEEQUIP_TOOLTIP_08", 1280941862),
    42: SlotLabel("FishingHarpoon", "LUA_LIFEEQUIP_TOOLTIP_09", 3629122271),
    43: SlotLabel("HuntRifle", "LUA_LIFEEQUIP_TOOLTIP_10", 896799684),
    44: SlotLabel("SniperRifle", "LUA_LIFEEQUIP_TOOLTIP_11", 1291273725),
    45: SlotLabel("Temp", "LUA_EQUIPMENT_AVATAR_BACK", 2811357827),
}

_KEY_HASHES = {GAME_SHEET: {label.key: label.key_hash for label in SLOT_LABELS.values()}}


def slot_label(equip_slot: int) -> str:
    """The slot's LOC text, else its enum name; '' for no slot, the number for an unknown one."""
    if equip_slot == NO_SLOT:
        return ""
    label = SLOT_LABELS.get(equip_slot)
    if label is None:
        return str(equip_slot)
    return ui_key_text(_KEY_HASHES, GAME_SHEET, label.key) or label.enum_name
