"""`employeeexp.bss`: sailor EXP and level-up growth, one row per sailor and level.

    PABR | u32 count | count x 89-byte row | u32 0 | string table
    | u32 string_table_start | u32 0

Each row holds the EXP a sailor needs at that level and, per employee ability,
an index into the string table of dice expressions (`1D5+30`). Full layout in
docs/file-formats/employeeexp_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import TRAILER_SIZE, read_string_table, string_at, string_table_start


_MAGIC = b"PABR"
_HEADER_SIZE = 8
# unknown_after_rows: the u32 between the rows and the string table; 0 in every client seen so far.
_UNKNOWN_AFTER_ROWS_SIZE = 4

ABILITY_COUNT = 19

# u8 unknown_00 | u16 level | u16 employee_key | u32 exp_to_next_level
# | u32 unknown_09 | u32 growth_ref[ABILITY_COUNT]
_RECORD = struct.Struct(f"<BHHII{ABILITY_COUNT}I")
_RECORD_SIZE = 89
assert _RECORD.size == _RECORD_SIZE


def parse_employeeexp_records(data: bytes) -> list[dict]:
    """Every row in file order, with its growth dice resolved.

    Raises ValueError on a bad magic, or when the rows and the zero
    unknown_after_rows do not end where the string table starts: then the
    row size has changed and every field is suspect.
    """
    if len(data) < _HEADER_SIZE + TRAILER_SIZE or data[:4] != _MAGIC:
        raise ValueError("employeeexp.bss has invalid magic.")

    count = u32(data, 4)
    rows_end = _HEADER_SIZE + count * _RECORD_SIZE
    table_start = string_table_start(data)
    if rows_end + _UNKNOWN_AFTER_ROWS_SIZE != table_start or u32(data, rows_end) != 0:
        raise ValueError(
            f"employeeexp.bss rows end at 0x{rows_end:X}, which does not leave the "
            f"4-byte unknown_after_rows (0) before its string table at 0x{table_start:X}"
        )

    strings = read_string_table(data)
    return [
        _record(_RECORD.unpack_from(data, offset), strings)
        for offset in range(_HEADER_SIZE, rows_end, _RECORD_SIZE)
    ]


def _record(fields: tuple[int, ...], strings: list[str]) -> dict:
    unknown_00, level, employee_key, exp_to_next_level, unknown_09, *growth_refs = fields
    return {
        "employee_key": employee_key,
        "level": level,
        "exp_to_next_level": exp_to_next_level,
        "unknown_00": unknown_00,
        "unknown_09": unknown_09,
        "growth_refs": growth_refs,
        "growth_dice": [string_at(strings, ref) for ref in growth_refs],
    }
