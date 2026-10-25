"""`itemlinkprice.bss`: items whose price follows another item's price.

    PABR | u32 count | count x (u32 price_follow_item_key, u32 price_target_item_key)
    | u32 0 (empty string table) | u32 string_table_start | u32 0

Layout 1 in docs/file-formats/bss/itemlinkprice_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "itemlinkprice.bss"

_ROW = struct.Struct("<II")


def parse_itemlinkprice_records(data: bytes) -> list[dict]:
    """Every pair in file order.

    Raises ValueError on a missing magic or a row count that does not end
    where the trailer says the string table starts.
    """
    records = []
    for pos in fixed_row_offsets(data, _ROW.size, FILE_NAME):
        follow_item_key, target_item_key = _ROW.unpack_from(data, pos)
        records.append({"price_follow_item_key": follow_item_key, "price_target_item_key": target_item_key})
    return records
