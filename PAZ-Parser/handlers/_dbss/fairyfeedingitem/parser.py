from __future__ import annotations

from _common.binary import u32, u64


_HEADER_SIZE = 4
_RECORD_SIZE = 28
_OFFSET_ROW_SIZE = 12

# The offset companion addresses the payload that follows the record's key.
_KEY_PREFIX_SIZE = 4

# Struct padding between the u32 item ID and the u64 EXP: the client 1784
# server never writes it, so the bytes are whatever the builder's stack held.
_PADDING_08_SIZE = 4


def _row_count(data: bytes, filename: str, row_size: int) -> int:
    if len(data) < _HEADER_SIZE:
        raise ValueError(f"{filename} is truncated: missing record count.")

    count = u32(data, 0)
    available = (len(data) - _HEADER_SIZE) // row_size

    # Trust whichever is smaller so a short or padded file cannot over-read.
    return min(count, available)


def parse_fairyfeedingitem_records(data: bytes) -> list[dict]:
    """Parse the fairy feeding items: item ID and the fairy EXP one item grants."""
    count = _row_count(data, "fairyfeedingitem.dbss", _RECORD_SIZE)

    records: list[dict] = []
    for index in range(count):
        pos = _HEADER_SIZE + index * _RECORD_SIZE
        records.append({
            "key": u32(data, pos),
            "item_id": u32(data, pos + 0x04),
            "padding_08": data[pos + 0x08 : pos + 0x08 + _PADDING_08_SIZE].hex(),
            "exp": u64(data, pos + 0x0C),
            "unknown_14": u64(data, pos + 0x14),
        })

    return records


def parse_fairyfeedingitemoffset_records(data: bytes) -> list[dict]:
    """Parse the item-keyed index into fairyfeedingitem.dbss."""
    count = _row_count(data, "fairyfeedingitemoffset.dbss", _OFFSET_ROW_SIZE)

    records: list[dict] = []
    for index in range(count):
        pos = _HEADER_SIZE + index * _OFFSET_ROW_SIZE
        data_offset = u32(data, pos + 0x04)
        records.append({
            "item_id": u32(data, pos),
            "data_offset": data_offset,
            "data_size": u32(data, pos + 0x08),
            "record_start": data_offset - _KEY_PREFIX_SIZE,
        })

    return records
