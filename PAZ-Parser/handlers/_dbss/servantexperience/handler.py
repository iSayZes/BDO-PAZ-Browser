from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.binary import whole_float
from _common.character import character_name
from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from .parser import (
    OFFSET_FILE,
    hp_dice,
    move_dice,
    parse_servantexperience_offset_records,
    parse_servantexperience_records,
    stamina_dice,
)


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# Stats are percent x 10,000 and weight is LT x 10,000, as the stable window
# divides them (panel_dialog_servantinfo_all_1.luac).
_STAT_SCALE = 10_000
_WEIGHT_SCALE = 10_000


def servant_experience_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_id", "characterId"),
            OffsetColumn("level", "level"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        parse_servantexperience_offset_records,
    )


def _stat_text(value: int) -> str:
    return f"{value / _STAT_SCALE:.1f}%"


def _weight_lt(value: int) -> float | int:
    return whole_float(value / _WEIGHT_SCALE)


def _with_display_fields(record: dict, names: dict[int, str]) -> dict:
    dice = record["growth_dice"]
    return {
        **record,
        # The shown name: LOC in the user's language, else the character ID.
        "name": names[record["character_id"]],
        "hp_dice": hp_dice(dice) or None,
        "stamina_dice": stamina_dice(dice) or None,
        "move_dice": move_dice(dice) or None,
    }


class ServantExperienceHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["name"], sort_key="name"),
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["exp"], "num", sort_key="exp"),
            Column(cols["hp"], "num", sort_key="max_hp"),
            Column(cols["stamina"], "num", sort_key="max_mp"),
            Column(cols["weight"], "num", sort_key="max_weight"),
            Column(cols["accel"], "num", sort_key="acceleration"),
            Column(cols["speed"], "num", sort_key="speed"),
            Column(cols["turn"], "num", sort_key="turn"),
            Column(cols["brake"], "num", sort_key="brake"),
            Column(cols["hpDice"], sort_key="hp_dice"),
            Column(cols["staminaDice"], sort_key="stamina_dice"),
            Column(cols["moveDice"], sort_key="move_dice"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{OFFSET_FILE} companion not found.")

        records = parse_servantexperience_records(data, offset_raw)
        # One LOC lookup per servant, not one per level record.
        names = {
            character_id: character_name(character_id) or str(character_id)
            for character_id in {record["character_id"] for record in records}
        }
        return [_with_display_fields(record, names) for record in records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        meta = handler_text(
            self.lang,
            _LANG_DIR,
            "meta.count",
            count=len(records),
            servants=len({record["character_id"] for record in records}),
        )
        weight_unit = handler_text(self.lang, _LANG_DIR, "units.weight")
        rows = [
            [
                e(r["character_id"]),
                e(r["name"]),
                e(r["level"]),
                e(f"{r['exp']:,}"),
                e(f"{r['max_hp']:,}"),
                e(f"{r['max_mp']:,}"),
                e(f"{_weight_lt(r['max_weight']):,} {weight_unit}"),
                e(_stat_text(r["acceleration"])),
                e(_stat_text(r["speed"])),
                e(_stat_text(r["turn"])),
                e(_stat_text(r["brake"])),
                e(r["hp_dice"] or _EMPTY),
                e(r["stamina_dice"] or _EMPTY),
                e(r["move_dice"] or _EMPTY),
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
