"""guildhouseinfo.dbss preview handler: one row per guild house with its town, node and uses."""
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
from _common.html import Column, e
from _common.lang import load_handler_strings
from _common.node import full_node_name
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from _common.town import town_name
from _dbss.houseinforeceipe.house_uses import labelled_crafts, receipe_companion, receipe_names_kr, uses_cell
from .parser import FILE_NAME, KEY_FIELD, parse_guildhouseinfo_records, parse_guildhouseinfooffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_SEPARATOR = ", "


def guild_house_info_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_guildhouseinfooffset_rows, KEY_FIELD, "houseKey")


class GuildHouseInfoHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        return [receipe_companion(entry.internal_path), characterstatic_offset_companion(entry.internal_path)]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["houseKey"], "num", sort_key=KEY_FIELD),
            Column(labels["house"], sort_key="name"),
            Column(labels["town"], sort_key="town"),
            Column(labels["node"], sort_key="node"),
            Column(labels["uses"], sort_key="crafts_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        names_kr = receipe_names_kr(companions)
        row_ids = character_row_ids(companions)
        level_format = load_handler_strings(self.lang, _LANG_DIR)["cells"]["level"]
        records = []
        for house in parse_guildhouseinfo_records(data):
            crafts = labelled_crafts(house["crafts"], names_kr, level_format)
            records.append({
                **house,
                "crafts": crafts,
                "name": character_name(house[KEY_FIELD]),
                "has_character_row": has_character_row(row_ids, house[KEY_FIELD]),
                "town": town_name(house["affiliated_town"]) or str(house["affiliated_town"]),
                "node": full_node_name(house["parent_node_key"]) or str(house["parent_node_key"]),
                "crafts_text": _LIST_SEPARATOR.join(craft["label"] for craft in crafts) or None,
            })
        return records

    def cells(self, record: dict) -> list[str]:
        return [
            character_key_cell(record[KEY_FIELD], record["has_character_row"]),
            e(record["name"] or _EMPTY),
            e(record["town"]),
            e(record["node"]),
            uses_cell(record["crafts"]),
        ]
