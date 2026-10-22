"""`seasonreward.dbss`: the reward items of each Season server season.

    u32 count | count x row
    row: u8 season_no | str16 season_name_key | str16 description_key
         | u32 reward_count | reward_count x u32 reward_item_keys

The two keys are `GAME` string sheet keys (`LUA_SEASONSERVER_NAME15`); each
reward is a packed item key. Layout 1 in docs/file-formats/seasonreward_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records, read_counted_u32s
from _common.record_reader import RecordReader


FILE_NAME = "seasonreward.dbss"
KEY_FIELD = "season_no"

_SEASON_NO = struct.Struct("<B")


def _read_row(reader: RecordReader) -> dict:
    (season_no,) = reader.unpack(_SEASON_NO)
    return {
        KEY_FIELD: season_no,
        "season_name_key": reader.text(wide=True),
        "description_key": reader.text(wide=True),
        "reward_item_keys": read_counted_u32s(reader, f"{FILE_NAME} reward"),
    }


def parse_seasonreward_records(data: bytes) -> list[dict]:
    """Every row in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)
