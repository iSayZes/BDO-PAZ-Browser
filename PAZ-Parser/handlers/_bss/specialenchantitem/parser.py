"""`specialenchantitem.bss`: the items whose name or icon changes per level.

    PABR | u32 count | count x 19-byte row | string table | u32 string_table_start | u32 0

Each row holds a packed item key, the level the client shows, and string-table
indices for the icon path and the Korean name of that level. It copies the
per-level icons of `itemenchant.dbss` for these items. Full layout in
docs/file-formats/specialenchantitem_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.item_key import split_item_key
from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at, string_table_start
from _common.ui_texture import UI_TEXTURE_ICON_ROOT, ui_texture_path


# u32 item_key | u8 display_level | u32 icon_ref | u32 name_ref | u32 unknown_0d (skipped)
# | u8 unknown_11 | u8 family_name_exception
_ROW = struct.Struct("<IBII4xBB")
_ROW_SIZE = 19
assert _ROW.size == _ROW_SIZE


def _row_offsets(data: bytes) -> range:
    """Start of every row. Raises ValueError when the rows do not fill the file."""
    return fixed_row_offsets(data, _ROW_SIZE, "specialenchantitem.bss")


def parse_specialenchantitem_records(data: bytes) -> list[dict]:
    """Every item level row in file order, with its strings resolved.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    offsets = _row_offsets(data)
    strings = read_string_table(data)
    records: list[dict] = []
    for offset in offsets:
        item_key, display_level, icon_ref, name_ref, unknown_11, family_name_exception = (
            _ROW.unpack_from(data, offset)
        )
        item_id, enchant_level = split_item_key(item_key)
        records.append({
            "item_key": item_key,
            "item_id": item_id,
            "enchant_level": enchant_level,
            "display_level": display_level,
            # Stored relative to ui_texture/icon/, as in itemenchant.dbss.
            "icon_path": ui_texture_path(string_at(strings, icon_ref), UI_TEXTURE_ICON_ROOT),
            "name_kr": string_at(strings, name_ref),
            "unknown_11": unknown_11,
            "family_name_exception": family_name_exception,
        })
    return records


def build_item_key_icon_index(data: bytes) -> dict[int, str]:
    """Icon path by packed item key, for `IndexKind.ITEM_KEY_ICON`."""
    return {
        record["item_key"]: record["icon_path"]
        for record in parse_specialenchantitem_records(data)
        if record["icon_path"]
    }
