"""The five documented Payload layouts read back from a small built file and its offset file."""

from __future__ import annotations

import struct
from dataclasses import dataclass

import pytest

from bdo_preview import set_handler_client
from .parser import parse_skilltype_records


_KEY = 0x0D820001  # skill 3458, level 1
_NAME = "광명의 태궁"
_ICON = "New_Icon/04_PC_Skill/01_PC_Skill/09_PEM_Skill/PEM_Skill_3458.dds"
_ICON_PATH = "ui_texture/icon/new_icon/04_pc_skill/01_pc_skill/09_pem_skill/pem_skill_3458.dds"
_AWAKENING_WEAPON = 1
_ACTIVE = 1


@dataclass(frozen=True)
class _Shape:
    """One layout as skilltype_dbss.md writes it."""

    has_movie_paths: bool
    # unknown_list_01 to is_developing_contents.
    flags_after_awakening_type: int
    has_unknown_code_09: bool
    has_unknown_code_0a: bool


_SHAPES = {
    5: _Shape(False, 3, True, True),
    4: _Shape(True, 3, True, True),
    3: _Shape(True, 3, True, False),
    2: _Shape(True, 3, False, False),
    1: _Shape(True, 2, False, False),
}


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def _str8(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("ascii")


def _payload(shape: _Shape, *, icon: str = _ICON) -> bytes:
    return (
        struct.pack("<I", _KEY)
        + _str16(_NAME)
        + _str16(_NAME)
        + struct.pack("<IH", _ACTIVE, 0)  # kind, unknown_group_name_04
        + struct.pack("<II", 1, _KEY + 1)  # next_rank_keys
        + struct.pack("<QQ", 1 << 29, 0)  # class_mask, unknown_next_rank_keys_08
        + bytes(9)  # equip type
        + struct.pack("<HII", 1, 0, _KEY)  # max_level, skill_owner_type, first_rank_key
        + _str8(icon)
        + _str16("")  # unknown_after_icon_path
        + _str16("설명")  # description
        + (_str8("UI_Movie/PEM_3458.webm") + _str8("") if shape.has_movie_paths else b"")
        + bytes(5)  # unknown_description_00 to can_quick_slot
        + struct.pack("<QI", 1, 2)  # unknown_list
        + struct.pack("<B", _AWAKENING_WEAPON)
        + bytes(shape.flags_after_awakening_type)
        + struct.pack("<II", 1, 0x6016CFF7)  # contents_group_hashes
        + struct.pack("<IH", 1, 3459)  # exclusive_skill_nos
        + b"\x00"  # condition
        + _str16("ARCHER_127")  # unknown_code
        + struct.pack("<BII", 1, 0, 0)  # branch, unknown_code_01, unknown_code_05
        + (b"\x02" if shape.has_unknown_code_09 else b"")
        + (_str16("") if shape.has_unknown_code_0a else b"")
    )


def _files(payload: bytes) -> tuple[bytes, bytes]:
    """`skilltype.dbss` holding one record and its `skilltypeoffset.dbss`."""
    data = struct.pack("<II", 1, _KEY) + payload  # count, key_prefix
    rows_end = 8 + 12
    offset_data = b"PABR" + struct.pack("<IIII", 1, _KEY, 8, len(payload)) + struct.pack("<III", 0, rows_end, 0)
    return data, offset_data


@pytest.mark.parametrize("layout", sorted(_SHAPES))
def test_each_layout_reads_the_same_record(layout: int) -> None:
    (record,) = parse_skilltype_records(*_files(_payload(_SHAPES[layout])))

    assert (record.skill_key, record.name_kr, record.kind) == (_KEY, _NAME, _ACTIVE)
    assert (record.icon_path, record.awakening_type) == (_ICON_PATH, _AWAKENING_WEAPON)


def test_a_png_icon_is_not_a_skill_icon() -> None:
    (record,) = parse_skilltype_records(*_files(_payload(_SHAPES[5], icon="Real_ETC/Scroll/Icon.png")))

    assert record.icon_path == ""


def test_a_record_with_a_byte_too_many_names_where_each_layout_broke() -> None:
    data, offset_data = _files(_payload(_SHAPES[5]) + b"\x00")

    with pytest.raises(
        ValueError, match=r"fits no known layout \(Layout 5: .*; Layout 4: .*; Layout 3: .*; Layout 2: .*; Layout 1: "
    ):
        parse_skilltype_records(data, offset_data)


def test_the_layout_covering_the_client_is_tried_first() -> None:
    set_handler_client(1784)
    data, offset_data = _files(_payload(_SHAPES[5]) + b"\x00")

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 4: .*; Layout 5: .*; Layout 3: "):
        parse_skilltype_records(data, offset_data)
