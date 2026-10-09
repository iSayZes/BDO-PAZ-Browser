"""Instance field titles in the loaded LOC language.

`instancefieldmapinfo.bss` names a field with a `GAME` sheet key
(`INSTANCEDUNGEONDATA_A1_001_NAME`); the INSTANCE_FIELD_TITLE lookup index
holds that key's hash, so a table names a field without opening
`stringtable.bss`.
"""

from __future__ import annotations

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text
from _common.instance_field import instance_field_name
from _common.lookup_index import IndexKind, lookup


def instance_field_title(key: int) -> str:
    """`The Magnus: The Great Single Path`, or '' without a title or LOC text."""
    key_hash = lookup(IndexKind.INSTANCE_FIELD_TITLE, key)
    return ui_hash_text(GAME_SHEET, key_hash) if isinstance(key_hash, int) else ""


def instance_field_label(key: int) -> str:
    """`Title (A1_001)`, the title or the internal name alone, or ''."""
    title, name = instance_field_title(key), instance_field_name(key)
    if title and name:
        return f"{title} ({name})"
    return title or name
