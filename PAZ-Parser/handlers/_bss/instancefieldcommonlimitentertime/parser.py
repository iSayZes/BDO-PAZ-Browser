"""`instancefieldcommonlimitentertime.bss`: per game service, seven hour pairs per entry.

    u32 count | count x Row
    Row: u8 service_type | u32 group_count | group_count x Group
    Group: u32 unknown_group_key | u32 entry_count | entry_count x Entry
    Entry: u16 unknown_00 | u16 unknown_02 | u8 unknown_04 | u8 unknown_05
           | u8 unknown_06[7][2]

`service_type` is a `CppEnums.GameServiceType` value. The parser returns one
record per Entry with its row's and group's keys. Layout 1 in
docs/file-formats/instancefieldcommonlimitentertime_bss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32
from _common.record_reader import RecordReader


FILE_NAME = "instancefieldcommonlimitentertime.bss"

DAY_COUNT = 7
_COUNT_SIZE = 4
_ROW_HEAD = struct.Struct("<BI")
_GROUP_HEAD = struct.Struct("<II")
_ENTRY = struct.Struct(f"<HHBB{DAY_COUNT * 2}B")

# `CppEnums.GameServiceType` of the client Lua (`global_define_cpp_enum.luac`).
GAME_SERVICE_TYPES = {
    0: "NONE", 1: "DEV", 2: "KOR_ALPHA", 3: "KOR_REAL", 4: "KOR_TEST",
    5: "JPN_ALPHA", 6: "JPN_REAL", 7: "RUS_ALPHA", 8: "RUS_REAL",
    9: "KR2_ALPHA", 10: "KR2_REAL", 11: "NA_ALPHA", 12: "NA_REAL",
    13: "TW_ALPHA", 14: "TW_REAL", 15: "SA_ALPHA", 16: "SA_REAL",
    17: "TH_ALPHA", 18: "TH_REAL", 19: "ID_ALPHA", 20: "ID_REAL",
    21: "TR_ALPHA", 22: "TR_REAL", 23: "PS_ALPHA", 24: "PS_REAL",
    25: "XB_ALPHA", 26: "XB_REAL", 27: "GT_ALPHA", 28: "GT_REAL",
    29: "XX_ALPHA", 30: "XX_REAL", 33: "CS_ALPHA", 34: "CS_REAL",
    35: "ASIA_ALPHA", 36: "ASIA_REAL",
}


def _read_entry(reader: RecordReader, service_type: int, group_key: int) -> dict:
    unknown_00, unknown_02, unknown_04, unknown_05, *days = reader.unpack(_ENTRY)
    return {
        "service_type": service_type,
        "unknown_group_key": group_key,
        "unknown_00": unknown_00,
        "unknown_02": unknown_02,
        "unknown_04": unknown_04,
        "unknown_05": unknown_05,
        "unknown_06": [days[i:i + 2] for i in range(0, len(days), 2)],
    }


def parse_instancefieldcommonlimitentertime_records(data: bytes) -> list[dict]:
    """Every entry of every group of every row, in file order.

    Raises ValueError when a row runs past the file or the rows do not end at
    its last byte.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    reader = RecordReader(data, _COUNT_SIZE, len(data), FILE_NAME)
    records = []
    for _ in range(u32(data, 0)):
        service_type, group_count = reader.unpack(_ROW_HEAD)
        for _ in range(group_count):
            group_key, entry_count = reader.unpack(_GROUP_HEAD)
            records.extend(_read_entry(reader, service_type, group_key) for _ in range(entry_count))
    if not reader.at_end():
        raise ValueError(f"{FILE_NAME} has {reader.remaining():,} bytes after its last row")
    return records
