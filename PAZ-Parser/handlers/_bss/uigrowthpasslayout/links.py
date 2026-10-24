"""The `growthpasslinkdata.bss` guide links of a quest cell.

The window shows `Button_GuideLink1` to `Button_GuideLink3` on a quest cell
for the links `growthpasslinkdata.bss` holds under the cell's quest chain and
quest ID (`panel_window_growthpass_1.luac`). Every service type's links are
listed, each address once; line cells get none.
"""

from __future__ import annotations

from collections.abc import Mapping

from _bss.growthpasslinkdata.parser import quest_link_addresses

LINKS_FIELD = "links"

QuestLinkIndex = Mapping[tuple[int, int], tuple[str, ...]]


def read_quest_links(data: bytes | None) -> QuestLinkIndex:
    """(quest chain, quest ID) -> link addresses from the optional companion;
    empty when it is missing or unreadable, since the links are only a
    convenience on the grid."""
    if data is None:
        return {}
    try:
        return quest_link_addresses(data)
    except ValueError:
        return {}


def cell_links(links: QuestLinkIndex, quest_chain_id: int, quest_id: int) -> list[str]:
    """The link addresses of one cell's quest, or [] for a cell without a quest or links."""
    return list(links.get((quest_chain_id, quest_id), ()))
