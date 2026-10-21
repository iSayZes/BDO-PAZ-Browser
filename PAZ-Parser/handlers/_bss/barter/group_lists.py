"""The two counted lists of groups that `bartersubgroup.bss` and `barter_normal.bss` hold.

    PABR | u32 group_count | group_count x group
    | u32 material_group_count | material_group_count x group
    | u32 0 (empty string table) | u32 string_table_start | u32 0
    group: head (ending in a u32 entry_count) | entry_count x fixed-size entry

The first list is the trade item barters, the second the material barters.
`bartersubgroup.bss` groups have a bare entry count as their head,
`barter_normal.bss` groups a u16 region key before it. Layouts in
docs/file-formats/bartersubgroup_bss.md and barter_normal_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_strings import U32_SIZE, check_rows_end, checked_string_table_start

# The first list's group count, after the PABR magic.
GROUP_COUNT_OFFSET = 4
# False for the trade item list, True for the material list, in file order.
_LISTS = (False, True)


@dataclass(frozen=True)
class GroupSpan:
    """One group: its list, its head values before the entry count, and where each entry starts."""

    is_material: bool
    head: tuple[int, ...]
    entries: range


def _read_count(data: bytes, pos: int, end: int, file_name: str) -> int:
    if pos + U32_SIZE > end:
        raise ValueError(f"{file_name}: the count at 0x{pos:X} runs past the string table")
    return u32(data, pos)


def group_spans(data: bytes, file_name: str, head: struct.Struct, entry_size: int) -> list[GroupSpan]:
    """Every group of both lists in file order.

    `head` reads a group's head and ends in its u32 entry count. Raises
    ValueError on a missing magic, a group that runs past the string table,
    or a material list that does not end where the string table starts.
    """
    end = checked_string_table_start(data, file_name)
    pos = GROUP_COUNT_OFFSET
    spans: list[GroupSpan] = []
    for is_material in _LISTS:
        group_count = _read_count(data, pos, end, file_name)
        pos += U32_SIZE
        for _ in range(group_count):
            if pos + head.size > end:
                raise ValueError(f"{file_name}: the group at 0x{pos:X} runs past the string table")
            *values, entry_count = head.unpack_from(data, pos)
            entries_start = pos + head.size
            group_end = entries_start + entry_count * entry_size
            if group_end > end:
                raise ValueError(f"{file_name}: the group at 0x{pos:X} runs past the string table")
            spans.append(GroupSpan(is_material, tuple(values), range(entries_start, group_end, entry_size)))
            pos = group_end
    check_rows_end(data, pos, f"{file_name} groups")
    return spans
