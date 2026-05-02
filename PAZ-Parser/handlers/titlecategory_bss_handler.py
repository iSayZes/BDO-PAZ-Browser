from __future__ import annotations

import html as _html
import struct
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from bdo_models import PazEntry
from bdo_preview import PreviewHandler, register_handler

_RECORD_SIZE = 8  # u32 title_id + u32 category_id

_CATEGORIES: dict[int, str] = {
    0: "World",
    1: "Combat",
    2: "Life Skill",
    3: "Fishing",
}


class TitleCategoryBssHandler(PreviewHandler):
    def render(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> str:
        records = _parse(data)
        meta    = f"{len(records):,} records  ·  {len(data):,} B"

        rows = []
        for title_id, category_id in records:
            cat_name = _CATEGORIES.get(category_id, f"Unknown ({category_id})")
            rows.append(
                f"<tr>"
                f"<td class='num'>{title_id}</td>"
                f"<td class='num'>{category_id}</td>"
                f"<td>{_html.escape(cat_name)}</td>"
                f"</tr>"
            )

        body = "".join(rows)
        return (
            f'<div class="table-meta">{_html.escape(meta)}</div>'
            f'<div class="table-wrap">'
            f'<table class="data-table">'
            f'<thead><tr>'
            f'<th class="num sortable">Title ID</th>'
            f'<th class="num sortable">Cat ID</th>'
            f'<th class="sortable">Category</th>'
            f'</tr></thead>'
            f'<tbody>{body}</tbody>'
            f'</table>'
            f'</div>'
        )


def _parse(data: bytes) -> list[tuple[int, int]]:
    count = len(data) // _RECORD_SIZE
    return [
        struct.unpack_from("<II", data, i * _RECORD_SIZE)
        for i in range(count)
    ]


register_handler("titlecategory.bss", TitleCategoryBssHandler())
