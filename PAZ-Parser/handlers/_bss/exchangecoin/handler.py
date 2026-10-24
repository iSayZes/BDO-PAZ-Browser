"""exchangecoin.bss preview handler: one row per coin exchange, the coin it costs and the item it gives."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.enum_name import enum_name
from _common.html import Column, e
from _common.item_key import item_count_list_cell, item_count_text, item_key_list_cell, item_key_text
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, NO_LEVEL, parse_exchangecoin_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# `__eExchangeCoinInfoCategory_*` names by value, read from the coins each value
# holds on client 3482 ([Season] tokens 0, [Event] seals 1, Boss Blitz tokens 4).
INFO_CATEGORY_NAMES = {0: "Season", 1: "Event", 2: "Contents", 4: "BossReward"}
# `_exchangeTypeEnum` of panel_exchangecoin_all.luac.
EXCHANGE_TYPE_NAMES = ("Always", "Day", "Week", "Family", "Level")


class ExchangeCoinHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["exchangeNo"], "num", sort_key=KEY_FIELD),
            Column(labels["coin"], sort_key="coin_name"),
            Column(labels["infoCategory"], sort_key="info_category_name"),
            Column(labels["needCoinCount"], "num", sort_key="need_coin_count"),
            Column(labels["reward"], sort_key="reward_text"),
            Column(labels["exchangeType"], sort_key="exchange_type_name"),
            Column(labels["limitCount"], "num", sort_key="limit_count_shown"),
            Column(labels["accumulatedNeedLevel"], "num", sort_key="accumulated_need_level_shown"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "coin_name": item_key_text(record["coin_item_key"]),
                "info_category_name": INFO_CATEGORY_NAMES.get(record["info_category"], str(record["info_category"])),
                "reward_text": item_count_text(record["item_key"], record["item_count"]),
                "exchange_type_name": enum_name(EXCHANGE_TYPE_NAMES, record["exchange_type"]),
                "limit_count_shown": record["limit_count"] or None,
                "accumulated_need_level_shown": (
                    None if record["accumulated_need_level"] == NO_LEVEL else record["accumulated_need_level"]
                ),
            }
            for record in parse_exchangecoin_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        limit = record["limit_count_shown"]
        level = record["accumulated_need_level_shown"]
        return [
            e(record[KEY_FIELD]),
            item_key_list_cell([record["coin_item_key"]], 1),
            e(record["info_category_name"]),
            e(f"{record['need_coin_count']:,}"),
            item_count_list_cell([(record["item_key"], record["item_count"])]),
            e(record["exchange_type_name"]),
            _EMPTY if limit is None else e(limit),
            _EMPTY if level is None else e(level),
        ]
