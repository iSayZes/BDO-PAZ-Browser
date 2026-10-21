"""displayexchangeitemnpc.dbss preview handler: the item exchanges each NPC dialog lists, in file order.

Each listed key shows its `itemexchangebynpc.dbss` row: need item and count, then result item and count.
"""
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
from _common.html import Column, e, error, html_list_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.quest.dialog import dialog_cell, dialog_key, dialog_name
from _dbss.itemexchangebynpc.exchange import exchange_cell, exchange_text, exchanges_by_key
from _dbss.itemexchangebynpc.parser import FILE_NAME as EXCHANGE_FILE
from .parser import FILE_NAME, parse_displayexchangeitemnpc_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def display_exchange_item_npc_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("dialog_key", "dialogKey"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "dialog_key", "data_offset", "data_size"),
    )


def _exchange_keys_text(keys: list[int]) -> str:
    """The `itemexchangebynpc.dbss` keys in list order, as `3, 4, 182`."""
    return ", ".join(str(key) for key in keys)


def _exchange_lines(keys: list[int], exchanges: dict[int, dict]) -> list[dict]:
    """Per listed key, in list order, its `itemexchangebynpc.dbss` row, or None when it has none."""
    return [{"key": key, "exchange": exchanges.get(key)} for key in keys]


class DisplayExchangeItemNpcHandler(PreviewHandler):
    def _missing_text(self, key: int) -> str:
        return handler_text(self.lang, _LANG_DIR, "missingExchange", exchange_key=key)

    def _exchanges_text(self, lines: list[dict]) -> str:
        """`181: Need x4 → Result x1; 182: ...` for search, sort and export."""
        return "; ".join(
            f"{line['key']}: {exchange_text(line['exchange'])}" if line["exchange"] else self._missing_text(line["key"])
            for line in lines
        )

    def _exchanges_cell(self, lines: list[dict]) -> str:
        """One line per listed key: the key, then its exchange with item icons, or a note when it has no row."""
        return html_list_cell(
            [
                f"{e(line['key'])}: {exchange_cell(line['exchange'])}" if line["exchange"] else e(self._missing_text(line["key"]))
                for line in lines
            ],
            separator="<br>",
        )

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["npcId"], "num", sort_key="npc_character_key"),
            Column(cols["npcName"], sort_key="npc_name"),
            Column(cols["dialog"], "num", sort_key="dialog_index"),
            Column(cols["dialogName"], sort_key="dialog_name"),
            Column(cols["exchangeCount"], "num", sort_key="item_exchange_count"),
            Column(cols["exchanges"], sort_key="exchanges_text"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [characterstatic_offset_companion(entry.internal_path), f"{folder}/{EXCHANGE_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_displayexchangeitemnpc_records(data)
            row_ids = character_row_ids(companions)
            exchanges = exchanges_by_key(companions.get(EXCHANGE_FILE))
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        display_records = []
        for record in records:
            lines = _exchange_lines(record["item_exchange_keys"], exchanges)
            display_records.append({
                **record,
                "npc_name": character_name(record["npc_character_key"]),
                "has_character_row": has_character_row(row_ids, record["npc_character_key"]),
                "dialog_key": dialog_key(record["npc_character_key"], record["dialog_index"]),
                "dialog_name": dialog_name(record["npc_character_key"], record["dialog_index"]),
                "item_exchange_keys_text": _exchange_keys_text(record["item_exchange_keys"]),
                "exchange_lines": lines,
                "exchanges_text": self._exchanges_text(lines),
            })
        return display_records

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
                character_key_cell(r["npc_character_key"], r["has_character_row"]),
                e(r["npc_name"] or _EMPTY),
                dialog_cell(r["dialog_key"], str(r["dialog_index"])),
                e(r["dialog_name"] or _EMPTY),
                e(r["item_exchange_count"]),
                self._exchanges_cell(r["exchange_lines"]),
            ]
            for r in records[start : start + page_size]
        ]
        npc_count = len({r["npc_character_key"] for r in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), npc_count=npc_count)
        return table(meta, self._columns(), rows)
