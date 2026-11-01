"""`yachtdicecard.dbss`: Yar! cards with a symbol and an eye value from 1 to 10.

    u32 count | count x (u32 card_key | u32 card_key_dup | u8 symbol | u8 eye)

`yachtdicecardoffset.dbss` points at `card_key_dup`. Layout in
docs/file-formats/dbss/yachtdicecard_dbss.md.
"""

from __future__ import annotations

import struct

from _common.record_reader import RecordReader
from _dbss.yacht_common.keyed_rows import parse_keyed_rows


FILE_NAME = "yachtdicecard.dbss"
OFFSET_FILE = "yachtdicecardoffset.dbss"
KEY_FIELD = "card_key"

# symbol, eye
_CARD = struct.Struct("<BB")


def _read_card(reader: RecordReader) -> dict:
    symbol, eye = reader.unpack(_CARD)
    return {"symbol": symbol, "eye": eye}


def parse_yachtdicecard_records(data: bytes) -> list[dict]:
    """Every card in file order. Raises ValueError when the rows do not fill the file."""
    return parse_keyed_rows(data, FILE_NAME, KEY_FIELD, _read_card)
