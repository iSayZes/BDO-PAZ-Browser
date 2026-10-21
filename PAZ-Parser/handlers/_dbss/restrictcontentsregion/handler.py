"""restrictcontentsregion.dbss preview handler: per region the functions it turns off."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, flag_cell
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from _common.town import town_name
from .parser import (
    BAN_FIELDS,
    FILE_NAME,
    KEY_FIELD,
    parse_restrictcontentsregion_records,
    parse_restrictcontentsregionoffset_rows,
)


_LANG_DIR = Path(__file__).parent / "lang"
# Column label key per ban field, in file order.
_BAN_LABELS = dict(zip(
    BAN_FIELDS,
    ("maid", "worldMap", "characterChange", "muster", "camp", "compass", "itemMap", "miniMap"),
    strict=True,
))


def restrict_contents_region_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_restrictcontentsregionoffset_rows, KEY_FIELD, "regionKey")


class RestrictContentsRegionHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["regionKey"], "num", sort_key=KEY_FIELD),
            Column(labels["region"], sort_key="region_name"),
            *(Column(labels[label], sort_key=field) for field, label in _BAN_LABELS.items()),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "region_name": town_name(record[KEY_FIELD])}
            for record in parse_restrictcontentsregion_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(record["region_name"] or "-"),
            *(flag_cell(bool(record[field])) for field in BAN_FIELDS),
        ]
