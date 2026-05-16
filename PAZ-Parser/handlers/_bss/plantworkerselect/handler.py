from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from _bss.plantworker.parser import parse_plantworker_records
from .parser import parse_plantworkerselect_records


_LANG_DIR = Path(__file__).parent / "lang"


def _loc_text(str_type: int, str_id1: int) -> str:
    if not is_loc_loaded():
        return ""

    return strip_pa_tags(loc_lookup(str_type, str_id1)).strip()


def _plantworker_index(companions: dict[str, bytes]) -> dict[int, dict]:
    raw = companions.get("plantworker.bss")
    if raw is None:
        return {}

    return {
        record["worker_id"]: record
        for record in parse_plantworker_records(raw)
    }


class PlantWorkerSelectBssHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/plantworker.bss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        workers = _plantworker_index(companions)
        records: list[dict] = []

        for record in parse_plantworkerselect_records(data):
            row = dict(record)
            worker = workers.get(row["worker_id"], {})
            row["selection_name"] = (
                _loc_text(17, row["selection_id"]) or str(row["selection_id"])
            )
            row["worker_name"] = _loc_text(6, row["worker_id"])
            row["worker_icon_path"] = worker.get("icon_path", "")
            row["worker_move_speed"] = worker.get("move_speed")
            row["worker_stamina"] = worker.get("stamina")
            row["worker_luck"] = worker.get("luck")
            row["worker_base_work_speed"] = worker.get("base_work_speed")
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
        named = sum(
            1
            for record in records
            if record.get("selection_name") or record.get("worker_name")
        )

        meta = f"{len(records):,} worker selection records"
        if named:
            meta += f" · {named:,} with LOC names"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("selectionId", "Selection ID"), "num", ""),
            (cols.get("selectionName", "Selection Name"), "", ""),
            (cols.get("workerId", "Worker ID"), "num", ""),
            (cols.get("workerName", "Worker Name"), "", ""),
            (cols.get("hireCost", "Hire Cost"), "num", ""),
        ]

        rows = [
            [
                e(record["selection_id"]),
                e(record.get("selection_name") or record["selection_id"]),
                e(record["worker_id"]),
                e(record.get("worker_name") or "-"),
                e(record["hire_cost"]),
            ]
            for record in slice_
        ]

        return table(meta, headers, rows)
