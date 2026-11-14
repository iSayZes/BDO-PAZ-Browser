"""The two action chart layouts of docs/file-formats/other/actionchart_paac.md.

Layout 2 is client 3258 and later, Layout 1 client 1784. The differences are
data here, so one walk reads both.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from _common.client_versions import ClientRange
from .events import TYPES_1784, TYPES_LIVE


@dataclass(frozen=True)
class ChartLayout:
    number: int
    # Animation, Skeleton and Mesh Group start with an extra string (`DEFAULT`).
    group_strings: bool
    animation_event_size: int
    # Slot Entry count, and the size of each of a Slot's two byte arrays.
    slot_count: int
    hit_part_size: int
    # u16, then three u8 (Layout 1) or two u8 (Layout 2), then a u32.
    package_header_u8_count: int
    event_types: Mapping[int, str]
    # Layout 1 elements are the 1784 loader's; Layout 2 has 33 unknown middle bytes.
    loader_element: bool
    clients: tuple[ClientRange, ...] = ()


LAYOUT_2 = ChartLayout(
    number=2,
    group_strings=True,
    animation_event_size=36,
    slot_count=42,
    hit_part_size=33,
    package_header_u8_count=2,
    event_types=TYPES_LIVE,
    loader_element=False,
    clients=(ClientRange(3258),),
)

LAYOUT_1 = ChartLayout(
    number=1,
    group_strings=False,
    animation_event_size=28,
    slot_count=32,
    hit_part_size=25,
    package_header_u8_count=3,
    event_types=TYPES_1784,
    loader_element=True,
    clients=(ClientRange(1784, 1784),),
)

# Newest first.
LAYOUTS = (LAYOUT_2, LAYOUT_1)
