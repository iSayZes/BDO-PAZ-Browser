"""`itemimprovementdefaultdisplaylist.bss`: the stones the Reform window lists by default.

A `PABR` table of u32 stone item IDs with an empty string table. Layout in
docs/file-formats/bss/itemimprovementdefaultdisplaylist_bss.md.
"""

from __future__ import annotations

from _common.pabr_strings import u32_rows


FILE_NAME = "itemimprovementdefaultdisplaylist.bss"


def parse_itemimprovementdefaultdisplaylist_records(data: bytes) -> list[dict]:
    """Every stone in list order, numbered from 1.

    Raises ValueError on a missing magic or rows that do not end where the
    string table starts.
    """
    return [
        {"order": order, "item_id": item_id}
        for order, item_id in enumerate(u32_rows(data, FILE_NAME), start=1)
    ]
