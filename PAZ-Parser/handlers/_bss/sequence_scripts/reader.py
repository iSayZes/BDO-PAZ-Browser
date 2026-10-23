"""What the sequence and cutscene script tables share.

Every table of the family is a PABR file:

    PABR | u32 row_count | rows | String Table | u32 string_table_start | u32 0

A row names its cutscene or sequence file by a u32 index into the string
table (`CS_Tutorial_06_EternalWinter_0000.pas`), by the file's hash, or both.
The hash is the client's ASCII key hash of the name without `.pas`
(`cutscene_file_hash()`). Text fields, such as the start condition and the
two scripts of `sequencedatatable.bss`, are u32 indexes into the same table;
several rows point at one string. Per-class lists are a u32 count of entries
that each start with a u8 class type (`read_class_entries()`).

See docs/file-formats/sequencedatatable_bss.md, sequence_skill_bss.md and
tutorial_equipment_bss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import TypeVar

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, checked_string_table_start, read_string_table
from _common.record_reader import RecordReader
from _common.string_hash import ascii_key_hash


CUTSCENE_FILE_SUFFIX = ".pas"
# The start condition and the scripts run when a cutscene starts and ends.
SCRIPT_FIELDS = ("start_condition", "start_execute", "end_execute")

_ROW_COUNT_OFFSET = 4
_U32 = struct.Struct("<I")

EntryT = TypeVar("EntryT")


@dataclass(frozen=True)
class ScriptTable:
    """The declared row count, the string table and a reader at the first row."""

    row_count: int
    strings: Sequence[str]
    reader: RecordReader


def open_table(data: bytes, file_name: str) -> ScriptTable:
    """The table's head and strings. Raises ValueError on a bad magic or trailer."""
    rows_end = checked_string_table_start(data, file_name)
    return ScriptTable(
        row_count=u32(data, _ROW_COUNT_OFFSET),
        strings=tuple(read_string_table(data)),
        reader=RecordReader(data, HEADER_SIZE, rows_end, file_name),
    )


def check_rows_end(table: ScriptTable, file_name: str) -> None:
    """Raise ValueError unless the rows end where the string table starts."""
    if not table.reader.at_end():
        raise ValueError(f"{file_name} rows leave {table.reader.remaining():,} bytes before the string table")


def string_ref(strings: Sequence[str], index: int, label: str) -> str:
    """The string at `index`. Raises ValueError when the index is past the table."""
    if not 0 <= index < len(strings):
        raise ValueError(f"{label} points at string {index} of {len(strings)}")
    return strings[index]


def read_string_refs(table: ScriptTable, fields: Sequence[str], label: str) -> dict[str, str]:
    """One u32 string index per field, read in order and resolved."""
    return {
        field: string_ref(table.strings, table.reader.unpack(_U32)[0], f"{label} {field}")
        for field in fields
    }


def cutscene_file_hash(file_name: str) -> int:
    """The hash a row stores for its cutscene file: the ASCII key hash of the name without `.pas`."""
    stem = file_name[: -len(CUTSCENE_FILE_SUFFIX)] if file_name.endswith(CUTSCENE_FILE_SUFFIX) else file_name
    return ascii_key_hash(stem)


def read_class_entries(reader: RecordReader, read_entry: Callable[[RecordReader], EntryT]) -> list[EntryT]:
    """A u32 count, then that many per-class entries read by `read_entry`."""
    (count,) = reader.unpack(_U32)
    return [read_entry(reader) for _ in range(count)]
