"""`manufactureitemnaminginfo.bss`: the items that take the crafter's name through processing.

A `PABR` table of u32 item IDs with an empty string table. Layout in
docs/file-formats/manufactureitemnaminginfo_bss.md.
"""

from __future__ import annotations

from _common.pabr_strings import u32_rows


FILE_NAME = "manufactureitemnaminginfo.bss"


def parse_manufactureitemnaminginfo_records(data: bytes) -> list[dict]:
    """Every item ID in file order.

    Raises ValueError on a missing magic or rows that do not end where the
    string table starts.
    """
    return [{"item_id": item_id} for item_id in u32_rows(data, FILE_NAME)]
