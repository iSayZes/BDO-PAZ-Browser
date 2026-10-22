"""`siegerewarddata.bss`: the siege reward items per tier and the Conquest War medals, in two blocks.

    PABR | Grid Block | Tier Block | string table | u32 table_start | u32 0
    Grid Block: u32 medal_item_id | u16 tier_grid_count
                | tier_grid_count x Tier Grid | Major Rewards
    Tier Block: u32 medal_item_id | u16 tier_count | tier_count x Tier
                | Major Rewards
    Tier Grid (48 bytes): u16[4] unknown_00 | u16[4] unknown_08
                | u16[4] unknown_10 | u16[4] plus_medal_counts
                | u32[4] plus_item_ids
    Tier (24 bytes): u16 win_reward_count | u16 lose_reward_count
                | u16 release_reward_count | u16 plus_medal_count
                | u32 win_reward_item_id | u32 lose_reward_item_id
                | u32 release_reward_item_id | u32 plus_item_id
    Major Rewards (64 bytes): u16 win_medal_count | u16 lose_medal_count
                | u16 release_medal_count | u16 plus_medal_count
                | u32 plus_item_id | u32 win_medal_item_id
                | u32 lose_medal_item_id | u32 release_medal_item_id
                | u32 plus_medal_item_id | 5 x Release Medal
                | u32 release_win_medal_item_id | u16 release_win_medal_count
    Release Medal (6 bytes): u16 count | u32 item_id

The file has no row count: the Grid Block starts at +0x04. Full layout in
docs/file-formats/siegerewarddata_bss.md.
"""

from __future__ import annotations

import struct
from collections.abc import Callable

from _common.pabr_strings import checked_string_table_start, check_rows_end
from _common.record_reader import RecordReader


FILE_NAME = "siegerewarddata.bss"
# The `block` of a record: the Grid Block, then the Tier Block.
GRID_BLOCK = 1
TIER_BLOCK = 2
# The values per array of a Tier Grid, one per tier.
GRID_TIERS = 4
RELEASE_MEDAL_COUNT = 5

_BLOCKS_START = 0x04
_BLOCK_HEAD = struct.Struct("<IH")
_GRID_ARRAYS = ("unknown_00", "unknown_08", "unknown_10", "plus_medal_counts", "plus_item_ids")
# The three u16 arrays of a Tier Grid nobody has named yet.
_GRID_UNNAMED = _GRID_ARRAYS[:3]
_TIER_GRID = struct.Struct(f"<{4 * GRID_TIERS}H{GRID_TIERS}I")
_TIER_FIELDS = (
    "win_reward_count",
    "lose_reward_count",
    "release_reward_count",
    "plus_medal_count",
    "win_reward_item_id",
    "lose_reward_item_id",
    "release_reward_item_id",
    "plus_item_id",
)
_TIER = struct.Struct("<4H4I")
_MAJOR_HEAD_FIELDS = (
    "win_medal_count",
    "lose_medal_count",
    "release_medal_count",
    "plus_medal_count",
    "plus_item_id",
    "win_medal_item_id",
    "lose_medal_item_id",
    "release_medal_item_id",
    "plus_medal_item_id",
)
_MAJOR_HEAD = struct.Struct("<4H5I")
_RELEASE_MEDAL = struct.Struct("<HI")
_MAJOR_TAIL = struct.Struct("<IH")

EntryReader = Callable[[RecordReader], dict]


def _read_tier_grid(reader: RecordReader) -> dict:
    values = reader.unpack(_TIER_GRID)
    arrays = [list(values[start : start + GRID_TIERS]) for start in range(0, len(values), GRID_TIERS)]
    return dict(zip(_GRID_ARRAYS, arrays, strict=True))


def _read_tier(reader: RecordReader) -> dict:
    return dict(zip(_TIER_FIELDS, reader.unpack(_TIER), strict=True))


def _read_major_rewards(reader: RecordReader) -> dict:
    head = dict(zip(_MAJOR_HEAD_FIELDS, reader.unpack(_MAJOR_HEAD), strict=True))
    release_medals = [
        dict(zip(("count", "item_id"), reader.unpack(_RELEASE_MEDAL), strict=True)) for _ in range(RELEASE_MEDAL_COUNT)
    ]
    release_win_medal_item_id, release_win_medal_count = reader.unpack(_MAJOR_TAIL)
    return {
        **head,
        "release_medals": release_medals,
        "release_win_medal_item_id": release_win_medal_item_id,
        "release_win_medal_count": release_win_medal_count,
    }


def _read_block(reader: RecordReader, entries_name: str, read_entry: EntryReader, entry_size: int) -> dict:
    """`medal_item_id`, the entries under `entries_name` and `major_rewards`."""
    medal_item_id, entry_count = reader.unpack(_BLOCK_HEAD)
    if entry_count * entry_size > reader.remaining():
        raise ValueError(f"{FILE_NAME} {entries_name} count {entry_count:,} runs past the string table")
    entries = [read_entry(reader) for _ in range(entry_count)]
    return {"medal_item_id": medal_item_id, entries_name: entries, "major_rewards": _read_major_rewards(reader)}


