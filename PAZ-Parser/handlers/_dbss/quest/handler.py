from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags

from _common.html import e, table
from _common.lang import load_handler_strings
from .parser import QuestIndex, build_quest_index, parse_quest_record


_LANG_DIR = Path(__file__).parent / "lang"


def _truncate(text: str, max_len: int = 140) -> str:
    return text if len(text) <= max_len else text[:max_len] + "..."


def _quest_loc_texts(quest_chain_id: int, quest_id: int) -> list[str]:
    if not is_loc_loaded():
        return []

    seen: set[str] = set()
    texts: list[str] = []
    for str_id4 in range(10):
        text = loc_lookup(18, quest_chain_id, quest_id, 0, str_id4)
        clean = strip_pa_tags(text).strip()
        if clean and clean not in seen:
            seen.add(clean)
            texts.append(clean)
    return texts


class QuestDbssHandler(PreviewHandler):

    def _get_index(self, data: bytes) -> QuestIndex:
        return self._data_cache(data, "index", lambda: build_quest_index(data))

    def get_record_count(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> int:
        return len(self._get_index(data).record_starts)

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = []
        index = self._get_index(data)
        for row, start in enumerate(index.record_starts):
            canonical_id = index.canonical_quest_ids[row] if row < len(index.canonical_quest_ids) else 0
            if start is None:
                records.append(self._partial_record(row, index, canonical_id))
                continue

            record = parse_quest_record(data, row, start, index.record_ends[row], canonical_id)
            if record is not None:
                record["loc_texts_en"] = _quest_loc_texts(record["quest_chain_id"], record["quest_id"])
                records.append(dict(record))
        return records

    def _records_for_page(
        self,
        data: bytes,
        page: int,
        page_size: int,
    ) -> list[dict]:
        index = self._get_index(data)
        start_row = page * page_size
        end_row = min(len(index.record_starts), start_row + page_size)
        records: list[dict] = []

        for row in range(start_row, end_row):
            canonical_id = index.canonical_quest_ids[row] if row < len(index.canonical_quest_ids) else 0
            start = index.record_starts[row]
            if start is None:
                records.append(self._partial_record(row, index, canonical_id))
                continue

            record = parse_quest_record(
                data,
                row,
                start,
                index.record_ends[row],
                canonical_id,
            )
            if record is not None:
                record["loc_texts_en"] = _quest_loc_texts(record["quest_chain_id"], record["quest_id"])
                records.append(dict(record))

        return records

    def render_data_page(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
        page: int,
        page_size: int,
    ) -> str:
        total = len(self._get_index(data).record_starts)
        return self._render_table(self._records_for_page(data, page, page_size), total)

    def search_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
        query: str,
    ) -> list[int]:
        q = query.lower()
        if not q:
            return []

        matches: list[int] = []
        index = self._get_index(data)
        for row, start in enumerate(index.record_starts):
            canonical_id = index.canonical_quest_ids[row] if row < len(index.canonical_quest_ids) else 0
            if start is None:
                record = self._partial_record(row, index, canonical_id)
                if q in "\t".join(str(value).lower() for value in record.values()):
                    matches.append(row)
                continue

            record = parse_quest_record(
                data,
                row,
                start,
                index.record_ends[row],
                canonical_id,
            )
            if record:
                record["loc_texts_en"] = _quest_loc_texts(record["quest_chain_id"], record["quest_id"])
            if record and q in "\t".join(str(value).lower() for value in record.values()):
                matches.append(row)

        return matches

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        return self._render_table(records[page * page_size : page * page_size + page_size], len(records))

    def _partial_record(self, row: int, index: QuestIndex, canonical_id: int = 0) -> dict:
        cid = canonical_id or 0
        chain_id = cid & 0xFFFF
        quest_id  = cid >> 16
        loc_texts = _quest_loc_texts(chain_id, quest_id) if cid else []
        return {
            "row": row,
            "offset": "",
            "size": "",
            "packed_quest_id": cid or "",
            "quest_chain_id": chain_id or "",
            "quest_id": quest_id or "",
            "condition_script": "",
            "action_script": "",
            "objective_text_kr": "",
            "icon_path": index.icon_paths[row] if row < len(index.icon_paths) else "",
            "loc_texts_en": loc_texts,
            "parse_status": "Icon-only",
        }

    def _render_table(self, records: list[dict], total: int) -> str:
        rows: list[list] = []
        with_loc = 0

        for record in records:
            loc_texts = record.get("loc_texts_en", [])
            if loc_texts:
                with_loc += 1
            title = loc_texts[0] if loc_texts else ""
            objective = loc_texts[3] if len(loc_texts) > 3 else ""
            if not objective:
                objective = record["objective_text_kr"]

            rows.append([
                e(record["packed_quest_id"]),
                e(record["quest_chain_id"]),
                e(record["quest_id"]),
                e(_truncate(title) if title else "-"),
                e(_truncate(record["condition_script"])),
                e(_truncate(record["action_script"])),
                e(_truncate(objective) if objective else "-"),
                e(record["icon_path"] or "-"),
            ])

        meta = f"{total:,} quests"
        if with_loc:
            meta += f" · {with_loc:,} with LOC type 18 text"
        icon_only = sum(1 for record in records if record.get("parse_status") == "Icon-only")
        if icon_only:
            meta += f" · {icon_only:,} icon-only on this page"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("displayId", "Display ID"), "num", ""),
            (cols.get("chainId", "Chain ID"), "num", ""),
            (cols.get("questId", "Quest ID"), "num", ""),
            (cols.get("titleName", "Title / Name"), "", ""),
            (cols.get("condition", "Condition"), "", ""),
            (cols.get("action", "Action"), "", ""),
            (cols.get("objective", "Objective"), "", ""),
            (cols.get("icon", "Icon"), "", ""),
        ]
        return table(meta, headers, rows)
