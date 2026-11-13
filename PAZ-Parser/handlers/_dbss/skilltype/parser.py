"""`skilltype.dbss`: the presentation record of every skill.

`skilltypeoffset.dbss` maps each skill key to its record. A record, in order
(Layout 5 shown):

    u32 skill_key | utf16 name | utf16 group_name | u32 kind | u16
    | u32 n + n x u32 next_rank_keys | u64 class_mask | u64 | u8[9] equip type
    | u16 max_level | u32 skill_owner_type | u32 first_rank_key
    | ascii icon_path | utf16 | utf16 description | u8[5]
    | u64 n + n x u32 | u8 awakening_type | u8[3]
    | u32 n + n x u32 contents_group_hashes | u32 n + n x u16 exclusive_skill_nos
    | u8 condition | utf16 pattern_control | u8 branch | u32[2] | u8 | utf16

Layout 4 (clients 1529 to 2250) has two ASCII movie paths after
`description`. Layout 3 (1519 to 1524) also ends after the u8 that follows
the u32 pair, Layout 2 (1381 to 1509) after the u32 pair, and Layout 1 (1346
to 1379) also has two bytes, not three, after `awakening_type`. Nothing in
the file names its layout, so it is read with the first layout, in client
order, that reads every record.

`pattern_control` (`ARCHER_20`) is the string key whose `key_hash()` is the
skill's `commandtooltip.dbss` row.

Strings are a u64 unit count plus UTF-16LE (text) or ASCII (paths). Full
layout in docs/file-formats/dbss/skilltype_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.client_versions import ClientRange, client_order
from _common.pabr_offset import PabrOffsetRow, parse_pabr_u32_offset_rows
from _common.record_reader import RecordReader
from _common.skill import split_skill_key
from _common.ui_texture import UI_TEXTURE_ICON_ROOT, ui_texture_path

_U8 = struct.Struct("<B")
_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
_U16_SIZE = 2
_U32_SIZE = 4
# Code unit sizes of the strings the parser skips without decoding.
_UTF16_UNIT = 2
_ASCII_UNIT = 1
_ICON_SUFFIX = ".dds"
# unknown_group_name_04.
_AFTER_KIND_SIZE = 2
# class_mask, unknown_next_rank_keys_08, the nine equip type bytes, max_level,
# skill_owner_type and first_rank_key.
_AFTER_NEXT_RANKS_SIZE = 35
# unknown_description_00 to can_quick_slot.
_AFTER_DESCRIPTION_SIZE = 5
# condition.
_AFTER_EXCLUSIVES_SIZE = 1
# branch, unknown_pattern_control_01 and unknown_pattern_control_05.
_AFTER_PATTERN_CONTROL_SIZE = 9
# unknown_pattern_control_09.
_PATTERN_CONTROL_09_SIZE = 1


@dataclass(frozen=True)
class SkillTypeLayout:
    """One documented Payload shape; `number` is its Layout N in the doc."""

    number: int
    # movie_path and unknown_after_movie_path after description.
    has_movie_paths: bool
    # unknown_list_01, unknown_list_02 and is_developing_contents after
    # awakening_type; Layout 1 has no unknown_list_02.
    flags_after_awakening_type: int
    # The u8 unknown_pattern_control_09, from Layout 3 on.
    has_unknown_pattern_control_09: bool
    # The utf16 unknown_pattern_control_0a, from Layout 4 on.
    has_unknown_pattern_control_0a: bool
    # Test clients this layout reads (the doc's Versions table, written by
    # check_docs); they only order the tries (`client_versions.py`).
    clients: tuple[ClientRange, ...] = ()


# Newest first.
LAYOUTS = (
    SkillTypeLayout(5, has_movie_paths=False, flags_after_awakening_type=3, has_unknown_pattern_control_09=True,
                    has_unknown_pattern_control_0a=True, clients=(ClientRange(2259),)),
    SkillTypeLayout(4, has_movie_paths=True, flags_after_awakening_type=3, has_unknown_pattern_control_09=True,
                    has_unknown_pattern_control_0a=True, clients=(ClientRange(1529, 2250),)),
    SkillTypeLayout(3, has_movie_paths=True, flags_after_awakening_type=3, has_unknown_pattern_control_09=True,
                    has_unknown_pattern_control_0a=False, clients=(ClientRange(1519, 1524),)),
    SkillTypeLayout(2, has_movie_paths=True, flags_after_awakening_type=3, has_unknown_pattern_control_09=False,
                    has_unknown_pattern_control_0a=False, clients=(ClientRange(1381, 1509),)),
    SkillTypeLayout(1, has_movie_paths=True, flags_after_awakening_type=2, has_unknown_pattern_control_09=False,
                    has_unknown_pattern_control_0a=False, clients=(ClientRange(1346, 1379),)),
)


@dataclass(frozen=True)
class SkillTypeRecord:
    skill_key: int
    name_kr: str
    group_name_kr: str
    kind: int
    icon_path: str
    # CppEnums.SkillAwakeningType: 0 normal, 1 Awakening weapon.
    awakening_type: int
    # The commandtooltip.dbss key, such as `ARCHER_20`; empty on most non-class skills.
    pattern_control: str

    @property
    def skill_no(self) -> int:
        return split_skill_key(self.skill_key)[0]


def _read_head(data: bytes, row: PabrOffsetRow) -> tuple[RecordReader, str, str, int]:
    """Reader positioned after `kind`, plus the name, group name and kind."""
    label = f"skill type 0x{row.entry_id:08X}"
    reader = RecordReader(data, row.offset, row.offset + row.size, label)
    (key,) = reader.unpack(_U32)
    if key != row.entry_id:
        raise ValueError(f"record at 0x{row.offset:X} holds key 0x{key:08X}, index says 0x{row.entry_id:08X}")
    name_kr = reader.text(wide=True)
    group_name_kr = reader.text(wide=True)
    (kind,) = reader.unpack(_U32)
    return reader, name_kr, group_name_kr, kind


def _skip_list(reader: RecordReader, count_fmt: struct.Struct, item_size: int) -> None:
    """Skip a counted list, or a u64-counted string with `item_size` its code unit size."""
    (count,) = reader.unpack(count_fmt)
    reader.skip(count * item_size)


def _icon_path(stored: str) -> str:
    """The stored `.dds` icon under ui_texture/icon/; item skills store `.png` paths, which are left out."""
    if not stored.lower().endswith(_ICON_SUFFIX):
        return ""
    # Stored paths start at "New_Icon/", which lives under ui_texture/icon/.
    return ui_texture_path(stored, UI_TEXTURE_ICON_ROOT)


def _read_icon(reader: RecordReader) -> str:
    """The stored icon path of a reader positioned after `kind`; every layout has it at the same place."""
    reader.skip(_AFTER_KIND_SIZE)
    _skip_list(reader, _U32, _U32_SIZE)  # next_rank_keys
    reader.skip(_AFTER_NEXT_RANKS_SIZE)
    return reader.text(wide=False)


def _parse_record(data: bytes, row: PabrOffsetRow, layout: SkillTypeLayout) -> SkillTypeRecord:
    """Walk one record. Raises ValueError when it does not end at its index size."""
    reader, name_kr, group_name_kr, kind = _read_head(data, row)
    stored_icon = _read_icon(reader)
    _skip_list(reader, _U64, _UTF16_UNIT)  # unknown_after_icon_path
    _skip_list(reader, _U64, _UTF16_UNIT)  # description
    if layout.has_movie_paths:
        _skip_list(reader, _U64, _ASCII_UNIT)  # movie_path
        _skip_list(reader, _U64, _ASCII_UNIT)  # unknown_after_movie_path
    reader.skip(_AFTER_DESCRIPTION_SIZE)
    _skip_list(reader, _U64, _U32_SIZE)  # unknown_list
    (awakening_type,) = reader.unpack(_U8)
    reader.skip(layout.flags_after_awakening_type)
    _skip_list(reader, _U32, _U32_SIZE)  # contents_group_hashes
    _skip_list(reader, _U32, _U16_SIZE)  # exclusive_skill_nos
    reader.skip(_AFTER_EXCLUSIVES_SIZE)
    pattern_control = reader.text(wide=True)
    reader.skip(_AFTER_PATTERN_CONTROL_SIZE)
    if layout.has_unknown_pattern_control_09:
        reader.skip(_PATTERN_CONTROL_09_SIZE)
    if layout.has_unknown_pattern_control_0a:
        _skip_list(reader, _U64, _UTF16_UNIT)
    if not reader.at_end():
        raise ValueError(f"skill type 0x{row.entry_id:08X} ends {reader.remaining()} bytes before its index size")

    return SkillTypeRecord(
        skill_key=row.entry_id,
        name_kr=name_kr,
        group_name_kr=group_name_kr,
        kind=kind,
        icon_path=_icon_path(stored_icon),
        awakening_type=awakening_type,
        pattern_control=pattern_control,
    )


def parse_skilltype_records(data: bytes, offset_data: bytes) -> list[SkillTypeRecord]:
    """One record per index row, in index order, read with the first layout
    (in client order) under which every record ends exactly at its index size.

    Raises ValueError, naming where each layout broke, when none fits.
    """
    rows = parse_pabr_u32_offset_rows(offset_data)
    breaks: list[str] = []
    for layout in client_order(LAYOUTS, lambda layout: layout.clients):
        try:
            return [_parse_record(data, row, layout) for row in rows]
        except ValueError as error:
            breaks.append(f"Layout {layout.number}: {error}")
    raise ValueError(f"skilltype.dbss fits no known layout ({'; '.join(breaks)})")


def build_skill_icon_index(data: bytes, offset_data: bytes) -> dict[int, str]:
    """Icon path by skill number, for `IndexKind.SKILL_ICON`.

    Reads each record only up to `icon_path`, so it needs no layout. Skills
    without an icon are left out. Every key is level 1, so each skill number
    has one record.
    """
    icons: dict[int, str] = {}
    for row in parse_pabr_u32_offset_rows(offset_data):
        reader, _, _, _ = _read_head(data, row)
        icon_path = _icon_path(_read_icon(reader))
        if icon_path:
            icons[split_skill_key(row.entry_id)[0]] = icon_path
    return icons


def build_skill_name_index(data: bytes, offset_data: bytes) -> dict[int, str]:
    """Korean skill name by skill number, for `IndexKind.SKILL_NAME_KR`.

    Reads only the head of each record. `skill_name()` falls back to it when
    LOC type 10 has no name.
    """
    names: dict[int, str] = {}
    for row in parse_pabr_u32_offset_rows(offset_data):
        _, name_kr, _, _ = _read_head(data, row)
        if name_kr:
            names.setdefault(split_skill_key(row.entry_id)[0], name_kr)
    return names
