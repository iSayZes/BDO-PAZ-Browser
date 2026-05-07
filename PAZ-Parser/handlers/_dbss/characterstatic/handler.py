from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from _common.html import e, table, error
from .parser import (
    parse_characterstaticoffset_records,
    parse_characterstatic_records,
)

_OFFSET_HEADERS: list[tuple[str, str, str]] = [
    ("ID Low16",    "num", ""),
    ("Byte Offset", "num", ""),
    ("Size",        "num", ""),
]

_STATIC_HEADERS_BASE: list[tuple[str, str, str]] = [
    ("Character ID",  "num", ""),
    ("Script",        "",    ""),
    ("Knowledge ID",  "num", ""),
    ("Payload Size",  "num", ""),
    ("Unknown Type",  "num", ""),
]


class CharacterStaticOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_characterstaticoffset_records(data)

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
            [e(r["id_low16"]), e(f"0x{r['offset']:08X}"), e(r["size"])]
            for r in slice_
        ]
        return table(meta, _OFFSET_HEADERS, rows)


class CharacterStaticHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [
            f"{folder}/characterstaticoffset.dbss",
            f"{folder}/languagedata_en.loc",
        ]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("characterstaticoffset.dbss")
        if not offset_raw:
            return [{"_error": "characterstaticoffset.dbss companion not found"}]

        offset_records = parse_characterstaticoffset_records(offset_raw)
        raw_records = parse_characterstatic_records(data, offset_records)
        loc = is_loc_loaded()

        result: list[dict] = []
        for r in raw_records:
            name = ""
            if loc:
                raw_name = loc_lookup(6, r["character_id"])
                name = strip_pa_tags(raw_name) if raw_name else ""
            result.append(
                {
                    "character_id": r["character_id"],
                    "name_en": name,
                    "script": r["script"],
                    "knowledge_id": r["knowledge_id"],
                    "payload_size": r["payload_size"],
                    "unknown_type": r["unknown_type"],
                }
            )
        return result

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        has_loc = is_loc_loaded()

        headers: list[tuple[str, str, str]] = [("Character ID", "num", "")]
        if has_loc:
            headers.append(("Name (EN)", "", ""))
        headers += _STATIC_HEADERS_BASE[1:]

        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} records"

        rows: list[list[str]] = []
        for r in slice_:
            row: list[str] = [e(r["character_id"])]
            if has_loc:
                row.append(e(r["name_en"]))
            row.append(e(r["script"]))
            row.append(e(r["knowledge_id"]) if r["knowledge_id"] is not None else "")
            row.append(e(r["payload_size"]))
            row.append(e(r["unknown_type"]))
            rows.append(row)

        return table(meta, headers, rows)
