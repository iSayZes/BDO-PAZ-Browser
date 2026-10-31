"""Both documented Card layouts read back from a small built file and its offset file."""

from __future__ import annotations

import struct

import pytest

from bdo_preview import set_handler_client
from .parser import LAYOUTS, parse_mentalcard_records


_CARD = 3001
_THEME = 5101
_NAME = "벨리아 마을"
_ICON = "UI_Artwork/IC_03001.dds"
_HASHES = (0x1234, 0x5678)
_KNOWLEDGE_TYPE = 1  # Story
_KNOWLEDGE_LEVEL = 2  # local reputation level 2
_LAYOUT_END_SIZES = {layout.number: layout.end_size for layout in LAYOUTS}


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def _str8(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("ascii")


def _card(layout: int) -> bytes:
    """Card `_CARD` with a Favor combo, in the given layout's shape."""
    return (
        struct.pack("<IHBBfffBfII", _CARD, _THEME, 0, 0, 45.0, 49.0, 20.0, 0, 4.0, 3, 1)
        + _str16(_NAME)
        + _str16("")
        + struct.pack("<BBI", _KNOWLEDGE_TYPE, 0, _KNOWLEDGE_LEVEL)
        + _str8(_ICON)
        + _str16("")
        + struct.pack("<fff", 1.0, 2.0, 3.0)
        + struct.pack("<BII", 17, 0, len(_HASHES))
        + struct.pack(f"<{len(_HASHES)}I", *_HASHES)
        + bytes(_LAYOUT_END_SIZES[layout])
    )


def _files(card: bytes) -> tuple[bytes, bytes]:
    """`mentalcard.dbss` holding one card, and its offset file."""
    data = struct.pack("<I", 1) + card
    end_of_rows = 8 + 12
    offsets = b"PABR" + struct.pack("<IIII", 1, _CARD, 4, len(card)) + struct.pack("<III", 0, end_of_rows, 0)
    return data, offsets


@pytest.mark.parametrize("layout", [2, 1])
def test_each_layout_reads_the_same_card(layout: int) -> None:
    (card,) = parse_mentalcard_records(*_files(_card(layout)))

    assert (card.card_id, card.theme_id, card.name_kr) == (_CARD, _THEME, _NAME)
    assert (card.min_favor, card.max_favor, card.interest) == (45.0, 49.0, 20.0)
    assert (card.buff_type, card.varied_value, card.valid_turn, card.apply_turn) == (0, 4.0, 3, 1)
    assert card.position == (1.0, 2.0, 3.0)
    assert (card.knowledge_type, card.knowledge_level, card.contents_group_hashes) == (
        _KNOWLEDGE_TYPE, _KNOWLEDGE_LEVEL, _HASHES,
    )


def test_a_card_with_a_byte_too_many_names_where_each_layout_broke() -> None:
    data, offsets = _files(_card(2) + b"\x00")

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 2: .* 1 bytes before .*; Layout 1: .* 2 bytes before "):
        parse_mentalcard_records(data, offsets)


def test_the_layout_covering_the_client_is_tried_first() -> None:
    set_handler_client(1784)
    data, offsets = _files(bytes(64))

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 1: .*; Layout 2: "):
        parse_mentalcard_records(data, offsets)
