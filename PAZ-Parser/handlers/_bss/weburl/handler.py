"""weburl.bss preview handler: one row per web address, with its insert points.

The URL column shows the text with `<insert_type>` where the client fills in
a value; which value each type is stays open (weburl_bss.md, Open Questions).
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from _common.html import Column, e
from _common.row_table import RowTableHandler
from .parser import FILE_NAME, parse_weburl_records


_LANG_DIR = Path(__file__).parent / "lang"
_EMPTY = "-"


def _inserts_text(inserts: list[dict]) -> str:
    """Each insert point as `offset: type`, in file order."""
    return ", ".join(f"{insert['insert_offset']}: {insert['insert_type']}" for insert in inserts)


class WebUrlBssHandler(RowTableHandler):
    file_name = FILE_NAME
    lang_dir = _LANG_DIR

    def columns(self, labels: Mapping[str, str]) -> list[Column]:
        return [
            Column(labels["position"], "num", sort_key="position"),
            Column(labels["url"], sort_key="url_template"),
            Column(labels["inserts"]),
        ]

    def read_records(self, data: bytes, companions: dict[str, bytes]) -> list[dict]:
        return parse_weburl_records(data)

    def cells(self, record: dict) -> list[str]:
        return [
            e(record["position"]),
            e(record["url_template"] or _EMPTY),
            e(_inserts_text(record["inserts"]) or _EMPTY),
        ]
