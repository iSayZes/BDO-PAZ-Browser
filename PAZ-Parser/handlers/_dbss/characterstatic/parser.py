"""`characterstatic.dbss` records, located through `characterstaticoffset.dbss`.

Each offset row points just past a two-byte inline copy of the character ID.
The payload opens with eight flag bytes and two scripts, then a fixed
287-byte block of character fields, then six strings back to back:

    u8[8] flags | u8 0x15 | action_script | condition_script
    | character fields: u8 | u16 character_id | i16 | u8 npc_kind | u8 grade
      | i32 tendency_on_dead | i32 ocean_tendency | ... | u8 vehicle_type @ +0xA6 | ...
    | ai_script | model_path | name_kr | label_kr | title_kr | voice_bank
    | ... | u32 holdable_item_count | u32[] | ... | u32 contents_group_count | u32[]
    | u8 class_type | ... | u32 source_item_id | ... (24 bytes)

Every string is a u64 count and its text: UTF-16LE for the scripts and the
three Korean strings, ASCII for the AI script (the stem of an `.ai` file,
`9999`, `PC`), the model path and the voice bank. Each contents group is
stored as the client's string hash of its decimal key, which
`contents_group_key` turns back into the key. Full layout in
docs/file-formats/characterstatic_dbss.md.
"""

from __future__ import annotations

import struct
from functools import cache

from _common.binary import whole_float
from _common.knowledge_script import knowledge_id_of
from _common.pabr_offset import PabrOffsetRow, parse_pabr_offset_rows
from _common.prefixed_string import read_prefixed_at
from _common.string_hash import KEY_HASH_SEED, hashlittle

_TAG = 0x08
_TAG_VALUE = 0x15
_ACTION_SCRIPT = 0x09
# From the first byte after condition_script, the start of the character fields.
_CHARACTER_ID = 0x01
_CHARACTER_GROUP = 0x03
_NPC_KIND = 0x05
_GRADE = 0x06
_TENDENCY_ON_DEAD = 0x07
_OCEAN_TENDENCY = 0x0B
_VEHICLE_TYPE = 0xA6
_TRIBE_TYPE = 0xB3
_LEVEL = 0xC3
_BODY_SIZE = 0xDB
# The AI script follows the character fields.
_CHARACTER_FIELDS_SIZE = 0x11F
# From the end of voice_bank, then from the end of holdable_item_keys.
_HOLDABLE_ITEM_COUNT = 0x0E
_CONTENTS_GROUP_COUNT = 0x18
# From the end of contents_group_hashes, which the payload ends 24 bytes after.
_CLASS_TYPE = 0x00
_SOURCE_ITEM = 0x09
_TAIL_SIZE = 0x18
# Contents group keys are searched up to this value; client 3474 uses up to 8,122.
_CONTENTS_GROUP_KEY_LIMIT = 0x10000
# class_type on every row that is not a player character.
NO_CLASS_TYPE = 101
# vehicle_type on every row that is not a vehicle: the sheet's -1 written as
# the CppEnums.VehicleType member count.
NO_VEHICLE_TYPE = 65
# gc::CharacterKind member names of the 2016 client, in value order. The file
# also stores 12, 15 and 17, which came later and have no name.
NPC_KIND_NAMES: tuple[str, ...] = (
    "Player", "Monster", "Npc", "Vehicle", "Collect",
    "SiegeGate", "SiegeSymbol", "Household", "Installation", "InstanceObject",
)

_I16 = struct.Struct("<h")
_I32 = struct.Struct("<i")
_U32 = struct.Struct("<I")
_F32 = struct.Struct("<f")


@cache
def _contents_group_keys_by_hash() -> dict[int, int]:
    # hashlittle, not the cached key_hash: 65,536 keys would flush its cache.
    return {
        hashlittle(str(key).encode("utf-16-le"), KEY_HASH_SEED): key
        for key in range(_CONTENTS_GROUP_KEY_LIMIT)
    }


def contents_group_key(group_hash: int) -> int | None:
    """The contents group key whose decimal text hashes to `group_hash`, or None."""
    return _contents_group_keys_by_hash().get(group_hash)


def _read_u32_list(data: bytes, count_at: int, end: int) -> tuple[tuple[int, ...], int]:
    """Read a u32 count and that many u32s; return them and the next position."""
    (count,) = _U32.unpack_from(data, count_at)
    list_end = count_at + _U32.size * (1 + count)
    if list_end > end:
        raise ValueError(f"list at 0x{count_at:X} runs past 0x{end:X}")
    return struct.unpack_from(f"<{count}I", data, count_at + _U32.size), list_end


