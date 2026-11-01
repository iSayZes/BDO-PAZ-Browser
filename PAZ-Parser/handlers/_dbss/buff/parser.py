"""`buff.dbss` records, located through `buffoffset.dbss`.

Each record chains fixed blocks and length-prefixed strings (Layout 3 shown):

    u32 buff_id | name | 133-byte stats block | effect_name | icon_path
    | u8 is_shown | u32 apply_rate | description | 15-byte tail head
    | ascii ui_effect | u8 is_developing_contents | u8 stacking_category
    | u8 is_exclusive | u8

Layout 2 (clients 2932 to 3458) stores `buff_id` as a u16, in the record and
in the 10-byte `buffoffset.dbss` rows. Layout 1 (clients 1774 to 1937) also
ends the record after `is_developing_contents`, with no `stacking_category`,
`is_exclusive` or `unknown_1a`; its records hold None for the first two.
Nothing in the files names their layout, so they are read with the first
layout, in client order, under which every record parses.

Full layout in docs/file-formats/dbss/buff_dbss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Callable
from dataclasses import dataclass

from _common.binary import u16, u32
from _common.buff import buff_icon_path
from _common.client_versions import ClientRange, client_order
from _common.inline_text import decode_inline_text
from _common.pabr_offset import PabrOffsetRow, parse_pabr_offset_rows, parse_pabr_u32_offset_rows
from _common.pabr_strings import HEADER_SIZE, check_rows_end
from _common.prefixed_string import read_prefixed_at
from _common.teleport import TELEPORT_EFFECT_TYPE, teleport_point_id


STATS_BLOCK_SIZE = 133
PARAM_COUNT = 10
# u32 data_offset and u32 size after the buff_id of an index row.
_INDEX_ROW_TAIL = 8

# Field offsets inside the stats block. buff_level is a u32 (the 1784 server
# reads `Level` with ReadColumnInt); its upper half is 0 on every record.
_LEVEL = 0x00
_GROUP = 0x04
_CONDITION_TYPE = 0x06
_EFFECT_TYPE = 0x08
_PARAM_SET_FLAGS = 0x09
_PARAMS = 0x13
_DURATION_MS = 0x68
_TICK_MS = 0x6C
# 1 on debuffs, which the buff bar lists apart (2016 `_isDebuff`).
_IS_DEBUFF = 0x63
# 1 when dying ends the buff (2016 `_doRemoveOnDead`).
_REMOVE_ON_DEAD = 0x83
# The equipment the buff needs, from its `_needEquipType` copy of an
# itemenchant.dbss equip type: the `equip_type` (0 for none) and the
# `equip_slot` (46 for none).
_NEED_EQUIP_TYPE = 0x7A
_NEED_EQUIP_SLOT = 0x81

# The tail head (unknown_00 to unknown_0b) runs up to ui_effect.
_UI_EFFECT = 0x0F
# From the end of ui_effect: 1 on the buffs whose name, icon and description
# the sheet build replaced with `UNKNOWN`.
_IS_DEVELOPING_CONTENTS = 0x00
# The broad family byte (food, elixir, perfume, ...).
_STACKING_CATEGORY = 0x01
# Applying the buff ends the others of its stacking category.
_IS_EXCLUSIVE = 0x02

_I16 = struct.Struct("<h")
_PARAMS_STRUCT = struct.Struct(f"<{PARAM_COUNT}q")


@dataclass(frozen=True)
class BuffLayout:
    """One documented Record shape; `number` is its Layout N in the doc."""

    number: int
    # Bytes of buff_id in the record and in the index rows: u32 or u16.
    id_size: int
    # Bytes from the end of ui_effect to the end of the record.
    tail_end_size: int
    # Whether the tail block holds stacking_category and is_exclusive.
    has_stacking: bool
    # Test clients this layout reads (the doc's Versions table, written by
    # check_docs); they only order the tries (`client_versions.py`).
    clients: tuple[ClientRange, ...] = ()

    def read_id(self, data: bytes, offset: int) -> int:
        return u32(data, offset) if self.id_size == 4 else u16(data, offset)

    def parse_rows(self, offset_data: bytes) -> list[PabrOffsetRow]:
        if self.id_size == 4:
            return parse_pabr_u32_offset_rows(offset_data)
        return parse_pabr_offset_rows(offset_data)


# Newest first.
LAYOUTS = (
    BuffLayout(3, id_size=4, tail_end_size=4, has_stacking=True, clients=(ClientRange(3464),)),
    BuffLayout(2, id_size=2, tail_end_size=4, has_stacking=True, clients=(ClientRange(2932, 3458),)),
    BuffLayout(1, id_size=2, tail_end_size=1, has_stacking=False, clients=(ClientRange(1774, 1937),)),
)


def _offset_rows(offset_data: bytes, layout: BuffLayout) -> list[PabrOffsetRow]:
    """The index rows in the layout's width.

    Raises ValueError unless they end where the PABR trailer says.
    """
    rows = layout.parse_rows(offset_data)
    rows_end = HEADER_SIZE + len(rows) * (layout.id_size + _INDEX_ROW_TAIL)
    check_rows_end(offset_data, rows_end, f"buffoffset.dbss rows of Layout {layout.number}")
    return rows


def parse_buff_offset_rows(offset_data: bytes) -> list[PabrOffsetRow]:
    """Every `buffoffset.dbss` row, in file order: u32 IDs from client 3464, u16 before.

    Raises ValueError when the rows end where the trailer says in no layout.
    """
    breaks: list[str] = []
    for layout in client_order(LAYOUTS, lambda layout: layout.clients):
        try:
            return _offset_rows(offset_data, layout)
        except ValueError as error:
            breaks.append(str(error))
    raise ValueError(f"buffoffset.dbss fits no known layout ({'; '.join(breaks)})")


def _parse_record(data: bytes, row: PabrOffsetRow, layout: BuffLayout) -> dict:
    start = row.offset
    end = start + row.size
    if end > len(data):
        raise ValueError(f"buff {row.entry_id} runs past the end of buff.dbss")
    if layout.read_id(data, start) != row.entry_id:
        raise ValueError(f"buff {row.entry_id} record does not start with its own ID")

    name, stats = read_prefixed_at(data, start + layout.id_size, end, wide=True)
    effect_name, pos = read_prefixed_at(data, stats + STATS_BLOCK_SIZE, end, wide=True)
    icon, pos = read_prefixed_at(data, pos, end, wide=False)

    is_shown = data[pos]
    apply_rate = u32(data, pos + 1)
    description, pos = read_prefixed_at(data, pos + 5, end, wide=True)
    ui_effect, pos = read_prefixed_at(data, pos + _UI_EFFECT, end, wide=False)

    if pos + layout.tail_end_size != end:
        raise ValueError(
            f"buff {row.entry_id} ends {end - pos} bytes after ui_effect, expected {layout.tail_end_size}"
        )

    params = _PARAMS_STRUCT.unpack_from(data, stats + _PARAMS)
    record = {
        "buff_id": row.entry_id,
        "name": name,
        "level": u32(data, stats + _LEVEL),
        "effect_type": data[stats + _EFFECT_TYPE],
        # A u16: keys from 40001 up read negative as an i16.
        "group": u16(data, stats + _GROUP),
        "condition_type": _I16.unpack_from(data, stats + _CONDITION_TYPE)[0],
        "duration_ms": u32(data, stats + _DURATION_MS),
        # Tick interval of a periodic effect; 0 on everything else.
        "tick_ms": u32(data, stats + _TICK_MS),
        "is_debuff": bool(data[stats + _IS_DEBUFF]),
        "remove_on_dead": bool(data[stats + _REMOVE_ON_DEAD]),
        "need_equip_type": data[stats + _NEED_EQUIP_TYPE],
        "need_equip_slot": data[stats + _NEED_EQUIP_SLOT],
        "effect_name": effect_name,
        "icon_path": buff_icon_path(icon),
        "is_shown": bool(is_shown),
        "apply_rate": apply_rate,
        "description_kr": decode_inline_text(description),
        # Empty on every record of the clients read so far.
        "ui_effect": ui_effect,
        "is_developing_contents": bool(data[pos + _IS_DEVELOPING_CONTENTS]),
        # None in Layout 1, whose tail block ends before them.
        "stacking_category": data[pos + _STACKING_CATEGORY] if layout.has_stacking else None,
        "is_exclusive": bool(data[pos + _IS_EXCLUSIVE]) if layout.has_stacking else None,
    }
    record.update({f"param_{index}": value for index, value in enumerate(params, 1)})
    # The param_N_set flags: which parameters the sheet row fills.
    record["params_set"] = tuple(bool(flag) for flag in data[stats + _PARAM_SET_FLAGS : stats + _PARAMS])
    return record


def parse_buff_records(data: bytes, offset_data: bytes) -> list[dict]:
    """Parse every record `buffoffset.dbss` points at, in its order, with the
    first layout (in client order) under which every record parses.

    Raises ValueError, naming where each layout broke, when none fits: the
    layout has no resync point, so a bad length would silently misread every
    field after it.
    """
    breaks: list[str] = []
    for layout in client_order(LAYOUTS, lambda layout: layout.clients):
        try:
            rows = _offset_rows(offset_data, layout)
            return [_parse_record(data, row, layout) for row in rows]
        except ValueError as error:
            breaks.append(f"Layout {layout.number}: {error}")
    raise ValueError(f"buff.dbss fits no known layout ({'; '.join(breaks)})")


def _teleport_buffs(data: bytes, offset_data: bytes) -> list[dict]:
    """The effect type 23 buffs, which name a teleport.dbss section and key."""
    records = parse_buff_records(data, offset_data)
    return [record for record in records if record["effect_type"] == TELEPORT_EFFECT_TYPE]


def build_teleport_buff_index(data: bytes, offset_data: bytes) -> dict[int, tuple[int, ...]]:
    """The `TELEPORT_BUFFS` index: each teleport point to the buffs that go there, by buff ID."""
    points: dict[int, list[int]] = {}
    for record in _teleport_buffs(data, offset_data):
        point_id = teleport_point_id(record["param_1"], record["param_2"])
        points.setdefault(point_id, []).append(record["buff_id"])
    return {point_id: tuple(sorted(buff_ids)) for point_id, buff_ids in points.items()}


def build_teleport_buff_name_index(data: bytes, offset_data: bytes) -> dict[int, str]:
    """The `TELEPORT_BUFF_NAME_KR` index: each teleport buff to its Korean name."""
    return {
        record["buff_id"]: record["name"].strip()
        for record in _teleport_buffs(data, offset_data)
        if record["name"].strip()
    }
