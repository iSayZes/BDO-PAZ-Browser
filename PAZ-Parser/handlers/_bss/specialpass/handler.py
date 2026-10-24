"""specialpass.bss preview handler: one row per reward step of each Special Pass."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from table_sort import TableSort

from _bss.pabr_values.names import utc_time
from _common.html import Column, e
from _common.item_key import item_count_list_cell, item_count_text
from _common.lang import load_handler_strings
from _common.pa_text import pa_fields, pa_line_cell
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_specialpass_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _reward_text(item_key: int, count: int) -> str:
    return item_count_text(item_key, count) if item_key else ""


def _reward_cell(item_key: int, count: int) -> str:
    return item_count_list_cell([(item_key, count)]) if item_key else _EMPTY


def _content_type_name(type_names: Mapping[str, str], content_type: int | None) -> str | None:
    """The lang label of a content type, its number when it has none, None for a step without a row."""
    if content_type is None:
        return None
    return type_names.get(str(content_type)) or str(content_type)


def _time_cell(seconds: int | None) -> str:
    return e(utc_time(seconds)) if seconds is not None else _EMPTY


def _text_cell(text: str | None) -> str:
    return e(text) if text else _EMPTY


class SpecialPassHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["passKey"], "num", sort_key=KEY_FIELD),
            Column(labels["contentType"], sort_key="content_type_name"),
            Column(labels["title"], sort_key="title_kr"),
            Column(labels["start"], sort_key="start_time"),
            Column(labels["end"], sort_key="end_time"),
            Column(labels["saleEnd"], sort_key="sale_end_time"),
            Column(labels["step"], "num", sort_key="step_no"),
            Column(labels["passPoints"], "num", sort_key="reward_point"),
            Column(labels["basicReward"], sort_key="basic_reward"),
            Column(labels["passReward"], sort_key="pass_reward"),
            Column(labels["description"], sort_key="description"),
        ]

    def default_sort(self) -> TableSort | None:
        # File order: each pass's steps from the first up.
        return None

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        type_names = load_handler_strings(self.lang, _LANG_DIR)["contentTypes"]
        return [
            {
                **record,
                "content_type_name": _content_type_name(type_names, record["content_type"]),
                "basic_reward": _reward_text(record["basic_item_key"], record["basic_item_count"]),
                "pass_reward": _reward_text(record["pass_item_key"], record["pass_item_count"]),
                **pa_fields("description", record["description_kr"]),
            }
            for record in parse_specialpass_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            _text_cell(record["content_type_name"]),
            _text_cell(record["title_kr"]),
            _time_cell(record["start_time"]),
            _time_cell(record["end_time"]),
            _time_cell(record["sale_end_time"]),
            e(record["step_no"]),
            e(f"{record['reward_point']:,}"),
            _reward_cell(record["basic_item_key"], record["basic_item_count"]),
            _reward_cell(record["pass_item_key"], record["pass_item_count"]),
            pa_line_cell(record, "description"),
        ]
