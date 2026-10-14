"""Quest lists: `newquest.bss`, `mainquest.bss`, `recommendationquest.bss`
and `repetitionquest.bss` share one layout.

    PABR | u32 group_count
    | group_count x (11-byte group header | 17-byte row x row_count | 12-byte group trailer)
    | string table | u32 string_table_start | u32 0

Every text (group names, condition lines, condition scripts, event dates) is
an index into the string table. Full layout in docs/file-formats/newquest_bss.md.
"""

from __future__ import annotations

import re
import struct
from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_strings import TRAILER_SIZE, read_string_table, string_at, string_table_start
from .model import QuestListRecord


_MAGIC = b"PABR"
_HEADER_SIZE = 8

# u16 group_key | u32 name_index | u8 unknown_06 | u32 row_count
_GROUP_HEADER = struct.Struct("<HIBI")
# u16 quest_chain_id | u16 quest_id | u32 condition_index | u32 script_1_index
# | u32 script_2_index | u8 unknown_10
_ROW = struct.Struct("<HHIIIB")
# u32 event_start_index | u32 event_end_index | u32 zero
_GROUP_TRAILER = struct.Struct("<II4x")

# Event times are stored without zero padding (`2018-10-3 10:00`).
_EVENT_TIME_RE = re.compile(r"(\d{4})-(\d{1,2})-(\d{1,2}) (\d{1,2}):(\d{2})")


@dataclass(frozen=True)
class _Group:
    index: int
    key: int
    name_kr: str
    unknown_06: int
    event_start: str
    event_end: str


def _event_time(text: str) -> str:
    """`2018-10-3 10:00` as `2018-10-03 10:00`, so event times sort as text.

    Text in any other form is returned as stored.
    """
    match = _EVENT_TIME_RE.fullmatch(text.strip())
    if match is None:
        return text
    year, month, day, hour, minute = match.groups()
    return f"{year}-{int(month):02}-{int(day):02} {int(hour):02}:{minute}"


def parse_quest_list_records(data: bytes) -> list[QuestListRecord]:
    """Every quest reference of a quest list in file order, with its texts resolved.

    Raises ValueError on a bad magic, or when the groups do not end where the
    string table starts: then a group's size has changed and every later
    field is suspect.
    """
    if len(data) < _HEADER_SIZE + TRAILER_SIZE or data[:4] != _MAGIC:
        raise ValueError("Quest list has invalid magic.")

    strings = read_string_table(data)
    groups_end = string_table_start(data)
    records: list[QuestListRecord] = []
    offset = _HEADER_SIZE
    for group_index in range(u32(data, 4)):
        offset = _read_group(data, offset, groups_end, group_index, strings, records)

    if offset != groups_end:
        raise ValueError(
            f"Quest list groups end at 0x{offset:X} but its string table "
            f"starts at 0x{groups_end:X}"
        )
    return records


def _read_group(
    data: bytes,
    offset: int,
    groups_end: int,
    group_index: int,
    strings: list[str],
    records: list[QuestListRecord],
) -> int:
    """Append one group's rows to `records` and return where the next group starts."""
    if offset + _GROUP_HEADER.size > groups_end:
        raise ValueError(f"Quest list group {group_index} header runs past 0x{groups_end:X}")

    key, name_index, unknown_06, row_count = _GROUP_HEADER.unpack_from(data, offset)
    rows_at = offset + _GROUP_HEADER.size
    trailer_at = rows_at + row_count * _ROW.size
    if trailer_at + _GROUP_TRAILER.size > groups_end:
        raise ValueError(f"Quest list group {group_index} runs past 0x{groups_end:X}")

    start_index, end_index = _GROUP_TRAILER.unpack_from(data, trailer_at)
    group = _Group(
        index=group_index,
        key=key,
        name_kr=string_at(strings, name_index),
        unknown_06=unknown_06,
        event_start=_event_time(string_at(strings, start_index)),
        event_end=_event_time(string_at(strings, end_index)),
    )
    for row, row_at in enumerate(range(rows_at, trailer_at, _ROW.size)):
        records.append(_row_record(data, row_at, row, group, strings))
    return trailer_at + _GROUP_TRAILER.size


def _row_record(
    data: bytes,
    offset: int,
    row: int,
    group: _Group,
    strings: list[str],
) -> QuestListRecord:
    (
        quest_chain_id, quest_id, condition_index, script_1_index, script_2_index, unknown_10,
    ) = _ROW.unpack_from(data, offset)
    return {
        "group": group.index,
        "group_key": group.key,
        "group_name_kr": group.name_kr,
        "unknown_06": group.unknown_06,
        "event_start": group.event_start,
        "event_end": group.event_end,
        "row": row,
        "unknown_10": unknown_10,
        "quest_chain_id": quest_chain_id,
        "quest_id": quest_id,
        "packed_quest_id": (quest_id << 16) | quest_chain_id,
        "condition_index": condition_index,
        "condition_kr": string_at(strings, condition_index),
        "script_1_index": script_1_index,
        "script_1": string_at(strings, script_1_index),
        "script_2_index": script_2_index,
        "script_2": string_at(strings, script_2_index),
    }
