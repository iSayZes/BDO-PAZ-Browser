"""`plantexchangegroup.bss`: worker production groups.

    PABR | u32 count | count x 94-byte row | string table | u32 string_table_start | u32 0

Each row maps a production key (the `plantzone.dbss` join) to the
`itemexchangesource.bss` exchange the node works, and carries a Korean
"node - work type" label. Full layout in docs/file-formats/plantexchangegroup_bss.md.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import fixed_row_offsets, read_string_table, string_at
from _bss.itemexchangesource.parser import parse_itemexchangesource_records
from _bss.itemmaingroup.drop_groups import DROP_GROUP_FILES, DropGroups, load_drop_groups


# u16 production_key | u16 unknown_02 | u16 unknown_04 | u32 exchange_key
# | 80 zero bytes (exchange key slots 2 to 21) | u32 name_ref
_RECORD = struct.Struct("<HHHI80xI")
_RECORD_SIZE = 94
assert _RECORD.size == _RECORD_SIZE


def parse_plantexchangegroup_records(data: bytes) -> list[dict]:
    """Every production group row in file order, with its label resolved.

    Raises ValueError on a bad magic, or when the rows do not end where the
    string table starts: then the row size has changed and every field is suspect.
    """
    offsets = fixed_row_offsets(data, _RECORD_SIZE, "plantexchangegroup.bss")
    strings = read_string_table(data)
    records: list[dict] = []
    for offset in offsets:
        production_key, unknown_02, unknown_04, exchange_key, name_ref = _RECORD.unpack_from(data, offset)
        records.append({
            "production_key": production_key,
            "unknown_02": unknown_02,
            "unknown_04": unknown_04,
            "exchange_key": exchange_key,
            "name_kr": string_at(strings, name_ref),
        })
    return records


def build_production_item_index(
    groups: bytes,
    exchanges: bytes,
    maingroups: bytes,
    subgroups: bytes,
    subgroup_offsets: bytes,
) -> dict[int, tuple[int, ...]]:
    """The `PRODUCTION_ITEMS` index: each production key to its product drop group's packed item keys."""
    return _production_drop_items(groups, exchanges, (maingroups, subgroups, subgroup_offsets), is_luck=False)


def build_production_luck_item_index(
    groups: bytes,
    exchanges: bytes,
    maingroups: bytes,
    subgroups: bytes,
    subgroup_offsets: bytes,
) -> dict[int, tuple[int, ...]]:
    """The `PRODUCTION_LUCK_ITEMS` index: each production key to its luck drop group's packed item keys."""
    return _production_drop_items(groups, exchanges, (maingroups, subgroups, subgroup_offsets), is_luck=True)


def _production_drop_items(
    groups: bytes,
    exchanges: bytes,
    drop_group_files: tuple[bytes, bytes, bytes],
    is_luck: bool,
) -> dict[int, tuple[int, ...]]:
    """Each production key to the items of one drop group of its exchange.

        production_key -> exchange_key -> itemexchangesource.bss product or luck drop key
                       -> itemmaingroup.bss group -> itemsubgroup.dbss subgroups -> items

    `drop_group_files` are the payloads of `DROP_GROUP_FILES`, in that order.
    Only the production exchanges and their groups are kept, so no table that
    shows production items opens the 3 MB `itemexchangesource.bss` or the
    13 MB `itemsubgroup.dbss`. Production keys whose exchange, drop group or
    items are missing are left out.
    """
    rows = parse_plantexchangegroup_records(groups)
    wanted = {row["exchange_key"] for row in rows}
    drop_keys = {
        exchange.key: exchange.luck_drop_key if is_luck else exchange.product_drop_key
        for exchange in parse_itemexchangesource_records(exchanges)
        if exchange.key in wanted
    }
    found = _load_groups(drop_group_files, set(drop_keys.values()))
    index: dict[int, tuple[int, ...]] = {}
    for row in rows:
        item_keys = found.item_keys(drop_keys.get(row["exchange_key"], 0))
        if item_keys:
            index[row["production_key"]] = tuple(item_keys)
    return index


def _load_groups(drop_group_files: tuple[bytes, bytes, bytes], wanted: set[int]) -> DropGroups:
    companions: dict[str, bytes] = dict(zip(DROP_GROUP_FILES, drop_group_files, strict=True))
    return load_drop_groups(companions, wanted)
