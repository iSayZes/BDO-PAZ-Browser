from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from _common.lang import load_handler_strings
from _common.zodiacsign.loc import resolve_loc_type7
from _common.zodiacsign.parser import parse_zodiacsign_records
from .parser import parse_zodiacsignindex_records


_LANG_DIR = Path(__file__).parent / "lang"


class ZodiacSignIndexHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        if folder == entry.internal_path:
            return ["zodiacsign.dbss"]
        return [f"{folder}/zodiacsign.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        zodiacsign_raw = companions.get("zodiacsign.dbss")
        if zodiacsign_raw is None:
            raise ValueError("zodiacsign.dbss companion not found.")

        records = parse_zodiacsignindex_records(data)
        valid_ids = {rec["zodiac_id"] for rec in parse_zodiacsign_records(zodiacsign_raw)}
        loc_names, _ = resolve_loc_type7([rec["zodiac_id"] for rec in records])

        result: list[dict] = []
        for rec in records:
            zodiac_id = rec["zodiac_id"]
            result.append({
                "slot": rec["slot"],
                "zodiac_id": zodiac_id,
                "name": loc_names.get(zodiac_id, f"#{zodiac_id}"),
                "known": zodiac_id in valid_ids,
            })

        return result

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} zodiac index entries"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("zodiacId", "Zodiac ID"), "num", ""),
            (cols.get("name", "Name"), "", ""),
        ]
        rows = [
            [e(r["zodiac_id"]), e(r["name"])]
            for r in slice_
        ]
        return table(meta, headers, rows)
