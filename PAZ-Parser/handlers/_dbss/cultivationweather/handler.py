"""cultivationweather.dbss preview handler: per crop, the growth speed change in each weather range."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.item_exchange import exchange_cell, exchange_text
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.rate import rate_percent
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_cultivationweather_records, parse_cultivationweatheroffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
# gc::WeatherKind value -> the record field (and lang column key) of its ranges.
WEATHER_KIND_FIELDS: dict[int, str] = {
    1: "water",
    2: "temperature",
    3: "humidity",
    4: "pruning",
    5: "birds",
}


def cultivation_weather_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_cultivationweatheroffset_rows, KEY_FIELD, "exchangeKey")


def speed_text(rate: int) -> str:
    """`23000` -> `+2.3%`, `-3168` -> `-0.3168%`, `0` -> `0%`."""
    text = rate_percent(rate)
    return f"+{text}" if rate > 0 else text


def range_text(weather_range: dict) -> str:
    """`25 ~ 60: +2.3%`, language-neutral so the record text needs no lang file."""
    return (
        f"{weather_range['weather_start_rate']:g} ~ {weather_range['weather_end_rate']:g}: "
        f"{speed_text(weather_range['product_speed_rate'])}"
    )


def _kind_fields(weathers: list[dict]) -> dict[str, list[str]]:
    """One list of range texts per known weather kind; a kind the record lacks stays empty."""
    fields: dict[str, list[str]] = {field: [] for field in WEATHER_KIND_FIELDS.values()}
    for weather in weathers:
        field = WEATHER_KIND_FIELDS.get(weather["weather_kind"])
        if field is not None:
            fields[field] = [range_text(weather_range) for weather_range in weather["ranges"]]
    return fields


class CultivationWeatherHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["exchangeKey"], "num", sort_key=KEY_FIELD),
            *(Column(labels[field]) for field in WEATHER_KIND_FIELDS.values()),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {
                **record,
                "exchange": exchange_text(record[KEY_FIELD]),
                **_kind_fields(record["weathers"]),
            }
            for record in parse_cultivationweather_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            exchange_cell(record[KEY_FIELD]),
            *("<br>".join(e(line) for line in record[field]) or "-" for field in WEATHER_KIND_FIELDS.values()),
        ]
