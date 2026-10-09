"""`instancefieldmapinfo.bss`: map data per instance field key.

    PABR | u32 count | count x record | string table | u32 table_start | u32 0
    record: 196 fixed bytes | u32 hash_count | u32[hash_count]
            | u32 spawn_count | f32[3][spawn_count] | (f32, u32) when spawn_count

The key is the `instancefield.dbss` field key. Title and description are
`GAME` sheet keys, the image a `ui_texture` path with a pixel region.
Full layout in docs/file-formats/instancefieldmapinfo_bss.md.
"""

from __future__ import annotations

import struct

from _bss.menu.parser import sprite_sheet_path
from _bss.stringtable.parser import GAME_SHEET, parse_sheet_key_hashes
from _common.binary import u32
from _common.pabr_strings import (
    HEADER_SIZE,
    check_rows_end,
    checked_string_table_start,
    read_string_table,
    string_at,
)
from _common.record_reader import RecordReader


_FILE = "instancefieldmapinfo.bss"
_HEAD = struct.Struct("<HII4fIIBII4H")
# +0x33 filler; then +0x9D u8, +0x9E u16, +0xA0 zero
_FILLER_SIZE = 0x9D - 0x33
_MIDDLE = struct.Struct("<BH8x")
# +0xA8 entry item, +0xAC, +0xB0 zero, +0xB4, +0xB8 zero
_TAIL = struct.Struct("<II4xI4x")
_COUNT = struct.Struct("<I")
_VEC3 = struct.Struct("<3f")
_SPAWN_TAIL = struct.Struct("<fI")


def _read_record(reader: RecordReader, strings: list[str]) -> dict:
    (
        key, unknown_02, unknown_06, x, y, z, radius,
        title_ref, description_ref, unknown_22, unknown_23, image_ref, *region,
    ) = reader.unpack(_HEAD)
    reader.skip(_FILLER_SIZE)
    unknown_9d, unknown_9e = reader.unpack(_MIDDLE)
    entry_item_id, unknown_ac, unknown_b4 = reader.unpack(_TAIL)
    (hash_count,) = reader.unpack(_COUNT)
    hashes = [reader.unpack(_COUNT)[0] for _ in range(hash_count)]
    (spawn_count,) = reader.unpack(_COUNT)
    spawns = [list(reader.unpack(_VEC3)) for _ in range(spawn_count)]
    spawn_f32, spawn_u32 = reader.unpack(_SPAWN_TAIL) if spawn_count else (None, None)
    return {
        "key": key,
        "title_key": string_at(strings, title_ref),
        "description_key": string_at(strings, description_ref),
        "x": x,
        "y": y,
        "z": z,
        "radius": radius,
        "image_path": sprite_sheet_path(string_at(strings, image_ref)),
        "image_region": region,
        "entry_item_id": entry_item_id,
        "spawns": spawns,
        "unknown_02": unknown_02,
        "unknown_06": unknown_06,
        "unknown_22": unknown_22,
        "unknown_23": unknown_23,
        "unknown_9d": unknown_9d,
        "unknown_9e": unknown_9e,
        "unknown_ac": unknown_ac,
        "unknown_b4": unknown_b4,
        "unknown_hashes": hashes,
        "unknown_spawn_f32": spawn_f32,
        "unknown_spawn_u32": spawn_u32,
    }


def parse_instancefieldmapinfo_records(data: bytes) -> list[dict]:
    """Every record in file order, with its strings resolved.

    Raises ValueError on a bad magic, a record running past the string table
    or records that do not end where the string table starts.
    """
    table_start = checked_string_table_start(data, _FILE)
    strings = read_string_table(data)
    reader = RecordReader(data, HEADER_SIZE, table_start, _FILE)
    records = [_read_record(reader, strings) for _ in range(u32(data, 4))]
    check_rows_end(data, reader.pos, f"{_FILE} records")
    return records


def build_instance_field_title_index(data: bytes, stringtable: bytes) -> dict[int, int]:
    """INSTANCE_FIELD_TITLE: field key -> `GAME` sheet hash of its title key.

    Fields without a title key, or whose key `stringtable.bss` lacks, are left out.
    """
    hashes = parse_sheet_key_hashes(stringtable, [GAME_SHEET])[GAME_SHEET]
    index: dict[int, int] = {}
    for record in parse_instancefieldmapinfo_records(data):
        key_hash = hashes.get(record["title_key"])
        if key_hash is not None:
            index[record["key"]] = key_hash
    return index
