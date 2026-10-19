"""Counted string table at the end of a PABR `.bss` file.

    ... rows ... | u32 count | count x (u8 is_wide | u32 byte_length | payload)
    | u32 string_table_start | u32 0

Wide entries are UTF-16LE, the rest UTF-8. Records point into the table by
index. `exploration.bss` and `npcsimply.bss` share this tail.
"""

from __future__ import annotations

from _common.binary import u32
from _common.pabr_offset import PABR_MAGIC


TRAILER_SIZE = 8
# ASCII PABR and a u32 row count.
HEADER_SIZE = 8
U32_SIZE = 4

_ENTRY_HEADER_SIZE = 5


def string_table_start(data: bytes) -> int:
    """Offset stored in the 8-byte trailer, where the rows end."""
    return u32(data, len(data) - TRAILER_SIZE)


def check_pabr(data: bytes, file_name: str) -> None:
    """Raise ValueError unless `data` holds the PABR header and the trailer."""
    if len(data) < HEADER_SIZE + TRAILER_SIZE or data[:4] != PABR_MAGIC:
        raise ValueError(f"{file_name} has invalid magic.")


def check_rows_end(data: bytes, rows_end: int, what: str) -> None:
    """Raise ValueError unless `what` ends where the string table starts.

    A mismatch means the row layout has changed and every field is suspect.
    """
    table_start = string_table_start(data)
    if rows_end != table_start:
        raise ValueError(
            f"{what} end at 0x{rows_end:X} but the string table starts at 0x{table_start:X}"
        )


def fixed_row_offsets(data: bytes, row_size: int, file_name: str) -> range:
    """Start of every row of a PABR file with fixed-size rows.

    Raises ValueError on a bad magic or when the rows do not fill the space
    before the string table.
    """
    check_pabr(data, file_name)
    rows_end = HEADER_SIZE + u32(data, 4) * row_size
    check_rows_end(data, rows_end, f"{file_name} rows")
    return range(HEADER_SIZE, rows_end, row_size)


def u32_rows(data: bytes, file_name: str) -> list[int]:
    """Every row of a PABR file whose rows are one u32 each, in file order.

    Raises ValueError like `fixed_row_offsets()`.
    """
    return [u32(data, start) for start in fixed_row_offsets(data, U32_SIZE, file_name)]


def checked_string_table_start(data: bytes, file_name: str) -> int:
    """Where variable-size records stop. Raises ValueError on a bad magic or trailer."""
    check_pabr(data, file_name)
    end = string_table_start(data)
    if not HEADER_SIZE <= end <= len(data) - TRAILER_SIZE:
        raise ValueError(f"{file_name} string table offset 0x{end:X} is outside the file")
    return end


def read_string_table(data: bytes) -> list[str]:
    """Every string in table order.

    Raises ValueError when an entry runs into the trailer, since every later
    index would then point at the wrong text.
    """
    end = len(data) - TRAILER_SIZE
    start = string_table_start(data)
    if not 0 <= start <= end - 4:
        raise ValueError(f"string table offset 0x{start:X} is outside the file")

    count = u32(data, start)
    pos = start + 4
    strings: list[str] = []
    for _ in range(count):
        is_wide, length = data[pos], u32(data, pos + 1)
        text_start = pos + _ENTRY_HEADER_SIZE
        pos = text_start + length
        if pos > end:
            raise ValueError(f"string at 0x{text_start:X} runs past the string table")
        encoding = "utf-16-le" if is_wide else "utf-8"
        strings.append(data[text_start:pos].decode(encoding, errors="replace"))
    return strings


def string_at(strings: list[str], index: int) -> str:
    """The string at `index`, or an empty string when it is out of range."""
    return strings[index] if 0 <= index < len(strings) else ""
