from __future__ import annotations

from _common.binary import u16, u32


_MAGIC = b"PABR"
_HEADER_SIZE = 8
_RECORD_SIZE = 12
_TRAILER_SIZE = 12


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
            "unknown_a": u16(data, pos + 0x04),
            "unknown_b": u16(data, pos + 0x06),
            "unknown_c": u16(data, pos + 0x08),
            "unknown_d": u16(data, pos + 0x0A),
        })

    return records
