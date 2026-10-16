"""`journalquest.dbss`: adventure journal books, located through `journalquestoffset.dbss`.

Each book record is self-describing:

    u32 journal_key | u32 book_key | u8 is_record_book
    | journal_name | journal_description | book_name | unlock_requirement
    | bookshelf_scene | book_model
    | u32 page_count | u32[page_count] page_quest_ids | u32 unknown_end

Strings are a u64 code-unit count followed by the text with no terminator: the
first four are UTF-16LE, the two model names ASCII. Page quest IDs pack
`(quest_id << 16) | quest_chain_id`. Full layout in
docs/file-formats/journalquest_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32, u32_hi, u32_lo
from _common.record_reader import RecordReader


_HEADER = struct.Struct("<IIB")
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


def _parse_book(block: bytes, row: int, offset_record: dict) -> dict:
    reader = RecordReader(block, 0, len(block), f"journalquest record {row}")
    group_id, entry_no, is_record_book = reader.unpack(_HEADER)
    journal_title = reader.text(wide=True)
    subtitle = reader.text(wide=True)
    page_vol_title = reader.text(wide=True)
    unlock_condition = reader.text(wide=True)
    combine_model = reader.text(wide=False)
    static_model = reader.text(wide=False)
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
        "group_id": group_id,
        "entry_no": entry_no,
        "is_record_book": is_record_book,
        # Every page of a book belongs to one quest chain.
        "journal_cat_id": pages[0]["journal_cat_id"] if pages else 0,
        "journal_title": journal_title,
        "subtitle": subtitle,
        "page_vol_title": page_vol_title,
        "unlock_condition": unlock_condition,
        "page_count": page_count,
        "page_refs": pages,
        "page_refs_text": ", ".join(f"{p['journal_cat_id']}:{p['page_no']}" for p in pages),
        "combine_model": combine_model,
        "static_model": static_model,
        "terminal": terminal,
    }


def parse_journalquest_records(data: bytes, offset_data: bytes) -> list[dict]:
    """One book per offset row, in offset-file order.

    Raises ValueError on the first record whose fields do not end exactly at
    its indexed size: the layout has changed and later fields would be misread.
    """
    records: list[dict] = []
    for row, offset_record in enumerate(parse_journalquest_offset_records(offset_data)):
        byte_offset = offset_record["byte_offset"]
        block = data[byte_offset:byte_offset + offset_record["byte_size"]]
        if len(block) != offset_record["byte_size"]:
            raise ValueError(f"journalquest record {row} exceeds file size")
        records.append(_parse_book(block, row, offset_record))
    return records
