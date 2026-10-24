"""beginnerroadmapdata.bss preview handler: each roadmap slot with its icon, text and event button."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.html import Column, e, sprite_icon_cell
from _common.inline_text import decode_inline_text
from _common.lang import load_handler_strings
from _common.pa_text import pa_cell, pa_fields, pa_line_cell
from _common.row_table import RowTableHandler
from _common.texture_string import TEXTURE_STRING_COMBINE, TEXTURE_STRING_COMBINE_PATH, icon_fields, parse_texture_regions
from .parser import FILE_NAME, parse_beginnerroadmapdata_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# `-1` marks an unused event parameter (`undefinedLoadMapEventParamValue` in the Lua).
_UNUSED_PARAMETER = -1
# processRoadMapEvent: category 1 opens the UI window its second parameter names.
_OPEN_UI_CATEGORY = 1


def _event_text(parameters: list[int], labels: Mapping[str, str]) -> str:
    """The Lua action of the event parameters, or '' without an event."""
    category, target, *_ = parameters
    if category == _UNUSED_PARAMETER:
        return ""
    if category == _OPEN_UI_CATEGORY:
        return labels.get(str(target), labels["openUi"].format(target=target))
    return labels["category"].format(category=category)


class BeginnerRoadmapHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["roadmapKey"], "num", sort_key="roadmap_key"),
            Column(labels["icon"], sort_key="icon_texture_id"),
            Column(labels["title"], sort_key="title"),
            Column(labels["text"], sort_key="desc"),
            Column(labels["eventName"], sort_key="event_name_kr"),
            Column(labels["event"], sort_key="event_text"),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        return [TEXTURE_STRING_COMBINE_PATH]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        records = parse_beginnerroadmapdata_records(data)
        labels = load_handler_strings(self.lang, _LANG_DIR)["events"]
        textures = parse_texture_regions(companions.get(TEXTURE_STRING_COMBINE), (r["icon_texture_id"] for r in records))
        return [
            {
                **record,
                **pa_fields("title", record["title_kr"]),
                **pa_fields("desc", decode_inline_text(record["desc_kr"])),
                "event_text": _event_text(record["event_parameters"], labels),
                **icon_fields(textures, record["icon_texture_id"]),
            }
            for record in records
        ]

    def cells(self, record: dict) -> list[str]:
        icon = sprite_icon_cell(record["icon_path"], record["icon_region"]) if record["icon_path"] else e(record["icon_texture_id"])
        return [
            e(record["roadmap_key"]),
            icon or _EMPTY,
            pa_cell(record, "title"),
            pa_line_cell(record, "desc"),
            e(record["event_name_kr"]) or _EMPTY,
            e(record["event_text"]) or _EMPTY,
        ]
