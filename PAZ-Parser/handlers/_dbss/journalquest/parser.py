"""`journalquest.dbss`: adventure journal books, located through `journalquestoffset.dbss`.

Each book record is self-describing:

    u32 journal_key | u32 book_key | u8 is_record_book
    | journal_name | journal_description | book_name | unlock_requirement
    | bookshelf_scene | book_model
    | u32 page_count | u32[page_count] page_quest_ids | u32 unknown_end

Strings are a u64 code-unit count followed by the text with no terminator: the
first four are UTF-16LE, the two model names ASCII. Page quest IDs pack
`(quest_id << 16) | quest_chain_id`.

Layout 1 (clients 1286 to 2138) books have no is_record_book, book name or
model names; after the unlock text they hold a u32 and an ASCII icon path. Nothing in
the file names its layout; the parser keeps the first layout, newest first,
whose every book ends at its indexed size (`LAYOUTS`). Both layouts in
docs/file-formats/dbss/journalquest_dbss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Callable
from dataclasses import dataclass

from _common.binary import u32, u32_hi, u32_lo
from _common.record_reader import RecordReader


_HEADER = struct.Struct("<IIB")
_KEYS = struct.Struct("<II")
_U32 = struct.Struct("<I")


def parse_journalquest_offset_records(data: bytes) -> list[dict]:
    if len(data) < 4:
        return []

    group_count = u32(data, 0)
    values = [u32(data, offset) for offset in range(0, len(data) - 3, 4)]
    cursor = 1
    records: list[dict] = []

    for group_index in range(group_count):
        if cursor + 2 > len(values):
            raise ValueError(f"journalquestoffset group {group_index} header exceeds file size")

        group_id = values[cursor]
        entry_count = values[cursor + 1]
        cursor += 2

        for _ in range(entry_count):
            if cursor + 3 > len(values):
                raise ValueError(f"journalquestoffset group {group_id} entries exceed file size")
            entry_no, byte_offset, byte_size = values[cursor:cursor + 3]
            cursor += 3
            records.append({
                "group_id": group_id,
                "entry_no": entry_no,
                "byte_offset": byte_offset,
                "byte_size": byte_size,
            })

    return records


def _page_ref(packed: int) -> dict:
    return {
        "raw_ref": packed,
        "journal_cat_id": u32_lo(packed),
        "page_no": u32_hi(packed),
    }


def _book_fields_layout_2(reader: RecordReader) -> dict:
    group_id, entry_no, is_record_book = reader.unpack(_HEADER)
    return {
        "group_id": group_id,
        "entry_no": entry_no,
        "is_record_book": is_record_book,
        "journal_title": reader.text(wide=True),
        "subtitle": reader.text(wide=True),
        "page_vol_title": reader.text(wide=True),
        "unlock_condition": reader.text(wide=True),
        "combine_model": reader.text(wide=False),
        "static_model": reader.text(wide=False),
    }


def _book_fields_layout_1(reader: RecordReader) -> dict:
    """Layout 1 stores no book name; its third string is the journal's unlock text."""
    group_id, entry_no = reader.unpack(_KEYS)
    journal_title = reader.text(wide=True)
    subtitle = reader.text(wide=True)
    unlock_condition = reader.text(wide=True)
    (unknown_unlock_requirement_kr_00,) = reader.unpack(_U32)
    return {
        "group_id": group_id,
        "entry_no": entry_no,
        "journal_title": journal_title,
        "subtitle": subtitle,
        "unlock_condition": unlock_condition,
        "unknown_unlock_requirement_kr_00": unknown_unlock_requirement_kr_00,
        "unknown_icon_path": reader.text(wide=False),
    }


@dataclass(frozen=True)
class BookLayout:
    """One documented Book Record shape; `number` is its Layout N in the doc.

    `read_fields` reads the fields before page_count.
    """

    number: int
    read_fields: Callable[[RecordReader], dict]


# Newest first.
LAYOUTS = (
    BookLayout(2, _book_fields_layout_2),
    BookLayout(1, _book_fields_layout_1),
)


def _parse_book(block: bytes, row: int, offset_record: dict, layout: BookLayout) -> dict:
    reader = RecordReader(block, 0, len(block), f"journalquest record {row}")
    fields = layout.read_fields(reader)
    (page_count,) = reader.unpack(_U32)
    packed_ids = reader.unpack(struct.Struct(f"<{page_count}I"))
    (terminal,) = reader.unpack(_U32)
    if not reader.at_end():
        raise ValueError(f"journalquest record {row} has bytes after its page list")

    pages = [_page_ref(packed) for packed in packed_ids]
    return {
        "row": row,
        "offset": offset_record["byte_offset"],
        "size": offset_record["byte_size"],
        **fields,
        # Every page of a book belongs to one quest chain.
        "journal_cat_id": pages[0]["journal_cat_id"] if pages else 0,
        "page_count": page_count,
        "page_refs": pages,
        "page_refs_text": ", ".join(f"{p['journal_cat_id']}:{p['page_no']}" for p in pages),
        "terminal": terminal,
    }


def _read_books(data: bytes, offset_rows: list[dict], layout: BookLayout) -> list[dict]:
    """Every book read with `layout`; raises ValueError on the first that does not end at its indexed size."""
    records: list[dict] = []
    for row, offset_record in enumerate(offset_rows):
        byte_offset = offset_record["byte_offset"]
        block = data[byte_offset:byte_offset + offset_record["byte_size"]]
        if len(block) != offset_record["byte_size"]:
            raise ValueError(f"journalquest record {row} exceeds file size")
        records.append(_parse_book(block, row, offset_record, layout))
    return records


def parse_journalquest_records(data: bytes, offset_data: bytes) -> list[dict]:
    """One book per offset row, in offset-file order, read with the first layout that fits.

    Raises ValueError, naming where each layout broke, when in every layout
    some record's fields do not end exactly at its indexed size.
    """
    offset_rows = parse_journalquest_offset_records(offset_data)
    breaks: list[str] = []
    for layout in LAYOUTS:
        try:
            return _read_books(data, offset_rows, layout)
        except ValueError as error:
            breaks.append(f"Layout {layout.number}: {error}")
    raise ValueError(f"journalquest.dbss fits no known layout ({'; '.join(breaks)})")
