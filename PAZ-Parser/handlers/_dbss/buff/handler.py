from __future__ import annotations

import re
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, icon_cell, table
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from _common.pabr_offset import parse_pabr_offset_rows
from .parser import parse_buff_records


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "buffoffset.dbss"

# English buff descriptions live in LOC type 5, keyed by buff ID.
_LOC_TYPE_BUFF_DESCRIPTION = 5
# LOC stores this literal for buffs that have no description.
_LOC_NULL = "<null>"

# "<PAColor0xffe9bd23>[Blessing] Adventure's Boon<PAOldColor>\n..."
_TITLE_LINE = re.compile(r"<PAColor0x[0-9a-fA-F]{8}>([^<\r\n]+)<PAOldColor>[ \t]*\r?\n")

_EMPTY = "-"
_SHOWN_PARAMS = 3


def format_duration(duration_ms: int) -> str:
    """Render milliseconds as "1h 30m", "45s" or "1.5s"; empty for zero."""
    if duration_ms <= 0:
        return ""

    seconds, millis = divmod(duration_ms, 1000)
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)

    parts: list[str] = []
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    if secs or millis:
        text = f"{secs}.{millis:03d}".rstrip("0").rstrip(".")
        parts.append(f"{text}s")
    return " ".join(parts)


def extract_title(raw_description: str) -> str:
    """Display name of a headline buff, or an empty string.

    About 2,000 shown buffs open their description with their name on a
    coloured line of its own, followed by the effects. A description that is
    only that one line is an effect, not a title, so it yields nothing.
    """
    match = _TITLE_LINE.match(raw_description)
    if not match or not raw_description[match.end():].strip():
        return ""
    return match.group(1).strip()


def _raw_description(buff_id: int, description_kr: str) -> str:
    """English description from LOC with PA tags intact, else the inline Korean."""
    if is_loc_loaded():
        english = loc_lookup(_LOC_TYPE_BUFF_DESCRIPTION, buff_id).strip()
        if english and english != _LOC_NULL:
            return english

    return description_kr


class BuffOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {"buff_id": row.entry_id, "offset": row.offset, "size": row.size}
            for row in parse_pabr_offset_rows(data)
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

        cols = load_handler_strings(self.lang, _LANG_DIR).get("offsetColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("buffId", "Buff ID"), "num", ""),
            (cols.get("dataOffset", "Data Offset"), "num", ""),
            (cols.get("size", "Size"), "num", ""),
        ]
        rows = [
            [e(r["buff_id"]), e(f"0x{r['offset']:08X}"), e(r["size"])]
            for r in slice_
        ]
        return table(meta, headers, rows)


class BuffHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_data = companions.get(_OFFSET_FILE)
        if not offset_data:
            raise ValueError(f"{_OFFSET_FILE} companion not found")

        records = parse_buff_records(data, parse_pabr_offset_rows(offset_data))
        for record in records:
            raw = _raw_description(record["buff_id"], record["description_kr"])
            record["title"] = extract_title(raw)
            record["description"] = strip_pa_tags(raw).strip()
            record["duration"] = format_duration(record["duration_ms"])
        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} buffs"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("buffId", "Buff ID"), "num", ""),
            (cols.get("icon", "Icon"), "", ""),
            (cols.get("title", "Title"), "", ""),
            (cols.get("name", "Internal Name"), "", ""),
            (cols.get("description", "Description"), "", ""),
            (cols.get("level", "Level"), "num", ""),
            (cols.get("effectType", "Effect Type"), "num", ""),
            (cols.get("duration", "Duration"), "num", ""),
        ]
        headers += [
            (cols.get(f"param{index}", f"Param {index}"), "num", "")
            for index in range(1, _SHOWN_PARAMS + 1)
        ]

        rows = [
            [
                e(r["buff_id"]),
                icon_cell(r["icon_path"]) if r["icon_path"] else _EMPTY,
                e(r["title"]) if r["title"] else _EMPTY,
                e(r["name"]),
                e(r["description"]) if r["description"] else _EMPTY,
                e(r["level"]),
                e(r["effect_type"]),
                e(r["duration"]) if r["duration"] else _EMPTY,
                *(e(r[f"param_{index}"]) for index in range(1, _SHOWN_PARAMS + 1)),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)
