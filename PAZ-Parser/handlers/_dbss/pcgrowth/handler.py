from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.class_type import LOC_CLASS
from _common.html import Column, e, flag_cell, sort_keys, table
from _common.item_key import item_key_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_tagged
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.pa_text import pa_fields, pa_line_cell
from _bss.pcgrowthsimply.parser import parse_pcgrowthsimply_records
from .combat_types import combat_type_text
from .parser import parse_pcgrowth_records, parse_pcgrowthoffset_records
from .text import class_display_name


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "pcgrowthoffset.dbss"
_SIMPLY_FILE = "pcgrowthsimply.bss"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 3
# LOC type 21 `str_id4` 1 is the class selection description.
_LOC_CLASS_DESCRIPTION = 1
_GENDER_KEYS = {0: "male", 1: "female"}


def pc_growth_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("class_type", "classType"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_pcgrowthoffset_records,
    )


def _text_fields(record: dict) -> dict:
    """Class name, combat type and description in the loaded LOC language; the
    name and description fall back to the inline Korean."""
    class_type = record["class_type"]
    description = loc_tagged(LOC_CLASS, class_type, _LOC_CLASS_DESCRIPTION) or record["description_kr"]
    return {
        "class_name": class_display_name(class_type, record["name_kr"]),
        "combat_type_name": combat_type_text(record["combat_type"]),
        **pa_fields("description", description),
    }


class PcGrowthHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["classType"], "num", sort_key="class_type"),
            Column(cols["className"], sort_key="class_name"),
            Column(cols["characterKey"], "num", sort_key="character_key"),
            Column(cols["gender"], sort_key="gender"),
            Column(cols["playable"], sort_key="is_playable"),
            Column(cols["combatType"], sort_key="combat_type"),
            Column(cols["starterWeapons"]),
            Column(cols["classWeapons"]),
            Column(cols["selectMovie"], sort_key="select_movie"),
            Column(cols["description"], sort_key="description"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}", f"{folder}/{_SIMPLY_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        simply_raw = companions.get(_SIMPLY_FILE)
        # Without pcgrowthsimply.bss the Playable column shows a dash.
        playable = (
            {row["class_type"]: row["is_playable"] for row in parse_pcgrowthsimply_records(simply_raw)}
            if simply_raw
            else {}
        )
        return [
            {**record, **_text_fields(record), "is_playable": playable.get(record["class_type"])}
            for record in parse_pcgrowth_records(data, offset_raw)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        strings = load_handler_strings(self.lang, _LANG_DIR)
        genders = strings["gender"]
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["class_type"]),
                e(r["class_name"] or _EMPTY),
                e(r["character_key"]),
                e(genders.get(_GENDER_KEYS.get(r["gender"], ""), r["gender"])),
                _EMPTY if r["is_playable"] is None else flag_cell(r["is_playable"]),
                e(r["combat_type_name"]),
                item_key_list_cell(r["starter_weapons"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                item_key_list_cell([w for w in r["class_weapons"] if w], _LIST_PREVIEW_ITEMS) or _EMPTY,
                e(r["select_movie"] or _EMPTY),
                pa_line_cell(r, "description"),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
