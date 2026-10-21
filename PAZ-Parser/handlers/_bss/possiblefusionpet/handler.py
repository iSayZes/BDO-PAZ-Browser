"""possiblefusionpet.bss preview handler: the pets of each fusion key."""

from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import SORT_ASC, TableSort

from _common.character import character_name
from _common.html import Column, e, error, record_link, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _dbss.pet.joins import PET_FILE, fusion_key_text
from .parser import FILE_NAME, parse_possiblefusionpet_records


_LANG_DIR = Path(__file__).parent / "lang"
_PET = f"gamecommondata/binary/{PET_FILE}"
_LINK_CLASS = "record-link"
_ERROR_FIELD = "_error"


class PossibleFusionPetBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["fusionKey"], "num", sort_key="fusion_key"),
            Column(cols["petId"], "num", sort_key="pet_id"),
            Column(cols["pet"], sort_key="pet_name"),
            Column(cols["species"], "num", sort_key="species"),
            Column(cols["variant"], "num", sort_key="variant"),
            Column(cols["tier"], "num", sort_key="tier"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # The file order: by fusion key, so the pets of one key sit together.
        return TableSort("fusion_key", SORT_ASC)

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_possiblefusionpet_records(data)
        except ValueError as ex:
            return [{_ERROR_FIELD: f"{FILE_NAME} could not be parsed: {ex}"}]
        return [{**record, "pet_name": character_name(record["pet_id"])} for record in records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and _ERROR_FIELD in records[0]:
            return error(records[0][_ERROR_FIELD])

        start = page * page_size
        rows = [
            [
                e(fusion_key_text(r["fusion_key"])),
                record_link(str(r["pet_id"]), _PET, "pet_id", r["pet_id"], _LINK_CLASS),
                e(r["pet_name"] or "-"),
                e(r["species"]),
                e(r["variant"]),
                e(handler_text(self.lang, _LANG_DIR, "tier", tier=r["tier"] + 1)),
            ]
            for r in records[start : start + page_size]
        ]
        keys = len({r["fusion_key"] for r in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), keys=keys)
        return table(meta, self._columns(), rows)
