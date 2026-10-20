# `alchemycharge.dbss` Format

## Purpose

The materials that recharge an alchemy stone's durability in the Recharge tab
of the alchemy stone window, per alchemy stone type. A row is the stone type,
the material item and the durability points that material counts for.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records                     | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | --------------------------- | --------- |
| 1      | 1784 and later | 3474    | `alchemycharge.dbss`       | 468   | 36 Row, 8 Group             | 12        |
| 1      | 1784 and later | 3474    | `alchemychargeoffset.dbss` | 468   | 36 Index Row, 8 Index Group | 12        |

| Layout | File                       | Known          | Unknown    |
| ------ | -------------------------- | -------------- | ---------- |
| 1      | `alchemycharge.dbss`       | 468 B (100.0%) | 0 B (0.0%) |
| 1      | `alchemychargeoffset.dbss` | 468 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

None. The handler reads the groups in file order and does not need
`alchemychargeoffset.dbss` (see below). Item names come from LOC type 0 and
icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A group count, then the groups back to
back; the file ends after the last group.

| Offset  | Type               | Field       | Notes                                                |
| ------- | ------------------ | ----------- | ---------------------------------------------------- |
| `+0x00` | u32                | group_count | One group per alchemy stone type; `8` on client 3464 |
| `+0x04` | Group[group_count] | groups      | Group `i` holds stone type `i`; see Group            |

### Group (variable: 4 bytes + rows)

| Offset  | Type           | Field     | Notes                           |
| ------- | -------------- | --------- | ------------------------------- |
| `+0x00` | u32            | row_count | `0` for a type with no material |
| `+0x04` | Row[row_count] | rows      | See Row                         |

### Row (12 bytes)

| Offset  | Type | Field        | Notes                                                    |
| ------- | ---- | ------------ | -------------------------------------------------------- |
| `+0x00` | u32  | stone_type   | Equals the group index; see Stone Types                  |
| `+0x04` | u32  | item_id      | Material item; unique within a group                     |
| `+0x08` | u32  | charge_point | Durability points per use of the material (see Notes)    |

On client 3464 groups 0 to 2 hold the same 12 materials in the same order and
groups 3 to 7 are empty:

| Materials                                                          | charge_point |
| ------------------------------------------------------------------ | ------------ |
| Oils 6601 to 6605 (Regeneration, Storms, Fortitude, Corruption, Tranquility) | `10` |
| Bloods 6351 to 6355 (Legendary Beast's, Tyrant's, Clown's, Sinner's, Wise Man's) | `4` |
| Reagents 5301 Clear Liquid Reagent, 5302 Pure Powder Reagent       | `1`          |

### `alchemychargeoffset.dbss`

The same grouped walk: a u32 group count (equal to the main file's), then per
group a u32 row count and 12-byte rows. A row leaves out the stone type; its
group index stands for it.

| Offset  | Type                     | Field       | Notes                                  |
| ------- | ------------------------ | ----------- | -------------------------------------- |
| `+0x00` | u32                      | group_count | Equals the main file's `group_count`   |
| `+0x04` | Index Group[group_count] | groups      | Group `i` holds stone type `i`; see Index Group |

### Index Group (variable: 4 bytes + rows)

| Offset  | Type                 | Field     | Notes                                |
| ------- | -------------------- | --------- | ------------------------------------ |
| `+0x00` | u32                  | row_count | Equals the main group's `row_count`  |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                        |

### Index Row (12 bytes)

| Offset  | Type | Field   | Notes                                                        |
| ------- | ---- | ------- | ------------------------------------------------------------ |
| `+0x00` | u32  | item_id | Row key together with the group index                        |
| `+0x04` | u32  | offset  | Start of the row in `alchemycharge.dbss`, at its `stone_type` |
| `+0x08` | u32  | size    | Always `12`, the main row size                               |

Every index row points at the main row with the same stone type and item, in
the same order. Both files are 468 bytes on client 3464, since every row is
12 bytes in both.

## Stone Types

The group index and `stone_type` are the alchemy stone's `_contentsEventParam1`,
which the alchemy stone Lua reads as the stone type
(`panel_window_alchemystone_all`, `invenStoneRClick`).

| stone_type | Stone       | Evidence                                                                 |
| ---------- | ----------- | ------------------------------------------------------------------------ |
| `0`        | Destruction | Lua names the Polishing material `LUA_ALCHEMYSTONE_PURESTONE` "Pure Metals"; the Alchemy Stone of Destruction tooltip says "Polishing Material: Pure metal crystals, ingots" |
| `1`        | Protection  | Lua `LUA_ALCHEMYSTONE_HARDWOOD` "Sturdy Plywood"; Protection tooltip "Sturdy plywood, plywood" |
| `2`        | Life        | Lua `LUA_ALCHEMYSTONE_CHOICEGOOD` "Special Crop"; Life tooltip "Special & high-quality crops" |
| `3` to `5` | `unknown`   | Empty groups                                                            |
| `6`, `7`   | Vell's Heart | `isAlchemyBellHeart()` in the same Lua returns true for these two types; empty groups |

The sibling [`alchemyupgrade.dbss`](alchemyupgrade_dbss.md) (the Polishing
materials) has the same grouped layout with 8 groups: group 0 holds ingots and
pure metal crystals, group 1 plywood and group 2 crops, which agrees with the
table above.

## Notes

- The Recharge tab asks the client for the points of one stone and material
  pair, `ToClient_GetAlchmeyStoneChargePoint(stone slot, material slot)`, and
  shows the material count needed to refill the stone as
  `ceil(lost durability / charge point) * getAlchemyStoneGrade()`
  (`panel_window_alchemystone_all`, `invenMatRClick`). The inventory filter
  for the material slot is `isAlchemyRepair(stone type)`. The pair key and the
  per-type groups match this file; the client code that reads it is not in Lua.
- The Recharge tab text (`LUA_ALCHEMYSTONE_RENEWAL_BOTTOM_DESC1`) lists
  "Oils, bloods, reagents, Mystical Spirit Powder, Vell's Fine Powder" as fuel.
  The last two are not in this file on client 3464.
- `charge_point` follows the material, not the stone: on client 3464 all three
  filled groups give the same value per item.

## Open Questions

### Stone Types 3 to 5

Groups 3, 4 and 5 are empty on client 3464 and no Lua names these types. The
renewal window (`panel_window_alchemystone_renewal_all`) skips stones with a
type above `2` in its Growth tab, so they are neither the three main stones
nor, by `isAlchemyBellHeart()`, Vell's Heart.

### Mystical Spirit Powder and Vell's Fine Powder

The Recharge tab lists both as fuel, but neither has a row here. Their points
may come from another table or from the item itself: the Mystical Spirit
Powder tooltip (item 4924) lists a count per stone grade, from "Imperfect
alchemy stone: x1" to "Shining alchemy stone: x8".

## In-Game Checks

### Durability per Material

Needs item (all):

- [Imperfect Alchemy Stone of Destruction](https://bdocodex.com/us/item/45201/), with lost durability
- [Oil of Regeneration](https://bdocodex.com/us/item/6601/)
- [Clown's Blood](https://bdocodex.com/us/item/6353/)

Put the stone in the Recharge tab, note its durability (`current / max`), then
pick each material and read Required Amount. The Lua shows
`ceil(lost / charge point) * grade`, so if the Oil's amount is
`ceil(lost / 10)` and the Blood's `ceil(lost / 4)` times the same whole
number, `charge_point` reaches the Lua as stored. A different ratio means the
client scales it by the stone first.
