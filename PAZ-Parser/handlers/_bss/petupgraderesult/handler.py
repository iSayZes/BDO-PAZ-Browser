"""petupgraderesult.bss preview handler: the Tier 5 pet and alpha talent of each Tier 4 pet."""

from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import SORT_ASC, TableSort

from _common.character import character_name
from _common.html import Column, e, error, record_link, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _dbss.pet.joins import PET_FILE, SKILL_CATALOG_FILE, base_skill_names
from .parser import FILE_NAME, parse_petupgraderesult_records


_LANG_DIR = Path(__file__).parent / "lang"
_BINARY = "gamecommondata/binary"
_PET = f"{_BINARY}/{PET_FILE}"
_CATALOG = f"{_BINARY}/{SKILL_CATALOG_FILE}"
_LINK_CLASS = "record-link"
_ERROR_FIELD = "_error"


def _with_names(record: dict, talent_names: dict[int, str]) -> dict:
    """The record with the LOC (else Korean) pet names and the alpha talent name ('' on a miss)."""
    result_pet_id = record["result_pet_id"]
    return {
        **record,
        "pet_name": character_name(record["pet_id"]),
        "result_pet_name": character_name(result_pet_id) if result_pet_id is not None else "",
        "leader_base_skill_name": talent_names.get(record["leader_base_skill_id"], ""),
    }


def _pet_link(pet_id: int | None) -> str:
    if pet_id is None:
        return "-"
    return record_link(str(pet_id), _PET, "pet_id", pet_id, _LINK_CLASS)


class PetUpgradeResultBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["petId"], "num", sort_key="pet_id"),
            Column(cols["pet"], sort_key="pet_name"),
            Column(cols["section"], sort_key="section"),
            Column(cols["resultPetId"], "num", sort_key="result_pet_id"),
            Column(cols["resultPet"], sort_key="result_pet_name"),
            Column(cols["talentId"], "num", sort_key="leader_base_skill_id"),
            Column(cols["talent"], sort_key="leader_base_skill_name"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # The Result rows first, then the Leader Skill rows, each in file order.
        return TableSort("section", SORT_ASC)

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{SKILL_CATALOG_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_petupgraderesult_records(data)
        except ValueError as ex:
            return [{_ERROR_FIELD: f"{FILE_NAME} could not be parsed: {ex}"}]

        talent_names = base_skill_names(companions.get(SKILL_CATALOG_FILE))
        return [_with_names(record, talent_names) for record in records]

    def _cells(self, record: dict, sections: dict[str, str]) -> list[str]:
        talent_id = record["leader_base_skill_id"]
        return [
            _pet_link(record["pet_id"]),
            e(record["pet_name"] or "-"),
            e(sections[str(record["section"])]),
            _pet_link(record["result_pet_id"]),
            e(record["result_pet_name"] or "-"),
            record_link(str(talent_id), _CATALOG, "equip_skill_id", talent_id, _LINK_CLASS),
            e(record["leader_base_skill_name"] or "-"),
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and _ERROR_FIELD in records[0]:
            return error(records[0][_ERROR_FIELD])

        sections = load_handler_strings(self.lang, _LANG_DIR)["sections"]
        start = page * page_size
        rows = [self._cells(record, sections) for record in records[start : start + page_size]]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
