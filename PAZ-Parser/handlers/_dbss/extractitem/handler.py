"""extractitem.dbss preview handler: Extract Reform Stone rows in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_u32_offset_rows
from _dbss.itemimprovement.parser import FILE_NAME as REFORM_FILE, SOURCE_FILE as STONE_FILE
from .parser import parse_extractitem_records
from .reform_group import ReformGroupLookup, reform_group_lookup


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# The four item slots of a row: the ID field and the name field added for search and sort.
_ITEM_FIELDS = (
    ("item_id", "item_name"),
    ("need_item_id", "need_item_name"),
    ("result_item_id", "result_item_name"),
    ("result_material_id", "result_material_name"),
)


def extract_item_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("item_id", "itemId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "item_id"),
    )


def _display_record(record: dict, reform_group: ReformGroupLookup) -> dict:
    """The row plus each slot's item name (the ID when it has none), for
    search and sort, and the reform group it undoes (None sorts last, as the
    dash of a row without one)."""
    return {
        **record,
        **{name_field: item_key_text(record[id_field]) for id_field, name_field in _ITEM_FIELDS},
        "reform_group": reform_group(record),
    }


def _item_cell(item_id: int) -> str:
    """The item with its icon and grade colour."""
    return item_key_list_cell([item_id], 1)


class ExtractItemHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["needItem"], sort_key="need_item_name"),
            Column(cols["resultItem"], sort_key="result_item_name"),
            Column(cols["resultMaterial"], sort_key="result_material_name"),
            Column(cols["reformGroup"], "num", sort_key="reform_group"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{REFORM_FILE}", f"{folder}/{STONE_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        reform_group = reform_group_lookup(companions.get(REFORM_FILE), companions.get(STONE_FILE))
        return [_display_record(record, reform_group) for record in parse_extractitem_records(data)]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        rows = [
            [
                e(r["item_id"]),
                *(_item_cell(r[id_field]) for id_field, _ in _ITEM_FIELDS),
                e(r["reform_group"]) if r["reform_group"] is not None else _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
