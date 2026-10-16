from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import STRINGTABLE_FILE, ui_key_hashes
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from .parser import parse_petskill_records, parse_petskilloffset_records
from .skill_type import pet_skill_type_name


_LANG_DIR = Path(__file__).parent / "lang"


def pet_skill_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("pet_skill_id", "petSkillId"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_petskilloffset_records,
    )


class PetSkillHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["petSkillId"], "num", sort_key="pet_skill_id"),
            Column(cols["skillType"], sort_key="skill_type_name"),
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["valueA"], "num", sort_key="param_0"),
            Column(cols["valueB"], "num", sort_key="param_1"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/petskilloffset.dbss", f"{folder}/{STRINGTABLE_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("petskilloffset.dbss")
        if offset_raw is None:
            raise ValueError("petskilloffset.dbss companion not found.")
        records = parse_petskill_records(data, offset_raw)
        hashes = ui_key_hashes(companions.get(STRINGTABLE_FILE), [GAME_SHEET])
        for record in records:
            record["skill_type_name"] = pet_skill_type_name(hashes, record["skill_type"])
        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        skill_count = len({r["pet_skill_id"] for r in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", skill_count=skill_count, count=len(records))
        rows = [
            [
                e(r["pet_skill_id"]),
                e(r["skill_type_name"] or r["skill_type"]),
                e(r["level"]),
                e(r["param_0"]),
                e(r["param_1"]),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)
