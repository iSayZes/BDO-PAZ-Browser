"""`groupcameradata.bss`: the summaries shown when a story cutscene is skipped.

    PABR | u32 count | count x 28-byte row | string table | u32 string_table_start | u32 0

Each row holds a scene ID and string-table indices for the Korean title,
recap and quote and the region symbol icon. Full layout in
docs/file-formats/bss/groupcameradata_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at, string_table_start
from _common.ui_texture import ui_texture_path


# u32 scene_id | u32 title_ref | u32 description_ref | u32 quote_ref | u32 icon_ref | 8x
_ROW = struct.Struct("<5I8x")
_ROW_SIZE = 28
assert _ROW.size == _ROW_SIZE


def _row_offsets(data: bytes) -> range:
    """Start of every row. Raises ValueError when the rows do not fill the file."""
    return fixed_row_offsets(data, _ROW_SIZE, "groupcameradata.bss")


def parse_groupcameradata_records(data: bytes) -> list[dict]:
    """Every cutscene row in file order, with its strings resolved.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    offsets = _row_offsets(data)
    strings = read_string_table(data)
    records: list[dict] = []
    for offset in offsets:
        scene_id, title_ref, description_ref, quote_ref, icon_ref = _ROW.unpack_from(data, offset)
        icon = string_at(strings, icon_ref)
        records.append({
            "scene_id": scene_id,
            "icon_path": ui_texture_path(icon),
            "title_kr": string_at(strings, title_ref),
            "description_kr": string_at(strings, description_ref),
            "quote_kr": string_at(strings, quote_ref),
        })
    return records


def build_cutscene_icon_index(data: bytes) -> dict[int, str]:
    """Region symbol path by scene ID, for `IndexKind.CUTSCENE_ICON`."""
    return {
        record["scene_id"]: record["icon_path"]
        for record in parse_groupcameradata_records(data)
        if record["icon_path"]
    }
