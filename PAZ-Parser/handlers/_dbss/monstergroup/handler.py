from __future__ import annotations

from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.character import character_name
from _common.html import Column, e, sort_keys, table, text_list_cell
from _common.hunting_ground import character_hunting_grounds, hunting_ground_list_cell, hunting_ground_text
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import (
    OffsetColumn,
    OffsetTableHandler,
    offset_column,
    offset_records,
    size_column,
)
from _common.rate import rate_percent
from .parser import parse_monstergroup_offset_rows, parse_monstergroup_records


_LANG_DIR = Path(__file__).parent / "lang"
_OFFSET_FILE = "monstergroupoffset.dbss"
_EMPTY = "-"
_LIST_PREVIEW_MONSTERS = 6
_LIST_PREVIEW_HUNTING_GROUNDS = 3


def _monster_text(member: dict) -> str:
    """`Altar Imp (20%)`: the monster's name, else its key, and its percent."""
    key = member["character_key"]
    name = character_name(key) or str(key)
    return f"{name} ({rate_percent(member['percent'])})"


def _hunting_ground_fields(members: list[dict]) -> dict:
    """The hunting grounds whose monster list holds at least one member, by key and name.

    `monstergroup.dbss` stores no hunting ground; the keys come from the
    `CHARACTER_HUNTING_GROUNDS` lookup index (`dropuihuntinggroundinfo.bss`).
    """
    keys = character_hunting_grounds(member["character_key"] for member in members)
    return {"hunting_ground_keys": list(keys), "hunting_grounds": [hunting_ground_text(key) for key in keys]}


def monster_group_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("group_key", "groupKey"),
            offset_column("offset", "byteOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_monstergroup_offset_rows, "group_key"),
    )


class MonsterGroupHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["groupKey"], "num", sort_key="group_key"),
            Column(cols["memberCount"], "num", sort_key="member_count"),
            # List columns: they would only sort by their string form.
            Column(cols["monsters"]),
            Column(cols["huntingGrounds"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{_OFFSET_FILE}"]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        offset_raw = companions.get(_OFFSET_FILE)
        if offset_raw is None:
            raise ValueError(f"{_OFFSET_FILE} companion not found.")

        return [
            {
                **record,
                "monsters": [_monster_text(member) for member in record["members"]],
                **_hunting_ground_fields(record["members"]),
            }
            for record in parse_monstergroup_records(data, offset_raw)
        ]

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        members = sum(record["member_count"] for record in records)
        meta = handler_text(self.lang, _LANG_DIR, "meta.count", count=len(records), members=members)
        rows = [
            [
                e(r["group_key"]),
                e(r["member_count"]),
                text_list_cell(r["monsters"], _LIST_PREVIEW_MONSTERS) or _EMPTY,
                hunting_ground_list_cell(
                    r["hunting_ground_keys"], r["hunting_grounds"], _LIST_PREVIEW_HUNTING_GROUNDS
                )
                or _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
