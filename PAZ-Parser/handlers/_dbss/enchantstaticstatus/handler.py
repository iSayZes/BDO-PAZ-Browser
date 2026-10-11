from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import TableSort

from _common.html import Column, e, sort_keys, table, truncate
from _common.item_key import item_key_list_cell, item_name
from _common.lang import handler_text, load_handler_strings
from _common.lookup_index import IndexKind, lookup
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.pa_text import pa_fields, pa_line_cell
from .parser import (
    FAIL_DOWNGRADE,
    parse_enchantstaticstatus_records,
    parse_enchantstaticstatusoffset_records,
)


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "enchantstaticstatusoffset.dbss"

_EMPTY = "-"
# A downgrade chance of 100% is the usual case and is left out of the cell.
_ALWAYS = 100
_LIST_PREVIEW_ITEMS = 3
_EFFECTS_PREVIEW_CHARS = 120


def _item_text(item_id: int) -> str:
    """The item's LOC name; its ID when LOC has none."""
    return item_name(item_id) or str(item_id)


def _key_items(enchant_key: int, cache: dict[int, tuple[list[int], list[str]]]) -> tuple[list[int], list[str]]:
    """The base items that enhance with this key (IndexKind.ENCHANT_KEY_ITEMS) and their names.

    Every level of a key lists the same items, so each key is named once.
    """
    if enchant_key not in cache:
        linked = lookup(IndexKind.ENCHANT_KEY_ITEMS, enchant_key)
        item_ids = list(linked) if isinstance(linked, tuple) else []
        cache[enchant_key] = item_ids, [_item_text(item_id) for item_id in item_ids]
    return cache[enchant_key]


def _fail_result_text(record: dict, labels: dict[str, str]) -> str:
    """What a failure does; '' on level 0 and on attempts that cannot fail."""
    result = record["fail_result"]
    if not result:
        return ""
    text = labels.get(str(result), str(result))
    chance = record["downgrade_chance"]
    if result == FAIL_DOWNGRADE and chance != _ALWAYS:
        text = f"{text} ({chance:g}%)"
    return text


def _with_names(
    record: dict,
    fail_labels: dict[str, str],
    key_items: tuple[list[int], list[str]],
) -> dict:
    """The parsed record plus item names for search and export, and one-line effects."""
    material = record["material_item_id"]
    has_ap = bool(record["ap_min"] or record["ap_max"])
    item_ids, item_names = key_items
    return {
        **record,
        "item_ids": item_ids,
        "item_names": item_names,
        # None sorts last: about a quarter of the keys belong to no item.
        "item_count": len(item_ids) or None,
        "fail_result_name": _fail_result_text(record, fail_labels),
        # None sorts last and exports empty: armour and most other gear have no AP.
        "ap_min": record["ap_min"] if has_ap else None,
        "ap_max": record["ap_max"] if has_ap else None,
        "material_name": _item_text(material) if material else "",
        "aid_names": [_item_text(item_id) for item_id in record["aid_item_ids"]],
        # The script is one formula per line; one line reads better in a cell.
        "effects": " ".join(record["effects"].split()),
        "aid_count": len(record["aid_item_ids"]) or None,
        # Korean, with the game's colour tags; ship equipment mostly.
        **pa_fields("description", record["description_kr"]),
    }


def _optional_cell(value: object) -> str:
    return _EMPTY if value is None else e(value)


def _chance_cell(chance: float | None) -> str:
    return _EMPTY if chance is None else e(f"{chance:.4f}%")


def _ap_cell(record: dict) -> str:
    if record["ap_max"] is None:
        return _EMPTY
    return e(f"{record['ap_min']} ~ {record['ap_max']}")


def _material_cell(record: dict) -> str:
    material = record["material_item_id"]
    return item_key_list_cell([material], 1) if material else _EMPTY


def enchant_static_status_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("enchant_key", "enchantKey"),
            OffsetColumn("level", "level"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_enchantstaticstatusoffset_records,
    )


class EnchantStaticStatusHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["enchantKey"], "num", sort_key="enchant_key"),
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["items"], sort_key="item_count"),
            Column(cols["material"], sort_key="material_name"),
            Column(cols["materialCount"], "num", sort_key="material_count"),
            Column(cols["chance"], "num", sort_key="success_chance"),
            Column(cols["onFailure"], sort_key="fail_result_name"),
            Column(cols["failDurability"], "num", sort_key="fail_durability_loss"),
            Column(cols["perfectCount"], "num", sort_key="perfect_count"),
            Column(cols["perfectDurability"], "num", sort_key="perfect_durability_loss"),
            Column(cols["durability"], "num", sort_key="max_durability"),
            Column(cols["ap"], "num", sort_key="ap_max"),
            Column(cols["accuracy"], "num", sort_key="accuracy"),
            Column(cols["evasion"], "num", sort_key="evasion"),
            Column(cols["hiddenEvasion"], "num", sort_key="hidden_evasion"),
            Column(cols["damageReduction"], "num", sort_key="damage_reduction"),
            Column(cols["hiddenDamageReduction"], "num", sort_key="hidden_damage_reduction"),
            Column(cols["maxHp"], "num", sort_key="max_hp"),
            Column(cols["aidItems"], sort_key="aid_count"),
            Column(cols["effects"], sort_key="effects"),
            Column(cols["description"], sort_key="description"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # Keep the parser's order: each enchant key with its levels in a row.
        return None

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
        fail_labels = load_handler_strings(self.lang, _LANG_DIR)["failResult"]
        items_by_key: dict[int, tuple[list[int], list[str]]] = {}
        return [
            _with_names(record, fail_labels, _key_items(record["enchant_key"], items_by_key))
            for record in parse_enchantstaticstatus_records(data, offset_raw)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        keys = len({record["enchant_key"] for record in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), keys=keys)
        rows = [
            [
                e(record["enchant_key"]),
                e(record["level"]),
                item_key_list_cell(record["item_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                _material_cell(record),
                _optional_cell(record["material_count"]),
                _chance_cell(record["success_chance"]),
                e(record["fail_result_name"] or _EMPTY),
                _optional_cell(record["fail_durability_loss"]),
                _optional_cell(record["perfect_count"]),
                _optional_cell(record["perfect_durability_loss"]),
                e(record["max_durability"]),
                _ap_cell(record),
                e(record["accuracy"]),
                e(record["evasion"]),
                e(record["hidden_evasion"]),
                e(record["damage_reduction"]),
                e(record["hidden_damage_reduction"]),
                e(record["max_hp"]),
                item_key_list_cell(record["aid_item_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                e(truncate(record["effects"], _EFFECTS_PREVIEW_CHARS)) if record["effects"] else _EMPTY,
                pa_line_cell(record, "description"),
            ]
            for record in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
