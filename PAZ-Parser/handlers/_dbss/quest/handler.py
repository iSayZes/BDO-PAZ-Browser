from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.loc import is_loc_loaded, loc_lookup_prefix, strip_pa_tags

from ..common.html import e, table
from .parser import QuestIndex, build_quest_index, parse_quest_record, parse_quest_records


_HEADERS: list[tuple[str, str, str]] = [
    ("Quest ID", "num", ""),
    ("Title / Name", "", ""),
    ("Condition", "", ""),
    ("Action", "", ""),
    ("Objective", "", ""),
    ("Icon", "", ""),
]


def _truncate(text: str, max_len: int = 140) -> str:
    return text if len(text) <= max_len else text[:max_len] + "..."


def _quest_loc_texts(quest_id: int) -> list[str]:
    if not is_loc_loaded():
        return []

    seen: set[str] = set()
    texts: list[str] = []
    for text in loc_lookup_prefix(39, quest_id):
        clean = strip_pa_tags(text).strip()
        if clean and clean not in seen:
            seen.add(clean)
            texts.append(clean)
    return texts


class QuestDbssHandler(PreviewHandler):
    _index: QuestIndex | None = None
    _index_data_id: int | None = None

    def supports_lazy_records(self) -> bool:
        return True

    def _get_index(self, data: bytes) -> QuestIndex:
        data_id = id(data)
        if self._index is None or self._index_data_id != data_id:
            self._index = build_quest_index(data)
            self._index_data_id = data_id
        return self._index

    def get_record_count(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> int:
        return len(self._get_index(data).starts)

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = []
        for record in parse_quest_records(data):
            record["loc_texts_en"] = _quest_loc_texts(record["quest_id"])
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
        end_row = min(len(index.starts), start_row + page_size)
        records: list[dict] = []

        for row in range(start_row, end_row):
            start = index.starts[row]
            end = index.starts[row + 1] if row + 1 < len(index.starts) else len(data)
            quest_id = int.from_bytes(data[start:start + 4], "little")
            record = parse_quest_record(
                data,
                row,
                start,
                end,
                loc_texts=_quest_loc_texts(quest_id),
            )
            if record is not None:
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
        total = len(self._get_index(data).starts)
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
        for row, start in enumerate(index.starts):
            end = index.starts[row + 1] if row + 1 < len(index.starts) else len(data)
            quest_id = int.from_bytes(data[start:start + 4], "little")
            record = parse_quest_record(
                data,
                row,
                start,
                end,
                loc_texts=_quest_loc_texts(quest_id),
            )
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

    def _render_table(self, records: list[dict], total: int) -> str:
        rows: list[list] = []
        with_loc = 0

        for record in records:
            loc_texts = record.get("loc_texts_en", [])
            if loc_texts:
                with_loc += 1
            title = loc_texts[0] if loc_texts else ""
            objective = loc_texts[1] if len(loc_texts) > 1 else ""
            if not objective:
                objective = record["objective_text_kr"]

            rows.append([
                e(record["quest_id"]),
                e(_truncate(title) if title else "-"),
                e(_truncate(record["condition_script"])),
                e(_truncate(record["action_script"])),
                e(_truncate(objective) if objective else "-"),
                e(record["icon_path"] or "-"),
            ])

        meta = f"{total:,} quests"
        if with_loc:
            meta += f" · {with_loc:,} with LOC type 39 text"

        return table(meta, _HEADERS, rows)
