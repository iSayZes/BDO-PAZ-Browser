"""contentsschedulerss.bss preview handler: the Contents Schedule window's contents."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _bss.stringtable.parser import RESOURCE_SHEET
from _bss.stringtable.text import STRINGTABLE_FILE, ui_key_hashes, ui_key_text
from _common.contents_group import contents_groups_text
from _common.html import Column, e, sprite_icon_cell
from _common.row_table import RowTableHandler
from _common.texture_string import (
    TEXTURE_STRING_COMBINE,
    TEXTURE_STRING_COMBINE_PATH,
    icon_fields,
    parse_texture_regions,
)
from .parser import FILE_NAME, parse_contentsschedulerss_records


_LANG_DIR = Path(__file__).parent / "lang"


class ContentsSchedulerHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["contentType"], "num", sort_key="content_type"),
            Column(labels["icon"], sort_key="icon_texture"),
            Column(labels["title"], sort_key="title_text"),
            Column(labels["contentsGroups"], sort_key="contents_groups"),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{STRINGTABLE_FILE}", TEXTURE_STRING_COMBINE_PATH]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        records = parse_contentsschedulerss_records(data)
        hashes = ui_key_hashes(companions.get(STRINGTABLE_FILE), [RESOURCE_SHEET])
        textures = parse_texture_regions(companions.get(TEXTURE_STRING_COMBINE), (r["icon_texture"] for r in records))
        return [
            {
                **record,
                # The key itself when LOC has no text for it.
                "title_text": ui_key_text(hashes, RESOURCE_SHEET, record["title"]) or record["title"],
                "contents_groups": contents_groups_text(record["contents_group_hashes"]),
                **icon_fields(textures, record["icon_texture"]),
            }
            for record in records
        ]

    def cells(self, record: dict) -> list[str]:
        icon = sprite_icon_cell(record["icon_path"], record["icon_region"]) if record["icon_path"] else e(record["icon_texture"])
        return [
            e(record["content_type"]),
            icon,
            e(record["title_text"]),
            e(record["contents_groups"]),
        ]
