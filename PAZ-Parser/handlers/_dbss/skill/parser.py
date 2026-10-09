"""`skill.dbss`: the rule record of every skill rank.

`skilloffset.dbss` maps each skill key (`skill_no << 16 | level`) to its
record. A record, in order:

    u32 skill_key | u32 level_1_key | u8 | ascii name | u32 name_hash
    | u8[40] | u16 resource_cost | u8[7] | u16 stamina_cost | u8[23]
    | u32 cooldown_ms | u32[10] buff_ids | utf16 description
    | utf16 script | u8[36] | u32 n + n x u32 next_skill_keys | u32 0
    | u32 m + m x u32 base_skill_keys | f32 | u8[3]

Strings are a u64 unit count plus UTF-16LE (text) or ASCII (name). Full
layout in docs/file-formats/skill_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.inline_text import decode_inline_text
from _common.pabr_offset import PabrOffsetRow, parse_pabr_u32_offset_rows
from _common.record_reader import RecordReader
from _common.skill import split_skill_key

_U8 = struct.Struct("<B")
_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")
_KEY_PAIR = struct.Struct("<II")
_BUFF_SLOTS = 10
_BUFF_IDS = struct.Struct(f"<{_BUFF_SLOTS}I")
# The 74 bytes between name_hash and cooldown_ms: unknown_n04, resource_cost
# (MP or WP, by class), unknown_n46, stamina_cost, unknown_n55.
_UNKNOWN_N04_SIZE = 40
_UNKNOWN_N46_SIZE = 7
_UNKNOWN_N55_SIZE = 23
_UNKNOWN_TAIL_SIZE = 36
# f32 unknown_f32 and u8[3] unknown_end.
_END_SIZE = 7


@dataclass(frozen=True)
class SkillRecord:
    skill_key: int
    name: str
    resource_cost: int
    stamina_cost: int
    cooldown_ms: int
    buff_ids: tuple[int, ...]
    description_kr: str
    script: str
    next_skill_keys: tuple[int, ...]
    base_skill_keys: tuple[int, ...]

    @property
    def skill_no(self) -> int:
        return split_skill_key(self.skill_key)[0]

    @property
    def level(self) -> int:
        return split_skill_key(self.skill_key)[1]


def _key_list(reader: RecordReader) -> tuple[int, ...]:
    (count,) = reader.unpack(_U32)
    return reader.unpack(struct.Struct(f"<{count}I"))


def parse_skill_record(data: bytes, row: PabrOffsetRow) -> SkillRecord:
    """Walk one record. Raises ValueError when it does not end at its index size."""
    label = f"skill 0x{row.entry_id:08X}"
    reader = RecordReader(data, row.offset, row.offset + row.size, label)
    key, _level_1_key = reader.unpack(_KEY_PAIR)
    if key != row.entry_id:
        raise ValueError(f"record at 0x{row.offset:X} holds key 0x{key:08X}, index says 0x{row.entry_id:08X}")

    reader.unpack(_U8)
    name = reader.text(wide=False)
    reader.unpack(_U32)  # name_hash
    reader.skip(_UNKNOWN_N04_SIZE)
    (resource_cost,) = reader.unpack(_U16)
    reader.skip(_UNKNOWN_N46_SIZE)
    (stamina_cost,) = reader.unpack(_U16)
    reader.skip(_UNKNOWN_N55_SIZE)
    (cooldown_ms,) = reader.unpack(_U32)
    # The IDs fill the front slots; the rest are zero.
    buff_ids = tuple(buff_id for buff_id in reader.unpack(_BUFF_IDS) if buff_id)
    description_kr = reader.text(wide=True)
    script = reader.text(wide=True)
    reader.skip(_UNKNOWN_TAIL_SIZE)
    next_skill_keys = _key_list(reader)
    reader.unpack(_U32)  # unknown_zero
    base_skill_keys = _key_list(reader)
    reader.skip(_END_SIZE)
    if not reader.at_end():
        raise ValueError(f"{label} ends {reader.remaining()} bytes before its index size")

    return SkillRecord(
        skill_key=key,
        name=name,
        resource_cost=resource_cost,
        stamina_cost=stamina_cost,
        cooldown_ms=cooldown_ms,
        buff_ids=buff_ids,
        description_kr=decode_inline_text(description_kr),
        script=script,
        next_skill_keys=next_skill_keys,
        base_skill_keys=base_skill_keys,
    )


def parse_skill_records(data: bytes, offset_data: bytes) -> list[SkillRecord]:
    """One record per index row, in index order.

    Raises ValueError on the first record that does not end exactly at its
    index size: the layout has changed and later fields would be misread.
    """
    return [parse_skill_record(data, row) for row in parse_pabr_u32_offset_rows(offset_data)]


def build_skill_buff_index(data: bytes, offset_data: bytes) -> dict[int, tuple[int, ...]]:
    """Map a skill key to the buffs it applies, in slot order; skills without buffs are left out."""
    return {
        record.skill_key: record.buff_ids
        for record in parse_skill_records(data, offset_data)
        if record.buff_ids
    }
