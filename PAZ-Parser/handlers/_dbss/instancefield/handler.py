from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.instancefieldmapinfo.titles import instance_field_title
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from .parser import parse_instancefield_records, parse_instancefieldoffset_records


_LANG_DIR = Path(__file__).parent / "lang"
_AXES = ("x", "y", "z")
_EMPTY = "-"


def _sector_range(record: dict, axis: str) -> str:
    """`46..52`: the box's sector span on one axis."""
    return f"{record[f'min_{axis}']}..{record[f'max_{axis}']}"


def instance_field_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("key", "key"),
            offset_column("offset", "byteOffset"),
            size_column("size", "size"),
        ],
        parse_instancefieldoffset_records,
    )


class InstanceFieldHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["title"], sort_key="title"),
            # Each span sorts by its lower bound.
            *(Column(cols[f"sector{axis.upper()}"], "num", sort_key=f"min_{axis}") for axis in _AXES),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            # None without a map info title, so the column sorts it last.
            {**record, "title": instance_field_title(record["key"]) or None}
            for record in parse_instancefield_records(data)
        ]

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
                e(r["key"]),
                e(r["name"]),
                e(r["title"] or _EMPTY),
                *(e(_sector_range(r, axis)) for axis in _AXES),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
