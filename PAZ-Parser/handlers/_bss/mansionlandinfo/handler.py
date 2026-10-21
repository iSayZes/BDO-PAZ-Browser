"""mansionlandinfo.bss preview handler: one row per rentable manor."""
from __future__ import annotations

from collections import Counter
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.houseinfo.parser import FILE_NAME as HOUSEINFO_FILE
from _bss.mansionpartinfo.parser import parse_mansionpartinfo_records
from _common.character import character_name
from _common.html import Column, e, error, record_link, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.lookup_builders import MANSIONPARTINFO
from _common.quest.quest import quest_title
from _common.town import town_name
from .parser import FILE_NAME, parse_mansionlandinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LINK_CLASS = "record-link"
_HOUSEINFO_PATH = f"gamecommondata/binary/{HOUSEINFO_FILE}"
_MANSIONPARTINFO_FILE = MANSIONPARTINFO.rsplit("/", 1)[1]


def _part_counts(part_data: bytes | None) -> Counter[int] | None:
    """Number of `mansionpartinfo.bss` parts per manor building, or None without the companion."""
    if part_data is None:
        return None
    return Counter(record["character_id"] for record in parse_mansionpartinfo_records(part_data))


def _sector_text(sector: list[int]) -> str:
    return ", ".join(str(value) for value in sector)


def _quest_text(record: dict) -> str:
    """`2063/8 [Manor] A Father's Heart`, or the bare pair without a title."""
    chain_id, quest_id = record["condition_quest_chain_id"], record["condition_quest_id"]
    return f"{chain_id}/{quest_id} {quest_title(chain_id, quest_id)}".strip()


def _with_display_fields(record: dict, part_counts: Counter[int] | None) -> dict:
    building = record["building_character_key"]
    return {
        **record,
        "name": character_name(record["land_character_key"]),
        "region": town_name(record["region_key"]) or str(record["region_key"]),
        "sector_start_text": _sector_text(record["sector_start"]),
        "sector_end_text": _sector_text(record["sector_end"]),
        "quest": _quest_text(record),
        # None without parts or without the companion, so the "-" cell sorts last.
        "part_count": (part_counts.get(building) or None) if part_counts is not None else None,
    }


def _house_link(character_key: int) -> str:
    """The key as a link to its `houseinfo.bss` row."""
    return record_link(str(character_key), _HOUSEINFO_PATH, "character_key", character_key, _LINK_CLASS)


def _parts_cell(building: int, part_count: int | None) -> str:
    """The part count linked to the building's first `mansionpartinfo.bss` row, '-' without parts."""
    if not part_count:
        return _EMPTY
    return record_link(str(part_count), MANSIONPARTINFO, "character_id", building, _LINK_CLASS)


class MansionLandInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["landKey"], "num", sort_key="land_character_key"),
            Column(cols["manor"], sort_key="name"),
            Column(cols["buildingKey"], "num", sort_key="building_character_key"),
            Column(cols["region"], sort_key="region"),
            Column(cols["contributionPoints"], "num", sort_key="need_point"),
            Column(cols["sectorStart"]),
            Column(cols["sectorEnd"]),
            Column(cols["quest"], sort_key="quest"),
            Column(cols["dayPay"], "num", sort_key="day_pay"),
            Column(cols["parts"], "num", sort_key="part_count"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_MANSIONPARTINFO_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_mansionlandinfo_records(data)
            part_counts = _part_counts(companions.get(_MANSIONPARTINFO_FILE))
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]
        return [_with_display_fields(record, part_counts) for record in records]

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
                _house_link(r["land_character_key"]),
                e(r["name"] or _EMPTY),
                _house_link(r["building_character_key"]),
                e(r["region"]),
                e(r["need_point"]),
                e(r["sector_start_text"]),
                e(r["sector_end_text"]),
                e(r["quest"]),
                e(f"{r['day_pay']:,}"),
                _parts_cell(r["building_character_key"], r["part_count"]),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
