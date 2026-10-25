"""`fishcompetition.bss`: the fish of the fishing contest and their rewards.

    PABR | u32 count | count x 33-byte row:
        u32 fish_item_key | u8 grade | u32 rank_reward_item_keys[6] | u32 title_item_key
    u32 unknown_rows_00, unknown_rows_04, unknown_rows_08 | u32 rank_tiers[6]
    string table | u32 table_start | u32 0

`rank_tiers` holds the last rank of each reward tier, in the order of every
row's `rank_reward_item_keys`. Layout 1 in
docs/file-formats/bss/fishcompetition_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_pabr, check_rows_end


FILE_NAME = "fishcompetition.bss"
KEY_FIELD = "fish_item_key"
RANK_TIER_COUNT = 6

_ROW = struct.Struct(f"<IB{RANK_TIER_COUNT}II")
_TAIL = struct.Struct(f"<3I{RANK_TIER_COUNT}I")


@dataclass(frozen=True)
class FishCompetition:
    """The rows and the reward tiers that follow them."""

    rows: list[dict]
    rank_tiers: list[int]


def _row(values: tuple) -> dict:
    fish_item_key, grade, *rewards, title_item_key = values
    return {
        KEY_FIELD: fish_item_key,
        "grade": grade,
        "rank_reward_item_keys": rewards,
        "title_item_key": title_item_key,
    }


def parse_fishcompetition(data: bytes) -> FishCompetition:
    """Every row in file order and the rank tiers.

    Raises ValueError on a bad magic, or when the rows and the tail do not
    end where the string table starts.
    """
    check_pabr(data, FILE_NAME)
    rows_end = HEADER_SIZE + u32(data, 4) * _ROW.size
    check_rows_end(data, rows_end + _TAIL.size, f"{FILE_NAME} rows and rank tiers")
    rows = [_row(values) for values in _ROW.iter_unpack(data[HEADER_SIZE:rows_end])]
    tail = _TAIL.unpack_from(data, rows_end)
    return FishCompetition(rows, list(tail[3:]))
