"""Spawn grid views: the spawns of one `x_y.bss` cell, and the square and cell lists of its folder."""

from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _bss.fieldinfo.names import FIELDINFO_PATH, field_no_label
from _bss.fieldinfo.parser import parse_fieldinfo_records
from _common.character import character_name
from _common.character_link import (
    CHARACTERSTATIC_OFFSET_FILE,
    character_key_cell,
    character_row_ids,
    has_character_row,
)
from _common.duration import format_duration
from _common.html import Column, e, error, flag_cell, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from .parser import (
    FIELDGRIDINFO_FILE,
    FILEINFO_FILE,
    GRID_SQUARE_SIZE,
    grid_field_no,
    parse_cell_spawns,
    parse_grid_pairs,
)

_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# A delay of 0 ms is a value, not a missing one, so it shows as 0 and sorts first.
_ZERO = "0"
_CHARACTERSTATIC_OFFSET_PATH = f"gamecommondata/binary/{CHARACTERSTATIC_OFFSET_FILE}"
_FIELDINFO_FILE = FIELDINFO_PATH.rsplit("/", 1)[-1]
# `key_type` values whose XML source file is named `<sector>_Monster.xml` / `_Npc.xml`.
_TYPE_LABELS = {2: "monster", 3: "npc"}
# gc::SpawnWaypointUsingType: SWUT_GOHOME and SWUT_GOBACK.
_GO_HOME_SLOT = 1
_GO_BACK_SLOT = 2
_NO_TERRITORY = -1
_ERROR_KEY = "_error"


def _error_records(file_name: str, ex: ValueError) -> list[dict]:
    return [{_ERROR_KEY: f"{file_name} could not be parsed: {ex}"}]


def _waypoint(spawn: dict, slot: int) -> int | None:
    """The waypoint key in `slot` of the spawn's list; None when the slot is missing or `0`."""
    return next((w["waypoint_key"] for w in spawn["waypoints"] if w["using_type"] == slot and w["waypoint_key"]), None)


def _spawn_key(spawn: dict) -> int:
    """The u64 `Key` the spawn's eight key bytes hold, as the XML source writes it."""
    return (
        spawn["key_index"]
        | (spawn["key_sector_z"] & 0xFFFF) << 16
        | (spawn["key_sector_x"] & 0xFFFF) << 32
        | spawn["key_type"] << 48
        | spawn["unknown_08"] << 56
    )


def _number_cell(value: float | int | None) -> str:
    """A coordinate or key with thousands separators, whole units only; a dash for None."""
    if value is None:
        return _EMPTY
    return e(f"{value:,.0f}" if isinstance(value, float) else f"{value:,}")


def _field_origin(companions: dict[str, bytes], field_no: int | None) -> tuple[float, float] | None:
    """The field's `world_start_x` and `world_start_z`; None without `fieldinfo.bss` or its row.

    Raises ValueError, naming the companion, when `fieldinfo.bss` does not parse.
    """
    raw = companions.get(_FIELDINFO_FILE)
    if raw is None or field_no is None:
        return None
    try:
        rows = parse_fieldinfo_records(raw)
    except ValueError as ex:
        raise ValueError(f"{_FIELDINFO_FILE}: {ex}") from ex
    row = next((r for r in rows if r["field_no"] == field_no), None)
    return (row["world_start_x"], row["world_start_z"]) if row else None


class _GridFileHandler(PreviewHandler):
    """Label loading and the count line of the three spawn grid views."""

    def _strings(self) -> dict:
        return load_handler_strings(self.lang, _LANG_DIR)

    def _meta(self, key: str, records: list[dict]) -> str:
        """The count line, with the field the folder belongs to when the path names one."""
        count = handler_text(self.lang, _LANG_DIR, key, count=len(records))
        field_no = records[0]["field_no"] if records else None
        if field_no is None:
            return count
        label = field_no_label(field_no)
        field = f"{field_no} ({label})" if label else str(field_no)
        return handler_text(self.lang, _LANG_DIR, "meta.withField", count=count, field=field)


