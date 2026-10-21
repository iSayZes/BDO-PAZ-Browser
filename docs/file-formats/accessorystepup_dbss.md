# `accessorystepup.dbss` Format

## Purpose

The accessory step-up: an accessory that grows from base to PEN in five
steps, each step paid with four materials and the accessory at its current
level. One row per accessory choice, with its group and the materials of
all five steps. The step-up window
(`panel_window_accessory_stepup_all_*.luac`) reads it through
`ToClient_getAccessoryStepUpItemKey(accessoryIndex)`,
`ToClient_getAccessoryStepUpMaterialItemEnchantKey(accessoryIndex,
enchantLevel, materialIndex)` and
`ToClient_getAccessoryStepUpMaterialNeedCount` with the same arguments.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records                      | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ---------------------------- | --------- |
| 1      | 2519 and later | 3474    | `accessorystepup.dbss` | 1,840 | 150 Material, 30 Step, 6 Row | 12        |

| Layout | File                   | Known            | Unknown    |
| ------ | ---------------------- | ---------------- | ---------- |
| 1      | `accessorystepup.dbss` | 1,840 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None; the file has no `*offset.dbss` index. The handler names the items
through LOC type 0 and the item icon index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

On client 3474 the file is 4 + 6 x 306 = 1,840 bytes.

### Row (306 bytes)

| Offset  | Type    | Field           | Notes                                                                  |
| ------- | ------- | --------------- | ---------------------------------------------------------------------- |
| `+0x00` | u32     | item_key        | The accessory, an item enchant key at level `0`                        |
| `+0x04` | u8      | group_no        | Group of the choice, `1` or `2` on client 3474                         |
| `+0x05` | u8      | accessory_index | Choice number from `1`, the `accessoryIndex` of the getters; unique    |
| `+0x06` | Step[5] | steps           | Step N (from 0) enhances the accessory to level N + 1, see Step        |

The rows are in descending `accessory_index` order (6 to 1 on client 3474).

### Step (60 bytes)

| Offset  | Type        | Field     | Notes                                      |
| ------- | ----------- | --------- | ------------------------------------------ |
| `+0x00` | Material[5] | materials | The materials of the step, see Material    |

### Material (12 bytes)

| Offset  | Type | Field      | Notes                                                                |
| ------- | ---- | ---------- | -------------------------------------------------------------------- |
| `+0x00` | u32  | item_key   | Material item, an item enchant key (`enchant_level << 24 \| item_id`) |
| `+0x04` | u64  | need_count | How many the step needs                                              |

The fifth material of step N is the row's accessory at level N, count `1`.
The window greys it out until the other four are in
(`materialIndex == __eMaxAccessoryStepUpMaterialCount - 1`).

## Steps and Groups

The window draws `__eMaxAccessoryStepUpEnchantLevel` steps
(`Static_Step_1` onward) of `__eMaxAccessoryStepUpMaterialCount` materials
(`Static_MaterialItem_L1`, `R1`, `L2`, `R2`, `L3`), five of each, which is
the `Step[5]` and `Material[5]` the row holds. The step of a material is the
`enchantLevel` argument, from 0, and the window names it
`accessoryEnchantLevel = enchantLevel + 1`.

`ToClient_getAccessoryMaxGroupIndex(groupNo)` gives the last
`accessory_index` of a group; the window lists the choices of the player's
current group. On client 3474 both groups hold the same three accessories:

| `accessory_index` | `group_no` | Accessory                        |
| ----------------- | ---------- | -------------------------------- |
| 1, 4              | 1, 2       | 550801 Ring of Crescent Guardian |
| 2, 5              | 1, 2       | 550802 Narc Ear Accessory        |
| 3, 6              | 1, 2       | 550803 Tungrad Earring           |

Every row of client 3474 asks for the same four materials per step: 44350
Yona's Fragment, 4918 Magical Shard, 16001 Black Stone and 45162 Old Moon
Alchemy Catalyst.

## Field Names

Neither the 2016 PDB nor a private server's `DataSheets.bexcel` on client
1784 has the table, and the client 1784 PAZ has no `accessorystepup.dbss`
(clients 2519 to 3474 have it). The names follow the Lua getters above and
`getAccessoryStepUpManager()`, whose `getAccessoryGroupNo()` and
`getAccessoryIndex()` pick a row; `need_count` is the value of
`ToClient_getAccessoryStepUpMaterialNeedCount`.

## Notes

- Client 2519 has the same rows with larger counts in the last step (for
  example 110 Yona's Fragment where client 3474 asks for 100).
