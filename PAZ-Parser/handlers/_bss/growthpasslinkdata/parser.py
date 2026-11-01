"""`growthpasslinkdata.bss`: the guide links of each Growth Pass quest (`GrowthPass_Link`).

    PABR | u32 record_count | record_count x record | string table
    | u32 string_table_start | u32 0

    record: u16 quest_chain_id | u16 quest_id | u32 entry_count | entry_count x entry
    entry:  u8 service_resource_type | u32 link_count | link_count x link
    link:   u32 link_ref | u32 author_ref

`link_ref` and `author_ref` index the string table. The quest key is a quest
cell of `uigrowthpasslayout.bss`. Full layout in
docs/file-formats/bss/growthpasslinkdata_bss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Sequence
from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_strings import (
    HEADER_SIZE,
    check_rows_end,
    checked_string_table_start,
    read_string_table,
)
from _common.record_reader import RecordReader

FILE_NAME = "growthpasslinkdata.bss"

_RECORD_HEAD = struct.Struct("<HHI")
_ENTRY_HEAD = struct.Struct("<BI")
_LINK = struct.Struct("<II")


@dataclass(frozen=True)
class GuideLink:
    link: str
    author: str


@dataclass(frozen=True)
class LinkEntry:
    service_resource_type: int
    links: tuple[GuideLink, ...]


@dataclass(frozen=True)
class QuestLinks:
    quest_chain_id: int
    quest_id: int
    entries: tuple[LinkEntry, ...]


def parse_growthpasslinkdata(data: bytes) -> list[QuestLinks]:
    """Every quest's links in file order, the string references resolved to text.

    Raises ValueError on a bad magic, a record that runs into the string
    table, records that do not end where the string table starts, or a
    string reference outside the table.
    """
    table_start = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE, table_start, f"{FILE_NAME} records")
    records = [_read_record(reader, strings) for _ in range(u32(data, 4))]
    check_rows_end(data, reader.pos, f"{FILE_NAME} records")
    return records


def quest_link_addresses(data: bytes) -> dict[tuple[int, int], tuple[str, ...]]:
    """(quest chain, quest ID) -> its link addresses over every service type, each once, in file order."""
    addresses: dict[tuple[int, int], tuple[str, ...]] = {}
    for record in parse_growthpasslinkdata(data):
        links = [link.link for entry in record.entries for link in entry.links]
        addresses[(record.quest_chain_id, record.quest_id)] = tuple(dict.fromkeys(links))
    return addresses


def _read_record(reader: RecordReader, strings: Sequence[str]) -> QuestLinks:
    quest_chain_id, quest_id, entry_count = reader.unpack(_RECORD_HEAD)
    entries = tuple(_read_entry(reader, strings) for _ in range(entry_count))
    return QuestLinks(quest_chain_id, quest_id, entries)


def _read_entry(reader: RecordReader, strings: Sequence[str]) -> LinkEntry:
    service_resource_type, link_count = reader.unpack(_ENTRY_HEAD)
    links = tuple(_read_link(reader, strings) for _ in range(link_count))
    return LinkEntry(service_resource_type, links)


def _read_link(reader: RecordReader, strings: Sequence[str]) -> GuideLink:
    link_ref, author_ref = reader.unpack(_LINK)
    return GuideLink(_string(strings, link_ref), _string(strings, author_ref))


def _string(strings: Sequence[str], index: int) -> str:
    if not 0 <= index < len(strings):
        raise ValueError(f"string reference {index} is outside the {len(strings)}-entry string table")
    return strings[index]
