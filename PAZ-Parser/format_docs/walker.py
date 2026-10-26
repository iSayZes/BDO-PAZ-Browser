"""Walks a game file's bytes by one layout of a format doc.

The walk reads every field the layout names, in order, takes counts,
conditions and string lengths from the bytes, and fails at the first place
the bytes disagree. A file fits when the walk ends exactly at its last byte.
"""
from __future__ import annotations

import struct
from collections.abc import Mapping
from dataclasses import dataclass

from .model import Field, Structure
from .names import OFFSET_FIELD, SIZE_FIELD, UNKNOWN_PREFIX
from .offsets import Offset, parse_offset
from .type_grammar import NUMBER_SIZES, STRING_HEADS, UNIT_SIZES, Clause, Condition, TypeSpec, parse_type
from .walk_model import FieldBytes, FileFit, RowStats, Unwalkable, WalkError

_FORMATS = {
    "u8": "B", "i8": "b", "u16": "H", "i16": "h", "u32": "I", "i32": "i", "u64": "Q", "i64": "q",
    "f16": "e", "f32": "f", "f64": "d",
}
_STRING_UNITS = {"str8": 1, "str16": 2}
_NUMBER, _STRING, _STRUCTURE = "number", "string", "structure"


@dataclass(frozen=True)
class _Row:
    """One field of a structure, with what a read of it needs worked out once: a large file reads each row millions of times."""

    field: Field
    spec: TypeSpec
    offset: Offset
    is_from_end: bool
    kind: str
    # The bytes of one value of a number or unit type; 0 for the other kinds.
    unit: int
    # Reads one number; None for a unit type, which only an array reads.
    number: struct.Struct | None
    cover_key: tuple[str, str]


@dataclass(frozen=True)
class _Plan:
    """A structure's rows, split by where they are read from, and the fields `_note_sizes` pairs."""

    rows: tuple[_Row, ...]
    forward: tuple[_Row, ...]
    from_end: tuple[_Row, ...]
    # How far back from the end the first trailer row starts; 0 without one.
    trailer: int
    offset_names: tuple[str, ...]
    size_names: tuple[str, ...]
    notes_sizes: bool
    # The fields `[sum field]` counts in this structure add up over its earlier repeated structures.
    summed: frozenset[str]


Values = dict[str, int | float | str]


def walk_file(
    name: str, data: bytes, top: Structure, structures: Mapping[str, Structure], sizes_by_file: Mapping[str, Mapping[int, int]]
) -> tuple[FileFit, dict[int, int]]:
    """Walk `data` from `top`; return the fit and the (offset, size) pairs its rows hold.

    `sizes_by_file` gives, per offset file, the size of the structure that starts at each offset.
    Raises `WalkError` where the bytes break the layout and `Unwalkable` for a form a walk cannot follow.
    """
    walker = _Walker(data, structures, sizes_by_file)
    walker.walk_top(top)
    return walker.result(name), walker.found_sizes


