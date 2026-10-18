"""`multiplequest.bss`: a range of quest IDs per quest chain.

    PABR | u32 count | count x (u16 quest_chain_id, u16 min_quest_id, u16 max_quest_id)
    | u32 0 (empty string table) | u32 string_table_start | u32 0

Layout in docs/file-formats/multiplequest_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "multiplequest.bss"

# u16 quest_chain_id | u16 min_quest_id | u16 max_quest_id
ROW = struct.Struct("<HHH")


def parse_multiplequest_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a bad magic or a row count that does not end where
    the trailer says the string table starts.
    """
    records = []
    for pos in fixed_row_offsets(data, ROW.size, FILE_NAME):
        quest_chain_id, min_quest_id, max_quest_id = ROW.unpack_from(data, pos)
        records.append({
            "quest_chain_id": quest_chain_id,
            "min_quest_id": min_quest_id,
            "max_quest_id": max_quest_id,
        })
    return records
