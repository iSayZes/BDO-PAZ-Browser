"""manufacture.bss preview handler: processing recipes with their materials and result group."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import SORT_ASC, TableSort

from _common.html import Column, e, error, sort_keys, table
from _common.item_key import item_count_list_cell, item_count_text, item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from _bss.itemmaingroup.drop_groups import DROP_GROUP_FILES, DropGroups, drop_group_cell, load_drop_groups
from .actions import action_display_name
from .parser import Recipe, parse_manufacture_records

_LANG_DIR = Path(__file__).parent / "lang"
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
        return [f"{folder}/{name}" for name in DROP_GROUP_FILES]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            recipes = parse_manufacture_records(data)
            groups = load_drop_groups(companions, (recipe.result_group for recipe in recipes))
        except ValueError as ex:
            return [{"_error": f"manufacture.bss could not be parsed: {ex}"}]

        return [_record_fields(index, recipe, groups) for index, recipe in enumerate(recipes)]

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
                item_count_list_cell(zip(record["material_keys"], record["material_counts"])) or _EMPTY,
                drop_group_cell(record["result_group"], record["has_result_group"]),
                item_key_list_cell(record["result_item_keys"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            for record in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)


def _record_fields(index: int, recipe: Recipe, groups: DropGroups) -> dict:
    result_item_keys = groups.item_keys(recipe.result_group)
    return {
        "index": index,
        "action": recipe.action,
        "action_name": action_display_name(recipe.action),
        "material_keys": [material.item_key for material in recipe.materials],
        "material_counts": [material.count for material in recipe.materials],
        # Materials as text, so tab search and CSV export see them.
        "materials": [item_count_text(material.item_key, material.count) for material in recipe.materials],
        "result_group": recipe.result_group,
        # Most result groups are missing from the client's itemmaingroup.bss.
        "has_result_group": groups.has(recipe.result_group),
        "result_item_keys": result_item_keys,
        "result_items": [item_key_text(key) for key in result_item_keys],
        # The sheet's SuccessPercent; the doc's In-Game Checks test its scale.
        "success_percent": recipe.success_percent,
    }
