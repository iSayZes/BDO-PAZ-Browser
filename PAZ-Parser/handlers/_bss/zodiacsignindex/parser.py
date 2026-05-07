from __future__ import annotations

from _common.binary import u32 as _u32
from .model import ZodiacSignIndexRecord


def parse_zodiacsignindex_records(data: bytes) -> list[ZodiacSignIndexRecord]:
    if len(data) < 8:
        return []

    if data[:4] != b"PABR":
        raise ValueError("zodiacsignindex.bss has invalid magic.")

    count = _u32(data, 4)
    entries_start = 8
    entries_end = entries_start + count
    trailer_end = entries_end + 12
    if trailer_end > len(data):
        count = max(0, len(data) - entries_start - 12)
        entries_end = entries_start + count

    records: list[ZodiacSignIndexRecord] = []
    for slot, zodiac_id in enumerate(data[entries_start:entries_end]):
        records.append({"slot": slot, "zodiac_id": zodiac_id})

    return records
