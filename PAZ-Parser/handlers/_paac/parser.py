"""Read an action chart (`*.paac`) or the shared tables file with the layout that fits.

`parse_chart()` reads a chart to its trailing version; `parse_shared_tables()`
reads `pc/pc_actionchartpackagepcraw.paac` (Layout 1 only: the frame events of
client 3483's copy are not decoded yet). Each tries the layout of the effective
client first, then the other.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import TypeVar

from _common.client_versions import client_order
from .events import skip_events
from .layouts import LAYOUT_1, LAYOUTS, ChartLayout
from .packages import Package, read_element, read_package
from .reader import ChartReader
from .sections import ChartHead, read_head, skip_condition_record

SHARED_TABLES_NAME = "pc_actionchartpackagepcraw.paac"


@dataclass(frozen=True)
class Chart:
    layout: int
    head: ChartHead
    event_count: int
    packages: list[Package]
    strings: list[str]


@dataclass(frozen=True)
class ElementGroup:
    key: int
    elements: list[dict]


@dataclass(frozen=True)
class SharedTables:
    layout: int
    condition_count: int
    event_count: int
    groups: list[ElementGroup]
    strings: list[str]


Parsed = TypeVar("Parsed")


def _first_fit(
    data: bytes, file_name: str, layouts: tuple[ChartLayout, ...], read: Callable[[ChartReader, ChartLayout], Parsed]
) -> Parsed:
    breaks = []
    for layout in client_order(layouts, lambda layout: layout.clients):
        reader = ChartReader(data, file_name)
        try:
            parsed = read(reader, layout)
            if not reader.at_end():
                raise ValueError(f"the fields end at 0x{reader.pos:X}, the string table version sits at 0x{reader.pos + reader.remaining():X}")
            return parsed
        except ValueError as error:
            breaks.append(f"Layout {layout.number}: {error}")
    raise ValueError("; ".join(breaks))


def _read_chart(reader: ChartReader, layout: ChartLayout) -> Chart:
    head = read_head(reader, layout)
    event_count = skip_events(reader, layout.event_types)
    packages = [read_package(reader, layout) for _ in range(reader.count())]
    return Chart(layout.number, head, event_count, packages, reader.strings)


def _read_shared_tables(reader: ChartReader, layout: ChartLayout) -> SharedTables:
    condition_count = reader.count()
    for _ in range(condition_count):
        skip_condition_record(reader)
    event_count = skip_events(reader, layout.event_types)
    groups = []
    for _ in range(reader.count()):
        key = reader.u32()
        groups.append(ElementGroup(key, [read_element(reader, layout) for _ in range(reader.count())]))
    return SharedTables(layout.number, condition_count, event_count, groups, reader.strings)


def parse_chart(data: bytes, file_name: str) -> Chart:
    """A class, object or monster chart. Raises ValueError when no layout reads it to its end."""
    return _first_fit(data, file_name, LAYOUTS, _read_chart)


def parse_shared_tables(data: bytes) -> SharedTables:
    """`pc_actionchartpackagepcraw.paac`. Raises ValueError when Layout 1 does not read it."""
    return _first_fit(data, SHARED_TABLES_NAME, (LAYOUT_1,), _read_shared_tables)
