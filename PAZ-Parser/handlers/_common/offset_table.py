"""One preview handler for offset companions: a key, a byte offset and a size per row.

Every `*offset.dbss` table lists where the records of its main file sit. A
format builds an `OffsetTableHandler` from its columns and a reader that turns
the file into records; the records keep the format's own field names, which
its parser, its tests and the CSV export share. Column labels come from the
format's `lang/<lang>.json` block (`offsetColumns` unless named otherwise).
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.binary import parse_offset_table
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.pabr_offset import PabrOffsetRow

ReadRecords = Callable[[bytes], list[dict]]
# The count line above the table, from the records and the UI language.
MetaText = Callable[[list[dict], str], str]

# Text every offset table shares.
_COMMON_LANG_DIR = Path(__file__).parent / "lang"


def offset_text(value: int) -> str:
    """A byte offset (or a hash key) as `0x0001A2B0`."""
    return f"0x{value:08X}"


def size_text(value: int) -> str:
    """A byte count as `1,024`."""
    return f"{value:,}"


@dataclass(frozen=True)
class OffsetColumn:
    """One column: the record field it shows and sorts by, its label key and cell text."""

    field: str
    label_key: str
    text: Callable[[int], str] = str


def offset_column(field: str, label_key: str) -> OffsetColumn:
    return OffsetColumn(field, label_key, offset_text)


def size_column(field: str, label_key: str) -> OffsetColumn:
    return OffsetColumn(field, label_key, size_text)


def offset_records(
    parse_rows: Callable[[bytes], list[PabrOffsetRow]],
    key_field: str,
    offset_field: str = "offset",
    size_field: str = "size",
) -> ReadRecords:
    """A reader that names the fields of shared offset rows (`_common/pabr_offset.py`)."""

    def read(data: bytes) -> list[dict]:
        return [
            {key_field: row.entry_id, offset_field: row.offset, size_field: row.size}
            for row in parse_rows(data)
        ]

    return read


def offset_map_records(key_field: str) -> ReadRecords:
    """A reader for `parse_offset_table()` files: key and offset rows in key order."""

    def read(data: bytes) -> list[dict]:
        return [
            {key_field: key, "offset": offset}
            for key, (offset, _size) in sorted(parse_offset_table(data).items())
        ]

    return read


def picked_records(
    parse: Callable[[bytes], Sequence[Mapping[str, object]]],
    fields: Sequence[str],
) -> ReadRecords:
    """A reader that keeps only `fields` of each parsed row, e.g. drops its row number."""

    def read(data: bytes) -> list[dict]:
        return [{field: row[field] for field in fields} for row in parse(data)]

    return read


def keyed_offset_handler(
    lang_dir: Path,
    parse_rows: Callable[[bytes], list[PabrOffsetRow]],
    key_field: str = "key",
    key_label: str = "key",
) -> OffsetTableHandler:
    """The usual index: `key_field`, `data_offset` and `data_size` per row, read by `parse_rows`.

    Labels come from `key_label`, `dataOffset` and `size` in the
    `offsetColumns` block of `lang_dir`.
    """
    return OffsetTableHandler(
        lang_dir,
        [
            OffsetColumn(key_field, key_label),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_rows, key_field, "data_offset", "data_size"),
    )


def count_meta(records: list[dict], lang: str) -> str:
    return handler_text(lang, _COMMON_LANG_DIR, "meta.offsetRecords", count=len(records))


class OffsetTableHandler(PreviewHandler):
    """Renders one offset companion; see the module docstring."""

    def __init__(
        self,
        lang_dir: Path,
        columns: Sequence[OffsetColumn],
        read_records: ReadRecords,
        *,
        lang_block: str = "offsetColumns",
        meta: MetaText = count_meta,
    ) -> None:
        self._lang_dir = lang_dir
        self._offset_columns = tuple(columns)
        self._read_records = read_records
        self._lang_block = lang_block
        self._meta = meta

    def _columns(self) -> list[Column]:
        labels = load_handler_strings(self.lang, self._lang_dir)[self._lang_block]
        return [
            Column(labels[column.label_key], "num", sort_key=column.field)
            for column in self._offset_columns
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return self._read_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        rows = [
            [e(column.text(record[column.field])) for column in self._offset_columns]
            for record in records[start : start + page_size]
        ]
        return table(self._meta(records, self.lang), self._columns(), rows)
