"""The row shape every keyed Yar! `.dbss` table shares.

    u32 count | count x (u32 key | u32 key_dup | payload)

`yachtdicepreset.dbss`, `yachtdice.dbss`, `yachtdicecard.dbss`,
`yachtbasecard.dbss` and `yachtclasstypetextureinfo.dbss` write each row's
key twice; their `*offset.dbss` index points at the second copy, so the
rows can be walked from the count without it. Only the payload differs per
table. Layouts in docs/file-formats/yacht*_dbss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Callable

from _common.binary import u32
from _common.record_reader import RecordReader


COUNT_SIZE = 4
# key, key_dup
_KEYS = struct.Struct("<II")

ReadPayload = Callable[[RecordReader], dict]


def parse_keyed_rows(data: bytes, file_name: str, key_field: str, read_payload: ReadPayload) -> list[dict]:
    """Every row in file order: `key_field`, `<key_field>_dup` and the payload fields.

    `read_payload` reads one row's fields after the two keys. Raises
    ValueError when a row runs past the file or the rows do not end at its
    last byte.
    """
    if len(data) < COUNT_SIZE:
        raise ValueError(f"{file_name} is too short to hold its row count")

    count = u32(data, 0)
    reader = RecordReader(data, COUNT_SIZE, len(data), file_name)
    records: list[dict] = []
    for _ in range(count):
        key, key_dup = reader.unpack(_KEYS)
        records.append({key_field: key, f"{key_field}_dup": key_dup, **read_payload(reader)})
    if not reader.at_end():
        raise ValueError(f"{file_name} has {reader.remaining():,} bytes after its {count:,} rows")
    return records
