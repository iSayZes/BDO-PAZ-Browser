"""`abyssoneaudioinfo.bss`: the music and ambience of the Abyss One fields.

    PABR | u32 row_count | row_count x row | String Table
    | u32 string_table_start | u32 0
    row: u16 field_no | u32 bgm_states[4] | u32 bank_no_environment

`field_no` is a `fieldinfo.bss` field; the row ends like an `audioinfo.bss`
area row (`_bss/audioinfo/bgm_states.py`). Layout 1 in
docs/file-formats/abyssoneaudioinfo_bss.md.
"""

from __future__ import annotations

import struct

from _bss.audioinfo.bgm_states import BGM_TAIL, bgm_fields
from _common.pabr_strings import fixed_row_offsets, read_string_table


FILE_NAME = "abyssoneaudioinfo.bss"
KEY_FIELD = "field_no"

_KEY = struct.Struct("<H")
_ROW_SIZE = _KEY.size + BGM_TAIL.size


def parse_abyssoneaudioinfo_records(data: bytes) -> list[dict]:
    """Every row in file order, with its state names.

    Raises ValueError on a missing magic or rows that do not end where the
    string table starts.
    """
    starts = fixed_row_offsets(data, _ROW_SIZE, FILE_NAME)
    strings = read_string_table(data)
    return [
        {
            KEY_FIELD: _KEY.unpack_from(data, start)[0],
            **bgm_fields(BGM_TAIL.unpack_from(data, start + _KEY.size), strings),
        }
        for start in starts
    ]
