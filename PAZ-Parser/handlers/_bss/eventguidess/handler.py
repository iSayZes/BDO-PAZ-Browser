"""eventguidess.bss preview handler: each Event Guide event with its period, button and rewards."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.html import Column, e, sprite_icon_cell
from _common.inline_text import decode_inline_text
from _common.item_key import item_key_list_cell, item_key_text
from _common.pa_text import pa_cell, pa_fields, pa_line_cell
from _common.row_table import RowTableHandler
from _common.texture_string import TEXTURE_STRING_COMBINE, TEXTURE_STRING_COMBINE_PATH, icon_fields, parse_texture_regions
from _common.utc_time import utc_text
from .parser import FILE_NAME, KEY_FIELD, parse_eventguidess_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_MAX_REWARDS = 4


class EventGuideHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["eventKey"], "num", sort_key=KEY_FIELD),
            Column(labels["icon"], sort_key="icon"),
            Column(labels["title"], sort_key="title"),
            Column(labels["text"], sort_key="sub_desc"),
            Column(labels["start"], sort_key="start_time"),
            Column(labels["end"], sort_key="end_time"),
            Column(labels["button"], sort_key="function_desc_kr"),
            Column(labels["function"], sort_key="function"),
            Column(labels["tag"], "num", sort_key="tag"),
            Column(labels["rewards"], sort_key="reward_names"),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        return [TEXTURE_STRING_COMBINE_PATH]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        records = parse_eventguidess_records(data)
        textures = parse_texture_regions(companions.get(TEXTURE_STRING_COMBINE), (r["icon"] for r in records))
        return [
            {
                **record,
                **pa_fields("title", record["main_title_kr"]),
                **pa_fields("sub_desc", decode_inline_text(record["sub_desc_kr"])),
                "start_text": utc_text(record["start_time"]),
                "end_text": utc_text(record["end_time"]),
                "reward_names": [item_key_text(item_key) for item_key in record["rewards"]],
                **icon_fields(textures, record["icon"]),
            }
            for record in records
        ]

    def cells(self, record: dict) -> list[str]:
        icon = sprite_icon_cell(record["icon_path"], record["icon_region"]) if record["icon_path"] else e(record["icon"])
        return [
            e(record[KEY_FIELD]),
            icon or _EMPTY,
            pa_cell(record, "title"),
            pa_line_cell(record, "sub_desc"),
            e(record["start_text"]),
            e(record["end_text"]),
            e(record["function_desc_kr"]) or _EMPTY,
            e(record["function"]) or _EMPTY,
            e(record["tag"]),
            item_key_list_cell(record["rewards"], _MAX_REWARDS) or _EMPTY,
        ]
