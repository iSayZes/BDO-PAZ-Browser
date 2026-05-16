from __future__ import annotations

from _common.binary import u16, u32


_MAGIC = b"PABR"
_HEADER_SIZE = 8
_RECORD_START = 8
_RECORD_SIZE = 0x390
_ICON_COUNT_SIZE = 4


def _read_icon_paths(data: bytes, offset: int) -> list[str]:
    if offset + _ICON_COUNT_SIZE > len(data):
        return []

    count = u32(data, offset)
    pos = offset + _ICON_COUNT_SIZE
    paths: list[str] = []

    for _ in range(count):
        if pos + 4 > len(data):
            break

        size = u32(data, pos)
        if (size == 0 or pos + 4 + size > len(data)) and data[pos] == 0:
            pos += 1
            size = u32(data, pos)
        pos += 4
        end = pos + size
        if end > len(data):
            break

        raw = data[pos:end]
        pos = end
        paths.append(raw.rstrip(b"\x00").decode("utf-8", errors="replace"))

    return paths


def parse_plantworker_records(data: bytes) -> list[dict]:
    if len(data) < _HEADER_SIZE:
        return []

    if data[:4] != _MAGIC:
        raise ValueError("plantworker.bss has invalid magic.")

    count = u32(data, 4)
    records_end = _RECORD_START + count * _RECORD_SIZE
    if records_end > len(data):
        count = max(0, (len(data) - _RECORD_START) // _RECORD_SIZE)
        records_end = _RECORD_START + count * _RECORD_SIZE

    icon_paths = _read_icon_paths(data, records_end)

    records: list[dict] = []
    for slot in range(count):
        pos = _RECORD_START + slot * _RECORD_SIZE
        icon_index = u32(data, pos + 0x1B)
        icon_path = icon_paths[icon_index] if icon_index < len(icon_paths) else ""

        records.append({
            "slot": slot,
            "worker_id": u16(data, pos),
            "next_worker_id": u16(data, pos + 0x02),
            "unknown_loc_a": u32(data, pos + 0x06),
            "unknown_loc_b": u32(data, pos + 0x0A),
            "move_speed": u32(data, pos + 0x0E),
            "stamina": u32(data, pos + 0x12),
            "luck": u32(data, pos + 0x16),
            "icon_index": icon_index,
            "icon_path": icon_path,
            "base_work_speed": u32(data, pos + 0x16F),
        })

    return records
