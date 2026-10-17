"""lifeactionexperience.dbss preview handler: life skill EXP slots per item in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, icon_cell, sort_keys, table
from _common.item_key import item_key_icon_path, item_key_text_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_cell, pa_fields
from _common.pabr_offset import parse_bare_u32_offset_rows
from _dbss.lifeexp.labels import life_skill_name
from .parser import EMPTY_LIFE_ACTION_TYPE, FILE_NAME, parse_lifeactionexperience_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def life_action_experience_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("item_key", "itemKey"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "item_key", "data_offset", "data_size"),
    )


def _slot_fields(slot: int, life_action_type: int, experience: int) -> dict:
    """One slot's life skill name and EXP, both None when the slot is empty."""
    if life_action_type == EMPTY_LIFE_ACTION_TYPE:
        return {f"life_skill_{slot}": None, f"exp_{slot}": None}
    return {f"life_skill_{slot}": life_skill_name(life_action_type), f"exp_{slot}": experience}


def _slots_fields(life_action_types: list[int], experiences: list[int]) -> dict:
    """`life_skill_1`, `exp_1`, `life_skill_2` and `exp_2`, for one sortable column each."""
    fields: dict = {}
    for slot, (life_action_type, experience) in enumerate(zip(life_action_types, experiences), start=1):
        fields.update(_slot_fields(slot, life_action_type, experience))
    return fields


def _optional_cell(value: object) -> str:
    return _EMPTY if value is None else e(value)


class LifeActionExperienceHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemKey"], "num", sort_key="item_key"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["lifeSkill1"], sort_key="life_skill_1"),
            Column(cols["exp1"], "num", sort_key="exp_1"),
            Column(cols["lifeSkill2"], sort_key="life_skill_2"),
            Column(cols["exp2"], "num", sort_key="exp_2"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_lifeactionexperience_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **record,
                "icon_path": item_key_icon_path(record["item_key"]),
                **pa_fields("item_name", item_key_text_tagged(record["item_key"])),
                **_slots_fields(record["life_action_types"], record["experiences"]),
            }
            for record in records
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        rows = [
            [
                e(r["item_key"]),
                icon_cell(r["icon_path"]),
                pa_cell(r, "item_name"),
                _optional_cell(r["life_skill_1"]),
                _optional_cell(r["exp_1"]),
                _optional_cell(r["life_skill_2"]),
                _optional_cell(r["exp_2"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
