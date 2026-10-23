"""setoption.dbss preview handler: each gear and furniture set with its pieces and set effects."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, html_list_cell
from _common.lang import load_handler_strings
from _common.linked_items import item_list_cell, item_list_fields
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from _common.skill import skill_name, split_skill_key
from _common.skill_cells import skill_link
from .parser import FILE_NAME, KEY_FIELD, parse_setoption_records, parse_setoptionoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
GEAR_SET = 0
FURNITURE_SET = 1


def set_option_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_setoptionoffset_rows, KEY_FIELD, "setKey")


def _effects(record: dict) -> list[tuple[int, int, int]]:
    """`(pieces, skill_no, points)` of every filled slot, in piece order."""
    effects = []
    for slot, (skill_key, points) in enumerate(zip(record["skill_keys"], record["points"], strict=True), start=1):
        if skill_key or points:
            skill_no, _ = split_skill_key(skill_key)
            effects.append((slot, skill_no, points))
    return effects


def _effect_text(pieces: int, skill_no: int, points: int, labels: Mapping[str, str]) -> str:
    """`4: Name (53265)` for a skill, `9: 500 points` for interior points."""
    if skill_no:
        name = skill_name(skill_no)
        return f"{pieces}: {name} ({skill_no})" if name else f"{pieces}: {skill_no}"
    return f"{pieces}: {labels['points'].format(points=f'{points:,}')}"


class SetOptionHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["setKey"], "num", sort_key=KEY_FIELD),
            Column(labels["setType"], sort_key="set_type"),
            Column(labels["effects"], sort_key="effects_text"),
            Column(labels["pieceCount"], "num", sort_key="item_count"),
            Column(labels["pieces"], sort_key="item_names"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        strings = load_handler_strings(self.lang, _LANG_DIR)
        type_names = strings["setTypes"]
        labels = strings["text"]
        records = []
        for record in parse_setoption_records(data):
            set_option_type = record["set_option_type"]
            effects = _effects(record)
            pieces = record["equip_items"] if set_option_type == GEAR_SET else record["installation_items"]
            records.append(
                {
                    **record,
                    "set_type": type_names.get(str(set_option_type), str(set_option_type)),
                    "effects_text": ", ".join(_effect_text(*effect, labels) for effect in effects),
                    "_effects": effects,
                    **item_list_fields(pieces),
                }
            )
        return records

    def cells(self, record: dict) -> list[str]:
        labels = load_handler_strings(self.lang, _LANG_DIR)["text"]
        effects = [
            f"{pieces}: {skill_link(skill_no, skill_name(skill_no) or str(skill_no))}"
            if skill_no
            else e(_effect_text(pieces, skill_no, points, labels))
            for pieces, skill_no, points in record["_effects"]
        ]
        return [
            e(record[KEY_FIELD]),
            e(record["set_type"]),
            html_list_cell(effects) or _EMPTY,
            e(record["item_count"]) if record["item_count"] else _EMPTY,
            item_list_cell(record["item_ids"]),
        ]
