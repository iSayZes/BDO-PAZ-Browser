"""sequence_skill.bss and cutscene_skill.bss preview handler: one row per
cutscene and class, with the skills listed for it.

A row stores only its file name hash. The name comes from the sibling
equipment table, which stores name and hash for the same files; a hash it
does not hold shows without a name. Skill names are LOC type 10.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _bss.tutorial_equipment.parser import CUTSCENE_FILE_NAME as CUTSCENE_EQUIPMENT
from _bss.tutorial_equipment.parser import SEQUENCE_FILE_NAME as SEQUENCE_EQUIPMENT
from _bss.tutorial_equipment.parser import file_names_by_hash
from _common.class_type import class_name
from _common.html import Column, e
from _common.row_table import RowTableHandler
from _common.skill import skill_name
from _common.skill_cells import skill_list_cell
from .parser import CUTSCENE_FILE_NAME, SEQUENCE_FILE_NAME, parse_sequence_skill_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_SKILL_PREVIEW = 6
# The equipment table that names the files of each skill table.
_NAME_SOURCES = {
    SEQUENCE_FILE_NAME: SEQUENCE_EQUIPMENT,
    CUTSCENE_FILE_NAME: CUTSCENE_EQUIPMENT,
}


def file_name_hash_text(file_name_hash: int) -> str:
    """The hash as the client's 8-digit hex, `0xDEFE7AE1`."""
    return f"0x{file_name_hash:08X}"


class SequenceSkillBssHandler(RowTableHandler):
    lang_dir = _LANG_DIR

    def __init__(self, file_name: str) -> None:
        super().__init__()
        self.file_name = file_name
        self._name_source = _NAME_SOURCES[file_name]

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{self._name_source}"]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["fileNameHash"], "num", sort_key="file_name_hash"),
            Column(labels["cutsceneFile"], sort_key="cutscene_file_name"),
            Column(labels["classType"], "num", sort_key="class_type"),
            Column(labels["className"], sort_key="class_name"),
            Column(labels["skillCount"], "num", sort_key="skill_count"),
            Column(labels["skills"]),
        ]

    def _file_names(self, companions: dict[str, bytes]) -> dict[int, str]:
        """File names by hash from the equipment table; empty when it is missing."""
        source = companions.get(self._name_source)
        return file_names_by_hash(source, self._name_source) if source else {}

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        file_names = self._file_names(companions)
        return [
            {
                "file_name_hash": row["file_name_hash"],
                "cutscene_file_name": file_names.get(row["file_name_hash"], ""),
                "class_type": entry["class_type"],
                "class_name": class_name(entry["class_type"]),
                "skill_count": entry["skill_count"],
                "skill_nos": entry["skill_nos"],
                "skill_names": [skill_name(skill_no) or str(skill_no) for skill_no in entry["skill_nos"]],
            }
            for row in parse_sequence_skill_rows(data, self.file_name)
            for entry in row["classes"]
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(file_name_hash_text(record["file_name_hash"])),
            e(record["cutscene_file_name"] or _EMPTY),
            e(record["class_type"]),
            e(record["class_name"]),
            e(record["skill_count"]),
            skill_list_cell(record["skill_nos"], _SKILL_PREVIEW),
        ]
