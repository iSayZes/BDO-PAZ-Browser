"""`playercharacterstatic.bss`: the characters a player can play.

    PABR | u32 character_count | character_count x u16 character_key
    | String Table (empty) | u32 string_table_start | u32 0

Layout 1 in docs/file-formats/playercharacterstatic_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_pabr, check_rows_end


FILE_NAME = "playercharacterstatic.bss"
KEY_FIELD = "character_key"

_COUNT_OFFSET = 4
_KEY = struct.Struct("<H")


def parse_playercharacterstatic_records(data: bytes) -> list[dict]:
    """Every character key in file order.

    Raises ValueError on a missing magic or keys that do not end where the
    string table starts.
    """
    check_pabr(data, FILE_NAME)
    rows_end = HEADER_SIZE + u32(data, _COUNT_OFFSET) * _KEY.size
    check_rows_end(data, rows_end, f"{FILE_NAME} keys")
    return [{KEY_FIELD: key} for (key,) in _KEY.iter_unpack(data[HEADER_SIZE:rows_end])]
