"""Preview handlers for the pet look table and its offset index.

One row per look. The Pets column lists the `pet.dbss` pets whose
`change_look_key` is the row's key; the Skill column names the look's skill
by its LOC type 10 name.
"""

from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, icon_cell, record_link, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.skill import skill_name
from _dbss.pet.joins import PET_FILE, pet_companion_paths, pet_ids_by, pet_names_text
from .parser import FILE_NAME, parse_petchangelook_records, parse_petchangelookoffset_records


_LANG_DIR = Path(__file__).parent / "lang"
_PET = f"gamecommondata/binary/{PET_FILE}"
_LINK_CLASS = "record-link"
_ERROR_FIELD = "_error"


def pet_change_look_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("change_look_key", "lookKey"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        parse_petchangelookoffset_records,
    )


def _change_look_key(pet: dict) -> int:
    return pet["change_look_key"]


class PetChangeLookHandler(PreviewHandler):
    """`petchangelook.dbss`: the looks of each look key, with their icons, skill and skin name."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["lookKey"], "num", sort_key="change_look_key"),
            Column(cols["pets"], sort_key="pet_names"),
            Column(cols["actionIndex"], "num", sort_key="action_index"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["icon1"], sort_key="icon_path_1"),
            Column(cols["icon2"], sort_key="icon_path_2"),
            Column(cols["skill"], sort_key="skill_name"),
            Column(cols["skinName"], sort_key="skin_name_kr"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        return pet_companion_paths(entry.internal_path.rsplit("/", 1)[0])

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            looks = parse_petchangelook_records(data)
            pets_by_look = pet_ids_by(companions, _change_look_key)
        except ValueError as ex:
            return [{_ERROR_FIELD: f"{FILE_NAME} could not be parsed: {ex}"}]
        return [
            {
                **look,
                "pet_names": pet_names_text(pets_by_look.get(look["change_look_key"], [])),
                "skill_name": skill_name(look["skill_no"]) if look["skill_no"] else "",
            }
            for look in looks
        ]

    def _skill_cell(self, record: dict) -> str:
        if not record["skill_no"]:
            return "-"
        return e(record["skill_name"] or record["skill_no"])

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
                record_link(str(r["change_look_key"]), _PET, "change_look_key", r["change_look_key"], _LINK_CLASS),
                e(r["pet_names"] or "-"),
                e(r["action_index"]),
                icon_cell(r["icon_path"]),
                icon_cell(r["icon_path_1"]),
                icon_cell(r["icon_path_2"]),
                self._skill_cell(r),
                e(r["skin_name_kr"] or "-"),
            ]
            for r in records[start : start + page_size]
        ]
        keys = len({r["change_look_key"] for r in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), keys=keys)
        return table(meta, self._columns(), rows)
