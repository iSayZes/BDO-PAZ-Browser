"""emoticonpackage.dbss preview handler: each package with the emoticons it unlocks."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from bdo_models import PazEntry

from _common.html import Column, IconEntry, e, hidden_slice, icon_list_cell
from _common.offset_table import OffsetColumn, OffsetTableHandler, offset_column, size_column
from _common.row_table import RowTableHandler
from _dbss.emoticon.parser import FILE_NAME as EMOTICON_FILE, KEY_FIELD as EMOTICON_KEY, parse_emoticon_records
from _dbss.emoticon.text import emoticon_name, texture_file
from .parser import FILE_NAME, KEY_FIELD, parse_emoticonpackage_records, parse_emoticonpackageoffset_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# Emoticons shown in the list cell before the rest collapse into a count.
_MAX_EMOTICONS = 6


def emoticon_package_offset_handler() -> OffsetTableHandler:
    return OffsetTableHandler(
        _LANG_DIR,
        [
            OffsetColumn(KEY_FIELD, "packageKey"),
            offset_column("data_offset", "dataOffset"),
            size_column("data_size", "size"),
        ],
        parse_emoticonpackageoffset_records,
    )


def _emoticon_rows(companions: dict[str, bytes]) -> dict[int, dict]:
    """Emoticon key -> its `emoticon.dbss` row, or none without the companion.

    Raises ValueError, naming the companion, when its rows do not parse.
    """
    data = companions.get(EMOTICON_FILE)
    if data is None:
        return {}
    try:
        return {row[EMOTICON_KEY]: row for row in parse_emoticon_records(data)}
    except ValueError as ex:
        raise ValueError(f"{EMOTICON_FILE}: {ex}") from ex


def _entry(emoticon_key: int, rows: dict[int, dict]) -> IconEntry:
    """(icon path, `name (key)`) of one emoticon; the key alone without its row."""
    row = rows.get(emoticon_key)
    if row is None:
        return "", str(emoticon_key)
    return texture_file(row["icon_path"]), f"{emoticon_name(emoticon_key, row['name_kr'])} ({emoticon_key})"


class EmoticonPackageHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def companions(self, entry: PazEntry) -> list[str]:
        folder = entry.internal_path.rsplit("/", 1)[0]
        return [f"{folder}/{EMOTICON_FILE}"]

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["packageKey"], "num", sort_key=KEY_FIELD),
            Column(labels["name"], sort_key="name_kr"),
            Column(labels["emoticonCount"], "num", sort_key="emoticon_count"),
            Column(labels["emoticons"], sort_key="emoticons_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        rows = _emoticon_rows(companions)
        records = []
        for record in parse_emoticonpackage_records(data):
            entries = [_entry(emoticon["emoticon_key"], rows) for emoticon in record["emoticons"]]
            records.append(
                {
                    **record,
                    "emoticon_count": len(entries),
                    "emoticons_text": ", ".join(label for _path, label in entries),
                    "_emoticon_entries": entries,
                }
            )
        return records

    def cells(self, record: dict) -> list[str]:
        entries = record["_emoticon_entries"]
        hidden = [label for _path, label in hidden_slice(entries, _MAX_EMOTICONS)]
        return [
            e(record[KEY_FIELD]),
            e(record["name_kr"]) if record["name_kr"] else _EMPTY,
            e(record["emoticon_count"]),
            icon_list_cell(entries[:_MAX_EMOTICONS], len(entries) - _MAX_EMOTICONS, hidden_names=hidden) or _EMPTY,
        ]
