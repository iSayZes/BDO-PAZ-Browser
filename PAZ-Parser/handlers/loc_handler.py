from __future__ import annotations

import html as _html
import sys
from collections.abc import Sequence
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from bdo_models import PazEntry
from bdo_preview import PreviewHandler, register_handler
from _common.binary import u8, u16, u32
from _common.html import Column, header_cell
from _common.loc import decompress_loc
from _common.pa_text import pa_html
from table_sort import TableSort, sort_order_by_values
from ui_text import ui_text



_LocRecordMeta = tuple[int, int, int, int, int, int, int, int]

# Record fields that sort the table; str_type_text sorts from the CLI and API only.
_COLUMN_FIELDS = ("str_id1", "str_id2", "str_id3", "str_id4", "str_type", "str_type_text", "text")
# The table's columns by the field they sort by, in order: the type number and
# name share one Type column. Labels are `loc.columns.<key>`.
_TABLE_COLUMNS = (
    ("str_id1", "str_id1"),
    ("str_id2", "str_id2"),
    ("str_id3", "str_id3"),
    ("str_id4", "str_id4"),
    ("str_type", "type"),
    ("text", "text"),
)

# Record fields that sort straight from the index tuple, by tuple position.
_META_FIELD_POSITIONS = {
    "str_type": 1,
    "str_id1": 2,
    "str_id2": 3,
    "str_id3": 4,
    "str_id4": 5,
}


def _parse_all_loc_records(raw: bytes) -> list[tuple[int, int, int, int, int, int, str]]:
    """Parse all loc records: (str_size, str_type, str_id1, str_id2, str_id3, str_id4, text)."""
    data = decompress_loc(raw)
    if data is None:
        return []

    records: list[tuple[int, int, int, int, int, int, str]] = []
    pos = 0

    while pos + 16 <= len(data):
        str_size = u32(data, pos)
        str_type = u32(data, pos + 4)
        str_id1  = u32(data, pos + 8)
        str_id2  = u16(data, pos + 12)
        str_id3  = u8(data, pos + 14)
        str_id4  = u8(data, pos + 15)

        text_start = pos + 16
        text_end   = text_start + str_size * 2

        if text_end + 4 > len(data):
            break

        text = data[text_start:text_end].decode("utf-16-le", errors="replace")
        records.append((str_size, str_type, str_id1, str_id2, str_id3, str_id4, text))
        pos = text_end + 4

    return records


def _columns() -> list[Column]:
    return [Column(ui_text(f"loc.columns.{label}"), sort_key=field) for field, label in _TABLE_COLUMNS]


def _type_name(str_type: int) -> str:
    """What the game keeps under LOC type `str_type`, in the UI language."""
    key = f"loc.types.{str_type}"
    name = ui_text(key)
    # ui_text() reads an unknown key as the key itself.
    return ui_text("loc.typeUnknown") if name == key else name


def _type_names(records: Sequence[_LocRecordMeta]) -> dict[int, str]:
    """`_type_name()` of every type in `records`, looked up once per type."""
    return {str_type: _type_name(str_type) for str_type in {meta[1] for meta in records}}


def _record_to_dict(data: bytes, meta: _LocRecordMeta, type_text: str) -> dict:
    _, str_type, str_id1, str_id2, str_id3, str_id4, text_start, text_end = meta
    text = data[text_start:text_end].decode("utf-16-le", errors="replace")
    return {
        "str_id1": str_id1,
        "str_id2": str_id2,
        "str_id3": str_id3,
        "str_id4": str_id4,
        "str_type": str_type,
        "str_type_text": type_text,
        "text": text,
    }


