"""`displayexchangeitemnpc.dbss`: the item exchange list each NPC dialog shows.

A u32 row count, then variable rows: the u16 NPC character key and u16 dialog
index (together the u32 `detail_dialog.dbss` key the index stores), a u64 count, that many u16
`itemexchangebynpc.dbss` keys, and the NPC key and dialog index again.
`displayexchangeitemnpcoffset.dbss` points 4 bytes into a row, at the count,
so the walk from the start needs no index. Layout 1 in
docs/file-formats/displayexchangeitemnpc_dbss.md.
"""

from __future__ import annotations

import struct

from _common.binary import u32


FILE_NAME = "displayexchangeitemnpc.dbss"
OFFSET_FILE = "displayexchangeitemnpcoffset.dbss"

_COUNT_SIZE = 4
# npc_character_key, dialog_index
_KEY = struct.Struct("<HH")
_LIST_COUNT = struct.Struct("<Q")
_EXCHANGE_KEY_SIZE = 2


def _parse_row(data: bytes, offset: int) -> tuple[dict, int]:
    """One row at `offset` and the offset after it.

    Raises ValueError when the row runs past the end of the file.
    """
    list_offset = offset + _KEY.size + _LIST_COUNT.size
    if list_offset > len(data):
        raise ValueError(f"row at 0x{offset:X} runs past the end of the file")
    npc_character_key, dialog_index = _KEY.unpack_from(data, offset)
    (item_exchange_count,) = _LIST_COUNT.unpack_from(data, offset + _KEY.size)

    tail_offset = list_offset + item_exchange_count * _EXCHANGE_KEY_SIZE
    end = tail_offset + _KEY.size
    if end > len(data):
        raise ValueError(
            f"row at 0x{offset:X} lists {item_exchange_count:,} exchanges and runs past the end of the file"
        )
    item_exchange_keys = list(struct.unpack_from(f"<{item_exchange_count}H", data, list_offset))
    npc_character_key_dup, dialog_index_dup = _KEY.unpack_from(data, tail_offset)
    record = {
        "npc_character_key": npc_character_key,
        "dialog_index": dialog_index,
        "item_exchange_count": item_exchange_count,
        "item_exchange_keys": item_exchange_keys,
        "npc_character_key_dup": npc_character_key_dup,
        "dialog_index_dup": dialog_index_dup,
    }
    return record, end


def parse_displayexchangeitemnpc_records(data: bytes) -> list[dict]:
    """Every row, in file order.

    Raises ValueError when the file is not the row count followed by exactly
    that many rows.
    """
    if len(data) < _COUNT_SIZE:
        raise ValueError(f"{FILE_NAME} is too short to hold its row count")

    count = u32(data, 0)
    records = []
    offset = _COUNT_SIZE
    for _ in range(count):
        record, offset = _parse_row(data, offset)
        records.append(record)
    if offset != len(data):
        raise ValueError(f"{count:,} rows end at 0x{offset:X}, the file is {len(data):,} bytes")
    return records
