"""`funtitureiteminfo.bss`: furniture items and the installation type of the object each one places.

    PABR | u32 row_count | row_count x row (9 bytes) | string table
    | u32 table_start | u32 0
    row: u32 item_key | u32 item_key_dup | u8 installation_type

The file name is spelled `funtiture` in the client. Layout 1 in
docs/file-formats/bss/funtitureiteminfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "funtitureiteminfo.bss"
KEY_FIELD = "item_key"

_ROW = struct.Struct("<IIB")
_FIELDS = (KEY_FIELD, "item_key_dup", "installation_type")


def parse_funtitureiteminfo_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a bad magic or when the rows do not end where the
    string table starts.
    """
    return [
        dict(zip(_FIELDS, _ROW.unpack_from(data, start), strict=True))
        for start in fixed_row_offsets(data, _ROW.size, FILE_NAME)
    ]
