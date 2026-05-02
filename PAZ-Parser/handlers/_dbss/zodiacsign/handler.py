from __future__ import annotations

import html

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.loc import loc_lookup, strip_pa_tags

from .parser import (
    parse_zodiacsign_records,
    parse_zodiacsignoffset_records,
    parse_zodiacsignorder_records,
    parse_zodiacsignorderoffset_records,
)


def _resolve_loc_type7(
    zodiac_ids: list[int],
) -> tuple[dict[int, str], dict[int, str]]:
    """Return (names, traits) keyed by zodiac_id using the module-level loc index."""
    names:  dict[int, str] = {}
    traits: dict[int, str] = {}
    for zid in zodiac_ids:
        name  = loc_lookup(7, zid, 0, 0, 0)
        trait = loc_lookup(7, zid, 0, 0, 1)
        if name:
            names[zid]  = name
        if trait:
            traits[zid] = strip_pa_tags(trait)
    return names, traits


def _e(value: object) -> str:
    return html.escape(str(value))


def _error(text: str) -> str:
    return f'<div class="error">{_e(text)}</div>'


def _table(meta: str, headers: list[tuple[str, str]], rows: list[list[object]]) -> str:
    head = "".join(
        f'<th class="{_e(cls)} sortable">{_e(label)}</th>'
        for label, cls in headers
    )
    body = "".join(
        "<tr>"
        + "".join(
            f'<td class="{_e(headers[i][1])}">{_e(cell)}</td>'
            for i, cell in enumerate(row)
        )
        + "</tr>"
        for row in rows
    )
    return (
        f'<div class="table-meta">{_e(meta)}</div>'
        '<div class="table-wrap"><table class="data-table">'
        f"<thead><tr>{head}</tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table></div>"
    )


def _truncate(text: str, max_len: int = 100) -> str:
    return text if len(text) <= max_len else text[:max_len] + "…"


class ZodiacSignHandler(PreviewHandler):
    def render(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> str:
        try:
            records = parse_zodiacsign_records(data)
        except Exception as exc:
            return _error(f"Failed to parse zodiacsign.dbss: {exc}")

        if not records:
            return _error("zodiacsign.dbss: no records found.")

        zodiac_ids = [rec["zodiac_id"] for rec in records]
        loc_names, loc_traits = _resolve_loc_type7(zodiac_ids)
        loc_ok = bool(loc_traits)

        headers = [
            ("ID", "num"),
            ("Name", ""),
            ("Stars", "num"),
            ("Pairs", "num"),
            ("Constellation", ""),
            ("Traits (EN)" if loc_ok else "Traits (KR)", ""),
        ]

        rows: list[list[object]] = []
        for rec in records:
            zid = rec["zodiac_id"]
            en_trait = loc_traits.get(zid)
            trait_display = (
                _truncate(en_trait) if en_trait else _truncate(rec["trait_text"], 60)
            )
            rows.append([
                zid,
                loc_names.get(zid, f"#{zid}"),
                rec["float_count"],
                rec["pairs_count"],
                rec["constellation_name"],
                trait_display,
            ])

        meta = f"{len(records):,} zodiac signs · {len(data):,} B"
        return _table(meta, headers, rows)


class ZodiacSignOffsetHandler(PreviewHandler):
    def render(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> str:
        try:
            records = parse_zodiacsignoffset_records(data)
        except Exception as exc:
            return _error(f"Failed to parse zodiacsignoffset.dbss: {exc}")

        if not records:
            return _error("zodiacsignoffset.dbss: no records found.")

        headers = [
            ("Zodiac ID", "num"),
            ("Data Offset", "num"),
        ]

        rows: list[list[object]] = [
            [
                rec["zodiac_id"],
                f"0x{rec['data_offset']:08X}",
            ]
            for rec in records
        ]

        meta = f"{len(records):,} offset records · {len(data):,} B"
        return _table(meta, headers, rows)


class ZodiacSignOrderHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/zodiacsignorderoffset.dbss"]

    def render(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> str:
        offset_raw = companions.get("zodiacsignorderoffset.dbss")
        if offset_raw is None:
            return _error("zodiacsignorderoffset.dbss companion not found.")

        try:
            records = parse_zodiacsignorder_records(data, offset_raw)
        except Exception as exc:
            return _error(f"Failed to parse zodiacsignorder.dbss: {exc}")

        if not records:
            return _error("zodiacsignorder.dbss: no records found.")

        headers = [
            ("Personality", "num"),
            ("Zodiac", ""),
            ("Variant", "num"),
            ("Triggers", "num"),
            ("Sequence", ""),
        ]

        unique_majors = list({rec["personality_type"] // 100 for rec in records})
        loc_names, _ = _resolve_loc_type7(unique_majors)

        rows: list[list[object]] = []
        for rec in records:
            pt = rec["personality_type"]
            major = pt // 100
            variant = pt % 100
            zodiac_name = loc_names.get(major, f"#{major}")
            sequence = "→".join(str(s) for s in rec["trigger_order"])
            rows.append([
                rec["row"],
                pt,
                zodiac_name,
                variant,
                rec["trigger_count"],
                sequence,
            ])

        meta = f"{len(records):,} order records · {len(data):,} B"
        return _table(meta, headers, rows)


class ZodiacSignOrderOffsetHandler(PreviewHandler):
    def render(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> str:
        try:
            records = parse_zodiacsignorderoffset_records(data)
        except Exception as exc:
            return _error(f"Failed to parse zodiacsignorderoffset.dbss: {exc}")

        if not records:
            return _error("zodiacsignorderoffset.dbss: no records found.")

        headers = [
            ("Personality Type", "num"),
            ("Data Offset", "num"),
        ]

        rows: list[list[object]] = [
            [
                rec["personality_type"],
                f"0x{rec['data_offset']:08X}",
            ]
            for rec in records
        ]

        meta = f"{len(records):,} offset records · {len(data):,} B"
        return _table(meta, headers, rows)
