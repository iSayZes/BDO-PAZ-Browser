"""`itemimprovementdefaultdisplaylist.bss`: the stones the Reform window lists by default.

A `PABR` table of u32 stone item IDs with an empty string table. Layout in
docs/file-formats/itemimprovementdefaultdisplaylist_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "itemimprovementdefaultdisplaylist.bss"

_ROW = struct.Struct("<I")


def parse_itemimprovementdefaultdisplaylist_records(data: bytes) -> list[dict]:
    """Every stone in list order, numbered from 1.

    Raises ValueError on a missing magic or rows that do not end where the
    string table starts.
    """
    return [
        {"order": order, "item_id": _ROW.unpack_from(data, start)[0]}
        for order, start in enumerate(fixed_row_offsets(data, _ROW.size, FILE_NAME), start=1)
    ]
