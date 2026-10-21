"""itemexchangebynpc.dbss preview handler: NPC item exchanges in file order, with the NPCs that list each one."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.html import Column, e, error, sort_keys, table
from _common.item_key import item_key_list_cell, item_key_text
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_offset_rows
from _dbss.displayexchangeitemnpc.parser import (
    FILE_NAME as DISPLAY_FILE,
    parse_displayexchangeitemnpc_records,
)
from .parser import FILE_NAME, parse_itemexchangebynpc_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def item_exchange_by_npc_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("item_exchange_key", "exchangeKey"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "item_exchange_key", "data_offset", "data_size"),
    )


def _npc_names_by_key(display_data: bytes | None) -> dict[int, str]:
    """Per exchange key, the names of the NPCs whose dialogs list it, sorted and joined.

    Empty when `displayexchangeitemnpc.dbss` is missing. Raises ValueError
    when it does not parse.
    """
    if display_data is None:
        return {}

    npc_keys: dict[int, set[int]] = {}
    for row in parse_displayexchangeitemnpc_records(display_data):
        for exchange_key in row["item_exchange_keys"]:
            npc_keys.setdefault(exchange_key, set()).add(row["npc_character_key"])
    return {
        exchange_key: ", ".join(sorted(character_name(npc) or str(npc) for npc in npcs))
        for exchange_key, npcs in npc_keys.items()
    }


def _item_cell(item_key: int) -> str:
    """The item with its icon and grade colour."""
    return item_key_list_cell([item_key], 1)


class ItemExchangeByNpcHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["exchangeKey"], "num", sort_key="item_exchange_key"),
            Column(cols["needItem"], sort_key="need_item_name"),
            Column(cols["needCount"], "num", sort_key="need_item_count"),
            Column(cols["resultItem"], sort_key="result_item_name"),
            Column(cols["resultCount"], "num", sort_key="result_item_count"),
            Column(cols["npcs"], sort_key="npc_names"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{DISPLAY_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_itemexchangebynpc_records(data)
            npc_names = _npc_names_by_key(companions.get(DISPLAY_FILE))
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **record,
                "need_item_name": item_key_text(record["need_item_key"]),
                "result_item_name": item_key_text(record["result_item_key"]),
                "npc_names": npc_names.get(record["item_exchange_key"], ""),
            }
            for record in records
        ]

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
                e(r["item_exchange_key"]),
                _item_cell(r["need_item_key"]),
                e(f"{r['need_item_count']:,}"),
                _item_cell(r["result_item_key"]),
                e(f"{r['result_item_count']:,}"),
                e(r["npc_names"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
