"""Crystal group names in the user's language.

LOC type 121 keys a group's name by `(group, max_count)` in `str_id1` and
`str_id2` (jewelgroupstaticstatus_bss.md, Notes).
"""

from __future__ import annotations

from _common.loc import loc_lookup, strip_pa_tags


_LOC_CRYSTAL_GROUP = 121

# The limit the item tooltip shows as "No Limit" (`LUA_TOOLTIP_CRYSTALGROUP_NOLIMIT`
# in panel_tooltip_item.luac).
NO_LIMIT = 1000


def jewel_group_name(group: int, max_count: int, name_kr: str) -> str:
    """The group's LOC name, else its Korean name."""
    return strip_pa_tags(loc_lookup(_LOC_CRYSTAL_GROUP, group, max_count)).strip() or name_kr.strip()
