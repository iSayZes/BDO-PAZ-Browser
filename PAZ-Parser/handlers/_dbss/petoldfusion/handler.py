"""Preview handlers for the old pet exchange table and its offset index.

Tiers show as the game numbers them (`Tier 1` for a stored `0`) and rates as
percent; the records keep the stored values. The Pets column lists the
`pet.dbss` pets with the row's fusion key.
"""

from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.rate import rate_percent
from _dbss.pet.joins import fusion_key_text, pet_companion_paths, pet_fusion_key, pet_ids_by, pet_names_text
from .parser import FILE_NAME, SELECT_FIELDS, parse_petoldfusion_records, parse_petoldfusionoffset_records


_LANG_DIR = Path(__file__).parent / "lang"
_ERROR_FIELD = "_error"


def pet_old_fusion_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("fusion_key", "fusionKey", fusion_key_text),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        parse_petoldfusionoffset_records,
    )


class PetOldFusionHandler(PreviewHandler):
    """`petoldfusion.dbss`: per fusion key of the main pet, up to four result tiers with their chances."""

    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        columns = [
            Column(cols["fusionKey"], "num", sort_key="key_prefix"),
            Column(cols["species"], "num", sort_key="species"),
            Column(cols["variant"], "num", sort_key="variant"),
            Column(cols["mainTier"], "num", sort_key="tier"),
            Column(cols["pets"], sort_key="pet_names"),
        ]
        for index, (tier_field, _padding, rate_field) in enumerate(SELECT_FIELDS, start=1):
            columns += [
                Column(handler_text(self.lang, _LANG_DIR, "columns.result", index=index), "num", sort_key=tier_field),
                Column(handler_text(self.lang, _LANG_DIR, "columns.chance", index=index), "num", sort_key=rate_field),
            ]
        return columns

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        return pet_companion_paths(entry.internal_path.rsplit("/", 1)[0])

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_petoldfusion_records(data)
            pets_by_key = pet_ids_by(companions, pet_fusion_key)
        except ValueError as ex:
            return [{_ERROR_FIELD: f"{FILE_NAME} could not be parsed: {ex}"}]
        return [
            {**record, "pet_names": pet_names_text(pets_by_key.get(record["key_prefix"], []))}
            for record in records
        ]

    def _tier_text(self, stored_tier: int) -> str:
        return handler_text(self.lang, _LANG_DIR, "tier", tier=stored_tier + 1)

    def _cells(self, record: dict) -> list[str]:
        cells = [
            e(fusion_key_text(record["key_prefix"])),
            e(record["species"]),
            e(record["variant"]),
            e(self._tier_text(record["tier"])),
            e(record["pet_names"] or "-"),
        ]
        for tier_field, _padding, rate_field in SELECT_FIELDS:
            cells += [e(self._tier_text(record[tier_field])), e(rate_percent(record[rate_field]))]
        return cells

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and _ERROR_FIELD in records[0]:
            return error(records[0][_ERROR_FIELD])

        start = page * page_size
        rows = [self._cells(record) for record in records[start : start + page_size]]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
