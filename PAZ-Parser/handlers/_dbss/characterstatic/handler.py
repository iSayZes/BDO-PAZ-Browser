from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.html import Column, e, error, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_name_tagged
from _common.lang import handler_text, load_handler_strings
from _common.pabr_offset import parse_pabr_offset_rows
from _common.pa_text import pa_cell, pa_fields
from _common.offset_table import (
    OffsetColumn,
    OffsetTableHandler,
    offset_column,
    offset_records,
    size_column,
)
from .parser import NO_CLASS_TYPE, NO_VEHICLE_TYPE, parse_characterstatic_records
from _common.vehicle_type import VEHICLE_TYPE_NAMES, vehicle_type_text

_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _optional(value: int | None) -> str:
    return _EMPTY if value is None else e(value)


def character_static_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_id", "characterId"),
            offset_column("offset", "byteOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_pabr_offset_rows, "character_id"),
    )


class CharacterStaticHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        columns = [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["icon"], sort_key="icon_path"),
            Column(cols["name"], sort_key="name"),
            Column(cols["actionScript"], sort_key="action_script"),
            Column(cols["conditionScript"], sort_key="condition_script"),
            Column(cols["knowledgeId"], "num", sort_key="knowledge_id"),
            Column(cols["npcKind"], "num", sort_key="npc_kind"),
            Column(cols["grade"], "num", sort_key="grade"),
            Column(cols["karma"], "num", sort_key="tendency_on_dead"),
            Column(cols["navalFame"], "num", sort_key="ocean_tendency"),
            Column(cols["vehicleType"], sort_key="vehicle_type"),
            Column(cols["classType"], "num", sort_key="class_type"),
            Column(cols["aiScript"], sort_key="ai_script"),
            Column(cols["model"], sort_key="model_path"),
            Column(cols["sourceItemId"], "num", sort_key="source_item_id"),
            Column(cols["sourceItem"], sort_key="source_item_name"),
            Column(cols["payloadSize"], "num", sort_key="payload_size"),
        ]
        return columns

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [
            f"{folder}/characterstaticoffset.dbss",
        ]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get("characterstaticoffset.dbss")
        if not offset_raw:
            return [{"_error": "characterstaticoffset.dbss companion not found"}]

        try:
            raw_records = parse_characterstatic_records(data, parse_pabr_offset_rows(offset_raw))
        except ValueError as ex:
            return [{"_error": f"characterstatic.dbss could not be parsed: {ex}"}]

        return [_record(r) for r in raw_records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))

        rows: list[list[str]] = []
        for r in slice_:
            row: list[str] = [
                e(r["character_id"]),
                icon_cell(r["icon_path"]) if r["icon_path"] else _EMPTY,
            ]
            row.append(e(r["name"] or _EMPTY))
            row.append(e(r["action_script"]))
            row.append(e(r["condition_script"]))
            row.append(_optional(r["knowledge_id"]))
            row.append(e(r["npc_kind"]))
            row.append(e(r["grade"]))
            row.append(e(r["tendency_on_dead"]))
            row.append(e(r["ocean_tendency"]))
            vehicle_type = r["vehicle_type"]
            row.append(_EMPTY if vehicle_type is None else e(vehicle_type_text(vehicle_type)))
            row.append(_optional(r["class_type"]))
            row.append(e(r["ai_script"] or _EMPTY))
            row.append(e(r["model_path"] or _EMPTY))
            row.append(_optional(r["source_item_id"]))
            row.append(pa_cell(r, "source_item_name") if r["source_item_name"] else _EMPTY)
            row.append(e(r["payload_size"]))
            rows.append(row)

        return table(meta, self._columns(), rows)


def _record(raw: dict) -> dict:
    """One preview row: names resolved, sentinel values stored as None so they sort last."""
    character_id = raw["character_id"]
    vehicle_type = raw["vehicle_type"]
    source_item_id = raw["source_item_id"] or None
    return {
        "character_id": character_id,
        "icon_path": icon_path(IconKind.CHARACTER, character_id),
        # The LOC name in the user's language, else the Korean name the record stores.
        "name": character_name(character_id) or raw["name_kr"],
        "action_script": raw["action_script"],
        "condition_script": raw["condition_script"],
        "knowledge_id": raw["knowledge_id"],
        "npc_kind": raw["npc_kind"],
        "grade": raw["grade"],
        "tendency_on_dead": raw["tendency_on_dead"],
        "ocean_tendency": raw["ocean_tendency"],
        # 65 means "not a vehicle".
        "vehicle_type": None if vehicle_type == NO_VEHICLE_TYPE else vehicle_type,
        "vehicle_type_name": VEHICLE_TYPE_NAMES.get(vehicle_type, ""),
        # 101 means "not a player character".
        "class_type": None if raw["class_type"] == NO_CLASS_TYPE else raw["class_type"],
        "ai_script": raw["ai_script"],
        "model_path": raw["model_path"],
        "source_item_id": source_item_id,
        # The LOC name in the user's language, else the Korean name itemenchant.dbss stores.
        **pa_fields("source_item_name", item_name_tagged(source_item_id) if source_item_id else ""),
        "payload_size": raw["payload_size"],
    }
