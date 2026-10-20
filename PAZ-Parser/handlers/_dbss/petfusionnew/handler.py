"""Preview handlers for the pet exchange tables and their offset index.

Tiers show as the game numbers them (`Tier 1` for a stored `0`) and rates as
percent; the records keep the stored values.
"""

from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.rate import rate_percent
from .parser import (
    ADD_RATE_FIELDS,
    ADD_RATE_FILE,
    FILE_NAME,
    GOSPHY_FIELD,
    SELECT_FIELDS,
    parse_add_rate_records,
    parse_petfusionnew_records,
    parse_petfusionnewoffset_records,
)


_LANG_DIR = Path(__file__).parent / "lang"
_ERROR_FIELD = "_error"


def pet_fusion_new_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("tier", "tier"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        parse_petfusionnewoffset_records,
    )


def _tier_text(lang: str, stored_tier: int) -> str:
    """A stored tier as the game shows it: `0` -> `Tier 1`."""
    return handler_text(lang, _LANG_DIR, "tier", tier=stored_tier + 1)


def _error_page(records: list[dict]) -> str | None:
    if records and _ERROR_FIELD in records[0]:
        return error(records[0][_ERROR_FIELD])
    return None


class PetFusionNewHandler(PreviewHandler):
    """`petfusionnew.dbss`: per main pet tier, the two result tiers and their chances."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        columns = [Column(cols["mainTier"], "num", sort_key="tier")]
        for index, (tier_field, _padding, rate_field) in enumerate(SELECT_FIELDS, start=1):
            columns += [
                Column(cols[f"result{index}"], "num", sort_key=tier_field),
                Column(cols[f"chance{index}"], "num", sort_key=rate_field),
            ]
        return columns

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            return parse_petfusionnew_records(data)
        except ValueError as ex:
            return [{_ERROR_FIELD: f"{FILE_NAME} could not be parsed: {ex}"}]

    def _cells(self, record: dict) -> list[str]:
        cells = [e(_tier_text(self.lang, record["tier"]))]
        for tier_field, _padding, rate_field in SELECT_FIELDS:
            cells += [e(_tier_text(self.lang, record[tier_field])), e(rate_percent(record[rate_field]))]
        return cells

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        failed = _error_page(records)
        if failed is not None:
            return failed
        start = page * page_size
        rows = [self._cells(record) for record in records[start : start + page_size]]
        meta = handler_text(self.lang, _LANG_DIR, "meta.mainTiers", count=len(records))
        return table(meta, self._columns(), rows)


class PetFusionNewAddRateInfoHandler(PreviewHandler):
    """`petfusionnewaddrateinfo.dbss`: per main pet tier, the chance each other pet adds by its tier."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["mainTier"], "num", sort_key="main_tier"),
            *(
                Column(handler_text(self.lang, _LANG_DIR, "columns.subTier", tier=sub_tier + 1), "num", sort_key=field)
                for sub_tier, field in enumerate(ADD_RATE_FIELDS)
            ),
            Column(cols["gosphy"], "num", sort_key=GOSPHY_FIELD),
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
            return parse_add_rate_records(data)
        except ValueError as ex:
            return [{_ERROR_FIELD: f"{ADD_RATE_FILE} could not be parsed: {ex}"}]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        failed = _error_page(records)
        if failed is not None:
            return failed
        start = page * page_size
        rows = [
            [
                e(_tier_text(self.lang, r["main_tier"])),
                *(e(rate_percent(r[field])) for field in (*ADD_RATE_FIELDS, GOSPHY_FIELD)),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.mainTiers", count=len(records))
        return table(meta, self._columns(), rows)
