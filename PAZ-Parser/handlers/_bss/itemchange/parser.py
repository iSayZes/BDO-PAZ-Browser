"""`itemchange.bss`: the Change Item conversions, an armor item to its costume.

    PABR | u32 row_count | row_count x 16-byte Row | String Table
    | u32 table_start | u32 0
    Row: u16 key | u16 key_dup | u32 from_item_key | u32 to_item_key | i32 type

Both item keys are packed (`enchant_level << 24 | item_id`). Layout 2 in
docs/file-formats/itemchange_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "itemchange.bss"
KEY_FIELD = "key"

_ROW = struct.Struct("<HHIIi")
_FIELDS = (KEY_FIELD, "key_dup", "from_item_key", "to_item_key", "type")


def parse_itemchange_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a bad magic or when the rows do not end where the
    string table starts.
    """
    return [
        dict(zip(_FIELDS, _ROW.unpack_from(data, pos), strict=True))
        for pos in fixed_row_offsets(data, _ROW.size, FILE_NAME)
    ]
