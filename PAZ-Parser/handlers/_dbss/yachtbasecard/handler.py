"""yachtbasecard.dbss preview handler: the cards on the faces of the Yar! dice, with their pictures."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, icon_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetTableHandler
from _common.ui_texture import ui_texture_path
from _dbss.yacht_common.offset import yacht_offset_handler
from .parser import FILE_NAME, parse_yachtbasecard_records


_LANG_DIR = Path(__file__).parent / "lang"


def yacht_base_card_offset_handler() -> OffsetTableHandler:
    return yacht_offset_handler(_LANG_DIR)


class YachtBaseCardHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="card_key"),
            Column(cols["symbol"], "num", sort_key="symbol"),
            Column(cols["eye"], "num", sort_key="eye"),
            Column(cols["image"], sort_key="image_path"),
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
            records = parse_yachtbasecard_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [{**record, "image_paz_path": ui_texture_path(record["image_path"])} for record in records]

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
            [e(r["card_key"]), e(r["symbol"]), e(r["eye"]), icon_cell(r["image_paz_path"])]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
