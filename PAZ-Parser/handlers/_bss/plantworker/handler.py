from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, icon_cell, table
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from .parser import parse_plantworker_records


_LANG_DIR = Path(__file__).parent / "lang"


def _worker_name(worker_id: int) -> str:
    if not is_loc_loaded():
        return ""
    return strip_pa_tags(loc_lookup(6, worker_id))


class PlantWorkerBssHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []
        for record in parse_plantworker_records(data):
            row = dict(record)
            row["name"] = _worker_name(record["worker_id"])
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
        named = sum(1 for record in records if record.get("name"))
        meta = f"{len(records):,} worker records"
        if named:
            meta += f" · {named:,} with LOC names"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("workerId", "Worker ID"), "num", ""),
            (cols.get("icon", "Icon"), "", ""),
            (cols.get("name", "Name"), "", ""),
            (cols.get("nextWorkerId", "Next Tier"), "num", ""),
            (cols.get("moveSpeed", "Move"), "num", ""),
            (cols.get("stamina", "Stamina"), "num", ""),
            (cols.get("luck", "Luck"), "num", ""),
            (cols.get("baseWorkSpeed", "Work Speed"), "num", ""),
        ]

        rows = [
            [
                e(record["worker_id"]),
                icon_cell(record.get("icon_path") or f"#{record['icon_index']}"),
                e(record.get("name") or "-"),
                e(record["next_worker_id"] or "-"),
                e(record["move_speed"]),
                e(record["stamina"]),
                e(record["luck"]),
                e(record["base_work_speed"]),
            ]
            for record in slice_
        ]

        return table(meta, headers, rows)
