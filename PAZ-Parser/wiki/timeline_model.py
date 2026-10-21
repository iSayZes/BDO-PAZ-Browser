"""Where the bands and ticks of a doc's layout timeline sit.

The axis holds every client any doc's Versions names, the newest at 0 (the
left end) and the oldest at 1, evenly spaced. Each client gets a result from
the doc's Clients table, else from the layout whose client range holds it;
consecutive clients with the same result make one band. A newer band reaches
the newest client of the older band, the newest band the left end and the
oldest band the right end. A layout with no checked client sits between the
layouts numbered around it.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass

from format_docs.versions import ClientCheck

LAYOUT = "layout"
UNDATED = "undated"
NO_LAYOUT = "no_layout"
NO_FILE = "no_file"


@dataclass(frozen=True)
class TimelineLayout:
    """A layout with the clients Versions gives it; `first` is None when no client fits it yet."""

    number: int
    first: int | None
    last: int | None
    is_open: bool
    checked: int | None

    @property
    def clients_text(self) -> str:
        if self.first is None:
            return "no checked client"
        if self.is_open:
            return f"client {self.first} and later"
        return f"client {self.first}" if self.first == self.last else f"client {self.first} to {self.last}"

    @property
    def pill(self) -> str:
        return f"Layout {self.number} · {self.clients_text}" if self.first is not None else f"Layout {self.number}"

    def fits(self, client: int) -> bool:
        return self.first is not None and client >= self.first and (self.is_open or client <= (self.last or 0))


@dataclass(frozen=True)
class Band:
    """A stretch of track: `kind` is LAYOUT, UNDATED, NO_LAYOUT or NO_FILE; `clients` newest first."""

    kind: str
    layout: int | None
    clients: tuple[int, ...]
    left: float
    right: float


@dataclass(frozen=True)
class Timeline:
    axis: tuple[int, ...]
    at: Mapping[int, float]
    bands: tuple[Band, ...]
    ticks: tuple[int, ...]
    results: Mapping[int, tuple[str, int | None]]


@dataclass
class _Slot:
    kind: str
    layout: int | None
    clients: list[int]


def build_timeline(layouts: Sequence[TimelineLayout], clients: Sequence[ClientCheck], axis: Sequence[int]) -> Timeline:
    """The timeline of a doc with `layouts` (any order) on the shared `axis`, which the doc's own clients join."""
    own = {check.client for check in clients} | {c for layout in layouts for c in (layout.first, layout.last, layout.checked) if c}
    full_axis = tuple(sorted(set(axis) | own))
    at = _positions(full_axis)
    results = _results(layouts, clients, full_axis)
    slots = _slots(results, full_axis)
    for layout in layouts:
        if layout.first is None:
            _insert_undated(slots, layout.number)
    edges = [_edge(newer, older) for newer, older in zip(slots, slots[1:])]
    xs = [at[edge] if edge is not None else None for edge in edges]
    xs = [x if x is not None else _middle(xs, index) for index, x in enumerate(xs)]
    bands = tuple(
        Band(slot.kind, slot.layout, tuple(slot.clients), xs[index - 1] if index else 0.0, xs[index] if index < len(xs) else 1.0)
        for index, slot in enumerate(slots)
    )
    ticks = tuple(sorted({full_axis[0], full_axis[-1], *(edge for edge in edges if edge is not None)}))
    return Timeline(full_axis, at, bands, ticks, results)


def _positions(axis: Sequence[int]) -> dict[int, float]:
    if len(axis) == 1:
        return {axis[0]: 0.5}
    last = len(axis) - 1
    return {client: (last - index) / last for index, client in enumerate(axis)}


def _results(layouts: Sequence[TimelineLayout], clients: Sequence[ClientCheck], axis: Sequence[int]) -> dict[int, tuple[str, int | None]]:
    """Each client's result: its Clients row, else the layout whose range holds it; unchecked clients are left out."""
    recorded = {check.client: check for check in clients}
    results: dict[int, tuple[str, int | None]] = {}
    for client in axis:
        check = recorded.get(client)
        if check is not None:
            if check.layout is not None:
                results[client] = (LAYOUT, check.layout)
            else:
                results[client] = (NO_LAYOUT if check.has_file else NO_FILE, None)
            continue
        fit = next((layout for layout in layouts if layout.fits(client)), None)
        if fit is not None:
            results[client] = (LAYOUT, fit.number)
    return results


def _slots(results: Mapping[int, tuple[str, int | None]], axis: Sequence[int]) -> list[_Slot]:
    """The runs of equal results, newest first."""
    slots: list[_Slot] = []
    for client in reversed(axis):
        result = results.get(client)
        if result is None:
            continue
        if slots and (slots[-1].kind, slots[-1].layout) == result:
            slots[-1].clients.append(client)
        else:
            slots.append(_Slot(result[0], result[1], [client]))
    return slots


def _insert_undated(slots: list[_Slot], number: int) -> None:
    """Puts a layout with no checked client before the first slot of an older layout, else after the last layout."""
    older = next((index for index, slot in enumerate(slots) if slot.kind in (LAYOUT, UNDATED) and (slot.layout or 0) < number), None)
    if older is None:
        layout_slots = [index for index, slot in enumerate(slots) if slot.kind in (LAYOUT, UNDATED)]
        older = layout_slots[-1] + 1 if layout_slots else len(slots)
    slots.insert(older, _Slot(UNDATED, number, []))


def _edge(newer: _Slot, older: _Slot) -> int | None:
    """The client two slots meet at: the older slot's newest, or the newer slot's oldest before a layout with no client."""
    if older.kind == UNDATED:
        return newer.clients[-1] if newer.clients else None
    return older.clients[0]


def _middle(xs: Sequence[float | None], index: int) -> float:
    """Between two layouts with no checked client: halfway between the nearest known edges."""
    before = next((x for x in reversed(xs[:index]) if x is not None), 0.0)
    after = next((x for x in xs[index + 1:] if x is not None), 1.0)
    return (before + after) / 2
