from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import e, table
from _common.lang import load_handler_strings
from .parser import parse_fairyfeedenchantfailcount_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class FairyFeedEnchantFailCountBssHandler(PreviewHandler):
    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_fairyfeedenchantfailcount_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        groups = len({record["group_id"] for record in records})
        meta = f"{len(records):,} entries across {groups} groups"

        cols = load_handler_strings(self.lang, _LANG_DIR).get("columns", {})
        headers: list[tuple[str, str, str]] = [
            (cols.get("groupId", "Group ID"), "num", ""),
            (cols.get("subKey", "Sub Key"), "num", ""),
            (cols.get("valueA", "Value A"), "num", ""),
            (cols.get("valueB", "Value B"), "num", ""),
        ]

        rows = [
            [
                e(record["group_id"]),
                e(record["sub_key"] or _EMPTY),
                e(f"{record['value_a']:,}"),
                e(f"{record['value_b']:,}"),
            ]
            for record in slice_
        ]

        return table(meta, headers, rows)
