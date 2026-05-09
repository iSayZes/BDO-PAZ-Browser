from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from _common.lang import load_handler_strings
from _common.loc import is_loc_loaded
from _common.quest.quest import quest_title
from .parser import parse_newquest_records


_LANG_DIR = Path(__file__).parent / "lang"


class NewQuestBssHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []
        has_loc = is_loc_loaded()

        for record in parse_newquest_records(data):
            row = dict(record)
            row["title"] = (
                quest_title(record["quest_chain_id"], record["quest_id"])
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
        group_count = len({record["group"] for record in records})
        meta = f"{len(records):,} quest references · {group_count:,} groups"
        if with_titles:
            meta += f" · {with_titles:,} with LOC titles"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("group", "Group"), "num", ""),
            (cols.get("mainId", "Main ID"), "num", ""),
            (cols.get("subId", "Sub ID"), "num", ""),
            (cols.get("title", "Title"), "", ""),
            (cols.get("sequenceA", "Sequence A"), "num", ""),
            (cols.get("sequenceB", "Sequence B"), "num", ""),
            (cols.get("sequenceC", "Sequence C"), "num", ""),
        ]
        rows = [
            [
                e(record["group"]),
                e(record["quest_chain_id"]),
                e(record["quest_id"]),
                e(record.get("title") or "-"),
                e(record["sequence_a"]),
                e(record["sequence_b"]),
                e(record["sequence_c"]),
            ]
            for record in slice_
        ]

        return table(meta, headers, rows)
