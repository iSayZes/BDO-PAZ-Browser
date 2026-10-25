"""`letter.bss`: the letter window an item opens (text key, background, alignment).

    PABR | u32 row_count | row_count x row (13 bytes) | string table
    | u32 table_start | u32 0
    row: u32 item_key | u32 main_desc_string_index | u32 texture_path_index
         | u8 is_center_alignment

Both string indexes point into the PABR string table at the end of the
file. Layout 2 in docs/file-formats/bss/letter_bss.md; clients before it
have no center alignment byte (Layout 1), which this parser does not read.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at


FILE_NAME = "letter.bss"
KEY_FIELD = "item_key"

_ROW = struct.Struct("<IIIB")


def parse_letter_records(data: bytes) -> list[dict]:
    """Every row in file order, with its two strings read from the string table.

    Raises ValueError on a bad magic, rows that do not end where the string
    table starts, or a string that runs past it.
    """
    starts = fixed_row_offsets(data, _ROW.size, FILE_NAME)
    strings = read_string_table(data)
    records = []
    for start in starts:
        item_key, desc_index, texture_index, is_center_alignment = _ROW.unpack_from(data, start)
        records.append(
            {
                KEY_FIELD: item_key,
                "main_desc_string_index": desc_index,
                "main_desc_string_key": string_at(strings, desc_index),
                "texture_path_index": texture_index,
                "texture_path": string_at(strings, texture_index),
                "is_center_alignment": is_center_alignment,
            }
        )
    return records
