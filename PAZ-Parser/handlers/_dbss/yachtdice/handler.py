"""yachtdice.dbss preview handler: the six cards on the faces of each Yar! die."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetTableHandler
from _dbss.yacht_common.offset import yacht_offset_handler
from _dbss.yacht_common.text import keys_text
from .parser import FILE_NAME, parse_yachtdice_records


_LANG_DIR = Path(__file__).parent / "lang"


def yacht_dice_offset_handler() -> OffsetTableHandler:
    return yacht_offset_handler(_LANG_DIR)


class YachtDiceHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="dice_key"),
            # A list column: it would only sort by its string form.
            Column(cols["cards"]),
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
            records = parse_yachtdice_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [{**record, "cards_text": keys_text(record["card_keys"])} for record in records]

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
            [e(r["dice_key"]), e(r["cards_text"])]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
