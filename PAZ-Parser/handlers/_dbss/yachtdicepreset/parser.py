"""`yachtdicepreset.dbss`: the five dice of each Yar! dice preset.

    u32 count | count x (u32 dice_preset_key | u32 dice_preset_key_dup | u32[5] dice_keys)

`yachtdicepresetoffset.dbss` points at `dice_preset_key_dup`. Layout in
docs/file-formats/yachtdicepreset_dbss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader
from _dbss.yacht_common.keyed_rows import parse_keyed_rows


FILE_NAME = "yachtdicepreset.dbss"
OFFSET_FILE = "yachtdicepresetoffset.dbss"
KEY_FIELD = "dice_preset_key"

DICE_PER_PRESET = 5
_DICE_KEYS = struct.Struct(f"<{DICE_PER_PRESET}I")


def _read_dice(reader: RecordReader) -> dict:
    return {"dice_keys": list(reader.unpack(_DICE_KEYS))}


def parse_yachtdicepreset_records(data: bytes) -> list[dict]:
    """Every preset in file order. Raises ValueError when the rows do not fill the file."""
    return parse_keyed_rows(data, FILE_NAME, KEY_FIELD, _read_dice)


def dice_keys_by_preset(data: bytes | None) -> dict[int, list[int]]:
    """The dice keys of every preset by preset key; empty when the file is missing.

    Raises ValueError when the file does not parse.
    """
    if data is None:
        return {}
    return {record[KEY_FIELD]: record["dice_keys"] for record in parse_yachtdicepreset_records(data)}
