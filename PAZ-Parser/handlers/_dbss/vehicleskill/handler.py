from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.contents_group import contents_groups_text
from _common.html import Column, e, flag_cell, icon_cell, sort_keys, table
from _common.icon_index import clean_stored_icon_path
from _common.inline_text import decode_inline_text
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_tagged, resolve_text_binds, strip_pa_tags
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_cell, pa_fields, pa_line_cell
from _common.pabr_offset import parse_pabr_u8_offset_rows
from _common.ui_texture import UI_TEXTURE_ICON_ROOT, ui_texture_path
from _common.vehicle_skill import LOC_VEHICLE_SKILL
from .parser import parse_vehicleskill_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# LOC type 8 `str_id4` of each text; the inline Korean field it falls back to.
_LOC_TEXTS = (
    ("name", 0, "name_kr"),
    ("key_command", 1, "desc_kr"),
    ("description", 3, "desc2_kr"),
    ("console_key_command", 4, "console_desc_kr"),
)


def vehicle_skill_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("key", "key"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_pabr_u8_offset_rows, "key"),
    )


def _text(key: int, str_id4: int, korean: str) -> str:
    """LOC text with its tags in the user's language, else the inline Korean text."""
    tagged = loc_tagged(LOC_VEHICLE_SKILL, key, str_id4)
    if strip_pa_tags(tagged).strip():
        return tagged
    return resolve_text_binds(decode_inline_text(korean))


def _with_display_fields(record: dict) -> dict:
    key = record["key"]
    texts: dict = {}
    for field, str_id4, korean_field in _LOC_TEXTS:
        texts.update(pa_fields(field, _text(key, str_id4, record[korean_field])))
    stored_icon = clean_stored_icon_path(record["icon_path"])
    return {
        **record,
        **texts,
        "icon_file": ui_texture_path(stored_icon, UI_TEXTURE_ICON_ROOT),
        "contents_groups": contents_groups_text(record["contents_group_key_hashes"]),
        # 0 is "none" on both; None keeps those rows last in a sort.
        "skill_order": record["skill_order"] or None,
        "need_life_level_for_auto_skill": record["need_life_level_for_auto_skill"] or None,
    }


class VehicleSkillHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["icon"], sort_key="icon_file"),
            Column(cols["name"], sort_key="name"),
            Column(cols["maxExp"], "num", sort_key="max_exp"),
            Column(cols["addExpForCheck"], "num", sort_key="add_exp_for_check"),
            Column(cols["basePrice"], "num", sort_key="base_price"),
            Column(cols["addMatingRate"], "num", sort_key="add_mating_rate"),
            Column(cols["isLearnFromItem"], sort_key="is_learn_from_item"),
            Column(cols["keyCommand"], sort_key="key_command"),
            Column(cols["description"], sort_key="description"),
            Column(cols["consoleKeyCommand"], sort_key="console_key_command"),
            Column(cols["trainingSkillCharacters"], sort_key="training_skill_characters"),
            Column(cols["isMarketFilter"], sort_key="is_market_filter"),
            Column(cols["contentsGroups"]),
            Column(cols["conditionDesc"], sort_key="condition_desc"),
            Column(cols["vehicleSkillLock"], sort_key="vehicle_skill_lock"),
            Column(cols["skillOrder"], "num", sort_key="skill_order"),
            Column(cols["needLifeLevelForAutoSkill"], "num", sort_key="need_life_level_for_auto_skill"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [_with_display_fields(record) for record in parse_vehicleskill_records(data)]

    def _row(self, r: dict) -> list[str]:
        return [
            e(r["key"]),
            icon_cell(r["icon_file"]),
            pa_cell(r, "name"),
            e(f"{r['max_exp']:,}"),
            e(f"{r['add_exp_for_check']:,}"),
            e(f"{r['base_price']:,}"),
            e(f"{r['add_mating_rate']:,}"),
            flag_cell(bool(r["is_learn_from_item"])),
            pa_cell(r, "key_command"),
            pa_line_cell(r, "description"),
            pa_cell(r, "console_key_command"),
            e(r["training_skill_characters"] or _EMPTY),
            flag_cell(bool(r["is_market_filter"])),
            e(r["contents_groups"]),
            e(r["condition_desc"] or _EMPTY),
            flag_cell(bool(r["vehicle_skill_lock"])),
            e(r["skill_order"] or _EMPTY),
            e(r["need_life_level_for_auto_skill"] or _EMPTY),
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [self._row(r) for r in records[start : start + page_size]]
        return table(meta, self._columns(), rows)
