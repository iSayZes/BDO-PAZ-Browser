from __future__ import annotations

import html

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from .parser import (
    parse_mentalcard_offset_records,
    parse_mentalcard_records,
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


class MentalCardOffsetHandler(PreviewHandler):
    def render(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> str:
        records = parse_mentalcard_offset_records(data)

        if not records and len(data) < 12:
            return _error("mentalcardoffset.dbss is too small.")

        headers = [
            ("Internal ID", "num"),
            ("DBSS Offset", "num"),
        ]

        rows = [
            [
                internal_id,
                f"0x{dbss_offset:08X}",

            ]
            for row, dbss_offset, size, internal_id in records
        ]

        meta = f"{len(records):,} offset records · {len(data):,} B"

        return _table(meta, headers, rows)


class MentalCardHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]

        return [f"{folder}/mentalcardoffset.dbss"]

    def render(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> str:
        offset_raw = companions.get("mentalcardoffset.dbss")

        if offset_raw is None:
            return _error("mentalcardoffset.dbss companion not found.")

        records = parse_mentalcard_records(data, offset_raw)

        with_entry_name = sum(1 for record in records if record["entry_name"])
        with_node_name = sum(1 for record in records if record["node_name"])

        meta = (
            f"{len(records):,} mentalcard records · {len(data):,} B"
            f" · {with_entry_name:,} entry names · {with_node_name:,} node names"
        )

        headers = [
            ("Knowledge ID", "num"),
            ("Knowledge Name", ""),
            ("Category ID", "num"),
            ("Category Name", ""),
        ]

        rows = [
            [
                record["entry_id"],
                record["entry_name"] or "—",
                record["node_id"],
                record["node_name"] or "—",
            ]
            for record in records
        ]

        return _table(meta, headers, rows)