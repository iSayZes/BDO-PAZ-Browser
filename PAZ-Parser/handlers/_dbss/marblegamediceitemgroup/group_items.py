"""The game items that grant a Black Spirit's Adventure dice drop group.

An item whose contents event is `98` names a `marblegamediceitemgroup.dbss`
group key in `contents_event_param1`; the `MARBLE_DICE_GROUP_ITEMS` lookup
index turns that around, so neither view loads `itemenchant.dbss`. Both
marble dice views show the items with `items_cell()`. See
docs/file-formats/marblegamediceitemgroup_dbss.md.
"""

from __future__ import annotations

from collections.abc import Iterable

from _common.item_key import item_key_list_cell, item_name
from _common.lookup_index import IndexKind, lookup

_LIST_PREVIEW_ITEMS = 3
_EMPTY = "-"


def group_item_ids(group_keys: Iterable[int]) -> list[int]:
    """The base items that grant any of the groups, each once, in group then item ID order."""
    item_ids: dict[int, None] = {}
    for group_key in group_keys:
        linked = lookup(IndexKind.MARBLE_DICE_GROUP_ITEMS, group_key)
        if isinstance(linked, tuple):
            item_ids.update(dict.fromkeys(linked))
    return list(item_ids)


def item_fields(item_ids: list[int]) -> dict:
    """`item_ids`, their names for search and export, and `item_count` (None sorts last)."""
    return {
        "item_ids": item_ids,
        "item_names": [item_name(item_id) or str(item_id) for item_id in item_ids],
        "item_count": len(item_ids) or None,
    }


def items_cell(item_ids: list[int]) -> str:
    """The first items with icon and grade colour, a hoverable count of the rest, or `-`."""
    return item_key_list_cell(item_ids, _LIST_PREVIEW_ITEMS) or _EMPTY
