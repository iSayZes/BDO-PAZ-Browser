"""The `killMonsterGroup(group, count)` calls of a quest script, with the group's members by name.

`quest.dbss` completion scripts and `guildquest.dbss` complete conditions
call it; `group` is a `characterstatic.dbss` `character_group` key (see
`_common/character_group.py`) and `count` the kills it needs. Scripts spell
the name in any case and some put a space after the comma.
"""

from __future__ import annotations

import re
from typing import NamedTuple

from _common.character_group import character_group_cell, character_group_text

_KILL_MONSTER_GROUP = re.compile(r"killmonstergroup\(\s*(\d+)\s*,\s*(\d+)\s*\)", re.IGNORECASE)
# One call per line in a cell.
_CALL_SEPARATOR = "<br>"


class KillMonsterGroup(NamedTuple):
    group: int
    kills: int


def kill_monster_groups(*scripts: str) -> list[KillMonsterGroup]:
    """Every distinct `killMonsterGroup` call of the scripts, in script order."""
    calls = (
        KillMonsterGroup(int(group), int(count))
        for script in scripts
        for group, count in _KILL_MONSTER_GROUP.findall(script)
    )
    return list(dict.fromkeys(calls))


def _label(call: KillMonsterGroup) -> str:
    return f"{call.group} (x{call.kills:,})"


def kill_monster_group_texts(calls: list[KillMonsterGroup]) -> list[str]:
    """`70 (x10): Khala Commanding Officer, ...` per call, every member named, for search and export."""
    return [character_group_text(call.group, _label(call)) for call in calls]


def kill_monster_groups_cell(calls: list[KillMonsterGroup], max_items: int) -> str:
    """One line per call with its first `max_items` member names, or '' without calls."""
    return _CALL_SEPARATOR.join(character_group_cell(call.group, max_items, _label(call)) for call in calls)
