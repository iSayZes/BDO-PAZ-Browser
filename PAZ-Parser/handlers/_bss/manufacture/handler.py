"""manufacture.bss preview handler: processing recipes with their materials and result group."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import SORT_ASC, TableSort

from _common.html import Column, e, error, icon_html_label_cell, html_list_cell, record_link, sort_keys, table
from _common.item_key import item_key_icon_path, item_key_list_cell, item_key_text, item_key_text_tagged
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_html
from _bss.itemmaingroup.parser import (
    ITEMMAINGROUP_PATH,
    ItemMainGroup,
    group_item_keys,
    parse_itemmaingroup_records,
)
from _dbss.itemsubgroup.parser import ItemSubgroup, subgroups_by_key
from .actions import action_display_name
from .parser import Material, Recipe, parse_manufacture_records

_LANG_DIR = Path(__file__).parent / "lang"
_MAINGROUP_FILE = "itemmaingroup.bss"
_SUBGROUP_FILE = "itemsubgroup.dbss"
_SUBGROUP_OFFSET_FILE = "itemsubgroupoffset.dbss"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 8


class ManufactureBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["index"], "num", sort_key="index"),
            Column(cols["action"], sort_key="action_name"),
            # List columns: they would only sort by their string form.
            Column(cols["materials"]),
            Column(cols["resultGroup"], "num", sort_key="result_group"),
            Column(cols["resultItems"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # The file has no unique key; open in file order.
        return TableSort("index", SORT_ASC)

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{name}" for name in (_MAINGROUP_FILE, _SUBGROUP_FILE, _SUBGROUP_OFFSET_FILE)]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            recipes = parse_manufacture_records(data)
            groups, subgroups = _result_groups(recipes, companions)
        except ValueError as ex:
            return [{"_error": f"manufacture.bss could not be parsed: {ex}"}]

        return [_record_fields(index, recipe, groups, subgroups) for index, recipe in enumerate(recipes)]

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
        rows = [
            [
                e(record["index"]),
                e(record["action_name"]),
                _materials_cell(record["material_keys"], record["material_counts"]),
                _result_group_cell(record["result_group"], record["has_result_group"]),
                item_key_list_cell(record["result_item_keys"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for record in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)


def _result_groups(
    recipes: list[Recipe],
    companions: dict[str, bytes],
) -> tuple[dict[int, ItemMainGroup], dict[int, ItemSubgroup]]:
    """The `itemmaingroup.bss` groups the recipes name and their subgroups.

    Both are empty without `itemmaingroup.bss`; the subgroups are empty
    without `itemsubgroup.dbss` and its offset table.
    """
    maingroup_raw = companions.get(_MAINGROUP_FILE)
    if maingroup_raw is None:
        return {}, {}
    wanted = {recipe.result_group for recipe in recipes}
    groups = {
        group.group_id: group
        for group in parse_itemmaingroup_records(maingroup_raw)
        if group.group_id in wanted
    }

    subgroup_raw = companions.get(_SUBGROUP_FILE)
    offset_raw = companions.get(_SUBGROUP_OFFSET_FILE)
    if subgroup_raw is None or offset_raw is None:
        return groups, {}
    subgroup_keys = {key for group in groups.values() for key in group.subgroup_keys}
    return groups, subgroups_by_key(subgroup_raw, offset_raw, subgroup_keys)


def _record_fields(
    index: int,
    recipe: Recipe,
    groups: dict[int, ItemMainGroup],
    subgroups: dict[int, ItemSubgroup],
) -> dict:
    group = groups.get(recipe.result_group)
    result_item_keys = group_item_keys(group, subgroups) if group is not None else []
    return {
        "index": index,
        "action": recipe.action,
        "action_name": action_display_name(recipe.action),
        "material_keys": [material.item_key for material in recipe.materials],
        "material_counts": [material.count for material in recipe.materials],
        # Materials as text, so tab search and CSV export see them.
        "materials": [_material_text(material) for material in recipe.materials],
        "result_group": recipe.result_group,
        # Most result groups are missing from the client's itemmaingroup.bss.
        "has_result_group": group is not None,
        "result_item_keys": result_item_keys,
        "result_items": [item_key_text(key) for key in result_item_keys],
    }


def _material_text(material: Material) -> str:
    return f"{item_key_text(material.item_key)} x{material.count:,}"


def _materials_cell(item_keys: list[int], counts: list[int]) -> str:
    """Each material with its per-level icon and grade colour, then its count."""
    entries = [
        icon_html_label_cell(item_key_icon_path(key), f"{pa_html(item_key_text_tagged(key))} x{count:,}")
        for key, count in zip(item_keys, counts)
    ]
    return html_list_cell(entries) or _EMPTY


def _result_group_cell(group_id: int, has_group: bool) -> str:
    """A link to the group's `itemmaingroup.bss` row when the client has it, else the bare ID."""
    if not has_group:
        return e(group_id)
    return record_link(str(group_id), ITEMMAINGROUP_PATH, "group_id", group_id, "record-link")
