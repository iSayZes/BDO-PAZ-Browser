"""Fields that several tables of `tables.py` share."""

from __future__ import annotations

from _common.character import character_name
from _common.item_key import item_name_tagged
from _common.title import title_name
from .layout import IconLookup, NameLookup, ValueField
from .names import item_icon_path


CHARACTER_NAME = NameLookup("character_name", "character", character_name)
CHARACTER_KEY = ValueField("character_key", "H", "characterId", CHARACTER_NAME)
ITEM_ID = ValueField(
    "item_id",
    "I",
    "itemId",
    NameLookup("item_name", "item", item_name_tagged, is_tagged=True),
    IconLookup("icon_path", "icon", item_icon_path),
)
TITLE_ID = ValueField("title_id", "I", "titleId", NameLookup("title_name", "title", title_name))
