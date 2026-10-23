"""tradeexperiencess.bss preview handler: the base Trading EXP of one sold item per Trading level.

Each row shows the Trading level and its rank, `trade_exp`, and the EXP one
rate 0.1 item (most fish) gives when sold at 1,000 distance.
"""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.row_table import RowTableHandler
from _dbss.lifeexp.labels import rank_text
from .parser import FILE_NAME, parse_tradeexperiencess_records
from .sale_exp import RATE_0_1, sale_exp_at_1000


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class TradeExperienceSsBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["tradingLevel"], "num", sort_key="trading_level"),
            # Sorting by Trading Level gives the rank order.
            Column(labels["rank"]),
            Column(labels["tradeExp"], "num", sort_key="trade_exp"),
            Column(labels["saleExpRate01"], "num", sort_key="sale_exp_rate_0_1"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "rank": rank_text(record["trading_level"]),
                "sale_exp_rate_0_1": sale_exp_at_1000(record["trade_exp"], RATE_0_1),
            }
            for record in parse_tradeexperiencess_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["trading_level"]),
            e(record["rank"] or _EMPTY),
            e(f"{record['trade_exp']:,}"),
            e(f"{record['sale_exp_rate_0_1']:,}"),
        ]
