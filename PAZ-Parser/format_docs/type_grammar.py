"""The Type column grammar of docs/format-docs.md.

`parse_type` turns a Type cell into a `TypeSpec`; `fixed_size` and
`fixed_part` give its size in bytes from the sizes of the structures it names.
"""
from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass

NUMBER_SIZES: Mapping[str, int] = {
    "u8": 1, "i8": 1, "u16": 2, "i16": 2, "u32": 4, "i32": 4,
    "u64": 8, "i64": 8, "f16": 2, "f32": 4, "f64": 8,
}
UNIT_SIZES: Mapping[str, int] = {"bytes": 1, "char": 1, "char16": 2}
# A string type has a count head of this many bytes, then text of any length.
STRING_HEADS: Mapping[str, int] = {"str8": 8, "str16": 8, "pstr": 5}

_FIELD = r"[a-z][a-z0-9_]*"
_CONDITION = re.compile(r"^(?P<base>.+?) if (?P<clauses>.+)$")
_CLAUSE = re.compile(rf"^(?P<field>{_FIELD}) (?P<op>!?\^?=) (?P<value>\S+)$")
_BASE = re.compile(rf"^(?P<name>[a-z][a-z0-9]*|[A-Z][A-Za-z0-9 ]*?)(?:\[(?P<count>[^\]]+)\])?(?:\[(?P<inner>\d+|{_FIELD})\])?$")
_UNTIL = re.compile(rf"^\.\.(?P<target>{_FIELD}|end)$")
_WHILE = re.compile(rf"^while (?P<field>{_FIELD}) != (?P<value>\S+)$")
_SUM = re.compile(rf"^sum (?P<field>{_FIELD})$")


@dataclass(frozen=True)
class Count:
    """How many elements: `kind` is fixed, field, until, while, sum, rest or scan.

    A `while` count holds the field it reads in `value` and the value that ends it in `stop`.
    A `sum` count holds a field of the structures repeated earlier in the same structure,
    whose values it adds up.
    """

    kind: str
    value: int | str
    stop: str | None = None


@dataclass(frozen=True)
class Clause:
    """`field op value`: `=` and `!=` compare, `^=` and `!^=` test a string prefix."""

    field: str
    op: str
    value: str


@dataclass(frozen=True)
class Condition:
    """Clauses joined by `and` into groups, groups joined by `or`: present when every clause of any group holds."""

    groups: tuple[tuple[Clause, ...], ...]

    @property
    def fields(self) -> tuple[str, ...]:
        return tuple(clause.field for group in self.groups for clause in group)


@dataclass(frozen=True)
class TypeSpec:
    """A parsed Type cell. `name` is a number, string or unit type, or a structure name."""

    name: str
    count: Count | None
    # The inner count of a two-dimensional array: a number, or the name of an earlier field.
    inner: int | str | None
    condition: Condition | None

    @property
    def is_structure(self) -> bool:
        return self.name[0].isupper()


def parse_type(text: str) -> TypeSpec | str:
    """The spec of a Type cell, or the reason it is not in the grammar."""
    condition = None
    match = _CONDITION.match(text)
    if match:
        groups = [[_CLAUSE.match(part) for part in group.split(" and ")] for group in match.group("clauses").split(" or ")]
        if not all(clause for group in groups for clause in group):
            return f"`{match.group('clauses')}` is not `field = value`, `!=`, `^=` or `!^=`, joined by `and` and `or`"
        condition = Condition(tuple(
            tuple(Clause(c.group("field"), c.group("op"), c.group("value")) for c in group if c) for group in groups
        ))
        text = match.group("base")
    base = _BASE.match(text)
    if not base:
        return f"`{text}` is not a type"
    name = base.group("name")
    if not name[0].isupper() and name not in NUMBER_SIZES and name not in UNIT_SIZES and name not in STRING_HEADS:
        return f"`{name}` is not a type"
    count = _parse_count(base.group("count")) if base.group("count") else None
    if isinstance(count, str):
        return count
    inner_text = base.group("inner")
    inner = (int(inner_text) if inner_text.isdigit() else inner_text) if inner_text else None
    return _validated(TypeSpec(name, count, inner, condition))


def structure_type(type_text: str) -> str | None:
    """The structure a Type cell names, or None for a number, string or unit type and a cell outside the grammar."""
    spec = parse_type(type_text)
    return spec.name if not isinstance(spec, str) and spec.is_structure else None


def fixed_size(spec: TypeSpec, structure_sizes: Mapping[str, int | None]) -> int | None:
    """The size in bytes when it does not depend on the data, else None."""
    if spec.condition is not None or spec.name in STRING_HEADS:
        return None
    unit = _unit_size(spec, structure_sizes)
    if unit is None:
        return None
    if spec.count is None:
        return unit
    if spec.count.kind != "fixed" or isinstance(spec.inner, str):
        return None
    return unit * int(spec.count.value) * (spec.inner or 1)


def fixed_part(spec: TypeSpec, structure_sizes: Mapping[str, int | None]) -> int:
    """The bytes a field always takes: its size, or the head of a single string."""
    size = fixed_size(spec, structure_sizes)
    if size is not None:
        return size
    if spec.condition is None and spec.count is None:
        return STRING_HEADS.get(spec.name, 0)
    return 0


def referenced_fields(spec: TypeSpec) -> tuple[str, ...]:
    """The fields of the enclosing structure a count or condition reads, `size` and `end` left out.

    A `while` count reads a field of the repeated structure and a `sum` count fields of earlier
    repeated structures, so neither is listed.
    """
    names: list[str] = []
    if spec.count and spec.count.kind in ("field", "until"):
        names.append(str(spec.count.value))
    if isinstance(spec.inner, str):
        names.append(spec.inner)
    if spec.condition:
        names.extend(spec.condition.fields)
    return tuple(name for name in names if name not in ("size", "end"))


def _parse_count(text: str) -> Count | str:
    if text.isdigit():
        return Count("fixed", int(text))
    if text in ("rest", "scan"):
        return Count(text, text)
    until = _UNTIL.match(text)
    if until:
        return Count("until", until.group("target"))
    loop = _WHILE.match(text)
    if loop:
        return Count("while", loop.group("field"), loop.group("value"))
    total = _SUM.match(text)
    if total:
        return Count("sum", total.group("field"))
    if re.fullmatch(_FIELD, text):
        return Count("field", text)
    return f"`[{text}]` is not a count"


def _validated(spec: TypeSpec) -> TypeSpec | str:
    if spec.name in UNIT_SIZES and spec.count is None:
        return f"`{spec.name}` needs a count, e.g. `{spec.name}[4]`"
    if spec.count is not None and spec.count.kind == "rest" and spec.name != "bytes":
        return "`[rest]` is only for `bytes`"
    if spec.count is not None and spec.count.kind == "scan" and spec.name != "bytes":
        return "`[scan]` is only for `bytes`"
    if spec.inner is not None and (spec.name in STRING_HEADS or spec.count is None or spec.count.kind not in ("fixed", "field")):
        return "a two-dimensional array takes two counts, each a number or a field, e.g. `f32[m][3]`"
    return spec


def _unit_size(spec: TypeSpec, structure_sizes: Mapping[str, int | None]) -> int | None:
    if spec.is_structure:
        return structure_sizes.get(spec.name)
    if spec.name in NUMBER_SIZES:
        return NUMBER_SIZES[spec.name]
    return UNIT_SIZES.get(spec.name)
