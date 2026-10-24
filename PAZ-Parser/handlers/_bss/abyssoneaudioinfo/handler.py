"""abyssoneaudioinfo.bss preview handler: the music and ambience of each Abyss One field."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _bss.audioinfo.bgm_states import bgm_states_cell
from _bss.fieldinfo.names import field_no_label, field_no_link
from _common.html import Column, e
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_abyssoneaudioinfo_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


class AbyssOneAudioInfoBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["fieldNo"], "num", sort_key=KEY_FIELD),
            Column(labels["field"], sort_key="field_name"),
            Column(labels["bgmStates"], sort_key="bgm_states_text"),
            Column(labels["bankNoEnvironment"], "num", sort_key="bank_no_environment"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return [
            {**record, "field_name": field_no_label(record[KEY_FIELD])}
            for record in parse_abyssoneaudioinfo_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        return [
            field_no_link(record[KEY_FIELD]),
            e(record["field_name"] or _EMPTY),
            bgm_states_cell(record["bgm_state_names"]),
            e(record["bank_no_environment"]),
        ]
