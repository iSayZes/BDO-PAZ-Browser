"""tutorial.bss preview handler: each Black Spirit guide step with its conditions and text."""
from __future__ import annotations

import re
from collections.abc import Iterable, Mapping
from pathlib import Path

from table_sort import TableSort

from _common.html import Column, e, flag_cell, icon_cell, text_list_cell
from _common.inline_text import decode_inline_text
from _common.pa_text import pa_cell, pa_fields, pa_line_cell
from _common.row_table import RowTableHandler
from _common.string_hash import ascii_key_hash
from _common.ui_texture import ui_texture_path
from .parser import FILE_NAME, parse_tutorial_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_PANEL_NAME_RE = re.compile(r"\bPanel_\w+")
_MAX_EVENTS = 6


def _panel_names(strings: Iterable[str]) -> dict[int, str]:
    """`ascii_key_hash` -> name of every `Panel_*` name the step scripts mention."""
    return {ascii_key_hash(name): name for text in strings for name in _PANEL_NAME_RE.findall(text)}


def _step_order(record: dict) -> tuple[int, int]:
    return record["tutorial_type"], record["tutorial_index"]


def _point_text(point: list[float]) -> str:
    return ", ".join(f"{value:g}" for value in point)


class TutorialHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["tutorialType"], "num", sort_key="tutorial_type"),
            Column(labels["tutorialIndex"], "num", sort_key="tutorial_index"),
            Column(labels["title"], sort_key="title"),
            Column(labels["text"], sort_key="desc"),
            Column(labels["startCondition"], sort_key="start_condition"),
            Column(labels["completeCondition"], sort_key="complete_condition"),
            Column(labels["startEvents"], sort_key="start_events_text"),
            Column(labels["panel"], sort_key="base_pos_panel"),
            Column(labels["image"], sort_key="image_texture"),
            Column(labels["usePopup"], sort_key="use_popup"),
        ]

    def default_sort(self) -> TableSort | None:
        # read_records() orders by tutorial type, then step index; no one column gives that.
        return None

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        rows, strings = parse_tutorial_records(data)
        panels = _panel_names(strings)
        records = [
            {
                **row,
                "step": f"{row['tutorial_type']}.{row['tutorial_index']}",
                **pa_fields("title", row["title_kr"]),
                **pa_fields("desc", decode_inline_text(row["desc_kr"])),
                "start_events_text": ", ".join(str(key) for key in row["start_event_keys"]),
                # The hash itself when no step script names the panel; None for the screen.
                "base_pos_panel": panels.get(row["base_pos_panel_hash"], str(row["base_pos_panel_hash"]))
                if row["base_pos_panel_hash"]
                else None,
                "pos_text": _point_text(row["pos"]),
                "pan_text": _point_text(row["pan"]),
                "image_texture": ui_texture_path(row["image_path"]),
            }
            for row in rows
        ]
        return sorted(records, key=_step_order)

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["tutorial_type"]),
            e(record["tutorial_index"]),
            pa_cell(record, "title"),
            pa_line_cell(record, "desc"),
            e(record["start_condition"]) or _EMPTY,
            e(record["complete_condition"]) or _EMPTY,
            text_list_cell(record["start_event_keys"], _MAX_EVENTS) or _EMPTY,
            e(record["base_pos_panel"]) if record["base_pos_panel"] else _EMPTY,
            icon_cell(record["image_texture"]) if record["image_texture"] else _EMPTY,
            flag_cell(bool(record["use_popup"])),
        ]
