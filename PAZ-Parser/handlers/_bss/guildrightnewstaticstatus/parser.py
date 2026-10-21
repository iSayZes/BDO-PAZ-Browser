"""`guildrightnewstaticstatus.bss`: the guild rights of the guild authority window, by group.

    PABR | u32 group_count | group_count x Group | string table
    | u32 table_start | u32 0
    Group: u8 group_no | u8 unknown_01 | u32 group_name_ref
           | u32 right_count | right_count x Right
    Right: u32 right_no | u32 name_ref | u32 description_ref

Every `*_ref` is an index into the PABR string table. One record per right,
with its group's fields. Full layout in
docs/file-formats/guildrightnewstaticstatus_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import (
    HEADER_SIZE,
    check_rows_end,
    checked_string_table_start,
    read_string_table,
    string_at,
)
from _common.record_reader import RecordReader


FILE_NAME = "guildrightnewstaticstatus.bss"

_COUNT = struct.Struct("<I")
_GROUP_HEAD = struct.Struct("<BBII")
_RIGHT = struct.Struct("<III")


def _read_group(reader: RecordReader, strings: list[str]) -> list[dict]:
    """The rights of one group, each with the group's fields."""
    group_no, unknown_01, group_name_ref, right_count = reader.unpack(_GROUP_HEAD)
    if right_count * _RIGHT.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} group {group_no} right count {right_count:,} runs past the string table")
    group = {
        "group_no": group_no,
        "unknown_01": unknown_01,
        "group_name_ref": group_name_ref,
        "group_name_kr": string_at(strings, group_name_ref),
    }
    records: list[dict] = []
    for _ in range(right_count):
        right_no, name_ref, description_ref = reader.unpack(_RIGHT)
        records.append(
            {
                "right_no": right_no,
                **group,
                "name_ref": name_ref,
                "name_kr": string_at(strings, name_ref),
                "description_ref": description_ref,
                "description_kr": string_at(strings, description_ref),
            }
        )
    return records


def parse_guild_right_records(data: bytes) -> list[dict]:
    """One record per right, in file order (group by group).

    Raises ValueError on a bad magic or trailer, or when the groups do not
    end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE - _COUNT.size, end, FILE_NAME)
    (group_count,) = reader.unpack(_COUNT)
    records: list[dict] = []
    for _ in range(group_count):
        records += _read_group(reader, strings)
    check_rows_end(data, reader.pos, f"{FILE_NAME} groups")
    return records
