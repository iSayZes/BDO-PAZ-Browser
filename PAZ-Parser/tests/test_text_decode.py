from __future__ import annotations

from bdo_preview import decode_text

# "오후" (PM), as the CreationTime in the .pa/.pc 3ds Max exports writes it.
_KOREAN = "오후"


def test_utf8_text_decodes_as_utf8() -> None:
    assert decode_text(_KOREAN.encode("utf-8")) == _KOREAN


def test_cp949_text_falls_back_to_cp949() -> None:
    data = f'CreationTime="2014-07-29 {_KOREAN} 8:08:51"'.encode("cp949")

    assert decode_text(data) == f'CreationTime="2014-07-29 {_KOREAN} 8:08:51"'


def test_truncated_utf8_drops_the_cut_character() -> None:
    data = ("abc" + _KOREAN).encode("utf-8")[:-1]

    assert decode_text(data, is_truncated=True) == "abc" + _KOREAN[0]


def test_untruncated_cut_character_is_not_dropped() -> None:
    data = ("abc" + _KOREAN).encode("utf-8")[:-1]

    assert decode_text(data) != "abc" + _KOREAN[0]


def test_bytes_valid_in_no_encoding_get_replacement_characters() -> None:
    assert decode_text(b"abc\xff") == "abc�"
