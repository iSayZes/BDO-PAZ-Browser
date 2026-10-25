"""Packed item keys and item names shared by the item tables.

`itemenchant.dbss`, `itemsubgroup.dbss` and the tables that hand out items
pack an item and its enhancement level into one key:

    item_key = enchant_level << 24 | item_id

Level 0 is the base item. LOC type 0 names an item by its ID alone, so every
level of one item shares a name; LOC type 79 (`str_id1` item ID, `str_id2`
level) names the levels of a few hundred items on their own (`DEC: Sovereign
Longsword`, `Wailing Fallen God's Armor`). See
docs/file-formats/dbss/itemenchant_dbss.md and specialenchantitem_bss.md.

A few hundred items also change icon with their level (Sovereign weapons,
Fallen God armor); `item_key_icon_path()` picks that icon when there is one.
See docs/file-formats/bss/specialenchantitem_bss.md. Item lists draw each name in
its grade colour (`_common/item_grade.py`).
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence

from _common.html import hidden_slice, html_list_cell, icon_html_label_cell, icon_html_list_cell
from _common.icon_index import IconKind, icon_path
from _common.item_grade import item_grade, item_grade_tagged
from _common.loc import loc_lookup, loc_text, strip_pa_tags
from _common.lookup_index import IndexKind, lookup
from _common.pa_text import pa_html

LOC_ITEM_NAME = 0
LOC_ITEM_LEVEL_NAME = 79

_ITEM_ID_MASK = 0x00FFFFFF
_ENCHANT_LEVEL_SHIFT = 24


def split_item_key(item_key: int) -> tuple[int, int]:
    """`(item_id, enchant_level)` of an item key."""
    return item_key & _ITEM_ID_MASK, item_key >> _ENCHANT_LEVEL_SHIFT


def item_name(item_id: int) -> str:
    """LOC type 0 name of an item, else the Korean name `itemenchant.dbss` stores, else ''."""
    return loc_text(LOC_ITEM_NAME, item_id) or _item_name_kr(item_id)


def _item_name_kr(item_id: int) -> str:
    name = lookup(IndexKind.ITEM_NAME_KR, item_id)
    return name if isinstance(name, str) else ""


def item_level_name(item_id: int, enchant_level: int) -> str:
    """LOC type 79 name of one item level (`DEC: Sovereign Longsword`), or ''."""
    return strip_pa_tags(loc_lookup(LOC_ITEM_LEVEL_NAME, item_id, enchant_level)).strip()


def item_name_tagged(item_id: int) -> str:
    """`item_name` in the item's grade colour, as a `<PAColor>` tag for `pa_fields`, or ''."""
    return item_grade_tagged(item_name(item_id), item_grade(item_id))


def item_key_icon_path(item_key: int) -> str:
    """Icon of an item at its level: that level's own icon, else the item's icon."""
    item_id, _ = split_item_key(item_key)
    return icon_path(IconKind.ITEM_KEY, item_key) or icon_path(IconKind.ITEM, item_id)


def item_key_text(item_key: int) -> str:
    """`DEC: Sovereign Longsword` or `Blackstar Helmet (19)`.

    A level whose LOC type 79 name differs from the item name shows that name
    alone: it carries a grade or a stage word that no other level of the item
    shares. Any other level shows the item name, then the level when above 0.
    The item ID stands in for a missing name.
    """
    item_id, enchant_level = split_item_key(item_key)
    name = item_name(item_id) or str(item_id)
    if not enchant_level:
        return name
    level_name = item_level_name(item_id, enchant_level)
    if level_name and level_name != name:
        return level_name
    return f"{name} ({enchant_level})"


def item_key_text_tagged(item_key: int) -> str:
    """`item_key_text` in the item's grade colour, as a `<PAColor>` tag for `pa_html`."""
    item_id, _ = split_item_key(item_key)
    return item_grade_tagged(item_key_text(item_key), item_grade(item_id))


def item_key_list_cell(item_keys: Sequence[int], max_items: int) -> str:
    """The first `max_items` items, each with its per-level icon and grade colour, and a count of the rest.

    Hovering the count names the hidden items.
    """
    shown = item_keys[:max_items]
    entries = [(item_key_icon_path(key), pa_html(item_key_text_tagged(key))) for key in shown]
    hidden = [item_key_text(key) for key in hidden_slice(item_keys, max_items)]
    return icon_html_list_cell(entries, len(item_keys) - len(shown), hidden_names=hidden)


def item_count_text(item_key: int, count: int) -> str:
    """`Steel x5`: an item and its count as plain text, for tab search and CSV export."""
    return f"{item_key_text(item_key)} x{count:,}"


def item_count_list_cell(items: Iterable[tuple[int, int]]) -> str:
    """Each `(item_key, count)` with its per-level icon and grade colour, then its count.

    Empty when there are no items.
    """
    entries = [
        icon_html_label_cell(item_key_icon_path(key), f"{pa_html(item_key_text_tagged(key))} x{count:,}")
        for key, count in items
    ]
    return html_list_cell(entries)
