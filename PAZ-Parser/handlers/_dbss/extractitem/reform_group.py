"""The Gear Reform group an extraction undoes, from the two reform tables.

An extraction row is an `itemimprovement.dbss` reform run backwards: the
reform's result is the row's `item_id` and its input is `result_item_id`.
Some (result, input) pairs have records in more than one group; the group
that also holds `result_material_id` as a stone in
`itemimprovementsource.dbss` picks one. See the Notes in
docs/file-formats/extractitem_dbss.md.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable

from _dbss.itemimprovement.parser import parse_itemimprovement_records, parse_itemimprovementsource_records


ReformGroupLookup = Callable[[dict], int | None]


def reform_group_lookup(reform_data: bytes | None, stone_data: bytes | None) -> ReformGroupLookup:
    """A function from an extraction row to its reform group.

    It returns None when either table is missing, no reform record matches
    the row, or the stone does not narrow the matches to one group.
    """
    if reform_data is None or stone_data is None:
        return lambda _row: None

    groups_by_pair: dict[tuple[int, int], set[int]] = defaultdict(set)
    for record in parse_itemimprovement_records(reform_data):
        if record["result_id"] is not None:
            groups_by_pair[(record["result_id"], record["input_id"])].add(record["group"])

    groups_by_stone: dict[int, set[int]] = defaultdict(set)
    for stone in parse_itemimprovementsource_records(stone_data):
        groups_by_stone[stone["item_id"]].add(stone["group"])

    def lookup(row: dict) -> int | None:
        pair_groups = groups_by_pair.get((row["item_id"], row["result_item_id"]), set())
        matches = pair_groups & groups_by_stone.get(row["result_material_id"], set())
        return next(iter(matches)) if len(matches) == 1 else None

    return lookup
