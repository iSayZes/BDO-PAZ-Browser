from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from .parser import parse_planttown_records


_LANG_DIR = Path(__file__).parent / "lang"


def _node_name(node_id: int) -> str:
    if not is_loc_loaded():
        return ""

    return strip_pa_tags(loc_lookup(29, node_id)).strip()


class PlantTownBssHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []

        for record in parse_planttown_records(data):
            row = dict(record)
            row["node_name"] = _node_name(record["node_id"])
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
        meta = f"{len(records):,} plant town records"
        if named:
            meta += f" · {named:,} LOC names"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("nodeId", "Node ID"), "num", ""),
            (cols.get("nodeName", "Node Name"), "", ""),
        ]

        rows = [
            [
                e(record["node_id"]),
                e(record.get("node_name") or record["node_id"]),
            ]
            for record in slice_
        ]

        return table(meta, headers, rows)
