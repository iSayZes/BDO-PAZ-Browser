from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.class_type import class_name
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import parse_experience_records


_LANG_DIR = Path(__file__).parent / "lang"


class ExperienceBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["classType"], "num", sort_key="class_type"),
            Column(cols["className"], sort_key="class_name"),
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["ap"], "num", sort_key="ap_bonus"),
            Column(cols["dp"], "num", sort_key="dp_bonus"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = parse_experience_records(data)
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
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            classes=len({record["class_type"] for record in records}),
        )
        rows = [
            [
                e(r["class_type"]),
                e(r["class_name"]),
                e(r["level"]),
                e(r["ap_bonus"]),
                e(r["dp_bonus"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
