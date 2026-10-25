"""`yachtdice.dbss`: the six cards on the faces of each Yar! die.

    u32 count | count x (u32 dice_key | u32 dice_key_dup | u32[6] card_keys)

`card_keys` are `yachtbasecard.dbss` keys; `yachtdiceoffset.dbss` points at
`dice_key_dup`. Layout in docs/file-formats/dbss/yachtdice_dbss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader
from _dbss.yacht_common.keyed_rows import parse_keyed_rows


FILE_NAME = "yachtdice.dbss"
OFFSET_FILE = "yachtdiceoffset.dbss"
KEY_FIELD = "dice_key"

FACES_PER_DIE = 6
_CARD_KEYS = struct.Struct(f"<{FACES_PER_DIE}I")


def _read_cards(reader: RecordReader) -> dict:
    return {"card_keys": list(reader.unpack(_CARD_KEYS))}


def parse_yachtdice_records(data: bytes) -> list[dict]:
    """Every die in file order. Raises ValueError when the rows do not fill the file."""
    return parse_keyed_rows(data, FILE_NAME, KEY_FIELD, _read_cards)
