from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_loc_name, character_loc_title
from _common.contents_group import contents_group_key, contents_groups_text
from _common.html import Column, e, error, icon_cell, sort_keys, table
from _common.icon_index import IconKind, icon_path
from _common.item_key import item_name_tagged
from _common.lang import handler_text, load_handler_strings
from _common.pabr_offset import parse_pabr_offset_rows
from _common.pa_text import pa_cell, pa_fields
from _common.tribe_labels import tribe_text
from _common.offset_table import (
    OffsetColumn,
    OffsetTableHandler,
    offset_column,
    offset_records,
    size_column,
)
from .parser import (
    NO_CLASS_TYPE,
    NO_VEHICLE_TYPE,
    korean_name,
    korean_title,
    npc_kind_name,
    npc_kind_text,
    parse_characterstatic_records,
)
from _common.vehicle_type import VEHICLE_TYPE_NAMES, vehicle_type_text

_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# The contents group key of a character in no group.
_NO_CONTENTS_GROUP = 0


def _optional(value: int | None) -> str:
    return _EMPTY if value is None else e(value)


def _contents_groups_text(group_hashes: tuple[int, ...]) -> str:
    """`6, 1448`: the keys behind the hashes, a hash in hex where no key fits; '' for key 0 alone (no group)."""
    if [contents_group_key(group_hash) for group_hash in group_hashes] == [_NO_CONTENTS_GROUP]:
        return ""
    return contents_groups_text(group_hashes)


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
            Column(cols["title"], sort_key="title"),
            Column(cols["label"], sort_key="label_kr"),
            Column(cols["actionScript"], sort_key="action_script"),
            Column(cols["conditionScript"], sort_key="condition_script"),
            Column(cols["knowledgeId"], "num", sort_key="knowledge_id"),
            # Sorts by the number; the cell adds the 2016 name where there is one.
            Column(cols["npcKind"], sort_key="npc_kind"),
            Column(cols["grade"], "num", sort_key="grade"),
            Column(cols["level"], "num", sort_key="level"),
            # Sorts by the number; the cell adds the species label where there is one.
            Column(cols["tribe"], sort_key="tribe_type"),
            Column(cols["characterGroup"], "num", sort_key="character_group"),
            Column(cols["karma"], "num", sort_key="tendency_on_dead"),
            Column(cols["navalFame"], "num", sort_key="ocean_tendency"),
            Column(cols["vehicleType"], sort_key="vehicle_type"),
            Column(cols["classType"], "num", sort_key="class_type"),
            Column(cols["bodySize"], "num", sort_key="body_size"),
            Column(cols["aiScript"], sort_key="ai_script"),
            Column(cols["model"], sort_key="model_path"),
            Column(cols["contentsGroups"], sort_key="contents_groups"),
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
            row.append(e(r["title"] or _EMPTY))
            row.append(e(r["label_kr"] or _EMPTY))
            row.append(e(r["action_script"]))
            row.append(e(r["condition_script"]))
            row.append(_optional(r["knowledge_id"]))
            row.append(e(npc_kind_text(r["npc_kind"])))
            row.append(e(r["grade"]))
            row.append(e(r["level"]))
            row.append(e(tribe_text(r["tribe_type"])))
            row.append(_optional(r["character_group"]))
            row.append(e(r["tendency_on_dead"]))
            row.append(e(r["ocean_tendency"]))
            vehicle_type = r["vehicle_type"]
            row.append(_EMPTY if vehicle_type is None else e(vehicle_type_text(vehicle_type)))
            row.append(_optional(r["class_type"]))
            row.append(e(r["body_size"]))
            row.append(e(r["ai_script"] or _EMPTY))
            row.append(e(r["model_path"] or _EMPTY))
            row.append(e(r["contents_groups"] or _EMPTY))
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
        # The LOC name in the user's language, else the Korean name the record
        # stores, the same text as the CHARACTER_NAME_KR lookup index.
        "name": character_loc_name(character_id) or korean_name(raw["name_kr"], raw["label_kr"]),
        # The same for the title (`<Node Manager>`), the CHARACTER_TITLE_KR text;
        # most characters have none.
        "title": character_loc_title(character_id) or korean_title(raw["title_kr"]),
        "label_kr": raw["label_kr"],
        "action_script": raw["action_script"],
        "condition_script": raw["condition_script"],
        "knowledge_id": raw["knowledge_id"],
        "npc_kind": raw["npc_kind"],
        "npc_kind_name": npc_kind_name(raw["npc_kind"]),
        "grade": raw["grade"],
        "level": raw["level"],
        "tribe_type": raw["tribe_type"],
        # 0 means "in no group".
        "character_group": raw["character_group"] or None,
        "tendency_on_dead": raw["tendency_on_dead"],
        "ocean_tendency": raw["ocean_tendency"],
        # 65 means "not a vehicle".
        "vehicle_type": None if vehicle_type == NO_VEHICLE_TYPE else vehicle_type,
        "vehicle_type_name": VEHICLE_TYPE_NAMES.get(vehicle_type, ""),
        # 101 means "not a player character".
        "class_type": None if raw["class_type"] == NO_CLASS_TYPE else raw["class_type"],
        "body_size": raw["body_size"],
        "ai_script": raw["ai_script"],
        "model_path": raw["model_path"],
        "contents_groups": _contents_groups_text(raw["contents_group_hashes"]),
        "source_item_id": source_item_id,
        # The LOC name in the user's language, else the Korean name itemenchant.dbss stores.
        **pa_fields("source_item_name", item_name_tagged(source_item_id) if source_item_id else ""),
        "payload_size": raw["payload_size"],
    }
