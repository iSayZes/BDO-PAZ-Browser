"""`carriagechar.bss`: the world map model of each warehouse transport carrier.

    PABR | u32 unknown_04 | rows up to table_start: (u16 character_key | u32 object_name_index)
    | u32 count | count x pstr | u32 table_start | u32 0

`unknown_04` is one less than the rows on every client checked, so the rows
are counted from the trailer. Layout in docs/file-formats/bss/carriagechar_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, read_string_table, string_at


FILE_NAME = "carriagechar.bss"

_ROW = struct.Struct("<HI")


def parse_carriagechar_records(data: bytes) -> list[dict]:
    """Every row in file order, with its model path resolved from the string table.

    Raises ValueError on a missing magic, a trailer outside the file, or rows
    that do not fill the space before the string table.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    rows_size = rows_end - HEADER_SIZE
    if rows_size % _ROW.size:
        raise ValueError(f"{FILE_NAME} rows take {rows_size} bytes, not a multiple of {_ROW.size}")

    strings = read_string_table(data)
    records: list[dict] = []
    for pos in range(HEADER_SIZE, rows_end, _ROW.size):
        character_key, object_name_index = _ROW.unpack_from(data, pos)
        records.append(
            {
                "character_key": character_key,
                "object_name_index": object_name_index,
                "object_name": string_at(strings, object_name_index),
            }
        )
    return records
