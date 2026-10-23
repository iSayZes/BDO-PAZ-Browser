"""solareoptionstaticstatusmanager.bss preview handler: the Arena of Solare rank tiers.

The view lists the tiers of every game mode; the equipment presets and the
other values stay in the parser's result.
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _bss.stringtable.parser import GAME_SHEET
from _bss.stringtable.text import STRINGTABLE_FILE, ui_key_hashes, ui_key_text
from _common.html import Column, e, sprite_icon_cell, text_list_cell
from _common.item_key import item_count_text
from _common.row_table import RowTableHandler
from _common.texture_string import (
    TEXTURE_STRING_COMBINE,
    TEXTURE_STRING_COMBINE_PATH,
    icon_fields,
    parse_texture_regions,
)
from .parser import FILE_NAME, parse_solareoption_file, tier_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_TIER_MASK = 0xFF
_SEPARATOR = "; "


def _item_lists_text(item_lists: list[list[dict]]) -> list[str]:
    """`1: Seal of Solare x20`: each non-empty list, numbered from 1."""
    return [
        f"{number}: " + ", ".join(item_count_text(item["item_key"], item["count"]) for item in items)
        for number, items in enumerate(item_lists, start=1)
        if items
    ]


class SolareOptionHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["gameMode"], "num", sort_key="game_mode"),
            Column(labels["rankGroup"], "num", sort_key="rank_group"),
            Column(labels["tier"], "num", sort_key="tier"),
            Column(labels["icon"], sort_key="icon_texture_key"),
            Column(labels["name"], sort_key="name"),
            Column(labels["minRating"], "num", sort_key="min_rating"),
            Column(labels["maxRanking"], "num", sort_key="max_ranking"),
            Column(labels["itemLists"]),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{STRINGTABLE_FILE}", TEXTURE_STRING_COMBINE_PATH]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        tiers = tier_records(parse_solareoption_file(data))
        hashes = ui_key_hashes(companions.get(STRINGTABLE_FILE), [GAME_SHEET])
        textures = parse_texture_regions(companions.get(TEXTURE_STRING_COMBINE), (t["icon_texture_key"] for t in tiers))
        return [
            {
                **tier,
                "tier": tier["rank_tier_key"] & _TIER_MASK,
                # The key itself when LOC has no text for it.
                "name": ui_key_text(hashes, GAME_SHEET, tier["description_key"]) or tier["description_key"],
                # 0 is "no ranking limit"; None keeps those rows last in a sort.
                "max_ranking": tier["max_ranking"] or None,
                "item_list_texts": _item_lists_text(tier["item_lists"]),
                **icon_fields(textures, tier["icon_texture_key"]),
            }
            for tier in tiers
        ]

    def cells(self, record: dict) -> list[str]:
        icon = (
            sprite_icon_cell(record["icon_path"], record["icon_region"])
            if record["icon_path"]
            else e(record["icon_texture_key"])
        )
        lists = record["item_list_texts"]
        return [
            e(record["game_mode"]),
            e(record["rank_group"]),
            e(record["tier"]),
            icon,
            e(record["name"]),
            e(record["min_rating"]),
            e(record["max_ranking"] or _EMPTY),
            text_list_cell(lists, len(lists), _SEPARATOR) if lists else _EMPTY,
        ]
