"""`plantupgradeparam.bss`: upgrade parameter groups of the worker system.

    PABR | u32 count | count x 6-byte entry | u32 0 (empty string table)
    | u32 string_table_start | u32 0

Each entry is a map key, the same key again and the group's highest upgrade
level. Full layout in docs/file-formats/plantupgradeparam_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets


FILE_NAME = "plantupgradeparam.bss"
ROW_SIZE = 6


def parse_plantupgradeparam_records(data: bytes) -> list[dict]:
    """Every entry in file order. Raises ValueError on a bad magic or row count."""
    records: list[dict] = []
    for pos in fixed_row_offsets(data, ROW_SIZE, FILE_NAME):
        key, param_key, max_level = struct.unpack_from("<HHh", data, pos)
        records.append({"key": key, "param_key": param_key, "max_level": max_level})
    return records
