"""Fields that several tables of `tables.py` share."""

from __future__ import annotations

from _common.character import character_name
from _common.item_key import item_name_tagged
from _common.title import title_name
from .layout import IconLookup, NameLookup, ValueField
from .names import item_icon_path, map_color_text


CHARACTER_NAME = NameLookup("character_name", "character", character_name)
CHARACTER_KEY = ValueField("character_key", "H", "characterId", CHARACTER_NAME)
_ITEM_NAME = NameLookup("item_name", "item", item_name_tagged, is_tagged=True)
_ITEM_ICON = IconLookup("icon_path", "icon", item_icon_path)


def item_field(name: str) -> ValueField:
    """A u32 item field under `name`, with the item's LOC name and icon."""
    return ValueField(name, "I", "itemId", _ITEM_NAME, _ITEM_ICON)


ITEM_ID = item_field("item_id")
# The same item field, for the tables whose source sheet names it `ItemKey`.
ITEM_KEY = item_field("item_key")
TITLE_ID = ValueField("title_id", "I", "titleId", NameLookup("title_name", "title", title_name))
# A colour of a region map bitmap (`ui_texture/minimap/area/<name>map.bmp`),
# as its `.rid` palette lists it; hardcorechannelinfo_bss.md, Field Names.
MAP_COLOR = ValueField("map_color", "3s", "mapColor", display=map_color_text)
