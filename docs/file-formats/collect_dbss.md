# `collect.dbss` Format

## Purpose

Gathering rules per gathering character: one row per Collect character (a
tree, ore vein, plant or animal corpse) with its gathering kind, gathering
time, the tools that work on it and the drop group each tool gives. The row
key is the character key that `collectresourcename.dbss` maps the world
models to. `collectoffset.dbss` is the key-ordered index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes  | Records        | Row bytes |
| ------ | -------------- | ------- | -------------------- | ------ | -------------- | --------- |
| 2      | 3002 and later | 3474    | `collect.dbss`       | 48,488 | 713 Row        | 68        |
| 2      | 3002 and later | 3474    | `collectoffset.dbss` | 7,134  | 713 Offset Row | 10        |
| 1      | 1485 to 1784   | 1784    | `collect.dbss`       | 29,092 | 606 Row        | 48        |
| 1      | 1485 to 1784   | 1784    | `collectoffset.dbss` | 6,064  | 606 Offset Row | 10        |

| Layout | File                 | Known             | Unknown         |
| ------ | -------------------- | ----------------- | --------------- |
| 2      | `collect.dbss`       | 39,932 B (82.4%)  | 8,556 B (17.6%) |
| 2      | `collectoffset.dbss` | 7,134 B (100.0%)  | 0 B (0.0%)      |
| 1      | `collect.dbss`       | 29,092 B (100.0%) | 0 B (0.0%)      |
| 1      | `collectoffset.dbss` | 6,064 B (100.0%)  | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3474   | Layout 2             |
| 3251   | Layout 2             |
| 3002   | Layout 2             |
| 2519   | No documented layout |
| 2107   | No documented layout |
| 1784   | Layout 1             |
| 1485   | Layout 1             |
| 1230   | No file              |
| 794    | No file              |

<!-- versions:end -->

## Companion Files

| File                                              | Required | Role                                                        |
| ------------------------------------------------- | -------- | ----------------------------------------------------------- |
| `collectoffset.dbss`                              | Optional | `character_key -> (data_offset, data_size)` index; the rows are fixed size and can be walked without it |
| [`characterstatic.dbss`](characterstatic_dbss.md) | Optional | The character a `character_key` names; the handler links each key to its row |

Character names come from LOC type 6.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                      |
| ------- | ---------- | ----- | ------------------------------------------ |
| `+0x00` | u32        | count | Number of rows; `713` on client 3474       |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 68 bytes + name text)

| Offset        | Type    | Field                  | Notes                                                              |
| ------------- | ------- | ---------------------- | ------------------------------------------------------------------ |
| `+0x00`       | u16     | character_key          | Gathering character, a `characterstatic.dbss` `character_id`; unique per row, the index key |
| `+0x02`       | str16   | name                   | Empty on every row; the index's `data_offset` points here          |
| `name+0x00`   | u16     | character_key_dup      | Equal to `character_key` in every row                              |
| `name+0x02`   | u8      | product_data_type      | Gathering kind, see Product Data Types                             |
| `name+0x03`   | u32     | product_time           | `60000` on every row (client 3474)                                 |
| `name+0x07`   | f32     | product_hp             | `1.0` on every row (client 3474)                                   |
| `name+0x0B`   | f32     | product_decrease_hp    | `1.0` on every row (client 3474)                                   |
| `name+0x0F`   | u32     | product_item_drop_key  | `10002` on every row (client 3474); an item main group key, see Notes |
| `name+0x13`   | u8[3]   | collect_tool_types     | Tool per slot, see Collect Tool Types; `19` is an empty slot       |
| `name+0x16`   | u32[3]  | collect_item_drop_keys | Item main group key per slot; `0` exactly where the slot's tool is `19` |
| `name+0x22`   | bytes[12] | unknown_name_22      | `0` on every row (client 3474); not in Layout 1                    |
| `name+0x2E`   | u32     | action_point           | `1` on every row (client 3474)                                     |
| `name+0x32`   | u32     | spawn_delay_time       | `0` on every row (client 3474)                                     |
| `name+0x36`   | u32     | spawn_variable_time    | `0` on every row (client 3474)                                     |

With the empty `name`, every row is 68 bytes. The rows are not sorted by key.

### `collectoffset.dbss`

