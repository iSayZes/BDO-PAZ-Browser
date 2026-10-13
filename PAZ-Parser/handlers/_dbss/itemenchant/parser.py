from __future__ import annotations

import struct
from collections.abc import Iterator

from _common.binary import u8, u16, u32, u64
from _common.item_key import split_item_key
from _common.pabr_offset import PabrOffsetRow, parse_pabr_u32_offset_rows
from _common.prefixed_string import STRING_PREFIX_SIZE, locate_prefixed_ascii, prefixes_ending_at, read_prefixed_at
from _dbss.skill.parser import build_skill_buff_index


# Keys are packed item keys (`_common/item_key.py`). Level 0 is the base item
# and there is exactly one per item ID; an item has one record per level up to
# its maximum.

# Stored icon paths are relative to this folder.
ICON_ROOT = "ui_texture/icon/"

# The item grade, 0 (white) to 5, which colours the item name (`_common/item_grade.py`).
_GRADE = 0x06

# When the item binds: 0 never, 1 when obtained, 2 when equipped. The flag
# after it binds to the family instead of the character.
_VESTED_TYPE = 0x49
_FAMILY_BOUND = 0x4A
# 1 on trade goods; the trade type after it says where they go.
_FOR_TRADE = 0x4B
_TRADE_TYPE = 0x4C
# Bit n allows class type n (`_common/class_type.py`).
_CLASS_MASK = 0x4D
# Character level needed to use the item; 0 or 1 when there is none.
_REQUIRED_LEVEL = 0x61
# 0 when the item can never be dyed. 1 allows it, but only an item whose
# model has dye parts can be dyed, and this file does not hold those.
_DYEABLE = 0xA8

# The character this item places or summons (furniture, fences, pets), keyed
# like characterstatic.dbss and characterobject.dbss; 0 when there is none.
_CHARACTER_ID = 0xAA

# Stored for items without durability.
_NO_DURABILITY = 32_767
_MAX_DURABILITY = 0xC5

# skill_key_1 and skill_key_2: the skills a consumable casts, `skill.dbss`
# keys whose buff_ids are the item's buffs; 0 when unused. Every level of an
# item stores the same keys.
_SKILL_KEYS = 0xCC
_SKILL_KEYS_STRUCT = struct.Struct("<II")

# The fixed numeric fields end here, so the string scan starts here. The
# lowest string prefix in any block sits at +0xF2 (client 3458).
_FIXED_FIELDS_END = 0xD4

# The enchant key (enchantstaticstatus.dbss) is the u32 just before the Korean
# name's length prefix; 0 when the item has no enhancement data. Every level of
# an item stores the same key (client 3464).
_ENCHANT_KEY_SIZE = 4

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


def _block_strings(data: bytes, start: int, end: int) -> list[tuple[int, str]]:
    """The length-prefixed ASCII strings of the block `[start, end)`, each with its prefix position."""
    return locate_prefixed_ascii(data, start + _FIXED_FIELDS_END, end)


def _name_prefix(data: bytes, start: int, icon_prefix: int) -> int | None:
    """Where the Korean name's length prefix starts: the UTF-16 string whose
    text ends at the icon's prefix.

    The nearest prefix that fits is the name; one further back would hold
    the name's own bytes as text.
    """
    return next(prefixes_ending_at(data, start + _FIXED_FIELDS_END, icon_prefix, wide=True), None)


def _name_kr(data: bytes, name_prefix: int | None, icon_prefix: int) -> str:
    if name_prefix is None:
        return ""
    return data[name_prefix + STRING_PREFIX_SIZE:icon_prefix].decode("utf-16-le", errors="replace")


def _enchant_key(data: bytes, name_prefix: int | None) -> int | None:
    """The enchantstaticstatus.dbss key before the Korean name; None when 0 or not found."""
    if name_prefix is None:
        return None
    return u32(data, name_prefix - _ENCHANT_KEY_SIZE) or None


def _header_fields(data: bytes, start: int) -> dict:
    """The confirmed fixed fields of the block at `start`; itemenchant_dbss.md has the evidence."""
    durability = u16(data, start + _MAX_DURABILITY)
    for_trade = bool(u8(data, start + _FOR_TRADE))
    return {
        "required_level": u8(data, start + _REQUIRED_LEVEL),
        "class_mask": u64(data, start + _CLASS_MASK),
        "vested_type": u8(data, start + _VESTED_TYPE),
        "family_bound": bool(u8(data, start + _FAMILY_BOUND)),
        # None sorts last and exports empty.
        "max_durability": None if durability == _NO_DURABILITY else durability,
        "trade_type": u8(data, start + _TRADE_TYPE) if for_trade else None,
        "dyeable": bool(u8(data, start + _DYEABLE)),
    }


def _icon_end(strings: list[tuple[int, str]]) -> int | None:
    """Where the icon text (the block's first string) ends; None without an icon."""
    if not strings:
        return None
    icon_prefix, icon = strings[0]
    return icon_prefix + STRING_PREFIX_SIZE + len(icon)


def _enhancement_type(data: bytes, icon_end: int, end: int) -> int:
    """The u32 13 bytes after the three strings that follow the icon.

    Raises ValueError when a string runs past the block, since the field
    would then be read from the wrong place.
    """
    pos = icon_end + _MESSAGES
    for _ in range(_MESSAGE_COUNT):
        _, pos = read_prefixed_at(data, pos, end, wide=True)
    return u32(data, pos + _ENHANCEMENT_TYPE_AFTER_MESSAGES)


