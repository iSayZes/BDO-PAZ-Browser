"""`weburl.bss`: the web addresses of the game client, with the points where it fills in values.

    PABR | url first_url | url[while url_ref != 0] urls | u32 unknown_after_urls
    | u32 string_count | strings | u32 table_start | u32 0
    url: u32 url_ref | u32 insert_count | insert_count x (u32 insert_offset | u8 insert_type)

The list has no count. String 0 is the first URL's text (the string table is
in first-use order), so the URLs after the first run up to the `url_ref` of
`0` that `unknown_after_urls` holds, 4 bytes before the string table.

Layout 2 in docs/file-formats/weburl_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_structs
from _common.pabr_strings import checked_string_table_start, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "weburl.bss"

# The first URL follows the PABR magic.
_URLS_START = 0x04
_U32 = struct.Struct("<I")
_INSERT = struct.Struct("<IB")
_INSERT_FIELDS = ("insert_offset", "insert_type")
# The `url_ref` that ends the list; only the first URL reads string 0.
_END_URL_REF = 0
# How the URL text shows an insert point: `<insert_type>`, as the doc writes it.
_INSERT_MARK = "<{}>"


def url_template(url: str, inserts: list[dict]) -> str:
    """The URL text with `<insert_type>` at each insert point, in offset order."""
    parts: list[str] = []
    start = 0
    for insert in inserts:
        offset = insert["insert_offset"]
        parts.append(url[start:offset])
        parts.append(_INSERT_MARK.format(insert["insert_type"]))
        start = offset
    parts.append(url[start:])
    return "".join(parts)


def _read_url(reader: RecordReader, strings: list[str], position: int) -> dict:
    (url_ref,) = reader.unpack(_U32)
    inserts = read_counted_structs(reader, _INSERT, _INSERT_FIELDS, f"URL {position} insert list")
    url = string_at(strings, url_ref)
    offsets = [insert["insert_offset"] for insert in inserts]
    if offsets != sorted(offsets) or any(offset > len(url) for offset in offsets):
        raise ValueError(f"URL {position} insert offsets {offsets} do not fit its {len(url)}-character text")
    return {
        "position": position,
        "url_ref": url_ref,
        "url": url,
        "insert_count": len(inserts),
        "inserts": inserts,
        "url_template": url_template(url, inserts),
    }


def _next_url_ref(data: bytes, reader: RecordReader) -> int:
    if reader.remaining() < _U32.size:
        raise ValueError(f"{FILE_NAME} URLs run into the string table at 0x{reader.pos:X}")
    return _U32.unpack_from(data, reader.pos)[0]


def parse_weburl_records(data: bytes) -> list[dict]:
    """One record per URL, in file order, each with `unknown_after_urls`.

    Raises ValueError on a bad PABR magic or trailer, an insert list that runs
    past the string table, insert offsets outside their URL, or URLs that do
    not end 4 bytes before the string table.
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, _URLS_START, table_start, FILE_NAME)
    records = [_read_url(reader, strings, 0)]
    while _next_url_ref(data, reader) != _END_URL_REF:
        records.append(_read_url(reader, strings, len(records)))
    (unknown_after_urls,) = reader.unpack(_U32)
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} URLs end at 0x{reader.pos:X}, but the string table starts at 0x{table_start:X}")
    return [{**record, "unknown_after_urls": unknown_after_urls} for record in records]
