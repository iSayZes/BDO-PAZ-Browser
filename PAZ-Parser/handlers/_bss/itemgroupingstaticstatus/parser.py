"""`itemgroupingstaticstatus.bss`: the items of each item group type.

    u32 group_count | group_count x Group
    Group: u8 item_group_type | u32 item_count | u32[item_count] item_ids

No PABR magic and no string table. The group types are the ones
`ToClient_getItemKeyGroupTypeByTItemKey` returns; `itemeffectgroupstaticstatus.bss`
keys its glow effects by them. Layout 1 in
docs/file-formats/itemgroupingstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records, read_counted_u32s
from _common.record_reader import RecordReader


FILE_NAME = "itemgroupingstaticstatus.bss"
KEY_FIELD = "item_group_type"

_TYPE = struct.Struct("<B")


def _read_group(reader: RecordReader) -> dict:
    (item_group_type,) = reader.unpack(_TYPE)
    item_ids = read_counted_u32s(reader, f"{FILE_NAME} group {item_group_type}")
    return {KEY_FIELD: item_group_type, "item_ids": item_ids}


def parse_itemgrouping_groups(data: bytes) -> list[dict]:
    """Every group in file order.

    Raises ValueError when a group runs past the file or the groups end before it.
    """
    return read_counted_records(data, _read_group, FILE_NAME)
