"""`characterstatic.dbss` records, located through `characterstaticoffset.dbss`.

Each offset row points just past a two-byte inline copy of the character ID.
The payload opens with two length-prefixed scripts, then the ID again:

    u8[8] header | u8 tag 0x15 | action_script | condition_script
    | u8 | u16 character_id | u16 | u8 npc_kind | u8 grade
    | i32 tendency_on_dead | i32 ocean_tendency | ... | u8 vehicle_type @ p+166
    | ... ai_script model_path name_kr label_kr title_kr ...
    | u8 class_type @ end-24 | ... | u32 source_item_id @ end-15 | ...

Both scripts are an i64 UTF-16 code-unit count followed by UTF-16LE text. The
model path is an i64 byte count plus ASCII at no fixed offset, so it is found by
scanning; it is the only folder path among the record's ASCII strings. The
string right before it names the character's AI script, the stem of an `.ai`
file (`9999`, `Monsters_Main_Manager`), and the three UTF-16 strings right
after it are the Korean name, internal label and title.
Full layout in docs/file-formats/characterstatic_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.knowledge_script import knowledge_id_of
from _common.pabr_offset import PabrOffsetRow, parse_pabr_offset_rows
from _common.prefixed_string import STRING_PREFIX_SIZE, locate_prefixed_ascii, read_prefixed_at

_TAG = 0x08
_TAG_VALUE = 0x15
_ACTION_SCRIPT = 0x09
# From the first byte after condition_script.
_CHARACTER_ID = 0x01
_NPC_KIND = 0x05
_GRADE = 0x06
_TENDENCY_ON_DEAD = 0x07
_OCEAN_TENDENCY = 0x0B
_VEHICLE_TYPE = 0xA6
# The fixed fields end before the AI script and model path strings.
_FIXED_SIZE = _VEHICLE_TYPE + 1
# From the end of the payload.
_CLASS_TYPE_FROM_END = 24
_SOURCE_ITEM_FROM_END = 15
# class_type on every row that is not a player character.
NO_CLASS_TYPE = 101
# vehicle_type on every row that is not a vehicle; not a CppEnums.VehicleType member.
NO_VEHICLE_TYPE = 65
# gc::CharacterKind member names of the 2016 client, in value order. The file
# also stores 12, 15 and 17, which came later and have no name.
NPC_KIND_NAMES: tuple[str, ...] = (
    "Player", "Monster", "Npc", "Vehicle", "Collect",
    "SiegeGate", "SiegeSymbol", "Household", "Installation", "InstanceObject",
)

_I64 = struct.Struct("<q")
_I32 = struct.Struct("<i")
_U32 = struct.Struct("<I")


def _read_script(data: bytes, pos: int, end: int, character_id: int) -> tuple[str, int]:
    """Read an i64-prefixed UTF-16LE script; return it and the next position."""
    (length,) = _I64.unpack_from(data, pos)
    text_end = pos + _I64.size + 2 * length
    if length < 0 or text_end > end:
        raise ValueError(f"character {character_id} has a script that runs past its record")
    return data[pos + _I64.size:text_end].decode("utf-16-le"), text_end


@dataclass(frozen=True)
class RecordStrings:
    """The strings after the fixed fields; '' for each when no model path is found."""

    ai_script: str = ""
    model_path: str = ""
    name_kr: str = ""
    label_kr: str = ""
    title_kr: str = ""


def _record_strings(data: bytes, start: int, end: int) -> RecordStrings:
    """The AI script, model path and Korean strings in `[start, end)`.

    The model path is the longest folder path among the ASCII strings; the AI
    script is the string right before it, '' when the path comes first
    (player characters). The Korean name, internal label and title are the
    three UTF-16 strings right after it.
    """
    found = locate_prefixed_ascii(data, start, end)
    paths = [(prefix_at, text) for prefix_at, text in found if "/" in text]
    if not paths:
        return RecordStrings()
    model_at, model_path = max(paths, key=lambda path: len(path[1]))
    model_index = found.index((model_at, model_path))
    before = found[model_index - 1][1] if model_index else ""
    name_kr, pos = read_prefixed_at(data, model_at + STRING_PREFIX_SIZE + len(model_path), end, wide=True)
    label_kr, pos = read_prefixed_at(data, pos, end, wide=True)
    title_kr, _ = read_prefixed_at(data, pos, end, wide=True)
    return RecordStrings(
        ai_script="" if "/" in before else before,
        model_path=model_path,
        name_kr=name_kr,
        label_kr=label_kr,
        title_kr=title_kr,
    )


def _parse_record(data: bytes, row: PabrOffsetRow) -> dict:
    start = row.offset
    end = start + row.size
    character_id = row.entry_id
    if end > len(data) or row.size < _CLASS_TYPE_FROM_END:
        raise ValueError(f"character {character_id} runs past the end of characterstatic.dbss")
    if data[start + _TAG] != _TAG_VALUE:
        raise ValueError(f"character {character_id} record does not carry the 0x15 tag")

    action_script, pos = _read_script(data, start + _ACTION_SCRIPT, end, character_id)
    condition_script, pos = _read_script(data, pos, end, character_id)
    if pos + _FIXED_SIZE > end:
        raise ValueError(f"character {character_id} ends inside its fixed fields")
    if struct.unpack_from("<H", data, pos + _CHARACTER_ID)[0] != character_id:
        raise ValueError(f"character {character_id} record does not repeat its own ID")

    strings = _record_strings(data, pos + _FIXED_SIZE, end)
    return {
        "character_id": character_id,
        "action_script": action_script,
        "condition_script": condition_script,
        "knowledge_id": knowledge_id_of(action_script),
        "npc_kind": data[pos + _NPC_KIND],
        "grade": data[pos + _GRADE],
        "tendency_on_dead": _I32.unpack_from(data, pos + _TENDENCY_ON_DEAD)[0],
        "ocean_tendency": _I32.unpack_from(data, pos + _OCEAN_TENDENCY)[0],
        "vehicle_type": data[pos + _VEHICLE_TYPE],
        "class_type": data[end - _CLASS_TYPE_FROM_END],
        "source_item_id": _U32.unpack_from(data, end - _SOURCE_ITEM_FROM_END)[0],
        "ai_script": strings.ai_script,
        "model_path": strings.model_path,
        "name_kr": strings.name_kr,
        "label_kr": strings.label_kr,
        "title_kr": strings.title_kr,
        "payload_size": row.size,
    }


def parse_characterstatic_records(data: bytes, rows: list[PabrOffsetRow]) -> list[dict]:
    """Parse every record the offset table points at, in offset-table order.

    Raises ValueError on the first malformed record: after a bad script length
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
