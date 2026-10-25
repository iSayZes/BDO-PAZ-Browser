"""`barter_npclist.bss`: the barter NPC of each barter region.

    PABR | u32 count | count x (u16 barter_region_key, u16 character_id)
    | u32 0 (empty string table) | u32 string_table_start | u32 0

Full layout in docs/file-formats/bss/barter_npclist_bss.md.
"""

from __future__ import annotations

from _common.binary import u16
from _common.pabr_strings import fixed_row_offsets


ROW_SIZE = 4

# Row field offsets.
_BARTER_REGION_KEY = 0x00
_CHARACTER_ID = 0x02


def parse_barter_npclist_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a missing magic or a row count that does not end
    where the trailer says the string table starts.
    """
    return [
        {
            "barter_region_key": u16(data, pos + _BARTER_REGION_KEY),
            "character_id": u16(data, pos + _CHARACTER_ID),
        }
        for pos in fixed_row_offsets(data, ROW_SIZE, "barter_npclist.bss")
    ]
