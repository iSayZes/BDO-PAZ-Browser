"""The three documented Record layouts read back from a small built file and its offset file."""

from __future__ import annotations

import struct
from dataclasses import dataclass

import pytest

from bdo_preview import set_handler_client
from .parser import parse_buff_offset_rows, parse_buff_records


_BUFF_ID = 356
_NAME = "공격력 증가"
_EFFECT_TYPE = 1
_DURATION_MS = 600000
_DESCRIPTION = "공격력 +1"
_STACKING_CATEGORY = 21
# Above a u16, to show buff_level is a u32.
_LEVEL = 70000


@dataclass(frozen=True)
class _Shape:
    """One layout as buff_dbss.md writes it."""

    id_format: str
    # From the end of ui_effect: is_developing_contents, then in Layouts 2
    # and 3 stacking_category, is_exclusive and unknown_1a.
    tail_end_size: int


_SHAPES = {
    3: _Shape("I", 4),
    2: _Shape("H", 4),
    1: _Shape("H", 1),
}


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def _str8(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("ascii")


def _record(shape: _Shape, ui_effect: str = "") -> bytes:
    stats = bytearray(133)
    struct.pack_into("<I", stats, 0x00, _LEVEL)
    stats[0x08] = _EFFECT_TYPE
    struct.pack_into("<I", stats, 0x68, _DURATION_MS)
    tail_end = bytearray(shape.tail_end_size)
    tail_end[0] = 1  # is_developing_contents
    if shape.tail_end_size > 1:
        tail_end[1] = _STACKING_CATEGORY
        tail_end[2] = 1  # is_exclusive
    return (
        struct.pack(f"<{shape.id_format}", _BUFF_ID)
        + _str16(_NAME)
        + bytes(stats)
        + _str16("0")  # effect_name
        + _str8("")  # icon_path
        + struct.pack("<BI", 1, 1000000)  # is_shown, apply_rate
        + _str16(_DESCRIPTION)
        + bytes(15)  # unknown_00 to unknown_0b
        + _str8(ui_effect)
        + bytes(tail_end)
    )


def _files(shape: _Shape, record: bytes) -> tuple[bytes, bytes]:
    """`buff.dbss` holding one record and its `buffoffset.dbss`."""
    row = struct.pack(f"<{shape.id_format}II", _BUFF_ID, 4, len(record))
    offset_data = b"PABR" + struct.pack("<I", 1) + row + struct.pack("<III", 0, 8 + len(row), 0)
    return struct.pack("<I", 1) + record, offset_data


@pytest.mark.parametrize("layout", sorted(_SHAPES))
def test_each_layout_reads_the_same_record(layout: int) -> None:
    shape = _SHAPES[layout]
    (record,) = parse_buff_records(*_files(shape, _record(shape)))

    assert (record["buff_id"], record["name"], record["effect_type"]) == (_BUFF_ID, _NAME, _EFFECT_TYPE)
    assert (record["duration_ms"], record["description_kr"]) == (_DURATION_MS, _DESCRIPTION)
    assert (record["level"], record["is_developing_contents"]) == (_LEVEL, True)


@pytest.mark.parametrize("layout", sorted(_SHAPES))
def test_the_tail_reads_ui_effect_as_a_string(layout: int) -> None:
    """Every client read so far stores it empty; a set one moves the tail end."""
    shape = _SHAPES[layout]
    (record,) = parse_buff_records(*_files(shape, _record(shape, "fx_buff_glow")))

    assert (record["ui_effect"], record["is_developing_contents"]) == ("fx_buff_glow", True)


@pytest.mark.parametrize("layout", sorted(_SHAPES))
def test_only_layout_1_holds_none_for_the_stacking_fields(layout: int) -> None:
    shape = _SHAPES[layout]
    (record,) = parse_buff_records(*_files(shape, _record(shape)))

    expected = (None, None) if layout == 1 else (_STACKING_CATEGORY, True)
    assert (record["stacking_category"], record["is_exclusive"]) == expected


@pytest.mark.parametrize("layout", sorted(_SHAPES))
def test_the_offset_view_reads_both_row_widths(layout: int) -> None:
    shape = _SHAPES[layout]
    _data, offset_data = _files(shape, _record(shape))

    ((buff_id, offset, size),) = [(row.entry_id, row.offset, row.size) for row in parse_buff_offset_rows(offset_data)]

    assert (buff_id, offset, size) == (_BUFF_ID, 4, len(_record(shape)))


def test_a_record_with_a_byte_too_many_names_where_each_layout_broke() -> None:
    shape = _SHAPES[2]
    data, offset_data = _files(shape, _record(shape) + b"\x00")

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 3: .*; Layout 2: .*; Layout 1: "):
        parse_buff_records(data, offset_data)


def test_the_layout_covering_the_client_is_tried_first() -> None:
    set_handler_client(1784)
    shape = _SHAPES[3]
    data, offset_data = _files(shape, bytes(16))

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 1: .*; Layout 3: .*; Layout 2: "):
        parse_buff_records(data, offset_data)
