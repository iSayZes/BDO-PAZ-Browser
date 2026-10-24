"""minigamefindtool.dbss preview handler: the Lakiaro minigame hoe values per item grade and enhancement level."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from table_sort import TableSort

from _common.enchant_level import enchant_level_text
from _common.html import Column, e
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_minigamefindtool, parse_minigamefindtooloffset


_LANG_DIR = Path(__file__).parent / "lang"


def minigame_find_tool_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("item_grade", "itemGrade"),
            OffsetColumn("enchant_level", "enchantLevel"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        _offset_records,
    )


def _offset_records(data: bytes) -> list[dict]:
    return [row._asdict() for row in parse_minigamefindtooloffset(data)]


def level_text(enchant_level: int) -> str:
    """`+0`, `+7` or `PEN`."""
    return enchant_level_text(enchant_level) or f"+{enchant_level}"


class MiniGameFindToolHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def default_sort(self) -> TableSort | None:
        # The file order is grade, then level: no single field gives it.
        return None

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["itemGrade"], "num", sort_key="item_grade"),
            Column(labels["enchantLevel"], "num", sort_key="enchant_level"),
            Column(labels["rClickCount"], "num", sort_key="r_click_count"),
            Column(labels["openSlotCount"], "num", sort_key="open_slot_count"),
            Column(labels["decreaseDamageRate"], "num", sort_key="decrease_damage_rate"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "enchant_level_text": level_text(record["enchant_level"])}
            for record in parse_minigamefindtool(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["item_grade"]),
            e(record["enchant_level_text"]),
            e(record["r_click_count"]),
            e(record["open_slot_count"]),
            e(f"{record['decrease_damage_rate']:,}"),
        ]