def _after_icon_fields(data: bytes, icon_end: int | None, end: int) -> dict:
    """The confirmed fields that follow the icon text; False and 0 without an icon."""
    if icon_end is None:
        return {"marketable": False, "family_inventory": False, "enhancement_type": 0}
    return {
        "marketable": bool(u8(data, icon_end + _MARKETABLE)),
        "family_inventory": u8(data, icon_end + _FAMILY_INVENTORY) == _FAMILY_INVENTORY_ALLOWED,
        "enhancement_type": _enhancement_type(data, icon_end, end),
    }


def _skill_keys(data: bytes, start: int) -> tuple[int, ...]:
    """The non-zero skill keys of the block at `start`, in slot order."""
    return tuple(key for key in _SKILL_KEYS_STRUCT.unpack_from(data, start + _SKILL_KEYS) if key)


def parse_itemenchant_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Parse one row per item from its level-0 block, with its highest level.

    Higher levels mostly repeat the base item's icon (the items of
    `specialenchantitem.bss` store their own per level), and what else differs
    per level is not decoded, so they only contribute `max_enchant_level`. The first
    string in a block is always the icon path; what the optional second string
    (e.g. `ITEM_BIC_HIT_1`) means is unconfirmed.
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

        strings = _block_strings(data, start, end)
        icon_prefix, icon = strings[0] if strings else (None, "")
        icon_end = _icon_end(strings)
        name_prefix = None if icon_prefix is None else _name_prefix(data, start, icon_prefix)
        records.append({
            "item_id": row["item_id"],
            "name_kr": "" if icon_prefix is None else _name_kr(data, name_prefix, icon_prefix),
            "max_enchant_level": max_levels[row["item_id"]],
            "enchant_key": _enchant_key(data, name_prefix),
            "icon_path": f"{ICON_ROOT}{icon.lower()}" if icon else "",
            "grade": u8(data, start + _GRADE),
            "character_id": u16(data, start + _CHARACTER_ID),
            **_header_fields(data, start),
            **_after_icon_fields(data, icon_end, end),
            "skill_keys": list(_skill_keys(data, start)),
            "second_string": strings[1][1] if len(strings) > 1 else "",
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
        start = row["data_offset"]
        end = start + row["data_size"]
        if end > len(data):
            continue

        strings = _block_strings(data, start, end)
        if strings:
            index[row["item_id"]] = f"{ICON_ROOT}{strings[0][1].lower()}"

    return index


def build_enchant_key_item_index(data: bytes, offset_data: bytes) -> dict[int, tuple[int, ...]]:
    """Map an enchantstaticstatus.dbss enchant key to its base item IDs, ascending.

    Only level-0 records are read: every level of an item stores the key of
    its base block. Items with key 0 have no enhancement data and are left out.
    """
    items_by_key: dict[int, list[int]] = {}

    for row in _base_rows(parse_itemenchantoffset_records(offset_data)):
        start = row["data_offset"]
        end = start + row["data_size"]
        if end > len(data):
            continue
        strings = _block_strings(data, start, end)
        if not strings:
            continue
        enchant_key = _enchant_key(data, _name_prefix(data, start, strings[0][0]))
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
        start = row["data_offset"]
        end = start + row["data_size"]
        if end > len(data):
            continue
        icon_end = _icon_end(_block_strings(data, start, end))
        if icon_end is None:
            continue
        enhancement_type = _enhancement_type(data, icon_end, end)
        if enhancement_type:
            items_by_type.setdefault(enhancement_type, []).append(row["item_id"])

    return {key: tuple(sorted(items)) for key, items in items_by_type.items()}


def build_item_name_kr_index(data: bytes, offset_data: bytes) -> dict[int, str]:
    """Map base item ID to the Korean name its level-0 block stores, when it has one.

    The fallback for items LOC type 0 does not name (`_common/item_key.py`).
    """
    index: dict[int, str] = {}

    for row in _base_rows(parse_itemenchantoffset_records(offset_data)):
        start = row["data_offset"]
        end = start + row["data_size"]
        if end > len(data):
            continue

        strings = _block_strings(data, start, end)
        if not strings:
            continue
        icon_prefix = strings[0][0]
        name = _name_kr(data, _name_prefix(data, start, icon_prefix), icon_prefix).strip()
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
    left out, because the value is then not a link: character 1 is named by 120
    unrelated items, and the few others with two or more have no single icon.
    """
    items_by_character: dict[int, list[int]] = {}

    for row in _base_rows(parse_itemenchantoffset_records(offset_data)):
        start = row["data_offset"]
        if start + _CHARACTER_ID + 2 > len(data):
            continue

        character_id = u16(data, start + _CHARACTER_ID)
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
        if start + _SKILL_KEYS + _SKILL_KEYS_STRUCT.size > len(data):
            continue

        for skill_key in _skill_keys(data, start):
            for buff_id in skill_buffs.get(skill_key, ()):
                items_by_buff.setdefault(buff_id, set()).add(row["item_id"])

    return {buff_id: tuple(sorted(items)) for buff_id, items in items_by_buff.items()}
