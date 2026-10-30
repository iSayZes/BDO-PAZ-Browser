"""itemenchantbackendtest.dbss: the itemenchant.dbss blocks up to Message Tail `+0x2B`.

The file has no offset index: a u32 count, then the blocks back to back in
the order of itemenchantoffset.dbss. Each block ends where
`_dbss.itemenchant.layout_2.front_end` finds the end of its Message Tail part,
so the walk reads every block's lists and strings
(itemenchantbackendtest_dbss.md).
"""

from __future__ import annotations

from _common.binary import u32
from _common.pabr_offset import PabrOffsetRow
from _dbss.itemenchant.layout_2 import front_end
from _dbss.itemenchant.parser import base_records, offset_record

FILE_NAME = "itemenchantbackendtest.dbss"

_COUNT_SIZE = 4
_KEY_SIZE = 4


def front_block_rows(data: bytes) -> list[dict]:
    """Every block's key, item ID, enchant level, offset and size, in file order.

    The rows have the shape of `parse_itemenchantoffset_records`. Raises
    ValueError when a block runs past the file or the blocks do not end at
    its last byte.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its block count")

    rows: list[dict] = []
    pos = _COUNT_SIZE
    for index in range(u32(data, 0)):
        if pos + _KEY_SIZE > len(data):
            raise ValueError(f"{FILE_NAME}: block {index:,} starts at {pos:,}, past the end of the file")
        try:
            end = front_end(data, pos, len(data))
        except ValueError as error:
            raise ValueError(f"{FILE_NAME} block {index:,}: {error}") from error
        rows.append(offset_record(PabrOffsetRow(u32(data, pos), pos, end - pos)))
        pos = end

    if pos != len(data):
        raise ValueError(f"{FILE_NAME}: the blocks end at {pos:,} but the file is {len(data):,} bytes")
    return rows


def parse_itemenchantbackendtest_records(data: bytes) -> list[dict]:
    """One record per item from its level-0 block, with its highest level.

    The fields are those `parse_itemenchant_records` reads up to
    `life_restrict_type`; the crystal group and `second_string` sit in the
    part of the block this file does not store.
    """
    return [
        {**fields, "block_size": row["data_size"]}
        for row, fields, _ in base_records(data, front_block_rows(data), FILE_NAME)
    ]
