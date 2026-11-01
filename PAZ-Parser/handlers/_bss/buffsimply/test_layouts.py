"""Both documented Buff Row layouts read back from a small built file."""

from __future__ import annotations

import struct

import pytest

from bdo_preview import set_handler_client
from .parser import parse_buffsimply_records

_BUFF_ID = 2078
_NEED_EQUIP_TYPE = 13
_NEED_EQUIP_SLOT = 6
_STRINGS = ("0", "", "Hide", "New_UI_Common_forLua/Skill/04_PC_Skill/04_Debuff.dds")
_EFFECT_NAME_REF = 2
_ICON_REF = 3
# The empty string, as in every row of clients 1784 and 3482.
_UNKNOWN_12_REF = 1

# Field offsets of each layout as buffsimply_bss.md writes them.
_OFFSETS = {
    2: {
        "row_size": 32, "id_format": "<I", "need_equip_type": 0x04, "need_equip_slot": 0x0B,
        "effect_name_ref": 0x0D, "is_debuff": 0x11, "unknown_12_ref": 0x12, "remove_on_dead": 0x16, "is_shown": 0x17,
        "unknown_18": 0x18, "icon_ref": 0x1C,
    },
    1: {
        "row_size": 30, "id_format": "<H", "need_equip_type": 0x02, "need_equip_slot": 0x09,
        "effect_name_ref": 0x0B, "is_debuff": 0x0F, "unknown_12_ref": 0x10, "remove_on_dead": 0x14, "is_shown": 0x15,
        "unknown_18": 0x16, "icon_ref": 0x1A,
    },
}


def _row(layout: int) -> bytes:
    offsets = _OFFSETS[layout]
    row = bytearray(offsets["row_size"])
    struct.pack_into(offsets["id_format"], row, 0, _BUFF_ID)
    row[offsets["need_equip_type"]] = _NEED_EQUIP_TYPE
    row[offsets["need_equip_slot"]] = _NEED_EQUIP_SLOT
    row[offsets["is_debuff"]] = 1
    row[offsets["remove_on_dead"]] = 1
    row[offsets["is_shown"]] = 1
    struct.pack_into("<I", row, offsets["unknown_18"], 2)
    struct.pack_into("<I", row, offsets["effect_name_ref"], _EFFECT_NAME_REF)
    struct.pack_into("<I", row, offsets["icon_ref"], _ICON_REF)
    struct.pack_into("<I", row, offsets["unknown_12_ref"], _UNKNOWN_12_REF)
    return bytes(row)


def _file(row: bytes) -> bytes:
    """`buffsimply.bss` holding one row and the string table it points into."""
    head = b"PABR" + struct.pack("<I", 1) + row
    table = struct.pack("<I", len(_STRINGS)) + b"".join(
        struct.pack("<BI", 1, len(text.encode("utf-16-le"))) + text.encode("utf-16-le") for text in _STRINGS
    )
    return head + table + struct.pack("<II", len(head), 0)


@pytest.mark.parametrize("layout", sorted(_OFFSETS))
def test_each_layout_reads_the_same_row(layout: int) -> None:
    (record,) = parse_buffsimply_records(_file(_row(layout)))

    assert (record["buff_id"], record["need_equip_type"], record["need_equip_slot"]) == (
        _BUFF_ID, _NEED_EQUIP_TYPE, _NEED_EQUIP_SLOT,
    )
    assert (record["is_debuff"], record["remove_on_dead"], record["is_shown"], record["unknown_18"]) == (
        True, True, True, 2,
    )
    assert (record["effect_name"], record["unknown_12"]) == ("Hide", "")
    assert record["icon_path"].endswith("04_debuff.dds")


def test_a_row_of_another_size_names_where_each_layout_broke() -> None:
    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 2: .*; Layout 1: "):
        parse_buffsimply_records(_file(bytes(31)))


def test_the_layout_covering_the_client_is_tried_first() -> None:
    set_handler_client(1784)

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 1: .*; Layout 2: "):
        parse_buffsimply_records(_file(bytes(31)))
