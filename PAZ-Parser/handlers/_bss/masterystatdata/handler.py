from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .display import mastery_text, rate_text
from .parser import parse_mastery_records
from .spec import MasteryTable


_LANG_DIR = Path(__file__).parent / "lang"


class MasteryStatDataBssHandler(PreviewHandler):
    """One life skill mastery table; `spec` gives its row fields and columns."""

    def __init__(self, spec: MasteryTable) -> None:
        self._spec = spec

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
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
        return parse_mastery_records(data, self._spec)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(mastery_text(r["mastery"])),
                *(e(rate_text(r[c.field], c.cell_format)) for c in self._spec.columns),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
