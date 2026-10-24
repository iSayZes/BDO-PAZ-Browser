"""blackspirit.dbss preview handler: the Black Spirit forms and their unlock conditions."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_blackspirit_records, parse_blackspiritoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def black_spirit_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_blackspiritoffset_rows, KEY_FIELD, "index")


class BlackSpiritHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["index"], "num", sort_key=KEY_FIELD),
            Column(labels["condition"], sort_key="condition"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_blackspirit_records(data)

    def cells(self, record: dict) -> list[str]:
        return [e(record[KEY_FIELD]), e(record["condition"] or _EMPTY)]
