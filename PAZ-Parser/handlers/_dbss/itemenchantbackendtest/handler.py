from __future__ import annotations

from bdo_models import PazEntry

from _dbss.itemenchant.handler import ItemEnchantHandler
from .parser import parse_itemenchantbackendtest_records


class ItemEnchantBackendTestHandler(ItemEnchantHandler):
    """The itemenchant.dbss view of the block fronts this file stores, without the crystal group."""

    shows_crystal_group = False

    def companions(self, entry: PazEntry) -> list[str]:
        return []

    def parsed_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_itemenchantbackendtest_records(data)