class _Walker:
    def __init__(self, data: bytes, structures: Mapping[str, Structure], sizes_by_file: Mapping[str, Mapping[int, int]]) -> None:
        self.data = data
        self.size = len(data)
        self.structures = structures
        self.sizes_by_file = sizes_by_file
        # Per structure: count, smallest, largest and total bytes, kept as plain numbers until `result`.
        self.row_sizes: dict[str, list[int]] = {}
        self.covered: dict[tuple[str, str], int] = {}
        self.found_sizes: dict[int, int] = {}
        self._plans: dict[str, _Plan] = {}

    def result(self, name: str) -> FileFit:
        rows = {structure: RowStats(*sizes) for structure, sizes in self.row_sizes.items()}
        fields = tuple(
            FieldBytes(structure, field, not field.startswith(UNKNOWN_PREFIX), size)
            for (structure, field), size in self.covered.items()
        )
        return FileFit(name, len(self.data), rows, fields)

    def walk_top(self, top: Structure) -> None:
        plan = self._plan(top)
        values: Values = {}
        body_end = self._read_end_rows(top, plan, len(self.data), values)
        pos = self._walk_rows(top, plan, 0, body_end, values)
        if pos != body_end:
            what = "the trailer starts" if body_end != len(self.data) else "the file ends"
            raise WalkError(top.name, "(end)", pos, f"the fields end at 0x{pos:X}, {what} at 0x{body_end:X}")

    def _structure(self, structure: Structure, pos: int, outer_end: int | None) -> tuple[int, Values]:
        start = pos
        values: Values = {}
        end = self._fixed_end(structure, pos, values)
        if end is not None and end > len(self.data) and structure.size is not None and structure.size.external:
            raise WalkError(structure.name, "(size)", pos, f"needs up to 0x{end:X}, the file ends at 0x{len(self.data):X}")
        plan = self._plan(structure)
        body_end = self._read_end_rows(structure, plan, end, values) if end is not None else outer_end
        pos = self._walk_rows(structure, plan, pos, body_end, values)
        if end is not None and pos != body_end:
            raise WalkError(structure.name, "(end)", pos, f"the fields end at 0x{pos:X}, its size says 0x{body_end:X}")
        final = end if end is not None else pos
        self._count_row(structure.name, final - start)
        if plan.notes_sizes:
            self._note_sizes(plan, values)
        return final, values

    def _fixed_end(self, structure: Structure, pos: int, values: Values) -> int | None:
        spec = structure.size
        if spec is None:
            return None
        if spec.external:
            sizes = self.sizes_by_file.get(spec.external)
            if sizes is None:
                raise WalkError(structure.name, "(size)", pos, f"`{spec.external}` was not read")
            if pos not in sizes:
                raise WalkError(structure.name, "(size)", pos, f"no row of `{spec.external}` starts a {structure.name} here")
            values["size"] = sizes[pos]
            return pos + sizes[pos]
        return None if spec.is_variable or spec.fixed is None else pos + spec.fixed

    def _read_end_rows(self, structure: Structure, plan: _Plan, end: int, values: Values) -> int:
        """Read the rows counted back from `end` first; return where they start."""
        if not plan.from_end:
            return end
        start = end - plan.trailer
        if start < 0:
            raise WalkError(structure.name, plan.from_end[0].field.name, 0, "the file is shorter than its trailer")
        for row in plan.from_end:
            self._read(structure, row, end - row.offset.value, end, values)
        return start

    def _walk_rows(self, structure: Structure, plan: _Plan, pos: int, end: int | None, values: Values) -> int:
        for row in plan.forward:
            pos = self._read(structure, row, pos, end, values)
        return pos

    def _read(self, structure: Structure, row: _Row, pos: int, end: int | None, values: Values) -> int:
        condition = row.spec.condition
        if condition is not None and not self._holds(structure, row, condition, pos, values):
            return pos
        if row.kind is _NUMBER:
            return self._read_numbers(structure, row, pos, end, values)
        if row.kind is _STRUCTURE:
            return self._read_structures(structure, row, pos, end, values)
        return self._read_strings(structure, row, pos, end, values)

    def _read_numbers(self, structure: Structure, row: _Row, pos: int, end: int | None, values: Values) -> int:
        spec, unit = row.spec, row.unit
        if spec.count is None:
            if row.number is None:
                raise Unwalkable(f"{structure.name} `{row.field.name}` is a {spec.name} without a count")
            # `_need` inlined: this is the walk's most frequent read.
            limit = self.size if end is None or end > self.size else end
            if pos + unit > limit:
                self._need(structure, row, pos, unit, end)
            values[row.field.name] = row.number.unpack_from(self.data, pos)[0]
            self.covered[row.cover_key] = self.covered.get(row.cover_key, 0) + unit
            return pos + unit
        size = self._array_bytes(structure, row, pos, end, values, unit)
        self._need(structure, row, pos, size, end)
        if spec.name in ("char", "char16"):
            values[row.field.name] = self.data[pos : pos + size].decode("ascii" if spec.name == "char" else "utf-16-le", errors="replace")
        self._cover(row, size)
        return pos + size

    def _array_bytes(self, structure: Structure, row: _Row, pos: int, end: int | None, values: Values, unit: int) -> int:
        count = row.spec.count
        assert count is not None
        if count.kind == "scan":
            raise Unwalkable(f"{structure.name} `{row.field.name}` is `bytes[scan]`")
        if count.kind in ("rest", "until"):
            target = end if count.kind == "rest" or count.value == "end" else self._value(structure, row, str(count.value), pos, values)
            if target is None:
                raise Unwalkable(f"{structure.name} `{row.field.name}` runs to an end nothing gives")
            size = target - pos
            if size < 0 or size % unit:
                raise WalkError(structure.name, row.field.name, pos, f"runs to 0x{target:X}, not a whole number of {unit}-byte values")
            return size
        return self._element_count(structure, row, pos, values) * unit

    def _element_count(self, structure: Structure, row: _Row, pos: int, values: Values) -> int:
        spec = row.spec
        assert spec.count is not None
        kind = spec.count.kind
        if kind == "fixed":
            outer = int(spec.count.value)
        elif kind == "sum":
            # A repeat with no elements, or one its condition left out, adds 0.
            outer = int(values.get(_sum_key(str(spec.count.value)), 0))
        else:
            outer = self._value(structure, row, str(spec.count.value), pos, values)
        inner = spec.inner if isinstance(spec.inner, int) or spec.inner is None else self._value(structure, row, spec.inner, pos, values)
        return outer * (inner or 1)

    def _read_strings(self, structure: Structure, row: _Row, pos: int, end: int | None, values: Values) -> int:
        start = pos
        count = 1 if row.spec.count is None else self._element_count(structure, row, pos, values)
        for _ in range(count):
            pos, text = self._string(structure, row, pos, end)
            if row.spec.count is None:
                values[row.field.name] = text
        self._cover(row, pos - start)
        return pos

    def _string(self, structure: Structure, row: _Row, pos: int, end: int | None) -> tuple[int, str]:
        head = STRING_HEADS[row.spec.name]
        self._need(structure, row, pos, head, end)
        if row.spec.name == "pstr":
            is_wide, length = struct.unpack_from("<BI", self.data, pos)
            if is_wide > 1:
                raise WalkError(structure.name, row.field.name, pos, f"`is_wide` is {is_wide}, not 0 or 1")
            self._need(structure, row, pos + head, length, end)
            text = self.data[pos + head : pos + head + length]
            return pos + head + length, text.decode("utf-16-le" if is_wide else "utf-8", errors="replace")
        count = struct.unpack_from("<Q", self.data, pos)[0]
        if count >> 32:
            raise WalkError(structure.name, row.field.name, pos, f"the string count 0x{count:X} has a high word that is not 0")
        unit = _STRING_UNITS[row.spec.name]
        self._need(structure, row, pos + head, count * unit, end)
        text = self.data[pos + head : pos + head + count * unit]
        return pos + head + count * unit, text.decode("ascii" if unit == 1 else "utf-16-le", errors="replace")

    def _read_structures(self, structure: Structure, row: _Row, pos: int, end: int | None, values: Values) -> int:
        spec = row.spec
        element = self.structures.get(spec.name)
        if element is None:
            raise WalkError(structure.name, row.field.name, pos, f"`{spec.name}` has no heading")
        count = spec.count
        if count is None:
            return self._structure(element, pos, end)[0]
        if count.kind in ("fixed", "field", "sum"):
            summed = self._plan(structure).summed
            for _ in range(self._element_count(structure, row, pos, values)):
                pos, element_values = self._structure(element, pos, end)
                if summed:
                    self._add_sums(element, row, pos, summed, element_values, values)
            return pos
        if count.kind == "while":
            return self._read_while(element, row, pos, end)
        if count.kind != "until":
            raise Unwalkable(f"{structure.name} `{row.field.name}` has a count a walk cannot follow")
        target = end if count.value == "end" else self._value(structure, row, str(count.value), pos, values)
        if target is None:
            raise Unwalkable(f"{structure.name} `{row.field.name}` runs to an end nothing gives")
        while pos < target:
            pos = self._next_structure(element, row, pos, target)
        if pos != target:
            raise WalkError(structure.name, row.field.name, pos, f"the last {element.name} ends at 0x{pos:X}, past 0x{target:X}")
        return pos

    def _add_sums(self, element: Structure, row: _Row, pos: int, summed: frozenset[str], element_values: Values, values: Values) -> None:
        """Add the summed fields one repeated `element` holds to the running totals in `values`."""
        for name in summed & element_values.keys():
            value = element_values[name]
            if not isinstance(value, int):
                raise WalkError(element.name, row.field.name, pos, f"`{name}` holds {value!r}, not a count to add up")
            key = _sum_key(name)
            values[key] = int(values.get(key, 0)) + value

    def _read_while(self, element: Structure, row: _Row, pos: int, end: int | None) -> int:
        """Repeat `element` up to the first one whose stop field holds the stop value, that one left out."""
        count = row.spec.count
        assert count is not None and count.stop is not None
        field_name = str(count.value)
        peek = next((r for r in self._plan(element).rows if r.field.name == field_name), None)
        if (
            peek is None or peek.offset.anchor is not None or peek.spec.name not in NUMBER_SIZES
            or peek.spec.count is not None or peek.spec.condition is not None
        ):
            raise Unwalkable(f"`{field_name}` of {element.name} is not an unconditional number at a fixed offset")
        stop_value = _literal(count.stop)
        while True:
            at = pos + peek.offset.value
            self._need(element, peek, at, NUMBER_SIZES[peek.spec.name], end)
            if struct.unpack_from("<" + _FORMATS[peek.spec.name], self.data, at)[0] == stop_value:
                return pos
            pos = self._next_structure(element, row, pos, end)

    def _next_structure(self, element: Structure, row: _Row, pos: int, end: int | None) -> int:
        """Walk one `element` of a repeat that runs to an end; one that takes no bytes would repeat forever."""
        after = self._structure(element, pos, end)[0]
        if after == pos:
            raise WalkError(element.name, row.field.name, pos, f"a {element.name} takes no bytes, so the repeat never ends")
        return after

    def _holds(self, structure: Structure, row: _Row, condition: Condition, pos: int, values: Values) -> bool:
        return any(
            all(self._clause_holds(structure, row, clause, pos, values) for clause in group) for group in condition.groups
        )

    def _clause_holds(self, structure: Structure, row: _Row, clause: Clause, pos: int, values: Values) -> bool:
        if clause.field not in values:
            raise WalkError(structure.name, row.field.name, pos, f"`{clause.field}` was not read before this condition")
        actual = values[clause.field]
        if clause.op in ("^=", "!^="):
            holds = isinstance(actual, str) and actual.startswith(_unquoted(clause.value))
        else:
            holds = actual == _literal(clause.value)
        return not holds if clause.op.startswith("!") else holds

    def _value(self, structure: Structure, row: _Row, name: str, pos: int, values: Values) -> int:
        value = values.get(name)
        if not isinstance(value, int) or value < 0:
            raise WalkError(structure.name, row.field.name, pos, f"`{name}` holds {value!r}, not a count or an offset")
        return value

    def _need(self, structure: Structure, row: _Row, pos: int, size: int, end: int | None) -> None:
        limit = len(self.data) if end is None else min(end, len(self.data))
        if pos + size > limit:
            where = "the file ends" if limit == len(self.data) else f"{structure.name} ends"
            raise WalkError(structure.name, row.field.name, pos, f"needs {size:,} bytes, {where} at 0x{limit:X}")

    def _cover(self, row: _Row, size: int) -> None:
        self.covered[row.cover_key] = self.covered.get(row.cover_key, 0) + size

    def _count_row(self, name: str, size: int) -> None:
        sizes = self.row_sizes.get(name)
        if sizes is None:
            self.row_sizes[name] = [1, size, size, size]
            return
        sizes[0] += 1
        if size < sizes[1]:
            sizes[1] = size
        if size > sizes[2]:
            sizes[2] = size
        sizes[3] += size

    def _note_sizes(self, plan: _Plan, values: Values) -> None:
        offsets = [value for key in plan.offset_names if isinstance(value := values.get(key), int)]
        sizes = [value for key in plan.size_names if isinstance(value := values.get(key), int)]
        if len(offsets) == 1 and len(sizes) == 1:
            self.found_sizes[offsets[0]] = sizes[0]

    def _plan(self, structure: Structure) -> _Plan:
        plan = self._plans.get(structure.name)
        if plan is None:
            plan = _plan(structure)
            self._plans[structure.name] = plan
        return plan


