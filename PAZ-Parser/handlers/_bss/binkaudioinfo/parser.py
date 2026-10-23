"""`binkaudioinfo.bss`: the Wwise event and bank of each Bink movie.

    PABR | u32 row_count | row_count x row | String Table
    | u32 string_table_start | u32 0
    row: u32 movie_name | u32 audio_name | u32 audio_name_dup
         | u8 unknown_0c | u8 unknown_0d | u8 unknown_0e

The three names index the string table; the record carries their text as
`<field>_text`. Layout 1 in docs/file-formats/binkaudioinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at


FILE_NAME = "binkaudioinfo.bss"
STRING_FIELDS = ("movie_name", "audio_name", "audio_name_dup")

_ROW = struct.Struct("<III3B")
_FIELDS = (*STRING_FIELDS, "unknown_0c", "unknown_0d", "unknown_0e")


def parse_binkaudioinfo_records(data: bytes) -> list[dict]:
    """Every row in file order, with the text of its names.

    Raises ValueError on a missing magic or rows that do not end where the
    string table starts.
    """
    starts = fixed_row_offsets(data, _ROW.size, FILE_NAME)
    strings = read_string_table(data)
    records = [dict(zip(_FIELDS, _ROW.unpack_from(data, start), strict=True)) for start in starts]
    return [
        {**record, **{f"{field}_text": string_at(strings, record[field]) for field in STRING_FIELDS}}
        for record in records
    ]
