"""charactervoice.bss preview handler: the voices each character can pick, per appearance type."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.character import character_name
from _common.character_link import (
    character_key_cell,
    character_row_ids,
    characterstatic_offset_companion,
    has_character_row,
)
from _common.html import Column, e, html_list_cell
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_charactervoice_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_SEPARATOR = "; "


def _voices_cell(names: list[str]) -> str:
    return html_list_cell([e(name) for name in names], separator="<br>") or _EMPTY


class CharacterVoiceBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        return [characterstatic_offset_companion(entry.internal_path)]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["characterKey"], "num", sort_key=KEY_FIELD),
            Column(labels["character"], sort_key="name"),
            Column(labels["voices"], sort_key="voices_0_text"),
            Column(labels["voiceCount"], "num", sort_key="voice_count_0"),
            Column(labels["voices1"], sort_key="voices_1_text"),
            Column(labels["voiceCount1"], "num", sort_key="voice_count_1"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        row_ids = character_row_ids(companions)
        return [
            {
                **record,
                "name": character_name(record[KEY_FIELD]),
                "has_character_row": has_character_row(row_ids, record[KEY_FIELD]),
                # One sort and search field per appearance type: the names, then the count.
                **{
                    f"voices_{appearance}_text": _LIST_SEPARATOR.join(names) or None
                    for appearance, names in enumerate(record["voice_names"])
                },
                **{
                    f"voice_count_{appearance}": count
                    for appearance, count in enumerate(record["voice_count"])
                },
            }
            for record in parse_charactervoice_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        first, second = record["voice_names"]
        return [
            character_key_cell(record[KEY_FIELD], record["has_character_row"]),
            e(record["name"] or _EMPTY),
            _voices_cell(first),
            e(record["voice_count_0"]),
            _voices_cell(second),
            e(record["voice_count_1"]),
        ]
