"""instancefieldrankingmanage.bss preview handler: the season rankings with their times and names."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import STRINGTABLE_FILE, ui_key_hashes, ui_key_text
from _common.html import Column, e
from _common.row_table import RowTableHandler
from _common.utc_time import utc_text
from .parser import FILE_NAME, parse_instancefieldrankingmanage_records


_LANG_DIR = Path(__file__).parent / "lang"


class InstanceFieldRankingManageHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["rankingIdx"], "num", sort_key="ranking_idx"),
            Column(labels["instanceType"], "num", sort_key="instance_type"),
            Column(labels["start"], sort_key="start_date_rank"),
            Column(labels["end"], sort_key="end_date_rank"),
            Column(labels["season"], sort_key="season"),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{STRINGTABLE_FILE}"]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        hashes = ui_key_hashes(companions.get(STRINGTABLE_FILE), [GAME_SHEET])
        return [
            {
                **record,
                "start_text": utc_text(record["start_date_rank"]),
                "end_text": utc_text(record["end_date_rank"]),
                # The key itself when LOC has no text for it.
                "season": ui_key_text(hashes, GAME_SHEET, record["ranking_name_key"]) or record["ranking_name_key"],
            }
            for record in parse_instancefieldrankingmanage_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["ranking_idx"]),
            e(record["instance_type"]),
            e(record["start_text"]),
            e(record["end_text"]),
            e(record["season"]),
        ]
