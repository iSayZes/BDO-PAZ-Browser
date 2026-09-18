from __future__ import annotations

from _common.binary import u8, u16, u32


_MAGIC = b"PABR"
_HEADER_SIZE = 8
_TRAILER_SIZE = 12
_RECORD_HEADER_SIZE = 4
_ENTRY_SIZE = 11

# Offset of end_of_records inside the 12-byte file trailer.
_TRAILER_END_OFFSET = 4


def _records_end(data: bytes) -> int:
    """Byte offset where the record stream stops, taken from the trailer."""
    fallback = max(_HEADER_SIZE, len(data) - _TRAILER_SIZE)

    if len(data) < _HEADER_SIZE + _TRAILER_SIZE:
        return fallback

    end = u32(data, len(data) - _TRAILER_SIZE + _TRAILER_END_OFFSET)
    if _HEADER_SIZE <= end <= fallback:
        return end

    return fallback


def parse_fairyfeedenchantfailcount_records(data: bytes) -> list[dict]:
    """Parse the table into one flat row per entry.

    Records are variable length and framed by `entry_count`, so the stride comes
    from that field rather than a fixed record size. Entries are unaligned: the
    two u32 values start at odd offsets inside the 11-byte entry.
    """
    if len(data) < _HEADER_SIZE or data[:4] != _MAGIC:
        raise ValueError("fairyfeedenchantfailcount.bss has invalid magic.")

    count = u32(data, 4)
    end = _records_end(data)
    rows: list[dict] = []
    pos = _HEADER_SIZE

    for index in range(count):
        if pos + _RECORD_HEADER_SIZE > end:
            raise ValueError(
                f"fairyfeedenchantfailcount.bss record {index} is truncated "
                f"at 0x{pos:X}."
            )

        entry_count = u32(data, pos)
        pos += _RECORD_HEADER_SIZE

        if pos + entry_count * _ENTRY_SIZE > end:
            raise ValueError(
                f"fairyfeedenchantfailcount.bss record {index} declares "
                f"{entry_count} entries but only {end - pos} bytes remain."
            )

        for _ in range(entry_count):
            rows.append({
                "record": index,
                "group_id": u16(data, pos),
                "sub_key": u8(data, pos + 0x02),
                "value_a": u32(data, pos + 0x03),
                "value_b": u32(data, pos + 0x07),
            })
            pos += _ENTRY_SIZE

    return rows
