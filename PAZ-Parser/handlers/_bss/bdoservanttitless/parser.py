"""`bdoservanttitless.bss`: the breed title (Base Coat) of each horse.

    PABR | u32 record_count | record_count x 10-byte Row | String Table
    | u32 string_table_start | u32 0
    Row: u16 character_id | u32 title_name | u32 contents_option

`title_name` indexes the string table (`품종 1번` to `품종 24번`). Layout 2
in docs/file-formats/bdoservanttitless_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at


FILE_NAME = "bdoservanttitless.bss"

_ROW = struct.Struct("<HII")


def parse_bdoservanttitless_records(data: bytes) -> list[dict]:
    """Every row in file order, with its title text.

    Raises ValueError on a missing magic, rows that do not end where the
    string table starts, or a string table that runs past the trailer.
    """
    offsets = fixed_row_offsets(data, _ROW.size, FILE_NAME)
    strings = read_string_table(data)
    records = []
    for pos in offsets:
        character_id, title_name, contents_option = _ROW.unpack_from(data, pos)
        records.append(
            {
                "character_id": character_id,
                "title_name": title_name,
                "title_kr": string_at(strings, title_name),
                "contents_option": contents_option,
            }
        )
    return records
