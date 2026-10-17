"""`extractitem.dbss`: Extract Reform Stone, reformed gear split back apart.

A u32 row count, then 48-byte rows back to back to the end of the file. A row
is four slots of a u32 item ID and its u64 count: the reformed item, the
item the extraction uses up, the gear returned and the reform stone
returned. `extractitemoffset.dbss` points at each row's
`item_id`, so the walk from the start needs no index. Layout in
docs/file-formats/extractitem_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "extractitem.dbss"
OFFSET_FILE = "extractitemoffset.dbss"

_COUNT_SIZE = 4
ROW = struct.Struct("<IQIQIQIQ")


def parse_extractitem_records(data: bytes) -> list[dict]:
    """Every extraction row, in file order.

    Raises ValueError when the file is not exactly its count of rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    expected_size = _COUNT_SIZE + count * ROW.size
    if len(data) != expected_size:
        raise ValueError(
            f"{FILE_NAME} declares {count:,} rows of {ROW.size} bytes "
            f"({expected_size:,} bytes) but is {len(data):,} bytes"
        )

    return [
        _record(row)
        for row in ROW.iter_unpack(data[_COUNT_SIZE:expected_size])
    ]


def _record(row: tuple[int, ...]) -> dict:
    (
        item_id, item_count,
        need_item_id, need_item_count,
        result_item_id, result_item_count,
        result_material_id, result_material_count,
    ) = row
    return {
        "item_id": item_id,
        "need_item_id": need_item_id,
        "result_item_id": result_item_id,
        "result_material_id": result_material_id,
        "item_count": item_count,
        "need_item_count": need_item_count,
        "result_item_count": result_item_count,
        "result_material_count": result_material_count,
    }
