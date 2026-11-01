"""Both documented Class Record layouts read back from a small built file and its offset file."""

from __future__ import annotations

import struct
from dataclasses import dataclass

import pytest

from bdo_preview import set_handler_client
from .parser import parse_pcgrowth_records


_CLASS_TYPE = 17  # Shai
_CHARACTER = 1
_RESOURCE_TYPE = 2
_NAME = "샤이"
_MODEL = "1_Pc/PSW/Weapon/PSW_01.pac"
_LIFE_SKILLS = ((0, 31), (4, 31))


@dataclass(frozen=True)
class _Shape:
    """One layout as pcgrowth_dbss.md writes it."""

    has_unknown_09: bool
    setup_size: int
    combat_resource_type: int
    has_unknown_37: bool


_SHAPES = {
    2: _Shape(True, 99, 0x5E, True),
    1: _Shape(False, 63, 0x3A, False),
}


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def _str8(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("ascii")


def _model_list() -> bytes:
    return struct.pack("<IB", 1, 1) + _str8(_MODEL)


def _body(shape: _Shape) -> bytes:
    setup = bytearray(shape.setup_size)
    setup[shape.combat_resource_type] = _RESOURCE_TYPE
    pairs = [value for pair in _LIFE_SKILLS for value in pair]
    return (
        struct.pack("<BHHHH", _CLASS_TYPE, _CHARACTER, 117, 523, 217)
        + (struct.pack("<I", 0) if shape.has_unknown_09 else b"")
        + struct.pack("<B", 101)  # unknown_0d
        + struct.pack("<II", 1, 10001)  # starter_weapons
        + bytes(setup)
        + _str16(_NAME) + _str16("") + _str16("")
        + struct.pack("<B", 1)  # gender
        + b"".join(_str8("") for _ in range(4))
        + struct.pack("<3f3fB3IBB3ff", 1, 1, 1, 1, 1, 1, 0, 10001, 0, 0, 1, 0, 100, 0.7, -0.3, 20)
        + (struct.pack("<I", 0) if shape.has_unknown_37 else b"")
        + struct.pack("<I", 0)  # unknown_list
        + struct.pack(f"<I{len(pairs)}I", len(_LIFE_SKILLS), *pairs)
        + struct.pack("<I", 0)  # unknown_end
        + _model_list() + _model_list()
    )


def _files(body: bytes) -> tuple[bytes, bytes]:
    """`pcgrowth.dbss` holding one class row and its `pcgrowthoffset.dbss`."""
    data = struct.pack("<IB", 1, _CLASS_TYPE) + body
    return data, struct.pack("<IBII", 1, _CLASS_TYPE, 5, len(body))


@pytest.mark.parametrize("layout", sorted(_SHAPES))
def test_each_layout_reads_the_same_row(layout: int) -> None:
    (record,) = parse_pcgrowth_records(*_files(_body(_SHAPES[layout])))

    assert (record["class_type"], record["character_key"], record["name_kr"]) == (_CLASS_TYPE, _CHARACTER, _NAME)
    assert (record["combat_resource_type"], record["is_open"]) == (_RESOURCE_TYPE, True)
    assert (record["default_life_skills"], record["weapon_models"]) == (list(_LIFE_SKILLS), [_MODEL])


def test_layout_1_has_no_unknown_09() -> None:
    (record,) = parse_pcgrowth_records(*_files(_body(_SHAPES[1])))

    assert record["unknown_09"] is None


def test_a_row_with_a_byte_too_many_names_where_each_layout_broke() -> None:
    data, offset_data = _files(_body(_SHAPES[2]) + b"\x00")

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 2: .*; Layout 1: "):
        parse_pcgrowth_records(data, offset_data)


def test_the_layout_covering_the_client_is_tried_first() -> None:
    set_handler_client(1784)
    data, offset_data = _files(bytes(16))

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 1: .*; Layout 2: "):
        parse_pcgrowth_records(data, offset_data)
