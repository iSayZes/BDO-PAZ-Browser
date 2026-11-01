"""Both documented Row layouts read back from a small built file."""

from __future__ import annotations

import struct

import pytest

from bdo_preview import set_handler_client
from .parser import parse_charactersimply_records

_CHARACTER = 40015
_LEVEL = 33
_MAX_HP = 2500.0
_VEHICLE = 18  # Boat
_INVENTORY_MAX = 8
_CARRIAGE_TYPE = 3
_STRINGS = ("npc/boat", "", "배", "", "getknowledge(304);", "")
# String-table index of each string field, as stored in the row.
_STRING_FIELDS = {
    "model_path_ref": 0, "voice_bank_ref": 1, "name_kr_ref": 2,
    "title_kr_ref": 3, "action_script_ref": 4, "condition_script_ref": 5,
}

# Field offsets of each layout as charactersimply_bss.md writes them.
_OFFSETS = {
    2: {
        "row_size": 119, "model_path_ref": 0x0D, "npc_kind": 0x15, "max_hp": 0x1F, "voice_bank_ref": 0x34,
        "vehicle_type": 0x3A, "name_kr_ref": 0x44, "title_kr_ref": 0x48, "level": 0x4F,
        "action_script_ref": 0x5D, "inventory_max": 0x65, "condition_script_ref": 0x6A, "carriage_type": 0x71,
        "no_vehicle_type": 65,
    },
    1: {
        "row_size": 121, "model_path_ref": 0x0D, "npc_kind": 0x19, "max_hp": 0x23, "voice_bank_ref": 0x38,
        "vehicle_type": 0x3E, "name_kr_ref": 0x48, "title_kr_ref": 0x4C, "level": 0x53,
        "action_script_ref": 0x61, "inventory_max": 0x67, "condition_script_ref": 0x6D, "carriage_type": 0x74,
        "no_vehicle_type": 63,
    },
}


def _row(layout: int, vehicle_type: int) -> bytes:
    offsets = _OFFSETS[layout]
    row = bytearray(offsets["row_size"])
    struct.pack_into("<H", row, 0, _CHARACTER)
    row[offsets["npc_kind"]] = 3
    struct.pack_into("<f", row, offsets["max_hp"], _MAX_HP)
    row[offsets["vehicle_type"]] = vehicle_type
    struct.pack_into("<I", row, offsets["level"], _LEVEL)
    row[offsets["inventory_max"]] = _INVENTORY_MAX
    row[offsets["carriage_type"]] = _CARRIAGE_TYPE
    for field, index in _STRING_FIELDS.items():
        struct.pack_into("<I", row, offsets[field], index)
    return bytes(row)


def _file(row: bytes) -> bytes:
    """`charactersimply.bss` holding one row and the string table it points into."""
    head = b"PABR" + struct.pack("<I", 1) + row
    table = struct.pack("<I", len(_STRINGS)) + b"".join(
        struct.pack("<BI", 1, len(text.encode("utf-16-le"))) + text.encode("utf-16-le") for text in _STRINGS
    )
    return head + table + struct.pack("<II", len(head), 0)


@pytest.mark.parametrize("layout", sorted(_OFFSETS))
def test_each_layout_reads_the_same_row(layout: int) -> None:
    (record,) = parse_charactersimply_records(_file(_row(layout, _VEHICLE)))

    assert (record["character_id"], record["npc_kind"], record["level"], record["max_hp"]) == (
        _CHARACTER, 3, _LEVEL, 2500,
    )
    assert (record["vehicle_type"], record["inventory_max"], record["carriage_type"]) == (
        _VEHICLE, _INVENTORY_MAX, _CARRIAGE_TYPE,
    )
    assert (record["model_path"], record["name_kr"], record["knowledge_id"]) == ("npc/boat", "배", 304)


@pytest.mark.parametrize("layout", sorted(_OFFSETS))
def test_the_layouts_no_vehicle_value_reads_as_none(layout: int) -> None:
    (record,) = parse_charactersimply_records(_file(_row(layout, _OFFSETS[layout]["no_vehicle_type"])))

    assert record["vehicle_type"] is None


def test_layout_1_rows_hold_none_for_the_layout_2_only_field() -> None:
    (record,) = parse_charactersimply_records(_file(_row(1, _VEHICLE)))

    assert record["unknown_76"] is None


def test_a_row_of_another_size_names_where_each_layout_broke() -> None:
    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 2: .*; Layout 1: "):
        parse_charactersimply_records(_file(bytes(120)))


def test_the_layout_covering_the_client_is_tried_first() -> None:
    set_handler_client(1784)

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 1: .*; Layout 2: "):
        parse_charactersimply_records(_file(bytes(120)))
