"""`submenu.bss`: the main menu (Esc menu) entries, grouped by category.

    PABR | u32 group_count | group_count x (u32 n | n x 49-byte entry)
    | string table | u32 string_table_start | u32 0

Each entry holds its ID, its `menu.bss` category and position, its icon as a
region of a sprite sheet, and its title as a UI string key with the key's
sheet. Full layout in docs/file-formats/bss/submenu_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import TRAILER_SIZE, read_string_table, string_at, string_table_start
from _common.ui_texture import ui_texture_path


_MAGIC = b"PABR"
_HEADER_SIZE = 8
_GROUP_COUNT_SIZE = 4

# u32 entry_id | u32 menu_id | u32 position | u64 unknown_0c | u8 unknown_14
# | u32 icon_ref | u32 x1 | u32 y1 | u32 x2 | u32 y2 | u32 sheet_ref | u32 key_ref
_ENTRY = struct.Struct("<IIIQBIIIIIII")
_ENTRY_SIZE = 49
assert _ENTRY.size == _ENTRY_SIZE


def _entry_offsets(data: bytes) -> list[int]:
    """Start of every entry, group by group.

    Raises ValueError on a bad magic, or when the groups do not end where the
    string table starts.
    """
    if len(data) < _HEADER_SIZE + TRAILER_SIZE or data[:4] != _MAGIC:
        raise ValueError("submenu.bss has invalid magic.")

    table_start = string_table_start(data)
    offsets: list[int] = []
    pos = _HEADER_SIZE
    for _ in range(u32(data, 4)):
        if pos + _GROUP_COUNT_SIZE > table_start:
            raise ValueError(f"submenu.bss group at 0x{pos:X} runs into the string table")
        count = u32(data, pos)
        pos += _GROUP_COUNT_SIZE
        offsets.extend(range(pos, pos + count * _ENTRY_SIZE, _ENTRY_SIZE))
        pos += count * _ENTRY_SIZE

    if pos != table_start:
        raise ValueError(
            f"submenu.bss groups end at 0x{pos:X} but its string table "
            f"starts at 0x{table_start:X}"
        )
    return offsets


def parse_submenu_records(data: bytes) -> list[dict]:
    """Every menu entry in file order, with its strings resolved."""
    offsets = _entry_offsets(data)
    strings = read_string_table(data)
    records: list[dict] = []
    for offset in offsets:
        (
            entry_id, menu_id, position, unknown_0c, unknown_14,
            icon_ref, x1, y1, x2, y2, sheet_ref, key_ref,
        ) = _ENTRY.unpack_from(data, offset)
        records.append({
            "entry_id": entry_id,
            "menu_id": menu_id,
            "position": position,
            "icon_path": ui_texture_path(string_at(strings, icon_ref)),
            "icon_region": (x1, y1, x2, y2),
            "sheet": string_at(strings, sheet_ref),
            "title_key": string_at(strings, key_ref),
            "unknown_0c": unknown_0c,
            "unknown_14": unknown_14,
        })
    return records


def build_submenu_icon_index(data: bytes) -> dict[int, str]:
    """Sprite sheet path by entry ID, for `IndexKind.SUBMENU_ICON`."""
    return {r["entry_id"]: r["icon_path"] for r in parse_submenu_records(data) if r["icon_path"]}


def build_submenu_icon_region_index(data: bytes) -> dict[int, tuple[int, ...]]:
    """Sprite region by entry ID, for `IndexKind.SUBMENU_ICON_REGION`."""
    return {r["entry_id"]: r["icon_region"] for r in parse_submenu_records(data) if r["icon_path"]}
