"""midiinstrument.bss preview handler: each composer instrument with its Wwise names, actions and tab."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, flag_cell
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_midiinstrument_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
_LIST_SEPARATOR = ", "


def _hash_text(value: int) -> str:
    return f"0x{value:08X}"


class MidiInstrumentBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["index"], "num", sort_key=KEY_FIELD),
            Column(labels["bankName"], sort_key="bank_name_text"),
            Column(labels["eventName"], sort_key="event_name_text"),
            Column(labels["ingameName"], sort_key="ingame_name_text"),
            Column(labels["articulations"], sort_key="articulations_text"),
            Column(labels["startAction"], sort_key="start_action_hash"),
            Column(labels["endAction"], sort_key="end_action_hash"),
            Column(labels["advancedType"], sort_key="advanced_type"),
            Column(labels["instrumentNameType"], sort_key="instrument_name_type_text"),
            Column(labels["isOpened"], sort_key="is_opened"),
            Column(labels["ingActions"], sort_key="ing_actions_text"),
            Column(labels["isProvided"], sort_key="is_provided"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        advanced_types: Mapping[str, str] = load_handler_strings(self.lang, _LANG_DIR)["advancedTypes"]
        return [
            {
                **record,
                "articulations_text": _LIST_SEPARATOR.join(str(value) for value in record["articulations"]),
                "ing_actions_text": _LIST_SEPARATOR.join(_hash_text(value) for value in record["ing_action_hashes"]),
                "advanced_type_name": advanced_types.get(str(record["advanced_type"]), ""),
            }
            for record in parse_midiinstrument_records(data)
        ]

    def cells(self, record: dict) -> list[str]:
        advanced_type = record["advanced_type_name"] or str(record["advanced_type"])
        return [
            e(record[KEY_FIELD]),
            e(record["bank_name_text"] or _EMPTY),
            e(record["event_name_text"] or _EMPTY),
            e(record["ingame_name_text"] or _EMPTY),
            e(record["articulations_text"] or _EMPTY),
            e(_hash_text(record["start_action_hash"])),
            e(_hash_text(record["end_action_hash"])),
            e(advanced_type),
            e(record["instrument_name_type_text"] or _EMPTY),
            flag_cell(bool(record["is_opened"])),
            e(record["ing_actions_text"] or _EMPTY),
            flag_cell(bool(record["is_provided"])),
        ]
