"""`cutscenecharacterdata.bss`: the character keys set aside as cutscene actors.

    PABR | u32 count | u16 character_key x count | string table (0 strings)
    | u32 string_table_start | u32 0

Layout in docs/file-formats/cutscenecharacterdata_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "cutscenecharacterdata.bss"

_ROW = struct.Struct("<H")


def parse_cutscenecharacterdata_records(data: bytes) -> list[dict]:
    """Every character key in file order.

    Raises ValueError on a missing magic or keys that do not end where the
    string table starts.
    """
    return [
        {"character_key": _ROW.unpack_from(data, start)[0]}
        for start in fixed_row_offsets(data, _ROW.size, FILE_NAME)
    ]
