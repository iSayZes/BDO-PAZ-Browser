# `alchemyupgrade.dbss` Format

## Purpose

The materials that polish an alchemy stone in the Polishing tab of the
alchemy stone window, per alchemy stone type. A row is the stone type, the
material item and the EXP one unit of that material adds to the stone.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                        | Bytes | Records                      | Row bytes |
| ------ | -------------- | ------- | --------------------------- | ----- | ---------------------------- | --------- |
| 1      | 1485 and later | 3474    | `alchemyupgrade.dbss`       | 2,028 | 166 Row, 8 Group             | 12        |
| 1      | 1485 and later | 3474    | `alchemyupgradeoffset.dbss` | 2,028 | 166 Index Row, 8 Index Group | 12        |

| Layout | File                        | Known            | Unknown    |
| ------ | --------------------------- | ---------------- | ---------- |
| 1      | `alchemyupgrade.dbss`       | 2,028 B (100.0%) | 0 B (0.0%) |
| 1      | `alchemyupgradeoffset.dbss` | 2,028 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler reads the groups in file order and does not need
`alchemyupgradeoffset.dbss` (see below). Item names come from LOC type 0 and
icons from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

The grouped layout of [`alchemycharge.dbss`](alchemycharge_dbss.md): a u32
group count, then per group a u32 row count and that many 12-byte rows. No
`PABR` magic and no string table; the file ends after the last group.

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

| Offset  | Type | Field      | Notes                                                             |
| ------- | ---- | ---------- | ----------------------------------------------------------------- |
| `+0x00` | u32  | stone_type | Equals the group index; see Stone Types                           |
| `+0x04` | u32  | item_id    | Material item; unique within a group                              |
| `+0x08` | u32  | experience | EXP per unit of the material, percent x 10,000 (`20408` = 2.0408%) |

On client 3464 the groups hold:

| Group | Rows | Materials                                                    | experience        |
| ----- | ---- | ------------------------------------------------------------ | ----------------- |
| `0`   | 28   | Ingots and pure crystals (4052 Iron Ingot, 4053 Pure Iron Crystal, 4253 Pure Silver Crystal, ...) | `18182` to `142857` |
| `1`   | 31   | Plywood and sturdy plywood (4652 Ash Plywood, 4653 Sturdy Ash Plywood, ...) | `18182` to `250000` |
| `2`   | 107  | High-quality and special crops (5444 High-quality Sunrise Herb, 7322 Special Strawberry, ...) | `649` to `6623` |
| `3` to `7` | 0 | Empty groups                                              |                   |

Every `experience` value on client 3464 is `1,000,000 / N` rounded, with `N`
a whole number: Iron Ingot `20408` is 1/49 of 100% EXP, Ash Plywood `18182`
1/55, High-quality Wheat `730` 1/1370.

### `alchemyupgradeoffset.dbss`

The grouped walk of `alchemychargeoffset.dbss`: a u32 group count (equal to
the main file's), then per group a u32 row count and 12-byte rows. A row
leaves out the stone type; its group index stands for it.

| Offset  | Type                     | Field       | Notes                                           |
| ------- | ------------------------ | ----------- | ----------------------------------------------- |
| `+0x00` | u32                      | group_count | Equals the main file's `group_count`            |
| `+0x04` | Index Group[group_count] | groups      | Group `i` holds stone type `i`; see Index Group |

### Index Group (variable: 4 bytes + rows)

| Offset  | Type                 | Field     | Notes                               |
| ------- | -------------------- | --------- | ----------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main group's `row_count` |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                       |

### Index Row (12 bytes)

| Offset  | Type | Field   | Notes                                                          |
| ------- | ---- | ------- | -------------------------------------------------------------- |
| `+0x00` | u32  | item_id | Row key together with the group index                          |
| `+0x04` | u32  | offset  | Start of the row in `alchemyupgrade.dbss`, at its `stone_type` |
| `+0x08` | u32  | size    | Always `12`, the main row size                                 |

Every index row points at the main row with the same stone type and item.
Unlike `alchemychargeoffset.dbss`, the rows inside a group are not in the
main file's order (group 0 lists 4052, 4061, 4253 where the main file has
4052, 4253, 4061). Both files are 2,028 bytes on client 3464.

## Stone Types

The group index and `stone_type` are the alchemy stone's `_contentsEventParam1`,
the same stone type as in `alchemycharge.dbss`; see its
[Stone Types](alchemycharge_dbss.md#stone-types) table. The Polishing tab
names each type's material from the same number (`panel_window_alchemystone_all`,
`invenStoneRClick`), and the groups hold those materials:

| stone_type | Stone       | Polishing Material (Lua)                                                  |
| ---------- | ----------- | ------------------------------------------------------------------------- |
| `0`        | Destruction | `LUA_ALCHEMYSTONE_PURESTONE` "Pure Metals", `LUA_ALCHEMYSTONE_PURESTONE2` "Metal Ingot" |
| `1`        | Protection  | `LUA_ALCHEMYSTONE_HARDWOOD` "Sturdy Plywood", `LUA_ALCHEMYSTONE_HARDWOOD2` "Plywood" |
| `2`        | Life        | `LUA_ALCHEMYSTONE_CHOICEGOOD` "Special Crop", `LUA_ALCHEMYSTONE_CHOICEGOOD2` "High-quality Crop" |

## Notes

- `experience` is named after the Polishing tab. Its guide text
  `LUA_ALCHEMYSTONE_DESC_2` reads "Polish your stone with material items to
  increase its EXP", and the tab (`_TAB_TYPE.EXP`, label
  `LUA_ALCHEMYSTONE_EXP` "Polishing") sends `alchemyUpgrade(material slot,
  count, stone slot)`; the Growth tab sends `alchemyEvolve()` instead
  (`panel_window_alchemystone_all`, `Panel_AlchemyStone_All_UpdateTime`). The inventory filter for
  a polishing material is `isAlchemyUpgradeItem(stone type)`.
- The window shows a stone's EXP as `getExperience() / 10000` with a `%`
  (`LUA_ALCHEMYSTONE_EXPERIENCE` "EXP {exp}%"), so a stone at 100% holds
  `1,000,000`. `experience` reads on the same scale, which the
  `1,000,000 / N` values above agree with. The client code that reads this
  file is not in Lua.
- The Polishing tab refuses a stone at 150% EXP or more
  (`LUA_ALCHEMYSTONE_EXPMAX_WARRING` "Cannot grow any further.",
  `HandleEventLUp_AlchemyStone_Doit`), and Growth
  opens from 80% (`LUA_ALCHEMYSTONE_DESC_3`).
- Item IDs are unique across the whole file on client 3464, not only within
  a group.

## Open Questions

### Stone Types 3 to 7

Groups 3 to 7 are empty on client 3464, as in `alchemycharge.dbss`. The
Polishing tab names a material only for types `0` to `2`; see that file's
Open Questions.

## In-Game Checks

### EXP per Material

Needs item (all):

- [Imperfect Alchemy Stone of Destruction](https://bdocodex.com/us/item/45201/)
- [Rough Alchemy Stone of Destruction](https://bdocodex.com/us/item/45205/)
- [Iron Ingot](https://bdocodex.com/us/item/4052/)

Polish each stone with one Iron Ingot and read its EXP before and after. A
rise of 2.04% on both stones means `experience` reaches the stone as
stored. A smaller rise on the Rough stone means the client scales it by the
stone's grade, as the Recharge tab does with durability.
