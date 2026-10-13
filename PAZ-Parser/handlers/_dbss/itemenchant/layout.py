"""The variable-length parts of an itemenchant.dbss block, read front to back.

Two counted parts move everything after them (itemenchant_dbss.md, Block
Structure):

- `unknown_5d`, a u32 count and that many bytes inside the header. Every header
  field after it moves by the count, so `header_shift` returns it; the parser
  adds it to the offsets of those fields.
- The lists between the header and the strings: two lists of 5-byte entries,
  4 bytes, a list of u32, then `enchant_key`, the Korean name and the icon path.
"""

from __future__ import annotations

import struct
from typing import NamedTuple

from _common.prefixed_string import read_prefixed_at


# u32 count, then that many bytes; 0 in all blocks but servant gear.
_UNKNOWN_5D = 0x5D

# Where the header ends in a block whose `unknown_5d` is empty.
HEADER_END = 0xD4

# The walk runs once per block of a 194 MB file, so it reads with the struct
# directly instead of the bounds-checked `_common.binary.u32`.
_U32 = struct.Struct("<I").unpack_from

_COUNT_SIZE = 4
# The two lists after the header: a class type (u8) and a u32 per entry in the
# first, entries of the same size in the second.
_ENTRY_SIZE = 5
# Between the second list and the u32 list.
_GAP_SIZE = 4
_VALUE_SIZE = 4
_ENCHANT_KEY_SIZE = 4


class BlockStrings(NamedTuple):
    # The enchantstaticstatus.dbss key; 0 when the item has no enhancement data.
    enchant_key: int
    name_kr: str
    # As stored, relative to `ui_texture/icon/`.
    icon: str
    # Where the icon text ends; the fields after the icon count from here.
    icon_end: int


def header_shift(data: bytes, start: int) -> int:
    """How far the header fields after `unknown_5d` sit from their usual offset."""
    return _U32(data, start + _UNKNOWN_5D)[0]


def _skip_list(data: bytes, pos: int, entry_size: int) -> int:
    """Where the field after the u32-counted list at `pos` starts."""
    return pos + _COUNT_SIZE + entry_size * _U32(data, pos)[0]


def read_block_strings(data: bytes, start: int, end: int) -> BlockStrings:
    """Walk the block `[start, end)` from the end of its header to the end of its icon.

    The block must lie inside `data`. Raises ValueError when a count runs the
    walk past the block, since the name and icon would then be read from the
    wrong place.
    """
    try:
        pos = start + HEADER_END + header_shift(data, start)
        pos = _skip_list(data, pos, _ENTRY_SIZE)
        pos = _skip_list(data, pos, _ENTRY_SIZE)
        pos = _skip_list(data, pos + _GAP_SIZE, _VALUE_SIZE)
    except struct.error as error:
        raise ValueError(f"block at 0x{start:X}: the lists run past the file") from error
    if pos + _ENCHANT_KEY_SIZE > end:
        raise ValueError(f"block at 0x{start:X}: the lists run past its end")

    enchant_key = _U32(data, pos)[0]
    name_kr, pos = read_prefixed_at(data, pos + _ENCHANT_KEY_SIZE, end, wide=True)
    icon, icon_end = read_prefixed_at(data, pos, end, wide=False)
    return BlockStrings(enchant_key, name_kr, icon, icon_end)
