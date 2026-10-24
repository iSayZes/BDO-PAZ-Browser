"""emoticon.dbss preview handler: the chat emoticons with their icons, names and keywords."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, icon_cell
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_emoticon_records, parse_emoticonoffset_records
from .text import emoticon_keyword, emoticon_name, stored_text, texture_file


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def emoticon_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn(KEY_FIELD, "emoticonKey"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        parse_emoticonoffset_records,
    )


def _text_cell(text: str) -> str:
    return e(text) if text else _EMPTY


class EmoticonHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["emoticonKey"], "num", sort_key=KEY_FIELD),
            Column(labels["name"], sort_key="name"),
            Column(labels["icon"], sort_key="icon_path"),
            Column(labels["iconCount"], "num", sort_key="icon_count"),
            Column(labels["rowCount"], "num", sort_key="row_count"),
            Column(labels["columnCount"], "num", sort_key="column_count"),
            Column(labels["keyword"], sort_key="keyword"),
            Column(labels["sequence"], sort_key="sequence"),
            Column(labels["group"], "num", sort_key="group"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "name": emoticon_name(record[KEY_FIELD], record["name_kr"]),
                "keyword": emoticon_keyword(record[KEY_FIELD], record["keyword_kr"]),
                "sequence": stored_text(record["sequence_path"]),
                "_icon_file": texture_file(record["icon_path"]),
            }
            for record in parse_emoticon_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            _text_cell(record["name"]),
            icon_cell(record["_icon_file"]),
            e(record["icon_count"]),
            e(record["row_count"]),
            e(record["column_count"]),
            _text_cell(record["keyword"]),
            _text_cell(record["sequence"]),
            e(record["group"]),
        ]
