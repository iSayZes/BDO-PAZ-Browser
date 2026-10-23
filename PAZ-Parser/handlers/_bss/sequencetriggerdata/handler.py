"""sequencetriggerdata.bss preview handler: one row per sequence trigger.

The sequence stays a path, folder and file name as the source XML writes
it; the `sequence/` files it names have no handler. Region names are LOC
type 17 of the region keys. The Options column lists the set flags.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _bss.sequence_scripts.display import EMPTY, contents_group_key, position_text, radius_text
from _common.html import Column, e
from _common.lang import load_handler_strings
from _common.row_table import RowTableHandler
from _common.town import town_name
from .parser import FILE_NAME, FLAG_FIELDS, parse_sequencetriggerdata_records


_LANG_DIR = Path(__file__).parent / "lang"


def sequence_path(folder: str, file_name: str) -> str:
    """`Sadang/CS_SadangSeoul_06_02_Pyeseja`: the folder and file name as the source XML joins them."""
    return f"{folder}/{file_name}" if folder else file_name


class SequenceTriggerDataBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["sequenceFile"], sort_key="sequence_path"),
            Column(labels["regionKeys"], "num", sort_key="region_keys_text"),
            Column(labels["regions"], sort_key="region_names_text"),
            Column(labels["contentsGroup"], "num", sort_key="contents_group_key"),
            Column(labels["position"], sort_key="position_text"),
            Column(labels["radius"], "num", sort_key="radius"),
            Column(labels["resurrectPosition"], sort_key="resurrect_position_text"),
            Column(labels["startCondition"], sort_key="start_condition"),
            Column(labels["startExecute"], sort_key="start_execute"),
            Column(labels["endExecute"], sort_key="end_execute"),
            Column(labels["skipCondition"], sort_key="skip_condition"),
            Column(labels["forceSkipEndExecute"], sort_key="force_skip_end_execute"),
            Column(labels["options"], sort_key="options_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        records = []
        for record in parse_sequencetriggerdata_records(data):
            options = [field for field in FLAG_FIELDS if record[field]]
            records.append({
                **record,
                "sequence_path": sequence_path(record["folder"], record["file_name"]),
                "region_keys_text": ", ".join(str(key) for key in record["region_keys"]),
                "region_names_text": ", ".join(name for name in map(town_name, record["region_keys"]) if name),
                "contents_group_key": contents_group_key(record["contents_group_open"]),
                "position_text": position_text(record["position"]),
                "resurrect_position_text": position_text(record["resurrect_position"]),
                "options": options,
                "options_text": ", ".join(options),
            })
        return records

    def cells(self, record: dict) -> list[str]:
        flag_labels = load_handler_strings(self.lang, _LANG_DIR)["flags"]
        options = ", ".join(flag_labels[field] for field in record["options"])
        return [
            e(record["sequence_path"]),
            e(record["region_keys_text"] or EMPTY),
            e(record["region_names_text"] or EMPTY),
            e(record["contents_group_open"] or EMPTY),
            e(record["position_text"]),
            e(radius_text(record["radius"])),
            e(record["resurrect_position_text"]),
            e(record["start_condition"] or EMPTY),
            e(record["start_execute"] or EMPTY),
            e(record["end_execute"] or EMPTY),
            e(record["skip_condition"] or EMPTY),
            e(record["force_skip_end_execute"] or EMPTY),
            e(options or EMPTY),
        ]
