from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.buff import buff_label, buff_list_cell
from _common.html import Column, e, flag_cell, icon_cell, sort_keys, table
from _common.item_grade import item_grade_tagged
from _common.lang import handler_text, load_handler_strings
from _common.loc import LOC_NULL, loc_tagged, loc_text
from _common.pa_text import pa_cell, pa_fields, pa_key, pa_line_cell, pa_list_cell, pa_list_fields
from _common.skill import skill_buff_ids
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _bss.lightstoneset.item_sets import item_set_ids, set_label_tagged
from .labels import binding_label, classes_label, trade_label
from .parser import (
    parse_itemenchant_records,
    parse_itemenchantoffset_records,
)


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "itemenchantoffset.dbss"

# Item names are LOC type 0 keyed by item ID; character names type 6.
_LOC_TYPE_ITEM = 0
# LOC type 0 field of the item description.
_LOC_ITEM_DESCRIPTION = 1
_LOC_TYPE_CHARACTER = 6

_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 3
# A required level of 0 or 1 means the item has none.
_NO_LEVEL_LIMIT = 1


def _item_description_tagged(item_id: int) -> str:
    """The item's LOC description with its PA tags, or ''; the file stores none of its own."""
    text = loc_tagged(_LOC_TYPE_ITEM, item_id, _LOC_ITEM_DESCRIPTION)
    return "" if text == LOC_NULL else text


def _item_name(record: dict) -> str:
    return loc_text(_LOC_TYPE_ITEM, record["item_id"]) or record["name_kr"]


def _with_links(record: dict, values: dict[str, str], classes: str) -> dict:
    """The parsed record plus its item name, placed character, buffs, Lightstone
    sets and field labels."""
    buff_ids = skill_buff_ids(record["skill_keys"])
    set_ids = item_set_ids(record["item_id"])
    return {
        **record,
        # None sorts last and exports empty.
        "required_level": record["required_level"] if record["required_level"] > _NO_LEVEL_LIMIT else None,
        "classes": classes,
        "binding": binding_label(record["vested_type"], record["family_bound"], values),
        "trade": trade_label(record["trade_type"], values),
        # In its grade colour, as the game draws item names; Korean when LOC has no row.
        **pa_fields("item_name", item_grade_tagged(_item_name(record), record["grade"])),
        **pa_fields("description", _item_description_tagged(record["item_id"])),
        # 0 means "places no character"; None sorts last and exports empty.
        "character_id": record["character_id"] or None,
        "character_name": (
            loc_text(_LOC_TYPE_CHARACTER, record["character_id"])
            if record["character_id"]
            else ""
        ),
        # Both skills' buffs, in slot order, from the SKILL_BUFFS lookup index.
        "buff_ids": buff_ids,
        "buffs": [buff_label(buff_id) for buff_id in buff_ids],
        "buff_count": len(buff_ids) or None,
        # From the LIGHTSTONE_SETS lookup index; empty when it is not loaded.
        "lightstone_set_ids": list(set_ids),
        **pa_list_fields("lightstone_sets", [set_label_tagged(set_id) for set_id in set_ids]),
        "lightstone_set_count": len(set_ids) or None,
    }


def _optional_cell(value: int | None) -> str:
    return _EMPTY if value is None else e(value)


def item_enchant_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("item_id", "itemId"),
            OffsetColumn("enchant_level", "enchantLevel"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_itemenchantoffset_records,
    )


class ItemEnchantHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemId"], "num", sort_key="item_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["description"], sort_key="description"),
            Column(cols["maxLevel"], "num", sort_key="max_enchant_level"),
            Column(cols["requiredLevel"], "num", sort_key="required_level"),
            Column(cols["classes"], sort_key="classes"),
            Column(cols["binding"], sort_key="binding"),
            Column(cols["durability"], "num", sort_key="max_durability"),
            Column(cols["marketable"], sort_key="marketable"),
            Column(cols["familyInventory"], sort_key="family_inventory"),
            Column(cols["trade"], sort_key="trade"),
            Column(cols["dyeable"], sort_key="dyeable"),
            Column(cols["objectId"], "num", sort_key="character_id"),
            Column(cols["object"], sort_key="character_name"),
            Column(cols["buffs"], sort_key="buff_count"),
            Column(cols["lightstoneSets"], sort_key="lightstone_set_count"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        if folder == entry.internal_path:
            return [_OFFSET_FILE]
        return [f"{folder}/{_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        values = load_handler_strings(self.lang, _LANG_DIR)["values"]
        records = parse_itemenchant_records(data, offset_raw)
        # About 150 masks cover all items, so each label is built once.
        classes = {mask: classes_label(mask, values) for mask in {record["class_mask"] for record in records}}
        return [_with_links(record, values, classes[record["class_mask"]]) for record in records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        enhanceable = sum(1 for record in records if record["max_enchant_level"])
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), enhanceable=enhanceable)

        with_icon = sum(1 for record in records if record["icon_path"])
        if with_icon:
            meta += handler_text(self.lang, _LANG_DIR, "meta.withIcon", with_icon=with_icon)

        rows = [
            [
                e(record["item_id"]),
                icon_cell(record["icon_path"]) if record["icon_path"] else _EMPTY,
                pa_cell(record, "item_name") if record["item_name"] else e(record["item_id"]),
                pa_line_cell(record, "description"),
                e(record["max_enchant_level"]),
                _optional_cell(record["required_level"]),
                e(record["classes"] or _EMPTY),
                e(record["binding"] or _EMPTY),
                _optional_cell(record["max_durability"]),
                flag_cell(record["marketable"]),
                flag_cell(record["family_inventory"]),
                e(record["trade"] or _EMPTY),
                flag_cell(record["dyeable"]),
                _optional_cell(record["character_id"]),
                e(record["character_name"] or _EMPTY),
                buff_list_cell(record["buff_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                pa_list_cell(record[pa_key("lightstone_sets")], _LIST_PREVIEW_ITEMS),
            ]
            for record in slice_
        ]
        return table(meta, self._columns(), rows)
