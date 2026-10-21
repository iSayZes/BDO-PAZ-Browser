from __future__ import annotations

import struct
from collections.abc import Iterator

from _common.binary import u8, u16, u32, u64
from _common.icon_index import clean_stored_icon_path
from _common.item_key import split_item_key
from _common.pabr_offset import PabrOffsetRow, parse_pabr_u32_offset_rows
from _common.prefixed_string import locate_prefixed_ascii, read_prefixed_at
from _common.ui_texture import UI_TEXTURE_ICON_ROOT
from _dbss.skill.parser import build_skill_buff_index
from .layout import BlockStrings, header_shift, read_block_strings


# Keys are packed item keys (`_common/item_key.py`). Level 0 is the base item
# and there is exactly one per item ID; an item has one record per level up to
# its maximum.

# The item grade, 0 (white) to 5, which colours the item name (`_common/item_grade.py`).
_GRADE = 0x06
# The equipment type; 0 on items that are not equipment. Weapon types are
# named after their Central Market subcategory (`weapon_types.py`).
_EQUIP_TYPE = 0x07
# The equipment slot, an `__eEquipSlotNo*` value (`slot_labels.py`).
_EQUIP_SLOT = 0x0E
# 1 when copies of the item share one inventory slot.
_STACKABLE = 0x43

# When the item binds: 0 never, 1 when obtained, 2 when equipped. The flag
# after it binds to the family instead of the character.
_VESTED_TYPE = 0x49
_FAMILY_BOUND = 0x4A
# 1 on trade goods; the trade type after it says where they go.
_FOR_TRADE = 0x4B
_TRADE_TYPE = 0x4C
# Bit n allows class type n (`_common/class_type.py`).
_CLASS_MASK = 0x4D
# Bit n allows `CppEnums.ServantKind` n; 0 on everything but servant gear
# (`servant_slots.py`).
_SERVANT_KINDS = 0x55

# The fields below follow `unknown_5d` (`layout.py`): these offsets hold when
# it is empty, and move by `header_shift` on servant gear.

# Character level needed to use the item (i32, 2016 `_minLevel`); 0 or 1 when
# there is none.
_REQUIRED_LEVEL = 0x61
# Highest character level that can use the item (i32, 2016 `_maxLevel`); the
# tooltip shows it when `isMaxLevelRestricted()`. 0x7FFFFFFF when there is none.
_MAX_LEVEL = 0x65
_NO_MAX_LEVEL = 0x7FFF_FFFF
# What using the item does, a `CppEnums.ContentsEventType` (u16,
# `contents_event.py`), then its two i64 parameters.
_CONTENTS_EVENT_TYPE = 0x86
_CONTENTS_EVENT_PARAMS = 0x88
_CONTENTS_EVENT_PARAMS_STRUCT = struct.Struct("<qq")
# 0 when the item can never be dyed. 1 allows it, but only an item whose
# model has dye parts can be dyed, and this file does not hold those.
_DYEABLE = 0xA8

# The character this item places or summons (furniture, fences, pets), keyed
# like characterstatic.dbss and characterobject.dbss; 0 when there is none.
_CHARACTER_ID = 0xAA
# Max durability one Memory Fragment restores (`_repairEnduranceCount` in the
# repair window Lua); 0 on items it cannot repair.
_REPAIR_ENDURANCE_COUNT = 0xAC

# Stored for items without durability.
_NO_DURABILITY = 32_767
_MAX_DURABILITY = 0xC5

# The Central Market category and subcategory, LOC type 44 `str_id1` and
# `str_id2`; 255 when the item is not listed.
_MARKET_CATEGORY = 0xC8
_MARKET_SUB_CATEGORY = 0xC9

# skill_key_1 and skill_key_2: the skills a consumable casts, `skill.dbss`
# keys whose buff_ids are the item's buffs; 0 when unused. Every level of an
# item stores the same keys.
_SKILL_KEYS = 0xCC
_SKILL_KEYS_STRUCT = struct.Struct("<II")

# Relative to the end of the icon text: 1 when the item can be listed on the
# Central Market, and 2 when it can go in the Family Inventory.
_MARKETABLE = 0x00
_FAMILY_INVENTORY = 0x0D
_FAMILY_INVENTORY_ALLOWED = 2
# Three UTF-16 strings follow at +0x12 (a pet script, a box prompt, Exchange
# Info); the enhancement type sits 13 bytes after the last of them. It is the
# enhancement system (1 ordinary weapons and armour, 19 Sovereign) and the
# group key of guaranteeenchantss.dbss; 0 when the item has none.
_MESSAGES = 0x12
_MESSAGE_COUNT = 3
_ENHANCEMENT_TYPE_AFTER_MESSAGES = 0x0D
# The Life Skill gear kind and the Life Skill tab it is for (`life_slots.py`),
# after the three strings; 37 and 15 on items that are not Life Skill gear.
_LIFE_EQUIP_TYPE_AFTER_MESSAGES = 0x29
_LIFE_RESTRICT_TYPE_AFTER_MESSAGES = 0x2A

