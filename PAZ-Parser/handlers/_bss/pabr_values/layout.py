"""The layout types of the small option tables: framing, row count and fields.

A PABR file is the PABR magic, the values, then the string table and the
trailer. A bare file is the values alone, with no magic, string table or
trailer. The values are one set of fields, a u32 count and that many rows
(optionally after head fields or before tail fields stored once), or rows up
to the string table or the end of a bare file. A field can be a
counted list: a u32 (or u64) count, then that many values, a list of a fixed
number of values with no count, or a string-table index whose string the
record keeps.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from typing import Any


# The record key of a row's position, for a table with `index_column`.
ROW_INDEX_FIELD = "index"


class Framing(Enum):
    """What surrounds the values."""

    # PABR magic at +0x00, the values from +0x04, then the string table and the trailer.
    PABR = "pabr"
    # The values alone, from +0x00 to the end of the file.
    BARE = "bare"


class RowCount(Enum):
    """How many times the fields repeat in the values."""

    ONE = "one"
    # A u32 count where the values start, then that many rows.
    COUNTED = "counted"
    # Rows from where the values start up to the string table (PABR) or the
    # end of the file (BARE), no count.
    TO_TABLE_START = "to_table_start"


@dataclass(frozen=True)
class NameLookup:
    """A display name for a key field, stored on the record next to it.

    With `is_tagged`, `name_of` returns game text with `<PAColor>` tags: the
    record keeps the plain text under `field` and the tagged copy under
    `pa_key(field)`, and the cell draws the colours. `name_of` takes the key,
    or the string of a `TextRef`. With `is_row_lookup` it takes the whole
    record: for a LOC key built from several fields, or LOC text that falls
    back to the row's inline Korean string.
    """

    field: str
    column: str
    name_of: Callable[[Any], str]
    is_tagged: bool = False
    is_row_lookup: bool = False


@dataclass(frozen=True)
class TextRef:
    """The string a string-table index points to, stored on the record under `field`.

    `column` is None to keep the string off the table. `lookup` names the
    string (a GAME sheet key to its LOC text); its column follows.
    """

    field: str
    column: str | None = None
    lookup: NameLookup | None = None


@dataclass(frozen=True)
class IconLookup:
    """An icon path for a key field, stored on the record; its column sits after the key."""

    field: str
    column: str
    path_of: Callable[[int], str]


@dataclass(frozen=True)
class ValueField:
    """One field: record key, `struct` format and its lang column key.

    `column` is None for a field with no column (`unknown_*`, or a copy of
    another field). An `s` format (`8s`) is a byte run, stored as hex text.
    `display` turns the value (a number, a byte run's hex text or an entry
    list) into its cell text; the record keeps the value.
    With `is_counted_list` the field is a `count_fmt` count, then that many
    values, stored as a list; a format of several values (`B3I`) stores each
    entry as a list. `fixed_count` reads a list of that many entries with no
    count before it. `display` then draws each entry on its own line, and
    `list_display` draws the whole list as one text. `text` reads the value
    as a string-table index.
    """

    name: str
    fmt: str
    column: str | None = None
    lookup: NameLookup | None = None
    icon: IconLookup | None = None
    display: Callable[[Any], str] | None = None
    is_counted_list: bool = False
    count_fmt: str = "I"
    text: TextRef | None = None
    list_display: Callable[[list[Any]], str] | None = None
    fixed_count: int | None = None

    def __post_init__(self) -> None:
        if self.is_counted_list and self.fixed_count is not None:
            raise ValueError(f"{self.name}: a list has a count in the file or a fixed count, not both")
        if self.fixed_count is not None and self.fixed_count < 1:
            raise ValueError(f"{self.name}: a fixed list needs at least one entry")
        if self.is_list and (self.lookup is not None or self.icon is not None or self.text is not None):
            raise ValueError(f"{self.name}: a counted list takes no name, icon or text lookup")
        if self.list_display is not None and (not self.is_list or self.display is not None):
            raise ValueError(f"{self.name}: list_display needs a counted list without display")

    @property
    def is_list(self) -> bool:
        """True for a counted list and for a list of `fixed_count` entries."""
        return self.is_counted_list or self.fixed_count is not None


@dataclass(frozen=True)
class ValueTable:
    """The layout of one file; `count_key` is the lang `meta` key of its count line.

    `first_fields` names fields whose columns come first, in that order: the
    row key when the row stores it after other fields, or a name stored late.
    `head` holds fields stored once where the values start, before the row
    count of `RowCount.COUNTED`, and `tail` fields stored once after the
    last row; every record holds their values, and their columns follow the
    row fields. `index_column` is the lang column key of the row's position
    (from 0), for a file whose rows hold no key: every record stores it under
    `ROW_INDEX_FIELD`, and its column comes first. `index_display` turns the
    position into its cell text, for a position that is an enum value.
    """

    file_name: str
    fields: tuple[ValueField, ...]
    rows: RowCount = RowCount.ONE
    framing: Framing = Framing.PABR
    count_key: str = "count"
    first_fields: tuple[str, ...] = ()
    head: tuple[ValueField, ...] = ()
    tail: tuple[ValueField, ...] = ()
    index_column: str | None = None
    index_display: Callable[[int], str] | None = None

    def __post_init__(self) -> None:
        if self.index_display is not None and self.index_column is None:
            raise ValueError(f"{self.file_name}: index_display needs an index_column")
        if self.rows is RowCount.TO_TABLE_START and any(field.is_counted_list for field in self.fields):
            raise ValueError(f"{self.file_name}: rows up to the string table need a fixed row size")
        if self.head and self.rows is not RowCount.COUNTED:
            raise ValueError(f"{self.file_name}: head fields need a row count after them")
        if self.tail and self.rows is not RowCount.COUNTED:
            raise ValueError(f"{self.file_name}: tail fields need a row count before the rows")
        if self.framing is Framing.BARE and any(field.text is not None for field in self.all_fields):
            raise ValueError(f"{self.file_name}: a bare file has no string table")
        missing = set(self.first_fields) - {field.name for field in self.all_fields}
        if missing:
            raise ValueError(f"{self.file_name}: no field {', '.join(sorted(missing))}")

    @property
    def all_fields(self) -> tuple[ValueField, ...]:
        """The row fields, then the head fields, then the tail fields."""
        return self.fields + self.head + self.tail

    @property
    def has_named_field(self) -> bool:
        return any(
            field.column is not None or (field.text is not None and field.text.column is not None)
            for field in self.all_fields
        )

    @property
    def has_text(self) -> bool:
        return any(field.text is not None for field in self.all_fields)

    @property
    def shown_fields(self) -> tuple[ValueField, ...]:
        """The fields in column order: `first_fields`, then the rest in row order, then the head and tail fields."""
        by_name = {field.name: field for field in self.all_fields}
        first = tuple(by_name[name] for name in self.first_fields)
        return first + tuple(field for field in self.all_fields if field.name not in self.first_fields)


def unknown_fields(*layout: tuple[int, str]) -> tuple[ValueField, ...]:
    """`unknown_<offset>` fields from (offset, format) pairs."""
    return tuple(ValueField(f"unknown_{offset:02x}", fmt) for offset, fmt in layout)
