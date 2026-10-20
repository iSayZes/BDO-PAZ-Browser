"""itemequipgroup.bss preview handler: each equipment group's items."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from .parser import FILE_NAME, parse_itemequipgroup_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 8


class ItemEquipGroupBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["groupKey"], "num", sort_key="group_key"),
            Column(cols["itemCount"], "num", sort_key="item_count"),
            # A list column: it would only sort by its string form.
            Column(cols["items"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            groups = parse_itemequipgroup_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        # Item names as text, so tab search and CSV export see them.
        return [
            {**group, "items": [item_key_text(item_id) for item_id in group["item_ids"]]}
            for group in groups
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            items=sum(record["item_count"] for record in records),
        )
        rows = [
            [
                e(record["group_key"]),
                e(record["item_count"]),
                item_key_list_cell(record["item_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for record in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
