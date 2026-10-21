"""yachtclasstypetextureinfo.dbss preview handler: the Yar! profile icon of each class type."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.class_type import class_name
from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetTableHandler
from _dbss.yacht_common.offset import yacht_offset_handler
from .parser import FILE_NAME, parse_yachtclasstypetextureinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def yacht_class_type_texture_info_offset_handler() -> OffsetTableHandler:
    return yacht_offset_handler(_LANG_DIR)


class YachtClassTypeTextureInfoHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["classType"], "num", sort_key="class_type"),
            Column(cols["class"], sort_key="class_name"),
            Column(cols["textureId"], sort_key="texture_id"),
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
            records = parse_yachtclasstypetextureinfo_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [{**record, "class_name": class_name(record["class_type"]) or None} for record in records]

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
            [e(r["class_type"]), e(r["class_name"] or _EMPTY), e(r["texture_id"])]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
