"""Item icon resolution.

Two sources, tried in order:

1. The **item icon index**, built from `itemenchant.dbss`, whose level-0 records
   store each item's icon path inline. This is the only source that covers items
   whose icon is named after a 3D asset (furniture) or sits in a per-category
   folder that cannot be derived from the ID. The app loads it once per PAZ
   folder and injects it here, the same way `loc.py` receives LOC data.

2. Derivation from the item ID in the flat `product_icon_png` folder, used when
   the index is unavailable or has no entry. A minority of items ship only a
   `web_`-prefixed file there, which the preview icon resolver falls back to, so
   the canonical unprefixed path is always what gets emitted.

Icons keyed by cash-product ID are deliberately not used: `cashproduct.dbss`
maps a product to the item it grants, but its icon is the shop product art, not
the item's own icon.
"""

from __future__ import annotations


ITEM_ICON_DIR = "ui_texture/icon/new_icon/product_icon_png"

# item_id -> PAZ icon path; populated by init_item_icons().
_ITEM_ICONS: dict[int, str] | None = None


def init_item_icons(index: dict[int, str] | None) -> None:
    """Install the item icon index. Pass None to clear it."""
    global _ITEM_ICONS
    _ITEM_ICONS = index


def is_item_icon_index_loaded() -> bool:
    return _ITEM_ICONS is not None


def item_icon_index_size() -> int:
    return len(_ITEM_ICONS) if _ITEM_ICONS else 0


def derive_item_icon_path(item_id: int) -> str:
    """Icon path implied by the item ID alone, ignoring the index."""
    return f"{ITEM_ICON_DIR}/{item_id:08d}.png"


def item_icon_path(item_id: int) -> str:
    """Return the best known icon path for an item ID."""
    if _ITEM_ICONS is not None:
        stored = _ITEM_ICONS.get(item_id)
        if stored:
            return stored

    return derive_item_icon_path(item_id)
