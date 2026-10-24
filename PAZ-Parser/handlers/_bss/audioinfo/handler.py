"""audioinfo.bss preview handler: music and ambience per audio map colour, special states and radio channels."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from _dbss.dyeingpalette.display import color_cell
from .bgm_states import bgm_states_cell
from .parser import FILE_NAME, SECTION_AREA, parse_audioinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _color_hex(color: int) -> str:
    """`#RRGGBB` of a `0x00RRGGBB` colour."""
    return f"#{color:06X}"


def _with_display_fields(record: dict, section_names: Mapping[str, str]) -> dict:
    """The record with every column's field, None where its section has no such value."""
    section = record["section"]
    is_area = section == SECTION_AREA
    return {
        **record,
        "section_name": section_names.get(section, section),
        "color_hex": _color_hex(record["color"]) if is_area else None,
        "state_group_text": record.get("state_group_text"),
        "states_text": record["bgm_states_text"] if is_area else record.get("state_name_text"),
        "bank_no_environment": record.get("bank_no_environment"),
        "channel_name_text": record.get("channel_name_text"),
        "event_name_text": record.get("event_name_text"),
    }


def _text_cell(value: object) -> str:
    return e(value if value not in (None, "") else _EMPTY)


class AudioInfoBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["color"], sort_key="color_hex"),
            Column(labels["section"], sort_key="section_name"),
            Column(labels["stateGroup"], sort_key="state_group_text"),
            Column(labels["states"], sort_key="states_text"),
            Column(labels["bankNoEnvironment"], "num", sort_key="bank_no_environment"),
            Column(labels["channelName"], sort_key="channel_name_text"),
            Column(labels["eventName"], sort_key="event_name_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        section_names: Mapping[str, str] = load_handler_strings(self.lang, _LANG_DIR)["sections"]
        return [_with_display_fields(record, section_names) for record in parse_audioinfo_records(data)]

    def cells(self, record: dict) -> list[str]:
        section = record["section"]
        if section == SECTION_AREA:
            states = bgm_states_cell(record["bgm_state_names"])
        else:
            states = _text_cell(record["states_text"])
        return [
            color_cell(record["color_hex"]),
            e(record["section_name"]),
            _text_cell(record["state_group_text"]),
            states,
            _text_cell(record["bank_no_environment"]),
            _text_cell(record["channel_name_text"]),
            _text_cell(record["event_name_text"]),
        ]

