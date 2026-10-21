from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_loc_name, character_title
from _common.html import Column, e, error, sort_keys, table
from _common.lang import handler_text, load_handler_strings
from _common.vehicle_type import VEHICLE_TYPE_NAMES, vehicle_type_text
from _dbss.characterstatic.parser import NO_CLASS_TYPE, NO_VEHICLE_TYPE, npc_kind_name, npc_kind_text

from .parser import parse_charactersimply_records

_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _optional(value: int | None) -> str:
    return _EMPTY if value is None else e(value)


def _record(raw: dict) -> dict:
    """One preview row: names resolved, sentinel values stored as None so they sort last."""
    character_id = raw["character_id"]
    vehicle_type = raw["vehicle_type"]
    return {
        **raw,
        # The LOC name in the user's language, else the Korean name the row points at.
        "name": character_loc_name(character_id) or raw["name_kr"],
        "title": character_title(character_id) or raw["title_kr"],
        "npc_kind_name": npc_kind_name(raw["npc_kind"]),
        # 0 means "in no group".
        "character_group": raw["character_group"] or None,
        # 65 means "not a vehicle".
        "vehicle_type": None if vehicle_type == NO_VEHICLE_TYPE else vehicle_type,
        "vehicle_type_name": VEHICLE_TYPE_NAMES.get(vehicle_type, ""),
        # 101 means "not a player character".
        "class_type": None if raw["class_type"] == NO_CLASS_TYPE else raw["class_type"],
    }


class CharacterSimplyBssHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["name"], sort_key="name"),
            Column(cols["title"], sort_key="title"),
            # Sorts by the number; the cell adds the 2016 name where there is one.
            Column(cols["npcKind"], sort_key="npc_kind"),
            Column(cols["grade"], "num", sort_key="grade"),
            Column(cols["level"], "num", sort_key="level"),
            Column(cols["characterGroup"], "num", sort_key="character_group"),
            Column(cols["maxHp"], "num", sort_key="max_hp"),
            Column(cols["bodySize"], "num", sort_key="body_size"),
            Column(cols["vehicleType"], sort_key="vehicle_type"),
            Column(cols["classType"], "num", sort_key="class_type"),
            Column(cols["model"], sort_key="model_path"),
            Column(cols["voice"], sort_key="voice_bank"),
            Column(cols["actionScript"], sort_key="action_script"),
            Column(cols["knowledgeId"], "num", sort_key="knowledge_id"),
            Column(cols["conditionScript"], sort_key="condition_script"),
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
            raw_records = parse_charactersimply_records(data)
        except ValueError as ex:
            return [{"_error": f"charactersimply.bss could not be parsed: {ex}"}]
        return [_record(raw) for raw in raw_records]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        start = page * page_size
        page_records = records[start : start + page_size]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))
        rows = [
            [
                e(r["character_id"]),
                e(r["name"] or _EMPTY),
                e(r["title"] or _EMPTY),
                e(npc_kind_text(r["npc_kind"])),
                e(r["grade"]),
                e(r["level"]),
                _optional(r["character_group"]),
                e(r["max_hp"]),
                e(r["body_size"]),
                _EMPTY if r["vehicle_type"] is None else e(vehicle_type_text(r["vehicle_type"])),
                _optional(r["class_type"]),
                e(r["model_path"] or _EMPTY),
                e(r["voice_bank"] or _EMPTY),
                e(r["action_script"]),
                _optional(r["knowledge_id"]),
                e(r["condition_script"]),
            ]
            for r in page_records
        ]
        return table(meta, self._columns(), rows)