# The last u16 of a base block: the crystal's jewelgroupstaticstatus.bss group,
# 0xFFFF on everything that is not a crystal. Higher levels always store 0xFFFF.
_CRYSTAL_GROUP_FROM_END = 0x02
_NO_CRYSTAL_GROUP = 0xFFFF


def parse_itemenchantoffset_records(data: bytes) -> list[dict]:
    """Parse the key/offset index into plain dicts."""
    return [_offset_record(row) for row in parse_pabr_u32_offset_rows(data)]


def _offset_record(row: PabrOffsetRow) -> dict:
    item_id, enchant_level = split_item_key(row.entry_id)
    return {
        "key": row.entry_id,
        "item_id": item_id,
        "enchant_level": enchant_level,
        "data_offset": row.offset,
        "data_size": row.size,
    }


def max_enchant_levels(offset_rows: list[dict]) -> dict[int, int]:
    """Map item ID to its highest enchant level; 0 when it cannot be enhanced."""
    levels: dict[int, int] = {}
    for row in offset_rows:
        item_id = row["item_id"]
        levels[item_id] = max(levels.get(item_id, 0), row["enchant_level"])
    return levels


def _base_rows(offset_rows: list[dict]) -> Iterator[dict]:
    """The level-0 (base item) rows, one per item."""
    return (row for row in offset_rows if not row["enchant_level"])


def _block_strings(data: bytes, row: dict) -> BlockStrings:
    """The enchant key, Korean name and icon of an offset row's block."""
    start = row["data_offset"]
    try:
        return read_block_strings(data, start, start + row["data_size"])
    except ValueError as error:
        raise ValueError(f"itemenchant.dbss block for key {row['key']}: {error}") from error


def _icon_path(icon: str) -> str:
    # Stored icon paths are relative to ui_texture/icon/.
    return f"{UI_TEXTURE_ICON_ROOT}{clean_stored_icon_path(icon)}"


def _second_string(data: bytes, icon_end: int, end: int) -> str:
    """The first length-prefixed ASCII string after the icon, or ''."""
    strings = locate_prefixed_ascii(data, icon_end, end)
    return strings[0][1] if strings else ""


def _late_fields_at(data: bytes, start: int) -> int:
    """The base for the header fields after `unknown_5d`: `start`, moved by its count."""
    return start + header_shift(data, start)


def _header_fields(data: bytes, start: int) -> dict:
    """The confirmed header fields of the block at `start`; itemenchant_dbss.md has the evidence.

    The block must lie inside `data`: this runs once per item, so the bytes
    are indexed directly instead of through the bounds-checked `u8`.
    """
    late = _late_fields_at(data, start)
    durability = u16(data, late + _MAX_DURABILITY)
    max_level = u32(data, late + _MAX_LEVEL)
    return {
        "grade": data[start + _GRADE],
        "equip_type": data[start + _EQUIP_TYPE],
        "equip_slot": data[start + _EQUIP_SLOT],
        "stackable": bool(data[start + _STACKABLE]),
        "vested_type": data[start + _VESTED_TYPE],
        "family_bound": bool(data[start + _FAMILY_BOUND]),
        "trade_type": data[start + _TRADE_TYPE] if data[start + _FOR_TRADE] else None,
        "class_mask": u64(data, start + _CLASS_MASK),
        "servant_kinds": u32(data, start + _SERVANT_KINDS),
        "required_level": u32(data, late + _REQUIRED_LEVEL),
        "contents_event_type": u16(data, late + _CONTENTS_EVENT_TYPE),
        **_contents_event_params(data, late),
        "dyeable": bool(data[late + _DYEABLE]),
        "character_id": u16(data, late + _CHARACTER_ID),
        # None sorts last and exports empty.
        "max_level": None if max_level == _NO_MAX_LEVEL else max_level,
        "repair_endurance_count": data[late + _REPAIR_ENDURANCE_COUNT] or None,
        "max_durability": None if durability == _NO_DURABILITY else durability,
        "market_category": data[late + _MARKET_CATEGORY],
        "market_sub_category": data[late + _MARKET_SUB_CATEGORY],
        "skill_keys": list(_skill_keys(data, late)),
    }


