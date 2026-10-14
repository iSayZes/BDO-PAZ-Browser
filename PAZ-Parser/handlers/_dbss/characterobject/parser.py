"""`characterobject.dbss` records, located through `characterobjectoffset.dbss`.

Each record opens with a fixed prefix, then a body chosen by `object_kind`:

    u16 character_id | u8 object_kind | u8 x3 | model_path | kind-specific body

Only the prefix is parsed here. The icon path sits at no fixed offset in the
body, so the icon index scans for it instead of walking the body: the scan
also drops the stray `?` three stored paths end with. Full layout in
docs/file-formats/characterobject_dbss.md; test_record_walk.py walks it.

Unlike `itemenchant.dbss`, blocks are not stored in key order, so offsets jump
around the file and a contiguity check on consecutive rows fails.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from _common.binary import u16
from _common.pabr_offset import PabrOffsetRow, parse_pabr_offset_rows
from _common.prefixed_string import read_prefixed_at


# Most stored paths start at "Icon/", so they hang off ui_texture. About 200
# start one level lower at "New_Icon/", which lives under ui_texture/icon/.
CHARACTER_ICON_ROOT = "ui_texture/"
_NEW_ICON_PREFIX = "new_icon/"
_NEW_ICON_ROOT = "ui_texture/icon/"

# The optional "New_" keeps a "New_Icon/..." path whole; without it the match
# starts at the inner "Icon/" and drops a folder level.
_ICON_RE = re.compile(rb"(?i)(?:new_)?icon/[ -~]{3,120}?\.(?:dds|png)")

# gc::ObjectKind member names of the 2016 client (ObjectKind_ prefix dropped).
# The file also stores kinds 10 to 37, which came later and have no name.
OBJECT_KIND_NAMES: tuple[str, ...] = (
    "PersonalTent", "FixedHouse", "Installation", "Barricade", "KingTent",
    "InnRoom", "LordTent", "Trap", "VillageTent", "Villa",
)

_KIND = 0x02
_MODEL_PATH = 0x06


@dataclass(frozen=True)
class CharacterObjectRecord:
    character_id: int
    object_kind: int
    model_path: str


def parse_characterobject_records(
    data: bytes,
    rows: list[PabrOffsetRow],
) -> list[CharacterObjectRecord]:
    """Parse every record prefix, in offset-table order.

    Raises ValueError when a row points outside the file or its record does not
    open with the row's own ID, since the prefix would then be misread.
    """
    return [_parse_record(data, row) for row in rows]


def _parse_record(data: bytes, row: PabrOffsetRow) -> CharacterObjectRecord:
    start = row.offset
    end = start + row.size
    if end > len(data):
        raise ValueError(
            f"character {row.entry_id} runs past the end of characterobject.dbss"
        )

    character_id = u16(data, start)
    if character_id != row.entry_id:
        raise ValueError(
            f"record at 0x{start:X} holds character {character_id}, "
            f"but the offset table says {row.entry_id}"
        )

    model_path, _ = read_prefixed_at(data, start + _MODEL_PATH, end, wide=False)
    return CharacterObjectRecord(
        character_id=character_id,
        object_kind=data[start + _KIND],
        model_path=model_path,
    )


def build_character_icon_index(data: bytes, offset_data: bytes) -> dict[int, str]:
    """Map character ID to icon path."""
    icons: dict[int, str] = {}

    for row in parse_pabr_offset_rows(offset_data):
        start = row.offset
        end = start + row.size
        if end > len(data):
            continue

        match = _ICON_RE.search(data, start, end)
        if match:
            icons[row.entry_id] = _icon_paz_path(match.group())

    return icons


def _icon_paz_path(stored: bytes) -> str:
    """PAZ path for a stored icon path."""
    path = stored.decode("ascii").lower()
    root = _NEW_ICON_ROOT if path.startswith(_NEW_ICON_PREFIX) else CHARACTER_ICON_ROOT
    return f"{root}{path}"
