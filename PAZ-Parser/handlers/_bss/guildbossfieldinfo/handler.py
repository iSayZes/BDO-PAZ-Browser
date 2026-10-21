"""guildbossfieldinfo.bss preview handler: the guild boss field point of each boss."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _bss.boss_spawn.parser import FILE_NAME as BOSS_SPAWN_FILE
from _bss.boss_spawnlevel.parser import FILE_NAME as LEVEL_FILE, boss_characters
from _common.character import character_name
from _common.html import Column, e, record_link
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_guildbossfieldinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_AXES = ("x", "y", "z")
_LINK_CLASS = "record-link"
_BOSS_SPAWN_PATH = f"gamecommondata/binary/{BOSS_SPAWN_FILE}"


def _characters(level_data: bytes | None) -> dict[int, int]:
    """Boss key -> character from the optional levels file; empty when it is
    missing or unreadable, since the names are only a convenience here."""
    if level_data is None:
        return {}
    try:
        return boss_characters(level_data)
    except ValueError:
        return {}


class GuildBossFieldInfoHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["bossSpawnKey"], "num", sort_key=KEY_FIELD),
            Column(labels["boss"], sort_key="boss_name"),
            *(Column(labels[axis], "num", sort_key=axis) for axis in _AXES),
        ]

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{LEVEL_FILE}"]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        characters = _characters(companions.get(LEVEL_FILE))
        return [
            {
                **record,
                "boss_name": character_name(characters[record[KEY_FIELD]]) if record[KEY_FIELD] in characters else "",
            }
            for record in parse_guildbossfieldinfo_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        key = record[KEY_FIELD]
        return [
            record_link(str(key), _BOSS_SPAWN_PATH, "key", key, _LINK_CLASS),
            e(record["boss_name"] or "-"),
            *(e(f"{record[axis]:,.0f}") for axis in _AXES),
        ]
