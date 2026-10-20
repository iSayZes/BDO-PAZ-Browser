"""employeecharactership.dbss preview handler: ship settings per boat character in file order."""
from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from .parser import FILE_NAME, parse_employeecharactership_records, parse_employeecharactershipoffset_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"

# (record field, label key) of every column after the name, in doc order.
_VALUE_COLUMNS = (
    ("employee_max", "employeeMax"),
    ("employee_spawn_count", "employeeSpawnCount"),
    ("food_max", "foodMax"),
    ("ocean_ship_cannon_setup", "cannonSetup"),
    ("ship_food_recovery", "foodRecovery"),
    ("ship_cannon_recovery", "cannonRecovery"),
    ("damage_diagram_restoration_cost", "restorationCost"),
    ("is_summon_full", "summonFull"),
    ("new_cannon_ship_ui", "newCannonShipUi"),
    ("new_cannon_count", "newCannonCount"),
    ("new_cannon_speed", "newCannonSpeed"),
    ("ocean_ship_skill_ui", "shipSkillUi"),
    ("manual_cannon_fire", "manualCannonFire"),
    ("manual_cannon_fire_min_length", "manualMinLength"),
    ("manual_cannon_fire_max_length", "manualMaxLength"),
    ("manual_cannon_fire_random_dist", "manualRandomDist"),
    ("manual_cannon_fire_random_pos", "manualRandomPos"),
    ("manual_cannon_fire_max_angle", "manualMaxAngle"),
    ("manual_cannon_fire_decrease_cool_time", "decreaseCoolTime"),
)
_CONDITION_FIELD = "manual_cannon_fire_decrease_cool_time_condition"


def employee_character_ship_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_key", "characterId"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        parse_employeecharactershipoffset_records,
    )


def _number_text(value: int | float) -> str:
    """Whole numbers with thousands separators, fractions as written (0.95)."""
    if float(value).is_integer():
        return f"{int(value):,}"
    return f"{value:g}"


class EmployeeCharacterShipHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_key"),
            Column(cols["name"], sort_key="character_name"),
            *(Column(cols[label], "num", sort_key=field) for field, label in _VALUE_COLUMNS),
            Column(cols["condition"], sort_key=_CONDITION_FIELD),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        try:
            records = parse_employeecharactership_records(data)
            row_ids = character_row_ids(companions)
        except ValueError as ex:
            return [{"_error": f"{FILE_NAME} could not be parsed: {ex}"}]

        return [
            {
                **record,
                "character_name": character_name(record["character_key"]),
                "has_character_row": has_character_row(row_ids, record["character_key"]),
            }
            for record in records
        ]

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
                character_key_cell(r["character_key"], r["has_character_row"]),
                e(r["character_name"] or _EMPTY),
                *(e(_number_text(r[field])) for field, _label in _VALUE_COLUMNS),
                e(r[_CONDITION_FIELD] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        return table(meta, self._columns(), rows)
