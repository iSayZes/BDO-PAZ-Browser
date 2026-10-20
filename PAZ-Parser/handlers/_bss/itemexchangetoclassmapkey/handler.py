"""itemexchangetoclassmapkey.bss preview handler: the weapon exchange group of each item."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, icon_html_label_cell, record_link, sort_keys, table
from _common.item_key import item_key_icon_path, item_key_text, item_key_text_tagged
from _common.lang import handler_text, load_handler_strings
from _common.pa_text import pa_html
from _dbss.itemexchangetoclass.parser import FILE_NAME as GROUP_FILE
from .parser import FILE_NAME, parse_itemexchangetoclassmapkey_records


_LANG_DIR = Path(__file__).parent / "lang"
_GROUP_PATH = f"gamecommondata/binary/{GROUP_FILE}"
_LINK_CLASS = "record-link"


class ItemExchangeToClassMapKeyBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["itemKey"], "num", sort_key="item_key"),
            Column(cols["item"], sort_key="item_name"),
            Column(cols["key"], "num", sort_key="key"),
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
            records = parse_itemexchangetoclassmapkey_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [{**record, "item_name": item_key_text(record["item_key"])} for record in records]

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
                e(r["item_key"]),
                icon_html_label_cell(item_key_icon_path(r["item_key"]), pa_html(item_key_text_tagged(r["item_key"]))),
                record_link(str(r["key"]), _GROUP_PATH, "key", r["key"], _LINK_CLASS),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
