"""The parts of a format doc the checks look at.

A doc is read once into these frozen records; the checks only read them.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Problem:
    """One thing a doc gets wrong, at a 1-based line."""

    line: int
    message: str

    def __str__(self) -> str:
        return f"line {self.line}: {self.message}"


@dataclass(frozen=True)
class Table:
    """A markdown table: its header cells and its rows with their line numbers."""

    line: int
    header: tuple[str, ...]
    rows: tuple[tuple[int, tuple[str, ...]], ...]


@dataclass(frozen=True)
class Section:
    """A heading and the lines up to the next heading of the same or a higher level."""

    level: int
    title: str
    line: int
    body: tuple[tuple[int, str], ...]


@dataclass(frozen=True)
class Field:
    """One row of a layout table."""

    line: int
    offset: str
    type_text: str
    name: str
    notes: str
    # Columns between Field and Notes, such as `Source`: (header, cell) pairs.
    extra: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class SizeSpec:
    """The size a structure heading states.

    `fixed` is the total for a fixed-size structure and the fixed part for a
    variable one. `external` names the offset file that gives the size, if any.
    """

    is_variable: bool
    fixed: int | None
    external: str | None = None


@dataclass(frozen=True)
class Structure:
    """A `###` heading inside a layout and its layout table.

    `size` is None for a top-level table (`File Layout` or a companion file).
    """

    name: str
    line: int
    size: SizeSpec | None
    fields: tuple[Field, ...]

    @property
    def is_top_level(self) -> bool:
        return self.size is None


@dataclass(frozen=True)
class Layout:
    """A `## Layout N` section."""

    number: int
    line: int
    structures: tuple[Structure, ...]

    def find(self, name: str) -> Structure | None:
        return next((structure for structure in self.structures if structure.name == name), None)
