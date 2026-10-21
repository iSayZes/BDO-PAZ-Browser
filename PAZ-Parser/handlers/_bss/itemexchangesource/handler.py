"""itemexchangesource.bss preview handler: item exchanges with their materials and drop groups."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.binary import whole_float
from _common.character import character_name
from _common.contents_group import contents_group_key, contents_groups_text
from _common.enum_name import enum_name
from _common.html import Column, e, error, icon_label_cell, sort_keys, table
from _common.item_exchange import LOC_EXCHANGE, LOC_EXCHANGE_DESCRIPTION, LOC_EXCHANGE_NAME
from _common.item_key import item_count_list_cell, item_count_text, item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_tagged, loc_text
from _common.pa_text import pa_fields, pa_line_cell
from _common.ui_texture import UI_TEXTURE_ICON_ROOT, ui_texture_path
from _common.work_ani_type import NO_WORK_ANI_TYPE, WORK_ANI_TYPE_NAMES
from _bss.itemmaingroup.drop_groups import DROP_GROUP_FILES, DropGroups, drop_group_cell, load_drop_groups
from .enums import EXCHANGE_TYPE_NAMES, PRODUCT_CATEGORY_NAMES
from .parser import FILE_NAME, ItemExchange, parse_itemexchangesource_records

_LANG_DIR = Path(__file__).parent / "lang"
_MS_PER_WORKLOAD = 1000
_NO_FIRST_WORKING_INDEX = -1
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 6


class ItemExchangeSourceBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["exchangeType"], sort_key="exchange_type_name"),
            # List columns: they would only sort by their string form.
            Column(cols["materials"]),
            Column(cols["productCategory"], sort_key="product_category_name"),
            Column(cols["workload"], "num", sort_key="workload"),
            Column(cols["productDropKey"], "num", sort_key="product_drop_key"),
            Column(cols["productItems"]),
            Column(cols["luckDropKey"], "num", sort_key="luck_drop_key"),
            Column(cols["luckItems"]),
            Column(cols["craftCharacter"], sort_key="craft_character_name"),
            Column(cols["description"], sort_key="detail_description"),
            Column(cols["workAnimation"], sort_key="work_ani_type_name"),
            Column(cols["repeatGroupKey"], "num", sort_key="repeat_group_key"),
            Column(cols["dailyWorkingCount"], "num", sort_key="daily_working_count"),
            Column(cols["firstWorkingIndex"], "num", sort_key="first_working_index"),
            Column(cols["contentsGroups"], sort_key="contents_groups_text"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{name}" for name in DROP_GROUP_FILES]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            exchanges = parse_itemexchangesource_records(data)
            groups = load_drop_groups(companions, _drop_keys(exchanges))
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [_record_fields(exchange, groups) for exchange in exchanges]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        materials = sum(len(record["material_keys"]) for record in records)
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), materials=materials)
        rows = [_row_cells(record) for record in records[start : start + page_size]]
        return table(meta, self._columns(), rows)


def _drop_keys(exchanges: list[ItemExchange]) -> set[int]:
    """Every product and luck drop group the exchanges name; `0` is no group."""
    return {key for exchange in exchanges for key in (exchange.product_drop_key, exchange.luck_drop_key) if key}


def _record_fields(exchange: ItemExchange, groups: DropGroups) -> dict:
    product = _drop_fields("product", exchange.product_drop_key, groups)
    luck = _drop_fields("luck", exchange.luck_drop_key, groups)
    return {
        "key": exchange.key,
        "name": loc_text(LOC_EXCHANGE, exchange.key, LOC_EXCHANGE_NAME) or exchange.description_kr or None,
        "icon_path": ui_texture_path(exchange.icon_path, UI_TEXTURE_ICON_ROOT),
        "description_kr": exchange.description_kr,
        **pa_fields(
            "detail_description",
            loc_tagged(LOC_EXCHANGE, exchange.key, LOC_EXCHANGE_DESCRIPTION) or exchange.detail_description_kr,
        ),
        "detail_description_kr": exchange.detail_description_kr,
        "exchange_type": exchange.exchange_type,
        "exchange_type_name": enum_name(EXCHANGE_TYPE_NAMES, exchange.exchange_type),
        "material_keys": [material.item_key for material in exchange.materials],
        "material_counts": [material.count for material in exchange.materials],
        # Materials as text, so tab search and CSV export see them.
        "materials": [item_count_text(material.item_key, material.count) for material in exchange.materials],
        "product_category": exchange.product_category,
        "product_category_name": enum_name(PRODUCT_CATEGORY_NAMES, exchange.product_category),
        "product_time": exchange.product_time,
        "workload": whole_float(exchange.product_time / _MS_PER_WORKLOAD),
        **product,
        **luck,
        "craft_character_key": exchange.craft_character_key or None,
        "craft_character_name": _character_text(exchange.craft_character_key),
        "work_ani_type": exchange.work_ani_type,
        "work_ani_type_name": _work_ani_text(exchange.work_ani_type),
        "repeat_group_key": exchange.repeat_group_key or None,
        "daily_working_count": exchange.daily_working_count or None,
        "first_working_index": _first_working_index(exchange.first_working_index),
        "contents_group_hashes": list(exchange.contents_group_hashes),
        "contents_groups": [contents_group_key(group_hash) for group_hash in exchange.contents_group_hashes],
        "contents_groups_text": contents_groups_text(exchange.contents_group_hashes),
        "unknown_08": exchange.unknown_08,
        "unknown_materials_21": exchange.unknown_materials_21,
        "unknown_materials_76": exchange.unknown_materials_76,
        "unknown_list": list(exchange.unknown_list),
        "unknown_list_00": exchange.unknown_list_00,
        "unknown_end": exchange.unknown_end,
    }


def _drop_fields(prefix: str, group_id: int, groups: DropGroups) -> dict:
    """`<prefix>_drop_key`, whether the client ships that group, and the items it lists."""
    item_keys = groups.item_keys(group_id)
    return {
        f"{prefix}_drop_key": group_id or None,
        f"has_{prefix}_group": groups.has(group_id),
        f"{prefix}_item_keys": item_keys,
        f"{prefix}_items": [item_key_text(key) for key in item_keys],
    }


def _character_text(character_key: int) -> str | None:
    if not character_key:
        return None
    return character_name(character_key) or str(character_key)


def _work_ani_text(work_ani_type: int) -> str | None:
    if work_ani_type == NO_WORK_ANI_TYPE:
        return None
    return enum_name(WORK_ANI_TYPE_NAMES, work_ani_type)


def _first_working_index(value: int) -> int | None:
    return None if value == _NO_FIRST_WORKING_INDEX else value


def _row_cells(record: dict) -> list[str]:
    return [
        e(record["key"]),
        icon_label_cell(record["icon_path"], record["name"]) if record["name"] else _EMPTY,
        e(record["exchange_type_name"]),
        item_count_list_cell(zip(record["material_keys"], record["material_counts"])) or _EMPTY,
        e(record["product_category_name"]),
        e(f"{record['workload']:,}"),
        _group_cell(record["product_drop_key"], record["has_product_group"]),
        item_key_list_cell(record["product_item_keys"], _LIST_PREVIEW_ITEMS) or _EMPTY,
        _group_cell(record["luck_drop_key"], record["has_luck_group"]),
        item_key_list_cell(record["luck_item_keys"], _LIST_PREVIEW_ITEMS) or _EMPTY,
        e(record["craft_character_name"] or _EMPTY),
        pa_line_cell(record, "detail_description"),
        e(record["work_ani_type_name"] or _EMPTY),
        _number_cell(record["repeat_group_key"]),
        _number_cell(record["daily_working_count"]),
        _number_cell(record["first_working_index"]),
        e(record["contents_groups_text"] or _EMPTY),
    ]


def _group_cell(group_id: int | None, has_group: bool) -> str:
    """`drop_group_cell`, or a dash when the exchange names no group."""
    return _EMPTY if group_id is None else drop_group_cell(group_id, has_group)


def _number_cell(value: int | None) -> str:
    return _EMPTY if value is None else e(value)
