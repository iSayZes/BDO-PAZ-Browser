"""Both documented block layouts read back from a small built file and its offset file."""

from __future__ import annotations

import struct

import pytest

from bdo_preview import set_handler_client
from .contents_event import CONTENTS_EVENT_CUSTOMIZED_ITEM_BOX, NO_CONTENTS_EVENT
from .parser import (
    build_character_item_index,
    build_customized_item_box_index,
    build_enchant_key_item_index,
    build_item_icon_index,
    build_mesh_key_item_index,
    parse_itemenchant_records,
)
from .slot_labels import NO_SLOT


_ITEM = 10011
_LEVEL_1_KEY = (1 << 24) | _ITEM
_ENCHANT_KEY = 6
_NAME = "바스터 롱소드"
_ICON = "New_Icon/06_PC_EquipItem/00_Common/01_Weapon/00010011.dds"
_SECOND_STRING = "ITEM_BIC_HIT_1"
_SKILL_KEY = 0x1234
_CHARACTER = 2053
_CUSTOMIZED_ITEM = 7
# Three days, as the Inventory 30% DC Coupon stores (itemenchant_dbss.md).
_EXPIRATION_MINUTES = 4_320


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def _str8(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("ascii")


def _layout_1_block(key: int) -> bytes:
    """A Layout 1 block with an entry in most of its lists, so the walk has to skip them."""
    header = bytearray(0xEE)
    struct.pack_into("<I", header, 0x00, key)
    header[0x0E] = 32  # no slot
    struct.pack_into("<BI", header, 0x58, 1, _EXPIRATION_MINUTES)  # do_apply_directly, expiration_minutes
    struct.pack_into("<II", header, 0x74, 0, 0x7FFF_FFFF)  # required_level, max_level
    event = bytearray(0x47)
    struct.pack_into("<HiI", event, 0x0A, CONTENTS_EVENT_CUSTOMIZED_ITEM_BOX, _CUSTOMIZED_ITEM, 0)
    struct.pack_into("<H", event, 0x38, _CHARACTER)
    market = bytearray(0x2E5)
    struct.pack_into("<H", market, 0x31, 32_767)  # no durability
    # The same skill key at two class types (Warrior and Valkyrie).
    struct.pack_into("<I", market, 0x47, _SKILL_KEY)
    struct.pack_into("<I", market, 0x47 + 24 * 4, _SKILL_KEY)
    key_part = bytearray(0x1B)
    struct.pack_into("<I", key_part, 0x09, _ENCHANT_KEY)
    tail = bytearray(25)
    tail[0x10] = 2  # Family Inventory allowed
    return b"".join((
        header, struct.pack("<Q", 1), bytes(16),
        event, struct.pack("<Q", 0),
        bytes(8), struct.pack("<QII", 2, 1, 2),
        market, struct.pack("<II", 1, 0x6016CFF7),
        struct.pack("<HI", 0, 0),
        struct.pack("<QH", 1, 0),
        key_part,
        _str16(_NAME), _str16(""), _str8(_ICON), _str16("설명"), _str16(""),
        _str8(_SECOND_STRING), _str16(""), _str16(""),
        b"\x01", struct.pack("<II", 1, 0), tail, struct.pack("<IH", 1, 0), b"\x00",
    ))


def _layout_2_block(key: int) -> bytes:
    """A Layout 2 block with empty lists and no `unknown_5d` bytes, up to its crystal group."""
    header = bytearray(0xD4)
    struct.pack_into("<I", header, 0x00, key)
    struct.pack_into("<H", header, 0x86, NO_CONTENTS_EVENT)
    return b"".join((
        header, struct.pack("<IIII", 0, 0, 0, 0),
        struct.pack("<I", _ENCHANT_KEY), _str16(_NAME), _str8(_ICON),
        bytes(0x12), _str16(""), _str16(""), _str16(""), bytes(91),
        struct.pack("<IH", key, 0xFFFF),
    ))


def _files(blocks: list[tuple[int, bytes]]) -> tuple[bytes, bytes]:
    """`itemenchant.dbss` holding the (key, block) pairs, and its offset file."""
    data = bytearray(struct.pack("<I", len(blocks)))
    rows = []
    for key, block in blocks:
        rows.append(struct.pack("<III", key, len(data), len(block)))
        data += block
    end_of_rows = 8 + 12 * len(rows)
    offsets = b"PABR" + struct.pack("<I", len(rows)) + b"".join(rows) + struct.pack("<III", 0, end_of_rows, 0)
    return bytes(data), offsets


def _layout_1_files() -> tuple[bytes, bytes]:
    return _files([(_ITEM, _layout_1_block(_ITEM)), (_LEVEL_1_KEY, _layout_1_block(_LEVEL_1_KEY))])


def test_layout_1_items_read_with_the_meanings_of_layout_2() -> None:
    (item,) = parse_itemenchant_records(*_layout_1_files())

    assert (item["item_id"], item["max_enchant_level"], item["enchant_key"]) == (_ITEM, 1, _ENCHANT_KEY)
    assert (item["name_kr"], item["second_string"]) == (_NAME, _SECOND_STRING)
    assert item["icon_path"].endswith("00010011.dds")
    assert (item["equip_slot"], item["contents_event_type"]) == (NO_SLOT, CONTENTS_EVENT_CUSTOMIZED_ITEM_BOX)
    assert item["skill_keys"] == [_SKILL_KEY]
    assert (item["max_level"], item["max_durability"], item["crystal_group"]) == (None, None, None)
    assert item["marketable"] and item["family_inventory"]
    assert (item["do_apply_directly"], item["expiration_minutes"]) == (True, _EXPIRATION_MINUTES)


def test_both_layouts_give_the_same_fields_in_the_same_order() -> None:
    (layout_1,) = parse_itemenchant_records(*_layout_1_files())
    (layout_2,) = parse_itemenchant_records(*_files([(_ITEM, _layout_2_block(_ITEM))]))

    assert list(layout_1) == list(layout_2)
    assert layout_2["contents_event_type"] == NO_CONTENTS_EVENT
    # Stored 0: applies on use, never expires.
    assert (layout_2["do_apply_directly"], layout_2["expiration_minutes"]) == (False, None)


def test_layout_1_files_feed_the_lookup_indexes() -> None:
    data, offsets = _layout_1_files()

    assert build_item_icon_index(data, offsets)[_ITEM].endswith("00010011.dds")
    assert build_enchant_key_item_index(data, offsets) == {_ENCHANT_KEY: (_ITEM,)}
    assert build_character_item_index(data, offsets) == {_CHARACTER: _ITEM}
    assert build_customized_item_box_index(data, offsets) == {_CUSTOMIZED_ITEM: (_ITEM,)}
    # Layout 1 has no class entries.
    assert build_mesh_key_item_index(data, offsets) == {}


def test_a_block_with_a_byte_too_many_names_where_each_layout_broke() -> None:
    data, offsets = _files([(_ITEM, _layout_1_block(_ITEM) + b"\x00")])

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 2: .*; Layout 1: .*before the block end"):
        parse_itemenchant_records(data, offsets)


def test_the_layout_covering_the_client_is_tried_first() -> None:
    set_handler_client(1784)
    data, offsets = _files([(_ITEM, bytes(64))])

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 1: .*; Layout 2: "):
        parse_itemenchant_records(data, offsets)
