"""The documented itemenchant.dbss block layouts, and which one a file has.

The parser reads every block with the layout picked here. The pick tries
the layouts in client order (`client_versions.py`) on the first base blocks
inside the file and keeps the first that reads all of them: Layout 1 must walk
each block to its last byte, and Layout 2 to the end of its Message Tail part
inside it (its tail is not decoded). One block is not enough: on client 1784,
2,050 of the 42,559 base blocks also pass the Layout 2 walk.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass

from _common.client_versions import ClientRange, client_order
from .layout_1 import read_block as read_layout_1_block
from .layout_2 import front_end


@dataclass(frozen=True)
class BlockLayout:
    """One documented block shape; `number` is its Layout N in the doc."""

    number: int
    # Reads the block [start, end) of `data`; raises ValueError when it does not fit.
    check: Callable[[bytes, int, int], object]
    # Test clients this layout reads (the doc's Versions table, written by
    # check_docs); they only order the tries (`client_versions.py`).
    clients: tuple[ClientRange, ...] = ()


LAYOUT_2 = BlockLayout(2, front_end, clients=(ClientRange(3387),))
LAYOUT_1 = BlockLayout(1, read_layout_1_block, clients=(ClientRange(1754, 1784),))
# Newest first.
LAYOUTS = (LAYOUT_2, LAYOUT_1)

# How many base blocks a layout must read to be picked.
_SAMPLE_BLOCKS = 8


def _break(layout: BlockLayout, data: bytes, sample: Sequence[dict]) -> str | None:
    """Where `layout` fails on the `sample` rows, or None when it reads them all."""
    for row in sample:
        start = row["data_offset"]
        try:
            layout.check(data, start, start + row["data_size"])
        except ValueError as error:
            return f"Layout {layout.number}: key {row['key']}: {error}"
    return None


def _sample(data: bytes, base_rows: Sequence[dict]) -> list[dict]:
    """The first `_SAMPLE_BLOCKS` rows whose block lies inside the file."""
    sample: list[dict] = []
    for row in base_rows:
        if len(sample) == _SAMPLE_BLOCKS:
            break
        if row["data_offset"] + row["data_size"] <= len(data):
            sample.append(row)
    return sample


def block_layout(data: bytes, base_rows: Sequence[dict]) -> BlockLayout:
    """The layout of the file `data`, from its level-0 offset rows `base_rows`.

    Rows whose block runs past the file are left out of the sample. Raises
    ValueError, naming where each layout broke, when none fits.
    """
    sample = _sample(data, base_rows)
    breaks: list[str] = []
    for layout in client_order(LAYOUTS, lambda layout: layout.clients):
        broke = _break(layout, data, sample)
        if broke is None:
            return layout
        breaks.append(broke)
    raise ValueError(f"itemenchant.dbss fits no known layout ({'; '.join(breaks)})")
