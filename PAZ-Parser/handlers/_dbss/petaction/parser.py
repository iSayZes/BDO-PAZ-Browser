from __future__ import annotations

import struct
from pathlib import PureWindowsPath

from _common.pabr_offset import parse_bare_u32_offset_rows
from _common.record_reader import RecordReader


_HEADER = struct.Struct("<IIII")
_TRAILER_SIZE = 12
_MAGIC = 0xDEBA1DCD


def parse_petactionoffset_records(data: bytes) -> list[dict]:
    return [
        {"action_id": row.entry_id, "record_offset": row.offset, "record_size": row.size}
        for row in parse_bare_u32_offset_rows(data)
    ]


def _derive_action_name(icon_path: str) -> str:
    stem = PureWindowsPath(icon_path.replace("/", "\\")).stem
    parts = stem.split("_")
    if len(parts) >= 3 and parts[0].lower() == "action":
        return parts[-1]
    return stem


def _parse_petaction_payload(row: int, offset_record: dict, block: bytes) -> dict:
    reader = RecordReader(block, 0, len(block), f"pet action record {row}")
    action_id, unknown_04, unknown_08, magic = reader.unpack(_HEADER)
    if magic != _MAGIC:
        raise ValueError(f"pet action record {row} has unexpected magic 0x{magic:08X}")

    # Two u64-length UTF-16 strings follow: the Korean action name, then the icon path.
    name_kr = reader.text(wide=True)
    icon_path = reader.text(wide=True)
    if reader.remaining() != _TRAILER_SIZE:
        raise ValueError(
            f"pet action record {row} has {reader.remaining()} bytes after the icon path, expected {_TRAILER_SIZE}"
        )
    trailer = block[reader.pos:]

    return {
        "row": row,
        "action_id": action_id,
        "action_name": _derive_action_name(icon_path),
        "name_kr": name_kr,
        "icon_path": icon_path,
        "magic": magic,
        "magic_hex": f"0x{magic:08X}",
        "record_offset": offset_record["record_offset"],
        "record_size": offset_record["record_size"],
        "unknown_04": unknown_04,
        "unknown_08": unknown_08,
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
