from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from _common.lang import load_handler_strings
from .parser import parse_offset_records, parse_plantzone_records


_LANG_DIR = Path(__file__).parent / "lang"


class PlantZoneOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_offset_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} offset records"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("offsetColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("recordId", "Record ID"), "num", ""),
            (cols.get("dataOffset", "Data Offset"), "num", ""),
            (cols.get("dataSize", "Data Size"), "num", ""),
        ]
        rows = [
            [
                e(r["record_id"]),
                e(f"0x{r['data_offset']:08X}"),
                e(r["data_size"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)


class PlantZoneHandler(PreviewHandler):
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
        return parse_plantzone_records(data, offset_raw)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} plant zone records"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("zoneId", "Zone ID"), "num", ""),
            (cols.get("variant", "Variant"), "num", ""),
            (cols.get("linkedId", "Linked ID"), "num", ""),
            (cols.get("values", "Values"), "", ""),
            (cols.get("dataSize", "Data Size"), "num", ""),
        ]
        rows = [
            [
                e(r["record_id"]),
                e(r["variant"]),
                e(r["linked_id"]),
                e(", ".join(str(v) for v in r["values"])),
                e(r["data_size"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)
