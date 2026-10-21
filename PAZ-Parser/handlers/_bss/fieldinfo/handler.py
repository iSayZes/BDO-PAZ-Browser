"""fieldinfo.bss preview handler: every field the world and its instances run in."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.enum_name import enum_name
from _common.html import Column, e, flag_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.rate import rate_percent
from .names import field_label
from .parser import parse_fieldinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_AXES = ("x", "y", "z")
# `gc::FieldInfo::FieldType` of the 2016 client; later values show as numbers.
FIELD_TYPE_NAMES = ("OpenField", "InstanceField", "Nightmare", "InstanceDungeon", "ChannelInstanceField")


def _sector_range(record: dict, axis: str) -> str:
    """`-159..111`: the field's sector span on one axis."""
    return f"{record[f'sector_start_{axis}']}..{record[f'sector_end_{axis}']}"


def _spawn(record: dict) -> str:
    return ", ".join(f"{record[f'spawn_{axis}']:g}" for axis in _AXES)


class FieldInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["fieldNo"], "num", sort_key="field_no"),
            Column(cols["name"], sort_key="label"),
            Column(cols["resource"], sort_key="resource_name"),
            Column(cols["type"], sort_key="field_type"),
            Column(cols["spawn"], "num"),
            # Each span sorts by its lower bound.
            *(Column(cols[f"sector{axis.upper()}"], "num", sort_key=f"sector_start_{axis}") for axis in _AXES),
            Column(cols["players"], "num", sort_key="enter_enable_user_count"),
            Column(cols["ridable"], sort_key="is_ridable"),
            Column(cols["rangeSpawn"], sort_key="use_range_spawn"),
            Column(cols["dropRate"], "num", sort_key="item_drop_rate"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [
            {
                **record,
                "label": field_label(record["field_no"], record["field_name"]),
                "field_type_name": enum_name(FIELD_TYPE_NAMES, record["field_type"]),
            }
            for record in parse_fieldinfo_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["field_no"]),
                e(r["label"]),
                e(r["resource_name"]),
                e(r["field_type_name"]),
                e(_spawn(r)),
                *(e(_sector_range(r, axis)) for axis in _AXES),
                e(r["enter_enable_user_count"]),
                flag_cell(bool(r["is_ridable"])),
                flag_cell(bool(r["use_range_spawn"])),
                e(rate_percent(r["item_drop_rate"])),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
