"""vehicleskillcount.dbss preview handler: the bound of the mount and ship skill keys."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import FILE_NAME, parse_vehicleskillcount_record


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _highest_key(count: int) -> int | None:
    """The highest skill key `count` stands for, or None when there are no skills."""
    return count - 1 if count > 0 else None


class VehicleSkillCountHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["count"], "num", sort_key="count"),
            Column(cols["highestKey"], "num", sort_key="highest_key"),
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
            record = parse_vehicleskillcount_record(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [{**record, "highest_key": _highest_key(record["count"])}]

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
                e(r["count"]),
                e(_EMPTY if r["highest_key"] is None else r["highest_key"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.summary")
        return table(meta, self._columns(), rows)
