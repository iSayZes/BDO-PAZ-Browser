"""`yachtbasecard.dbss`: the cards on the faces of the Yar! dice.

    u32 count | count x (u32 card_key | u32 card_key_dup | u8 symbol | u8 eye | str16 image_path)

`yachtbasecardoffset.dbss` points at `card_key_dup`. Layout in
docs/file-formats/yachtbasecard_dbss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader
from _dbss.yacht_common.keyed_rows import parse_keyed_rows


FILE_NAME = "yachtbasecard.dbss"
OFFSET_FILE = "yachtbasecardoffset.dbss"
KEY_FIELD = "card_key"

# symbol, eye
_CARD = struct.Struct("<BB")


def _read_card(reader: RecordReader) -> dict:
    symbol, eye = reader.unpack(_CARD)
    return {"symbol": symbol, "eye": eye, "image_path": reader.text(wide=True)}


def parse_yachtbasecard_records(data: bytes) -> list[dict]:
    """Every card in file order. Raises ValueError when a row runs past the file or the rows do not fill it."""
    return parse_keyed_rows(data, FILE_NAME, KEY_FIELD, _read_card)
