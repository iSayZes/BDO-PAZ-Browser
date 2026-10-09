"""`lightstoneset.bss`: the Lightstone sets of the Artifact slots.

    PABR | u32 count | count x set row | u32 substitute count
    | substitute count x (u32 item_id, u32 member_id) | string table
    | u32 string_table_start | u32 0

    set row: u32 set_id | u16 skill_no | u32 member_count
             | member_count x u32 member item ID | u32 text_ref

The substitute table says which Lightstone item counts as which set member:
each member to itself, and each Amplified Lightstone to its base Lightstone.
Full layout in docs/file-formats/lightstoneset_bss.md.
"""

from __future__ import annotations

import struct
from collections import defaultdict
from typing import NamedTuple

from _common.binary import u32
from _common.inline_text import decode_inline_text
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "lightstoneset.bss"
# The set count follows the PABR magic.
_COUNT_OFFSET = 4

_U32 = struct.Struct("<I")
_SET_HEAD = struct.Struct("<IHI")
_SUBSTITUTE = struct.Struct("<II")


class LightstoneSets(NamedTuple):
    """The set rows in file order and the substitute table as item ID -> member ID."""

    sets: list[dict]
    substitutes: dict[int, int]


def _read_set(reader: RecordReader, strings: list[str]) -> dict:
    set_id, skill_no, member_count = reader.unpack(_SET_HEAD)
    member_ids = list(reader.unpack(struct.Struct(f"<{member_count}I")))
    (text_ref,) = reader.unpack(_U32)
    return {
        "set_id": set_id,
        "skill_no": skill_no,
        "member_ids": member_ids,
        "text_kr": decode_inline_text(string_at(strings, text_ref)),
    }


def _read_substitutes(reader: RecordReader) -> dict[int, int]:
    (count,) = reader.unpack(_U32)
    return dict(reader.unpack(_SUBSTITUTE) for _ in range(count))


def parse_lightstone_sets(data: bytes) -> LightstoneSets:
    """Every set row in file order and the substitute table.

    Raises ValueError on a bad magic, when a row runs into the string table,
    or when the substitute table does not end where the string table starts:
    then the layout has changed and every field is suspect.
    """
    rows_end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE, rows_end, f"{FILE_NAME} rows")
    sets = [_read_set(reader, strings) for _ in range(u32(data, _COUNT_OFFSET))]
    substitutes = _read_substitutes(reader)
    if not reader.at_end():
        raise ValueError(
            f"{FILE_NAME} substitute table ends {reader.remaining()} bytes before the string table"
        )
    return LightstoneSets(sets, substitutes)


def substitute_ids(member_ids: list[int], substitutes: dict[int, int]) -> list[int]:
    """Items that count as one of `member_ids`, other than the member itself, in table order."""
    members = set(member_ids)
    return [
        item_id
        for item_id, member_id in substitutes.items()
        if member_id in members and item_id != member_id
    ]


def build_lightstone_set_index(data: bytes) -> dict[int, tuple[int, ...]]:
    """The `LIGHTSTONE_SETS` index: each Lightstone item to the sets it counts
    toward, by ascending set ID.

    A member counts toward every set that lists it, a substitute toward the
    sets of the member it stands in for.
    """
    parsed = parse_lightstone_sets(data)
    sets_by_member: defaultdict[int, set[int]] = defaultdict(set)
    for record in parsed.sets:
        for member_id in record["member_ids"]:
            sets_by_member[member_id].add(record["set_id"])
    counted_as = {**{member_id: member_id for member_id in sets_by_member}, **parsed.substitutes}
    return {
        item_id: tuple(sorted(sets_by_member[member_id]))
        for item_id, member_id in counted_as.items()
        if member_id in sets_by_member
    }
