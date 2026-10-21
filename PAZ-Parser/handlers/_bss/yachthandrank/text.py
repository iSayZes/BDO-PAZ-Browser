"""Yar! hand rank names and descriptions, for the tables that list hand ranks by key.

LOC type 105 holds each hand rank's name (`str_id4` 0) and description
(`str_id4` 1) under its `yachthandrank.bss` key. The Korean text of the
table itself is the fallback where LOC has none.
"""

from __future__ import annotations

from _common.loc import loc_text
from .parser import parse_yachthandrank_records


LOC_HAND_RANK = 105
_NAME = 0
_DESC = 1
# Hand rank names a list cell shows before its `... (+N)`: every hand rank
# of `yachthandrank.bss` (15 on client 3474), so no row is cut.
HAND_RANKS_SHOWN = 15


def hand_rank_name(key: int, name_kr: str = "") -> str:
    """The hand rank's name in the loaded LOC, else `name_kr`."""
    return loc_text(LOC_HAND_RANK, key, _NAME) or name_kr


def hand_rank_desc(key: int, desc_kr: str = "") -> str:
    """The hand rank's description in the loaded LOC, else `desc_kr`."""
    return loc_text(LOC_HAND_RANK, key, _DESC) or desc_kr


def korean_hand_rank_names(data: bytes | None) -> dict[int, str]:
    """The Korean name of every hand rank by key; empty when the file is missing.

    Raises ValueError when the file does not parse.
    """
    if data is None:
        return {}
    return {record["hand_rank_key"]: record["name_kr"] for record in parse_yachthandrank_records(data)}


def hand_rank_names(keys: list[int], korean_names: dict[int, str]) -> list[str]:
    """The name of each hand rank in list order; the bare key where neither LOC nor the table has one."""
    return [hand_rank_name(key, korean_names.get(key, "")) or str(key) for key in keys]