def parse_siege_reward_blocks(data: bytes) -> tuple[dict, dict]:
    """The Grid Block (`tier_grids`) and the Tier Block (`tiers`).

    Raises ValueError on a bad magic or trailer, or when the Tier Block does
    not end where the string table starts.
    """
    end = checked_string_table_start(data, FILE_NAME)
    reader = RecordReader(data, _BLOCKS_START, end, FILE_NAME)
    grid_block = _read_block(reader, "tier_grids", _read_tier_grid, _TIER_GRID.size)
    tier_block = _read_block(reader, "tiers", _read_tier, _TIER.size)
    check_rows_end(data, reader.pos, f"{FILE_NAME} blocks")
    return grid_block, tier_block


def _slot(block: int, slot: str, item_id: int, count: int | None, **position: int | None) -> dict:
    """One reward slot: its block, tier grid and tier (1-based, None outside them), the item and its count.

    The three unnamed u16 of a Tier Grid tier are None; `_grid_slots` fills them.
    """
    return {
        "block": block,
        "tier_grid": position.get("tier_grid"),
        "tier": position.get("tier"),
        "slot": slot,
        "item_id": item_id,
        "count": count,
        **dict.fromkeys(_GRID_UNNAMED),
    }


def _grid_slots(medal_item_id: int, tier_grids: list[dict]) -> list[dict]:
    """Per Tier Grid and tier: the medals and the plus item, with that tier's three unnamed u16."""
    slots: list[dict] = []
    for grid_number, grid in enumerate(tier_grids, start=1):
        for tier in range(GRID_TIERS):
            unnamed = {name: grid[name][tier] for name in _GRID_UNNAMED}
            position = {"tier_grid": grid_number, "tier": tier + 1}
            slots += [
                {**_slot(GRID_BLOCK, "plus_medal", medal_item_id, grid["plus_medal_counts"][tier], **position), **unnamed},
                {**_slot(GRID_BLOCK, "plus_item", grid["plus_item_ids"][tier], None, **position), **unnamed},
            ]
    return slots


def _tier_slots(medal_item_id: int, tiers: list[dict]) -> list[dict]:
    """Per tier: the victory, defeat and liberation items, the medals and the plus item."""
    slots: list[dict] = []
    for number, tier in enumerate(tiers, start=1):
        slots += [
            _slot(TIER_BLOCK, kind, tier[f"{kind}_reward_item_id"], tier[f"{kind}_reward_count"], tier=number)
            for kind in ("win", "lose", "release")
        ]
        slots += [
            _slot(TIER_BLOCK, "plus_medal", medal_item_id, tier["plus_medal_count"], tier=number),
            _slot(TIER_BLOCK, "plus_item", tier["plus_item_id"], None, tier=number),
        ]
    return slots


def _major_slots(block: int, major: dict) -> list[dict]:
    """The Conquest War victory, defeat and liberation medals, score places 2nd to 6th and 1st, the plus medals and the plus item."""
    slots = [
        _slot(block, f"major_{kind}", major[f"{kind}_medal_item_id"], major[f"{kind}_medal_count"])
        for kind in ("win", "lose", "release")
    ]
    slots += [
        _slot(block, f"major_release_{index}", medal["item_id"], medal["count"])
        for index, medal in enumerate(major["release_medals"])
    ]
    slots += [
        _slot(block, "major_release_win", major["release_win_medal_item_id"], major["release_win_medal_count"]),
        _slot(block, "major_plus_medal", major["plus_medal_item_id"], major["plus_medal_count"]),
        _slot(block, "major_plus_item", major["plus_item_id"], None),
    ]
    return slots


def parse_reward_records(data: bytes) -> list[dict]:
    """One record per reward slot: the Grid Block's, then the Tier Block's, each ending with its Conquest War slots.

    `slot` names the field pair the item and count come from (`win` for
    `win_reward_item_id` and `win_reward_count`, `major_win` for the Major
    Rewards' `win_medal_*`); a plus item has no count. A Grid Block slot also
    holds its tier's `unknown_00`, `unknown_08` and `unknown_10`. Raises
    ValueError like `parse_siege_reward_blocks`.
    """
    grid_block, tier_block = parse_siege_reward_blocks(data)
    return [
        *_grid_slots(grid_block["medal_item_id"], grid_block["tier_grids"]),
        *_major_slots(GRID_BLOCK, grid_block["major_rewards"]),
        *_tier_slots(tier_block["medal_item_id"], tier_block["tiers"]),
        *_major_slots(TIER_BLOCK, tier_block["major_rewards"]),
    ]
