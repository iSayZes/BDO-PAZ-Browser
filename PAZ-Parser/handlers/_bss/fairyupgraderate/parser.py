from __future__ import annotations

from _common.binary import u8, u32


_MAGIC = b"PABR"
_HEADER_SIZE = 8
_TRAILER_SIZE = 12
_RECORD_HEADER_SIZE = 9
_ENTRY_SIZE = 16

# Offset of end_of_records inside the 12-byte file trailer.
_TRAILER_END_OFFSET = 4


def _records_end(data: bytes) -> int:
    """Byte offset where the record stream stops.

    The trailer stores this explicitly; fall back to the start of the trailer
    when the stored value is not usable.
    """
    fallback = max(_HEADER_SIZE, len(data) - _TRAILER_SIZE)

    if len(data) < _HEADER_SIZE + _TRAILER_SIZE:
        return fallback

    end = u32(data, len(data) - _TRAILER_SIZE + _TRAILER_END_OFFSET)
    if _HEADER_SIZE <= end <= fallback:
        return end

    return fallback


def parse_fairyupgraderate_records(data: bytes) -> list[dict]:
    """Parse fairy Sprouting rates into one flat row per (step, item) pair.

    Each record is one grade upgrade step and holds an entry per item type that
    can be used for it. Records are variable length, so `entry_count` drives the
    stride rather than a fixed record size.
    """
    if len(data) < _HEADER_SIZE or data[:4] != _MAGIC:
        raise ValueError("fairyupgraderate.bss has invalid magic.")

    count = u32(data, 4)
    end = _records_end(data)
    rows: list[dict] = []
    pos = _HEADER_SIZE

    for step in range(count):
        if pos + _RECORD_HEADER_SIZE > end:
            raise ValueError(
                f"fairyupgraderate.bss record {step} is truncated at 0x{pos:X}."
            )

        unknown_lead = u8(data, pos)
        success_cap_ppm = u32(data, pos + 0x01)
        entry_count = u32(data, pos + 0x05)
        pos += _RECORD_HEADER_SIZE

        if pos + entry_count * _ENTRY_SIZE > end:
            raise ValueError(
                f"fairyupgraderate.bss record {step} declares {entry_count} "
                f"entries but only {end - pos} bytes remain."
            )

        for _ in range(entry_count):
            rate_ppm = u32(data, pos + 0x04)
            rows.append({
                "step": step,
                "unknown_lead": unknown_lead,
                "success_cap_ppm": success_cap_ppm,
                "item_id": u32(data, pos),
                "rate_ppm": rate_ppm,
                "items_for_max": u32(data, pos + 0x08),
                "reserved": u32(data, pos + 0x0C),
                "chance_pct": _chance_pct(rate_ppm, success_cap_ppm),
            })
            pos += _ENTRY_SIZE

    return rows


def _chance_pct(rate_ppm: int, success_cap_ppm: int) -> float:
    """Success chance contributed by a single item, as a percentage."""
    if success_cap_ppm <= 0:
        return 0.0

    return rate_ppm / success_cap_ppm * 100.0
