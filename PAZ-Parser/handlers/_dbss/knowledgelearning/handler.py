from __future__ import annotations

import html
from collections import Counter

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from .parser import (
    parse_knowledgelearning_offset_records,
    parse_knowledgelearning_records,
)


def _e(value: object) -> str:
    return html.escape(str(value))


def _error(text: str) -> str:
    return f'<div class="error">{_e(text)}</div>'


def _table(meta: str, headers: list[tuple[str, str]], rows: list[list[object]]) -> str:
    head = "".join(
        f'<th class="{_e(css_class)} sortable">{_e(label)}</th>'
        for label, css_class in headers
    )

    body = "".join(
        "<tr>"
        + "".join(
            f'<td class="{_e(headers[index][1])}">{_e(cell)}</td>'
            for index, cell in enumerate(row)
        )
        + "</tr>"
        for row in rows
    )

    return (
        f'<div class="table-meta">{_e(meta)}</div>'
        '<div class="table-wrap">'
        '<table class="data-table">'
        f"<thead><tr>{head}</tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table>"
        "</div>"
    )


class KnowledgeLearningOffsetHandler(PreviewHandler):
    def render(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> str:
        records = parse_knowledgelearning_offset_records(data)

        if not records and len(data) < 12:
            return _error("knowledgelearningoffset.dbss is too small.")

        meta = (
            f"{len(records):,} offset records · {len(data):,} B"
        )



        headers = [
            ("Row", "num"),
            ("DBSS Offset", "num"),
            ("Kind", "num"),
            ("Idx ID", "num"),
        ]

        rows = [
            [
                record["row"],
                f"0x{record['offset']:08X}",
                record["kind"],
                record["idx_id"],
            ]
            for record in records
        ]

        return _table(meta, headers, rows)


class KnowledgeLearningHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]

        return [f"{folder}/knowledgelearningoffset.dbss"]

    def render(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> str:
        offset_raw = companions.get("knowledgelearningoffset.dbss")

        if offset_raw is None:
            return _error("knowledgelearningoffset.dbss companion not found.")

        records = parse_knowledgelearning_records(data, offset_raw)

        with_knowledge_name = sum(1 for record in records if record["knowledge_name"])

        meta = (
            f"{len(records):,} records · {len(data):,} B"
            f" · {with_knowledge_name:,} knowledge names"
        )

        headers = [
            ("Row", "num"),
            ("Offset", "num"),
            ("Kind", "num"),
            ("Knowledge ID", "num"),
            ("Knowledge Name", ""),
        ]

        rows = [
            [
                record["row"],
                f"0x{record['offset']:08X}",
                record["kind"],
                record["knowledge_id"] or "—",
                record["knowledge_name"] or "—",
            ]
            for record in records
        ]

        return _table(meta, headers, rows)