from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from .parser import parse_questgroup_records


_HEADERS: list[tuple[str, str, str]] = [
    ("Group ID", "num", ""),
    ("Name", "", ""),
    ("Quests", "num", ""),
    ("Quest IDs", "", ""),
    ("Group:No", "", ""),
]


def _join_limited(values: list[str], max_items: int = 8) -> str:
    if len(values) <= max_items:
        return ", ".join(values)
    return ", ".join(values[:max_items]) + f", ... (+{len(values) - max_items})"


class QuestGroupDbssHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []

        for record in parse_questgroup_records(data):
            quest_ids = [quest["quest_id"] for quest in record["quests"]]
            quest_links = [
                f"{quest['group_id']}:{quest['quest_no']}"
                for quest in record["quests"]
            ]
            records.append(
                {
                    "row": record["row"],
                    "offset": record["offset"],
                    "size": record["size"],
                    "group_id": record["group_id"],
                    "name_kr": record["name_kr"],
                    "quest_count": record["quest_count"],
                    "quest_ids": quest_ids,
                    "quest_links": quest_links,
                    "quest_ids_text": ", ".join(str(quest_id) for quest_id in quest_ids),
                    "quest_links_text": ", ".join(quest_links),
                }
            )

        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start:start + page_size]
        total_links = sum(r["quest_count"] for r in records)
        meta = f"{len(records):,} quest groups · {total_links:,} quest links"
        rows = [
            [
                e(r["group_id"]),
                e(r["name_kr"]),
                e(r["quest_count"]),
                e(_join_limited([str(quest_id) for quest_id in r["quest_ids"]])),
                e(_join_limited(r["quest_links"])),
            ]
            for r in slice_
        ]
        return table(meta, _HEADERS, rows)
