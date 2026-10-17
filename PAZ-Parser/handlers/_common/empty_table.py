"""One preview handler for tables the client ships empty: a u32 count of 0 and no records.

The tables are listed in `_dbss/empty_tables/tables.py` (a bare count) and
`_bss/empty_tables/tables.py` (PABR, the count after the magic, read by that
package's parser). The preview is one status row with the header count. A
file that declares records raises ValueError, so a patch that fills the table
shows as a parse error instead of an empty preview. Labels come from
`_common/lang/` (`emptyColumns`).
"""

from __future__ import annotations

import struct
from collections.abc import Callable
from pathlib import Path

from bdo_models import PazEntry
from bdo_preview import PreviewHandler

from _common.html import Column, e, sort_keys, table
from _common.lang import handler_text, load_handler_strings

_COMMON_LANG_DIR = Path(__file__).parent / "lang"
_COUNT_SIZE = 4

# (data, file name, status text) -> the one status row.
EmptyTableParser = Callable[[bytes, str, str], list[dict]]


def parse_empty_table(data: bytes, file_name: str, status: str) -> list[dict]:
    """One status row for a zero-count table; `extra_bytes` counts bytes after the count."""
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{file_name} is too short to contain a record-count header.")

    count = struct.unpack_from("<I", data, 0)[0]
    if count != 0:
        raise ValueError(
            f"{file_name} declares {count} records, but only the empty layout is documented."
        )
    return [{"count": count, "status": status, "extra_bytes": len(data) - _COUNT_SIZE}]


class EmptyTableHandler(PreviewHandler):
    """Renders a zero-count table; see the module docstring."""

    def __init__(self, file_name: str, parse: EmptyTableParser = parse_empty_table) -> None:
        self._file_name = file_name
        self._parse = parse

    def _columns(self) -> list[Column]:
        labels = load_handler_strings(self.lang, _COMMON_LANG_DIR)["emptyColumns"]
        return [
            Column(labels["count"], "num", sort_key="count"),
            Column(labels["status"], sort_key="status"),
        ]

    def sortable_fields(self) -> tuple[str, ...]:
        return sort_keys(self._columns())

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        status = handler_text(self.lang, _COMMON_LANG_DIR, "meta.noRecords")
        return self._parse(data, self._file_name, status)

    def render_records_page(
        self,
        records: list[dict],
        page: int,
        page_size: int,
    ) -> str:
        start = page * page_size
        count = records[0]["count"] if records else 0
        meta = handler_text(self.lang, _COMMON_LANG_DIR, "meta.headerCount", count=count)
        rows = [[e(r["count"]), e(r["status"])] for r in records[start : start + page_size]]
        return table(meta, self._columns(), rows)
