"""Cell text of the item tables (`item_tables.py`)."""

from __future__ import annotations

from _common.enum_name import enum_name
from _common.loc import loc_text


# `CppEnums.ItemType` and `CppEnums.ItemClassifyType` member names in value
# order, from `global_define_cpp_enum.luac` (client 3482), the second without
# its `eItemClassify_` prefix.
ITEM_TYPE_NAMES: tuple[str, ...] = (
    "Normal",
    "Equip",
    "Skill",
    "Tent",
    "Installation",
    "Jewel",
    "CannonBall",
    "Mapae",
    "Material",
    "Interaction",
    "ContentsEvent",
    "ToVehicle",
)
ITEM_CLASSIFY_NAMES: tuple[str, ...] = (
    "Etc",
    "MainWeapon",
    "SubWeapon",
    "Armor",
    "Accessory",
    "BlackStone",
    "Jewel",
    "Potion",
    "Cook",
    "PearlGoods",
    "Housing",
    "Vehicle",
    "Mine",
    "Wood",
    "Seed",
    "Leather",
    "Fish",
    "DyeAmpule",
)

# LOC type 101 names each item move filter by `item_type << 24 |
# item_classify << 16 | contents_event_type` (itemmovedata_bss.md, Filter Names).
LOC_MOVE_FILTER_NAME = 101
_ITEM_TYPE_SHIFT = 24
_ITEM_CLASSIFY_SHIFT = 16
# LOC type 118 names each auto-use category by its key (autousebuffitemcategoryinfo_bss.md).
LOC_AUTO_USE_CATEGORY_NAME = 118


def _numbered(value: int, names: tuple[str, ...]) -> str:
    """`2 Skill`: a stored enum value and its member name, or the bare value."""
    name = enum_name(names, value)
    return name if name == str(value) else f"{value} {name}"


def item_type_text(item_type: int) -> str:
    return _numbered(item_type, ITEM_TYPE_NAMES)


def item_classify_text(item_classify: int) -> str:
    return _numbered(item_classify, ITEM_CLASSIFY_NAMES)


def move_filter_loc_key(item_type: int, item_classify: int, contents_event_type: int) -> int:
    """The LOC type 101 `str_id1` of an item move filter."""
    return item_type << _ITEM_TYPE_SHIFT | item_classify << _ITEM_CLASSIFY_SHIFT | contents_event_type


def move_filter_name(record: dict) -> str:
    """The LOC name of an `itemmovedata.bss` row, else its inline Korean name."""
    key = move_filter_loc_key(record["item_type"], record["item_classify"], record["contents_event_type"])
    return loc_text(LOC_MOVE_FILTER_NAME, key) or record["exception_filter_name_tag_kr"]


def auto_use_category_name(record: dict) -> str:
    """The LOC name of an `autousebuffitemcategoryinfo.bss` category, else its inline Korean name."""
    return loc_text(LOC_AUTO_USE_CATEGORY_NAME, record["category_key"]) or record["category_name_kr"]
