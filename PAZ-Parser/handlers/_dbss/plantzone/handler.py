from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from ..common.html import e, table
from .parser import parse_offset_records, parse_plantzone_records


_OFFSET_HEADERS: list[tuple[str, str, str]] = [
    ("Record ID",   "num", ""),
    ("Data Offset", "num", ""),
    ("Data Size",   "num", ""),
]

_PLANTZONE_HEADERS: list[tuple[str, str, str]] = [
    ("Zone ID",   "num", ""),
    ("Variant",   "num", ""),
    ("Linked ID", "num", ""),
    ("Values",    "",    ""),
    ("Data Size", "num", ""),
]


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
        rows = [
            [
                e(r["record_id"]),
                e(f"0x{r['data_offset']:08X}"),
                e(r["data_size"]),
            ]
            for r in slice_
        ]
        return table(meta, _OFFSET_HEADERS, rows)


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
        return table(meta, _PLANTZONE_HEADERS, rows)
