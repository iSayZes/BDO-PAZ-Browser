"""guildhonorsystem.bss preview handler: the Guild Fame change reasons, benefits and daily pay steps.

One row per list entry, in file order. Each row shows its English text (LOC
type 141 for a change reason, 140 for a benefit, the GAME sheet text for a
daily pay step) or its Korean text, and what its parameters name: a guild
boss, a guild skill or a range of guild missions.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _bss.boss_spawn.parser import FILE_NAME as BOSS_SPAWN_FILE
from _bss.boss_spawnlevel.parser import FILE_NAME as LEVEL_FILE, optional_boss_characters
from _common.character import character_name
from _common.html import Column, e, record_link
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from _common.skill import split_skill_key
from _common.skill_cells import skill_label, skill_link
from .parser import FILE_NAME, parse_guildhonorsystem
from .records import (
    BENEFIT_SECTION,
    BOSS_REASON_TYPES,
    CHANGE_REASON_SECTION,
    UNLOCK_SKILL_BENEFIT,
    UPGRADE_SKILL_BENEFIT,
    UPGRADE_ARROW,
    guild_honor_records,
)


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LINK_CLASS = "record-link"
_BOSS_SPAWN_PATH = f"gamecommondata/binary/{BOSS_SPAWN_FILE}"


def _boss_label(boss_key: int, characters: Mapping[int, int]) -> str:
    """`8 Gumiho`, or the bare key without a boss character."""
    character = characters.get(boss_key)
    name = character_name(character) if character is not None else ""
    return f"{boss_key} {name}".strip()


def _skill_key_label(skill_key: int) -> str:
    skill_no, _ = split_skill_key(skill_key)
    return skill_label(skill_no)


def _skill_key_cell(skill_key: int) -> str:
    skill_no, _ = split_skill_key(skill_key)
    return skill_link(skill_no)


def _details_cell(record: dict) -> str:
    """The details text, with the bosses and skills linked to their rows."""
    if not record["details_text"]:
        return _EMPTY
    if record["section"] == CHANGE_REASON_SECTION:
        param = record["reason_param"]
        if record["reason_type"] in BOSS_REASON_TYPES:
            return record_link(record["details_text"], _BOSS_SPAWN_PATH, "key", param, _LINK_CLASS)
        return _skill_key_cell(param)
    if record["section"] == BENEFIT_SECTION and record["benefit_type"] == UNLOCK_SKILL_BENEFIT:
        return _skill_key_cell(record["param_1"])
    if record["section"] == BENEFIT_SECTION and record["benefit_type"] == UPGRADE_SKILL_BENEFIT:
        return f"{_skill_key_cell(record['param_1'])}{e(UPGRADE_ARROW)}{_skill_key_cell(record['param_2'])}"
    return e(record["details_text"])


def _section_label(record: dict, sections: Mapping[str, str]) -> str:
    """Change reasons show as gains or uses by the sign of their point, as the game's two tabs do."""
    if record["section"] == CHANGE_REASON_SECTION:
        return sections["gain"] if record["point"] >= 0 else sections["use"]
    if record["section"] == BENEFIT_SECTION:
        return sections["benefit"]
    return sections["dailyPay"]


def _plain_number(value: int | None) -> str:
    return _EMPTY if value is None else str(value)


class GuildHonorSystemHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["key"], "num", sort_key="key"),
            Column(labels["section"], sort_key="section"),
            Column(labels["description"], sort_key="description"),
            Column(labels["point"], "num", sort_key="point"),
            Column(labels["type"], "num", sort_key="type_value"),
            Column(labels["details"], sort_key="details_text"),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{LEVEL_FILE}"]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        characters = optional_boss_characters(companions.get(LEVEL_FILE))
        return guild_honor_records(
            parse_guildhonorsystem(data),
            boss_label=lambda boss_key: _boss_label(boss_key, characters),
            skill_label=_skill_key_label,
        )

    def cells(self, record: dict) -> list[str]:
        sections = load_handler_strings(self.lang, _LANG_DIR)["sections"]
        return [
            e(_plain_number(record["key"])),
            e(_section_label(record, sections)),
            e(record["description"] or _EMPTY),
            e(f"{record['point']:,}"),
            e(_plain_number(record["type_value"])),
            _details_cell(record),
        ]