class _LocIndex:
    def __init__(self, raw: bytes) -> None:
        self.data = decompress_loc(raw)
        self.records: list[_LocRecordMeta] = []
        self.search_texts: list[str] | None = None
        # The UI language `search_texts` was built in; its type names follow it.
        self.search_language: str | None = None
        if self.data is None:
            return

        pos = 0
        while pos + 16 <= len(self.data):
            str_size = u32(self.data, pos)
            str_type = u32(self.data, pos + 4)
            str_id1  = u32(self.data, pos + 8)
            str_id2  = u16(self.data, pos + 12)
            str_id3  = u8(self.data, pos + 14)
            str_id4  = u8(self.data, pos + 15)
            text_start = pos + 16
            text_end = text_start + str_size * 2

            if text_end + 4 > len(self.data):
                break

            self.records.append((
                str_size,
                str_type,
                str_id1,
                str_id2,
                str_id3,
                str_id4,
                text_start,
                text_end,
            ))
            pos = text_end + 4

    def page(self, page: int, page_size: int) -> list[dict]:
        start = page * page_size
        end = min(start + page_size, len(self.records))
        return self.records_at(range(start, end))

    def records_at(self, indices: Sequence[int]) -> list[dict]:
        if self.data is None:
            return []
        metas = [self.records[index] for index in indices]
        names = _type_names(metas)
        return [_record_to_dict(self.data, meta, names[meta[1]]) for meta in metas]

    def sort_values(self, field: str) -> list[object]:
        """One raw value per record for `field`, read from the index without
        building record dicts."""
        position = _META_FIELD_POSITIONS.get(field)
        if position is not None:
            return [meta[position] for meta in self.records]
        if field == "str_type_text":
            names = _type_names(self.records)
            return [names[meta[1]] for meta in self.records]
        if field == "text" and self.data is not None:
            data = self.data
            return [
                data[meta[6]:meta[7]].decode("utf-16-le", errors="replace")
                for meta in self.records
            ]
        raise ValueError(f"LOC records cannot be sorted by {field!r}")

    def search(self, query: str, language: str) -> list[int]:
        if self.data is None:
            return []
        q = query.lower()
        if self.search_texts is None or self.search_language != language:
            names = _type_names(self.records)
            search_texts: list[str] = []
            for meta in self.records:
                _, str_type, str_id1, str_id2, str_id3, str_id4, text_start, text_end = meta
                text = self.data[text_start:text_end].decode("utf-16-le", errors="replace")
                type_text = names[str_type]
                search_texts.append(
                    f"{str_id1}\t{str_id2}\t{str_id3}\t{str_id4}\t{str_type}\t{type_text}\t{text}".lower()
                )
            self.search_texts = search_texts
            self.search_language = language
        return [index for index, text in enumerate(self.search_texts) if q in text]


class LocHandler(PreviewHandler):

    def _index(self, data: bytes) -> _LocIndex:
        return self._data_cache(data, "index", lambda: _LocIndex(data))

    def get_record_count(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> int:
        return len(self._index(data).records)

    def sortable_fields(self) -> tuple[str, ...]:
        return _COLUMN_FIELDS

    def _build_sort_order(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
        sort: TableSort,
    ) -> list[int]:
        return sort_order_by_values(self._index(data).sort_values(sort.field), sort.descending)

    def render_sorted_page(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
        page: int,
        page_size: int,
        sort: TableSort,
    ) -> str:
        # Decode only the rows on this page; the order itself is an index array.
        index = self._index(data)
        order = self.sorted_order(data, entry, companions, sort)
        start = page * page_size
        records = index.records_at(order[start:start + page_size])
        return self._render_page(records, page, page_size, len(index.records))

    def render_data_page(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
        page: int,
        page_size: int,
    ) -> str:
        index = self._index(data)
        return self._render_page(index.page(page, page_size), page, page_size, len(index.records))

    def search_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
        query: str,
    ) -> list[int]:
        return self._index(data).search(query, self.lang)

    def get_records(self, data: bytes, entry: PazEntry, companions: dict[str, bytes]) -> list[dict]:
        index = self._index(data)
        return index.records_at(range(len(index.records)))

    def render_records_page(self, records: list[dict], page: int, page_size: int) -> str:
        total = len(records)
        start = page * page_size
        end = min(start + page_size, total)
        return self._render_page(records[start:end], page, page_size, total)

    def _render_page(self, records: list[dict], page: int, page_size: int, total: int) -> str:
        start = page * page_size
        end   = min(start + page_size, total)
        rows_html = "".join(
            f"<tr>"
            f"<td>{_html.escape(str(r['str_id1']))}</td>"
            f"<td>{_html.escape(str(r['str_id2']))}</td>"
            f"<td>{r['str_id3']}</td>"
            f"<td>{r['str_id4']}</td>"
            f"<td class='loc-type'><span class='loc-type-num'>{r['str_type']}</span> "
            f"{_html.escape(r['str_type_text'])}</td>"
            f"<td class='loc-text'>{pa_html(r['text'])}</td>"
            f"</tr>"
            for r in records
        )
        count = ui_text("loc.showing", first=f"{start + 1:,}", last=f"{end:,}", total=f"{total:,}")
        header_cells = "".join(header_cell(column) for column in _columns())
        return f"""
<div class="loc-view">
  <div class="loc-header">
    <span class="loc-count">{_html.escape(count)}</span>
  </div>
  <table class="loc-table">
    <thead>
      <tr>{header_cells}</tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>
</div>
"""


register_handler(".loc", LocHandler())
