"""binkaudioinfo.bss preview handler: the Wwise audio name of each Bink movie."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_binkaudioinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class BinkAudioInfoBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["movieName"], sort_key="movie_name_text"),
            Column(labels["audioName"], sort_key="audio_name_text"),
            Column(labels["audioNameDup"], sort_key="audio_name_dup_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_binkaudioinfo_records(data)

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["movie_name_text"] or _EMPTY),
            e(record["audio_name_text"] or _EMPTY),
            e(record["audio_name_dup_text"] or _EMPTY),
        ]
