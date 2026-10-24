"""musiclevel.dbss preview handler: each music level with its EXP, bar and note counts and rank."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_musiclevel_records, parse_musicleveloffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def musiclevel_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_musicleveloffset_rows, KEY_FIELD, "musicLevel")


class MusicLevelHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["musicLevel"], "num", sort_key=KEY_FIELD),
            Column(labels["musicLevelExp"], "num", sort_key="music_level_exp"),
            Column(labels["increasingBarNumber"], "num", sort_key="increasing_bar_number"),
            Column(labels["increasingNoteNumber"], "num", sort_key="increasing_note_number"),
            Column(labels["musicRank"], sort_key="music_rank"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_musiclevel_records(data)

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(f"{record['music_level_exp']:,}"),
            e(record["increasing_bar_number"]),
            e(record["increasing_note_number"]),
            e(record["music_rank"] or _EMPTY),
        ]
