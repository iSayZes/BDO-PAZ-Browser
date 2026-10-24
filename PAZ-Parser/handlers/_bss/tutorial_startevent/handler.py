"""tutorial_startevent.bss preview handler: one row per start event.

Panel and control hashes show as names: the UI names the `tutorial.bss`
step scripts mention, plus the few in `_bss/tutorial/ui_names.py`. The
`tutorial.bss` companion also gives the steps that start each event; each
links to its step row, and the step rows link back here.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _bss.tutorial.links import TUTORIAL_FILE, step_link, steps_by_start_event
from _bss.tutorial.parser import parse_tutorial_records
from _bss.tutorial.ui_names import ui_name, ui_names_by_hash
from _common.html import Column, e, flag_cell, html_list_cell
from _common.item_key import item_key_list_cell, item_key_text
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_tutorial_startevent_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _control_text(names: dict[int, str], control_hash: int, control_index: int) -> str:
    """`Template_Button_Unseal [2]`: a child control and, past `0`, which of its copies."""
    name = ui_name(names, control_hash)
    return f"{name} [{control_index}]" if control_index else name


def _highlight_text(names: dict[int, str], highlight: dict) -> str:
    """`Panel_Widget_ServantIcon / Button_Icon_10, offset 55, 55`, or '' when the frame is off."""
    if not highlight["use_bg"]:
        return ""
    target = [ui_name(names, highlight["panel_hash"])]
    if highlight["child_control_hash"]:
        target.append(_control_text(names, highlight["child_control_hash"], highlight["child_control_index"]))
    parts = [" / ".join(name for name in target if name)]
    offset_x, offset_y = highlight["offset"]
    if offset_x or offset_y:
        parts.append(f"offset {offset_x:g}, {offset_y:g}")
    return ", ".join(part for part in parts if part)


def _selected_text(names: dict[int, str], record: dict) -> str:
    """`Panel_Window_PetList_All: Static_FeedingBg, Button_FeedOne`, or '' with no panel."""
    panel = ui_name(names, record["selected_panel_hash"])
    if not panel:
        return ""
    controls = [
        _control_text(names, control["child_control_hash"], control["child_control_index"])
        for control in record["selected_controls"]
        if control["child_control_hash"]
    ]
    return f"{panel}: {', '.join(controls)}" if controls else panel


class TutorialStartEventBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{TUTORIAL_FILE}"]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["key"], "num", sort_key="key"),
            Column(labels["itemWhereType"], "num", sort_key="item_where_type"),
            Column(labels["item"], sort_key="item_name"),
            Column(labels["blackBg"], sort_key="black_bg_text"),
            Column(labels["whiteBg"], sort_key="white_bg_text"),
            Column(labels["whiteIgnore"], sort_key="white_ignore"),
            Column(labels["selected"], sort_key="selected_text"),
            Column(labels["snappingEffect"], sort_key="snapping_effect_on"),
            Column(labels["doLua"], sort_key="do_lua"),
            Column(labels["steps"], sort_key="steps_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        tutorial = companions.get(TUTORIAL_FILE)
        steps, strings = parse_tutorial_records(tutorial) if tutorial else ([], [])
        names = ui_names_by_hash(strings)
        steps_by_event = steps_by_start_event(steps)
        records = []
        for record in parse_tutorial_startevent_records(data):
            event_steps = steps_by_event.get(record["key"], [])
            records.append({
                **record,
                "item_name": item_key_text(record["item_key"]) if record["item_key"] else "",
                "black_bg_text": _highlight_text(names, record["black_bg"]),
                "white_bg_text": _highlight_text(names, record["white_bg"]),
                "selected_text": _selected_text(names, record),
                "steps": event_steps,
                "steps_text": ", ".join(event_steps),
            })
        return records

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["key"]),
            e(record["item_where_type"]),
            item_key_list_cell([record["item_key"]], 1) if record["item_key"] else _EMPTY,
            e(record["black_bg_text"] or _EMPTY),
            e(record["white_bg_text"] or _EMPTY),
            flag_cell(bool(record["white_ignore"])),
            e(record["selected_text"] or _EMPTY),
            flag_cell(bool(record["snapping_effect_on"])),
            e(record["do_lua"] or _EMPTY),
            html_list_cell([step_link(step) for step in record["steps"]]) or _EMPTY,
        ]
