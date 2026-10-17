"""Crystal group names in the user's language.

LOC type 121 keys a group's name by `(group, max_count)` in `str_id1` and
`str_id2` (jewelgroupstaticstatus_bss.md, Notes).
"""

from __future__ import annotations

from typing import NamedTuple

from _common.loc import loc_lookup, strip_pa_tags
from .parser import parse_jewel_group_records


_LOC_CRYSTAL_GROUP = 121

# The limit the item tooltip shows as "No Limit" (`LUA_TOOLTIP_CRYSTALGROUP_NOLIMIT`
# in panel_tooltip_item.luac).
NO_LIMIT = 1000


class JewelGroup(NamedTuple):
    name: str
    max_count: int


def jewel_group_name(group: int, max_count: int, name_kr: str) -> str:
    """The group's LOC name, else its Korean name."""
    return strip_pa_tags(loc_lookup(_LOC_CRYSTAL_GROUP, group, max_count)).strip() or name_kr.strip()


def jewel_groups(group_data: bytes | None) -> dict[int, JewelGroup]:
    """Group number -> its name and preset limit; empty without `jewelgroupstaticstatus.bss`."""
    if group_data is None:
        return {}
    return {
        row["group"]: JewelGroup(
            jewel_group_name(row["group"], row["max_count"], row["name_kr"]),
            row["max_count"],
        )
        for row in parse_jewel_group_records(group_data)
    }
