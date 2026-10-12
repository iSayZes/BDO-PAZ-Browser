"""alchemyupgrade.dbss preview handler."""
from __future__ import annotations

from pathlib import Path

from _common.offset_table import OffsetTableHandler
from _dbss.alchemystone.handler import StoneMaterialHandler, stone_offset_handler
from .parser import EXPERIENCE_PER_PERCENT, OFFSET_FILE, parse_alchemyupgrade_records


_LANG_DIR = Path(__file__).parent / "lang"


def experience_text(experience: int) -> str:
    """EXP per material as the window shows a stone's EXP, `20408` as `2.0408%`."""
    return f"{experience / EXPERIENCE_PER_PERCENT:g}%"


def alchemy_upgrade_offset_handler() -> OffsetTableHandler:
    return stone_offset_handler(OFFSET_FILE)


class AlchemyUpgradeHandler(StoneMaterialHandler):
    def __init__(self) -> None:
        super().__init__(_LANG_DIR, parse_alchemyupgrade_records, "experience", "experience", experience_text)
