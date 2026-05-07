from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from _common.loc import is_loc_loaded, loc_lookup, strip_pa_tags
from .parser import parse_allquestlist_records


_HEADERS: list[tuple[str, str, str]] = [
    ("Main ID", "num", ""),
    ("Sub ID", "num", ""),
    ("Title", "", ""),
]


def _quest_title(quest_chain_id: int, quest_id: int) -> str:
    if not is_loc_loaded():
        return ""

    return strip_pa_tags(loc_lookup(18, quest_chain_id, quest_id, 0, 0)).strip()


class AllQuestListBssHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []
        has_loc = is_loc_loaded()

        for record in parse_allquestlist_records(data):
            row = dict(record)
            row["title"] = (
                _quest_title(record["quest_chain_id"], record["quest_id"])
                if has_loc
                else ""
            )
            records.append(row)

        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        with_titles = sum(1 for record in records if record.get("title"))
        meta = f"{len(records):,} quest list entries"
        if with_titles:
            meta += f" · {with_titles:,} with LOC titles"

        rows = [
            [
                e(record["quest_chain_id"]),
                e(record["quest_id"]),
                e(record.get("title") or "-"),
            ]
            for record in slice_
        ]

        return table(meta, _HEADERS, rows)
