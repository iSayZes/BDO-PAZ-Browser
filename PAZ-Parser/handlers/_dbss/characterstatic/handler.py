from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.loc import is_loc_loaded
from _common.html import Column, e, error, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.lang import handler_text, load_handler_strings
from _common.pabr_offset import parse_pabr_offset_rows
from _common.offset_table import (
    OffsetColumn,
    OffsetTableHandler,
    offset_column,
    offset_records,
    size_column,
)
from .parser import NO_CLASS_TYPE, parse_characterstatic_records

_LANG_DIR = Path(__file__).parent / "lang"
# The low byte of `npc_kind` is the character kind; the higher bits are unmapped flags.
_NPC_KIND_LOW_MASK = 0xFF
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
    def _columns(self, has_loc: bool) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        columns = [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["icon"], sort_key="icon_path"),
        ]
        if has_loc:
            columns.append(Column(cols["name"], sort_key="name"))
        columns += [
            Column(cols["actionScript"], sort_key="action_script"),
            Column(cols["conditionScript"], sort_key="condition_script"),
            Column(cols["knowledgeId"], "num", sort_key="knowledge_id"),
            Column(cols["npcKind"], "num", sort_key="npc_kind_low"),
            Column(cols["classType"], "num", sort_key="class_type"),
            Column(cols["aiScript"], sort_key="ai_script"),
            Column(cols["model"], sort_key="model_path"),
            Column(cols["payloadSize"], "num", sort_key="payload_size"),
        ]
        return columns

    def sortable_fields(self) -> tuple[str, ...]:
        # Includes the name, so a saved sort survives LOC not being loaded.
        return sort_keys(self._columns(has_loc=True))

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

        has_loc = is_loc_loaded()
        return [
            {
                "character_id": r["character_id"],
                "icon_path": icon_path(IconKind.CHARACTER, r["character_id"]),
                "name": character_name(r["character_id"]),
                "action_script": r["action_script"],
                "condition_script": r["condition_script"],
                "knowledge_id": r["knowledge_id"],
                "npc_kind": r["npc_kind"],
                "npc_kind_low": r["npc_kind"] & _NPC_KIND_LOW_MASK,
                # 101 means "not a player character"; None sorts last.
                "class_type": None if r["class_type"] == NO_CLASS_TYPE else r["class_type"],
                "ai_script": r["ai_script"],
                "model_path": r["model_path"],
                "payload_size": r["payload_size"],
            }
            for r in raw_records
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        if records and "_error" in records[0]:
            return error(records[0]["_error"])

        has_loc = is_loc_loaded()

        start = page * page_size
        slice_ = records[start : start + page_size]
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records))

        rows: list[list[str]] = []
        for r in slice_:
            row: list[str] = [
                e(r["character_id"]),
                icon_cell(r["icon_path"]) if r["icon_path"] else _EMPTY,
            ]
            if has_loc:
                row.append(e(r["name"]))
            row.append(e(r["action_script"]))
            row.append(e(r["condition_script"]))
            row.append(_optional(r["knowledge_id"]))
            row.append(e(r["npc_kind_low"]))
            row.append(_optional(r["class_type"]))
            row.append(e(r["ai_script"] or _EMPTY))
            row.append(e(r["model_path"] or _EMPTY))
            row.append(e(r["payload_size"]))
            rows.append(row)

        return table(meta, self._columns(has_loc), rows)
