"""moonblessingss.dbss preview handler: one row per Pearl spending level of each Moon's Blessing event."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from table_sort import TableSort

from _bss.pabr_values.names import utc_time
from _common.html import Column, e
from _common.pa_text import pa_fields, pa_line_cell
from _common.quest.reward_text import reward_texts, rewards_cell
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_moonblessingss_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_SEPARATOR = ", "


def _text_cell(text: str) -> str:
    return e(text) if text else _EMPTY


class MoonBlessingHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["key"], "num", sort_key=KEY_FIELD),
            Column(labels["start"], sort_key="start_time"),
            Column(labels["end"], sort_key="end_time"),
            Column(labels["maxPearl"], "num", sort_key="max_used_pearl"),
            Column(labels["level"], "num", sort_key="level_no"),
            Column(labels["title"], sort_key="title_kr"),
            Column(labels["targetPearl"], "num", sort_key="target_used_pearl"),
            Column(labels["rewards"], sort_key="rewards_text"),
            Column(labels["description"], sort_key="description"),
        ]

    def default_sort(self) -> TableSort | None:
        # File order: each event's levels from the lowest Pearl target up.
        return None

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                **pa_fields("description", record["description_kr"]),
                "rewards_text": _LIST_SEPARATOR.join(reward_texts(record["base_rewards"])),
            }
            for record in parse_moonblessingss_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(utc_time(record["start_time"])),
            e(utc_time(record["end_time"])),
            e(f"{record['max_used_pearl']:,}"),
            e(record["level_no"]),
            _text_cell(record["title_kr"]),
            e(f"{record['target_used_pearl']:,}"),
            rewards_cell(record["base_rewards"]) or _EMPTY,
            pa_line_cell(record, "description"),
        ]
