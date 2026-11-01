"""`mentalcard.dbss`: knowledge cards, located through `mentalcardoffset.dbss`.

The offset file is `PABR`, a u32 count and 12-byte rows (`card_id`,
`data_offset`, `size`). Each record is a 33-byte header followed by a body:

    u32 card_id | u16 theme_id | u8 is_general | u8 is_developing_contents
    | f32 min_favor | f32 max_favor | f32 interest | u8 buff_type
    | f32 varied_value | u32 valid_turn | u32 apply_turn | name | description
    | u8 knowledge_type | u8 | u32 knowledge_level | icon_path | acquisition
    | f32[3] position | u8 u32 | u32 contents_group_count
    | contents_group_count x u32 contents group hash | zero end

The zero end is 5 bytes in Layout 2 (client 2098 on) and 4 bytes in Layout 1
(clients 1220 to 2089); every other field is the same. Nothing in the file
names its layout, so it is read with the first layout, in client order, whose
records all end at their index size. Strings are an i64 UTF-16 code-unit count
plus UTF-16LE text; the icon path is an i64 byte count plus ASCII. Full layout
in docs/file-formats/dbss/mentalcard_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.client_versions import ClientRange, client_order
from _common.pabr_offset import PabrOffsetRow, parse_pabr_u32_offset_rows
from _common.record_reader import RecordReader
from _common.ui_texture import ui_texture_path

_HEADER = struct.Struct("<IHBBfffBfII")
# u8 knowledge_type, u8 unknown_description_kr_01, u32 knowledge_level
_AFTER_DESCRIPTION = struct.Struct("<BBI")
_POSITION = struct.Struct("<fff")
# u8 unknown_acquisition_kr_0c, u32 unknown_acquisition_kr_0d, u32 contents_group_count
_TAIL_HEAD = struct.Struct("<BII")

FILE_NAME = "mentalcard.dbss"
# knowledge_type values: the client alerts a new Story card apart from the others.
KNOWLEDGE_TYPE_NORMAL = 0
KNOWLEDGE_TYPE_STORY = 1
# knowledge_level of a card with no world map step (an empty sheet cell).
NO_MAP_STEP = 5


@dataclass(frozen=True)
class CardLayout:
    """One documented Card shape; `number` is its Layout N in the doc."""

    number: int
    # Zero bytes after the hash list.
    end_size: int
    # Test clients this layout reads (the doc's Versions table, written by
    # check_docs); they only order the tries (`client_versions.py`).
    clients: tuple[ClientRange, ...] = ()


# Newest first.
LAYOUTS = (
    CardLayout(2, 5, clients=(ClientRange(2098),)),
    CardLayout(1, 4, clients=(ClientRange(1220, 2089),)),
)


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
    # KNOWLEDGE_TYPE_NORMAL or KNOWLEDGE_TYPE_STORY.
    knowledge_type: int
    # World map step that shows the card's position as `?`; NO_MAP_STEP for none.
    knowledge_level: int
    icon_path: str
    acquisition_kr: str
    position: tuple[float, float, float]
    contents_group_hashes: tuple[int, ...]


def parse_mentalcard_offset_records(data: bytes) -> list[PabrOffsetRow]:
    """Every index row in file order; `entry_id` is the card ID. Raises ValueError on a bad header."""
    return parse_pabr_u32_offset_rows(data)


def _parse_record(data: bytes, row: PabrOffsetRow, layout: CardLayout) -> MentalCardRecord:
    end = row.offset + row.size
    reader = RecordReader(data, row.offset, end, f"card {row.entry_id}")
    (
        card_id, theme_id, _is_general, _is_developing_contents, min_favor, max_favor, interest,
        buff_type, varied_value, valid_turn, apply_turn,
    ) = reader.unpack(_HEADER)
    if card_id != row.entry_id:
        raise ValueError(f"record at 0x{row.offset:X} holds card {card_id}, index says {row.entry_id}")

    name_kr = reader.text(wide=True)
    description_kr = reader.text(wide=True)
    knowledge_type, _unknown_01, knowledge_level = reader.unpack(_AFTER_DESCRIPTION)
    icon_path = reader.text(wide=False)
    acquisition_kr = reader.text(wide=True)
    position = reader.unpack(_POSITION)
    _unknown_0c, _unknown_0d, contents_group_count = reader.unpack(_TAIL_HEAD)
    contents_group_hashes = reader.unpack(struct.Struct(f"<{contents_group_count}I"))
    reader.skip(layout.end_size)
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
        knowledge_type=knowledge_type,
        knowledge_level=knowledge_level,
        icon_path=ui_texture_path(icon_path),
        acquisition_kr=acquisition_kr,
        position=position,
        contents_group_hashes=contents_group_hashes,
    )


def parse_mentalcard_records(data: bytes, offset_data: bytes) -> list[MentalCardRecord]:
    """One record per index row, in index order, read with the first layout that fits.

    Raises ValueError when no layout reads every record to exactly its index
    size, naming where each layout broke; later fields would be misread.
    """
    rows = parse_mentalcard_offset_records(offset_data)
    breaks: list[str] = []
    for layout in client_order(LAYOUTS, lambda layout: layout.clients):
        try:
            return [_parse_record(data, row, layout) for row in rows]
        except ValueError as error:
            breaks.append(f"Layout {layout.number}: {error}")
    raise ValueError(f"{FILE_NAME} fits no known layout ({'; '.join(breaks)})")
