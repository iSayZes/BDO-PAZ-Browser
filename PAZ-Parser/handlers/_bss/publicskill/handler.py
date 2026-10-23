"""publicskill.bss preview handler: the item and event skills."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_publicskill_keys
from .skill_rows import SKILL_FIELD, SKILL_NO_FIELD, skill_key_fields, skill_name_cell, skill_no_cell


_LANG_DIR = Path(__file__).parent / "lang"


class PublicSkillHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["skillNo"], "num", sort_key=SKILL_NO_FIELD),
            Column(labels["skill"], sort_key=SKILL_FIELD),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [skill_key_fields(skill_key) for skill_key in parse_publicskill_keys(data)]

    def cells(self, record: dict) -> list[str]:
        return [skill_no_cell(record), skill_name_cell(record)]