def _contents_event_params(data: bytes, late: int) -> dict:
    """`contents_event_param1` and `param2`; `late` is from `_late_fields_at`."""
    param1, param2 = _CONTENTS_EVENT_PARAMS_STRUCT.unpack_from(data, late + _CONTENTS_EVENT_PARAMS)
    return {"contents_event_param1": param1, "contents_event_param2": param2}


def _messages_end(data: bytes, icon_end: int, end: int) -> int:
    """Where the three strings that follow the icon end.

    Raises ValueError when a string runs past the block, since the fields
    after them would then be read from the wrong place.
    """
    pos = icon_end + _MESSAGES
    for _ in range(_MESSAGE_COUNT):
        _, pos = read_prefixed_at(data, pos, end, wide=True)
    return pos


def _enhancement_type(data: bytes, icon_end: int, end: int) -> int:
    """The u32 13 bytes after the three strings that follow the icon."""
    return u32(data, _messages_end(data, icon_end, end) + _ENHANCEMENT_TYPE_AFTER_MESSAGES)


def _after_icon_fields(data: bytes, icon_end: int, end: int) -> dict:
    """The confirmed fields that follow the icon text."""
    messages_end = _messages_end(data, icon_end, end)
    return {
        "marketable": bool(u8(data, icon_end + _MARKETABLE)),
        "family_inventory": u8(data, icon_end + _FAMILY_INVENTORY) == _FAMILY_INVENTORY_ALLOWED,
        "enhancement_type": u32(data, messages_end + _ENHANCEMENT_TYPE_AFTER_MESSAGES),
        "life_equip_type": u8(data, messages_end + _LIFE_EQUIP_TYPE_AFTER_MESSAGES),
        "life_restrict_type": u8(data, messages_end + _LIFE_RESTRICT_TYPE_AFTER_MESSAGES),
    }


def _crystal_group(data: bytes, end: int) -> int | None:
    """The crystal group of the block ending at `end`, or None when it is not a crystal."""
    group = u16(data, end - _CRYSTAL_GROUP_FROM_END)
    return None if group == _NO_CRYSTAL_GROUP else group


def _skill_keys(data: bytes, late: int) -> tuple[int, ...]:
    """The non-zero skill keys of a block, in slot order; `late` is from `_late_fields_at`."""
    return tuple(key for key in _SKILL_KEYS_STRUCT.unpack_from(data, late + _SKILL_KEYS) if key)


