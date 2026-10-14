"""`stringtable.bss`: the client's named UI string sheets.

A PABR file of sheets, then the shared counted string table and trailer:

    PABR | u32 sheet_count | sheet_count x sheet | string table | trailer
    sheet: u32 sheet_hash | u32 name_ref | u32 row_count
           | row_count x (u32 key_hash | u32 key_ref | u32 value_ref | u32 0)

`key_hash` is the LOC type 37 `str_id1` of the key, and the sheet fixes
`str_id2` (`GAME` = 1). Full layout in docs/file-formats/stringtable_bss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Iterable, Iterator
from dataclasses import dataclass

from _common.pabr_strings import read_string_table, string_at

_MAGIC = b"PABR"
_U32 = struct.Struct("<I")
_SHEET_HEADER = struct.Struct("<III")
_ROW = struct.Struct("<IIII")

GAME_SHEET = "GAME"
# LOC type 37 str_id2 of the GAME sheet's keys.
GAME_SHEET_LOC_ID2 = 1

# The sheet of the UI panel resources (`PANEL_*` keys).
RESOURCE_SHEET = "RESOURCE"

# LOC type 37 str_id2 of every sheet's keys, by sheet name (stringtable_bss.md).
SHEET_LOC_ID2 = {
    "CUTSCENE": 0,
    GAME_SHEET: GAME_SHEET_LOC_ID2,
    RESOURCE_SHEET: 2,
    "ACTIONCHART": 3,
    "TOOL": 4,
    "WEB": 5,
    "SymbolNo": 6,
    "IMAGESLIDE": 7,
}


@dataclass(frozen=True)
class StringRow:
    """One keyed UI string: its sheet, key, key hash and Korean text."""

    sheet: str
    key_hash: int
    key: str
    value: str


def _iter_sheets(data: bytes, strings: list[str]) -> Iterator[tuple[str, bytes]]:
    """`(sheet name, row bytes)` for every sheet in file order.

    Raises ValueError when the file is not a PABR string table or a sheet runs
    past the file.
    """
    if data[:4] != _MAGIC:
        raise ValueError("stringtable.bss does not start with PABR")

    (sheet_count,) = _U32.unpack_from(data, 4)
    pos = 8
    for _ in range(sheet_count):
        _, name_ref, row_count = _SHEET_HEADER.unpack_from(data, pos)
        pos += _SHEET_HEADER.size
        rows_end = pos + row_count * _ROW.size
        if rows_end > len(data):
            raise ValueError(f"stringtable sheet at 0x{pos:X} runs past the file")
        yield string_at(strings, name_ref), data[pos:rows_end]
        pos = rows_end


def parse_rows(data: bytes) -> list[StringRow]:
    """Every row of every sheet, in file order."""
    strings = read_string_table(data)
    return [
        StringRow(sheet, key_hash, string_at(strings, key_ref), string_at(strings, value_ref))
        for sheet, rows in _iter_sheets(data, strings)
        for key_hash, key_ref, value_ref, _ in _ROW.iter_unpack(rows)
    ]


def parse_sheet_key_hashes(data: bytes, sheet_names: Iterable[str]) -> dict[str, dict[str, int]]:
    """`sheet -> {key -> key_hash}` for the named sheets; absent sheets map to {}."""
    wanted = set(sheet_names)
    found: dict[str, dict[str, int]] = {name: {} for name in wanted}
    strings = read_string_table(data)
    for name, rows in _iter_sheets(data, strings):
        if name in wanted:
            found[name] = {
                string_at(strings, key_ref): key_hash
                for key_hash, key_ref, _, _ in _ROW.iter_unpack(rows)
            }
    return found


def parse_key_hashes(data: bytes, sheet_name: str) -> dict[str, int]:
    """`key -> key_hash` for every row of one sheet; empty when it is absent."""
    return parse_sheet_key_hashes(data, (sheet_name,))[sheet_name]
