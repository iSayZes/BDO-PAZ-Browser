"""Which shared data a records build read: LOC, which lookup indexes, the client.

A table's records depend on its own bytes and handler code, and on the LOC and
lookup indexes the app injects (`loc.py`, `lookup_index.py`) and, for the few
handlers that ask, on the client version (`effective_client.py`). LOC, the big
indexes and the client change with nearly every patch, so the parsed records
disk cache keys a table only on the shared data its build actually read. Those
modules call `note_read()` on every access; `recording()` collects the names
while a build runs.

Recorders are shared across threads: a build on another thread at the same
time can add a name it did not read itself. That only makes a cache entry
stale sooner, never wrong.
"""

from __future__ import annotations

import threading
from collections.abc import Iterator
from contextlib import contextmanager

LOC = "loc"
INDEX_PREFIX = "index:"
# The client version a build read (`effective_client.py`).
CLIENT = "client"
# Which of a handler's layout ranges the client falls in (`client_versions.py`):
# the name lists the ranges, the digest is the index of the covering layout.
CLIENT_RANGES_PREFIX = "client-ranges:"

# One layout's client ranges as (first, last) pairs; last None is open-ended.
LayoutRanges = tuple[tuple[int, int | None], ...]

_NO_LAYOUT = "none"

# Replaced, never mutated, so `note_read()` iterates a stable tuple while
# another thread starts or ends a recording.
_recorders: tuple[set[str], ...] = ()
_recorders_lock = threading.Lock()


def index_dep(kind_value: str) -> str:
    """Dependency name of one lookup index, by `IndexKind.value`."""
    return f"{INDEX_PREFIX}{kind_value}"


def client_ranges_dep(layouts: list[LayoutRanges]) -> str:
    """Dependency name of the ranges of each layout, e.g. `client-ranges:1194-1261|1267-`."""
    groups = (",".join(f"{first}-{'' if last is None else last}" for first, last in ranges) for ranges in layouts)
    return CLIENT_RANGES_PREFIX + "|".join(groups)


def covering_layout(layouts: list[LayoutRanges], client: int | None) -> int | None:
    """Index of the first layout whose ranges cover `client`, or None."""
    if client is None:
        return None
    for index, ranges in enumerate(layouts):
        if any(first <= client and (last is None or client <= last) for first, last in ranges):
            return index
    return None


def client_ranges_digest(name: str, client: int | None) -> str:
    """Digest of a `client_ranges_dep()` name: which layout covers `client`.

    A patch that keeps the client inside the same layout's range keeps the
    digest, so a table whose build only ordered its layouts by the client is
    not parsed again.
    """
    layouts: list[LayoutRanges] = []
    for group in name[len(CLIENT_RANGES_PREFIX):].split("|"):
        pairs = (span.split("-") for span in group.split(",") if span)
        layouts.append(tuple((int(first), int(last) if last else None) for first, last in pairs))
    index = covering_layout(layouts, client)
    return _NO_LAYOUT if index is None else str(index)


def note_read(dep: str) -> None:
    for deps in _recorders:
        deps.add(dep)


@contextmanager
def recording() -> Iterator[set[str]]:
    """Collect the dependency names read until the block ends."""
    global _recorders

    deps: set[str] = set()
    with _recorders_lock:
        _recorders = (*_recorders, deps)
    try:
        yield deps
    finally:
        with _recorders_lock:
            _recorders = tuple(other for other in _recorders if other is not deps)
