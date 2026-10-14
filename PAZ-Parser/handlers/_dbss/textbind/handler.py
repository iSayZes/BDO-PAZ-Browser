"""Parsed preview handler for textbind.dbss and textbindoffset.dbss."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_lookup, resolve_text_binds
from _common.offset_table import (
    OffsetColumn,
    OffsetTableHandler,
    offset_column,
    offset_records,
    size_column,
)
from _common.pa_text import pa_fields, pa_line_cell
from _common.text_bind import LOC_TEXT_BIND
from .parser import PC_VARIANT, VARIANT_COUNT, TextBindRecord, parse_textbind_offset_rows, parse_textbind_records


_LANG_DIR = Path(__file__).parent / "lang"
# Record field of each variant's text; variant 0 is the PC text.
_VARIANT_FIELDS = ("text", *(f"variant_{variant}" for variant in range(1, VARIANT_COUNT)))


def text_bind_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("key", "key"),
            offset_column("offset", "offset"),
            size_column("size", "size"),
        ],
        offset_records(parse_textbind_offset_rows, "key"),
    )


def _variant_tagged(record: TextBindRecord, variant: int) -> str:
    """LOC type 59 text of one variant, else its Korean text, TextBinds filled."""
    localized = loc_lookup(LOC_TEXT_BIND, record.key, 0, 0, variant).strip()
    return localized or resolve_text_binds(record.variants[variant]).strip()


class TextBindHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["text"], sort_key="text"),
            *(Column(cols[field], sort_key=field) for field in _VARIANT_FIELDS[1:]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        records: list[dict] = []
        for record in parse_textbind_records(data):
            row: dict = {"key": record.key, "korean": record.variants[PC_VARIANT]}
            for variant, field in enumerate(_VARIANT_FIELDS):
                row.update(pa_fields(field, _variant_tagged(record, variant)))
            row["unknown_pre_variant_3"] = record.unknown_pre_variant_3
            records.append(row)
        return records

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [e(r["key"]), *(pa_line_cell(r, field) for field in _VARIANT_FIELDS)]
            for r in slice_
        ]
        return table(meta, self._columns(), rows)
