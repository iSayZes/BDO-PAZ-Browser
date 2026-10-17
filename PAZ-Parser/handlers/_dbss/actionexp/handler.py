"""actionexp.dbss and actionexpoffset.dbss preview handlers."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.class_type import class_name
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from .parser import parse_actionexp_records, parse_actionexpoffset_records


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "actionexpoffset.dbss"


def _class_count(records: list[dict]) -> int:
    return len({record["class_type"] for record in records})


def _offset_meta(records: list[dict], lang: str) -> str:
    return handler_text(lang, _LANG_DIR, "meta.offsetCount", count=len(records), classes=_class_count(records))


def action_exp_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("class_type", "classType"),
            OffsetColumn("level", "level"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_actionexpoffset_records,
        meta=_offset_meta,
    )


class ActionExpHandler(PreviewHandler):
    """Class type and level of every row; the EXP bytes stay on the record as `unknown_05`."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["classType"], "num", sort_key="class_type"),
            Column(cols["className"], sort_key="class_name"),
            Column(cols["level"], "num", sort_key="level"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

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
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        records = parse_actionexp_records(data, offset_raw)
        # One LOC lookup per class, not one per level record.
        names = {class_type: class_name(class_type) for class_type in {r["class_type"] for r in records}}
        return [{**record, "class_name": names[record["class_type"]]} for record in records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), classes=_class_count(records))
        rows = [
            [e(r["class_type"]), e(r["class_name"]), e(r["level"])]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
