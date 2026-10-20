"""Preview of the small PABR option tables; one instance per file of `tables.py`.

Named fields get a column, with a resolved name next to a key that has one.
A file with no named field shows its raw value bytes instead.
"""

from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.binary import whole_float
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import parse_value_table, value_bytes
from .tables import ValueTable


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
VALUE_BYTES_FIELD = "value_bytes"


def _cell(value: object) -> str:
    if value == "":
        return _EMPTY
    return e(whole_float(value) if isinstance(value, float) else value)


class PabrValuesBssHandler(PreviewHandler):
    """One small PABR option table; the layout comes from its `ValueTable`."""

    def __init__(self, value_table: ValueTable) -> None:
        self._table = value_table

    def _shown_fields(self) -> list[tuple[str, Column]]:
        """Each shown record key with its column, in column order."""
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        if not self._table.has_named_field:
            return [(VALUE_BYTES_FIELD, Column(cols["valueBytes"], sort_key=VALUE_BYTES_FIELD))]
        shown: list[tuple[str, Column]] = []
        for field in self._table.fields:
            if field.column is None:
                continue
            shown.append((field.name, Column(cols[field.column], "num", sort_key=field.name)))
            if field.lookup is not None:
                name_key = field.lookup.field
                shown.append((name_key, Column(cols[field.lookup.column], sort_key=name_key)))
        return shown

    def _columns(self) -> list[Column]:
        return [column for _, column in self._shown_fields()]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = parse_value_table(data, self._table)
        if not self._table.has_named_field:
            raw = value_bytes(data, self._table.file_name)
            return [{**record, VALUE_BYTES_FIELD: raw} for record in records]
        lookups = [(field.name, field.lookup) for field in self._table.fields if field.lookup is not None]
        return [
            {**record, **{lookup.field: lookup.name_of(record[key]) for key, lookup in lookups}}
            for record in records
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        shown = self._shown_fields()
        rows = [[_cell(r[name]) for name, _ in shown] for r in records[start : start + page_size]]
        return table(meta, [column for _, column in shown], rows)
