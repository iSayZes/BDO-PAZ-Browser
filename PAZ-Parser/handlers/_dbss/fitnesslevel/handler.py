from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from .labels import fitness_type_name, fitness_type_names
from .parser import parse_fitnesslevel_records, parse_fitnessleveloffset_records


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "fitnessleveloffset.dbss"


def _amount_text(value: float) -> str:
    """`800`, `38.5` or `1,234`: the stored float without a trailing `.0`."""
    return f"{value:,g}"


def _type_count(records: list[dict]) -> int:
    return len({record["fitness_type"] for record in records})


def _offset_meta(records: list[dict], lang: str) -> str:
    return handler_text(lang, _LANG_DIR, "meta.offsetCount", count=len(records), types=_type_count(records))


def fitness_level_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("fitness_type", "fitnessType"),
            OffsetColumn("level", "level"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_fitnessleveloffset_records,
        meta=_offset_meta,
    )


class FitnessLevelHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["fitnessType"], sort_key="fitness_type"),
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["exp"], "num", sort_key="exp"),
            Column(cols["maxStamina"], "num", sort_key="max_stamina"),
            Column(cols["weightLimit"], "num", sort_key="weight_limit"),
            Column(cols["maxHp"], "num", sort_key="max_hp"),
            Column(cols["maxMp"], "num", sort_key="max_mp"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        names = fitness_type_names(self.lang)
        return [
            {**record, "fitness_name": fitness_type_name(names, record["fitness_type"])}
            for record in parse_fitnesslevel_records(data, offset_raw)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), types=_type_count(records))
        rows = [
            [
                e(r["fitness_name"]),
                e(r["level"]),
                e(f"{r['exp']:,}"),
                e(_amount_text(r["max_stamina"])),
                e(f"{_amount_text(r['weight_limit'])} LT"),
                e(_amount_text(r["max_hp"])),
                e(_amount_text(r["max_mp"])),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
