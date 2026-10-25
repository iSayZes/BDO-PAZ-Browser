"""Members of a `characterstatic.dbss` `character_group`, by name.

The quest condition `killMonsterGroup(group, count)` and the soul collector
items (`itemenchant.dbss` `contents_event_param1`) name a group by this key.
No client file names the groups, so a group shows as its key and the names
of its members. The members come from the `CHARACTER_GROUP_MEMBERS` lookup
index, so no table needs `characterstatic.dbss` as a companion. See
"Character Group" in docs/file-formats/dbss/characterstatic_dbss.md.
"""

from __future__ import annotations

from _common.character import character_name
from _common.html import e, text_list_cell
from _common.lookup_index import IndexKind, lookup


def character_group_members(group: int) -> tuple[int, ...]:
    """Character IDs in the group, ascending; empty when the index is not loaded or lacks the group."""
    members = lookup(IndexKind.CHARACTER_GROUP_MEMBERS, group)
    return members if isinstance(members, tuple) else ()


def character_group_names(group: int) -> list[str]:
    """Distinct member names in character ID order, a member's ID where it has no name.

    Copies of one monster share a name, so the 199 rows of the Infinity Tower
    group reduce to far fewer names.
    """
    names = (character_name(character_id) or str(character_id) for character_id in character_group_members(group))
    return list(dict.fromkeys(names))


def character_group_text(group: int, label: str = "") -> str:
    """`70: Khala Commanding Officer, Khala Elite Combatant`, every member named, for search and export.

    `label` replaces the bare key before the colon (`70 (x10)`); without
    members the text is the label alone.
    """
    head = label or str(group)
    names = character_group_names(group)
    return f"{head}: {', '.join(names)}" if names else head


def character_group_cell(group: int, max_items: int, label: str = "") -> str:
    """`character_group_text()` as HTML: the first `max_items` names and a hoverable count of the rest."""
    head = e(label or str(group))
    names = character_group_names(group)
    return f"{head}: {text_list_cell(names, max_items)}" if names else head
