"""`palacemanagementstaticstatus.bss`: the palace management board groups, their boards and items.

    PABR | u32 group_count | group_count x Board Group
    | u32 production_board_count | production_board_count x Production Board
    | u32 manufacture_board_count | manufacture_board_count x Manufacture Board
    | 6 x u16 | u32 nation_count | nation_count x (u32 nation_code_ref | u16)
    | string table | u32 table_start | u32 0
    Board Group: u16 board_group_key | u32 board_group_name_ref | u32 texture_ref
        | u32 desc_ref | u8 board_group_type | u16 npc_character_key
        | u16 npc_dialog_index | u32 board_count | board_count x (u16 board_key | u8)
    Production Board: u16 board_key | u32 board_name_ref | u32 item_count
        | item_count x (u16 item_index | u32 probability | u32 exchange_key)
    Manufacture Board: u16 board_key | u32 board_name_ref | u32 item_count
        | item_count x (u16 item_index | u32 exchange_key)

Full layout in docs/file-formats/palacemanagementstaticstatus_bss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Callable
from dataclasses import dataclass

from _common.pabr_strings import checked_string_table_start, check_rows_end, read_string_table, string_at
from _common.record_reader import RecordReader


FILE_NAME = "palacemanagementstaticstatus.bss"
# __ePalaceManageType_Production and _Manufacture, as the boards of each group show.
PRODUCTION = 0
MANUFACTURE = 1

_VALUES_START = 0x04
_COUNT = struct.Struct("<I")
_GROUP_HEAD = struct.Struct("<HIIIBHHI")
_BOARD_REF = struct.Struct("<HB")
_BOARD_HEAD = struct.Struct("<HII")
_PRODUCTION_ITEM = struct.Struct("<HII")
_MANUFACTURE_ITEM = struct.Struct("<HI")
_SETTINGS = struct.Struct("<6H")
_NATION = struct.Struct("<IH")
_SETTINGS_FIELDS = tuple(f"unknown_manufacture_boards_{offset:02x}" for offset in range(0, _SETTINGS.size, 2))


@dataclass(frozen=True)
class _Board:
    name_kr: str
    items: list[dict]


def _counted(reader: RecordReader, entry: struct.Struct, what: str) -> list[tuple]:
    """A u32 count, then that many entries of `entry`."""
    (count,) = reader.unpack(_COUNT)
    if count * entry.size > reader.remaining():
        raise ValueError(f"{FILE_NAME} {what} count {count:,} runs past the string table")
    return [reader.unpack(entry) for _ in range(count)]


def _read_groups(reader: RecordReader, strings: list[str]) -> list[dict]:
    (count,) = reader.unpack(_COUNT)
    groups: list[dict] = []
    for _ in range(count):
        key, name_ref, texture_ref, desc_ref, group_type, npc, dialog, board_count = reader.unpack(_GROUP_HEAD)
        if board_count * _BOARD_REF.size > reader.remaining():
            raise ValueError(f"{FILE_NAME} board group {key} board count {board_count:,} runs past the string table")
        groups.append(
            {
                "board_group_key": key,
                "board_group_name_ref": name_ref,
                "board_group_name_kr": string_at(strings, name_ref),
                "texture_ref": texture_ref,
                "texture": string_at(strings, texture_ref),
                "desc_ref": desc_ref,
                "desc_kr": string_at(strings, desc_ref),
                "board_group_type": group_type,
                "npc_character_key": npc,
                "npc_dialog_index": dialog,
                "boards": [reader.unpack(_BOARD_REF) for _ in range(board_count)],
            }
        )
    return groups


def _production_item(raw: tuple) -> dict:
    item_index, probability, exchange_key = raw
    return {"item_index": item_index, "probability": probability, "exchange_key": exchange_key}


def _manufacture_item(raw: tuple) -> dict:
    item_index, exchange_key = raw
    return {"item_index": item_index, "probability": None, "exchange_key": exchange_key}


def _read_boards(
    reader: RecordReader,
    strings: list[str],
    entry: struct.Struct,
    to_item: Callable[[tuple], dict],
) -> dict[int, _Board]:
    """Boards by key, each with its name and items."""
    (count,) = reader.unpack(_COUNT)
    boards: dict[int, _Board] = {}
    for _ in range(count):
        key, name_ref, item_count = reader.unpack(_BOARD_HEAD)
        if item_count * entry.size > reader.remaining():
            raise ValueError(f"{FILE_NAME} board {key} item count {item_count:,} runs past the string table")
        items = [to_item(reader.unpack(entry)) for _ in range(item_count)]
        boards[key] = _Board(string_at(strings, name_ref), [{"board_name_ref": name_ref, **item} for item in items])
    return boards


def _group_records(group: dict, boards: dict[int, _Board]) -> list[dict]:
    """One record per item of each board the group lists, in list order."""
    head = {name: value for name, value in group.items() if name != "boards"}
    records: list[dict] = []
    for board_key, unknown_02 in group["boards"]:
        board = boards.get(board_key)
        if board is None:
            raise ValueError(f"{FILE_NAME} board group {group['board_group_key']} lists missing board {board_key}")
        records += [
            {**head, "board_key": board_key, "unknown_02": unknown_02, "board_name_kr": board.name_kr, **item}
            for item in board.items
        ]
    return records


def parse_palace_records(data: bytes) -> list[dict]:
    """One record per board item, by board group in file order, with the settings after the boards.

    A production group lists production boards, a manufacture group
    manufacture boards (`board_group_type`). Raises ValueError on a bad magic
    or trailer, a group that lists a board the file lacks, or values that do
    not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    strings = read_string_table(data)
    reader = RecordReader(data, _VALUES_START, end, FILE_NAME)
    groups = _read_groups(reader, strings)
    boards_by_type = {
        PRODUCTION: _read_boards(reader, strings, _PRODUCTION_ITEM, _production_item),
        MANUFACTURE: _read_boards(reader, strings, _MANUFACTURE_ITEM, _manufacture_item),
    }
    settings = dict(zip(_SETTINGS_FIELDS, reader.unpack(_SETTINGS)))
    nations = [[string_at(strings, code_ref), value] for code_ref, value in _counted(reader, _NATION, "nation")]
    check_rows_end(data, reader.pos, f"{FILE_NAME} values")
    tail = {**settings, "nations": nations}
    records: list[dict] = []
    for group in groups:
        boards = boards_by_type.get(group["board_group_type"])
        if boards is None:
            raise ValueError(f"{FILE_NAME} board group {group['board_group_key']} has type {group['board_group_type']}")
        records += [{**record, **tail} for record in _group_records(group, boards)]
    return records
