"""Icon extraction from `characterobject.dbss`.

There is no preview handler for this format yet, only the part needed to map a
character ID to its icon, which `characterstatic.dbss` and
`characterspawntype.dbss` both key by.

Unlike `itemenchant.dbss`, blocks are not stored in key order, so offsets jump
around the file and a contiguity check on consecutive rows fails. The offset row
is also 10 bytes rather than 12, because the key is a u16.
"""

from __future__ import annotations

import re

from _common.binary import u16, u32


_MAGIC = b"PABR"
_OFFSET_HEADER_SIZE = 8
_OFFSET_ROW_SIZE = 10

# Stored paths already start at "Icon/", so they hang off ui_texture.
CHARACTER_ICON_ROOT = "ui_texture/"

_ICON_RE = re.compile(rb"(?i)icon/[ -~]{3,120}?\.(?:dds|png)")


def parse_characterobjectoffset_records(data: bytes) -> list[dict]:
    """Parse the character-ID index into plain dicts."""
    if len(data) < _OFFSET_HEADER_SIZE or data[:4] != _MAGIC:
        raise ValueError("characterobjectoffset.dbss has invalid magic.")

    count = u32(data, 4)
    end = _OFFSET_HEADER_SIZE + count * _OFFSET_ROW_SIZE
    if end > len(data):
        raise ValueError(
            f"characterobjectoffset.dbss declares {count:,} rows but is only "
            f"{len(data):,} bytes."
        )

    records: list[dict] = []
    for index in range(count):
        pos = _OFFSET_HEADER_SIZE + index * _OFFSET_ROW_SIZE
        records.append({
            "character_id": u16(data, pos),
            "data_offset": u32(data, pos + 0x02),
            "data_size": u32(data, pos + 0x06),
        })

    return records


def build_character_icon_index(data: bytes, offset_data: bytes) -> dict[int, str]:
    """Map character ID to icon path."""
    icons: dict[int, str] = {}

    for row in parse_characterobjectoffset_records(offset_data):
        start = row["data_offset"]
        end = start + row["data_size"]
        if end > len(data):
            continue

        match = _ICON_RE.search(data, start, end)
        if match:
            path = match.group().decode("ascii").lower()
            icons[row["character_id"]] = f"{CHARACTER_ICON_ROOT}{path}"

    return icons
