"""The fixed run of function slots in every `characterfunction.dbss` record.

A record is a 4-byte head, 40 function slots in the order below, then a 7-byte
tail. A slot is two u64-prefixed UTF-16LE strings, the button text (`name`) and
its `condition` script, followed by the slot's own fields. Three slots store
the condition first. With every string empty a record is 732 bytes; the
`unknown_<hex>` names are offsets in that all-empty record.

`loc_index` is `str_id4` of the button text in LOC type 32 (`str_id1` is the
character ID). Slots the client gives no LOC text have `None`.
Full layout in docs/file-formats/dbss/characterfunction_dbss.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

FieldKind = Literal["u8", "u16", "u32", "u8[]", "u32[]"]


@dataclass(frozen=True)
class FieldSpec:
    name: str
    kind: FieldKind


@dataclass(frozen=True)
class SlotSpec:
    key: str
    loc_index: int | None
    fields: tuple[FieldSpec, ...] = ()
    condition_first: bool = False


def _u8(name: str) -> FieldSpec:
    return FieldSpec(name, "u8")


def _u16(name: str) -> FieldSpec:
    return FieldSpec(name, "u16")


def _u32(name: str) -> FieldSpec:
    return FieldSpec(name, "u32")


# On most slots a u8 after the strings is 1 exactly when the slot has button text.
_HAS_BUTTON = _u8("has_button")

# `shop_type` is an `eShopType` value (the `_shopType` table of
# panel_dialog_main_all.luac), `trade_group_type` an `ETradeGroupType`
# (1 Normal, 2 Desert) and `servant_type` an `eServantType` (0 Vehicle,
# 1 Ship; 6 on records without a stable).
# eShopType member names in value order, without the prefix. The file also
# stores 16 (eShopType_Count) on 9 NPCs.
SHOP_TYPE_NAMES: tuple[str, ...] = (
    "None", "Potion", "Weapon", "Jewel", "Furniture", "Collect", "Fish", "Worker",
    "Alchemy", "Cook", "PC", "Grocery", "RandomShop", "DayRandomShop", "ItemMarket",
    "Instrument",
)

HEAD_FIELDS: tuple[FieldSpec, ...] = (
    _u8("shop_type"),
    _u8("trade_group_type"),
    _u8("is_smuggle_shop"),
    _u8("servant_type"),
)

# The `*_group` fields are `itemmaingroup.bss` group IDs, 0 for none: the shop
# window's Buy and Sell tab lists, and the trade item list. `vehicle_types`
# holds `CppEnums.VehicleType` values, `servant_where_type` a
# `CppEnums.ServantWhereType` (9 on records without a stable).
SLOTS: tuple[SlotSpec, ...] = (
    SlotSpec("shop", 0, (_u32("shop_buy_group"),)),
    SlotSpec("shop_sell", None, (_u32("shop_sell_group"),)),
    SlotSpec("guild_shop", 4, (_u32("guild_shop_buy_group"),)),
    SlotSpec("guild_shop_sell", None, (_u32("guild_shop_sell_group"),)),
    SlotSpec("trade", 2, (_u32("trade_group"),)),
    SlotSpec("auction", 6, (_u16("auction_key"),)),
    SlotSpec("mating", None, (_u16("mating_key"),)),
    SlotSpec("inn", None, (_u16("inn_key"),)),
    SlotSpec("reward_explore", None),
    SlotSpec("learn_skill", 10, (_HAS_BUTTON,)),
    SlotSpec("repair", 11, (_HAS_BUTTON,)),
    SlotSpec("traces_of_blood", None, (_HAS_BUTTON,)),
    SlotSpec("storage", 12, (_HAS_BUTTON,)),
    SlotSpec("stable", 13, (_u8("servant_where_type"), FieldSpec("vehicle_types", "u8[]"))),
    SlotSpec("transport", 14, (_HAS_BUTTON,)),
    SlotSpec("transport_person", None, (_HAS_BUTTON,)),
    SlotSpec("conversation", 16, (_HAS_BUTTON, _u8("is_greet"))),
    SlotSpec("create_guild", 17, (_HAS_BUTTON,)),
    SlotSpec(
        "node_management",
        18,
        (FieldSpec("managed_node_keys", "u32[]"), FieldSpec("town_node_keys", "u32[]")),
    ),
    SlotSpec("lord_information", 19, (_HAS_BUTTON,)),
    SlotSpec("minor_lord_menu", None, (_HAS_BUTTON, _u8("unknown_186"))),
    SlotSpec("extraction", 21, (_HAS_BUTTON,)),
    SlotSpec("imperial_delivery", 23, (_u16("territory_key"),)),
    SlotSpec("unknown_1aa", None, (_u16("unknown_1ba"),)),
    SlotSpec("knowledge_management", 24, (_HAS_BUTTON,)),
    SlotSpec("imperial_crafting_delivery", 25, (_HAS_BUTTON, _u8("supply_shop_key"))),
    SlotSpec("imperial_fishing_delivery", 26, (_HAS_BUTTON,)),
    SlotSpec("guild_supply_shop", None, (_HAS_BUTTON,)),
    SlotSpec("skill_addon", 28, (_HAS_BUTTON, _u8("is_stallion_skill_training"))),
    SlotSpec("give_gift", 29, (_HAS_BUTTON,), condition_first=True),
    SlotSpec("cleanse_gear", 30, (_HAS_BUTTON,), condition_first=True),
    SlotSpec("black_spirit_adventure", None, (_HAS_BUTTON,), condition_first=True),
    SlotSpec("central_market", 31, (_u16("territory_key"),)),
    SlotSpec("maritime_trade", None, (_u16("barter_region_key"),)),
    SlotSpec(
        "hire_sailor",
        32,
        (_u8("employee_job"), _HAS_BUTTON, _u8("unknown_27c"), _u16("employee_key")),
    ),
    SlotSpec("season_special_gift", 34, (_u8("unknown_28f"),)),
    SlotSpec("hall_of_honor", 35, (_HAS_BUTTON,)),
    SlotSpec("yar", 36, (_u8("unknown_2b1"),)),
    SlotSpec("pet_training", 38, (_HAS_BUTTON, _u8("unknown_2c3"))),
    SlotSpec("lightstone", 39, (_u8("unknown_2d4"),)),
)

# (slot key, field) of every `itemmaingroup.bss` group ID, in slot order.
ITEM_GROUP_FIELDS: tuple[tuple[str, str], ...] = (
    ("shop", "shop_buy_group"),
    ("shop_sell", "shop_sell_group"),
    ("guild_shop", "guild_shop_buy_group"),
    ("guild_shop_sell", "guild_shop_sell_group"),
    ("trade", "trade_group"),
)

TAIL_FIELDS: tuple[FieldSpec, ...] = (
    _u8("unknown_2d5"),
    _u8("unknown_2d6"),
    _u32("unknown_2d7"),
    _u8("unknown_2db"),
)
