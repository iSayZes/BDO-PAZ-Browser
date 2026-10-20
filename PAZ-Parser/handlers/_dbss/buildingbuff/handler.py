"""buildingbuff.dbss preview handler: the villa buffs on sale and their silver cost."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, record_link, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.lookup_builders import SKILL
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.skill import skill_name
from .parser import FILE_NAME, parse_buildingbuff_records, parse_buildingbuffoffset_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LINK_CLASS = "record-link"


def building_buff_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("villa_count", "villaCount"),
            OffsetColumn("buff_index", "buffIndex"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        parse_buildingbuffoffset_records,
    )


class BuildingBuffHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["villaCount"], "num", sort_key="villa_count"),
            Column(cols["buffIndex"], "num", sort_key="buff_index"),
            Column(cols["skillNo"], "num", sort_key="skill_no"),
            Column(cols["skill"], sort_key="skill_name"),
            Column(cols["cost"], "num", sort_key="cost"),
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
            records = parse_buildingbuff_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [{**record, "skill_name": skill_name(record["skill_no"])} for record in records]

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
                e(r["villa_count"]),
                e(r["buff_index"]),
                record_link(str(r["skill_no"]), SKILL, "skill_no", r["skill_no"], _LINK_CLASS),
                e(r["skill_name"] or _EMPTY),
                e(f"{r['cost']:,}"),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
