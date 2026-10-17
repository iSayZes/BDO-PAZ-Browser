"""`skilltype.dbss`: the presentation record of every skill.

`skilltypeoffset.dbss` maps each skill key to its record. A record opens with

    u32 skill_key | utf16 name | utf16 group_name | u32 kind | config ...

where strings are a u64 UTF-16 code-unit count plus UTF-16LE text. The action
`config` is not decoded; the skill icon is its first length-prefixed ASCII
`.dds` path. Full layout in docs/file-formats/skilltype_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_offset import PabrOffsetRow, parse_pabr_u32_offset_rows
from _common.prefixed_string import find_prefixed_ascii
from _common.record_reader import RecordReader
from _common.skill import split_skill_key
from _common.ui_texture import UI_TEXTURE_ICON_ROOT, ui_texture_path

_U32 = struct.Struct("<I")
_ICON_SUFFIX = ".dds"


@dataclass(frozen=True)
class SkillTypeRecord:
    skill_key: int
    name_kr: str
    group_name_kr: str
    kind: int
    icon_path: str

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


def _icon_path(data: bytes, start: int, end: int) -> str:
    for path in find_prefixed_ascii(data, start, end):
        if path.lower().endswith(_ICON_SUFFIX):
            # Stored paths start at "New_Icon/", which lives under ui_texture/icon/.
            return ui_texture_path(path, UI_TEXTURE_ICON_ROOT)
    return ""


def parse_skilltype_records(data: bytes, offset_data: bytes) -> list[SkillTypeRecord]:
    """One record per index row, in index order."""
    records: list[SkillTypeRecord] = []
    for row in parse_pabr_u32_offset_rows(offset_data):
        reader, name_kr, group_name_kr, kind = _read_head(data, row)
        records.append(SkillTypeRecord(
            skill_key=row.entry_id,
            name_kr=name_kr,
            group_name_kr=group_name_kr,
            kind=kind,
            icon_path=_icon_path(data, reader.pos, row.offset + row.size),
        ))
    return records


def build_skill_icon_index(data: bytes, offset_data: bytes) -> dict[int, str]:
    """Icon path by skill number, for `IndexKind.SKILL_ICON`.

    Skills without an icon are left out. Every key is level 1, so each skill
    number has one record.
    """
    return {
        record.skill_no: record.icon_path
        for record in parse_skilltype_records(data, offset_data)
        if record.icon_path
    }


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
