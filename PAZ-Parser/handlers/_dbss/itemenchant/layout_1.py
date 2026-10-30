"""An itemenchant.dbss Layout 1 block (clients 1754 to 1784), read front to back to its last byte.

Six counted lists sit in the header and move everything after them, so each
fixed part is read at the position the walk reached (itemenchant_dbss.md,
Layout 1). The walk must end exactly at the block's indexed size: that is how
a Layout 1 file is told from a Layout 2 one (`layouts.py`).

`read_block` returns the fields the parser needs with the meaning Layout 2
gives them: the "none" values that differ (equip slot `32`, contents event
`125`) become Layout 2's, and the fields Layout 1 does not store are None or
the value Layout 2 stores on such items.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _common.record_reader import RecordReader
from .contents_event import NO_CONTENTS_EVENT
from .life_slots import NO_LIFE_EQUIP_TYPE
from .slot_labels import NO_SLOT
from .stored_values import (
    durability_value,
    expiration_value,
    family_inventory_value,
    max_level_value,
    trade_type_value,
)


_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
_I32 = struct.Struct("<i")

# The header, from the block start to the first list count.
_HEADER_SIZE = 0xEE
_GRADE = 0x06
_EQUIP_TYPE = 0x07
_EQUIP_SLOT = 0x0E
_STACKABLE = 0x57
_DO_APPLY_DIRECTLY = 0x58
_EXPIRATION_MINUTES = 0x59
_VESTED_TYPE = 0x5D
_FAMILY_BOUND = 0x5E
_FOR_TRADE = 0x60
_TRADE_TYPE = 0x61
_CLASS_MASK = 0x63
_SERVANT_KINDS = 0x6B
_REQUIRED_LEVEL = 0x74
_MAX_LEVEL = 0x78
# Layout 2 stores `NO_SLOT` instead.
_NO_SLOT = 32

# The 16-byte entries of the first two lists.
_LIST_ENTRY_SIZE = 16

# After the first list, up to the second list count: the contents event and
# the placed character.
_EVENT_PART_SIZE = 0x47
_CONTENTS_EVENT_TYPE = 0x0A
_CONTENTS_EVENT_PARAM1 = 0x0C
_CONTENTS_EVENT_PARAM2 = 0x10
_DYEABLE = 0x33
_CHARACTER_ID = 0x38
_REPAIR_ENDURANCE_COUNT = 0x42
# Layout 2 stores `NO_CONTENTS_EVENT` instead.
_NO_CONTENTS_EVENT = 125

# Between the second list and the u64 count of the third, a list of u32.
_GAP_AFTER_SECOND_LIST = 8
_VALUE_SIZE = 4

# After the third list, up to the u32 count of the fourth: durability, the
# Central Market category and one skill key per class type.
_MARKET_PART_SIZE = 0x2E5
_MAX_DURABILITY = 0x31
_MARKET_CATEGORY = 0x38
_MARKET_SUB_CATEGORY = 0x39
_SKILL_KEYS = 0x47
_SKILL_KEYS_STRUCT = struct.Struct("<101I")

# After the fourth list, a u16 and then the u32 count of the fifth (u32
# entries); after that, the u64 count of the sixth (u16 entries).
_GAP_AFTER_FOURTH_LIST = 2
_SIXTH_ENTRY_SIZE = 2

# After the sixth list, up to the Korean name.
_KEY_PART_SIZE = 0x1B
_ENCHANT_KEY = 0x09

# After the eight strings: `marketable`, then the u32 count of a u32 list.
_MARKETABLE_SIZE = 1
_TAIL_SIZE = 25
_FAMILY_INVENTORY = 0x10
# After the Tail, the u32 count of a u16 list, then one u8.
_END_ENTRY_SIZE = 2
_END_SIZE = 1

# Layout 2 stores the Life Skill gear kind and tab, and Layout 1 has no such
# field; client 1784 has no `item_type` 20 (Life Skill gear) items, which on
# Layout 2 are the only ones without these values.
_NO_LIFE_RESTRICT_TYPE = 15


class Layout1Block(NamedTuple):
    # The enchantstaticstatus.dbss key; 0 when the item has no enhancement data.
    enchant_key: int
    name_kr: str
    # As stored, relative to `ui_texture/icon/`.
    icon: str
    second_string: str
    # The parser's header and after-icon fields, with the names and meanings
    # of Layout 2 (`parser._header_fields`, `parser._after_icon_fields`).
    header: dict
    after_icon: dict


def _skip_list(reader: RecordReader, count: struct.Struct, entry_size: int) -> None:
    (entries,) = reader.unpack(count)
    reader.skip(entries * entry_size)


def _header(data: bytes, header: int, event: int, market: int) -> dict:
    """The header fields, from the positions where the walk found each part."""
    equip_slot = data[header + _EQUIP_SLOT]
    event_type = _U16.unpack_from(data, event + _CONTENTS_EVENT_TYPE)[0]
    skill_keys = _SKILL_KEYS_STRUCT.unpack_from(data, market + _SKILL_KEYS)
    return {
        "grade": data[header + _GRADE],
        "equip_type": data[header + _EQUIP_TYPE],
        "equip_slot": NO_SLOT if equip_slot == _NO_SLOT else equip_slot,
        "stackable": bool(data[header + _STACKABLE]),
        "do_apply_directly": bool(data[header + _DO_APPLY_DIRECTLY]),
        "expiration_minutes": expiration_value(_U32.unpack_from(data, header + _EXPIRATION_MINUTES)[0]),
        "vested_type": data[header + _VESTED_TYPE],
        "family_bound": bool(data[header + _FAMILY_BOUND]),
        "trade_type": trade_type_value(data[header + _FOR_TRADE], data[header + _TRADE_TYPE]),
        "class_mask": _U64.unpack_from(data, header + _CLASS_MASK)[0],
        "servant_kinds": _U32.unpack_from(data, header + _SERVANT_KINDS)[0],
        "required_level": _U32.unpack_from(data, header + _REQUIRED_LEVEL)[0],
        "contents_event_type": NO_CONTENTS_EVENT if event_type == _NO_CONTENTS_EVENT else event_type,
        "contents_event_param1": _I32.unpack_from(data, event + _CONTENTS_EVENT_PARAM1)[0],
        "contents_event_param2": _I32.unpack_from(data, event + _CONTENTS_EVENT_PARAM2)[0],
        "dyeable": bool(data[event + _DYEABLE]),
        "character_id": _U16.unpack_from(data, event + _CHARACTER_ID)[0],
        "max_level": max_level_value(_U32.unpack_from(data, header + _MAX_LEVEL)[0]),
        "repair_endurance_count": data[event + _REPAIR_ENDURANCE_COUNT] or None,
        "max_durability": durability_value(_U16.unpack_from(data, market + _MAX_DURABILITY)[0]),
        "market_category": data[market + _MARKET_CATEGORY],
        "market_sub_category": data[market + _MARKET_SUB_CATEGORY],
        # One key per class type, the same key at every class the item allows:
        # each distinct key once, in class order.
        "skill_keys": list(dict.fromkeys(key for key in skill_keys if key)),
    }


def _after_icon(data: bytes, marketable: int, tail: int) -> dict:
    return {
        "marketable": bool(data[marketable]),
        "family_inventory": family_inventory_value(data[tail + _FAMILY_INVENTORY]),
        # Not stored in Layout 1 (itemenchant_dbss.md, Layout 1 Field Matches).
        "enhancement_type": None,
        "life_equip_type": NO_LIFE_EQUIP_TYPE,
        "life_restrict_type": _NO_LIFE_RESTRICT_TYPE,
    }


def read_block(data: bytes, start: int, end: int) -> Layout1Block:
    """Read the block `[start, end)` to its last byte.

    Raises ValueError when a field runs past `end`, or the walk ends before
    it: the block then has another layout.
    """
    reader = RecordReader(data, start, end, f"block at 0x{start:X}")
    reader.skip(_HEADER_SIZE)
    _skip_list(reader, _U64, _LIST_ENTRY_SIZE)
    event = reader.pos
    reader.skip(_EVENT_PART_SIZE)
    _skip_list(reader, _U64, _LIST_ENTRY_SIZE)
    reader.skip(_GAP_AFTER_SECOND_LIST)
    _skip_list(reader, _U64, _VALUE_SIZE)
    market = reader.pos
    reader.skip(_MARKET_PART_SIZE)
    _skip_list(reader, _U32, _VALUE_SIZE)
    reader.skip(_GAP_AFTER_FOURTH_LIST)
    _skip_list(reader, _U32, _VALUE_SIZE)
    _skip_list(reader, _U64, _SIXTH_ENTRY_SIZE)
    key_part = reader.pos
    reader.skip(_KEY_PART_SIZE)

    name_kr = reader.text(wide=True)
    reader.text(wide=True)  # the use condition script
    icon = reader.text(wide=False)
    reader.text(wide=True)  # the Korean description
    reader.text(wide=True)  # Layout 2's first message, such as a pet script
    second_string = reader.text(wide=False)
    reader.text(wide=True)  # Layout 2's second message, the box prompt
    reader.text(wide=True)  # Exchange Info

    marketable = reader.pos
    reader.skip(_MARKETABLE_SIZE)
    _skip_list(reader, _U32, _VALUE_SIZE)
    tail = reader.pos
    reader.skip(_TAIL_SIZE)
    _skip_list(reader, _U32, _END_ENTRY_SIZE)
    reader.skip(_END_SIZE)
    if not reader.at_end():
        raise ValueError(f"block at 0x{start:X}: the walk ends at 0x{reader.pos:X}, before the block end 0x{end:X}")

    return Layout1Block(
        enchant_key=_U32.unpack_from(data, key_part + _ENCHANT_KEY)[0],
        name_kr=name_kr,
        icon=icon,
        second_string=second_string,
        header=_header(data, start, event, market),
        after_icon=_after_icon(data, marketable, tail),
    )
