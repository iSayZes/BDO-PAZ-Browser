"""`detail_dialog.dbss`: NPC dialog trees, located through `detail_dialogoffset.dbss`.

The offset file is `PABR`, a u32 count and 12-byte rows (`key`, `offset`,
`size`); the key is `dialog_index << 16 | character_id`. In the data file every
record is preceded by a copy of its key, and walks as:

    u32 key | u16 text_id | ascii internal_name | ascii unknown_name_2
    | utf16 greeting | u32 n + n x (u8 contents_type, utf16 text)
    | u32 n + n x (utf16 condition, utf16 title, u32 dialog_button_type, utf16 text, utf16 action, u16 text_id)
    | u32 n + n x (utf16 condition, utf16 text, u16 text_id)
    | u64 n + n x u16 | u32 0

Strings are a u64 unit count plus UTF-16LE or ASCII. The Korean text is
localized in LOC type 39, keyed `(key, text_id, 0, field)`. Full layout in
docs/file-formats/detail_dialog_dbss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.lease import Lease
from _common.pabr_offset import PabrOffsetRow, parse_pabr_u32_offset_rows
from _common.record_reader import RecordReader
from .lease import parse_lease

_KEY_INDEX_SHIFT = 16
_CHARACTER_MASK = 0xFFFF

_U8 = struct.Struct("<B")
_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")
_U64 = struct.Struct("<Q")
_KEY_AND_TEXT_ID = struct.Struct("<IH")

# CppEnums.ContentsType from global_define_cpp_enum.luac, without the
# "Contents_" prefix: the NPC function a greeting line belongs to.
CONTENTS_TYPE_NAMES: tuple[str, ...] = (
    "Quest", "NewQuest", "Shop", "Skill", "Repair", "Auction", "Inn", "Warehouse",
    "IntimacyGame", "Stable", "Transfer", "Guild", "Explore", "DeliveryPerson",
    "Enchant", "Socket", "Awaken", "ReAwaken", "LordMenu", "Extract", "Temp",
    "TerritorySupply", "GuildShop", "ItemMarket", "Knowledge", "HelpDesk",
    "SupplyShop", "MinorLordMenu", "FishSupplyShop", "Join", "GuildSupplyShop",
    "Improve", "NpcGift", "WeakenEnchant", "DiceGame", "NewItemMarket", "Barter",
    "Employee", "Talk", "Exchange", "Temp1", "MainQuest", "NewMainQuest",
    "SeasonReward", "Wanted", "Crew", "YachtDice", "OldMoonSmelting", "PetUpgrade",
)

# CppEnums.DialogButtonType, without the "eDialogButton_" prefix and the
# closing _Count. Options with an empty action store 99, outside the enum.
DIALOG_BUTTON_TYPE_NAMES: tuple[str, ...] = (
    "Normal", "Knowledge", "Function", "CutScene", "Exchange", "ExceptExchange",
    "TimeAttack", "Sequence",
)


@dataclass(frozen=True)
class GreetingLine:
    contents_type: int
    text: str


@dataclass(frozen=True)
class DialogOption:
    condition: str
    title: str
    dialog_button_type: int
    text: str
    action: str
    text_id: int

    @property
    def lease(self) -> Lease | None:
        return parse_lease(self.action)


@dataclass(frozen=True)
class ConditionalGreeting:
    condition: str
    text: str
    text_id: int


@dataclass(frozen=True)
class DialogRecord:
    key: int
    text_id: int
    internal_name: str
    unknown_name_2: str
    greeting: str
    lines: tuple[GreetingLine, ...]
    options: tuple[DialogOption, ...]
    conditionals: tuple[ConditionalGreeting, ...]
    unknown_list: tuple[int, ...]

    @property
    def character_id(self) -> int:
        return self.key & _CHARACTER_MASK

    @property
    def dialog_index(self) -> int:
        return self.key >> _KEY_INDEX_SHIFT


def split_key(key: int) -> tuple[int, int]:
    """`(character_id, dialog_index)` of a dialog key."""
    return key & _CHARACTER_MASK, key >> _KEY_INDEX_SHIFT


def parse_detail_dialog_offset_rows(data: bytes) -> list[PabrOffsetRow]:
    """Every index row in file order; `entry_id` is the dialog key."""
    return parse_pabr_u32_offset_rows(data)


def _count(reader: RecordReader, fmt: struct.Struct = _U32) -> int:
    (count,) = reader.unpack(fmt)
    return count


def _read_option(reader: RecordReader) -> DialogOption:
    condition = reader.text(wide=True)
    title = reader.text(wide=True)
    (dialog_button_type,) = reader.unpack(_U32)
    text = reader.text(wide=True)
    action = reader.text(wide=True)
    (text_id,) = reader.unpack(_U16)
    return DialogOption(condition, title, dialog_button_type, text, action, text_id)


def _read_conditional(reader: RecordReader) -> ConditionalGreeting:
    condition = reader.text(wide=True)
    text = reader.text(wide=True)
    (text_id,) = reader.unpack(_U16)
    return ConditionalGreeting(condition, text, text_id)


def _read_line(reader: RecordReader) -> GreetingLine:
    (contents_type,) = reader.unpack(_U8)
    return GreetingLine(contents_type, reader.text(wide=True))


def parse_detail_dialog_record(data: bytes, row: PabrOffsetRow) -> DialogRecord:
    """Walk one record. Raises ValueError when it does not end at its index size."""
    label = f"dialog 0x{row.entry_id:08X}"
    reader = RecordReader(data, row.offset, row.offset + row.size, label)
    key, text_id = reader.unpack(_KEY_AND_TEXT_ID)
    if key != row.entry_id:
        raise ValueError(f"record at 0x{row.offset:X} holds key 0x{key:08X}, index says 0x{row.entry_id:08X}")

    internal_name = reader.text(wide=False)
    unknown_name_2 = reader.text(wide=False)
    greeting = reader.text(wide=True)
    lines = tuple(_read_line(reader) for _ in range(_count(reader)))
    options = tuple(_read_option(reader) for _ in range(_count(reader)))
    conditionals = tuple(_read_conditional(reader) for _ in range(_count(reader)))
    list_count = _count(reader, _U64)
    if list_count > reader.remaining():
        raise ValueError(f"{label} declares {list_count:,} list values past its record")
    unknown_list = tuple(reader.unpack(_U16)[0] for _ in range(list_count))
    reader.skip(_U32.size)  # always 0
    if not reader.at_end():
        raise ValueError(f"{label} ends {reader.remaining()} bytes before its index size")

    return DialogRecord(
        key=key,
        text_id=text_id,
        internal_name=internal_name,
        unknown_name_2=unknown_name_2,
        greeting=greeting,
        lines=lines,
        options=options,
        conditionals=conditionals,
        unknown_list=unknown_list,
    )


def parse_detail_dialog_records(data: bytes, offset_data: bytes) -> list[DialogRecord]:
    """One record per index row, in index order.

    Raises ValueError on the first record that does not end exactly at its
    index size: the layout has changed and later fields would be misread.
    """
    return [parse_detail_dialog_record(data, row) for row in parse_detail_dialog_offset_rows(offset_data)]


def build_character_lease_index(data: bytes, offset_data: bytes) -> dict[int, tuple[int, ...]]:
    """Map character ID to its lease options as flat `(item_id, cost, ...)` pairs.

    Pairs keep dialog order (dialog index, then option order) and each
    `(item, cost)` appears once. A malformed record is skipped rather than
    failing the whole index: the preview of this table reports it instead.
    """
    leases: dict[int, dict[tuple[int, int], None]] = {}
    rows = sorted(parse_detail_dialog_offset_rows(offset_data), key=lambda row: split_key(row.entry_id))
    for row in rows:
        try:
            record = parse_detail_dialog_record(data, row)
        except (ValueError, struct.error):
            continue
        for option in record.options:
            lease = option.lease
            if lease is not None:
                leases.setdefault(record.character_id, {})[(lease.item_id, lease.cost)] = None

    return {
        character_id: tuple(value for pair in pairs for value in pair)
        for character_id, pairs in leases.items()
    }
