"""Reader for the option runs of `gameoption.bss` past the head.

A run is the part of the record one option sheet's loader fills, in the
loader's read order (`ServantOption`, `EtcOption`, ...). Each field is one
number, a fixed array, or a counted array whose count is an earlier field of
the same run. The field lists are in `run_fields.py`; the layout is in
docs/file-formats/bss/gameoption_bss.md (Layout 6).
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.record_reader import RecordReader


@dataclass(frozen=True)
class RunField:
    """One field of a run.

    `fmt` is the `struct` format of one element (`"Q"`, `"If"` for a pair,
    `"41s"` for a byte run). `count` is empty for a single element, a number
    for a fixed array, or the name of the earlier field that counts the
    elements. `kind` says what the value names: `item` (an item key), `items`
    (item keys), `string` (a string-table index), `buffs` (buff keys packed
    as `key << 16 | 1`), or `count` (the count of a later field).
    """

    name: str
    fmt: str
    count: str = ""
    kind: str = ""

    @property
    def is_unknown(self) -> bool:
        return self.name.startswith("unknown_")

    @property
    def is_shown(self) -> bool:
        """Named and not just the count of the next field."""
        return not self.is_unknown and self.kind != "count"


@dataclass(frozen=True)
class Run:
    """The fields one sheet's loader fills, in file order; `sheet` is empty for blocks no loader explains."""

    sheet: str
    fields: tuple[RunField, ...]


@dataclass(frozen=True)
class RunValue:
    """One field as read: its offset and size in the file, its run's sheet and its value.

    A single number is an int or a float, a byte run is bytes, an array is a
    tuple (of tuples for a pair format).
    """

    offset: int
    size: int
    sheet: str
    field: RunField
    value: int | float | bytes | tuple


def read_run(reader: RecordReader, run: Run) -> list[RunValue]:
    """Every field of `run` from the reader's position. Raises ValueError past the record's end."""
    values: dict[str, int | float | bytes | tuple] = {}
    out: list[RunValue] = []
    for field in run.fields:
        offset = reader.pos
        value = _read_field(reader, field, values)
        values[field.name] = value
        out.append(RunValue(offset, reader.pos - offset, run.sheet, field, value))
    return out


def _read_field(reader: RecordReader, field: RunField, values: dict) -> int | float | bytes | tuple:
    element = struct.Struct("<" + field.fmt)
    if not field.count:
        unpacked = reader.unpack(element)
        return unpacked[0] if len(unpacked) == 1 else unpacked
    count = int(field.count) if field.count.isdigit() else values[field.count]
    if not isinstance(count, int) or count * element.size > reader.remaining():
        raise ValueError(f"`{field.name}` counts {count!r} elements, past the record at 0x{reader.pos:X}")
    elements = [reader.unpack(element) for _ in range(count)]
    return tuple(e[0] if len(e) == 1 else e for e in elements)
