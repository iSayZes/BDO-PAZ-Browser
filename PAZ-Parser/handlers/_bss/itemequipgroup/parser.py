"""`itemequipgroup.bss`: equipment groups, each a list of item IDs.

    PABR | u32 count | count x group | string table | u32 string_table_start | u32 0

    group: u16 group_key | u16 group_key_dup | u32 item_count | item_count x u32 item_id

`checkequipitemgroup(group, min, max)` and `checkinventoryitemgroup(group,
min, max)` conditions in `quest.dbss` and `detail_dialog.dbss` name a group by
its key. The string table is empty. Layout in
docs/file-formats/bss/itemequipgroup_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start


FILE_NAME = "itemequipgroup.bss"

# u16 group_key | u16 group_key_dup | u32 item_count
_GROUP_HEAD = struct.Struct("<HHI")
_ITEM_ID_SIZE = 4


def parse_itemequipgroup_records(data: bytes) -> list[dict]:
    """Every group in file order.

    Raises ValueError on a bad magic, a group that runs past the string
    table, or groups that do not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    count = u32(data, 4)
    pos = HEADER_SIZE
    records: list[dict] = []
    for index in range(count):
        if pos + _GROUP_HEAD.size > end:
            raise ValueError(f"{FILE_NAME} group {index} at 0x{pos:X} runs past the string table")
        group_key, group_key_dup, item_count = _GROUP_HEAD.unpack_from(data, pos)
        items_start = pos + _GROUP_HEAD.size
        pos = items_start + item_count * _ITEM_ID_SIZE
        if pos > end:
            raise ValueError(f"{FILE_NAME} group {group_key} lists {item_count} items past the string table")
        records.append({
            "group_key": group_key,
            "group_key_dup": group_key_dup,
            "item_count": item_count,
            "item_ids": list(struct.unpack_from(f"<{item_count}I", data, items_start)),
        })
    check_rows_end(data, pos, f"{FILE_NAME} groups")
    return records
