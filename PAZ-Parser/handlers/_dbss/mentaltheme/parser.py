from __future__ import annotations

import struct

from _common.loc import loc_lookup, strip_pa_tags
from .model import MentalThemeOffsetRecord, MentalThemeRecord

_OFFSET_RECORD_SIZE = 10
_STATS_SIZE = 23


def _u8(data: bytes, offset: int) -> int:
    if offset < 0 or offset + 1 > len(data):
        return 0
    return data[offset]


def _u16(data: bytes, offset: int) -> int:
    if offset < 0 or offset + 2 > len(data):
        return 0
    return struct.unpack_from("<H", data, offset)[0]


def _u32(data: bytes, offset: int) -> int:
    if offset < 0 or offset + 4 > len(data):
        return 0
    return struct.unpack_from("<I", data, offset)[0]


def _decode_utf16le(data: bytes, offset: int, code_units: int) -> str:
    byte_len = code_units * 2
    if code_units < 0 or offset < 0 or offset + byte_len > len(data):
        return ""
    return data[offset:offset + byte_len].decode("utf-16-le", errors="replace")


def _lookup_clean(str_type: int, str_id1: int) -> str:
    return strip_pa_tags(loc_lookup(str_type, str_id1))


def parse_mentalthemeoffset_records(data: bytes) -> list[MentalThemeOffsetRecord]:
    records: list[MentalThemeOffsetRecord] = []

    if len(data) < 4:
        return records

    count = _u32(data, 0)
    expected_size = 4 + count * _OFFSET_RECORD_SIZE

    if len(data) < expected_size:
        count = (len(data) - 4) // _OFFSET_RECORD_SIZE

    for index in range(count):
        base = 4 + index * _OFFSET_RECORD_SIZE
        records.append(MentalThemeOffsetRecord(
            row=index,
            theme_id=_u16(data, base),
            payload_offset=_u32(data, base + 0x02),
            payload_size=_u32(data, base + 0x06),
        ))

    return records


def parse_mentaltheme_records(
    dbss_data: bytes,
    offset_data: bytes,
) -> list[MentalThemeRecord]:
    records: list[MentalThemeRecord] = []

    for offset_record in parse_mentalthemeoffset_records(offset_data):
        payload_offset = offset_record["payload_offset"]
        payload_size = offset_record["payload_size"]

        if payload_offset < 0 or payload_offset + 0x0A > len(dbss_data):
            continue

        theme_id = _u16(dbss_data, payload_offset)
        name_len = _u16(dbss_data, payload_offset + 0x02)
        name_offset = payload_offset + 0x0A
        name_ko = _decode_utf16le(dbss_data, name_offset, name_len)

        stats_offset = name_offset + name_len * 2
        if stats_offset + _STATS_SIZE > len(dbss_data):
            continue

        entry_count = _u32(dbss_data, stats_offset + 0x13)
        entries_offset = stats_offset + _STATS_SIZE
        entries_end = entries_offset + entry_count * 4
        if entries_end + 4 > len(dbss_data):
            continue

        entry_ids = [
            _u32(dbss_data, entries_offset + index * 4)
            for index in range(entry_count)
        ]

        child_count = _u32(dbss_data, entries_end)
        children_offset = entries_end + 4
        children_end = children_offset + child_count * 2
        if children_end + 4 > len(dbss_data):
            continue

        child_ids = [
            _u16(dbss_data, children_offset + index * 2)
            for index in range(child_count)
        ]

        parent_id = _u16(dbss_data, stats_offset)
        theme_name = _lookup_clean(9, theme_id)
        parent_name = _lookup_clean(9, parent_id) if parent_id else ""
        entry_names = [
            name
            for name in (_lookup_clean(34, entry_id) for entry_id in entry_ids)
            if name
        ]

        records.append(MentalThemeRecord(
            row=offset_record["row"],
            theme_id=theme_id,
            offset_theme_id=offset_record["theme_id"],
            payload_offset=payload_offset,
            payload_size=payload_size,
            name_ko=name_ko,
            name=theme_name or name_ko,
            parent_id=parent_id,
            parent_name=parent_name,
            increase_wp=_u16(dbss_data, stats_offset + 0x02),
            need_count=_u32(dbss_data, stats_offset + 0x04),
            increase_wp_2=_u16(dbss_data, stats_offset + 0x08),
            need_count_2=_u32(dbss_data, stats_offset + 0x0A),
            unknown_flag=_u8(dbss_data, stats_offset + 0x0E),
            unknown_value=_u32(dbss_data, stats_offset + 0x0F),
            entry_count=entry_count,
            entry_ids=", ".join(str(entry_id) for entry_id in entry_ids),
            entry_names=" | ".join(entry_names),
            child_count=child_count,
            child_ids=", ".join(str(child_id) for child_id in child_ids),
            terminator=_u32(dbss_data, children_end),
        ))

    return records