def parse_itemenchant_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Parse one row per item from its level-0 block, with its highest level.

    Higher levels mostly repeat the base item's icon (the items of
    `specialenchantitem.bss` store their own per level), and what else differs
    per level is not decoded, so they only contribute `max_enchant_level`. What
    the optional ASCII string after the icon (e.g. `ITEM_BIC_HIT_1`) means is
    unconfirmed.
    """
    offset_rows = parse_itemenchantoffset_records(offset_data)
    max_levels = max_enchant_levels(offset_rows)
    records: list[dict] = []

    for row in _base_rows(offset_rows):
        start = row["data_offset"]
        end = start + row["data_size"]
        if end > len(data):
            raise ValueError(
                f"itemenchant.dbss block for key {row['key']} ends at "
                f"{end:,} but the file is {len(data):,} bytes."
            )

        strings = _block_strings(data, row)
        records.append({
            "item_id": row["item_id"],
            "name_kr": strings.name_kr,
            "max_enchant_level": max_levels[row["item_id"]],
            # None sorts last and exports empty.
            "enchant_key": strings.enchant_key or None,
            "icon_path": _icon_path(strings.icon),
            **_header_fields(data, start),
            **_after_icon_fields(data, strings.icon_end, end),
            # None sorts last and exports empty.
            "crystal_group": _crystal_group(data, end),
            "second_string": _second_string(data, strings.icon_end, end),
            "block_size": row["data_size"],
        })

    return records


def build_item_icon_index(data: bytes, offset_data: bytes) -> dict[int, str]:
    """Map item ID to icon path using only the level-0 (base item) records.

    Higher levels mostly repeat the base item's icon, so skipping them cuts
    the work to a third. The per-level icons of the items that change icon come
    from `specialenchantitem.bss` instead (`IndexKind.ITEM_KEY_ICON`).
    """
    index: dict[int, str] = {}

    for row in _base_rows(parse_itemenchantoffset_records(offset_data)):
        if row["data_offset"] + row["data_size"] > len(data):
            continue
        index[row["item_id"]] = _icon_path(_block_strings(data, row).icon)

    return index


def build_enchant_key_item_index(data: bytes, offset_data: bytes) -> dict[int, tuple[int, ...]]:
    """Map an enchantstaticstatus.dbss enchant key to its base item IDs, ascending.

    Only level-0 records are read: every level of an item stores the key of
    its base block. Items with key 0 have no enhancement data and are left out.
    """
    items_by_key: dict[int, list[int]] = {}

    for row in _base_rows(parse_itemenchantoffset_records(offset_data)):
        if row["data_offset"] + row["data_size"] > len(data):
            continue
        enchant_key = _block_strings(data, row).enchant_key
        if enchant_key:
            items_by_key.setdefault(enchant_key, []).append(row["item_id"])

    return {key: tuple(sorted(items)) for key, items in items_by_key.items()}


def build_enhancement_type_item_index(data: bytes, offset_data: bytes) -> dict[int, tuple[int, ...]]:
    """Map an enhancement type (the guaranteeenchantss.dbss group) to its base item IDs, ascending.

    Only level-0 records are read, like the enchant key index. Items with
    type 0 cannot be enhanced and are left out.
    """
    items_by_type: dict[int, list[int]] = {}

    for row in _base_rows(parse_itemenchantoffset_records(offset_data)):
        end = row["data_offset"] + row["data_size"]
        if end > len(data):
            continue
        enhancement_type = _enhancement_type(data, _block_strings(data, row).icon_end, end)
        if enhancement_type:
            items_by_type.setdefault(enhancement_type, []).append(row["item_id"])

    return {key: tuple(sorted(items)) for key, items in items_by_type.items()}


def build_item_name_kr_index(data: bytes, offset_data: bytes) -> dict[int, str]:
    """Map base item ID to the Korean name its level-0 block stores, when it has one.

    The fallback for items LOC type 0 does not name (`_common/item_key.py`).
    """
    index: dict[int, str] = {}

    for row in _base_rows(parse_itemenchantoffset_records(offset_data)):
        if row["data_offset"] + row["data_size"] > len(data):
            continue
        name = _block_strings(data, row).name_kr.strip()
        if name:
            index[row["item_id"]] = name

    return index


def build_item_grade_index(data: bytes, offset_data: bytes) -> dict[int, int]:
    """Map base item ID to its grade, from the level-0 records.

    Every level of an item shares its name, so the base grade colours them all.
    """
    index: dict[int, int] = {}

    for row in _base_rows(parse_itemenchantoffset_records(offset_data)):
        start = row["data_offset"]
        if start + _GRADE >= len(data):
            continue
        index[row["item_id"]] = u8(data, start + _GRADE)

    return index


def build_character_item_index(data: bytes, offset_data: bytes) -> dict[int, int]:
    """Map character ID to the one base item that places or summons it.

    Only level-0 records are read. A character named by more than one item is
    left out, because it then has no single icon to borrow.
    """
    items_by_character: dict[int, list[int]] = {}

    for row in _base_rows(parse_itemenchantoffset_records(offset_data)):
        start = row["data_offset"]
        if start + row["data_size"] > len(data):
            continue

        character_id = u16(data, _late_fields_at(data, start) + _CHARACTER_ID)
        if character_id:
            items_by_character.setdefault(character_id, []).append(row["item_id"])

    return {
        character_id: items[0]
        for character_id, items in items_by_character.items()
        if len(items) == 1
    }


def build_buff_item_index(
    data: bytes,
    offset_data: bytes,
    skill_data: bytes,
    skill_offset_data: bytes,
) -> dict[int, tuple[int, ...]]:
    """Map a buff ID to every base item whose skills apply it, in ascending ID order.

    The link runs item -> skill keys -> `skill.dbss` buff_ids. Skill keys with
    no `skill.dbss` record (a few items store `0x1`) link nothing.
    """
    skill_buffs = build_skill_buff_index(skill_data, skill_offset_data)
    items_by_buff: dict[int, set[int]] = {}

    for row in _base_rows(parse_itemenchantoffset_records(offset_data)):
        start = row["data_offset"]
        if start + row["data_size"] > len(data):
            continue

        for skill_key in _skill_keys(data, _late_fields_at(data, start)):
            for buff_id in skill_buffs.get(skill_key, ()):
                items_by_buff.setdefault(buff_id, set()).add(row["item_id"])

    return {buff_id: tuple(sorted(items)) for buff_id, items in items_by_buff.items()}
