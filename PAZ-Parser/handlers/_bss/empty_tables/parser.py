"""Reads a PABR table that declares no records (docs/file-formats/empty_bss.md).

    PABR | u32 count (0) | u32 string_count (0) | u32 table_start (0x08) | u32 0

A file that declares records or strings raises ValueError, so a client that
fills the table shows a parse error instead of an empty preview.
"""

from __future__ import annotations

from _common.binary import u32
from _common.pabr_strings import (
    HEADER_SIZE,
    TRAILER_SIZE,
    check_rows_end,
    checked_string_table_start,
    read_string_table,
)

# The string table of an empty file holds only its u32 count.
_STRING_COUNT_SIZE = 4
EMPTY_PABR_SIZE = HEADER_SIZE + _STRING_COUNT_SIZE + TRAILER_SIZE


def parse_empty_pabr_table(data: bytes, file_name: str, status: str) -> list[dict]:
    """One status row; `extra_bytes` counts bytes past the 20 of the empty layout."""
    checked_string_table_start(data, file_name)
    count = u32(data, 4)
    if count != 0:
        raise ValueError(
            f"{file_name} declares {count} records, but only the empty layout is documented."
        )
    check_rows_end(data, HEADER_SIZE, f"{file_name} records")
    string_count = len(read_string_table(data))
    if string_count != 0:
        raise ValueError(f"{file_name} holds {string_count} strings, but the empty layout has none.")
    return [{"count": count, "status": status, "extra_bytes": len(data) - EMPTY_PABR_SIZE}]
