"""contentsgroupoptionstaticstatusmanager.bss preview handler."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, flag_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import FILE_NAME, parse_contentsgroupoption_records


_LANG_DIR = Path(__file__).parent / "lang"


def _group_number(key: str) -> int | None:
    """The decimal key as a number, so the column sorts 2 before 10."""
    return int(key) if key.isdecimal() else None


class ContentsGroupOptionBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["contentsGroup"], "num", sort_key="contents_group_number"),
            Column(cols["isOpen"], sort_key="is_open"),
            Column(cols["keyHash"], "num", sort_key="key_hash"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_contentsgroupoption_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {**record, "contents_group_number": _group_number(record["contents_group_key"])}
            for record in records
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        rows = [
            [
                e(r["contents_group_key"]),
                flag_cell(r["is_open"]),
                e(f"0x{r['key_hash']:08X}"),
            ]
            for r in records[start : start + page_size]
        ]
        open_count = sum(1 for r in records if r["is_open"])
        meta = handler_text(
            self.lang, _LANG_DIR, "meta.count", count=len(records), open=open_count
        )
        return table(meta, self._columns(), rows)