| Offset  | Type              | Field | Notes                                  |
| ------- | ----------------- | ----- | -------------------------------------- |
| `+0x00` | u32               | count | Equals the `collect.dbss` count        |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row   |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                  |
| ------- | ---- | ------------- | -------------------------------------- |
| `+0x00` | u16  | character_key | Row key                                |
| `+0x02` | u32  | data_offset   | Row start + 2, at `name`               |
| `+0x06` | u32  | data_size     | Row size - 2: `66` on client 3474      |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3474 every index row points
at the row with its key.

## Layout 1

### Row (variable: 48 bytes + name text)

| Offset      | Type   | Field                  | Notes                                                   |
| ----------- | ------ | ---------------------- | ------------------------------------------------------- |
| `+0x00`     | u16    | character_key          | Gathering character                                     |
| `+0x02`     | str16  | name                   | Empty on every row                                      |
| `name+0x00` | u16    | character_key_dup      | Equal to `character_key` in every row                   |
| `name+0x02` | u8     | product_data_type      | Gathering kind, see Product Data Types                  |
| `name+0x03` | u32    | product_time           | `60000` on every row (client 1784)                      |
| `name+0x07` | f32    | product_hp             | `1.0` on every row (client 1784)                        |
| `name+0x0B` | f32    | product_decrease_hp    | `1.0` on every row (client 1784)                        |
| `name+0x0F` | u16    | product_item_drop_key  | `10002` on every row (client 1784)                      |
| `name+0x11` | u8[3]  | collect_tool_types     | Tool per slot; `15` is an empty slot                    |
| `name+0x14` | u16[3] | collect_item_drop_keys | `0` exactly where the slot's tool is `15`               |
| `name+0x1A` | u32    | action_point           | `1` on every row (client 1784)                          |
| `name+0x1E` | u32    | spawn_delay_time       | `0` on every row (client 1784)                          |
| `name+0x22` | u32    | spawn_variable_time    | `0` on every row (client 1784)                          |

The drop keys are u16 here and u32 in Layout 2, and `unknown_name_22` does
not exist yet. Every row is 48 bytes; the index's `data_size` is `46`.

## Field Names

The row is the 2016 `gc::CollectStaticStatus` in member order: `_name`,
`_key`, `_productDataType`, `_productTime`, `_productHp`,
`_productDecreaseHp`, `_productItemDropKey`, `_collectToolType[3]`,
`_collectItemDropKey[3]`, `_actionPoint`, `_spawnDelayTime`,
`_spawnVariableTime`. The 2016 drop keys are u16, as in Layout 1.

