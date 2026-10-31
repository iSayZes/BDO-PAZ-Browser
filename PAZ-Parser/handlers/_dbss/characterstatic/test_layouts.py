"""The three documented Payload layouts read back from a small built file and its offset rows."""

from __future__ import annotations

import struct
from dataclasses import dataclass

import pytest

from bdo_preview import set_handler_client
from _common.pabr_offset import PabrOffsetRow
from .parser import NO_CLASS_TYPE, parse_characterstatic_records


_CHARACTER = 40015
_KNOWLEDGE = 304
_LEVEL = 33
_SOURCE_ITEM = 42000
_VEHICLE = 18  # Boat
_MAX_HP = 2500.0


@dataclass(frozen=True)
class _Shape:
    """The offsets of one layout as characterstatic_dbss.md writes them."""

    fields_size: int
    character_id: int
    npc_kind: int
    max_hp: int
    vehicle_type: int
    level: int
    holdable_item_count: int
    contents_group_count: int
    tail_size: int
    no_vehicle_type: int


_SHAPES = {
    3: _Shape(0x11F, 0x01, 0x05, 0x21, 0xA6, 0xC3, 0x0E, 0x18, 0x18, 65),
    2: _Shape(0x117, 0x01, 0x05, 0x21, 0xA6, 0xC3, 0x0E, 0x18, 0x17, 65),
    1: _Shape(0x12A, 0x02, 0x06, 0x22, 0xB9, 0xD5, 0x1E, 0x28, 0x13, 63),
}


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def _str8(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("ascii")


def _payload(shape: _Shape, vehicle_type: int) -> bytes:
    fields = bytearray(shape.fields_size)
    struct.pack_into("<H", fields, shape.character_id, _CHARACTER)
    fields[shape.npc_kind] = 3
    fields[shape.vehicle_type] = vehicle_type
    struct.pack_into("<f", fields, shape.max_hp, _MAX_HP)
    struct.pack_into("<I", fields, shape.level, _LEVEL)
    tail = bytearray(shape.tail_size)
    tail[0] = NO_CLASS_TYPE
    struct.pack_into("<I", tail, 0x09, _SOURCE_ITEM)
    return (
        bytes(8) + b"\x15"
        + _str16(f"getknowledge({_KNOWLEDGE});")
        + _str16("")
        + bytes(fields)
        + _str8("9999") + _str8("npc/boat") + _str16("배") + _str16("") + _str16("") + _str8("")
        + bytes(shape.holdable_item_count) + struct.pack("<I", 0)
        + bytes(shape.contents_group_count) + struct.pack("<II", 1, 0x6016CFF7)
        + bytes(tail)
    )


def _file(payload: bytes) -> tuple[bytes, list[PabrOffsetRow]]:
    """`characterstatic.dbss` holding one record, and its offset row."""
    data = struct.pack("<IH", 1, _CHARACTER) + payload
    return data, [PabrOffsetRow(_CHARACTER, 6, len(payload))]


@pytest.mark.parametrize("layout", sorted(_SHAPES))
def test_each_layout_reads_the_same_record(layout: int) -> None:
    (record,) = parse_characterstatic_records(*_file(_payload(_SHAPES[layout], _VEHICLE)))

    assert (record["character_id"], record["npc_kind"], record["level"]) == (_CHARACTER, 3, _LEVEL)
    assert (record["vehicle_type"], record["knowledge_id"], record["source_item_id"]) == (
        _VEHICLE, _KNOWLEDGE, _SOURCE_ITEM,
    )
    assert (record["name_kr"], record["max_hp"]) == ("배", 2500)


@pytest.mark.parametrize("layout", sorted(_SHAPES))
def test_the_layouts_no_vehicle_value_reads_as_none(layout: int) -> None:
    shape = _SHAPES[layout]
    (record,) = parse_characterstatic_records(*_file(_payload(shape, shape.no_vehicle_type)))

    assert record["vehicle_type"] is None


def test_client_1784_stores_63_for_no_vehicle_and_the_live_client_a_guild_dragon() -> None:
    (old,) = parse_characterstatic_records(*_file(_payload(_SHAPES[1], 63)))
    (live,) = parse_characterstatic_records(*_file(_payload(_SHAPES[3], 63)))

    assert (old["vehicle_type"], live["vehicle_type"]) == (None, 63)


def test_a_record_with_a_byte_too_many_names_where_each_layout_broke() -> None:
    data, rows = _file(_payload(_SHAPES[3], _VEHICLE) + b"\x00")

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 3: .*; Layout 2: .*; Layout 1: "):
        parse_characterstatic_records(data, rows)


def test_the_layout_covering_the_client_is_tried_first() -> None:
    set_handler_client(1784)
    data, rows = _file(bytes(64))

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 1: .*; Layout 3: .*; Layout 2: "):
        parse_characterstatic_records(data, rows)
