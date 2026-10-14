"""`manufacture.bss`: processing recipes, one material set per action and result group.

    PABR | u32 count | count x row | string table | u32 string_table_start | u32 0

    row:      u32 first_item_key | 8 zero bytes | u32 action_index | u32 unknown_10
              | u32 action_hash | u8 unknown_18 | u32 result_group
              | u32 material_count | material_count x material
    material: u32 item_key | u64 count

`action_index` indexes the string table of action names (`MANUFACTURE_HEAT`)
and `action_hash` is the lookup3 hash of the same name over its ASCII bytes.
`first_item_key` repeats `materials[0].item_key`. Full layout in
docs/file-formats/manufacture_bss.md.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from _common.binary import u32
from _common.pabr_strings import (
    HEADER_SIZE,
    check_rows_end,
    checked_string_table_start,
    read_string_table,
)
from _common.string_hash import KEY_HASH_SEED, hashlittle

_FILE_NAME = "manufacture.bss"
_HEAD = struct.Struct("<I8xIIIBII")
_MATERIAL = struct.Struct("<IQ")


@dataclass(frozen=True)
class Material:
    item_key: int
    count: int


@dataclass(frozen=True)
class Recipe:
    # The action name the processing window passes to the client, such as `MANUFACTURE_HEAT`.
    action: str
    # An `itemmaingroup.bss` group ID; most are missing from the client's copy of that file.
    result_group: int
    materials: tuple[Material, ...]


def action_hash(action: str) -> int:
    """The `action_hash` the file stores for an action name."""
    return hashlittle(action.encode("ascii"), KEY_HASH_SEED)


def parse_manufacture_records(data: bytes) -> list[Recipe]:
    """Every recipe in file order.

    Raises ValueError on a bad magic, an action index past the string table,
    an action hash or first item key that does not match, or when the rows do
    not end where the string table starts.
    """
    end = checked_string_table_start(data, _FILE_NAME)
    actions = read_string_table(data)
    hashes = [action_hash(action) for action in actions]
    count = u32(data, 4)
    pos = HEADER_SIZE
    recipes: list[Recipe] = []
    for index in range(count):
        recipe, pos = _read_row(data, pos, end, index, actions, hashes)
        recipes.append(recipe)
    check_rows_end(data, pos, f"{_FILE_NAME} rows")
    return recipes


def _read_row(
    data: bytes,
    pos: int,
    end: int,
    index: int,
    actions: list[str],
    hashes: list[int],
) -> tuple[Recipe, int]:
    if pos + _HEAD.size > end:
        raise ValueError(f"{_FILE_NAME} row {index} at 0x{pos:X} runs into the string table")
    first_item_key, action_index, _, stored_hash, _, result_group, material_count = _HEAD.unpack_from(data, pos)
    if action_index >= len(actions):
        raise ValueError(f"{_FILE_NAME} row {index} points at action {action_index}, past the string table")
    if stored_hash != hashes[action_index]:
        raise ValueError(f"{_FILE_NAME} row {index} stores hash 0x{stored_hash:08X} for {actions[action_index]}")

    first = pos + _HEAD.size
    row_end = first + material_count * _MATERIAL.size
    if row_end > end:
        raise ValueError(f"{_FILE_NAME} row {index} holds {material_count:,} materials, more than fit")
    materials = tuple(Material(*_MATERIAL.unpack_from(data, offset)) for offset in range(first, row_end, _MATERIAL.size))
    if not materials or materials[0].item_key != first_item_key:
        raise ValueError(f"{_FILE_NAME} row {index} key {first_item_key} is not its first material")
    return Recipe(actions[action_index], result_group, materials), row_end
