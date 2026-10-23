"""`instancefieldranking.bss`: the season rankings of each instance field type.

    PABR | u32 record_count | record_count x Row | String Table (empty)
    | u32 string_table_start | u32 0
    Row: u16 instance_field_type | u32 ranking_count | u32[ranking_count] ranking_idxs

`ranking_idxs` are `ranking_idx` keys of `instancefieldrankingmanage.bss`.
Layout 1 in docs/file-formats/instancefieldranking_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.pabr_strings import HEADER_SIZE, check_rows_end, checked_string_table_start
from _common.record_reader import RecordReader


FILE_NAME = "instancefieldranking.bss"
_COUNT_OFFSET = 4
_HEAD = struct.Struct("<HI")


def _read_row(reader: RecordReader) -> dict:
    instance_field_type, ranking_count = reader.unpack(_HEAD)
    return {
        "instance_field_type": instance_field_type,
        "ranking_count": ranking_count,
        "ranking_idxs": list(reader.unpack(struct.Struct(f"<{ranking_count}I"))),
    }


def parse_instancefieldranking_records(data: bytes) -> list[dict]:
    """Every row in file order.

    Raises ValueError on a missing magic, a row that runs past the string
    table, or rows that end before it.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, HEADER_SIZE, end, FILE_NAME)
    records = [_read_row(reader) for _ in range(u32(data, _COUNT_OFFSET))]
    check_rows_end(data, reader.pos, f"{FILE_NAME} rows")
    return records
