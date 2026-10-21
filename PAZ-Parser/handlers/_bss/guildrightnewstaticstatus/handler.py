from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import parse_guild_right_records


_LANG_DIR = Path(__file__).parent / "lang"


class GuildRightNewStaticStatusBssHandler(PreviewHandler):
    """One row per guild right, with its group; the names are the file's Korean text."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["rightNo"], "num", sort_key="right_no"),
            Column(cols["right"], sort_key="name_kr"),
            Column(cols["groupNo"], "num", sort_key="group_no"),
            Column(cols["group"], sort_key="group_name_kr"),
            Column(cols["description"], sort_key="description_kr"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_guild_right_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["right_no"]),
                e(r["name_kr"]),
                e(r["group_no"]),
                e(r["group_name_kr"]),
                e(r["description_kr"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
