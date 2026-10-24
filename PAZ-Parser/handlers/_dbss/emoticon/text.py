"""Display text and icon paths of `emoticon.dbss` rows, shared with `emoticonpackage.dbss`."""

from __future__ import annotations

from _common.icon_index import clean_stored_icon_path
from _common.loc import LOC_NULL, loc_text
from _common.ui_texture import UI_TEXTURE_ROOT

# LOC type 60: str_id1 = emoticon_key; str_id4 0 name, 1 chat keyword.
LOC_EMOTICON = 60
LOC_NAME = 0
LOC_KEYWORD = 1


def stored_text(value: str) -> str:
    """`value`, or '' for the `<NULL>` placeholder the item link row stores
    (and its LOC keyword holds as `<null>`)."""
    return "" if value.lower() == LOC_NULL else value


def emoticon_name(emoticon_key: int, name_kr: str) -> str:
    """The LOC name (`Angry Black Spirit`), else the Korean name."""
    return stored_text(loc_text(LOC_EMOTICON, emoticon_key, LOC_NAME)) or name_kr


def emoticon_keyword(emoticon_key: int, keyword_kr: str) -> str:
    """The LOC chat keyword (`Angry`), else the Korean keyword, else ''."""
    return stored_text(loc_text(LOC_EMOTICON, emoticon_key, LOC_KEYWORD)) or stored_text(keyword_kr)


def texture_file(stored: str) -> str:
    """PAZ path of a stored texture path under `ui_texture/`, or '' for none.

    Row `1` stores `Emoticon\\Emoticon_Item.dds` with a backslash.
    """
    path = stored_text(stored)
    return f"{UI_TEXTURE_ROOT}{clean_stored_icon_path(path)}" if path else ""
