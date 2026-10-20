"""`nodeexperience.bss`: the EXP a node needs from one node level to the next.

    PABR | u32 row_count | row_count x 15-byte row | 12-byte PABR trailer
    row = u8 is_integrity | u32 node_exp_type | i16 level | i64 exp

The row is the 2016 client's `gc::NodeExperienceStaticStatus` with its
padding left out (`_isIntegrity`, `_nodeExpType`, `_nodeLevel`,
`_requiredExperience`).

The trailer's middle u32 is the end of the rows. Full layout in
docs/file-formats/nodeexperience_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_offset import PABR_MAGIC


FILE_NAME = "nodeexperience.bss"
_COUNT = struct.Struct("<I")
ROWS_START = len(PABR_MAGIC) + _COUNT.size
ROW = struct.Struct("<BIhq")
TRAILER = struct.Struct("<III")


def parse_nodeexperience_records(data: bytes) -> list[dict]:
    """One record per node level, in file order (level 0 first).

    Raises ValueError on a bad magic, or when the declared rows do not end
    where the trailer says: then the row size has changed and every field is
    suspect.
    """
    if len(data) < ROWS_START + TRAILER.size or data[: len(PABR_MAGIC)] != PABR_MAGIC:
        raise ValueError(f"{FILE_NAME}: missing PABR magic")
    (row_count,) = _COUNT.unpack_from(data, len(PABR_MAGIC))
    rows_end = ROWS_START + row_count * ROW.size
    _, end_of_data, _ = TRAILER.unpack_from(data, len(data) - TRAILER.size)
    if rows_end != end_of_data or end_of_data != len(data) - TRAILER.size:
        raise ValueError(
            f"{FILE_NAME}: {row_count} rows of {ROW.size} bytes end at {rows_end}, "
            f"but the trailer says {end_of_data} and the file holds {len(data)} bytes"
        )
    return [
        {"level": level, "exp": exp, "is_integrity": is_integrity, "node_exp_type": node_exp_type}
        for is_integrity, node_exp_type, level, exp in ROW.iter_unpack(data[ROWS_START:rows_end])
    ]
