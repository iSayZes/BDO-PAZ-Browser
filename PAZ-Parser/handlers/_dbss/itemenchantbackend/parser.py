"""itemenchantbackend.dbss: the itemenchant.dbss blocks from Message Tail `+0x2B` to their end.

`itemenchantbackendoffset.dbss` has the layout of itemenchantoffset.dbss and
the same keys; each block here is the end of the itemenchant.dbss block of
that key, the part itemenchantbackendtest.dbss leaves out. `layout.py` walks
a block to its last byte (itemenchantbackend_dbss.md).
"""

from __future__ import annotations

from dataclasses import asdict

from _dbss.itemenchant.parser import base_rows, max_enchant_levels, parse_itemenchantoffset_records
from .layout import read_block

FILE_NAME = "itemenchantbackend.dbss"
OFFSET_FILE = "itemenchantbackendoffset.dbss"

# The packed key sits this many bytes before the block end, the crystal group after it.
KEY_FROM_END = 0x06
_NO_CRYSTAL_GROUP = 0xFFFF
# Off the record: the key repeats `item_id`, the LOC description is in the
# user's language, and the two item lists are not single values.
_LEFT_OUT = ("key", "description_kr", "jewel_need_items", "popup_result_items")


def _block_fields(data: bytes, row: dict) -> dict:
    """The named fields of the row's block; raises ValueError when it does not fit or holds another key."""
    start = row["data_offset"]
    end = start + row["data_size"]
    if end > len(data):
        raise ValueError(
            f"{FILE_NAME} block for key {row['key']} at {start:,} ({row['data_size']:,} bytes) "
            f"does not fit the {len(data):,}-byte file"
        )
    try:
        block = read_block(data, start, end)
    except ValueError as error:
        raise ValueError(f"{FILE_NAME} block for key {row['key']}: {error}") from error
    if block.key != row["key"]:
        raise ValueError(f"{FILE_NAME} block for key {row['key']} ends with key {block.key}")
    fields = {name: value for name, value in asdict(block).items() if name not in _LEFT_OUT}
    # None sorts last and exports empty.
    if fields["crystal_group"] == _NO_CRYSTAL_GROUP:
        fields["crystal_group"] = None
    return fields


def parse_itemenchantbackend_records(data: bytes, offset_data: bytes) -> list[dict]:
    """One record per item from its level-0 block, with its highest level.

    Raises ValueError when a block does not fit the file, does not walk to
    its last byte or does not end with the key of its index row.
    """
    offset_rows = parse_itemenchantoffset_records(offset_data)
    max_levels = max_enchant_levels(offset_rows)
    return [
        {
            "item_id": row["item_id"],
            "max_enchant_level": max_levels[row["item_id"]],
            **_block_fields(data, row),
            "block_size": row["data_size"],
        }
        for row in base_rows(offset_rows)
    ]
