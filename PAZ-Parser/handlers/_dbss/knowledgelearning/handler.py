from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from ..common.html import e, table
from .parser import (
    parse_knowledgelearning_offset_records,
    parse_knowledgelearning_records,
)


_OFFSET_HEADERS: list[tuple[str, str, str]] = [
    ("Idx ID",      "num", ""),
    ("Kind",        "num", ""),
    ("DBSS Offset", "num", ""),
]

_LEARNING_HEADERS: list[tuple[str, str, str]] = [
    ("Knowledge ID",    "num", ""),
    ("Kind",            "num", ""),
    ("Knowledge Name",  "",    ""),
    ("Offset",          "num", ""),
]


class KnowledgeLearningOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = parse_knowledgelearning_offset_records(data)
        return [
            {"idx_id": rec["idx_id"], "kind": rec["kind"], "offset": rec["offset"]}
            for rec in records
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
            [e(r["idx_id"]), e(r["kind"]), e(f"0x{r['offset']:08X}")]
            for r in slice_
        ]
        return table(meta, _OFFSET_HEADERS, rows)


class KnowledgeLearningHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/knowledgelearningoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("knowledgelearningoffset.dbss")
        if offset_raw is None:
            raise ValueError("knowledgelearningoffset.dbss companion not found.")

        records = parse_knowledgelearning_records(data, offset_raw)
        return [
            {
                "knowledge_id":   record["knowledge_id"] or "",
                "kind":           record["kind"],
                "knowledge_name": record["knowledge_name"] or "",
                "offset":         record["offset"],
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

        with_knowledge_name = sum(1 for r in records if r["knowledge_name"])
        meta = (
            f"{len(records):,} records"
            f" · {with_knowledge_name:,} knowledge names"
        )

        rows = [
            [
                e(r["knowledge_id"] or "—"),
                e(r["kind"]),
                e(r["knowledge_name"] or "—"),
                e(f"0x{r['offset']:08X}"),
            ]
            for r in slice_
        ]
        return table(meta, _LEARNING_HEADERS, rows)
