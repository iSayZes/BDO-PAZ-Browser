from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from ..common.html import e, error, table
from .parser import (
    parse_mentalcard_offset_records,
    parse_mentalcard_records,
)


_OFFSET_HEADERS: list[tuple[str, str, str]] = [
    ("Internal ID",  "num", ""),
    ("DBSS Offset",  "num", ""),
]

_CARD_HEADERS: list[tuple[str, str, str]] = [
    ("Knowledge ID",    "num", ""),
    ("Knowledge Name",  "",    ""),
    ("Category ID",     "num", ""),
    ("Category Name",   "",    ""),
]


class MentalCardOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = parse_mentalcard_offset_records(data)
        return [
            {"internal_id": internal_id, "dbss_offset": dbss_offset}
            for row, dbss_offset, size, internal_id in records
        ]

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
            [e(r["internal_id"]), e(f"0x{r['dbss_offset']:08X}")]
            for r in slice_
        ]
        return table(meta, _OFFSET_HEADERS, rows)


class MentalCardHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/mentalcardoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("mentalcardoffset.dbss")
        if offset_raw is None:
            raise ValueError("mentalcardoffset.dbss companion not found.")

        records = parse_mentalcard_records(data, offset_raw)
        return [
            {
                "entry_id":   record["entry_id"],
                "entry_name": record["entry_name"] or "",
                "node_id":    record["node_id"],
                "node_name":  record["node_name"] or "",
            }
            for record in records
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]

        with_entry_name = sum(1 for r in records if r["entry_name"])
        with_node_name  = sum(1 for r in records if r["node_name"])
        meta = (
            f"{len(records):,} mentalcard records"
            f" · {with_entry_name:,} entry names · {with_node_name:,} node names"
        )

        rows = [
            [
                e(r["entry_id"]),
                e(r["entry_name"] or "—"),
                e(r["node_id"]),
                e(r["node_name"] or "—"),
            ]
            for r in slice_
        ]
        return table(meta, _CARD_HEADERS, rows)
