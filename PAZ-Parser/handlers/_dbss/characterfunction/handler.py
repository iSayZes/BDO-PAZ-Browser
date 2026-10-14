from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.enum_name import enum_name
from _bss.itemmaingroup.parser import ITEMMAINGROUP_PATH
from _common.html import Column, e, error, html_list_cell, record_link, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.loc import is_loc_loaded
from _common.offset_table import (
    OffsetColumn,
    OffsetTableHandler,
    offset_column,
    offset_records,
    size_column,
)
from _common.pabr_offset import parse_pabr_offset_rows
from .layout import SHOP_TYPE_NAMES
from .parser import CharacterFunctionRecord, parse_characterfunction_records
from .text import function_labels, node_names, vehicle_names

_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "characterfunctionoffset.dbss"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 6
# Label key in lang/*.json "itemGroupKinds" of each item group field.
_ITEM_GROUP_LABELS = {
    "shop_buy_group": "shopBuy",
    "shop_sell_group": "shopSell",
    "guild_shop_buy_group": "guildShopBuy",
    "guild_shop_sell_group": "guildShopSell",
    "trade_group": "trade",
}


def character_function_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_id", "characterId"),
            offset_column("offset", "byteOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_pabr_offset_rows, "character_id"),
    )


class CharacterFunctionHandler(PreviewHandler):
    def _columns(self, has_loc: bool) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        columns = [Column(cols["characterId"], "num", sort_key="character_id")]
        if has_loc:
            columns.append(Column(cols["name"], sort_key="name"))
        columns += [
            Column(cols["functions"], sort_key="functions_text"),
            Column(cols["shopType"], sort_key="shop_type_name"),
            Column(cols["managedNodes"], sort_key="managed_nodes_text"),
            Column(cols["town"], sort_key="town_nodes_text"),
            # A list of links: it would only sort by its string form.
            Column(cols["itemGroups"]),
            Column(cols["mounts"], sort_key="vehicles_text"),
        ]
        return columns

    def sortable_fields(self) -> tuple[str, ...]:
        # Includes the name, so a saved sort survives LOC not being loaded.
        return sort_keys(self._columns(has_loc=True))

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if not offset_raw:
            return [{"_error": f"{_OFFSET_FILE} companion not found"}]

        try:
            records = parse_characterfunction_records(data, parse_pabr_offset_rows(offset_raw))
        except ValueError as ex:
            return [{"_error": f"characterfunction.dbss could not be parsed: {ex}"}]

        return [_record_fields(record) for record in records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        has_loc = is_loc_loaded()
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))

        labels = load_handler_strings(self.lang, _LANG_DIR)["itemGroupKinds"]
        rows: list[list[str]] = []
        for r in records[start : start + page_size]:
            row = [e(r["character_id"])]
            if has_loc:
                row.append(e(r["name"] or _EMPTY))
            row += [
                text_list_cell(r["functions"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                e(r["shop_type_name"] or _EMPTY),
                text_list_cell(r["managed_nodes"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                text_list_cell(r["town_nodes"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                _item_groups_cell(r, labels) or _EMPTY,
                text_list_cell(r["vehicles"], _LIST_PREVIEW_ITEMS) or _EMPTY,
            ]
            rows.append(row)

        return table(meta, self._columns(has_loc), rows)


def _record_fields(record: CharacterFunctionRecord) -> dict:
    functions = function_labels(record)
    managed_nodes = node_names(record.managed_node_keys)
    town_nodes = node_names(record.town_node_keys)
    vehicles = vehicle_names(record)
    shop_type = record.head_value("shop_type")
    return {
        "character_id": record.character_id,
        "name": character_name(record.character_id),
        "functions": functions,
        # Full lists as text, so tab search, sorting and CSV export see every entry.
        "functions_text": ", ".join(functions),
        "shop_type": shop_type,
        # None for eShopType_None, so NPCs without a shop type sort last.
        "shop_type_name": enum_name(SHOP_TYPE_NAMES, shop_type) if shop_type else None,
        "trade_group_type": record.head_value("trade_group_type"),
        "servant_type": record.head_value("servant_type"),
        "managed_node_keys": list(record.managed_node_keys),
        "managed_nodes": managed_nodes,
        "managed_nodes_text": ", ".join(managed_nodes),
        "town_node_keys": list(record.town_node_keys),
        "town_nodes": town_nodes,
        "town_nodes_text": ", ".join(town_nodes),
        **record.item_groups,
        "vehicle_types": list(record.vehicle_types),
        "vehicles": vehicles,
        "vehicles_text": ", ".join(vehicles),
    }


def _item_groups_cell(record: dict, labels: dict[str, str]) -> str:
    """Each item group the NPC has, as its label and a link to its `itemmaingroup.bss` row."""
    links = [
        f"{e(labels[label_key])} " + record_link(str(group_id), ITEMMAINGROUP_PATH, "group_id", group_id, "record-link")
        for field, label_key in _ITEM_GROUP_LABELS.items()
        if (group_id := record[field])
    ]
    return html_list_cell(links, separator="<br>")
