"""guildhousecraftstorage.dbss preview handler: the storage count of each guild storage house use."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, record_link, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_u32_offset_rows
from _dbss.guildhousecraftskill.labels import house_use_name
from .parser import FILE_NAME, parse_guildhousecraftstorage_records


_LANG_DIR = Path(__file__).parent / "lang"
_HOUSEINFORECEIPE = "gamecommondata/binary/houseinforeceipe.dbss"
_EMPTY = "-"
_LINK_CLASS = "record-link"


def guild_house_craft_storage_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("receipe_key", "receipeKey"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        offset_records(parse_bare_u32_offset_rows, "receipe_key", "data_offset", "data_size"),
    )


class GuildHouseCraftStorageHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["receipeKey"], "num", sort_key="receipe_key"),
            Column(cols["name"], sort_key="name"),
            Column(cols["storageCount"], "num", sort_key="storage_count"),
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
            records = parse_guildhousecraftstorage_records(data)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [{**record, "name": house_use_name(record["receipe_key"]) or None} for record in records]

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
                record_link(str(r["receipe_key"]), _HOUSEINFORECEIPE, "receipe_key", r["receipe_key"], _LINK_CLASS),
                e(r["name"] or _EMPTY),
                e(r["storage_count"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
