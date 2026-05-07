from __future__ import annotations

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from _common.binary import u32
from _common.html import e, table

_RECORD_SIZE = 8  # u32 title_id + u32 category_id

_CATEGORIES: dict[int, str] = {
    0: "World",
    1: "Combat",
    2: "Life Skill",
    3: "Fishing",
}

_HEADERS = [
    ("Title ID", "num", ""),
    ("Cat ID",   "num", ""),
    ("Category", "",    ""),
]


def _parse(data: bytes) -> list[tuple[int, int]]:
    count = len(data) // _RECORD_SIZE
    return [
        (u32(data, i * _RECORD_SIZE), u32(data, i * _RECORD_SIZE + 4))
        for i in range(count)
    ]


class TitleCategoryBssHandler(PreviewHandler):
    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict]:
        return [
            {"title_id": title_id, "category_id": category_id}
            for title_id, category_id in _parse(data)
        ]

    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = f"{len(records):,} records"
        rows = [
            [
                e(r["title_id"]),
                e(r["category_id"]),
                e(_CATEGORIES.get(r["category_id"], f"Unknown ({r['category_id']})")),
            ]
            for r in slice_
        ]
        return table(meta, _HEADERS, rows)
