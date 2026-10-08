from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_title
from _common.duration import format_duration
from _common.html import Column, e, icon_html_label_cell, sort_keys, table, text_list_cell
from _common.item_key import item_key_icon_path
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.pa_text import pa_html, pa_key, pa_line_cell
from .parser import parse_employeespawninfo_records, parse_employeespawninfooffset_records
from .text import hire_item_fields, sailor_name, sailor_text_fields, spawn_towns


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "employeespawninfooffset.dbss"
_SPAWN_POSITION_FILE = "employeespawnposition.dbss"
_SPAWN_POSITION_OFFSET_FILE = "employeespawnpositionoffset.dbss"
_EMPTY = "-"
_LIST_PREVIEW_ITEMS = 5
_MS_PER_SECOND = 1000


def employee_spawn_info_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_key", "characterKey"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "dataSize"),
        ],
        parse_employeespawninfooffset_records,
    )


def _hire_item_cell(record: dict) -> str:
    """The item icon and name in its grade colour, then ` x<count>`."""
    if not record["hire_item"]:
        return _EMPTY
    count = e(f"x{record['hire_item_count']:,}")
    label = f"{pa_html(record[pa_key('hire_item')])} {count}"
    return icon_html_label_cell(item_key_icon_path(record["hire_item_key"]), label)


class EmployeeSpawnInfoHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterKey"], "num", sort_key="character_key"),
            Column(cols["employeeKey"], "num", sort_key="employee_key"),
            # Every sailor is named "Sailor"; the title tells them apart.
            Column(cols["name"], sort_key="title"),
            Column(cols["towns"]),
            Column(cols["spawnPositions"]),
            Column(cols["hireItem"], sort_key="hire_item"),
            Column(cols["respawn"], "num", sort_key="respawn_time_s"),
            Column(cols["acceptText"], sort_key="accept_text"),
            Column(cols["refuseText"], sort_key="refuse_text"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [
            f"{folder}/{_OFFSET_FILE}",
            f"{folder}/{_SPAWN_POSITION_FILE}",
            f"{folder}/{_SPAWN_POSITION_OFFSET_FILE}",
        ]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        towns_of = spawn_towns(
            companions.get(_SPAWN_POSITION_FILE),
            companions.get(_SPAWN_POSITION_OFFSET_FILE),
        )
        return [
            {
                **record,
                "name": sailor_name(record["character_key"]),
                "title": character_title(record["character_key"]),
                "towns": towns_of(record["spawn_position_keys"]),
                **hire_item_fields(record["hire_item_key"]),
                **sailor_text_fields(record),
            }
            for record in parse_employeespawninfo_records(data, offset_raw)
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
                e(r["character_key"]),
                e(r["employee_key"]),
                e(r["name"] or _EMPTY),
                text_list_cell(r["towns"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                text_list_cell(r["spawn_position_keys"], _LIST_PREVIEW_ITEMS) or _EMPTY,
                _hire_item_cell(r),
                e(format_duration(r["respawn_time_s"] * _MS_PER_SECOND) or _EMPTY),
                pa_line_cell(r, "accept_text"),
                pa_line_cell(r, "refuse_text"),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
