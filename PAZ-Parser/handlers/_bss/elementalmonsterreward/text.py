"""Rank tier labels as the detailed reward window builds them (LOC type 37).

`panel_window_morningland_detailreward_all.luac` writes a tier as
`LUA_MORNING_ATTRBOSS_RANK` ("#{rank}"); a tier whose rank is above 1 gets
the previous tier's rank + 1 in front, "~ " between, so the second tier of
1, 5, 20 reads "#2 ~ #5" and a lone tier of 50 "~ #50". The base rewards row
reads `LUA_MORNING_ATTRBOSS_OUTOFRANKREWARD`.
"""

from __future__ import annotations

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text
from _common.string_hash import key_hash


_RANK_KEY = "LUA_MORNING_ATTRBOSS_RANK"
_BASE_REWARD_KEY = "LUA_MORNING_ATTRBOSS_OUTOFRANKREWARD"
_RANK_PLACEHOLDER = "{rank}"
_RANGE_JOIN = "~ "


def _rank_text(rank_format: str, rank: int) -> str:
    return rank_format.replace(_RANK_PLACEHOLDER, str(rank))


def rank_label(rank: int, previous_rank: int | None, fallback_format: str) -> str:
    """`#1`, `#2 ~ #5`, `~ #50`; `fallback_format` ("#{rank}") stands in when LOC has no text."""
    rank_format = ui_hash_text(GAME_SHEET, key_hash(_RANK_KEY)) or fallback_format
    label = _rank_text(rank_format, rank)
    if rank <= 1:
        return label
    first = f"{_rank_text(rank_format, previous_rank + 1)} " if previous_rank is not None else ""
    return f"{first}{_RANGE_JOIN}{label}"


def base_reward_label() -> str:
    """`Bonus Rewards`, or '' when LOC has no text."""
    return ui_hash_text(GAME_SHEET, key_hash(_BASE_REWARD_KEY))
