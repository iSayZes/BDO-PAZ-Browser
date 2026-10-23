"""tooltiptable.dbss preview handler: the skill and item tooltip lines with their effect icons."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, text_list_cell
from _common.lang import load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column
from _common.pa_text import pa_fields, pa_line_cell
from _common.row_table import RowTableHandler
from table_sort import SORT_ASC, TableSort
from .parser import FILE_NAME, icon_bits, parse_tooltip_offset_rows, parse_tooltip_records
from .text import tooltip_text


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# Icons shown before the cell cuts the list.
_MAX_ICONS = 4


def tooltip_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("tooltip_type", "type"),
            OffsetColumn("key_hash", "keyHash"),
            offset_column("data_offset", "dataOffset"),
        ],
        parse_tooltip_offset_rows,
    )


def _icon_names(icon_flags: int, labels: Mapping[str, str]) -> list[str]:
    """The name of every icon bit set, or the bit number for a bit the lang file does not name."""
    return [labels.get(str(bit), str(bit)) for bit in icon_bits(icon_flags)]


class TooltipTableHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def default_sort(self) -> TableSort | None:
        """By tooltip type; the stable sort keeps the file order within a type."""
        return TableSort("tooltip_type", SORT_ASC)

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["keyHash"], "num", sort_key="key_hash"),
            Column(labels["type"], "num", sort_key="tooltip_type"),
            Column(labels["text"], sort_key="text"),
            Column(labels["paramCount"], "num", sort_key="param_count"),
            Column(labels["icons"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        icon_labels = load_handler_strings(self.lang, _LANG_DIR)["icons"]
        return [
            {
                **record,
                **pa_fields("text", tooltip_text(record["key_hash"], record["tooltip_type"], record["format_kr"])),
                "icons": _icon_names(record["icon_flags"], icon_labels),
            }
            for record in parse_tooltip_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["key_hash"]),
            e(record["tooltip_type"]),
            pa_line_cell(record, "text"),
            e(record["param_count"]),
            text_list_cell(record["icons"], _MAX_ICONS) or _EMPTY,
        ]
