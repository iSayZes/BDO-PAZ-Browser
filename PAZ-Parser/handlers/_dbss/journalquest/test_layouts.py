"""Both documented Book Record layouts read back from a small built file and its offset file."""

from __future__ import annotations

import struct

import pytest

from .parser import parse_journalquest_records


_JOURNAL = 1
_PAGES = [(1 << 16) | 3001, (2 << 16) | 3001]
_UNLOCK = "59레벨 달성"


def _str16(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("utf-16-le")


def _str8(text: str) -> bytes:
    return struct.pack("<Q", len(text)) + text.encode("ascii")


def _pages() -> bytes:
    return struct.pack(f"<I{len(_PAGES)}II", len(_PAGES), *_PAGES, 0)


def _book_layout_2(book_key: int) -> bytes:
    return b"".join((
        struct.pack("<IIB", _JOURNAL, book_key, 1),
        _str16("일지"), _str16("설명"), _str16("1권"), _str16(_UNLOCK),
        _str8("Combine_Etc_Adventure_Bookshelf01"), _str8("Adventure_Bookshelf_Static_book_00"),
        _pages(),
    ))


def _book_layout_1(book_key: int) -> bytes:
    return b"".join((
        struct.pack("<II", _JOURNAL, book_key),
        _str16("일지"), _str16("설명"), _str16(_UNLOCK),
        struct.pack("<I", 5),
        _str8("Icon/Quest/Journal_BlackSpirit.dds"),
        _pages(),
    ))


def _files(books: list[bytes]) -> tuple[bytes, bytes]:
    """`journalquest.dbss` with one group of `books`, and its offset file."""
    data = bytearray(struct.pack("<II", 1, len(books)))
    entries = []
    for book_key, book in enumerate(books, start=1):
        entries.append((book_key, len(data), len(book)))
        data += book
    offsets = struct.pack("<III", 1, _JOURNAL, len(entries)) + b"".join(struct.pack("<III", *e) for e in entries)
    return bytes(data), offsets


def test_layout_2_books_keep_their_flag_unlock_text_and_models() -> None:
    (book,) = parse_journalquest_records(*_files([_book_layout_2(1)]))

    assert (book["is_record_book"], book["page_vol_title"], book["unlock_condition"]) == (1, "1권", _UNLOCK)
    assert book["static_model"] == "Adventure_Bookshelf_Static_book_00"


def test_layout_1_books_read_the_unlock_text_and_icon() -> None:
    books = parse_journalquest_records(*_files([_book_layout_1(1), _book_layout_1(2)]))

    assert [b["entry_no"] for b in books] == [1, 2]
    first = books[0]
    assert (first["unlock_condition"], first["unknown_unlock_requirement_kr_00"]) == (_UNLOCK, 5)
    assert first["unknown_icon_path"] == "Icon/Quest/Journal_BlackSpirit.dds"
    assert [p["raw_ref"] for p in first["page_refs"]] == _PAGES
    assert "is_record_book" not in first and "page_vol_title" not in first


def test_a_book_that_fits_no_layout_names_where_each_broke() -> None:
    data, offsets = _files([_book_layout_1(1) + b"\x00"])

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 2: .*; Layout 1: .*after its page list"):
        parse_journalquest_records(data, offsets)
