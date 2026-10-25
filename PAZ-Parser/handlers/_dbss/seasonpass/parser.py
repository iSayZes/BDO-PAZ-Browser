"""`seasonpass.dbss`: the rows of the Black Spirit Pass (season pass) window.

    u32 count | count x row | u16 unknown_rows_00
    | u32 season_range_count | season_range_count x season range
    row: u32 pass_no | u32 base_reward_quest | u32 premium_reward_quest
         | u8 season_type | str16 changed_title_kr | str16 changed_desc_kr
         | u32 condition_quest | u32 unknown_changed_desc_kr_04
    season range: u16 unknown_00 | u16 first_quest_chain | u16 last_quest_chain

The quests are packed quest IDs (low u16 chain, high u16 quest). Clients up
to 2107 end the file after the rows (Layout 1). Layout 2 in
docs/file-formats/dbss/seasonpass_dbss.md.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _common.binary import u32
from _common.counted_rows import read_counted_structs
from _common.record_reader import RecordReader


FILE_NAME = "seasonpass.dbss"
KEY_FIELD = "pass_no"

_COUNT = struct.Struct("<I")
_HEAD = struct.Struct("<IIIB")
_TAIL = struct.Struct("<II")
_RANGE_HEAD = struct.Struct("<H")
_RANGE = struct.Struct("<HHH")
_RANGE_FIELDS = ("unknown_00", "first_quest_chain", "last_quest_chain")


class SeasonPassFile(NamedTuple):
    rows: list[dict]
    # Layout 2 only; None for a Layout 1 file that ends after the rows.
    unknown_rows_00: int | None
    season_ranges: list[dict]


def _read_row(reader: RecordReader) -> dict:
    pass_no, base_quest, premium_quest, season_type = reader.unpack(_HEAD)
    changed_title_kr = reader.text(wide=True)
    changed_desc_kr = reader.text(wide=True)
    condition_quest, unknown_04 = reader.unpack(_TAIL)
    return {
        KEY_FIELD: pass_no,
        "base_reward_quest": base_quest,
        "premium_reward_quest": premium_quest,
        "season_type": season_type,
        "changed_title_kr": changed_title_kr,
        "changed_desc_kr": changed_desc_kr,
        "condition_quest": condition_quest,
        "unknown_changed_desc_kr_04": unknown_04,
    }


def _read_ranges(reader: RecordReader) -> tuple[int, list[dict]]:
    (unknown_rows_00,) = reader.unpack(_RANGE_HEAD)
    return unknown_rows_00, read_counted_structs(reader, _RANGE, _RANGE_FIELDS, f"{FILE_NAME} season range")


def parse_seasonpass_file(data: bytes) -> SeasonPassFile:
    """The rows in file order and the season ranges after them.

    Raises ValueError when a row runs past the file or bytes are left over.
    """
    if len(data) < _COUNT.size:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")
    reader = RecordReader(data, _COUNT.size, len(data), FILE_NAME)
    rows = [_read_row(reader) for _ in range(u32(data, 0))]
    if reader.at_end():
        return SeasonPassFile(rows, None, [])
    unknown_rows_00, ranges = _read_ranges(reader)
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} season ranges end at 0x{reader.pos:X}, the file at 0x{len(data):X}")
    return SeasonPassFile(rows, unknown_rows_00, ranges)
