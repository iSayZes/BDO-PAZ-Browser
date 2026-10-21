"""Character names and titles, shared by the tables that link a character.

LOC type 6 holds the name plate of every character key: monsters, NPCs,
summons, siege objects and placed furniture. `str_id4` 0 is the name and 1
the title above it (`<Storage Keeper>`), `<null>` when the character has none.

Characters without a LOC name or title fall back to their Korean
`characterstatic.dbss` one from the `CHARACTER_NAME_KR` and
`CHARACTER_TITLE_KR` lookup indexes, so no table needs `characterstatic.dbss`
as a companion for them.
"""

from __future__ import annotations

from _common.loc import LOC_NULL, loc_text
from _common.lookup_index import IndexKind, lookup

LOC_CHARACTER_NAME = 6
_LOC_TITLE_ID4 = 1


def _korean_text(kind: IndexKind, character_id: int) -> str:
    """Korean `characterstatic.dbss` text of a character from `kind`, or '' when the index lacks it."""
    text = lookup(kind, character_id)
    return text if isinstance(text, str) else ""


def character_loc_name(character_id: int) -> str:
    """LOC type 6 name of a character in the loaded LOC language, else ''.

    For tables that store a Korean name of their own and show it before the
    `characterstatic.dbss` one; every other table calls `character_name`.
    """
    return loc_text(LOC_CHARACTER_NAME, character_id)


def character_name_kr(character_id: int) -> str:
    """Korean `characterstatic.dbss` name of a character, or '' when the index lacks it."""
    return _korean_text(IndexKind.CHARACTER_NAME_KR, character_id)


def character_name(character_id: int) -> str:
    """LOC type 6 name of a character, else its Korean `characterstatic.dbss` name, else ''."""
    return character_loc_name(character_id) or character_name_kr(character_id)


def character_loc_title(character_id: int) -> str:
    """LOC type 6 title of a character in the loaded LOC language, else ''.

    For tables that store a Korean title of their own and show it before the
    `characterstatic.dbss` one; every other table calls `character_title`.
    """
    title = loc_text(LOC_CHARACTER_NAME, character_id, _LOC_TITLE_ID4)
    return "" if title == LOC_NULL else title


def character_title_kr(character_id: int) -> str:
    """Korean `characterstatic.dbss` title of a character, or '' when the index lacks it."""
    return _korean_text(IndexKind.CHARACTER_TITLE_KR, character_id)


def character_title(character_id: int) -> str:
    """LOC type 6 title of a character, else its Korean `characterstatic.dbss` title, else ''."""
    return character_loc_title(character_id) or character_title_kr(character_id)
