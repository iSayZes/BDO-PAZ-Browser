"""`regioninfo.bss`: the world region table.

    PABR | u32 count | count x (210-byte head + two counted lists + 171-byte tail)
    | string table | u32 string_table_start | u32 0

Records are byte-packed with no alignment, so they are walked, not searched
for. Region names come from LOC type 17 keyed by `region_key`; the string table
holds the Korean source names. Full layout in docs/file-formats/regioninfo_bss.md.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _common.binary import f32, u16, u32
from _common.pabr_strings import check_pabr, check_rows_end, read_string_table, string_at, string_table_start


_HEADER_SIZE = 8
_HEAD_SIZE = 210
_TAIL_SIZE = 171
_KEY_SIZE = 2
_VECTOR_SIZE = 12

# Head field offsets.
_COLOR = 0x02
_REGION_TYPE = 0x06
_NODE_WAR_DAY = 0x07
_IS_DESERT = 0x0F
_TERRITORY_KEY = 0x5A
_NAME_INDEX = 0x5C
_UNKNOWN_NAME_INDEX = 0x60
_CAPITAL_REGION_KEY = 0x64
_REGION_GROUP_KEY = 0x68
_NODE_KEY = 0x6F
# Tail field offsets. The siege fields are node war stat limits: flat stats are
# f32, rates u32 on the 1,000,000 = 100% scale.
_MAX_PARTICIPANTS = 0x03
_SIEGE_AP_LIMIT = 0x05
_SIEGE_DR_LIMIT = 0x09
_SIEGE_EVASION_LIMIT = 0x0D
_SIEGE_DR_RATE_LIMIT = 0x4D
_SIEGE_ACCURACY_LIMIT = 0x51
_SIEGE_RESISTANCE_LIMITS = 0x59
_RESISTANCE_COUNT = 4
_GUILD_WHARF_MANAGER = 0xA9


class _UnknownLayout(NamedTuple):
    """Offsets of unconfirmed fields in one block, grouped by type."""

    u8: tuple[int, ...] = ()
    u16: tuple[int, ...] = ()
    u32: tuple[int, ...] = ()
    f32: tuple[int, ...] = ()
    f32_arrays: dict[int, int] = {}
    u32_arrays: dict[int, int] = {}


# Unconfirmed fields, kept on the record for search and CSV export. Head
# fields are unknown_<offset>, tail fields unknown_tail_<offset> (relative to
# the tail start). Spans that are zero in every record are not kept.
_HEAD_UNKNOWNS = _UnknownLayout(
    u8=(
        0x0B, 0x0C, 0x0D, 0x0E, *range(0x10, 0x1D), 0x1F, 0x25,
        *range(0x36, 0x3B), 0x42, 0x52, 0x73, 0x93, 0xD1,
    ),
    u16=(0x1D, 0x66, 0x6B),
    u32=(0x20, 0x26, 0x3C, 0x44, 0x54, 0x95, 0xAD, 0xB1, 0xB5),
    f32_arrays={0x2A: 3, 0x77: 3, 0x83: 3, 0x99: 5},
    u32_arrays={0xB9: 6},
)
_TAIL_UNKNOWNS = _UnknownLayout(
    u8=(0x15, 0x17, 0x18, 0x45, 0x46, 0x6D, 0x86, 0x88, 0x89, 0x91),
    u16=(0x01, 0x4B),
    u32=(0x11, 0x47, 0x55, 0x69, 0x9A, 0xA2),
    f32=(0x39, 0x3D),
    f32_arrays={0x19: 6, 0x6E: 3, 0x7A: 3},
)

# CppEnums.RegionType from global_define_cpp_enum.luac, without the
# "eRegionType_" prefix. The file also uses 7 and 8, which no client enum
# names (see the format doc's In-Game Checks).
REGION_TYPE_NAMES: tuple[str, ...] = (
    "MinorTown", "MainTown", "Hunting", "Siege", "Fortress", "CastleInSiege", "Arena",
)

# CppEnums.VillageSiegeType, without the "eVillageSiegeType_" prefix. The
# value 7 (_Count) marks a region with no node war.
NODE_WAR_DAY_NAMES: tuple[str, ...] = (
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
)


def _list(data: bytes, pos: int, item_size: int, end: int) -> tuple[int, int]:
    """Count and end offset of the counted list at `pos`."""
    count = u32(data, pos)
    list_end = pos + 4 + item_size * count
    if list_end > end:
        raise ValueError(f"regioninfo.bss list at 0x{pos:X} runs past the records")
    return count, list_end


def _floats(data: bytes, offset: int, count: int) -> list[float]:
    return list(struct.unpack_from(f"<{count}f", data, offset))


_NO_LIMITS: dict = {
    "siege_ap_limit": None,
    "siege_dr_limit": None,
    "siege_evasion_limit": None,
    "siege_accuracy_limit": None,
    "siege_dr_rate_limit": None,
    "siege_resistance_limits": None,
}


def _siege_fields(data: bytes, tail: int) -> dict:
    """Max participants and node war stat limits.

    Regions without node war store FLT_MAX, INT32_MAX or other filler in the
    limit fields (`+0x4D` holds 658), so their limits are None.
    """
    max_participants = u16(data, tail + _MAX_PARTICIPANTS)
    if not max_participants:
        return {"max_participants": 0, **_NO_LIMITS}
    resistances = tail + _SIEGE_RESISTANCE_LIMITS
    return {
        "max_participants": max_participants,
        "siege_ap_limit": f32(data, tail + _SIEGE_AP_LIMIT),
        "siege_dr_limit": f32(data, tail + _SIEGE_DR_LIMIT),
        "siege_evasion_limit": f32(data, tail + _SIEGE_EVASION_LIMIT),
        "siege_accuracy_limit": f32(data, tail + _SIEGE_ACCURACY_LIMIT),
        "siege_dr_rate_limit": u32(data, tail + _SIEGE_DR_RATE_LIMIT),
        "siege_resistance_limits": list(struct.unpack_from(f"<{_RESISTANCE_COUNT}I", data, resistances)),
    }


def _unknown_fields(data: bytes, base: int, layout: _UnknownLayout, prefix: str) -> dict:
    """The unconfirmed fields of the block at `base`, named `<prefix><offset>`."""
    fields: dict = {f"{prefix}{o:02x}": data[base + o] for o in layout.u8}
    fields.update({f"{prefix}{o:02x}": u16(data, base + o) for o in layout.u16})
    fields.update({f"{prefix}{o:02x}": u32(data, base + o) for o in layout.u32})
    fields.update({f"{prefix}{o:02x}": f32(data, base + o) for o in layout.f32})
    fields.update({
        f"{prefix}{o:02x}": _floats(data, base + o, n) for o, n in layout.f32_arrays.items()
    })
    fields.update({
        f"{prefix}{o:02x}": list(struct.unpack_from(f"<{n}I", data, base + o))
        for o, n in layout.u32_arrays.items()
    })
    return fields


def _parse_record(data: bytes, head: int, end: int, strings: list[str]) -> tuple[dict, int]:
    """One record and the offset right after it."""
    key_count, keys_end = _list(data, head + _HEAD_SIZE, _KEY_SIZE, end)
    vector_count, vectors_end = _list(data, keys_end, _VECTOR_SIZE, end)
    tail = vectors_end
    if tail + _TAIL_SIZE > end:
        raise ValueError(f"regioninfo.bss record at 0x{head:X} runs past the records")

    record = {
        "region_key": u16(data, head),
        "name_kr": string_at(strings, u32(data, head + _NAME_INDEX)),
        "region_type": data[head + _REGION_TYPE],
        "node_war_day": data[head + _NODE_WAR_DAY],
        "is_desert": data[head + _IS_DESERT],
        "territory_key": data[head + _TERRITORY_KEY],
        "capital_region_key": u16(data, head + _CAPITAL_REGION_KEY),
        "region_group_key": u16(data, head + _REGION_GROUP_KEY),
        "node_key": u16(data, head + _NODE_KEY),
        "guild_wharf_manager_key": u16(data, tail + _GUILD_WHARF_MANAGER),
        **_siege_fields(data, tail),
        "unknown_02": data[head + _COLOR : head + _COLOR + 3].hex(),
        "unknown_60": string_at(strings, u32(data, head + _UNKNOWN_NAME_INDEX)),
        **_unknown_fields(data, head, _HEAD_UNKNOWNS, "unknown_"),
        "unknown_d2_keys": list(struct.unpack_from(f"<{key_count}H", data, head + _HEAD_SIZE + 4)),
        "unknown_d2_vectors": [
            _floats(data, keys_end + 4 + i * _VECTOR_SIZE, 3) for i in range(vector_count)
        ],
        **_unknown_fields(data, tail, _TAIL_UNKNOWNS, "unknown_tail_"),
    }
    return record, tail + _TAIL_SIZE


def parse_regioninfo_records(data: bytes) -> list[dict]:
    """Every region in file order.

    Raises ValueError on a bad magic, or when the walk does not end where the
    string table starts: then the layout has changed and every field is suspect.
    """
    check_pabr(data, "regioninfo.bss")

    strings = read_string_table(data)
    end = string_table_start(data)
    pos = _HEADER_SIZE
    records: list[dict] = []
    for _ in range(u32(data, 4)):
        record, pos = _parse_record(data, pos, end, strings)
        records.append(record)

    check_rows_end(data, pos, "regioninfo.bss records")
    return records
