from __future__ import annotations

import struct

from _common.binary import u32


_MAGIC = b"PABR"
_HEADER_SIZE = 8
_RECORD_SIZE = 12
_TRAILER_SIZE = 12


def _parse_town_fields(data: bytes, pos: int) -> dict:
    """The four fields after the node; names follow the PlantTown_Table sheet (see the doc)."""
    warehouse, worker_capacity, max_level, upgrade_resource = struct.unpack_from("<HHhH", data, pos)
    return {
        "warehouse_upgrade_group_index": warehouse,
        "worker_capacity_upgrade_group_index": worker_capacity,
        "max_level": max_level,
        "upgrade_resource_key": upgrade_resource,
    }


def parse_planttown_records(data: bytes) -> list[dict]:
    if len(data) < _HEADER_SIZE:
        return []

    if data[:4] != _MAGIC:
        raise ValueError("planttown.bss has invalid magic.")

    count = u32(data, 4)
    records_end = _HEADER_SIZE + count * _RECORD_SIZE
    if records_end + _TRAILER_SIZE > len(data):
        count = max(0, (len(data) - _HEADER_SIZE - _TRAILER_SIZE) // _RECORD_SIZE)

    records: list[dict] = []
    for slot in range(count):
        pos = _HEADER_SIZE + slot * _RECORD_SIZE
        records.append({
            "slot": slot,
            "node_id": u32(data, pos),
            **_parse_town_fields(data, pos + 0x04),
        })

    return records
