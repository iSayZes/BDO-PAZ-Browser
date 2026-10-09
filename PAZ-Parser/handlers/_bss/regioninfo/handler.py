from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.enum_name import enum_name
from _common.html import Column, e, flag_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.loc import loc_text
from _common.node import node_name
from _common.town import town_name
from .parser import NODE_WAR_DAY_NAMES, REGION_TYPE_NAMES, parse_regioninfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# Territory names; str_id4 1 is the territory, 0 the nation.
_LOC_TERRITORY = 12
_LOC_TERRITORY_NAME = 1
# Siege rate limits are stored on the 1,000,000 = 100% scale.
_RATE_PER_PERCENT = 10_000


def _region_name(region_key: int) -> str:
    """LOC type 17 name (the town names are region names too), else ''."""
    return town_name(region_key)


def _territory(territory_key: int) -> str:
    return loc_text(_LOC_TERRITORY, territory_key, _LOC_TERRITORY_NAME) or str(territory_key)


def _named_key(key: int, name_of: Callable[[int], str]) -> str | None:
    """`key name`, or None when the field is 0 so it sorts last."""
    if not key:
        return None
    return f"{key} {name_of(key)}".strip()


def _flat_limit(value: float | None) -> str:
    return _EMPTY if value is None else f"{value:g}"


def _rate(value: int) -> str:
    return f"{value / _RATE_PER_PERCENT:g}%"


def _resistance_limit(values: list[int] | None) -> str:
    """One rate when all four resistances share it (every region so far), else each."""
    if values is None:
        return _EMPTY
    if len(set(values)) == 1:
        return _rate(values[0])
    return " / ".join(_rate(value) for value in values)


def _display_fields(record: dict) -> dict:
    day = record["node_war_day"]
    has_node_war = day < len(NODE_WAR_DAY_NAMES)
    return {
        # LOC type 17 is the display name; the Korean source name stands in
        # when LOC is not loaded or has no entry.
        "region_name": _region_name(record["region_key"]) or record["name_kr"],
        "region_type_name": enum_name(REGION_TYPE_NAMES, record["region_type"]),
        "node_war_day_name": NODE_WAR_DAY_NAMES[day] if has_node_war else None,
        # Sorts the days in week order; regions without a node war sort last.
        "node_war_day_order": day if has_node_war else None,
        "territory": _territory(record["territory_key"]),
        "capital": _region_name(record["capital_region_key"]) or str(record["capital_region_key"]),
        "node": _named_key(record["node_key"], node_name),
        "guild_wharf_manager": _named_key(record["guild_wharf_manager_key"], character_name),
        # 0 participants means no node war; sorts last.
        "max_participants_sort": record["max_participants"] or None,
        "siege_resistance_limit_sort": (record["siege_resistance_limits"] or [None])[0],
    }


class RegionInfoBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["regionKey"], "num", sort_key="region_key"),
            Column(cols["regionName"], sort_key="region_name"),
            Column(cols["type"], sort_key="region_type_name"),
            Column(cols["territory"], sort_key="territory_key"),
            Column(cols["capital"], sort_key="capital"),
            Column(cols["node"], sort_key="node"),
            Column(cols["regionGroup"], "num", sort_key="region_group_key"),
            Column(cols["nodeWarDay"], sort_key="node_war_day_order"),
            Column(cols["desert"], sort_key="is_desert"),
            Column(cols["guildWharfManager"], sort_key="guild_wharf_manager"),
            Column(cols["maxParticipants"], "num", sort_key="max_participants_sort"),
            Column(cols["apLimit"], "num", sort_key="siege_ap_limit"),
            Column(cols["drLimit"], "num", sort_key="siege_dr_limit"),
            Column(cols["accuracyLimit"], "num", sort_key="siege_accuracy_limit"),
            Column(cols["evasionLimit"], "num", sort_key="siege_evasion_limit"),
            Column(cols["drRateLimit"], "num", sort_key="siege_dr_rate_limit"),
            Column(cols["resistanceLimit"], "num", sort_key="siege_resistance_limit_sort"),
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
            {**record, **_display_fields(record)}
            for record in parse_regioninfo_records(data)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))

        rows = [
            [
                e(record["region_key"]),
                e(record["region_name"] or _EMPTY),
                e(record["region_type_name"]),
                e(record["territory"]),
                e(record["capital"]),
                e(record["node"] or _EMPTY),
                e(record["region_group_key"]),
                e(record["node_war_day_name"] or _EMPTY),
                flag_cell(bool(record["is_desert"])),
                e(record["guild_wharf_manager"] or _EMPTY),
                e(record["max_participants"] or _EMPTY),
                e(_flat_limit(record["siege_ap_limit"])),
                e(_flat_limit(record["siege_dr_limit"])),
                e(_flat_limit(record["siege_accuracy_limit"])),
                e(_flat_limit(record["siege_evasion_limit"])),
                e(_EMPTY if record["siege_dr_rate_limit"] is None else _rate(record["siege_dr_rate_limit"])),
                e(_resistance_limit(record["siege_resistance_limits"])),
            ]
            for record in slice_
        ]

        return table(meta, self._columns(), rows)
