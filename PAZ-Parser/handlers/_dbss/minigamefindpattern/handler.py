"""minigamefindpattern.dbss preview handler: the Lakiaro minigame tile patterns, one row per slot and pattern."""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

from table_sort import TableSort

from _common.html import Column, e, sprite_icon_cell, text_list_cell
from _common.lang import load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.row_table import RowTableHandler
from _common.ui_texture import ui_texture_path
from .parser import DIRECTION_COUNT, FILE_NAME, parse_minigamefindpattern, parse_minigamefindpatternoffset


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 8
# The image path a direction-only row (slots 101 and 102) stores.
_NO_IMAGE = "None"
_DIRECTION_KEYS = ("left", "right", "top", "bottom")


def pattern_image_path(stored: str) -> str:
    """PAZ path of a stored `New_UI_Common_forLua\\...` image path, or '' for none."""
    if not stored or stored == _NO_IMAGE:
        return ""
    return ui_texture_path(stored.replace("\\", "/"))


def minigame_find_pattern_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("slot_index", "slotIndex"),
            OffsetColumn("pattern_index", "patternIndex"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        _offset_records,
    )


def _offset_records(data: bytes) -> list[dict]:
    return [row._asdict() for row in parse_minigamefindpatternoffset(data)]


class MiniGameFindPatternHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def default_sort(self) -> TableSort | None:
        # The records come sorted by slot, then pattern: no single field gives that order.
        return None

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["slotIndex"], "num", sort_key="slot_index"),
            Column(labels["patternIndex"], "num", sort_key="pattern_index"),
            Column(labels["image"]),
            Column(labels["image2"]),
            Column(labels["rootSize"], "num", sort_key="root_size"),
            Column(labels["changePattern"], "num", sort_key="change_pattern"),
            Column(labels["rootBeginNo"], "num", sort_key="root_begin_no"),
            Column(labels["endDirection"], sort_key="next_pattern_end_direction"),
            Column(labels["beginDirection"]),
            # A list column: it would only sort by its string form.
            Column(labels["nextPatterns"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        directions = load_handler_strings(self.lang, _LANG_DIR)["directions"]
        names = [directions[key] for key in _DIRECTION_KEYS]
        records = sorted(parse_minigamefindpattern(data), key=lambda r: (r["slot_index"], r["pattern_index"]))
        return [_pattern_fields(record, names) for record in records]

    def cells(self, record: dict) -> list[str]:
        region = record["slot_coordinate"]
        return [
            e(record["slot_index"]),
            e(record["pattern_index"]),
            sprite_icon_cell(record["image_path"], region) if record["image_path"] else _EMPTY,
            sprite_icon_cell(record["image2_path"], region) if record["image2_path"] else _EMPTY,
            e(record["root_size"]),
            _optional(record["change_pattern"]),
            _optional(record["root_begin_no"]),
            e(record["end_direction_name"] or _EMPTY),
            e(", ".join(record["begin_direction_names"]) or _EMPTY),
            text_list_cell(record["next_pattern_indexes"], _LIST_PREVIEW_ITEMS) or _EMPTY,
        ]


def _optional(value: int | None) -> str:
    return e(value) if value is not None else _EMPTY


def _direction_name(direction: int | None, direction_names: Sequence[str]) -> str:
    """The name of a direction value; the number itself past the known ones, '' for none."""
    if direction is None:
        return ""
    return direction_names[direction] if direction < DIRECTION_COUNT else str(direction)


def _pattern_fields(record: dict, direction_names: Sequence[str]) -> dict:
    end_direction = record["next_pattern_end_direction"]
    return {
        **record,
        "image_path": pattern_image_path(record["image_file"]),
        "image2_path": pattern_image_path(record["image_file2"]),
        "end_direction_name": _direction_name(end_direction, direction_names),
        "begin_direction_names": [
            name for name, flag in zip(direction_names, record["root_begin_direction"], strict=True) if flag
        ],
    }
