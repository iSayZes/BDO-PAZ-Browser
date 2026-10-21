"""exptoskillexprate.dbss preview handler: the character EXP to skill EXP rate per level."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_exptoskillexprate_records, parse_exptoskillexprateoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"


def exp_to_skill_exp_rate_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_exptoskillexprateoffset_rows, KEY_FIELD, "level")


class ExpToSkillExpRateHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["level"], "num", sort_key="level"),
            Column(labels["rate"], "num", sort_key="exp_to_skill_exp_rate"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_exptoskillexprate_records(data)

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["level"]),
            # Server-only: the client file holds 0, and its scale is unknown.
            e(f"{record['exp_to_skill_exp_rate']:,}"),
        ]
