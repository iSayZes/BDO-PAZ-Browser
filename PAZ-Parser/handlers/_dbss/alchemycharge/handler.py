"""alchemycharge.dbss preview handler."""
from __future__ import annotations

from pathlib import Path

from _common.offset_table import OffsetTableHandler
from _dbss.alchemystone.handler import StoneMaterialHandler, stone_offset_handler
from .parser import OFFSET_FILE, parse_alchemycharge_records


_LANG_DIR = Path(__file__).parent / "lang"


def alchemy_charge_offset_handler() -> OffsetTableHandler:
    return stone_offset_handler(OFFSET_FILE)


class AlchemyChargeHandler(StoneMaterialHandler):
    def __init__(self) -> None:
        super().__init__(_LANG_DIR, parse_alchemycharge_records, "charge_point", "chargePoint")
