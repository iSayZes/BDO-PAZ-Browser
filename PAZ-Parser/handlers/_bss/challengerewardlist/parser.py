"""`challengerewardlist.bss`: every item key a challenge (Rewards window) hands out.

    PABR | u32 item_count | item_count x u32 item_keys
    | string table | u32 table_start | u32 0

Each key is a packed item key (enchant level << 24 | item ID), ascending.
Layout 1 in docs/file-formats/challengerewardlist_bss.md.
"""

from __future__ import annotations

from _common.item_key import split_item_key
from _common.pabr_strings import u32_rows


FILE_NAME = "challengerewardlist.bss"
KEY_FIELD = "item_key"


def parse_challengerewardlist_records(data: bytes) -> list[dict]:
    """One record per item key, in file order, with its item ID and level.

    Raises ValueError on a bad magic or when the keys do not fill the space
    before the string table.
    """
    records: list[dict] = []
    for item_key in u32_rows(data, FILE_NAME):
        item_id, enchant_level = split_item_key(item_key)
        records.append({KEY_FIELD: item_key, "item_id": item_id, "enchant_level": enchant_level})
    return records
