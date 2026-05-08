from __future__ import annotations

import re

from _common.binary import u8, u32, u32_hi, u32_lo


_ASCII_RE = re.compile(rb"[ -~]{4,}")
_COMBINE_RE = re.compile(rb"Combine_[ -~]+")
_STATIC_RE = re.compile(rb"Adventure_Bookshelf[ -~]+")


def _read_ascii(data: bytes, offset: int) -> tuple[str, int]:
    end = offset
    while end < len(data) and 32 <= data[end] <= 126:
        end += 1
    return data[offset:end].decode("ascii", errors="replace"), end


def _clean_text(text: str, remove_marker: bool) -> str:
    result = text.replace("\\n", " ").strip()
    while result and ord(result[-1]) < 32:
        result = result[:-1].rstrip()
    if remove_marker and result and ord(result[-1]) < 128:
        result = result[:-1].rstrip()
    return result


def _find_aligned_nul(data: bytes, start: int, limit: int) -> int:
    for offset in range(start, limit - 1):
        if (offset - start) % 2 == 0 and data[offset:offset + 2] == b"\x00\x00":
            return offset
    return -1


def _parse_text_fields(block: bytes, limit: int) -> list[str]:
    fields: list[str] = []
    offset = 17

    while offset < limit - 1 and len(fields) < 4:
        end = _find_aligned_nul(block, offset, limit)
        if end < 0:
            break

        raw = block[offset:end]
        if raw:
            text = raw.decode("utf-16le", errors="replace")
            fields.append(_clean_text(text, remove_marker=len(fields) < 3))

        offset = end + 2
        while offset < limit and block[offset] == 0:
            offset += 1

    while len(fields) < 4:
        fields.append("")
    return fields


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


def _find_model_offsets(block: bytes) -> tuple[int, int]:
    combine_match = _COMBINE_RE.search(block)
    static_start = combine_match.end() if combine_match is not None else 0
    static_match = _STATIC_RE.search(block, static_start)
    if combine_match is None or static_match is None:
        ascii_matches = list(_ASCII_RE.finditer(block))
        if len(ascii_matches) >= 2:
            return ascii_matches[0].start(), ascii_matches[1].start()
        raise ValueError("journalquest record model strings not found")
    return combine_match.start(), static_match.start()


def _parse_page_refs(block: bytes, page_count_offset: int) -> tuple[int, int, list[dict]]:
    page_count = u32(block, page_count_offset)
    refs: list[dict] = []
    offset = page_count_offset + 4

    for index in range(page_count):
        raw_ref = u32(block, offset + index * 4)
        hi = u32_hi(raw_ref)
        lo = u32_lo(raw_ref)

        if hi <= 512 and lo > 512:
            page_no = hi
            journal_cat_id = lo
            encoding = "page_index_cat_id"
        else:
            journal_cat_id = hi
            page_no = lo + 1
            encoding = "cat_id_page_index"

        refs.append({
            "raw_ref": raw_ref,
            "journal_cat_id": journal_cat_id,
            "page_no": page_no,
            "encoding": encoding,
        })

    return page_count, u32(block, offset + page_count * 4), refs


def parse_journalquest_records(data: bytes, offset_data: bytes) -> list[dict]:
    offset_records = parse_journalquest_offset_records(offset_data)
    records: list[dict] = []

    for row, offset_record in enumerate(offset_records):
        byte_offset = offset_record["byte_offset"]
        byte_size = offset_record["byte_size"]
        block = data[byte_offset:byte_offset + byte_size]
        if len(block) != byte_size:
            raise ValueError(f"journalquest record {row} exceeds file size")
        if len(block) < 21:
            raise ValueError(f"journalquest record {row} is too small")

        combine_offset, static_offset = _find_model_offsets(block)
        text_fields = _parse_text_fields(block, combine_offset)
        combine_model, _ = _read_ascii(block, combine_offset)
        static_model, static_end = _read_ascii(block, static_offset)
        page_count, terminal, pages = _parse_page_refs(block, static_end)
        journal_cat_id = pages[0]["journal_cat_id"] if pages else 0

        records.append({
            "row": row,
            "offset": byte_offset,
            "size": byte_size,
            "group_id": u32(block, 0),
            "entry_no": u32(block, 4),
            "unknown_08": u32(block, 8),
            "unknown_0c": u32(block, 12),
            "unknown_10": u8(block, 16),
            "journal_cat_id": journal_cat_id,
            "journal_title": text_fields[0],
            "subtitle": text_fields[1],
            "page_vol_title": text_fields[2],
            "unlock_condition": text_fields[3],
            "page_count": page_count,
            "page_refs": pages,
            "page_refs_text": ", ".join(f"{p['journal_cat_id']}:{p['page_no']}" for p in pages),
            "combine_model": combine_model,
            "static_model": static_model,
            "terminal": terminal,
        })

    return records
