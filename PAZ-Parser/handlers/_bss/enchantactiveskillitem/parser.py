"""`enchantactiveskillitem.bss`: the skill a piece of gear grants at an enhancement level.

    u32 count | count x (u32 item_key | u32 skill_key | u32 item_key_dup | u8 unknown_0c)

`item_key` packs `enchant_level << 24 | item_id`, `skill_key`
`skill_no << 16 | level`. Layout 1 in
docs/file-formats/enchantactiveskillitem_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import parse_counted_rows


FILE_NAME = "enchantactiveskillitem.bss"

_ROW = struct.Struct("<IIIB")
_FIELDS = ("item_key", "skill_key", "item_key_dup", "unknown_0c")


def parse_enchantactiveskillitem_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when the rows do not fill the file."""
    return parse_counted_rows(data, _ROW, _FIELDS, FILE_NAME)
