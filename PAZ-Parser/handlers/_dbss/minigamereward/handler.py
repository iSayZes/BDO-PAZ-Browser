"""minigamereward.dbss preview handler: energy, drop group and vehicle type per minigame."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler
from table_sort import SORT_ASC, TableSort

from _bss.itemmaingroup.drop_groups import DROP_GROUP_FILES, DropGroups, drop_group_cell, load_drop_groups
from _common.html import Column, e, error, sort_keys, table
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_offset_rows
from _common.vehicle_type import VEHICLE_TYPE_NAMES, vehicle_type_text
from .parser import FILE_NAME, parse_minigamereward_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 8


def minigame_reward_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("minigame_key", "minigameKey"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "minigame_key", "data_offset", "data_size"),
    )


class MiniGameRewardHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["minigameKey"], "num", sort_key="minigame_key"),
            Column(cols["successWp"], "num", sort_key="success_wp"),
            Column(cols["failWp"], "num", sort_key="fail_wp"),
            Column(cols["dropGroup"], "num", sort_key="drop_group"),
            # A list column: it would only sort by its string form.
            Column(cols["dropItems"]),
            Column(cols["vehicleType"], sort_key="check_vehicle_type"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def default_sort(self) -> TableSort | None:
        # The file stores the rows in descending key order.
        return TableSort("minigame_key", SORT_ASC)

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
            rows = parse_minigamereward_records(data)
            groups = load_drop_groups(companions, (row["drop_group"] for row in rows))
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [_record_fields(row, groups) for row in rows]

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
                e(r["minigame_key"]),
                e(r["success_wp"]),
                e(r["fail_wp"]),
                drop_group_cell(r["drop_group"], r["has_drop_group"]),
                item_key_list_cell(r["drop_item_keys"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                e(vehicle_type_text(r["check_vehicle_type"])),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)


def _record_fields(row: dict, groups: DropGroups) -> dict:
    drop_item_keys = groups.item_keys(row["drop_group"])
    return {
        **row,
        "has_drop_group": groups.has(row["drop_group"]),
        "drop_item_keys": drop_item_keys,
        # Item names as text, so tab search and CSV export see them.
        "drop_items": [item_key_text(key) for key in drop_item_keys],
        "check_vehicle_type_name": VEHICLE_TYPE_NAMES.get(row["check_vehicle_type"], ""),
    }
