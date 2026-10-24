"""itemenchantbackend.dbss: the itemenchant.dbss blocks from Message Tail `+0x2B` to their end.

`itemenchantbackendoffset.dbss` has the layout of itemenchantoffset.dbss and
the same keys; each block here is the end of the itemenchant.dbss block of
that key, the part itemenchantbackendtest.dbss leaves out
(itemenchantbackend_dbss.md).
"""

from __future__ import annotations

from _common.binary import u8, u32
from _dbss.itemenchant.parser import (
    base_rows,
    crystal_group_before,
    max_enchant_levels,
    parse_itemenchantoffset_records,
)

FILE_NAME = "itemenchantbackend.dbss"
OFFSET_FILE = "itemenchantbackendoffset.dbss"

# Message Tail +0x5A in itemenchant.dbss; 2016 `_itemAccessLevel`.
_ITEM_ACCESS_LEVEL = 0x2F
# The packed key sits this many bytes before the block end, the crystal group after it.
KEY_FROM_END = 0x06
# `unknown_00`, `item_access_level`, `key` and `crystal_group`.
_MIN_BLOCK_SIZE = 0x30 + KEY_FROM_END


def _check_block(data: bytes, row: dict) -> int:
    """The end of the row's block; raises ValueError when it does not fit or holds another key."""
    start = row["data_offset"]
    end = start + row["data_size"]
    if end > len(data) or row["data_size"] < _MIN_BLOCK_SIZE:
        raise ValueError(
            f"{FILE_NAME} block for key {row['key']} at {start:,} ({row['data_size']:,} bytes) "
            f"does not fit the {len(data):,}-byte file"
        )
    key = u32(data, end - KEY_FROM_END)
    if key != row["key"]:
        raise ValueError(f"{FILE_NAME} block for key {row['key']} ends with key {key}")
    return end


def parse_itemenchantbackend_records(data: bytes, offset_data: bytes) -> list[dict]:
    """One record per item from its level-0 block, with its highest level.

    Raises ValueError when a block does not fit the file or does not end with
    the key of its index row.
    """
    offset_rows = parse_itemenchantoffset_records(offset_data)
    max_levels = max_enchant_levels(offset_rows)
    records: list[dict] = []
    for row in base_rows(offset_rows):
        end = _check_block(data, row)
        records.append({
            "item_id": row["item_id"],
            "max_enchant_level": max_levels[row["item_id"]],
            "item_access_level": u8(data, row["data_offset"] + _ITEM_ACCESS_LEVEL),
            # None sorts last and exports empty.
            "crystal_group": crystal_group_before(data, end),
            "block_size": row["data_size"],
        })
    return records