The values match the `Collect_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `Index`, the `character_key`: all 606
sheet keys are rows on both clients. An empty sheet cell in a tool slot is
tool `15` with drop key `0` on client 1784, and tool `19` with drop key `0`
on client 3474.

| Field                  | Column                           | Same value (client 1784) | Same value (client 3474) |
| ---------------------- | -------------------------------- | ------------------------ | ------------------------ |
| product_data_type      | `ProductDataType`                | 606 of 606               | 606 of 606               |
| product_time           | `ProductTime`                    | 606 of 606               | 606 of 606               |
| product_hp             | `ProductAllHP`                   | 606 of 606               | 606 of 606               |
| product_decrease_hp    | `ProductDeceraseHP`              | 606 of 606               | 606 of 606               |
| product_item_drop_key  | `ItemDropID`                     | 606 of 606               | 606 of 606               |
| collect_tool_types     | `ToolType_0` to `ToolType_2`     | 606 of 606               | 598 of 606               |
| collect_item_drop_keys | `ItemDropID_0` to `ItemDropID_2` | 606 of 606               | 598 of 606               |
| action_point           | `ActionPoint`                    | 606 of 606               | 606 of 606               |
| spawn_delay_time       | `SpawnDelayTime`                 | 606 of 606               | 606 of 606               |
| spawn_variable_time    | `SpawnVariableTime`              | 606 of 606               | 606 of 606               |

`product_time`, `product_hp`, `product_decrease_hp`, `product_item_drop_key`,
`action_point` and both spawn times hold one value on every row and in the
sheet, so their names rest on the 2016 member order and the Layout 1
positions, not on the values. The eight rows that differ on client 3474 are
`11985` to `11992` (Chanterelle, Red-spotted Amanita, Mesima, Dictyophora,
three Citron Trees, Jadeite): their tool slots or drop groups changed after
client 1784. The client 3474 file adds 107 keys the sheet lacks.

The sheet columns `NeedObjectSkillNo`, `ProductSkillLevel`, `Exp`,
`ProductSkillPointExp` and `IsNotReduce` have no place in the row. `Exp`
and `IsNotReduce` vary in the sheet, and no row byte follows them.

## Product Data Types

The names are the 2016 `gc::ProductDataType::Type` values.

| Value | Name                           | Rows (client 3474) | Tools in the rows                    |
| ----- | ------------------------------ | ------------------ | ------------------------------------ |
| 0     | `eProductData_Default`         | 0                  |                                      |
| 1     | `eProductData_Collect_Base`    | 0                  |                                      |
| 2     | `eProductData_Collect_Collect` | 229                | BareHands, Hoe, Syringe, Pray        |
| 3     | `eProductData_Collect_Farm`    | 0                  |                                      |
| 4     | `eProductData_Collect_Mining`  | 97                 | Pickax, BareHands, ButcheryKnife     |
| 5     | `eProductData_Collect_Purify`  | 0                  |                                      |
| 6     | `eProductData_Collect_Logging` | 246                | Axe, Syringe, Hoe, BareHands, Pickax |
| 7     | `eProductData_Collect_Tanning` | 141                | ButcheryKnife, SkinKnife, Syringe, Hoe, Axe |

## Collect Tool Types

Values `0` to `10` are the 2016 `gc::CollectToolType::Type` values, which end
at `TypeCount = 11`. The client Lua's `CppEnums.CollectToolTypeName`
(`global_define_cpp_enum.luac`) lists the same names in the same order and
adds MassStone, FishingChair, Whip, Oar and, on client 3474, Reserve; it
keys them by engine globals, so their numbers do not show in the Lua.

| Value | Name           | Slots (client 3474) |
| ----- | -------------- | ------------------- |
| 0     | BareHands      | 281                 |
| 2     | Axe            | 151                 |
| 3     | Syringe        | 175                 |
| 4     | Hoe            | 217                 |
| 5     | ButcheryKnife  | 122                 |
| 6     | SkinKnife      | 38                  |
| 7     | Pickax         | 110                 |
| 9     | Pray           | 2                   |
| 19    | Empty slot     | 1,043               |

The empty slot is `15` on client 1784, where the Lua lists 15 names (`0`
BareHands to `14` Oar) followed by `__eCollectToolType_Count`, which puts
`__eCollectToolType_Count` if the values run on from `0`. On client 3474 it
is `19` while the Lua lists 16 names.

## Notes

- On client 3474, 564 of the 713 keys are `characterstatic.dbss`
  characters: 563 with `npc_kind` Collect and `18561` Pine Mushroom with
  `npc_kind` 2. The one Collect character without a row is `501` Test
  Object. The other 149 keys (`10003`, `10146`, `10701` and more) have no
  `characterstatic.dbss` row and no LOC type 6 name.
- 561 keys are the `character_key` of a `collectresourcename.dbss` model;
  152 keys have no model there.
- None of the 564 distinct drop keys on client 3474 is a group of
  `itemmaingroup.bss` or a subgroup of `itemsubgroup.dbss`, so the drops
  cannot be resolved from the client. 481 of them are keys of the
  `ItemMainGroup_Table` sheet of a private server on client 1784, where
  main group `10002` holds subgroup `10002` and three subgroups many
  gathering groups share.
- The tool slot fill follows the gathering kind: logging rows hold Axe and
  Syringe (`11983` Snowfield Cedar Tree), mining rows Pickax, tanning rows
  ButcheryKnife and SkinKnife.
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  lists this file with `collectresourcename.dbss` as "gatherable identity
  and internal mesh names; no yields or rates". The row has no rate, but it
  holds the drop group per tool.

## Open Questions

### The 12 Bytes After The Drop Keys

`unknown_name_22` is 12 bytes that Layout 1 does not have, `0` on every row
of client 3474. The 2016 struct has nothing between `_collectItemDropKey`
and `_actionPoint`, and the client 1784 sheet has no column for it.
