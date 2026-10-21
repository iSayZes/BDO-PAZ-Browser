"""`pcroommaid.bss`: the character keys of the PC room maids and butlers.

No PABR magic, no trailer:

    u32 count | u16 character_key[count]

Layout in docs/file-formats/pcroommaid_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "pcroommaid.bss"

_COUNT = struct.Struct("<I")
_CHARACTER_KEY_SIZE = 2


def parse_pcroommaid(data: bytes) -> list[dict]:
    """One record per character key, in file order.

    Raises ValueError when the file is too short for its count, or when the
    keys do not end exactly at the end of the file.
    """
    if len(data) < _COUNT.size:
        raise ValueError(f"{FILE_NAME} is too short for its count")
    count = u32(data, 0)
    end = _COUNT.size + count * _CHARACTER_KEY_SIZE
    if end != len(data):
        raise ValueError(f"{FILE_NAME} declares {count} keys ({end} bytes) but holds {len(data)} bytes")
    keys = struct.unpack_from(f"<{count}H", data, _COUNT.size)
    return [{"character_key": key} for key in keys]