class SpawnGridCellHandler(_GridFileHandler):
    """`x_y.bss`: every spawn of one cell, with the grid square it is listed under."""

    def _columns(self) -> list[Column]:
        cols = self._strings()["cellColumns"]
        return [
            Column(cols["spawnKey"], "num", sort_key="spawn_key"),
            Column(cols["type"], sort_key="type_label"),
            Column(cols["characterKey"], "num", sort_key="character_key"),
            Column(cols["name"], sort_key="character_name"),
            Column(cols["gridX"], "num", sort_key="grid_x"),
            Column(cols["gridZ"], "num", sort_key="grid_z"),
            Column(cols["x"], "num", sort_key="position_x"),
            Column(cols["y"], "num", sort_key="position_y"),
            Column(cols["z"], "num", sort_key="position_z"),
            Column(cols["spawnRange"], "num", sort_key="spawn_range"),
            Column(cols["delay"], "num", sort_key="spawn_delay_time"),
            Column(cols["variableDelay"], "num", sort_key="spawn_delay_variable_time"),
            Column(cols["actionIndex"], "num", sort_key="action_index"),
            Column(cols["dialogIndex"], "num", sort_key="dialog_index"),
            Column(cols["territory"], "num", sort_key="territory_key"),
            Column(cols["goHome"], "num", sort_key="go_home_waypoint"),
            Column(cols["goBack"], "num", sort_key="go_back_waypoint"),
            Column(cols["spawnable"], sort_key="is_spawnable"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        return [_CHARACTERSTATIC_OFFSET_PATH]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        file_name = entry.internal_path.rsplit("/", 1)[-1]
        try:
            spawns = parse_cell_spawns(data, file_name)
            row_ids = character_row_ids(companions)
        except ValueError as ex:
            return _error_records(file_name, ex)

        types = self._strings()["types"]
        field_no = grid_field_no(entry.internal_path)
        return [_cell_record(spawn, row_ids, types, field_no) for spawn in spawns]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and _ERROR_KEY in records[0]:
            return error(records[0][_ERROR_KEY])

        start = page * page_size
        rows = [_cell_row(r) for r in records[start : start + page_size]]
        return table(self._meta("meta.spawns", records), self._columns(), rows)


def _cell_record(spawn: dict, row_ids: frozenset[int] | None, types: dict[str, str], field_no: int | None) -> dict:
    character_key = spawn["character_key"]
    type_name = _TYPE_LABELS.get(spawn["key_type"])
    return {
        **spawn,
        "field_no": field_no,
        "spawn_key": _spawn_key(spawn),
        "type_label": types[type_name] if type_name else str(spawn["key_type"]),
        "character_name": character_name(character_key) if character_key is not None else "",
        "has_character_row": character_key is not None and has_character_row(row_ids, character_key),
        "territory_key": spawn["territory"] if spawn["territory"] != _NO_TERRITORY else None,
        "go_home_waypoint": _waypoint(spawn, _GO_HOME_SLOT),
        "go_back_waypoint": _waypoint(spawn, _GO_BACK_SLOT),
    }


def _cell_row(r: dict) -> list[str]:
    character_key = r["character_key"]
    return [
        e(r["spawn_key"]),
        e(r["type_label"]),
        character_key_cell(character_key, r["has_character_row"]) if character_key is not None else _EMPTY,
        e(r["character_name"] or _EMPTY),
        e(r["grid_x"]),
        e(r["grid_z"]),
        _number_cell(r["position_x"]),
        _number_cell(r["position_y"]),
        _number_cell(r["position_z"]),
        e(r["spawn_range"]),
        e(format_duration(r["spawn_delay_time"]) or _ZERO),
        e(format_duration(r["spawn_delay_variable_time"]) or _ZERO),
        e(r["action_index"]),
        e(r["dialog_index"]),
        _number_cell(r["territory_key"]),
        _number_cell(r["go_home_waypoint"]),
        _number_cell(r["go_back_waypoint"]),
        flag_cell(r["is_spawnable"] == 1),
    ]


class _GridPairsHandler(_GridFileHandler):
    """`fieldgridinfo.bss` and `fileinfo.bss`: (x, z) grid pairs with the world corner of each.

    The world corner needs the field's `world_start_x` / `world_start_z` from
    `fieldinfo.bss`, whose row the folder's field number names; without it the
    corner columns stay empty.
    """

    file_name = ""
    columns_key = ""
    meta_key = ""
    # The doc's field names of the pair.
    x_key = ""
    z_key = ""

    def _columns(self) -> list[Column]:
        cols = self._strings()[self.columns_key]
        return [
            Column(cols["x"], "num", sort_key=self.x_key),
            Column(cols["z"], "num", sort_key=self.z_key),
            Column(cols["worldX"], "num", sort_key="world_x"),
            Column(cols["worldZ"], "num", sort_key="world_z"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        return [FIELDINFO_PATH]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        field_no = grid_field_no(entry.internal_path)
        try:
            pairs = parse_grid_pairs(data, self.file_name)
            origin = _field_origin(companions, field_no)
        except ValueError as ex:
            return _error_records(self.file_name, ex)

        return [
            {
                self.x_key: x,
                self.z_key: z,
                "field_no": field_no,
                "world_x": origin[0] + x * GRID_SQUARE_SIZE if origin else None,
                "world_z": origin[1] + z * GRID_SQUARE_SIZE if origin else None,
            }
            for x, z in pairs
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and _ERROR_KEY in records[0]:
            return error(records[0][_ERROR_KEY])

        start = page * page_size
        rows = [
            [e(r[self.x_key]), e(r[self.z_key]), _number_cell(r["world_x"]), _number_cell(r["world_z"])]
            for r in records[start : start + page_size]
        ]
        return table(self._meta(self.meta_key, records), self._columns(), rows)


class FieldGridInfoHandler(_GridPairsHandler):
    """`fieldgridinfo.bss`: every grid square of the field that holds a spawn."""

    file_name = FIELDGRIDINFO_FILE
    columns_key = "gridColumns"
    meta_key = "meta.squares"
    x_key = "grid_x"
    z_key = "grid_z"


class FileInfoHandler(_GridPairsHandler):
    """`fileinfo.bss`: every `x_y.bss` cell file of the folder, by the square its name gives."""

    file_name = FILEINFO_FILE
    columns_key = "fileColumns"
    meta_key = "meta.cells"
    x_key = "cell_x"
    z_key = "cell_z"
