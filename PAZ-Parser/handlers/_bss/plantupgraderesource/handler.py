from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.item_key import item_key_text
from _common.lang import handler_text, load_handler_strings
from .parser import parse_plantupgraderesource_records


_LANG_DIR = Path(__file__).parent / "lang"
_ITEM_SEPARATOR = ", "


def _need_items_text(items: list[dict]) -> str:
    """`Item × count` for every filled slot, '' when the upgrade takes no items."""
    return _ITEM_SEPARATOR.join(f"{item_key_text(item['item_key'])} × {item['count']:,}" for item in items)


class PlantUpgradeResourceBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["group"], "num", sort_key="group"),
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["needTime"], "num", sort_key="need_time"),
            Column(cols["needPoint"], "num", sort_key="need_point"),
            Column(cols["needMoney"], "num", sort_key="need_money"),
            Column(cols["needItems"], sort_key="need_items_text"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = [
            {**record, "need_items_text": _need_items_text(record["need_items"])}
            for record in parse_plantupgraderesource_records(data)
        ]
        # File order is hash-map order; sort by group, then level, for browsing.
        return sorted(records, key=lambda record: (record["group"], record["level"]))

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        groups = len({record["group"] for record in records})
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), groups=groups)
        rows = [
            [
                e(record["group"]),
                e(record["level"]),
                e(record["need_time"]),
                e(record["need_point"]),
                e(f"{record['need_money']:,}"),
                e(record["need_items_text"]),
            ]
            for record in slice_
        ]
        return table(meta, self._columns(), rows)
