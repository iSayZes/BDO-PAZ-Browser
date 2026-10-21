"""actionverificationindex.dbss and actionverificationindexoffset.dbss preview handlers."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.class_type import class_name
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from .parser import (
    parse_actionverificationindex_records,
    parse_actionverificationindexoffset_records,
)


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "actionverificationindexoffset.dbss"


def action_verification_index_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("class_type", "classType"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_actionverificationindexoffset_records,
    )


class ActionVerificationIndexHandler(PreviewHandler):
    """Class type of every record; the bytes after it stay on the record as `unknown_01`."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["classType"], "num", sort_key="class_type"),
            Column(cols["className"], sort_key="class_name"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_data = companions.get(_OFFSET_FILE)
        if offset_data is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        return [
            {**record, "class_name": class_name(record["class_type"])}
            for record in parse_actionverificationindex_records(data, offset_data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [e(r["class_type"]), e(r["class_name"])]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
