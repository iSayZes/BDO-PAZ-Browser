"""`itemexchangetoclassmapkey.bss`: the weapon exchange group of each item.

    PABR | u32 count | count x (u32 item_key | i32 key) | string table | u32 string_table_start | u32 0

The reverse of `itemexchangetoclass.dbss`: every item key that file lists,
once, with the `key` of its row. The string table is empty. Layout in
docs/file-formats/bss/itemexchangetoclassmapkey_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "itemexchangetoclassmapkey.bss"

# item_key, key
_ENTRY = struct.Struct("<Ii")


def parse_itemexchangetoclassmapkey_records(data: bytes) -> list[dict]:
    """Every entry in file order.

    Raises ValueError on a bad magic or entries that do not end where the
    string table starts.
    """
    records: list[dict] = []
    for offset in fixed_row_offsets(data, _ENTRY.size, FILE_NAME):
        item_key, key = _ENTRY.unpack_from(data, offset)
        records.append({"item_key": item_key, "key": key})
    return records
