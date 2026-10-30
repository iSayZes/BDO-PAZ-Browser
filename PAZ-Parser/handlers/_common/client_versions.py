"""Client ranges of a handler's layouts, and the order to try the layouts in.

A handler with more than one layout keeps the first layout that reads the file
to its end. The client only orders the tries: the layout whose ranges cover
the effective client goes first, the others follow in their own order (newest
first). The ranges come from the Versions table of the handler's format doc,
which `check_docs.py` writes from the test clients; a layout with no checked
client declares none.

Ordering reads the client as a `client_ranges_dep()` dependency, not the raw
version: the parsed records cache keeps a table while the client stays in the
same layout's range, so a patch does not re-parse it.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import TypeVar

from _common.data_deps import LayoutRanges, client_ranges_dep, covering_layout, note_read
from _common.effective_client import unrecorded_client


@dataclass(frozen=True)
class ClientRange:
    """Client versions `first` to `last`; `last` None is open-ended (the live client)."""

    first: int
    last: int | None = None

    def covers(self, client: int) -> bool:
        return self.first <= client and (self.last is None or client <= self.last)


Layout = TypeVar("Layout")


def _ranges(clients: Sequence[ClientRange]) -> LayoutRanges:
    return tuple((span.first, span.last) for span in clients)


def _covering_index(layouts: Sequence[Layout], clients: Callable[[Layout], Sequence[ClientRange]]) -> int | None:
    ranges = [_ranges(clients(layout)) for layout in layouts]
    note_read(client_ranges_dep(ranges))
    return covering_layout(ranges, unrecorded_client())


def covering(layouts: Sequence[Layout], clients: Callable[[Layout], Sequence[ClientRange]]) -> Layout | None:
    """The first of `layouts` whose `clients` ranges cover the effective client, or None."""
    index = _covering_index(layouts, clients)
    return None if index is None else layouts[index]


def client_order(layouts: Sequence[Layout], clients: Callable[[Layout], Sequence[ClientRange]]) -> list[Layout]:
    """`layouts` with the one whose `clients` ranges cover the effective client first.

    Without a client (no folder, an older exe) or a covering layout, the order
    is unchanged.
    """
    index = _covering_index(layouts, clients)
    if index is None:
        return list(layouts)
    return [layouts[index], *(layout for position, layout in enumerate(layouts) if position != index)]