def _read_strings(data: bytes, pos: int, end: int, wide: tuple[bool, ...]) -> tuple[list[str], int]:
    """Read strings back to back from `pos`; return them and the next position."""
    texts = []
    for is_wide in wide:
        text, pos = read_prefixed_at(data, pos, end, wide=is_wide)
        texts.append(text)
    return texts, pos


def _parse_record(data: bytes, row: PabrOffsetRow) -> dict:
    character_id = row.entry_id
    try:
        return _parse_payload(data, row)
    except ValueError as ex:
        raise ValueError(f"character {character_id}: {ex}") from ex


def _parse_payload(data: bytes, row: PabrOffsetRow) -> dict:
    start = row.offset
    end = start + row.size
    character_id = row.entry_id
    if end > len(data) or row.size < _ACTION_SCRIPT:
        raise ValueError("record runs past the end of characterstatic.dbss")
    if data[start + _TAG] != _TAG_VALUE:
        raise ValueError("record does not carry the 0x15 tag")

    (action_script, condition_script), pos = _read_strings(data, start + _ACTION_SCRIPT, end, (True, True))
    if pos + _CHARACTER_FIELDS_SIZE > end:
        raise ValueError("record ends inside its character fields")
    if struct.unpack_from("<H", data, pos + _CHARACTER_ID)[0] != character_id:
        raise ValueError("record does not repeat its own ID")

    (ai_script, model_path, name_kr, label_kr, title_kr, _voice_bank), voice_end = _read_strings(
        data, pos + _CHARACTER_FIELDS_SIZE, end, (False, False, True, True, True, False)
    )
    _holdable_items, holdable_end = _read_u32_list(data, voice_end + _HOLDABLE_ITEM_COUNT, end)
    contents_group_hashes, tail = _read_u32_list(data, holdable_end + _CONTENTS_GROUP_COUNT, end)
    if tail + _TAIL_SIZE != end:
        raise ValueError(f"record ends {end - tail} bytes after its contents groups, not {_TAIL_SIZE}")
    return {
        "character_id": character_id,
        "action_script": action_script,
        "condition_script": condition_script,
        "knowledge_id": knowledge_id_of(action_script),
        "character_group": _I16.unpack_from(data, pos + _CHARACTER_GROUP)[0],
        "npc_kind": data[pos + _NPC_KIND],
        "grade": data[pos + _GRADE],
        "tendency_on_dead": _I32.unpack_from(data, pos + _TENDENCY_ON_DEAD)[0],
        "ocean_tendency": _I32.unpack_from(data, pos + _OCEAN_TENDENCY)[0],
        "vehicle_type": data[pos + _VEHICLE_TYPE],
        "tribe_type": data[pos + _TRIBE_TYPE],
        "level": _U32.unpack_from(data, pos + _LEVEL)[0],
        "body_size": whole_float(_F32.unpack_from(data, pos + _BODY_SIZE)[0]),
        "contents_group_hashes": contents_group_hashes,
        "class_type": data[tail + _CLASS_TYPE],
        "source_item_id": _U32.unpack_from(data, tail + _SOURCE_ITEM)[0],
        "ai_script": ai_script,
        "model_path": model_path,
        "name_kr": name_kr,
        "label_kr": label_kr,
        "title_kr": title_kr,
        "payload_size": row.size,
    }


def parse_characterstatic_records(data: bytes, rows: list[PabrOffsetRow]) -> list[dict]:
    """Parse every record the offset table points at, in offset-table order.

    Raises ValueError on the first malformed record: after a bad string length
    every later field would be misread.
    """
    return [_parse_record(data, row) for row in rows]


def build_knowledge_character_index(data: bytes, offset_data: bytes) -> dict[int, tuple[int, ...]]:
    """Map knowledge ID to every character whose action script grants it.

    Character IDs are ascending, so the original NPC comes before later copies
    of it (47280 before 59998). A malformed record is skipped rather than
    failing the whole index: the preview of this table reports it instead.
    """
    characters: dict[int, list[int]] = {}

    for row in parse_pabr_offset_rows(offset_data):
        try:
            knowledge_id = _parse_record(data, row)["knowledge_id"]
        except (ValueError, struct.error):
            continue
        if knowledge_id is not None:
            characters.setdefault(knowledge_id, []).append(row.entry_id)

    return {
        knowledge_id: tuple(sorted(ids))
        for knowledge_id, ids in characters.items()
    }


def build_character_ai_script_index(data: bytes, offset_data: bytes) -> dict[int, str]:
    """Map character ID to the stem of its `.ai` script, for characters that name one.

    A malformed record is skipped, as in `build_knowledge_character_index`.
    """
    scripts: dict[int, str] = {}
    for row in parse_pabr_offset_rows(offset_data):
        try:
            ai_script = _parse_record(data, row)["ai_script"]
        except (ValueError, struct.error):
            continue
        if ai_script:
            scripts[row.entry_id] = ai_script
    return scripts
