"""petdetectposition.dbss preview handler: the pet Location Find positions, in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_offset_rows
from .parser import FILE_NAME, parse_petdetectposition_records


_LANG_DIR = Path(__file__).parent / "lang"


def pet_detect_position_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("pet_detect_position_key", "positionKey"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "pet_detect_position_key"),
    )


class PetDetectPositionHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["positionKey"], "num", sort_key="pet_detect_position_key"),
            Column(cols["x"], "num", sort_key="pos_x"),
            Column(cols["y"], "num", sort_key="pos_y"),
            Column(cols["z"], "num", sort_key="pos_z"),
            Column(cols["type"], "num", sort_key="pet_detect_position_type"),
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
            return parse_petdetectposition_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

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
                e(r["pet_detect_position_key"]),
                e(f"{r['pos_x']:,.0f}"),
                e(f"{r['pos_y']:,.0f}"),
                e(f"{r['pos_z']:,.0f}"),
                e(r["pet_detect_position_type"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