def _plan(structure: Structure) -> _Plan:
    rows = tuple(_row(structure, field) for field in structure.fields)
    from_end = tuple(row for row in rows if row.is_from_end)
    # The keys a structure's values can hold: its fields, and `size` from an external size.
    names = tuple(dict.fromkeys((*(row.field.name for row in rows), "size")))
    offset_names = tuple(name for name in names if OFFSET_FIELD.match(name))
    size_names = tuple(name for name in names if SIZE_FIELD.match(name))
    return _Plan(
        rows,
        tuple(row for row in rows if not row.is_from_end),
        from_end,
        max((row.offset.value for row in from_end), default=0),
        offset_names,
        size_names,
        bool(offset_names and size_names) and (structure.size is None or structure.size.external is None),
        frozenset(str(row.spec.count.value) for row in rows if row.spec.count is not None and row.spec.count.kind == "sum"),
    )


def _sum_key(name: str) -> str:
    """The `values` key of the running total of `name`; a space keeps it apart from every field name."""
    return f"sum {name}"


def _row(structure: Structure, field: Field) -> _Row:
    spec = parse_type(field.type_text)
    offset = parse_offset(field.offset)
    if isinstance(spec, str) or isinstance(offset, str):
        raise Unwalkable(f"{structure.name} `{field.name}` does not pass the doc check")
    if spec.is_structure:
        kind, unit, number = _STRUCTURE, 0, None
    elif spec.name in STRING_HEADS:
        kind, unit, number = _STRING, 0, None
    else:
        fmt = _FORMATS.get(spec.name)
        kind, unit, number = _NUMBER, NUMBER_SIZES.get(spec.name) or UNIT_SIZES[spec.name], None if fmt is None else struct.Struct("<" + fmt)
    return _Row(field, spec, offset, offset.is_from_end, kind, unit, number, (structure.name, field.name))


def _unquoted(text: str) -> str:
    return text.strip("`\"'")


def _literal(text: str) -> int | float | str:
    text = _unquoted(text)
    try:
        return int(text, 0)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        return text
