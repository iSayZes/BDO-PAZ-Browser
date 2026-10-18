"""guildmanufacture.dbss preview handler: the Guild Crafting recipes, one per product item."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import ui_hash_text
from _common.character import character_name
from _common.html import Column, e, error, html_list_cell, icon_html_label_cell, sort_keys, table, text_list_cell
from _common.item_key import item_key_icon_path, item_key_text, item_key_text_tagged
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pa_text import pa_html
from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.skill import skill_name, split_skill_key
from _common.string_hash import key_hash
from .parser import FILE_NAME, parse_guildmanufacture_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_HOUSES = 4
# The Guild Crafting product window (panel_guild_manufactureselect_all.luac)
# titles category N with this GAME sheet key; category 3 uses CATEGORY4.
_CATEGORY_KEYS = {
    0: "LUA_GUILD_MANUFACTURE_SELECT_CATEGORY0",
    1: "LUA_GUILD_MANUFACTURE_SELECT_CATEGORY1",
    2: "LUA_GUILD_MANUFACTURE_SELECT_CATEGORY2",
    3: "LUA_GUILD_MANUFACTURE_SELECT_CATEGORY4",
}


def guild_manufacture_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("product_item_key", "productItemKey"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "product_item_key", "data_offset", "data_size"),
    )


def _category_name(category: int) -> str:
    """The category title the product window shows, else the number."""
    key = _CATEGORY_KEYS.get(category)
    name = ui_hash_text(GAME_SHEET, key_hash(key)) if key is not None else ""
    return name or str(category)


def _skill_text(skill_key: int) -> str:
    """The guild skill name (`Building Boat Lv. 1`), else its number and level."""
    skill_no, level = split_skill_key(skill_key)
    return skill_name(skill_no) or f"{skill_no} ({level})"


def _required_items(keys: list[int], counts: list[int]) -> list[tuple[int, int]]:
    """The filled slots as `(item_key, count)`; an empty slot holds key 0."""
    return [(key, count) for key, count in zip(keys, counts) if key]


def _required_items_text(items: list[tuple[int, int]]) -> list[str]:
    return [f"{item_key_text(key)} x{count:,}" for key, count in items]


def _required_items_cell(items: list[tuple[int, int]]) -> str:
    """Each required item with its icon and grade colour, then its count."""
    entries = [
        icon_html_label_cell(item_key_icon_path(key), f"{pa_html(item_key_text_tagged(key))} x{count:,}")
        for key, count in items
    ]
    return html_list_cell(entries) or _EMPTY


def _product_cell(item_key: int) -> str:
    return icon_html_label_cell(item_key_icon_path(item_key), pa_html(item_key_text_tagged(item_key)))


def _record_fields(record: dict) -> dict:
    items = _required_items(record["required_item_keys"], record["required_item_counts"])
    return {
        **record,
        "product_name": item_key_text(record["product_item_key"]),
        "category_name": _category_name(record["category"]),
        "skill_name": _skill_text(record["skill_key"]),
        # Text forms of the lists, so tab search and CSV export see them.
        "required_items": _required_items_text(items),
        "guild_house_names": [character_name(key) or str(key) for key in record["guild_house_keys"]],
    }


class GuildManufactureHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["productItemKey"], "num", sort_key="product_item_key"),
            Column(cols["product"], sort_key="product_name"),
            Column(cols["category"], sort_key="category_name"),
            Column(cols["exchangeItemKey"], "num", sort_key="exchange_item_key"),
            # List columns: they would only sort by their string form.
            Column(cols["requiredItems"]),
            Column(cols["time"], "num", sort_key="time"),
            Column(cols["price"], "num", sort_key="price"),
            Column(cols["productItemLimit"], "num", sort_key="product_item_limit"),
            Column(cols["guildSkill"], sort_key="skill_name"),
            Column(cols["guildHouses"]),
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
            records = parse_guildmanufacture_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [_record_fields(record) for record in records]

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
                e(r["product_item_key"]),
                _product_cell(r["product_item_key"]),
                e(r["category_name"]),
                e(r["exchange_item_key"]),
                _required_items_cell(_required_items(r["required_item_keys"], r["required_item_counts"])),
                e(f"{r['time']:,}"),
                e(f"{r['price']:,}"),
                e(r["product_item_limit"]),
                e(r["skill_name"]),
                text_list_cell(r["guild_house_names"], _LIST_PREVIEW_HOUSES) or _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
