"""`tooltiptable.dbss`: the lines skill and item tooltips are built from.

    PABR | Section[..table_start] | string table | u32 table_start | u32 0
    Section: u32 row_count | row_count x Row
    Row (21 bytes): u32 key_hash | u32 format_ref | u32 param_count
        | u32 tooltip_type | u8 unknown_10 | u32 icon_flags

Section `n` holds the rows of tooltip type `n`; `format_ref` indexes the
string table. `tooltiptableoffset.dbss` has the same frame, with 12-byte
index rows (u32 key_hash, u32 data_offset, u32 unknown_08) and an empty
string table. Layout 2 in docs/file-formats/dbss/tooltiptable_dbss.md; the
17-byte rows of Layout 1 (no `icon_flags`) are not read.
"""

from __future__ import annotations

import struct
from collections.abc import Iterator

from _common.binary import u32
from _common.inline_text import decode_inline_text
from _common.pabr_strings import checked_string_table_start, read_string_table, string_at


FILE_NAME = "tooltiptable.dbss"
OFFSET_FILE = "tooltiptableoffset.dbss"

_MAGIC_SIZE = 4
_COUNT_SIZE = 4
_ROW = struct.Struct("<IIIIBI")
_INDEX_ROW = struct.Struct("<III")


def _section_rows(data: bytes, row_size: int, file_name: str) -> Iterator[tuple[int, int]]:
    """(section number, row start) of every row, section by section.

    Raises ValueError on a bad magic or trailer, or when the sections do not
    end where the string table starts.
    """
    end = checked_string_table_start(data, file_name)
    pos = _MAGIC_SIZE
    section = 0
    while pos < end:
        if pos + _COUNT_SIZE > end:
            raise ValueError(f"{file_name} section {section} count at 0x{pos:X} runs into the string table")
        count = u32(data, pos)
        rows_start = pos + _COUNT_SIZE
        pos = rows_start + count * row_size
        if pos > end:
            raise ValueError(
                f"{file_name} section {section} declares {count:,} rows that run past "
                f"the string table at 0x{end:X}"
            )
        for row_start in range(rows_start, pos, row_size):
            yield section, row_start
        section += 1
    if pos != end:
        raise ValueError(f"{file_name} sections end at 0x{pos:X} but the string table starts at 0x{end:X}")


def parse_tooltip_records(data: bytes) -> list[dict]:
    """Every row in file order, with its Korean text.

    Raises ValueError like `_section_rows()` or when a string runs past the
    string table.
    """
    row_starts = [row_start for _section, row_start in _section_rows(data, _ROW.size, FILE_NAME)]
    strings = read_string_table(data)
    records: list[dict] = []
    for row_start in row_starts:
        key_hash, format_ref, param_count, tooltip_type, unknown_10, icon_flags = _ROW.unpack_from(data, row_start)
        records.append({
            "key_hash": key_hash,
            "format_ref": format_ref,
            "format_kr": decode_inline_text(string_at(strings, format_ref)),
            "param_count": param_count,
            "tooltip_type": tooltip_type,
            "unknown_10": unknown_10,
            "icon_flags": icon_flags,
        })
    return records


def parse_tooltip_offset_rows(data: bytes) -> list[dict]:
    """Every index row in file order: its section (the tooltip type), key hash, row offset and `unknown_08`.

    Raises ValueError like `_section_rows()`.
    """
    records: list[dict] = []
    for section, row_start in _section_rows(data, _INDEX_ROW.size, OFFSET_FILE):
        key_hash, data_offset, unknown_08 = _INDEX_ROW.unpack_from(data, row_start)
        records.append({
            "tooltip_type": section,
            "key_hash": key_hash,
            "data_offset": data_offset,
            "unknown_08": unknown_08,
        })
    return records


def icon_bits(icon_flags: int) -> list[int]:
    """The set bits of `icon_flags`, lowest first."""
    return [bit for bit in range(icon_flags.bit_length()) if icon_flags >> bit & 1]
