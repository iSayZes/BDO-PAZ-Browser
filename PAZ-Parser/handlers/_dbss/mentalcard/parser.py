"""`mentalcard.dbss`: knowledge cards, located through `mentalcardoffset.dbss`.

The offset file is `PABR`, a u32 count and 12-byte rows (`card_id`,
`data_offset`, `size`). Each record is a 33-byte header followed by a body:

    u32 card_id | u16 theme_id | u8 u8 | f32 min_favor | f32 max_favor
    | f32 interest | u8 buff_type | f32 varied_value | u32 valid_turn | u32 apply_turn
    | name | description | u8 u8 u32 | icon_path | acquisition | f32[3] position
    | u8 u32 | u32 hash_count + hash_count x u32 | u8[5]

Strings are an i64 UTF-16 code-unit count plus UTF-16LE text; the icon path is
an i64 byte count plus ASCII. Full layout in docs/file-formats/mentalcard_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.pabr_offset import PabrOffsetRow, parse_pabr_u32_offset_rows
from _common.record_reader import RecordReader

_HEADER = struct.Struct("<IHBBfffBfII")
# u8 unknown_description_kr_00, u8 unknown_description_kr_01, u32 unknown_description_kr_02
_BODY_FLAGS_SIZE = 6
_POSITION = struct.Struct("<fff")
# u8 unknown_acquisition_kr_0c, u32 unknown_acquisition_kr_0d, u32 hash_count
_TAIL_HEAD = struct.Struct("<BII")
_PADDING_SIZE = 5

# Stored icon paths start at "UI_Artwork/", which hangs off ui_texture.
ICON_ROOT = "ui_texture/"


@dataclass(frozen=True)
class MentalCardRecord:
    card_id: int
    theme_id: int
    min_favor: float
    max_favor: float
    interest: float
    # Combo effect; buff_type 4 means no combo, see combo.py.
    buff_type: int
    varied_value: float
    valid_turn: int
    apply_turn: int
    name_kr: str
    description_kr: str
    icon_path: str
    acquisition_kr: str
    position: tuple[float, float, float]


def parse_mentalcard_offset_records(data: bytes) -> list[PabrOffsetRow]:
    """Every index row in file order; `entry_id` is the card ID. Raises ValueError on a bad header."""
    return parse_pabr_u32_offset_rows(data)


def _parse_record(data: bytes, row: PabrOffsetRow) -> MentalCardRecord:
    end = row.offset + row.size
    reader = RecordReader(data, row.offset, end, f"card {row.entry_id}")
    (
        card_id, theme_id, _flag_a, _flag_b, min_favor, max_favor, interest,
        buff_type, varied_value, valid_turn, apply_turn,
    ) = reader.unpack(_HEADER)
    if card_id != row.entry_id:
        raise ValueError(f"record at 0x{row.offset:X} holds card {card_id}, index says {row.entry_id}")

    name_kr = reader.text(wide=True)
    description_kr = reader.text(wide=True)
    reader.skip(_BODY_FLAGS_SIZE)
    icon_path = reader.text(wide=False)
    acquisition_kr = reader.text(wide=True)
    position = reader.unpack(_POSITION)
    _kind, _value, hash_count = reader.unpack(_TAIL_HEAD)
    reader.skip(4 * hash_count + _PADDING_SIZE)
    if not reader.at_end():
        raise ValueError(f"card {card_id} ends {reader.remaining()} bytes before its index size")

    return MentalCardRecord(
        card_id=card_id,
        theme_id=theme_id,
        min_favor=min_favor,
        max_favor=max_favor,
        interest=interest,
        buff_type=buff_type,
        varied_value=varied_value,
        valid_turn=valid_turn,
        apply_turn=apply_turn,
        name_kr=name_kr,
        description_kr=description_kr,
        icon_path=f"{ICON_ROOT}{icon_path.lower()}" if icon_path else "",
        acquisition_kr=acquisition_kr,
        position=position,
    )


def parse_mentalcard_records(data: bytes, offset_data: bytes) -> list[MentalCardRecord]:
    """One record per index row, in index order.

    Raises ValueError on the first record that does not end exactly at its
    index size: the layout has changed and later fields would be misread.
    """
    return [_parse_record(data, row) for row in parse_mentalcard_offset_records(offset_data)]
