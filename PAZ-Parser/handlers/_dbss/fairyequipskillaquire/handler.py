from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from _common.lang import load_handler_strings
from .parser import (
    parse_fairyequipskillaquire_records,
    parse_fairyequipskillaquireoffset_records,
)


_LANG_DIR = Path(__file__).parent / "lang"


class FairyEquipSkillAcquireOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_fairyequipskillaquireoffset_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
        ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        cols = load_handler_strings(self.lang, _LANG_DIR).get("offsetColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("acquireTypeId", "Acquire Type ID"), "num", ""),
            (cols.get("dataOffset", "Data Offset"), "num", ""),
            (cols.get("dataSize", "Data Size"), "num", ""),
            (cols.get("recordStart", "Record Start"), "num", ""),
        ]
        rows = [
            [
                e(r["acquire_type_id"]),
                e(f"0x{r['data_offset']:08X}"),
                e(r["data_size"]),
                e(f"0x{r['record_start']:08X}"),
            ]
            for r in slice_
        ]
        return table(f"{len(records):,} fairy acquire offset records", headers, rows)


class FairyEquipSkillAcquireHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/fairyequipskillaquireoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("fairyequipskillaquireoffset.dbss")
        if offset_raw is None:
            raise ValueError("fairyequipskillaquireoffset.dbss companion not found.")

        return parse_fairyequipskillaquire_records(data, offset_raw)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} fairy acquire cost records"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("acquireTypeId", "Acquire Type ID"), "num", ""),
            (cols.get("activeEntries", "Active Entries"), "num", ""),
            (cols.get("maxCost", "Max Cost"), "num", ""),
            (cols.get("costTable", "Cost Table"), "", ""),
        ]
        rows = [
            [
                e(r["acquire_type_id"]),
                e(r["active_entry_count"]),
                e(r["max_cost"]),
                e(r["cost_table"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)
