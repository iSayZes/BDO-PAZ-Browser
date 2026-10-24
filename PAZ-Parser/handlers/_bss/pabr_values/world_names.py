"""Cell text of the monster and world tables in `world_tables.py`."""

from __future__ import annotations

from _common.item_key import item_count_text, item_key_text, split_item_key


# One reward entry of bloodaltar.bss: item enchant key, 4 alignment bytes, item count.
_REWARD_ITEM_KEY, _REWARD_ITEM_COUNT = 0, 2


def reward_entry_text(entry: list) -> str:
    """An `[item_enchant_key, padding, item_count]` entry as `Combat Secret Book (M) x1`."""
    return item_count_text(entry[_REWARD_ITEM_KEY], entry[_REWARD_ITEM_COUNT])


def item_key_entry_text(item_key: int) -> str:
    """`Archaeologist's Map Piece (44273)`: an item enchant key's name and the key, or the bare key."""
    item_id, _ = split_item_key(item_key)
    text = item_key_text(item_key)
    return str(item_key) if text == str(item_id) else f"{text} ({item_key})"
