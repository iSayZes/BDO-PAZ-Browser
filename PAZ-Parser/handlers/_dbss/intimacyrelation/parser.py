"""`intimacyrelation.dbss`: the first meeting with each NPC, keyed by NPC character key.

    u32 count | count x (u16 key_prefix | row)
    row: u16 npc_key | str16 covered_dialog_kr | str8 discover_cutscene
         | str16 discover_dialog_kr | str16 discover_function
         | str16[5] discover_conditions | str16[5] discover_dialogs_kr
         | u32 unknown_discover_dialogs_kr_00

`key_prefix` repeats `npc_key`. `intimacyrelationoffset.dbss` (u32 count,
then u16 key, u32 offset and u32 size per row, no PABR magic) points past
the key prefix. Layout 3 in docs/file-formats/intimacyrelation_dbss.md;
clients with `npc_importance` (Layout 2) or without the key prefix
(Layout 1) are not read.
"""

from __future__ import annotations

import re
import struct

from _common.counted_rows import read_counted_records
from _common.pabr_offset import PabrOffsetRow, parse_bare_offset_rows
from _common.record_reader import RecordReader


FILE_NAME = "intimacyrelation.dbss"
OFFSET_FILE = "intimacyrelationoffset.dbss"
KEY_FIELD = "npc_key"
# discover_conditions and discover_dialogs_kr hold this many strings each.
DIALOG_LINE_COUNT = 5

_HEAD = struct.Struct("<HH")
_U32 = struct.Struct("<I")
# `Pushknowledge(<knowledge key>,0)`, spelled in three cases.
_PUSH_KNOWLEDGE = re.compile(r"pushknowledge\((\d+)\s*,", re.IGNORECASE)


def _read_texts(reader: RecordReader) -> list[str]:
    return [reader.text(wide=True) for _ in range(DIALOG_LINE_COUNT)]


def _read_row(reader: RecordReader) -> dict:
    key_prefix, npc_key = reader.unpack(_HEAD)
    if key_prefix != npc_key:
        raise ValueError(f"{FILE_NAME} row {npc_key} follows the key prefix {key_prefix}")
    covered_dialog_kr = reader.text(wide=True)
    discover_cutscene = reader.text(wide=False)
    discover_dialog_kr = reader.text(wide=True)
    discover_function = reader.text(wide=True)
    discover_conditions = _read_texts(reader)
    discover_dialogs_kr = _read_texts(reader)
    (unknown_discover_dialogs_kr_00,) = reader.unpack(_U32)
    return {
        KEY_FIELD: npc_key,
        "covered_dialog_kr": covered_dialog_kr,
        "discover_cutscene": discover_cutscene,
        "discover_dialog_kr": discover_dialog_kr,
        "discover_function": discover_function,
        "discover_conditions": discover_conditions,
        "discover_dialogs_kr": discover_dialogs_kr,
        "unknown_discover_dialogs_kr_00": unknown_discover_dialogs_kr_00,
    }


def parse_intimacyrelation_records(data: bytes) -> list[dict]:
    """Every NPC row in file order.

    Raises ValueError when a row runs past the file, its key prefix differs
    from its key, or the rows end before the last byte.
    """
    return read_counted_records(data, _read_row, FILE_NAME)


def parse_intimacyrelationoffset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row: NPC key, row offset and row size. Raises ValueError on a count the file cannot hold."""
    return parse_bare_offset_rows(data)


def knowledge_key_of(discover_function: str) -> int | None:
    """The knowledge key a `Pushknowledge(<key>,0)` script grants, or None for any other script."""
    match = _PUSH_KNOWLEDGE.search(discover_function)
    return int(match.group(1)) if match else None
