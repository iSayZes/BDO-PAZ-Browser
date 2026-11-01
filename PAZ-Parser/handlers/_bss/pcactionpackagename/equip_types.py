"""Internal names of the equip types, the cell position in a class block.

`0` to `62` are the `gc::ItemEquipType::Type` enum of the 2016 client's debug
symbols (`BlackDesert64.pdb`), which ends with `TypeCount = 63`. `63` to `89`
are the `PcActionWeapon_Table` columns of a private server's
`DataSheets.bexcel` on client 1784 whose cells match that position in the
client 1784 file (docs/file-formats/bss/pcactionpackagename_bss.md, Equip Types).
Types the sheet has no column for, `93` and up among them, have no name.
"""

from __future__ import annotations

from collections.abc import Mapping

_PDB_NAMES = (
    "None", "LongSword", "ElBlade", "Blade", "Bow", "Dagger", "Staff", "Gun",
    "Shield", "Chest", "Pants", "Glove", "Boots", "Helm", "Shoulder", "Necklace",
    "Ring", "Earing", "Belt", "Lantern", "Rapier", "Buckler", "Avatar_Chest", "Avatar_Pants",
    "Avatar_Glove", "Avatar_Boots", "Avatar_Helm", "Avatar_Shoulder", "EnchantArm", "DoubleAxe", "Avatar_Weapon", "BowOneHanded",
    "Quiver", "Talisman", "Aiguillette", "Avatar_SubWeapon", "ShortBow", "Norigae", "Avatar_Underwear", "FaceDecoration1",
    "FaceDecoration2", "FaceDecoration3", "Installation4", "Rifle", "FishingRod", "Flute", "CollectTool", "Cane",
    "FishingHarpoon", "FishingNet", "Drum", "Body", "Avatar_Body", "HuntRifle", "AlchemyStone", "Shuriken1",
    "Shuriken2", "AwakenWeapon", "Avatar_AwakenWeapon", "Bobber", "Cymbals", "Guitar", "Trumpet",
)

_SHEET_NAMES = {
    63: "Kriegsmesser",
    64: "SiegeRifle",
    65: "Gauntlet",
    67: "Sherry_Main",
    69: "SiegeAxe",
    71: "HandGrenade",
    73: "CrossBow_Main",
    75: "WaterBomb",
    77: "SniperRifle",
    78: "Boomerang",
    80: "Scimitar",
    82: "BroadSword",
    83: "OneHandAxe",
    86: "Mace",
    88: "PPM_Main",
    89: "PFW_Main",
}

EQUIP_TYPE_NAMES: Mapping[int, str] = {**dict(enumerate(_PDB_NAMES)), **_SHEET_NAMES}


def equip_type_name(equip_type: int | None) -> str:
    """The internal name of `equip_type`, or "" when it has none or the record has no equip type."""
    return "" if equip_type is None else EQUIP_TYPE_NAMES.get(equip_type, "")
