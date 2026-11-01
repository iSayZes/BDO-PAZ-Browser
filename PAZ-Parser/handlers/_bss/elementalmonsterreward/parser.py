"""`elementalmonsterreward.bss`: the ranking rewards of the Black Shrine bosses.

    u32 count | count x record | u32 part2_count | part2_count x record
    record: u16 character_key | u32 rank_tier_count | rank_tier_count x tier
            | u64 base_reward_count | base_reward_count x reward item
    tier: u32 rank | u64 reward_count | reward_count x reward item
    reward item: u32 item_key | 4 bytes padding | i64 count

No PABR magic. The second table is the one the window reads with its Part 2
(Hwanghae party) flag on. Full layout in
docs/file-formats/bss/elementalmonsterreward_bss.md.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _bss.elementalmonsterstat.parser import read_reward_items
from _common.record_reader import RecordReader


FILE_NAME = "elementalmonsterreward.bss"

_COUNT = struct.Struct("<I")
_RECORD_HEAD = struct.Struct("<HI")
_TIER_HEAD = struct.Struct("<IQ")
_ITEM_COUNT = struct.Struct("<Q")


class RewardTables(NamedTuple):
    records: list[dict]
    part2_records: list[dict]


def _read_tier(reader: RecordReader) -> dict:
    rank, reward_count = reader.unpack(_TIER_HEAD)
    return {
        "rank": rank,
        "reward_count": reward_count,
        "rewards": read_reward_items(reader, reward_count),
    }


def _read_record(reader: RecordReader) -> dict:
    character_key, rank_tier_count = reader.unpack(_RECORD_HEAD)
    rank_tiers = [_read_tier(reader) for _ in range(rank_tier_count)]
    (base_reward_count,) = reader.unpack(_ITEM_COUNT)
    return {
        "character_key": character_key,
        "rank_tier_count": rank_tier_count,
        "rank_tiers": rank_tiers,
        "base_reward_count": base_reward_count,
        "base_rewards": read_reward_items(reader, base_reward_count),
    }


def _read_table(reader: RecordReader) -> list[dict]:
    (count,) = reader.unpack(_COUNT)
    return [_read_record(reader) for _ in range(count)]


def parse_elementalmonsterreward(data: bytes) -> RewardTables:
    """Both tables in file order.

    Raises ValueError when a record runs past the file or the second table
    does not end at the end of the file.
    """
    reader = RecordReader(data, 0, len(data), FILE_NAME)
    tables = RewardTables(_read_table(reader), _read_table(reader))
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME}: {reader.remaining():,} bytes left after the second table")
    return tables
