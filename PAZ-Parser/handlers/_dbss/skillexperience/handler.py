from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from .parser import LevelTable, parse_level_offset_records, parse_level_records


_LANG_DIR = Path(__file__).parent / "lang"
_EXP_FIELD = "exp"


def level_offset_handler() -> OffsetTableHandler:
    """The offset companion of any skill point EXP table: level, offset, size."""
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("level", "level"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_level_offset_records,
    )


class LevelExpHandler(PreviewHandler):
    """One skill point EXP table; `table` names its files and row fields."""

    def __init__(self, table: LevelTable) -> None:
        self._table = table

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["exp"], "num", sort_key=_EXP_FIELD),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{self._table.offset_file}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(self._table.offset_file)
        if offset_raw is None:
            raise ValueError(f"{self._table.offset_file} companion not found.")
        return parse_level_records(self._table, data, offset_raw)

    def _row(self, record: dict) -> list[str]:
        return [e(record["level"]), e(f"{record[_EXP_FIELD]:,}")]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [self._row(record) for record in records[start : start + page_size]]
        return table(meta, self._columns(), rows)
