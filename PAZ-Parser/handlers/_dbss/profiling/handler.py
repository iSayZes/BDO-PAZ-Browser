"""profiling.dbss preview handler: each profiling key's information messages and reward scripts."""
from __future__ import annotations

import re
from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e, text_list_cell, truncate
from _common.offset_table import OffsetTableHandler, keyed_offset_handler
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, KEY_FIELD, parse_profiling_records, parse_profilingoffset_rows


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"
# Each message opens with `[<subject>]에 대한 정보를 획득하였습니다.`
_SUBJECT_RE = re.compile(r"^\[([^\]]+)\]")
_MAX_LIST_ITEMS = 6
_MESSAGE_PREVIEW_CHARS = 160
_SEPARATOR = " | "


def profiling_offset_handler() -> OffsetTableHandler:
    return keyed_offset_handler(_LANG_DIR, parse_profilingoffset_rows, KEY_FIELD, "profilingKey")


def _subject(message: str) -> str:
    match = _SUBJECT_RE.match(message)
    return match.group(1) if match else ""


def _one_line(text: str) -> str:
    return " ".join(text.split())


class ProfilingHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["profilingKey"], "num", sort_key=KEY_FIELD),
            Column(labels["infoCount"], "num", sort_key="info_count"),
            Column(labels["subjects"], sort_key="subjects_text"),
            Column(labels["messages"], sort_key="messages_text"),
            Column(labels["execute"], sort_key="execute_text"),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        records = []
        for record in parse_profiling_records(data):
            messages = [info["profile_message_kr"] for info in record["infos"]]
            subjects = [_subject(message) for message in messages]
            scripts = [info["execute"] for info in record["infos"] if info["execute"]]
            records.append(
                {
                    **record,
                    "info_count": len(messages),
                    "subjects": subjects,
                    "subjects_text": ", ".join(subjects),
                    "messages_text": _SEPARATOR.join(_one_line(message) for message in messages),
                    "execute_text": _SEPARATOR.join(scripts),
                }
            )
        return records

    def cells(self, record: dict) -> list[str]:
        return [
            e(record[KEY_FIELD]),
            e(record["info_count"]),
            text_list_cell(record["subjects"], _MAX_LIST_ITEMS) or _EMPTY,
            e(truncate(record["messages_text"], _MESSAGE_PREVIEW_CHARS)) or _EMPTY,
            e(record["execute_text"]) or _EMPTY,
        ]
