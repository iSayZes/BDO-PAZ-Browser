"""The shared preview handler of a table with one record per row.

Most `.dbss` tables with an `*offset.dbss` index are a u32 row count and the
rows; the index (`offset_table.py`, `keyed_offset_handler()`) only says where
each row sits. A format subclasses `RowTableHandler` with three parts:

- `read_records()`: the parser's records, joined with any companions. A
  `ValueError` becomes an error page that names the file.
- `columns()`: the columns, from the `columns` block of the format's
  `lang/<lang>.json`; `sortable_fields()` follows from them.
- `cells()`: the HTML cells of one record.

The count line above the table is the `meta.count` text of the same file.
`counted_rows.parse_counted_rows()` reads the common case of rows that all
have one size; tables with strings or lists in their rows walk them with
`record_reader.RecordReader` and use the handler all the same.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings

# The record that stands in for the rows when the file does not parse.
ERROR_FIELD = "_error"


class RowTableHandler(PreviewHandler):
    """A table of one record per row; see the module docstring.

    Subclasses set `file_name` and `lang_dir` as class attributes.
    """

    file_name: str
    lang_dir: Path

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        """Every record, in file order. Raises ValueError when the file does not parse."""
        raise NotImplementedError

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        """The table's columns, labelled from the `columns` block of the lang file."""
        raise NotImplementedError

    def cells(self, record: dict) -> list[str]:
        """One HTML cell per column."""
        raise NotImplementedError

    def _columns(self) -> list[Column]:
        return self.columns(load_handler_strings(self.lang, self.lang_dir)["columns"])

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            return self.read_records(data, companions)
        except ValueError as ex:
            return [{ERROR_FIELD: f"{self.file_name} could not be parsed: {ex}"}]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and ERROR_FIELD in records[0]:
            return error(records[0][ERROR_FIELD])

        start = page * page_size
        rows = [self.cells(record) for record in records[start : start + page_size]]
        meta = handler_text(self.lang, self.lang_dir, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
