"""What walking a game file by a doc's layout gives: a fit, or the place it broke."""
from __future__ import annotations

from dataclasses import dataclass


class WalkError(Exception):
    """The bytes do not follow the layout at `offset`."""

    def __init__(self, structure: str, field: str, offset: int, message: str) -> None:
        super().__init__(f"{structure} `{field}` at 0x{offset:X}: {message}")
        self.structure = structure
        self.field = field
        self.offset = offset
        self.message = message


class Unwalkable(Exception):
    """The layout holds a form a walk cannot follow, such as `bytes[scan]`."""


@dataclass(frozen=True)
class RowStats:
    """The sizes of every instance of one structure in a file."""

    count: int
    smallest: int
    largest: int
    total: int

    @property
    def average(self) -> float:
        return self.total / self.count if self.count else 0.0


@dataclass(frozen=True)
class FieldBytes:
    """The bytes one field takes over the whole file, every instance added up."""

    structure: str
    field: str
    is_known: bool
    size: int


@dataclass(frozen=True)
class FileFit:
    """A file that walks to its last byte by one layout."""

    file: str
    size: int
    rows: dict[str, RowStats]
    fields: tuple[FieldBytes, ...]

    @property
    def known(self) -> int:
        return sum(field.size for field in self.fields if field.is_known)

    @property
    def unknown(self) -> int:
        return sum(field.size for field in self.fields if not field.is_known)


@dataclass(frozen=True)
class LayoutFit:
    """Every file of a doc walked by one layout."""

    layout: int
    files: tuple[FileFit, ...]


@dataclass(frozen=True)
class LayoutMiss:
    """Why one layout does not fit: the first file and place that broke."""

    layout: int
    file: str
    error: WalkError
