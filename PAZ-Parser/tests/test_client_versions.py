"""Client ranges of multi-layout handlers and the try order they give."""
from __future__ import annotations

from collections.abc import Sequence

import pytest

from bdo_preview import set_handler_client
from _common.client_versions import ClientRange, client_order
from _common.data_deps import CLIENT, client_ranges_dep, client_ranges_digest, recording
from _bss.privateskill.parser import LAYOUTS as PRIVATESKILL_LAYOUTS
from _bss.sequencetriggerdata.parser import LAYOUTS as SEQUENCETRIGGERDATA_LAYOUTS
from _bss.territoryinfo.parser import LAYOUTS as TERRITORYINFO_LAYOUTS
from _dbss.guildquest.parser import LAYOUTS as GUILDQUEST_LAYOUTS, parse_guildquest_records
from _dbss.itemenchant.layouts import LAYOUTS as ITEMENCHANT_LAYOUTS
from _dbss.journalquest.parser import LAYOUTS as JOURNALQUEST_LAYOUTS
from _dbss.quest.parser import _LAYOUTS as QUEST_LAYOUTS


_OLD = (ClientRange(1194, 1261),)
_LIVE = (ClientRange(1267),)
# Newest first, as handlers list them.
_LAYOUTS = (("Layout 2", _LIVE), ("Layout 1", _OLD))
_HANDLER_LAYOUTS = {
    "privateskill.bss": PRIVATESKILL_LAYOUTS,
    "sequencetriggerdata.bss": SEQUENCETRIGGERDATA_LAYOUTS,
    "territoryinfo.bss": TERRITORYINFO_LAYOUTS,
    "guildquest.dbss": GUILDQUEST_LAYOUTS,
    "itemenchant.dbss": ITEMENCHANT_LAYOUTS,
    "journalquest.dbss": JOURNALQUEST_LAYOUTS,
    "quest.dbss": QUEST_LAYOUTS,
}


def _names(layouts: Sequence[tuple[str, tuple[ClientRange, ...]]]) -> list[str]:
    return [name for name, _clients in client_order(layouts, lambda layout: layout[1])]


def _ranges(clients: tuple[ClientRange, ...]) -> tuple[tuple[int, int | None], ...]:
    return tuple((span.first, span.last) for span in clients)


def test_a_range_covers_its_ends_and_an_open_range_every_later_client() -> None:
    assert ClientRange(1194, 1261).covers(1194) and ClientRange(1194, 1261).covers(1261)
    assert not ClientRange(1194, 1261).covers(1262)
    assert ClientRange(1267).covers(9999) and not ClientRange(1267).covers(1266)


def test_without_a_client_the_newest_layout_goes_first() -> None:
    assert _names(_LAYOUTS) == ["Layout 2", "Layout 1"]


def test_the_layout_covering_the_client_goes_first() -> None:
    set_handler_client(1200)
    assert _names(_LAYOUTS) == ["Layout 1", "Layout 2"]

    set_handler_client(1100)  # covered by no layout
    assert _names(_LAYOUTS) == ["Layout 2", "Layout 1"]


def test_ordering_records_the_ranges_not_the_raw_client() -> None:
    with recording() as deps:
        _names(_LAYOUTS)

    assert deps == {client_ranges_dep([_ranges(_LIVE), _ranges(_OLD)])}
    assert CLIENT not in deps


def test_the_ranges_digest_changes_only_when_the_client_leaves_its_range() -> None:
    name = client_ranges_dep([_ranges(_LIVE), _ranges(_OLD)])

    assert client_ranges_digest(name, 3483) == client_ranges_digest(name, 3484)
    assert client_ranges_digest(name, 1200) != client_ranges_digest(name, 3483)
    assert client_ranges_digest(name, 1100) == client_ranges_digest(name, None)


@pytest.mark.parametrize("file_name", sorted(_HANDLER_LAYOUTS))
def test_no_client_falls_in_two_layouts_of_one_handler(file_name: str) -> None:
    spans = sorted(
        (span.first, span.last if span.last is not None else 10**9, layout.number)
        for layout in _HANDLER_LAYOUTS[file_name]
        for span in layout.clients
    )
    for (first, last, number), (next_first, _next_last, next_number) in zip(spans, spans[1:]):
        assert last < next_first, f"{file_name}: Layout {number} and Layout {next_number} share clients"


def test_a_handler_tries_the_layout_of_its_client_first() -> None:
    set_handler_client(1784)  # guildquest Layout 1 covers 1598 to 2545

    with pytest.raises(ValueError, match=r"fits no known layout \(Layout 1: .*; Layout 2: "):
        parse_guildquest_records(b"\x01\x00")
