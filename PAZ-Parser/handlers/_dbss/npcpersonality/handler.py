from __future__ import annotations

import html

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.loc import loc_lookup
from .parser import parse_npcpersonality_records, parse_npcpersonalityoffset_records


def _e(value: object) -> str:
    return html.escape(str(value))


def _decode_personality_type(code: int) -> str:
    major = code // 100
    name = loc_lookup(7, major)
    return name if name else f"?{major}"


def _group_cell(group_id: int, item_count: int) -> str:
    if group_id == 0:
        return "—"
    return _e(f"{group_id} ×{item_count}")


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


def _table_raw(meta: str, headers: list[tuple[str, str]], rows: list[list[str]]) -> str:
    """Like _table but cells are already-escaped HTML strings."""
    head = "".join(
        f'<th class="{_e(css_class)} sortable">{_e(label)}</th>'
        for label, css_class in headers
    )

    body = "".join(
        "<tr>"
        + "".join(
            f'<td class="{_e(headers[index][1])}">{cell}</td>'
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


def _error(text: str) -> str:
    return f'<div class="error">{_e(text)}</div>'


class NpcPersonalityOffsetHandler(PreviewHandler):
    def render(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> str:
        try:
            records = parse_npcpersonalityoffset_records(data)
        except Exception as exc:
            return _error(f"Failed to parse npcpersonalityoffset.dbss: {exc}")

        if not records:
            return _error("npcpersonalityoffset.dbss: no records found.")

        headers = [
            ("Personality ID", "num"),
            ("Data Offset", "num"),
        ]

        rows = [
            [
                rec["personality_id"],
                f"0x{rec['data_offset']:08X}",
            ]
            for rec in records
        ]

        meta = f"{len(records):,} offset records · {len(data):,} B"
        return _table(meta, headers, rows)


class NpcPersonalityHandler(PreviewHandler):
    def render(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> str:
        try:
            records = parse_npcpersonality_records(data)
        except Exception as exc:
            return _error(f"Failed to parse npcpersonality.dbss: {exc}")

        if not records:
            return _error("npcpersonality.dbss: no records found.")

        headers = [
            ("Row", "num"),
            ("ID", "num"),
            ("Group A (ID ×cnt)", "num"),
            ("Group B (ID ×cnt)", "num"),
            ("Group C (ID ×cnt)", "num"),
            ("Int Min", "num"),
            ("Int Max", "num"),
            ("Fav Min", "num"),
            ("Fav Max", "num"),
            ("Horoscope", ""),
        ]

        rows: list[list[str]] = [
            [
                _e(rec["row"]),
                _e(rec["personality_id"]),
                _group_cell(rec["group_a_id"], rec["group_a_count"]),
                _group_cell(rec["group_b_id"], rec["group_b_count"]),
                _group_cell(rec["group_c_id"], rec["group_c_count"]),
                _e(int(rec["interest_min"])),
                _e(int(rec["interest_max_excl"])),
                _e(int(rec["favor_min"])),
                _e(int(rec["favor_max_excl"])),
                _e(_decode_personality_type(rec["personality_type"])),
            ]
            for rec in records
        ]

        meta = f"{len(records):,} personality records · {len(data):,} B"
        return _table_raw(meta, headers, rows)
