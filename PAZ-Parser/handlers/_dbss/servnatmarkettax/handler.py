"""servnatmarkettax.dbss preview handler: the Horse Market silver bonus per Training level."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.rate import rate_percent
from _common.row_table import RowTableHandler
from _dbss.lifeexp.labels import rank_text
from .parser import FILE_NAME, KEY_FIELD, parse_servnatmarkettax_records, parse_servnatmarkettaxoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def servant_market_tax_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_servnatmarkettaxoffset_rows, KEY_FIELD, "level")


class ServantMarketTaxHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["level"], "num", sort_key="life_level"),
            # Sorting by Level gives the rank order.
            Column(labels["rank"]),
            Column(labels["bonus"], "num", sort_key="horse_market_tax_percent"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "rank": rank_text(record["life_level"])}
            for record in parse_servnatmarkettax_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["life_level"]),
            e(record["rank"] or _EMPTY),
            e(f"+{rate_percent(record['horse_market_tax_percent'])}"),
        ]
