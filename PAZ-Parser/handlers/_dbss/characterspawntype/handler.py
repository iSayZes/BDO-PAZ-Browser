from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from _common.html import e, table
from _common.lang import load_handler_strings
from .parser import (
    parse_characterspawntype_records,
    parse_characterspawntypeoffset_records,
)

_NUM_FLAGS = 44
_LANG_DIR = Path(__file__).parent / "lang"

_FLAG_NAMES: dict[int, str] = {
    1: "villa_vendor",
    12: "quest_variant",
    14: "battlefield_vendor",
    15: "wandering_merchant",
    18: "specialty_shop",
    22: "guild_vendor",
    30: "event_npc",
    32: "timed_spawn",
    43: "main_quest",
}

def _lookup_name(entity_id: int) -> str:
    name = loc_lookup(6, entity_id)
    if name:
        return strip_pa_tags(name)
    if entity_id >> 16:
        for t in (0, 50):
            name = loc_lookup(t, entity_id)
            if name:
                return strip_pa_tags(name)
    return ""


def _flag_header(idx: int) -> tuple[str, str, str]:
    name = _FLAG_NAMES.get(idx, "")
    extra = f'title="{name}"' if name else ""
    return (f"f{idx:02d}", "num", extra)


def _entity_id_cell(entity_id: int) -> str:
    return f'<span title="0x{entity_id:08X}">{e(entity_id)}</span>'


class CharacterSpawnTypeOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_characterspawntypeoffset_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} offset records"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("offsetColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("idLow16", "ID Low16"), "num", ""),
            (cols.get("byteOffset", "Byte Offset"), "num", ""),
            (cols.get("size", "Size"), "num", ""),
        ]
        rows = [
            [e(r["id_low16"]), e(f"0x{r['offset']:08X}"), e(r["size"])]
            for r in slice_
        ]
        return table(meta, headers, rows)


class CharacterSpawnTypeHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        raw = parse_characterspawntype_records(data)
        loc = is_loc_loaded()
        return [
            {
                "entity_id": r["entity_id"],
                "name_en": _lookup_name(r["entity_id"]) if loc else "",
                "flags": r["flags"],
            }
            for r in raw
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        active = [i for i in range(_NUM_FLAGS) if any(r["flags"][i] for r in records)]
        has_loc = is_loc_loaded()

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("entityId", "entity_id"), "num", "")
        ]
        if has_loc:
            headers.append((cols.get("nameEn", "Name (EN)"), "", ""))
        headers.extend(_flag_header(i) for i in active)

        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} records · {len(active)} active flag columns"

        rows = []
        for r in slice_:
            row = [_entity_id_cell(r["entity_id"])]
            if has_loc:
                row.append(e(r["name_en"]))
            for i in active:
                row.append("1" if r["flags"][i] else "")
            rows.append(row)

        return table(meta, headers, rows)
