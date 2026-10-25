"""`itemsubgroup.dbss`: lists of items that other tables hand out as a group.

    u32 record_count | record_count x variable-length subgroup record

    subgroup record: u32 subgroup_key | 10 zero bytes | u32 entry_count
                     | entry_count x 135-byte item entry (u32 item_key first)

`itemsubgroupoffset.dbss` addresses the records. Only the item key of each
entry is decoded; the other entry fields are unconfirmed. Full layout in
docs/file-formats/dbss/itemsubgroup_dbss.md.
"""

from __future__ import annotations

from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_offset import PabrOffsetRow, parse_pabr_offset_rows


_ENTRY_COUNT = 0x0E
_ENTRIES = 0x12
_ENTRY_SIZE = 135


@dataclass(frozen=True)
class ItemSubgroup:
    subgroup_key: int
    # Packed `enchant_level << 24 | item_id` keys, see `_common/item_key.py`.
    item_keys: tuple[int, ...]


def parse_itemsubgroup_records(data: bytes, offset_data: bytes) -> list[ItemSubgroup]:
    """Every subgroup in offset table order.

    Raises ValueError when a record does not match its offset row.
    """
    return [read_subgroup(data, row) for row in parse_pabr_offset_rows(offset_data)]


def subgroups_by_key(data: bytes, offset_data: bytes, keys: set[int]) -> dict[int, ItemSubgroup]:
    """The subgroups among `keys` that the offset table holds, read on their own.

    Keys the table lacks are left out.
    """
    return {
        row.entry_id: read_subgroup(data, row)
        for row in parse_pabr_offset_rows(offset_data)
        if row.entry_id in keys
    }


def read_subgroup(data: bytes, row: PabrOffsetRow) -> ItemSubgroup:
    """The subgroup record an offset row points at.

    Raises ValueError when the record runs past the file, repeats a different
    key, or its entry count does not fill the size the row gives.
    """
    start, end = row.offset, row.offset + row.size
    if row.size < _ENTRIES or end > len(data):
        raise ValueError(f"itemsubgroup record {row.entry_id} at 0x{start:X} is outside the file")

    subgroup_key = u32(data, start)
    if subgroup_key != row.entry_id:
        raise ValueError(
            f"itemsubgroup record at 0x{start:X} has key {subgroup_key}, "
            f"its offset row says {row.entry_id}"
        )

    entry_count = u32(data, start + _ENTRY_COUNT)
    if _ENTRIES + entry_count * _ENTRY_SIZE != row.size:
        raise ValueError(
            f"itemsubgroup record {subgroup_key} holds {entry_count:,} entries "
            f"but is {row.size:,} bytes"
        )

    first = start + _ENTRIES
    item_keys = tuple(u32(data, pos) for pos in range(first, end, _ENTRY_SIZE))
    return ItemSubgroup(subgroup_key, item_keys)
