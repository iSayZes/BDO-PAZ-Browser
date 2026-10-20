"""instancedungeoninfo.dbss preview handler: field and entry position of each instance dungeon."""
from __future__ import annotations

import math
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_u32_offset_rows
from .parser import parse_instancedungeoninfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_ROTATION_DECIMALS = 1


def _rotation_text(radians: float) -> str:
    """The facing as degrees, such as `90°`; the file stores radians."""
    # `+ 0.0` turns a rounded -0.0 into 0.0.
    degrees = round(math.degrees(radians), _ROTATION_DECIMALS) + 0.0
    return f"{degrees:g}°"


def instance_dungeon_info_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("key", "key"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "key"),
    )


class InstanceDungeonInfoHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["key"], "num", sort_key="key"),
            Column(cols["fieldNo"], "num", sort_key="field_no"),
            Column(cols["x"], "num", sort_key="enter_x"),
            Column(cols["y"], "num", sort_key="enter_y"),
            Column(cols["z"], "num", sort_key="enter_z"),
            Column(cols["direction"], "num", sort_key="enter_rotation"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return parse_instancedungeoninfo_records(data)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        rows = [
            [
                e(r["key"]),
                e(r["field_no"]),
                e(f"{r['enter_x']:,.0f}"),
                e(f"{r['enter_y']:,.0f}"),
                e(f"{r['enter_z']:,.0f}"),
                e(_rotation_text(r["enter_rotation"])),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
