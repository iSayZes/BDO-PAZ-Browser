"""`characterstatic.dbss` records, located through `characterstaticoffset.dbss`.

Each offset row points just past a two-byte inline copy of the character ID.
The payload opens with two length-prefixed scripts, then the ID again:

    u8[8] header | u8 tag 0x15 | action_script | condition_script
    | u8 | u16 character_id | u16 | u32 npc_kind | ... model_path ...
    | ... | u8 class_type @ end-24 | u8[23]

Both scripts are an i64 UTF-16 code-unit count followed by UTF-16LE text. The
model path is an i64 byte count plus ASCII at no fixed offset, so it is found by
scanning; it is the only folder path among the record's ASCII strings.
Full layout in docs/file-formats/characterstatic_dbss.md.
"""

from __future__ import annotations

import struct

from _common.knowledge_script import knowledge_id_of
from _common.pabr_offset import PabrOffsetRow, parse_pabr_offset_rows
from _common.prefixed_string import find_prefixed_ascii

_TAG = 0x08
_TAG_VALUE = 0x15
_ACTION_SCRIPT = 0x09
# From the first byte after condition_script.
_CHARACTER_ID = 0x01
_NPC_KIND = 0x05
_AFTER_SCRIPTS_SIZE = _NPC_KIND + 4
# From the end of the payload.
_CLASS_TYPE_FROM_END = 24
# class_type on every row that is not a player character.
NO_CLASS_TYPE = 101

_I64 = struct.Struct("<q")


def _read_script(data: bytes, pos: int, end: int, character_id: int) -> tuple[str, int]:
    """Read an i64-prefixed UTF-16LE script; return it and the next position."""
    (length,) = _I64.unpack_from(data, pos)
    text_end = pos + _I64.size + 2 * length
    if length < 0 or text_end > end:
        raise ValueError(f"character {character_id} has a script that runs past its record")
    return data[pos + _I64.size:text_end].decode("utf-16-le"), text_end


def _model_path(data: bytes, start: int, end: int) -> str:
    """Longest folder path among the ASCII strings in `[start, end)`.

    The other strings are behaviour names such as `9999` or `Pet_Dog`.
    """
    paths = [text for text in find_prefixed_ascii(data, start, end) if "/" in text]
    return max(paths, key=len, default="")


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
    if pos + _AFTER_SCRIPTS_SIZE > end:
        raise ValueError(f"character {character_id} ends inside its fixed fields")
    if struct.unpack_from("<H", data, pos + _CHARACTER_ID)[0] != character_id:
        raise ValueError(f"character {character_id} record does not repeat its own ID")

    return {
        "character_id": character_id,
        "action_script": action_script,
        "condition_script": condition_script,
        "knowledge_id": knowledge_id_of(action_script),
        "npc_kind": struct.unpack_from("<I", data, pos + _NPC_KIND)[0],
        "class_type": data[end - _CLASS_TYPE_FROM_END],
        "model_path": _model_path(data, pos + _AFTER_SCRIPTS_SIZE, end),
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
