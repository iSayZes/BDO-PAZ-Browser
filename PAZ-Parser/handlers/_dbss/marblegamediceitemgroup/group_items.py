"""The game items that grant a Black Spirit's Adventure dice drop group.

An item whose contents event is `98` names a `marblegamediceitemgroup.dbss`
group key in `contents_event_param1`; the `MARBLE_DICE_GROUP_ITEMS` lookup
index turns that around, so neither view loads `itemenchant.dbss`. Both
marble dice views show the items with `item_list_cell()` from
`_common/linked_items.py`. See docs/file-formats/dbss/marblegamediceitemgroup_dbss.md.
"""

from __future__ import annotations

from collections.abc import Iterable

from _common.linked_items import linked_item_ids
from _common.lookup_index import IndexKind


def group_item_ids(group_keys: Iterable[int]) -> list[int]:
    """The base items that grant any of the groups, each once, in group then item ID order."""
    return linked_item_ids(IndexKind.MARBLE_DICE_GROUP_ITEMS, group_keys)
