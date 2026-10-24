"""`CppEnums.InstallationType` names (`global_define_cpp_enum.luac`, client 3482).

The Lua names carry an `eType_` prefix, dropped here. `TypeCount` is 40.
"""

from __future__ import annotations


INSTALLATION_TYPE_NAMES: tuple[str, ...] = (
    "Default", "Carpenter", "Alchemy1", "Founding", "Cooking",
    "Forging", "Treasure", "Smithing", "Weaving", "Bed",
    "Havest", "Mortar", "Anvil", "Stump", "FireBowl",
    "Reserve_15", "Reserve_16", "Buff", "Reserve_18", "Bookcase",
    "WarehouseBox", "Alchemy", "JukeBox", "Pet", "WallPaper",
    "FloorMaterial", "Chandelier", "Curtain", "Scarecrow", "Waterway",
    "Maid", "Curtain_Tied", "LivestockHarvest", "FirePlace", "InstanceWater",
    "Shelf", "Bath", "FurnitureWarehouse", "MansionTree", "EventPersonalTent",
)


def installation_type_name(value: int) -> str:
    """The enum name of `value`, or '' for a value past the client's list."""
    return INSTALLATION_TYPE_NAMES[value] if value < len(INSTALLATION_TYPE_NAMES) else ""
