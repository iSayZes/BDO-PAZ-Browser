"""Names of the enum fields of `itemexchangesource.bss`, in value order from `0`.

`exchange_type` and `work_ani_type` follow the 2016 `gc::ItemExchangeType::Type`
and `gc::EWorkAniType` enums (the current client Lua has no copy);
`product_category` follows `CppEnums.ProductCategory` in
`global_define_cpp_enum.luac`. Member prefixes are dropped.
"""

from __future__ import annotations

EXCHANGE_TYPE_NAMES: tuple[str, ...] = (
    "Undefined",
    "Recipe",
    "Disassemble",
    "Gamble",
    "Plant",
    "NonRecipeCraft",
    "LargeCraft",
    "Improved",
    "GuildHouseLargeCraft",
    "Garden",
    "GardenManage",
)

PRODUCT_CATEGORY_NAMES: tuple[str, ...] = (
    "Undefined",
    "Disassemble",
    "Farm",
    "Mine",
    "LumberCamp",
    "UseRecipe",
    "DynamicPlant",
    "RegionManager",
    "LargeCraft",
)

WORK_ANI_TYPE_NAMES: tuple[str, ...] = (
    "Mining",
    "Gather",
    "Cultivation",
    "Logging",
    "Making",
    "Architecture",
    "Hide",
    "HouseParty",
    "Breeding",
)

# `eWorkAniType_Count`: the value of every row without a work animation.
NO_WORK_ANI_TYPE = len(WORK_ANI_TYPE_NAMES)
