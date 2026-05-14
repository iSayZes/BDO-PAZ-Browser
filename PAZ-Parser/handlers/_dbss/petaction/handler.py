from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, icon_cell, table
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from .parser import parse_petaction_records, parse_petactionoffset_records


_LANG_DIR = Path(__file__).parent / "lang"


class PetActionOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_petactionoffset_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} pet action offset records"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("offsetColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("actionId", "Action ID"), "num", ""),
            (cols.get("recordOffset", "Record Offset"), "num", ""),
            (cols.get("recordSize", "Record Size"), "num", ""),
        ]
        rows = [
            [
                e(r["action_id"]),
                e(f"0x{r['record_offset']:08X}"),
                e(r["record_size"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)


class PetActionHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [
            f"{folder}/petactionoffset.dbss",
            f"{folder}/languagedata_en.loc",
        ]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("petactionoffset.dbss")
        if offset_raw is None:
            raise ValueError("petactionoffset.dbss companion not found.")
        records = parse_petaction_records(data, offset_raw)
        has_loc = is_loc_loaded()
        for record in records:
            icon_action_name = record["action_name"]
            record["icon_action_name"] = icon_action_name
            loc_name = ""
            if has_loc:
                loc_name = strip_pa_tags(loc_lookup(19, record["action_id"])).strip()
            record["action_name"] = loc_name or icon_action_name
        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        groups = len({r["action_group"] for r in records})
        meta = f"{len(records):,} pet actions · {groups:,} groups"
        with_loc = sum(1 for r in records if r["action_name"] != r["icon_action_name"])
        if with_loc:
            meta += f" · {with_loc:,} with LOC type 19 names"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("actionId", "Action ID"), "num", ""),
            (cols.get("icon", "Icon"), "", ""),
            (cols.get("actionName", "Action Name"), "", ""),
            (cols.get("group", "Group"), "num", ""),
        ]
        rows = [
            [
                e(r["action_id"]),
                icon_cell(r["icon_path"]),
                e(r["action_name"]),
                e(r["action_group"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)
