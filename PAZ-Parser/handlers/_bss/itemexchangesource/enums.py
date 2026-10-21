"""Names of the enum fields of `itemexchangesource.bss`, in value order from `0`.

`exchange_type` follows the 2016 `gc::ItemExchangeType::Type` enum (the
current client Lua has no copy); `product_category` follows
`CppEnums.ProductCategory` in `global_define_cpp_enum.luac`. Member prefixes
are dropped. `work_ani_type` names are in `_common/work_ani_type.py`.
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
