"""houseinfo.bss preview handler: one row per node house with its uses and the items it makes."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e, error, html_list_cell, record_link, sort_keys, table
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from _common.node import full_node_name
from _common.town import town_name
from _dbss.guildhousecraftskill.labels import house_use_name
from _dbss.houseinforeceipe.parser import FILE_NAME as RECEIPE_FILE, parse_houseinforeceipe_records
from .parser import FILE_NAME, parse_houseinfo, products_by_house


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_SEPARATOR = ", "
_LINK_CLASS = "record-link"
_HOUSEINFO_PATH = f"gamecommondata/binary/{FILE_NAME}"
_RECEIPE_PATH = f"gamecommondata/binary/{RECEIPE_FILE}"
# Products shown per row; the rest go behind a hoverable count.
_PRODUCTS_SHOWN = 4


def _receipe_names_kr(receipe_data: bytes | None) -> dict[int, str]:
    """Korean name of each `houseinforeceipe.dbss` receipe; empty without the companion."""
    if receipe_data is None:
        return {}
    return {r["receipe_key"]: r["name_kr"] for r in parse_houseinforeceipe_records(receipe_data)}


def _house_label(character_key: int) -> str:
    """`2108 Velia Cliff House`, or the bare key without a name."""
    return f"{character_key} {character_name(character_key)}".strip()


class HouseInfoBssHandler(PreviewHandler):
    def _strings(self) -> dict:
        return load_handler_strings(self.lang, _LANG_DIR)

    def _columns(self) -> list[Column]:
        cols = self._strings()["columns"]
        return [
            Column(cols["houseKey"], "num", sort_key="character_key"),
            Column(cols["house"], sort_key="name"),
            Column(cols["town"], sort_key="town"),
            Column(cols["node"], sort_key="node"),
            Column(cols["contributionPoints"], "num", sort_key="need_explore_point"),
            Column(cols["group"], "num", sort_key="group"),
            Column(cols["floor"], "num", sort_key="floor"),
            Column(cols["needHouses"], sort_key="need_houses_text"),
            Column(cols["uses"], sort_key="crafts_text"),
            Column(cols["products"], sort_key="product_count"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{RECEIPE_FILE}", characterstatic_offset_companion(entry.internal_path)]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            info = parse_houseinfo(data)
            receipe_names_kr = _receipe_names_kr(companions.get(RECEIPE_FILE))
            row_ids = character_row_ids(companions)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        level_format = self._strings()["cells"]["level"]
        products = products_by_house(info.products)
        return [
            self._with_display_fields(house, products.get(house["character_key"], []), receipe_names_kr, level_format, row_ids)
            for house in info.houses
        ]

    @staticmethod
    def _with_display_fields(
        house: dict,
        product_item_keys: list[int],
        receipe_names_kr: dict[int, str],
        level_format: str,
        row_ids: frozenset[int] | None,
    ) -> dict:
        """The house with its names, its uses as text and the items the product list names for it."""
        crafts = [
            {
                **craft,
                "label": level_format.format(
                    name=house_use_name(craft["receipe_key"])
                    or receipe_names_kr.get(craft["receipe_key"])
                    or craft["receipe_key"],
                    level=craft["level"],
                ),
            }
            for craft in house["crafts"]
        ]
        return {
            **house,
            "crafts": crafts,
            "name": character_name(house["character_key"]),
            "has_character_row": has_character_row(row_ids, house["character_key"]),
            "town": town_name(house["affiliated_town"]) or str(house["affiliated_town"]),
            "node": full_node_name(house["parent_node_key"]) or str(house["parent_node_key"]),
            "need_houses_text": _LIST_SEPARATOR.join(_house_label(key) for key in house["need_house_keys"]) or None,
            "crafts_text": _LIST_SEPARATOR.join(craft["label"] for craft in crafts) or None,
            # None on a house of its own and on a house without products, so their "-" cells sort last.
            "group": house["house_group"] or None,
            "floor": house["house_floor"] if house["house_group"] else None,
            "product_item_keys": product_item_keys,
            "product_count": len(product_item_keys) or None,
            "products_text": _LIST_SEPARATOR.join(item_key_text(key) for key in product_item_keys),
        }

    @staticmethod
    def _need_houses_cell(keys: list[int]) -> str:
        """Each house key linked to its own row in this table."""
        if not keys:
            return _EMPTY
        return html_list_cell([
            record_link(_house_label(key), _HOUSEINFO_PATH, "character_key", key, _LINK_CLASS) for key in keys
        ])

    @staticmethod
    def _uses_cell(crafts: list[dict]) -> str:
        """One line per use, linked to its `houseinforeceipe.dbss` row."""
        if not crafts:
            return _EMPTY
        lines = [
            record_link(craft["label"], _RECEIPE_PATH, "receipe_key", craft["receipe_key"], _LINK_CLASS)
            for craft in crafts
        ]
        return html_list_cell(lines, separator="<br>")

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
                character_key_cell(r["character_key"], r["has_character_row"]),
                e(r["name"] or _EMPTY),
                e(r["town"]),
                e(r["node"]),
                e(r["need_explore_point"]),
                e(_EMPTY if r["group"] is None else r["group"]),
                e(_EMPTY if r["floor"] is None else r["floor"]),
                self._need_houses_cell(r["need_house_keys"]),
                self._uses_cell(r["crafts"]),
                item_key_list_cell(r["product_item_keys"], _PRODUCTS_SHOWN) if r["product_item_keys"] else _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            products=len({key for r in records for key in r["product_item_keys"]}),
        )
        return table(meta, self._columns(), rows)
