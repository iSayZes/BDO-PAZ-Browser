"""`moonblessingss.dbss`: the Moon's Blessing Pearl spending events.

    u32 count | count x row
    row: u16 key | u64 start_time | u64 end_time | u64 max_used_pearl
         | u16 unknown_1a | str16 description_kr | u8 unknown_description_kr_00
         | u32 level_count | level_count x level
    level: str16 title_kr | u32 reward_count | reward_count x reward entry
           | u16 level_no | u64 target_used_pearl

A reward entry is the 178-byte quest reward entry of `quest.dbss`
(`_common/quest/reward_entry.py`). Layout 1 in
docs/file-formats/dbss/moonblessingss_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.quest.reward_entry import REWARD_ENTRY_SIZE, read_reward_entry
from _common.record_reader import RecordReader


FILE_NAME = "moonblessingss.dbss"
KEY_FIELD = "key"

_HEAD = struct.Struct("<HQQQH")
_HEAD_FIELDS = (KEY_FIELD, "start_time", "end_time", "max_used_pearl", "unknown_1a")
_AFTER_DESCRIPTION = struct.Struct("<BI")
_COUNT = struct.Struct("<I")
_LEVEL_TAIL = struct.Struct("<HQ")


def _read_level(reader: RecordReader) -> dict:
    title_kr = reader.text(wide=True)
    (reward_count,) = reader.unpack(_COUNT)
    if reward_count * REWARD_ENTRY_SIZE > reader.remaining():
        raise ValueError(f"{FILE_NAME} reward count {reward_count:,} runs past the file")
    base_rewards = [read_reward_entry(reader) for _ in range(reward_count)]
    level_no, target_used_pearl = reader.unpack(_LEVEL_TAIL)
    return {
        "title_kr": title_kr,
        "base_rewards": base_rewards,
        "level_no": level_no,
        "target_used_pearl": target_used_pearl,
    }


def _read_row(reader: RecordReader) -> dict:
    head = dict(zip(_HEAD_FIELDS, reader.unpack(_HEAD), strict=True))
    description_kr = reader.text(wide=True)
    unknown_description_kr_00, level_count = reader.unpack(_AFTER_DESCRIPTION)
    return {
        **head,
        "description_kr": description_kr,
        "unknown_description_kr_00": unknown_description_kr_00,
        "levels": [_read_level(reader) for _ in range(level_count)],
    }


def parse_moonblessingss_rows(data: bytes) -> list[dict]:
    """Every row in file order with its levels.

    Raises ValueError when a row runs past the file or the rows end early.
    """
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_moonblessingss_records(data: bytes) -> list[dict]:
    """One record per level, in file order, with its row's fields.

    A row without levels has no record. Raises ValueError like
    `parse_moonblessingss_rows`.
    """
    records: list[dict] = []
    for row in parse_moonblessingss_rows(data):
        head = {field: value for field, value in row.items() if field != "levels"}
        records += [{**head, **level} for level in row["levels"]]
    return records
