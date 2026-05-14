from __future__ import annotations

import struct
from pathlib import PureWindowsPath


_OFFSET_HEADER_SIZE = 4
_OFFSET_RECORD_SIZE = 12
_BASE_HEADER_SIZE = 0x24
_EXTENDED_HEADER_SIZE = 0x28
_TRAILER_SIZE = 12
_MAGIC = 0xDEBA1DCD


def parse_petactionoffset_records(data: bytes) -> list[dict]:
    if len(data) < _OFFSET_HEADER_SIZE:
        return []

    (count,) = struct.unpack_from("<I", data, 0)
    records: list[dict] = []

    for index in range(count):
        pos = _OFFSET_HEADER_SIZE + index * _OFFSET_RECORD_SIZE
        if pos + _OFFSET_RECORD_SIZE > len(data):
            break

        action_id, record_offset, record_size = struct.unpack_from("<III", data, pos)
        records.append({
            "action_id": action_id,
            "record_offset": record_offset,
            "record_size": record_size,
        })

    return records


def _read_utf16le_path(block: bytes, path_start: int, path_len: int) -> str:
    path_end = path_start + path_len * 2
    if path_end > len(block):
        raise ValueError("pet action icon path exceeds record size")

    return block[path_start:path_end].decode("utf-16-le", errors="replace")


def _derive_action_name(icon_path: str) -> str:
    stem = PureWindowsPath(icon_path.replace("/", "\\")).stem
    parts = stem.split("_")
    if len(parts) >= 3 and parts[0].lower() == "action":
        return parts[-1]
    return stem


def _parse_petaction_payload(row: int, offset_record: dict, block: bytes) -> dict:
    if len(block) < _BASE_HEADER_SIZE + _TRAILER_SIZE:
        raise ValueError(f"pet action record {row} is too small")

    action_id = struct.unpack_from("<I", block, 0x00)[0]
    reserved_04 = struct.unpack_from("<I", block, 0x04)[0]
    reserved_08 = struct.unpack_from("<I", block, 0x08)[0]
    magic = struct.unpack_from("<I", block, 0x0C)[0]
    action_group = struct.unpack_from("<I", block, 0x10)[0]
    reserved_14 = struct.unpack_from("<I", block, 0x14)[0]

    if magic != _MAGIC:
        raise ValueError(f"pet action record {row} has unexpected magic 0x{magic:08X}")

    hash_values = [struct.unpack_from("<I", block, 0x18)[0]]
    path_len_offset = 0x1C
    reserved_path_offset = 0x20
    path_start = _BASE_HEADER_SIZE

    if action_group == 4:
        if len(block) < _EXTENDED_HEADER_SIZE + _TRAILER_SIZE:
            raise ValueError(f"pet action record {row} extended header is too small")
        hash_values.append(struct.unpack_from("<I", block, 0x1C)[0])
        path_len_offset = 0x20
        reserved_path_offset = 0x24
        path_start = _EXTENDED_HEADER_SIZE

    icon_path_len = struct.unpack_from("<I", block, path_len_offset)[0]
    reserved_path = struct.unpack_from("<I", block, reserved_path_offset)[0]
    icon_path = _read_utf16le_path(block, path_start, icon_path_len)
    path_end = path_start + icon_path_len * 2
    trailer = block[path_end:path_end + _TRAILER_SIZE]
    if len(trailer) < _TRAILER_SIZE:
        raise ValueError(f"pet action record {row} trailer exceeds record size")

    return {
        "row": row,
        "action_id": action_id,
        "action_name": _derive_action_name(icon_path),
        "action_group": action_group,
        "icon_path": icon_path,
        "icon_path_len": icon_path_len,
        "icon_hash": hash_values[0],
        "icon_hash_hex": f"0x{hash_values[0]:08X}",
        "icon_hashes": hash_values,
        "icon_hashes_hex": ", ".join(f"0x{value:08X}" for value in hash_values),
        "magic": magic,
        "magic_hex": f"0x{magic:08X}",
        "record_offset": offset_record["record_offset"],
        "record_size": offset_record["record_size"],
        "reserved_04": reserved_04,
        "reserved_08": reserved_08,
        "reserved_14": reserved_14,
        "reserved_path": reserved_path,
        "trailing_zeroes": trailer == b"\x00" * _TRAILER_SIZE,
        "action_id_match": action_id == offset_record["action_id"],
    }


def parse_petaction_records(data: bytes, offset_data: bytes) -> list[dict]:
    records: list[dict] = []

    for row, offset_record in enumerate(parse_petactionoffset_records(offset_data)):
        start = offset_record["record_offset"]
        size = offset_record["record_size"]
        if start + size > len(data):
            raise ValueError(f"pet action record {row} exceeds file size")

        block = data[start:start + size]
        records.append(_parse_petaction_payload(row, offset_record, block))

    return sorted(records, key=lambda record: record["action_id"])
