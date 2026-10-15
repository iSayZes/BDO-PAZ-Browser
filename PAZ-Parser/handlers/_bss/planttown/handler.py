from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_text
from .parser import parse_planttown_records


_LANG_DIR = Path(__file__).parent / "lang"
# Node names are LOC type 29, keyed by node ID.
_NODE_LOC_TYPE = 29


class PlantTownBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["nodeId"], "num", sort_key="node_id"),
            Column(cols["nodeName"], sort_key="node_name"),
            Column(cols["maxLevel"], "num", sort_key="max_level"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []

        for record in parse_planttown_records(data):
            row = dict(record)
            row["node_name"] = loc_text(_NODE_LOC_TYPE, record["node_id"])
            records.append(row)

        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        named = sum(1 for record in records if record.get("node_name"))
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        if named:
            meta += handler_text(self.lang, _LANG_DIR, "meta.named", named=named)

        rows = [
            [
                e(record["node_id"]),
                e(record.get("node_name") or record["node_id"]),
                e(record["max_level"]),
            ]
            for record in slice_
        ]

        return table(meta, self._columns(), rows)
