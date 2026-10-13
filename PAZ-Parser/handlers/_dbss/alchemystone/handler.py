"""The table both alchemy stone material files show, and their offset index.

A row is a stone type, a material item and one value per material; each
format names that value and labels its column. Every other label (columns,
stone type names, the offset index, the count line) lives in this package's
`lang/` folder.
"""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import SORT_ASC, TableSort

from _common.html import Column, e, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_name_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.pa_text import pa_cell, pa_fields
from .grouped import parse_stone_offset_records

_LANG_DIR = Path(__file__).parent / "lang"

ParseRecords = Callable[[bytes], list[dict]]


def stone_type_name(lang: str, stone_type: int) -> str:
    """The alchemy stone type's name, or its number when it has none."""
    names = load_handler_strings(lang, _LANG_DIR)["stoneTypes"]
    return names.get(str(stone_type), str(stone_type))


def stone_offset_handler(file_name: str) -> OffsetTableHandler:
    """The handler of an alchemy stone `*offset.dbss` index named `file_name`."""
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("stone_type", "stoneType"),
            OffsetColumn("item_id", "itemId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        lambda data: parse_stone_offset_records(data, file_name),
    )


class StoneMaterialHandler(PreviewHandler):
    """Stone type, item and one value column, opened sorted by stone type.

    `lang_dir` is the format's own folder; its `columns.<value_label>` labels
    the value column.
    """

    def __init__(
        self,
        lang_dir: Path,
        parse: ParseRecords,
        value_field: str,
        value_label: str,
        value_text: Callable[[int], str] = str,
    ) -> None:
        self._lang_dir = lang_dir
        self._parse = parse
        self._value_field = value_field
        self._value_label = value_label
        self._value_text = value_text

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        value_label = load_handler_strings(self.lang, self._lang_dir)["columns"][self._value_label]
        return [
            Column(cols["stoneType"], sort_key="stone_type"),
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
            Column(value_label, "num", sort_key=self._value_field),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # Destruction first; each stone type keeps the file's material order.
        return TableSort("stone_type", SORT_ASC)

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {
                **record,
                "stone_type_name": stone_type_name(self.lang, record["stone_type"]),
                **pa_fields("item_name", item_name_tagged(record["item_id"])),
                "icon_path": icon_path(IconKind.ITEM, record["item_id"]),
            }
            for record in self._parse(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            types=len({record["stone_type"] for record in records}),
        )
        rows = [
            [
                e(r["stone_type_name"]),
                e(r["item_id"]),
                icon_cell(r["icon_path"]),
                pa_cell(r, "item_name") if r["item_name"] else e(r["item_id"]),
                e(self._value_text(r[self._value_field])),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
