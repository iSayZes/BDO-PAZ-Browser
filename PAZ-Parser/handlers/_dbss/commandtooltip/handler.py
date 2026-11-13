"""commandtooltip.dbss preview handler: the keyboard and console pad command text of each skill tooltip."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.offset_table import (
    OffsetTableHandler,
    offset_column,
    offset_records,
    offset_text,
    size_column,
)
from _common.pa_text import pa_line_cell
from _common.pabr_offset import parse_pabr_u32_offset_rows
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_commandtooltip_records
from .text import command_fields


_LANG_DIR = Path(__file__).parent / "lang"


def command_tooltip_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            offset_column(KEY_FIELD, "keyHash"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_pabr_u32_offset_rows, KEY_FIELD, "data_offset", "data_size"),
    )


class CommandTooltipHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["keyHash"], "num", sort_key=KEY_FIELD),
            Column(labels["pcCommand"], sort_key="pc_command"),
            Column(labels["consoleCommand"], sort_key="console_command"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, **command_fields(record[KEY_FIELD], record["pc_command_kr"], record["console_command_kr"])}
            for record in parse_commandtooltip_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(offset_text(record[KEY_FIELD])),
            pa_line_cell(record, "pc_command"),
            pa_line_cell(record, "console_command"),
        ]
