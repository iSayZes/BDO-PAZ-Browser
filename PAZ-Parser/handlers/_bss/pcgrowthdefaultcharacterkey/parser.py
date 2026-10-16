"""`pcgrowthdefaultcharacterkey.bss`: one character key next to the class tables.

    PABR | u16 character_key | string table (0 strings)
    | u32 string_table_start | u32 0

No row count: the single u16 is the only row, so the string table starts at
0x06. Layout in docs/file-formats/pcgrowthdefaultcharacterkey_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import PABR_MAGIC
from _common.pabr_strings import check_pabr, check_rows_end


FILE_NAME = "pcgrowthdefaultcharacterkey.bss"

_CHARACTER_KEY = struct.Struct("<H")
_ROWS_START = len(PABR_MAGIC)


def parse_default_character_key(data: bytes) -> list[dict]:
    """The one record of the file.

    Raises ValueError on a bad magic, or when the string table does not start
    right after the u16: then the file holds more than the one key.
    """
    check_pabr(data, FILE_NAME)
    check_rows_end(data, _ROWS_START + _CHARACTER_KEY.size, f"{FILE_NAME} character key")
    (character_key,) = _CHARACTER_KEY.unpack_from(data, _ROWS_START)
    return [{"character_key": character_key}]
