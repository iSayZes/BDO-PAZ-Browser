"""deliverer.bss preview handler: the Transport wagons and ships with their routes and waypoints."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e, text_list_cell
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_deliverer_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_SEPARATOR = ", "
# Waypoint names shown before the rest collapse into a count.
_MAX_WAYPOINTS = 5


class DelivererBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["carrierKey"], "num", sort_key=KEY_FIELD),
            Column(labels["carrier"], sort_key="name"),
            Column(labels["route"], "num", sort_key="delivery_route"),
            Column(labels["load"], "num", sort_key="load_age"),
            Column(labels["fee"], "num", sort_key="fee"),
            Column(labels["model"], sort_key="object_file"),
            Column(labels["waypoints"], sort_key="waypoints_text"),
            Column(labels["type"], sort_key="deliverer_type_name"),
        ]

    def _type_name(self, deliverer_type: int) -> str:
        """The `CppEnums.DelivererType` name in the UI language, else the number."""
        names = load_handler_strings(self.lang, _LANG_DIR)["types"]
        return names.get(str(deliverer_type), str(deliverer_type))

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        row_ids = character_row_ids(companions)
        return [
            {
                **record,
                "name": character_name(record[KEY_FIELD]),
                "has_character_row": has_character_row(row_ids, record[KEY_FIELD]),
                "waypoints_text": _LIST_SEPARATOR.join(record["waypoint_names"]),
                "deliverer_type_name": self._type_name(record["deliverer_type"]),
            }
            for record in parse_deliverer_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            character_key_cell(record[KEY_FIELD], record["has_character_row"]),
            e(record["name"]) if record["name"] else _EMPTY,
            e(record["delivery_route"]),
            e(record["load_age"]),
            e(f"{record['fee']:,}"),
            e(record["object_file"]) if record["object_file"] else _EMPTY,
            text_list_cell(record["waypoint_names"], _MAX_WAYPOINTS) or _EMPTY,
            e(record["deliverer_type_name"]),
        ]
