"""The Lightstone sets an item counts toward, for the `itemenchant.dbss` table.

Read from the `LIGHTSTONE_SETS` lookup index, so the item table needs no
`lightstoneset.bss` companion. See docs/file-formats/lightstoneset_bss.md.
"""

from __future__ import annotations

from _common.lookup_index import IndexKind, lookup
from _common.pa_text import strip_pa_tags
from .text import set_text


def item_set_ids(item_id: int) -> tuple[int, ...]:
    """Set IDs the item counts toward as a member or substitute, ascending.

    Empty for other items and when the index is not loaded.
    """
    linked = lookup(IndexKind.LIGHTSTONE_SETS, item_id)
    return linked if isinstance(linked, tuple) else ()


def set_label_tagged(set_id: int) -> str:
    """`12 [Well-prepared]` with the name in its LOC type 113 colours, or the
    set ID alone when LOC has no text for it."""
    name = set_text(set_id, "").name
    return f"{set_id} {name}" if strip_pa_tags(name).strip() else str(set_id)
