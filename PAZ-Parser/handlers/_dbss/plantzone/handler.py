from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.enum_name import enum_name
from _common.html import Column, e, sort_keys, table
from _common.item_key import item_key_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.node import node_name
from _common.production_items import production_item_fields, production_luck_item_fields
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.work_ani_type import WORK_ANI_TYPE_NAMES
from .parser import (
    WORKER_SPECIES_NAMES,
    parse_offset_records,
    parse_plantzone_records,
)


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 8


def plant_zone_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("record_id", "recordId"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_offset_records,
    )


class PlantZoneHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["zoneId"], "num", sort_key="record_id"),
            Column(cols["nodeName"], sort_key="node_name"),
            Column(cols["workAnimation"], sort_key="work_animation"),
            Column(cols["productionKey"], "num", sort_key="production_key"),
            # List columns: they would only sort by their string form.
            Column(cols["producedItems"]),
            Column(cols["luckItems"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/plantzoneoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("plantzoneoffset.dbss")
        if offset_raw is None:
            raise ValueError("plantzoneoffset.dbss companion not found.")

        return [
            {
                **record,
                **production_item_fields(record["production_key"]),
                **production_luck_item_fields(record["production_key"]),
                "node_name": node_name(record["record_id"]),
                "work_animation": enum_name(WORK_ANI_TYPE_NAMES, record["work_ani_type"]),
                # Not shown: the list is not a worker lock and its use is
                # unknown. Kept for search and export.
                "worker_species_text": ", ".join(
                    enum_name(WORKER_SPECIES_NAMES, species) for species in record["worker_species"]
                ),
            }
            for record in parse_plantzone_records(data, offset_raw)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        resolved = sum(1 for record in records if record["item_keys"] is not None)
        luck = sum(1 for record in records if record["luck_item_keys"] is not None)
        meta = handler_text(
            self.lang, _LANG_DIR, "meta.count", count=len(records), resolved=resolved, luck=luck,
        )
        rows = [
            [
                e(r["record_id"]),
                e(r["node_name"] or _EMPTY),
                e(r["work_animation"]),
                e(r["production_key"]),
                item_key_list_cell(r["item_keys"] or [], _LIST_PREVIEW_ITEMS) or _EMPTY,
                item_key_list_cell(r["luck_item_keys"] or [], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)
