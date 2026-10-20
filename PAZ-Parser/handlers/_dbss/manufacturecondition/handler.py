"""manufacturecondition.dbss preview handler: the processing actions and their conditions."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.manufacture.actions import action_display_name
from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, offset_text, size_column
from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import FILE_NAME, parse_manufacturecondition_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def manufacture_condition_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("action_hash", "actionHash", offset_text),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "action_hash", "data_offset", "data_size"),
    )


class ManufactureConditionHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["actionHash"], "num", sort_key="action_hash"),
            Column(cols["action"], sort_key="action_name"),
            Column(cols["name"], sort_key="display_name"),
            Column(cols["visibleCondition"], sort_key="check_visible_condition"),
            Column(cols["enableCondition"], sort_key="check_enable_condition"),
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
            records = parse_manufacturecondition_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {**record, "display_name": action_display_name(record["action_name"])}
            for record in records
        ]

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
                e(offset_text(r["action_hash"])),
                e(r["action_name"]),
                e(r["display_name"]),
                e(r["check_visible_condition"] or _EMPTY),
                e(r["check_enable_condition"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
