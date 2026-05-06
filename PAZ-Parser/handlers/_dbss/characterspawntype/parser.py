from __future__ import annotations

import struct

_RECORD_SIZE = 48
_NUM_FLAGS = 44

_OFFSET_MAGIC = b"PABR"
_OFFSET_HEADER_SIZE = 8
_OFFSET_RECORD_SIZE = 10  # u16 + u32 + u32


def parse_characterspawntype_records(data: bytes) -> list[dict]:
    if len(data) < 4:
        return []
    (count,) = struct.unpack_from("<I", data, 0)
    records: list[dict] = []
    for i in range(count):
        pos = 4 + i * _RECORD_SIZE
        if pos + _RECORD_SIZE > len(data):
            break
        (entity_id,) = struct.unpack_from("<I", data, pos)
        flags = list(data[pos + 4 : pos + 4 + _NUM_FLAGS])
        records.append({"entity_id": entity_id, "flags": flags})
    return records


def parse_characterspawntypeoffset_records(data: bytes) -> list[dict]:
    if len(data) < _OFFSET_HEADER_SIZE or data[:4] != _OFFSET_MAGIC:
        return []
    (count,) = struct.unpack_from("<I", data, 4)
    records: list[dict] = []
    for i in range(count):
        pos = _OFFSET_HEADER_SIZE + i * _OFFSET_RECORD_SIZE
        if pos + _OFFSET_RECORD_SIZE > len(data):
            break
        id_low16, byte_offset, size = struct.unpack_from("<HII", data, pos)
        records.append({"id_low16": id_low16, "offset": byte_offset, "size": size})
    return records
