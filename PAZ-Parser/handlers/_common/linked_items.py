"""Item lists read from a lookup index whose values are base item IDs.

Several tables show the items that point at a record, through an index that
turns an `itemenchant.dbss` field around (`MARBLE_DICE_GROUP_ITEMS`,
`CUSTOMIZED_ITEM_BOXES`, `MESH_KEY_ITEMS`). These helpers read such an index
and give every view the same `item_ids` / `item_names` / `item_count` fields
and the same icon cell.
"""

from __future__ import annotations

from collections.abc import Iterable

from _common.item_key import item_key_list_cell, item_name
from _common.lookup_index import IndexKind, lookup

_LIST_PREVIEW_ITEMS = 3
_EMPTY = "-"


def linked_item_ids(kind: IndexKind, keys: Iterable[int]) -> list[int]:
    """The base items `kind` links to any of `keys`, each once, in key then item ID order.

    Empty when the index is not loaded or holds none of the keys.
    """
    item_ids: dict[int, None] = {}
    for key in keys:
        linked = lookup(kind, key)
        if isinstance(linked, tuple):
            item_ids.update(dict.fromkeys(linked))
    return list(item_ids)


def item_list_fields(item_ids: list[int], prefix: str = "") -> dict:
    """`item_ids`, their names for search and export, and `item_count` (None sorts last).

    `prefix` goes before each field name, for a table whose own fields
    already use one of them.
    """
    return {
        f"{prefix}item_ids": item_ids,
        f"{prefix}item_names": [item_name(item_id) or str(item_id) for item_id in item_ids],
        f"{prefix}item_count": len(item_ids) or None,
    }


def item_list_cell(item_ids: list[int]) -> str:
    """The first items with icon and grade colour, a hoverable count of the rest, or `-`."""
    return item_key_list_cell(item_ids, _LIST_PREVIEW_ITEMS) or _EMPTY
