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
from _common.duration import format_duration
from _common.html import Column, e, sort_keys, table, text_list_cell
from _common.lang import handler_text, load_handler_strings
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, offset_records, size_column
from _common.pabr_offset import parse_bare_offset_rows
from _common.skill import skill_name
from _dbss.servantbuff.parser import FILE_NAME as SERVANT_BUFF_FILE, servant_buff_skills
from .parser import parse_servantinteraction_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_BUFFS_SHOWN = 5


def servant_interaction_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn("character_id", "characterId"),
            offset_column("offset", "dataOffset"),
            size_column("size", "size"),
        ],
        offset_records(parse_bare_offset_rows, "character_id"),
    )


def _buff_label(buff_key: int, buff_skills: dict[int, int]) -> str:
    """The name of the skill the buff uses, else the bare buff key."""
    skill_no = buff_skills.get(buff_key)
    return (skill_name(skill_no) if skill_no is not None else "") or str(buff_key)


class ServantInteractionHandler(PreviewHandler):
    def _columns(self) -> list[Column]:
        cols = load_handler_strings(self.lang, _LANG_DIR)["columns"]
        return [
            Column(cols["characterId"], "num", sort_key="character_id"),
            Column(cols["name"], sort_key="name"),
            Column(cols["coolTime"], "num", sort_key="cool_time"),
            Column(cols["buffs"]),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [
            characterstatic_offset_companion(entry.internal_path),
            f"{folder}/{SERVANT_BUFF_FILE}",
        ]

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        row_ids = character_row_ids(companions)
        try:
            buff_skills = servant_buff_skills(companions.get(SERVANT_BUFF_FILE))
        except ValueError as ex:
            raise ValueError(f"{SERVANT_BUFF_FILE}: {ex}") from ex
        return [
            {
                **record,
                # The shown name: LOC in the user's language, else the character ID.
                "name": character_name(record["character_id"]) or str(record["character_id"]),
                "buffs": [_buff_label(key, buff_skills) for key in record["buff_keys"]],
                "has_character_row": has_character_row(row_ids, record["character_id"]),
            }
            for record in parse_servantinteraction_records(data)
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
                character_key_cell(r["character_id"], r["has_character_row"]),
                e(r["name"]),
                # Milliseconds: the interaction panel shows it through convertStringFromMillisecondtime.
                e(format_duration(r["cool_time"]) or "0"),
                text_list_cell(r["buffs"], _BUFFS_SHOWN) or _EMPTY,
            ]
            for r in records[start : start + page_size]
        ]
        return table(meta, self._columns(), rows)
