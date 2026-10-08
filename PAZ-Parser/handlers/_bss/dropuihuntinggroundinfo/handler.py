from __future__ import annotations

from collections.abc import Callable, Iterable
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.html import Column, e, sort_keys, table, text_list_cell
from _common.hunting_ground import hunting_ground_name
from _common.item_key import item_key_list_cell, item_name
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_text
from _common.node import node_name
from _common.quest.quest import quest_title
from _common.title import title_name
from _bss.dropuitaginfo.parser import TagColors, parse_tag_colors
from _bss.dropuitaginfo.tag_chips import tag_chips_cell
from _bss.dropuitaginfo.text import tag_name
from .parser import parse_hunting_ground_records, parse_territory_keys
from .tribe_labels import tribe_text


_LANG_DIR = Path(__file__).parent / "lang"
_MAIN_CATEGORY_FILE = "dropuimaincategoryinfo.bss"
_TAG_INFO_FILE = "dropuitaginfo.bss"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 8

# Territory names; str_id4 1 is the territory, 0 the nation.
_LOC_TERRITORY = 12
_LOC_TERRITORY_NAME = 1
_LOC_CATEGORY = 115

# Packed quest key: low u16 quest chain, high u16 quest, as in allquestlist.bss.
_QUEST_CHAIN_MASK = 0xFFFF
_QUEST_ID_SHIFT = 16


def _names(ids: Iterable[int], name_of: Callable[[int], str]) -> list[str]:
    """The name of each ID, the ID itself where it has none."""
    return [name_of(value) or str(value) for value in ids]


def _quest_text(quest_key: int) -> str:
    """The quest title, else `chain/quest`."""
    chain, quest = quest_key & _QUEST_CHAIN_MASK, quest_key >> _QUEST_ID_SHIFT
    return quest_title(chain, quest) or f"{chain}/{quest}"


def _max_ap_text(limited_ap: int, apply_percent: int) -> str:
    """`2485 (5%)`, as the drop window shows it; no percent when it is 0."""
    return f"{limited_ap} ({apply_percent}%)" if apply_percent else str(limited_ap)


def _region_text(tab_key: int, territories: dict[int, int]) -> str:
    """The tab's territory name, else the tab key."""
    territory = territories.get(tab_key)
    name = loc_text(_LOC_TERRITORY, territory, _LOC_TERRITORY_NAME) if territory is not None else ""
    return name or str(tab_key)


def _number(value: float) -> str:
    """A stored f32 stat without a trailing `.0`."""
    return f"{value:g}"


class DropUiHuntingGroundInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["name"], sort_key="name"),
            # Sorts in the game's tab order rather than by name.
            Column(cols["region"], sort_key="main_category_key"),
            Column(cols["categories"]),
            Column(cols["species"], sort_key="tribe_type"),
            Column(cols["ap"], "num", sort_key="recommended_ap"),
            Column(cols["dp"], "num", sort_key="recommended_dp"),
            Column(cols["totalAp"], "num", sort_key="total_ap"),
            Column(cols["totalDp"], "num", sort_key="total_dp"),
            Column(cols["maxAp"], "num", sort_key="limited_ap"),
            Column(cols["node"], sort_key="node_name"),
            # List columns: they would only sort by their string form.
            Column(cols["monsters"]),
            Column(cols["items"]),
            Column(cols["quests"]),
            Column(cols["tags"]),
            Column(cols["titles"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_MAIN_CATEGORY_FILE}", f"{folder}/{_TAG_INFO_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        main_categories = companions.get(_MAIN_CATEGORY_FILE)
        # Without the tab table the Region column shows the tab keys.
        territories = parse_territory_keys(main_categories) if main_categories else {}
        tag_info = companions.get(_TAG_INFO_FILE)
        # Without the tag table the Tags column shows plain names.
        tag_colors: dict[int, TagColors] = parse_tag_colors(tag_info) if tag_info else {}

        records: list[dict] = []
        for record in parse_hunting_ground_records(data):
            node_key = record["node_key"] or None
            records.append({
                **record,
                "node_key": node_key,
                "name": hunting_ground_name(record["key"]) or record["name_kr"].strip(),
                "region": _region_text(record["main_category_key"], territories),
                "categories": _names(record["sub_category_keys"], lambda k: loc_text(_LOC_CATEGORY, k)),
                "species": tribe_text(record["tribe_type"]),
                "max_ap": _max_ap_text(record["limited_ap"], record["limited_ap_apply_percent"]),
                "node_name": node_name(node_key) if node_key else "",
                "monsters": _names(record["monster_ids"], character_name),
                "items": _names(record["drop_item_ids"], item_name),
                "quests": [
                    _quest_text(k) for k in record["repeat_quest_keys"] + record["sudden_quest_keys"]
                ],
                "tags": _names(record["tag_keys"], tag_name),
                "_tag_colors": [tag_colors.get(k) for k in record["tag_keys"]],
                "titles": _names(record["title_keys"], title_name),
            })
        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["key"]),
                e(r["name"] or _EMPTY),
                e(r["region"]),
                _list_cell(r["categories"]),
                e(r["species"]),
                e(_number(r["recommended_ap"])),
                e(_number(r["recommended_dp"])),
                e(_number(r["total_ap"])),
                e(_number(r["total_dp"])),
                e(r["max_ap"]),
                e(r["node_name"] or _EMPTY),
                _list_cell(r["monsters"]),
                # A plain item ID is its level 0 item key.
                item_key_list_cell(r["drop_item_ids"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                _list_cell(r["quests"]),
                tag_chips_cell(r["tags"], r["_tag_colors"], _LIST_PREVIEW_ITEMS),
                _list_cell(r["titles"]),
            ]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)


def _list_cell(values: list[str]) -> str:
    return text_list_cell(values, _LIST_PREVIEW_ITEMS) or _EMPTY
