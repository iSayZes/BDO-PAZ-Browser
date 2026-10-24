"""classinputdata.bss preview handler: one row per index and class entry.

The commands show as their `CppEnums.ActionInputType` names joined by `+`
(`Dash + MoveBack`, the sheet's `Shift,S`).
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.enum_name import enum_name
from _common.html import Column, e
from _common.row_table import RowTableHandler
from .parser import ACTION_INPUT_TYPES, FILE_NAME, parse_classinput_records


_LANG_DIR = Path(__file__).parent / "lang"
_COMMAND_SEPARATOR = " + "


def command_text(commands: list[int]) -> str:
    """`Dash + MoveBack`: the action input names of a command list."""
    return _COMMAND_SEPARATOR.join(enum_name(ACTION_INPUT_TYPES, command) for command in commands)


class ClassInputDataBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["index"], "num", sort_key="index"),
            Column(labels["classNo"], "num", sort_key="class_no"),
            Column(labels["commands"], sort_key="command_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "command_text": command_text(record["commands"])}
            for record in parse_classinput_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [e(record["index"]), e(record["class_no"]), e(record["command_text"])]
