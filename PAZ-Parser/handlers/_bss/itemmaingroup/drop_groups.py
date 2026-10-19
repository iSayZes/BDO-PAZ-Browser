"""Drop groups for tables that name an `itemmaingroup.bss` group: the group and the items it lists.

`manufacture.bss` (result group) and `itemexchangesource.bss` (product and
luck drop keys) store a group ID; its items come from the group's
`itemsubgroup.dbss` subgroups. All three files are optional companions.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

from _common.html import e, record_link
from _dbss.itemsubgroup.parser import ItemSubgroup, subgroups_by_key
from .parser import ITEMMAINGROUP_PATH, ItemMainGroup, group_item_keys, parse_itemmaingroup_records

DROP_GROUP_FILES = ("itemmaingroup.bss", "itemsubgroup.dbss", "itemsubgroupoffset.dbss")
_MAINGROUP_FILE, _SUBGROUP_FILE, _SUBGROUP_OFFSET_FILE = DROP_GROUP_FILES


@dataclass(frozen=True)
class DropGroups:
    """The wanted groups the client ships, and their subgroups."""

    groups: dict[int, ItemMainGroup]
    subgroups: dict[int, ItemSubgroup]

    def has(self, group_id: int) -> bool:
        return group_id in self.groups

    def item_keys(self, group_id: int) -> list[int]:
        """The group's items; empty when the client lacks the group or its subgroups."""
        group = self.groups.get(group_id)
        return group_item_keys(group, self.subgroups) if group is not None else []


def load_drop_groups(companions: dict[str, bytes], wanted: Iterable[int]) -> DropGroups:
    """The `wanted` groups from `itemmaingroup.bss` and their subgroups.

    Both are empty without `itemmaingroup.bss`; the subgroups are empty
    without `itemsubgroup.dbss` and its offset table. Raises ValueError when
    a companion does not parse.
    """
    maingroup_raw = companions.get(_MAINGROUP_FILE)
    if maingroup_raw is None:
        return DropGroups({}, {})
    wanted_ids = set(wanted)
    groups = {
        group.group_id: group
        for group in parse_itemmaingroup_records(maingroup_raw)
        if group.group_id in wanted_ids
    }

    subgroup_raw = companions.get(_SUBGROUP_FILE)
    offset_raw = companions.get(_SUBGROUP_OFFSET_FILE)
    if subgroup_raw is None or offset_raw is None:
        return DropGroups(groups, {})
    subgroup_keys = {key for group in groups.values() for key in group.subgroup_keys}
    return DropGroups(groups, subgroups_by_key(subgroup_raw, offset_raw, subgroup_keys))


def drop_group_cell(group_id: int, has_group: bool) -> str:
    """A link to the group's `itemmaingroup.bss` row when the client has it, else the bare ID."""
    if not has_group:
        return e(group_id)
    return record_link(str(group_id), ITEMMAINGROUP_PATH, "group_id", group_id, "record-link")
