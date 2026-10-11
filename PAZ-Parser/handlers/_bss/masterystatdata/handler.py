from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .display import cell_text, mastery_text
from .parser import parse_mastery_records
from .spec import MasteryTable
from .sub_types import sub_type_name


_LANG_DIR = Path(__file__).parent / "lang"


class MasteryStatDataBssHandler(PreviewHandler):
    """One life skill mastery table; `spec` gives its row fields and columns."""

    def __init__(self, spec: MasteryTable) -> None:
        self._spec = spec

    def _type_columns(self, cols: dict[str, str]) -> list[Column]:
        if self._spec.sub_types is None:
            return []
        return [
            Column(cols["typeId"], "num", sort_key="sub_type"),
            Column(cols["type"], sort_key="sub_type_name"),
        ]

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            *self._type_columns(cols),
            Column(cols["mastery"], "num", sort_key="mastery"),
            *(Column(cols[c.label_key], "num", sort_key=c.field) for c in self._spec.columns),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records = parse_mastery_records(data, self._spec)
        sub_types = self._spec.sub_types
        if sub_types is None:
            return records
        return [{**r, "sub_type_name": sub_type_name(sub_types, r["sub_type"])} for r in records]

    def _meta(self, records: list[dict]) -> str:
        if self._spec.sub_types is None:
            return handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        types = len({r["sub_type"] for r in records})
        return handler_text(self.lang, _LANG_DIR, "meta.groupedCount", count=len(records), types=types)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        has_types = self._spec.sub_types is not None
        rows = [
            [
                *([e(r["sub_type"]), e(r["sub_type_name"])] if has_types else []),
                e(mastery_text(r["mastery"])),
                *(e(cell_text(r[c.field], c.cell_format)) for c in self._spec.columns),
            ]
            for r in records[start : start + page_size]
        ]
        return table(self._meta(records), self._columns(), rows)
