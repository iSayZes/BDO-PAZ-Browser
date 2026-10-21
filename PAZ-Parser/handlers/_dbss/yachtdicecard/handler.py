"""yachtdicecard.dbss preview handler: Yar! cards with a symbol and an eye value from 1 to 10."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetTableHandler
from _dbss.yacht_common.offset import yacht_offset_handler
from .parser import FILE_NAME, parse_yachtdicecard_records


_LANG_DIR = Path(__file__).parent / "lang"


def yacht_dice_card_offset_handler() -> OffsetTableHandler:
    return yacht_offset_handler(_LANG_DIR)


class YachtDiceCardHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="card_key"),
            Column(cols["symbol"], "num", sort_key="symbol"),
            Column(cols["eye"], "num", sort_key="eye"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            return parse_yachtdicecard_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

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
            [e(r["card_key"]), e(r["symbol"]), e(r["eye"])]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
