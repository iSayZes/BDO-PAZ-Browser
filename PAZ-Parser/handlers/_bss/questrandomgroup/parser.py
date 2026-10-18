"""`questrandomgroup.bss`: the groups `checkRandomGroup(group, index)` reads.

    PABR | u32 count | count x row | string table | u32 string_table_start | u32 0

    row (32 bytes): u64 unknown_00 | u32 group_key | u16 quest_count
        | u16 quest_chain_id | u16 draw_count | u16 unknown_12 | u32 unknown_14
        | bytes[8] unknown_18

The string table is empty. Layout in docs/file-formats/questrandomgroup_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "questrandomgroup.bss"

ROW = struct.Struct("<QIHHHHI8s")


def parse_questrandomgroup_records(data: bytes) -> list[dict]:
    """One record per row, in file order.

    Raises ValueError on a bad magic or rows that do not end where the
    string table starts.
    """
    records: list[dict] = []
    for pos in fixed_row_offsets(data, ROW.size, FILE_NAME):
        (
            unknown_00,
            group_key,
            quest_count,
            quest_chain_id,
            draw_count,
            unknown_12,
            unknown_14,
            unknown_18,
        ) = ROW.unpack_from(data, pos)
        records.append({
            "group_key": group_key,
            "quest_count": quest_count,
            "quest_chain_id": quest_chain_id,
            "draw_count": draw_count,
            "unknown_00": unknown_00,
            "unknown_12": unknown_12,
            "unknown_14": unknown_14,
            "unknown_18": unknown_18.hex(),
        })
    return records
