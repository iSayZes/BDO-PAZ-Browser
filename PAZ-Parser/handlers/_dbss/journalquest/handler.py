from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from .parser import parse_journalquest_offset_records, parse_journalquest_records


_LANG_DIR = Path(__file__).parent / "lang"


def _page_title(journal_cat_id: int, page_no: int) -> str:
    return strip_pa_tags(loc_lookup(18, journal_cat_id, page_no, 0, 0)).strip()


def _journal_text(group_id: int, entry_no: int, field_id: int) -> str:
    return strip_pa_tags(loc_lookup(63, group_id, entry_no, 0, field_id)).strip()


def _join_limited(values: list[str], max_items: int = 6) -> str:
    if len(values) <= max_items:
        return ", ".join(values)
    return ", ".join(values[:max_items]) + f", ... (+{len(values) - max_items})"


class JournalQuestOffsetHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_journalquest_offset_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        groups = len({r["group_id"] for r in records})
        meta = f"{len(records):,} entries · {groups:,} groups"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("offsetColumns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("group", "Group"), "num", ""),
            (cols.get("entry", "Entry"), "num", ""),
            (cols.get("offset", "Offset"), "num", ""),
            (cols.get("size", "Size"), "num", ""),
        ]
        rows = [
            [
                e(r["group_id"]),
                e(r["entry_no"]),
                e(f"0x{r['byte_offset']:08X}"),
                e(r["byte_size"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)


class JournalQuestDbssHandler(PreviewHandler):
    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/journalquestoffset.dbss"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("journalquestoffset.dbss")
        if offset_raw is None:
            raise ValueError("journalquestoffset.dbss companion not found - cannot parse records.")

        records = parse_journalquest_records(data, offset_raw)
        has_loc = is_loc_loaded()

        for record in records:
            title_en = _journal_text(record["group_id"], record["entry_no"], 0) if has_loc else ""
            subtitle_en = _journal_text(record["group_id"], record["entry_no"], 1) if has_loc else ""
            unlock_en = _journal_text(record["group_id"], record["entry_no"], 2) if has_loc else ""
            volume_en = _journal_text(record["group_id"], record["entry_no"], 3) if has_loc else ""
            page_titles: list[str] = []
            for page_ref in record["page_refs"]:
                if has_loc:
                    title = _page_title(page_ref["journal_cat_id"], page_ref["page_no"])
                else:
                    title = ""
                page_titles.append(title or f"{page_ref['journal_cat_id']}:{page_ref['page_no']}")
            record["journal_title_en"] = title_en
            record["subtitle_en"] = subtitle_en
            record["page_vol_title_en"] = volume_en
            record["unlock_condition_en"] = unlock_en
            record["journal_title_text"] = title_en or record["journal_title"]
            record["subtitle_text"] = subtitle_en or record["subtitle"]
            record["page_vol_title_text"] = volume_en or record["page_vol_title"]
            record["unlock_condition_text"] = unlock_en or strip_pa_tags(record["unlock_condition"])
            record["page_titles"] = page_titles
            record["page_titles_text"] = ", ".join(page_titles)

        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        pages = sum(r["page_count"] for r in records)
        groups = len({r["group_id"] for r in records})
        meta = f"{len(records):,} journal entries · {groups:,} groups · {pages:,} pages"
        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("group", "Group"), "num", ""),
            (cols.get("entry", "Entry"), "num", ""),
            (cols.get("journalCategoryId", "Journal Category ID"), "num", ""),
            (cols.get("title", "Title"), "", ""),
            (cols.get("subtitle", "Subtitle"), "", ""),
            (cols.get("volume", "Volume"), "", ""),
            (cols.get("pageTitles", "Page Titles"), "", ""),
            (cols.get("unlockCondition", "Unlock Condition"), "", ""),
            (cols.get("pages", "Pages"), "num", ""),
            (cols.get("combineModel", "Combine Model"), "", ""),
            (cols.get("staticModel", "Static Model"), "", ""),
        ]
        rows = [
            [
                e(r["group_id"]),
                e(r["entry_no"]),
                e(r["journal_cat_id"]),
                e(r["journal_title_text"]),
                e(r["subtitle_text"]),
                e(r["page_vol_title_text"]),
                e(_join_limited(r["page_titles"])),
                e(r["unlock_condition_text"]),
                e(r["page_count"]),
                e(r["combine_model"]),
                e(r["static_model"]),
            ]
            for r in slice_
        ]
        return table(meta, headers, rows)
