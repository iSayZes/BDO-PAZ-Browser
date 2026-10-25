"""`explorepointexperiencenew.bss`: the contribution EXP a character needs for
one more contribution point, by the points it already holds.

    u32 row_count | row_count x (u16 contribution_points, u64 exp)

No PABR magic and no trailer: the rows fill the file. Full layout in
docs/file-formats/bss/explorepointexperiencenew_bss.md.
"""

from __future__ import annotations

import struct


FILE_NAME = "explorepointexperiencenew.bss"
_COUNT = struct.Struct("<I")
_ROW = struct.Struct("<HQ")


def parse_explorepointexperience_records(data: bytes) -> list[dict]:
    """One record per row, in file order (ascending `contribution_points`).

    Raises ValueError when the file is not exactly the declared rows.
    """
    if len(data) < _COUNT.size:
        raise ValueError(f"{FILE_NAME} is too short for its row count")
    (row_count,) = _COUNT.unpack_from(data)
    expected = _COUNT.size + row_count * _ROW.size
    if len(data) != expected:
        raise ValueError(
            f"{FILE_NAME} declares {row_count} rows ({expected} bytes) but holds {len(data)} bytes"
        )
    return [
        {"contribution_points": points, "exp": exp}
        for points, exp in _ROW.iter_unpack(data[_COUNT.size :])
    ]
