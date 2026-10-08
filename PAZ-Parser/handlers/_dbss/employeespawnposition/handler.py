from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.town import town_name
from _dbss.employeespawninfo.text import sailors_by_spawn_position
from .parser import parse_employeespawnposition_records, parse_employeespawnpositionoffset_records


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "employeespawnpositionoffset.dbss"
_SAILOR_FILE = "employeespawninfo.dbss"
_SAILOR_OFFSET_FILE = "employeespawninfooffset.dbss"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 5
_DIRECTION_DECIMALS = 2


def _region_name(region_key: int) -> str:
    """The region's LOC name, else its key."""
    return town_name(region_key) or str(region_key)


def _direction_text(record: dict) -> str:
    """The facing vector as `-0.71, 0, 0.71`."""
    # `+ 0.0` turns a rounded -0.0 into 0.0.
    parts = (round(record[field], _DIRECTION_DECIMALS) + 0.0 for field in ("dir_x", "dir_y", "dir_z"))
    return ", ".join(f"{part:g}" for part in parts)


def employee_spawn_position_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("spawn_position_key", "spawnPositionKey"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_employeespawnpositionoffset_records,
    )


class EmployeeSpawnPositionHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["spawnPositionKey"], "num", sort_key="spawn_position_key"),
            Column(cols["region"], sort_key="region"),
            # A list column: it would only sort by its string form.
            Column(cols["sailors"]),
            Column(cols["x"], "num", sort_key="pos_x"),
            Column(cols["y"], "num", sort_key="pos_y"),
            Column(cols["z"], "num", sort_key="pos_z"),
            Column(cols["direction"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}", f"{folder}/{_SAILOR_FILE}", f"{folder}/{_SAILOR_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        sailor_data = companions.get(_SAILOR_FILE)
        sailor_offset_data = companions.get(_SAILOR_OFFSET_FILE)
        # Without both sailor files the Sailors column is a dash.
        sailors = (
            sailors_by_spawn_position(sailor_data, sailor_offset_data)
            if sailor_data is not None and sailor_offset_data is not None
            else {}
        )
        return [
            {
                **record,
                "region": _region_name(record["region_key"]),
                "direction": _direction_text(record),
                "sailors": sailors.get(record["spawn_position_key"], []),
            }
            for record in parse_employeespawnposition_records(data, offset_raw)
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
                e(r["spawn_position_key"]),
                e(r["region"]),
                text_list_cell(r["sailors"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                e(f"{r['pos_x']:,.0f}"),
                e(f"{r['pos_y']:,.0f}"),
                e(f"{r['pos_z']:,.0f}"),
                e(r["direction"]),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
