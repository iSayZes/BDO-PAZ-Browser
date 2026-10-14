"""`itemmaingroup.bss`: item main groups, each a list of `itemsubgroup.dbss` subgroups.

    PABR | u32 count | count x group | string table | u32 string_table_start | u32 0

    group: u32 group_id | u8 unknown_04 | 8 zero bytes | i32 unknown_0d
           | 8 zero bytes | u32 entry_count | entry_count x 10-byte entry
    entry: u32 unknown_00 (always 0) | u32 condition_ref | u16 subgroup_key

`condition_ref` indexes the string table; string 0 is empty (no condition).
Full layout in docs/file-formats/itemmaingroup_bss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Mapping
from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_strings import (
    HEADER_SIZE,
    check_rows_end,
    checked_string_table_start,
    read_string_table,
)
from _dbss.itemsubgroup.parser import ItemSubgroup

_FILE_NAME = "itemmaingroup.bss"
# PAZ path for links from tables that store a group ID (`characterfunction.dbss`).
ITEMMAINGROUP_PATH = f"gamecommondata/binary/{_FILE_NAME}"
_GROUP_HEAD_SIZE = 29
_ENTRY_COUNT = 0x19
_ENTRY = struct.Struct("<4xIH")


@dataclass(frozen=True)
class MainGroupEntry:
    subgroup_key: int
    # The condition script that gates the subgroup; empty for none.
    condition: str


@dataclass(frozen=True)
class ItemMainGroup:
    group_id: int
    entries: tuple[MainGroupEntry, ...]

    @property
    def subgroup_keys(self) -> tuple[int, ...]:
        return tuple(entry.subgroup_key for entry in self.entries)


def group_item_keys(group: ItemMainGroup, subgroups: Mapping[int, ItemSubgroup]) -> list[int]:
    """Items of each distinct subgroup in entry order; a group may list one subgroup twice.

    Subgroups missing from `subgroups` add nothing.
    """
    keys: list[int] = []
    for subgroup_key in dict.fromkeys(group.subgroup_keys):
        subgroup = subgroups.get(subgroup_key)
        if subgroup is not None:
            keys.extend(subgroup.item_keys)
    return keys


def parse_itemmaingroup_records(data: bytes) -> list[ItemMainGroup]:
    """Every group in file order.

    Raises ValueError on a bad magic, a condition index outside the string
    table, or when the groups do not end where the string table starts.
    """
    end = checked_string_table_start(data, _FILE_NAME)
    strings = read_string_table(data)
    count = u32(data, 4)
    pos = HEADER_SIZE
    groups: list[ItemMainGroup] = []
    for _ in range(count):
        if pos + _GROUP_HEAD_SIZE > end:
            raise ValueError(f"{_FILE_NAME} group at 0x{pos:X} runs into the string table")
        group_id = u32(data, pos)
        entry_count = u32(data, pos + _ENTRY_COUNT)
        first = pos + _GROUP_HEAD_SIZE
        pos = first + entry_count * _ENTRY.size
        if pos > end:
            raise ValueError(f"{_FILE_NAME} group {group_id} holds {entry_count:,} entries, more than fit")
        groups.append(ItemMainGroup(group_id, tuple(
            _read_entry(data, offset, strings, group_id)
            for offset in range(first, pos, _ENTRY.size)
        )))
    check_rows_end(data, pos, f"{_FILE_NAME} groups")
    return groups


def _read_entry(data: bytes, offset: int, strings: list[str], group_id: int) -> MainGroupEntry:
    condition_ref, subgroup_key = _ENTRY.unpack_from(data, offset)
    if condition_ref >= len(strings):
        raise ValueError(f"{_FILE_NAME} group {group_id} points at condition {condition_ref}, past the string table")
    return MainGroupEntry(subgroup_key, strings[condition_ref])
