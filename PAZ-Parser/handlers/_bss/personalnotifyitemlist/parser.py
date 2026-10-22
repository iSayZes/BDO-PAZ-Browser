"""`personalnotifyitemlist.bss`: a list of item IDs, ascending.

A `PABR` table of u32 item IDs with an empty string table. Layout 1 in
docs/file-formats/personalnotifyitemlist_bss.md.
"""

from __future__ import annotations

from _common.pabr_strings import u32_rows


FILE_NAME = "personalnotifyitemlist.bss"
KEY_FIELD = "item_id"


def parse_personalnotifyitemlist_records(data: bytes) -> list[dict]:
    """Every item ID in file order.

    Raises ValueError on a missing magic or rows that do not end where the
    string table starts.
    """
    return [{KEY_FIELD: item_id} for item_id in u32_rows(data, FILE_NAME)]
