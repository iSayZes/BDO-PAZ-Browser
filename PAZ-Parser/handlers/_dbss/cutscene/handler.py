"""cutscene.dbss preview handler: each `.pas` cutscene with its Korean name and place."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_cutscene_records, parse_cutsceneoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def key_text(key: int) -> str:
    """A file name hash as `0xDD6CA8B8`."""
    return f"0x{key:08X}"


def cutscene_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn(KEY_FIELD, "cutsceneKey", text=key_text),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_cutsceneoffset_rows, KEY_FIELD, "data_offset", "data_size"),
    )


class CutsceneHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["cutsceneKey"], "num", sort_key=KEY_FIELD),
            Column(labels["fileName"], sort_key="file_name"),
            Column(labels["name"], sort_key="cutscene_name_kr"),
            Column(labels["place"], sort_key="description_kr"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_cutscene_records(data)

    def cells(self, record: dict) -> list[str]:
        return [
            e(key_text(record[KEY_FIELD])),
            e(record["file_name"]) or _EMPTY,
            e(record["cutscene_name_kr"]) or _EMPTY,
            e(record["description_kr"]) or _EMPTY,
        ]
