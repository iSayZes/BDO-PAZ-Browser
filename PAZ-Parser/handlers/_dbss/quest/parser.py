"""`quest.dbss`: quest definitions, read in `allquestlist.bss` order.

Two layouts, newest first: Layout 2 of the live client (`layout2.py`), whose
walk scans for each record's packed quest ID, and Layout 1 of clients 1717 to
2000 (`layout1.py`), read field by field. `build_quest_index` keeps the first
that reads the whole file; the other functions dispatch on the index it returns.
Full layouts in docs/file-formats/dbss/quest_dbss.md.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from _bss.allquestlist.parser import parse_allquestlist_records
from _common.client_versions import ClientRange, client_order
from _common.ui_texture import ui_texture_path
from .layout1 import QuestIndexLayout1, build_quest_index_layout1, parse_quest_record_layout1
from .layout2 import (
    QuestIndexLayout2,
    build_quest_index_layout2,
    parse_quest_record_layout2,
    quest_icon_path_layout2,
)
from .model import QuestRecord


QuestIndex = QuestIndexLayout2 | QuestIndexLayout1


@dataclass(frozen=True)
class _Layout:
    """One documented Record shape and the walk that indexes it."""

    number: int
    build_index: Callable[[bytes, list[int]], QuestIndex]
    # Test clients this layout reads (the doc's Versions table, written by
    # check_docs); they only order the tries (`client_versions.py`).
    clients: tuple[ClientRange, ...] = ()


# Newest first. Layout 2 declares no clients: check_docs cannot walk its
# scanned fields, so no test client is checked against it.
_LAYOUTS = (
    _Layout(2, build_quest_index_layout2),
    _Layout(1, build_quest_index_layout1, clients=(ClientRange(1717, 2000),)),
)


def build_quest_index(data: bytes, allquestlist_ids: list[int]) -> QuestIndex:
    """Walk every record with the first layout that reads the whole file.

    Raises ValueError, naming where each layout broke, when none fits.
    """
    breaks: list[str] = []
    for layout in client_order(_LAYOUTS, lambda layout: layout.clients):
        try:
            return layout.build_index(data, allquestlist_ids)
        except ValueError as error:
            breaks.append(f"Layout {layout.number}: {error}")
    raise ValueError(f"quest.dbss fits no known layout ({'; '.join(breaks)})")


def parse_quest_record(data: bytes, index: QuestIndex, row: int) -> QuestRecord:
    if isinstance(index, QuestIndexLayout1):
        return parse_quest_record_layout1(data, index, row)
    return parse_quest_record_layout2(data, index, row)


def _quest_icon_path(data: bytes, index: QuestIndex, row: int) -> str:
    if isinstance(index, QuestIndexLayout1):
        return parse_quest_record_layout1(data, index, row)["icon_path"]
    return quest_icon_path_layout2(data, index, row)


def build_quest_icon_index(data: bytes, allquestlist_data: bytes) -> dict[int, str]:
    """Map packed quest ID to icon path.

    `allquestlist.bss` names the record order the walk needs.
    """
    ids = [record["packed_quest_id"] for record in parse_allquestlist_records(allquestlist_data)]
    index = build_quest_index(data, ids)
    icons: dict[int, str] = {}
    for row, packed_quest_id in enumerate(index.packed_quest_ids):
        icon = _quest_icon_path(data, index, row)
        if icon:
            # A few stored paths carry a doubled separator, such as
            # "Icon/Quest//lost_wagon.dds", which can never match a PAZ entry.
            icons[packed_quest_id] = ui_texture_path(icon.replace("//", "/"))
    return icons
