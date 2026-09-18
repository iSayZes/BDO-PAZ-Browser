"""Item icon path derivation.

Item icons are keyed by item ID in one flat folder. Items also have a `.dds`
icon, but those live in per-category folders that differ per item and are not
derivable from the ID, so the flat PNG folder is the only usable source.

A small minority of items ship only a `web_`-prefixed file in that folder. The
preview icon resolver falls back to that sibling, so handlers always emit the
canonical unprefixed path.

Some items are keyed in that folder by asset name rather than by ID and cannot be
reached from the ID alone; they render as a missing-icon placeholder. Resolving
them needs an item ID to icon name mapping that is not yet decoded.
"""

from __future__ import annotations


ITEM_ICON_DIR = "ui_texture/icon/new_icon/product_icon_png"


def item_icon_path(item_id: int) -> str:
    """Return the canonical icon path for an item ID."""
    return f"{ITEM_ICON_DIR}/{item_id:08d}.png"
