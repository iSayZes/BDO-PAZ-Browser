from __future__ import annotations

import re
import struct

_OFFSET_MAGIC = b"PABR"
_OFFSET_HEADER_SIZE = 8
_OFFSET_RECORD_SIZE = 10  # u16 + u32 + u32

_PAYLOAD_PREFIX_SIZE = 16  # 4 × u32 before the script string
_POST_STRING_PADDING = 8   # zero bytes after the null terminator

_GETKNOWLEDGE_RE = re.compile(r"getknowledge\((\d+)\)")


def parse_characterstaticoffset_records(data: bytes) -> list[dict]:
    if len(data) < _OFFSET_HEADER_SIZE or data[:4] != _OFFSET_MAGIC:
        return []
    (count,) = struct.unpack_from("<I", data, 4)
    records: list[dict] = []
    for i in range(count):
        pos = _OFFSET_HEADER_SIZE + i * _OFFSET_RECORD_SIZE
        if pos + _OFFSET_RECORD_SIZE > len(data):
            break
        id_low16, data_offset, payload_size = struct.unpack_from("<HII", data, pos)
        records.append({"id_low16": id_low16, "offset": data_offset, "size": payload_size})
    return records


def _read_utf16be_z(data: bytes, pos: int) -> tuple[str, int]:
    """Read a null-terminated UTF-16BE string from `data` at `pos`.

    Returns (decoded_text, position_after_null_terminator).
    """
    end = len(data)
    char_bytes: list[bytes] = []
    while pos + 1 < end:
        hi = data[pos]
        lo = data[pos + 1]
        pos += 2
        if hi == 0 and lo == 0:
            break
        char_bytes.append(bytes([hi, lo]))
    return b"".join(char_bytes).decode("utf-16-be", errors="replace"), pos


def parse_characterstatic_records(
    main_data: bytes,
    offset_records: list[dict],
) -> list[dict]:
    records: list[dict] = []
    for row in offset_records:
        data_offset: int = row["offset"]
        payload_size: int = row["size"]
        char_id: int = row["id_low16"]

        payload_end = data_offset + payload_size
        if data_offset < 4 or payload_end > len(main_data):
            continue

        payload = main_data[data_offset:payload_end]
        if len(payload) < _PAYLOAD_PREFIX_SIZE:
            continue

        # Parse the script string (UTF-16BE, null-terminated, starting at +0x10)
        script, str_end = _read_utf16be_z(payload, _PAYLOAD_PREFIX_SIZE)

        # Skip 8 padding bytes after the null terminator
        num_block_start = str_end + _POST_STRING_PADDING

        unknown_type = 0
        if num_block_start + 8 <= len(payload):
            # numeric_block: +0x00 = char_id again, +0x04 = unknown_type
            unknown_type = struct.unpack_from("<I", payload, num_block_start + 4)[0]

        m = _GETKNOWLEDGE_RE.search(script)
        knowledge_id: int | None = int(m.group(1)) if m else None

        records.append(
            {
                "character_id": char_id,
                "script": script,
                "knowledge_id": knowledge_id,
                "payload_size": payload_size,
                "unknown_type": unknown_type,
            }
        )
    return records
