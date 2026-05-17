from __future__ import annotations

import struct


_HEADER_SIZE = 4
_OFFSET_RECORD_SIZE = 10
_KEY_PREFIX_SIZE = 2
_RECORD_SIZE = 176
_DATA_SIZE = _RECORD_SIZE - _KEY_PREFIX_SIZE
_RESERVED_OFFSET = 4
_COST_TABLE_OFFSET = 8
_COST_ENTRY_SIZE = 12
_COST_ENTRY_COUNT = 14


def parse_petequipskillaquireoffset_records(data: bytes) -> list[dict]:
    if len(data) < _HEADER_SIZE:
        return []

    (count,) = struct.unpack_from("<I", data, 0)
    records: list[dict] = []

    for index in range(count):
        pos = _HEADER_SIZE + index * _OFFSET_RECORD_SIZE
        if pos + _OFFSET_RECORD_SIZE > len(data):
            break

        acquire_type_id, data_offset, data_size, padding = struct.unpack_from(
            "<HIHH", data, pos
        )
        records.append({
            "source_index": index,
            "acquire_type_id": acquire_type_id,
            "data_offset": data_offset,
            "data_size": data_size,
            "record_start": data_offset - _KEY_PREFIX_SIZE,
            "padding": padding,
        })

    return records


def _parse_cost_entries(data: bytes, record_start: int) -> list[dict]:
    entries: list[dict] = []

    for index in range(_COST_ENTRY_COUNT):
        pos = record_start + _COST_TABLE_OFFSET + index * _COST_ENTRY_SIZE
        cost_a, cost_b, cost_c = struct.unpack_from("<III", data, pos)
        entries.append({
            "index": index,
            "cost_a": cost_a,
            "cost_b": cost_b,
            "cost_c": cost_c,
        })

    return entries


def _group(acquire_type_id: int) -> int:
    return acquire_type_id // 100


def _tier(acquire_type_id: int) -> int:
    return acquire_type_id % 100


def parse_petequipskillaquire_records(data: bytes, offset_data: bytes) -> list[dict]:
    if len(data) < _HEADER_SIZE:
        return []

    (count,) = struct.unpack_from("<I", data, 0)
    offsets = parse_petequipskillaquireoffset_records(offset_data)
    if len(offsets) != count:
        raise ValueError(
            "petequipskillaquire count mismatch: "
            f"main has {count}, offset has {len(offsets)}"
        )

    records: list[dict] = []
    for offset_record in offsets:
        source_index = offset_record["source_index"]
        acquire_type_id = offset_record["acquire_type_id"]
        data_offset = offset_record["data_offset"]
        data_size = offset_record["data_size"]
        record_start = offset_record["record_start"]

        if data_size != _DATA_SIZE:
            raise ValueError(
                f"petequipskillaquire record {source_index} has unexpected size {data_size}"
            )
        if record_start < _HEADER_SIZE or data_offset + data_size > len(data):
            raise ValueError(
                f"petequipskillaquire record {source_index} exceeds file size"
            )

        key_prefix = struct.unpack_from("<H", data, record_start)[0]
        payload_key = struct.unpack_from("<H", data, data_offset)[0]
        packed_key = struct.unpack_from("<I", data, record_start)[0]
        reserved = struct.unpack_from("<I", data, record_start + _RESERVED_OFFSET)[0]
        cost_entries = _parse_cost_entries(data, record_start)
        active_entries = [
            entry for entry in cost_entries
            if entry["cost_a"] or entry["cost_b"] or entry["cost_c"]
        ]
        max_cost = max(
            max(entry["cost_a"], entry["cost_b"], entry["cost_c"])
            for entry in cost_entries
        )

        records.append({
            "source_index": source_index,
            "acquire_type_id": acquire_type_id,
            "group": _group(acquire_type_id),
            "tier": _tier(acquire_type_id),
            "key_prefix": key_prefix,
            "payload_key": payload_key,
            "packed_key": packed_key,
            "key_match": key_prefix == payload_key == acquire_type_id,
            "reserved": reserved,
            "active_entry_count": len(active_entries),
            "max_cost": max_cost,
            "sub0_cost_a": cost_entries[0]["cost_a"],
            "sub0_cost_b": cost_entries[0]["cost_b"],
            "sub0_cost_c": cost_entries[0]["cost_c"],
            "cost_entries": cost_entries,
            "cost_table": "; ".join(
                f"{entry['index']}=({entry['cost_a']}, {entry['cost_b']}, {entry['cost_c']})"
                for entry in active_entries
            ),
            "data_offset": data_offset,
            "data_size": data_size,
            "record_start": record_start,
        })

    return records
