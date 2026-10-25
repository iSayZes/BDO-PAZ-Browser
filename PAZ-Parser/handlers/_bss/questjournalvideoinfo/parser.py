"""`questjournalvideoinfo.bss`: the video pages of the Morning Light journal.

    PABR | u32 count | count x 13-byte row | string table | u32 string_table_start | u32 0

Each row names a quest and string-table indices for its Bink video and its
full-size artwork. Full layout in docs/file-formats/bss/questjournalvideoinfo_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at, string_table_start
from _common.ui_texture import ui_texture_path


# Stored video names are relative to this folder and carry no extension.
VIDEO_ROOT = "ui_movie/pc/"
VIDEO_EXTENSION = ".bk2"

# u16 quest_chain_id | u16 quest_id | u32 video_ref | u32 artwork_ref | u8 unknown_0c
_ROW = struct.Struct("<HHIIB")
_ROW_SIZE = 13
assert _ROW.size == _ROW_SIZE


def _row_offsets(data: bytes) -> range:
    """Start of every row. Raises ValueError when the rows do not fill the file."""
    return fixed_row_offsets(data, _ROW_SIZE, "questjournalvideoinfo.bss")


def _video_path(stored: str) -> str:
    return f"{VIDEO_ROOT}{stored.lower()}{VIDEO_EXTENSION}" if stored else ""


def parse_questjournalvideoinfo_records(data: bytes) -> list[dict]:
    """Every journal video row in file order, with its paths resolved.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    offsets = _row_offsets(data)
    strings = read_string_table(data)
    records: list[dict] = []
    for offset in offsets:
        quest_chain_id, quest_id, video_ref, artwork_ref, unknown_0c = _ROW.unpack_from(data, offset)
        records.append({
            "quest_chain_id": quest_chain_id,
            "quest_id": quest_id,
            "packed_quest_id": quest_id << 16 | quest_chain_id,
            "video_path": _video_path(string_at(strings, video_ref)),
            "artwork_path": ui_texture_path(string_at(strings, artwork_ref)),
            "unknown_0c": unknown_0c,
        })
    return records


def build_quest_artwork_index(data: bytes) -> dict[int, str]:
    """Journal artwork path by packed quest ID, for `IndexKind.QUEST_ARTWORK_ICON`."""
    return {
        record["packed_quest_id"]: record["artwork_path"]
        for record in parse_questjournalvideoinfo_records(data)
        if record["artwork_path"]
    }
