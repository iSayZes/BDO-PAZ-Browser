"""Weapon type names for `equip_type`, from the Central Market menu.

The client Lua names no equipment type on its own: `PaGlobalFunc_Util_ClassEquipParts`
only groups the types by slot. Each main and sub-weapon type has its own
Central Market subcategory, though, and LOC type 44 names it under
`market_category` / `market_sub_category` (`(1, 1)` Longsword, `(5, 7)` Kunai).
Most items are not listed, so the subcategory is taken from the listed items
of a type and applied to all of its items. A weapon type that a patch adds
gets its name once one of its items is listed (itemenchant_dbss.md,
`equip_type`).
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable

from _common.loc import loc_lookup, strip_pa_tags

LOC_MARKET_CATEGORY = 44
MAIN_WEAPON_CATEGORY = 1
SUB_WEAPON_CATEGORY = 5
_WEAPON_CATEGORIES = frozenset({MAIN_WEAPON_CATEGORY, SUB_WEAPON_CATEGORY})
# The market fields of an item that is not listed.
NOT_LISTED = 255


def weapon_market_menus(records: Iterable[dict]) -> dict[int, tuple[int, int]]:
    """`equip_type` -> (category, subcategory) for each type whose listed items
    all share one main or sub-weapon subcategory."""
    menus: defaultdict[int, set[tuple[int, int]]] = defaultdict(set)
    for record in records:
        if record["equip_type"] and record["market_category"] != NOT_LISTED:
            menus[record["equip_type"]].add((record["market_category"], record["market_sub_category"]))
    weapon_menus: dict[int, tuple[int, int]] = {}
    for equip_type, type_menus in menus.items():
        if len(type_menus) != 1:
            continue
        (menu,) = type_menus
        if menu[0] in _WEAPON_CATEGORIES:
            weapon_menus[equip_type] = menu
    return weapon_menus


def weapon_type_names(records: Iterable[dict]) -> dict[int, str]:
    """`equip_type` -> its LOC type 44 subcategory name, for the weapon types
    `weapon_market_menus` finds; a type whose name LOC lacks is left out."""
    names = {
        equip_type: strip_pa_tags(loc_lookup(LOC_MARKET_CATEGORY, category, sub_category)).strip()
        for equip_type, (category, sub_category) in weapon_market_menus(records).items()
    }
    return {equip_type: name for equip_type, name in names.items() if name}
