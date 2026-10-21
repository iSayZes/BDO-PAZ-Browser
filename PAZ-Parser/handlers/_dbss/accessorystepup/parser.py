"""`accessorystepup.dbss`: the accessory step-up, five steps of materials per accessory.

    u32 count | count x (u32 item_key | u8 group_no | u8 accessory_index
                         | 5 steps x 5 materials x (u32 item_key | u64 need_count))

Step N (from 0) enhances the accessory to level N + 1. The file has no
offset index. Layout 1 in docs/file-formats/accessorystepup_dbss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import counted_row_values


FILE_NAME = "accessorystepup.dbss"

STEP_COUNT = 5
MATERIAL_COUNT = 5
_HEAD_FIELDS = ("item_key", "group_no", "accessory_index")
_ROW = struct.Struct("<IBB" + "Iq" * (STEP_COUNT * MATERIAL_COUNT))
_VALUES_PER_STEP = 2 * MATERIAL_COUNT


def _step(values: tuple, step: int) -> list[dict]:
    """The materials of one step, from the values after the row head."""
    start = step * _VALUES_PER_STEP
    pairs = values[start : start + _VALUES_PER_STEP]
    return [{"item_key": pairs[i], "need_count": pairs[i + 1]} for i in range(0, len(pairs), 2)]


def parse_accessorystepup_records(data: bytes) -> list[dict]:
    """Every row in file order, its steps as lists of materials.

    Raises ValueError when the rows do not fill the file.
    """
    records = []
    for values in counted_row_values(data, _ROW, FILE_NAME):
        head, materials = values[: len(_HEAD_FIELDS)], values[len(_HEAD_FIELDS) :]
        records.append(
            {
                **dict(zip(_HEAD_FIELDS, head, strict=True)),
                "steps": [_step(materials, step) for step in range(STEP_COUNT)],
            }
        )
    return records
