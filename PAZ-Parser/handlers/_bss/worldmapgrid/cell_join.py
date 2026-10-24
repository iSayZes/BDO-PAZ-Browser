"""One row of a world map grid table: the cells it covers and the keys they join."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

from .parser import CellArea


@dataclass(frozen=True)
class CellJoin:
    """The keys a row's cells stand for and their names in the user's language."""

    keys: tuple[int, ...]
    names: tuple[str, ...]


NO_JOIN = CellJoin((), ())


@dataclass(frozen=True)
class GridRow:
    """One table row: the cells of one value (or of one group of a shared value) and their join."""

    area: CellArea
    join: CellJoin


def names(values: Iterable[str]) -> tuple[str, ...]:
    """The names that are not empty: a key without a LOC name drops out."""
    return tuple(name for name in values if name)
