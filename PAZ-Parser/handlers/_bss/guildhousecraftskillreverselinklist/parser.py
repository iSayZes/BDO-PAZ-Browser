"""`guildhousecraftskillreverselinklist.bss`: the house uses that grant each guild skill.

    PABR | u32 count | count x skill | string table | u32 string_table_start | u32 0

    skill: u16 skill_no | u32 link_count | link_count x (i32 receipe_key | u32 slot)

The reverse of `guildhousecraftskill.dbss`: `slot` is `1` for that row's
`skill_nos[0]`. The string table is empty. Layout in
docs/file-formats/bss/guildhousecraftskillreverselinklist_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start


FILE_NAME = "guildhousecraftskillreverselinklist.bss"

# u16 skill_no | u32 link_count, unpadded
_SKILL_HEAD = struct.Struct("<HI")
# i32 receipe_key | u32 slot
_LINK = struct.Struct("<iI")


def _parse_links(data: bytes, start: int, link_count: int) -> list[dict]:
    return [
        {"receipe_key": receipe_key, "slot": slot}
        for receipe_key, slot in _LINK.iter_unpack(data[start : start + link_count * _LINK.size])
    ]


def parse_reverse_link_records(data: bytes) -> list[dict]:
    """Every skill in file order.

    Raises ValueError on a bad magic, a skill that runs past the string
    table, or skills that do not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    count = u32(data, 4)
    pos = HEADER_SIZE
    records: list[dict] = []
    for index in range(count):
        if pos + _SKILL_HEAD.size > end:
            raise ValueError(f"{FILE_NAME} skill {index} at 0x{pos:X} runs past the string table")
        skill_no, link_count = _SKILL_HEAD.unpack_from(data, pos)
        links_start = pos + _SKILL_HEAD.size
        pos = links_start + link_count * _LINK.size
        if pos > end:
            raise ValueError(f"{FILE_NAME} skill {skill_no} lists {link_count} links past the string table")
        records.append({
            "skill_no": skill_no,
            "link_count": link_count,
            "links": _parse_links(data, links_start, link_count),
        })
    check_rows_end(data, pos, f"{FILE_NAME} skills")
    return records
