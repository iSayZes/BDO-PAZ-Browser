"""petpcroom.dbss preview handler: the three equip skills of each PC room pet."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.equipskill_roll import equip_skill_name, read_skill_nos
from _common.html import Column, e, error, record_link, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_offset_rows
from .parser import FILE_NAME, SKILL_FIELDS, parse_petpcroom_records


_LANG_DIR = Path(__file__).parent / "lang"
_BINARY = "gamecommondata/binary"
_PET = f"{_BINARY}/pet.dbss"
_CATALOG_FILE = "petequipskill.bss"
_CATALOG = f"{_BINARY}/{_CATALOG_FILE}"
_LINK_CLASS = "record-link"
# skill_name_0 to skill_name_2, next to equip_skill_id_0 to equip_skill_id_2
_NAME_FIELDS = tuple(f"skill_name_{index}" for index in range(len(SKILL_FIELDS)))


def pet_pc_room_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("pet_id", "petId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "pet_id"),
    )


def _with_names(record: dict, skill_nos: dict[int, int]) -> dict:
    """The record with the pet's LOC name and each equip skill's catalog name ('' on a miss)."""
    names = {}
    for id_field, name_field in zip(SKILL_FIELDS, _NAME_FIELDS):
        skill_no = skill_nos.get(record[id_field], 0)
        names[name_field] = equip_skill_name(skill_no) if skill_no else ""
    return {**record, "pet_name": character_name(record["pet_id"]), **names}


class PetPcRoomHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["petId"], "num", sort_key="pet_id"),
            Column(cols["pet"], sort_key="pet_name"),
            *(Column(cols[f"skill{index + 1}"], sort_key=field) for index, field in enumerate(_NAME_FIELDS)),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_CATALOG_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_petpcroom_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        catalog_raw = companions.get(_CATALOG_FILE)
        skill_nos = read_skill_nos(catalog_raw) if catalog_raw else {}
        return [_with_names(record, skill_nos) for record in records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        rows = [
            [
                record_link(str(r["pet_id"]), _PET, "pet_id", r["pet_id"], _LINK_CLASS),
                e(r["pet_name"] or "-"),
                *(
                    record_link(r[name_field] or str(r[id_field]), _CATALOG, "equip_skill_id", r[id_field], _LINK_CLASS)
                    for id_field, name_field in zip(SKILL_FIELDS, _NAME_FIELDS)
                ),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
