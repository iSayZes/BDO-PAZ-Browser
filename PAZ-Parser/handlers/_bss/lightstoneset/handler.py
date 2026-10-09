"""Parsed preview handler for lightstoneset.bss."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.buff import buff_label, buff_list_cell
from _common.html import Column, e, sort_keys, table
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_cell, pa_fields, pa_key, pa_list_cell, pa_list_fields
from _common.skill import skill_buff_ids
from .parser import parse_lightstone_sets, substitute_ids
from .text import set_text


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 4
_EFFECT_PREVIEW_LINES = 6
# The set skill has one rank; skill.dbss keys its buffs under level 1.
_SET_SKILL_LEVEL = 1
_SKILL_NO_SHIFT = 16


def _set_record(record: dict, substitutes: dict[int, int]) -> dict:
    text = set_text(record["set_id"], record["text_kr"])
    substitute_item_ids = substitute_ids(record["member_ids"], substitutes)
    buff_ids = skill_buff_ids([record["skill_no"] << _SKILL_NO_SHIFT | _SET_SKILL_LEVEL])
    return {
        **record,
        "member_count": len(record["member_ids"]),
        **pa_fields("name", text.name),
        "members": [item_key_text(item_id) for item_id in record["member_ids"]],
        "substitute_ids": substitute_item_ids,
        "substitutes": [item_key_text(item_id) for item_id in substitute_item_ids],
        **pa_list_fields("effects", text.effects),
        # From the SKILL_BUFFS lookup index; empty when it is not loaded.
        "buff_ids": buff_ids,
        "buffs": [buff_label(buff_id) for buff_id in buff_ids],
    }


class LightstoneSetBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["setId"], "num", sort_key="set_id"),
            Column(cols["name"], sort_key="name"),
            # List columns: they would only sort by their string form.
            Column(cols["lightstones"]),
            Column(cols["substitutes"]),
            Column(cols["effect"]),
            Column(cols["skillId"], "num", sort_key="skill_no"),
            Column(cols["buffs"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        parsed = parse_lightstone_sets(data)
        return [_set_record(record, parsed.substitutes) for record in parsed.sets]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["set_id"]),
                pa_cell(r, "name"),
                item_key_list_cell(r["member_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                item_key_list_cell(r["substitute_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                pa_list_cell(r[pa_key("effects")], _EFFECT_PREVIEW_LINES),
                e(r["skill_no"]),
                buff_list_cell(r["buff_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)
