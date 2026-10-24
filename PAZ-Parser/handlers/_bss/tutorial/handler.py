"""tutorial.bss preview handler: each Black Spirit guide step with its conditions and text."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from table_sort import TableSort

from _common.html import Column, e, flag_cell, hidden_slice, html_list_cell, icon_cell
from _common.inline_text import decode_inline_text
from _common.pa_text import pa_cell, pa_fields, pa_line_cell
from _common.row_table import RowTableHandler
from _common.ui_texture import ui_texture_path
from .links import start_event_link, step_text
from .parser import FILE_NAME, parse_tutorial_records
from .ui_names import ui_name, ui_names_by_hash


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_MAX_EVENTS = 6


def _step_order(record: dict) -> tuple[int, int]:
    return record["tutorial_type"], record["tutorial_index"]


def _point_text(point: list[float]) -> str:
    return ", ".join(f"{value:g}" for value in point)


def _start_events_cell(keys: list[int]) -> str:
    """Each start event key as a link to its `tutorial_startevent.bss` row, or '-'."""
    if not keys:
        return _EMPTY
    shown = [start_event_link(key) for key in keys[:_MAX_EVENTS]]
    return html_list_cell(shown, len(keys) - _MAX_EVENTS, [str(key) for key in hidden_slice(keys, _MAX_EVENTS)])


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
        ui_names = ui_names_by_hash(strings)
        records = [
            {
                **row,
                "step": step_text(row["tutorial_type"], row["tutorial_index"]),
                **pa_fields("title", row["title_kr"]),
                **pa_fields("desc", decode_inline_text(row["desc_kr"])),
                "start_events_text": ", ".join(str(key) for key in row["start_event_keys"]),
                # The hash in hex when no name fits; None for the screen.
                "base_pos_panel": ui_name(ui_names, row["base_pos_panel_hash"]) or None,
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
            _start_events_cell(record["start_event_keys"]),
            e(record["base_pos_panel"]) if record["base_pos_panel"] else _EMPTY,
            icon_cell(record["image_texture"]) if record["image_texture"] else _EMPTY,
            flag_cell(bool(record["use_popup"])),
        ]
