"""socialaction.dbss preview handler: the social actions with their chat commands, icons and unlock texts."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.contents_group import contents_groups_text
from _common.html import Column, e, icon_cell, truncate
from _common.loc import loc_tagged, resolve_text_binds
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.pa_text import pa_fields, pa_line_cell, strip_pa_tags
from _common.row_table import RowTableHandler
from _common.ui_texture import UI_TEXTURE_ICON_ROOT, ui_texture_path
from .parser import FILE_NAME, KEY_FIELD, parse_socialaction_records, parse_socialactionoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# LOC type 15: str_id1 = social_action_key; str_id4 picks the text.
LOC_SOCIAL_ACTION = 15
LOC_NAME = 0
LOC_COMMAND = 1
LOC_KEYWORDS = 2
LOC_CONDITION_MESSAGE = 3
# Condition scripts run to 1,257 characters; the cell shows the start.
_CONDITION_CHARS = 120


def social_action_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_socialactionoffset_rows, KEY_FIELD, "socialActionKey")


def _loc_or_korean(key: int, str_id4: int, korean: str) -> str:
    """The LOC type 15 text with its PA tags, else the Korean text with its TextBinds filled."""
    return loc_tagged(LOC_SOCIAL_ACTION, key, str_id4) or resolve_text_binds(korean).strip()


def _text_cell(text: str) -> str:
    return e(text) if text else _EMPTY


class SocialActionHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["socialActionKey"], "num", sort_key=KEY_FIELD),
            Column(labels["name"], sort_key="name"),
            Column(labels["condition"], sort_key="condition"),
            Column(labels["command"], sort_key="command"),
            Column(labels["keywords"], sort_key="keywords"),
            Column(labels["action"], sort_key="action_name"),
            Column(labels["icon"], sort_key="icon_path"),
            Column(labels["conditionMessage"], sort_key="condition_message"),
            Column(labels["contentsGroups"], sort_key="contents_groups"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        records = []
        for record in parse_socialaction_records(data):
            key = record[KEY_FIELD]
            records.append(
                {
                    **record,
                    "name": strip_pa_tags(_loc_or_korean(key, LOC_NAME, record["name_kr"])).strip(),
                    "command": strip_pa_tags(_loc_or_korean(key, LOC_COMMAND, record["chatting_command_kr"])).strip(),
                    "keywords": strip_pa_tags(_loc_or_korean(key, LOC_KEYWORDS, record["chatting_keywords_kr"])).strip(),
                    **pa_fields(
                        "condition_message",
                        _loc_or_korean(key, LOC_CONDITION_MESSAGE, record["condition_message_kr"]),
                    ),
                    "contents_groups": contents_groups_text(record["contents_group_hashes"]),
                    "_icon_file": ui_texture_path(record["icon_path"], UI_TEXTURE_ICON_ROOT),
                }
            )
        return records

    def cells(self, record: dict) -> list[str]:
        condition = record["condition"]
        return [
            e(record[KEY_FIELD]),
            _text_cell(record["name"]),
            f'<span title="{e(condition)}">{e(truncate(condition, _CONDITION_CHARS))}</span>' if condition else _EMPTY,
            _text_cell(record["command"]),
            _text_cell(record["keywords"]),
            _text_cell(record["action_name"]),
            icon_cell(record["_icon_file"]),
            pa_line_cell(record, "condition_message"),
            _text_cell(record["contents_groups"]),
        ]
