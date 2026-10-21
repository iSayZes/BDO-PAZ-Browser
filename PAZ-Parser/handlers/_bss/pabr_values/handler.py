"""Preview of the small option tables; one instance per file of `tables.py`.

Named fields get a column, with an icon and a resolved name next to a key
that has them, and a string-table index shows its string. A file with no
named field shows each row's raw bytes instead.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any, NamedTuple

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.binary import whole_float
from _common.html import Column, e, html_list_cell, icon_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_cell, pa_fields
from .parser import parse_value_rows, parse_value_table
from .layout import IconLookup, NameLookup, TextRef, ValueField, ValueTable


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
VALUE_BYTES_FIELD = "value_bytes"

Cell = Callable[[dict], str]


class _Shown(NamedTuple):
    """One column and how a record's cell reads."""

    column: Column
    cell: Cell


def _cell(value: object, display: Callable[[Any], str] | None = None) -> str:
    """The cell text of a value: `display` of a number or an entry list when the field has one."""
    if display is not None and isinstance(value, (int, list)):
        return e(display(value))
    if value == "":
        return _EMPTY
    return e(whole_float(value) if isinstance(value, float) else value)


def _value_cell(field: ValueField) -> Cell:
    if field.is_counted_list:
        return lambda r: html_list_cell([_cell(value, field.display) for value in r[field.name]]) or _EMPTY
    return lambda r: _cell(r[field.name], field.display)


def _name_cell(lookup: NameLookup) -> Cell:
    if lookup.is_tagged:
        return lambda r: pa_cell(r, lookup.field)
    return lambda r: _cell(r[lookup.field])


def _icon_cell(icon: IconLookup) -> Cell:
    return lambda r: icon_cell(r[icon.field])


def _name_column(lookup: NameLookup, cols: dict[str, str]) -> _Shown:
    return _Shown(Column(cols[lookup.column], sort_key=lookup.field), _name_cell(lookup))


def _text_columns(text: TextRef, cols: dict[str, str]) -> list[_Shown]:
    """The string column of a string-table index, then its name column."""
    if text.column is None:
        return []
    shown = [_Shown(Column(cols[text.column], sort_key=text.field), lambda r: _cell(r[text.field]))]
    if text.lookup is not None:
        shown.append(_name_column(text.lookup, cols))
    return shown


def _field_columns(field: ValueField, cols: dict[str, str]) -> list[_Shown]:
    """The key column, then its icon and name columns when it has them, then its string."""
    shown: list[_Shown] = []
    if field.column is not None:
        # A list column stays unsortable: it would sort by its string form.
        sort_key = None if field.is_counted_list else field.name
        shown.append(_Shown(Column(cols[field.column], "num", sort_key=sort_key), _value_cell(field)))
        if field.icon is not None:
            shown.append(_Shown(Column(cols[field.icon.column], sort_key=field.icon.field), _icon_cell(field.icon)))
        if field.lookup is not None:
            shown.append(_name_column(field.lookup, cols))
    if field.text is not None:
        shown.extend(_text_columns(field.text, cols))
    return shown


def _name_fields(lookup: NameLookup, key: object) -> dict[str, str]:
    name = lookup.name_of(key)
    return pa_fields(lookup.field, name) if lookup.is_tagged else {lookup.field: name}


def _derived_fields(fields: tuple[ValueField, ...], record: dict) -> dict[str, str]:
    """Each key field's resolved name, then its icon path, then its string's name, in field order."""
    derived: dict[str, str] = {}
    for field in fields:
        if field.lookup is not None:
            derived |= _name_fields(field.lookup, record[field.name])
        if field.icon is not None:
            derived[field.icon.field] = field.icon.path_of(record[field.name])
        if field.text is not None and field.text.lookup is not None:
            derived |= _name_fields(field.text.lookup, record[field.text.field])
    return derived


class PabrValuesBssHandler(PreviewHandler):
    """One small option table; the layout comes from its `ValueTable`."""

    def __init__(self, value_table: ValueTable) -> None:
        self._table = value_table

    def _shown(self) -> list[_Shown]:
        """Each shown column with its cell, in column order."""
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        if not self._table.has_named_field:
            column = Column(cols["valueBytes"], sort_key=VALUE_BYTES_FIELD)
            return [_Shown(column, lambda r: _cell(r[VALUE_BYTES_FIELD]))]
        return [shown for field in self._table.shown_fields for shown in _field_columns(field, cols)]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys([shown.column for shown in self._shown()])

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        if not self._table.has_named_field:
            return [{**record, VALUE_BYTES_FIELD: raw} for record, raw in parse_value_rows(data, self._table)]
        records = parse_value_table(data, self._table)
        return [{**record, **_derived_fields(self._table.fields, record)} for record in records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, f"meta.{self._table.count_key}", count=len(records))
        shown = self._shown()
        rows = [[item.cell(r) for item in shown] for r in records[start : start + page_size]]
        return table(meta, [item.column for item in shown], rows)
