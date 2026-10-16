# `manufacture.bss` Format

## Purpose

Processing recipes: each row is one material set for one processing action (Heating, Grinding, Simple Alchemy, Imperial Cuisine, Manufacture and the rest) and the [`itemmaingroup.bss`](itemmaingroup_bss.md) group the action hands out. The plain PABR file holds the rows, then a string table of the action names the processing window passes to the client (`actionName` in `panel_window_manufacture_all.luac`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes   | Records                    | Row bytes |
| ------ | -------------- | ------- | ----------------- | ------- | -------------------------- | --------- |
| 2      | 3473 and later | 3473    | `manufacture.bss` | 417,753 | 15,361 Material, 7,064 Row | 12        |
| 1      | 1784           | 1784    | `manufacture.bss` | 466,321 | 16,442 Material, 8,668 Row | 12        |

| Layout | File              | Known             | Unknown           |
| ------ | ----------------- | ----------------- | ----------------- |
| 2      | `manufacture.bss` | 325,921 B (78.0%) | 91,832 B (22.0%)  |
| 1      | `manufacture.bss` | 336,301 B (72.1%) | 130,020 B (27.9%) |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                 |
| --------------------- | -------- | ------------------------------------------------------------------------------------ |
| `itemmaingroup.bss`   | Optional | The result group of a row, when the client ships it                                  |
| `itemsubgroup.dbss`   | Optional | The items of the result group's subgroups                                            |
| `itemsubgroupoffset.dbss` | Optional | Index the subgroup lookup reads `itemsubgroup.dbss` through                      |
| `languagedata_en.loc` | Optional | Item names (type 0 at `str_id1=item_id`) and the action names (type 37, see below)    |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type         | Field              | Notes                                         |
| ------------------- | ------------ | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32          | count              | Number of rows; `7,064` on client 3464        |
| `+0x08`             | Row[count]   | rows               | See Row                                       |
| `rows+0x00`         | String Table | string_table       | See String Table                              |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the rows end  |
| `string_table+0x04` | u32          | zero               | Always `0`                                    |

The string table has the shape `itemmaingroup.bss`, `exploration.bss` and `npcsimply.bss` use (`_common/pabr_strings.py`). Every string here is narrow (`is_wide = 0`, ASCII). Walking `count` rows ends exactly at `string_table_start`, and the string table ends exactly at the trailer.

### Row (variable: 33 bytes + materials)

| Offset  | Type                     | Field          | Notes                                                                                   |
| ------- | ------------------------ | -------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u32                      | first_item_key | Packed item key, equal to `materials[0].item_key` on every row                          |
| `+0x04` | bytes[8]                 | unknown_04     | Always zero                                                                             |
| `+0x0C` | u32                      | action_index   | Index into the string table, see [Actions](#actions)                                    |
| `+0x10` | u32                      | unknown_10     | `1,000,000`, `700,000`, `900,000` or `850,000`, see In-Game Checks                      |
| `+0x14` | u32                      | action_hash    | Hash of the action name, see below; matches `action_index` on every row                 |
| `+0x18` | u8                       | unknown_18     | Always `40`                                                                             |
| `+0x19` | u32                      | result_group   | `itemmaingroup.bss` group ID; unaligned                                                 |
| `+0x1D` | u32                      | material_count | `1` to `5`; unaligned                                                                   |
| `+0x21` | Material[material_count] | materials      | See Material                                                                            |

### Material (12 bytes)

| Offset  | Type | Field    | Notes                                                       |
| ------- | ---- | -------- | ----------------------------------------------------------- |
| `+0x00` | u32  | item_key | `(enchant_level << 24) \| item_id`, as in `itemsubgroup.dbss` |
| `+0x04` | u64  | count    | How many of the item the recipe takes                       |

On client 3464 the 7,064 rows hold 15,361 material entries: 3,072 rows have one, 1,551 two, 1,121 three, 776 four and 544 five. Counts run from `1` to `39,000`. Every one of the 5,304 distinct material keys is a key in `itemenchantoffset.dbss`. 675 entries carry an enchant level (`1` to `5`, `16` to `18` or `20`), such as Dandelion Jade Pillar at `18` for Simple Alchemy.

The entries of a row are in ascending `item_key` order on every row, so `first_item_key` is the row's lowest key. The same key can fill more than one entry: 17 rows (client 3464) list one key two or three times with count `1`, such as row 162 (Simple Alchemy) with three entries of Bonghwang's Fragment.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `12` on client 3464         |
| `+0x04` | pstr[string_count] | strings      | `u8 is_wide`, `u32 byte_length`, then the text |

## Layout 1

On client 1784 the row holds a u16 `unknown_19`, always `0`, where Layout 2
has the u32 `result_group`, so `material_count` sits at `+0x1B` and the
fixed part is 31 bytes. Only the Row differs from Layout 2.

### Row (variable: 31 bytes + materials)

| Offset  | Type                     | Field          | Notes                                   |
| ------- | ------------------------ | -------------- | --------------------------------------- |
| `+0x00` | u32                      | first_item_key |                                         |
| `+0x04` | bytes[8]                 | unknown_04     | Always zero on client 1784              |
| `+0x0C` | u32                      | action_index   |                                         |
| `+0x10` | u32                      | unknown_10     | Always `0` on client 1784               |
| `+0x14` | u32                      | action_hash    |                                         |
| `+0x18` | u8                       | unknown_18     | Always `39` on client 1784              |
| `+0x19` | u16                      | unknown_19     | Always `0` on client 1784               |
| `+0x1B` | u32                      | material_count | `1` to `5`                              |
| `+0x1F` | Material[material_count] | materials      |                                         |

## `action_hash`

`action_hash` is Bob Jenkins' lookup3 `hashlittle` over the action name's ASCII bytes with seed `0xC5EDE`, the function and seed of `_common/string_hash.py`. That module's `key_hash` runs over UTF-16LE text instead, so the stored value is `hashlittle(name.encode("ascii"), 0xC5EDE)`. It reproduces the hash for all 12 names, and on every row it is the hash of the string at `action_index`.

## Actions

The display name is the `PAGetString(Defines.StringSheet_GAME, key)` text the processing window (`MANUFACTURE_INFO` in `panel_window_manufacture_all.luac`) shows for that `actionName`, read from LOC type 37 at `str_id1 = key_hash(key)`. The index is the position in this file's string table and can move between clients; the hash cannot.

| Index | Action name                     | `action_hash` | Display name     | Rows (client 3464) |
| ----- | ------------------------------- | ------------- | ---------------- | ------------------ |
| 0     | `MANUFACTURE_HEAT`              | `0x1B6F02F1`  | Heating          | 1,610              |
| 1     | `MANUFACTURE_ALCHEMY`           | `0x8347A078`  | Simple Alchemy   | 2,134              |
| 2     | `MANUFACTURE_DRY`               | `0xF00F4092`  | Drying           | 262                |
| 3     | `MANUFACTURE_GRIND`             | `0x42AE9CE7`  | Grinding         | 182                |
| 4     | `MANUFACTURE_CRAFT`             | `0xC48B5E9F`  | Manufacture      | 1,353              |
| 5     | `MANUFACTURE_COOK`              | `0x4437F6B7`  | Simple Cooking   | 139                |
| 6     | `MANUFACTURE_SHAKE`             | `0xB61F6930`  | Shaking          | 203                |
| 7     | `MANUFACTURE_ROYALGIFT_ALCHEMY` | `0x810D0D4C`  | Imperial Alchemy | 300                |
| 8     | `MANUFACTURE_GUILD`             | `0x3D249288`  | Guild Processing | 6                  |
| 9     | `MANUFACTURE_ROYALGIFT_COOK`    | `0x431295C7`  | Imperial Cuisine | 811                |
| 10    | `MANUFACTURE_THINNING`          | `0x77B04381`  | Filtering        | 12                 |
| 11    | `MANUFACTURE_FIREWOOD`          | `0x68721E0B`  | Chopping         | 52                 |

The display keys are `ALCHEMY_MANUFACTURE_HEATING`, `LUA_ALCHEMY_MANUFACTURE_ALCHEMY`, `ALCHEMY_MANUFACTURE_DRY`, `ALCHEMY_MANUFACTURE_GRIND`, `LUA_MANUFACTURE_CRAFT_NAME`, `LUA_ALCHEMY_MANUFACTURE_COOK`, `ALCHEMY_MANUFACTURE_SHAKE`, `LUA_ALCHEMY_MANUFACTURE_ROYALGIFT_ALCHEMY`, `LUA_MANUFACTURE_GUILDMANURACTURE_NAME` (the client's spelling), `LUA_ALCHEMY_MANUFACTURE_ROYALGIFT_COOK`, `ALCHEMY_MANUFACTURE_THINNING` and `ALCHEMY_MANUFACTURE_WOODSPLITTING`. The window also lists `MANUFACTURE_RAINWATER` (Collect rainwater) and `REPAIR_ITEM` (Repair), which have no rows here.

## Notes

- No two rows share both the action and the full material list (client 3464), so (action, materials) identifies a row. `first_item_key` alone does not: Elixir of Demihuman Hunt starts eleven rows over Simple and Imperial Alchemy.
- On client 3464, 201 of the 2,791 distinct `result_group` values are group IDs in `itemmaingroup.bss`, covering 901 rows (525 Heating, 375 Manufacture, 1 Simple Alchemy). Each of those groups has one subgroup with the group's own key, and its items fit the recipe: Heating Steel Taritas Helmet gives group 9978 (Melted Iron Shard, Mud Crystal), Heating Bares Necklace gives 9901 (Ruby, Melted Silver Shard). Each of the 58 Manufacture rows with La Orzeca's Orb gives a La Orzeca part of the same name and enchant level as its other material, under a different item ID (`[Valkyrie] La Orzeca Helmet` 601603 gives 604001).
- The other 2,590 values (6,163 rows) fall between 10129 and 19994. The client's `itemmaingroup.bss` holds one group from 10000 to 29999 (group 10000), so the groups for most processing results are absent from the client files, not a different ID space.
- 439 of the 2,791 groups are shared by more than one row (client 3464). Group 12537 is the result of all 25 Heating rows of Black Alloy with a Black Abyssal weapon or the Black Abyssal Amulet. Only one group serves two actions (Simple Alchemy and Manufacture).
- The processing window has five material slots (`_slotMaxCount = 5`), the largest `material_count` in the file.
- `manufacturecondition.dbss` (14 rows) is keyed by the same `action_hash` values: it holds the 12 action names of this file plus `REPAIR_ITEM` and `MANUFACTURE_RAINWATER`, each with a condition script such as `getlevel()>0` or `getWeatherFactor(WindForce,0)>300;`. That table is not documented here.

## Open Questions

### `unknown_04`

The eight bytes at `+0x04` are zero on every row (client 3464). calpheonlabs calls them retired processing controls, with no source given. Nothing in the client data shows what they held.

### `unknown_18`

`unknown_18` is `40` on every row (client 3464), over all actions and all `unknown_10` values. calpheonlabs treats it as a fixed row marker. No client Lua or other table explains it.

### Missing Result Groups

Most `result_group` values (2,590 of 2,791 on client 3464) are not in `itemmaingroup.bss`, so a preview cannot show what Heating Melted Copper Shard or any Imperial Cuisine recipe gives. No other client table found so far holds groups 10000 to 29999.

## In-Game Checks

### Recipe Success Rate

This settles whether `unknown_10` is the chance that one processing run succeeds.

`unknown_10` is `1,000,000` on 3,641 rows, `700,000` on 3,336, `900,000` on 81 and `850,000` on 6 (client 3464). `1,000,000` is also the usual value of `itemsubgroup.dbss` `unknown_33`. `700,000` is the common value for ordinary processing (1,423 of 1,610 Heating rows, all 262 Drying rows), `1,000,000` dominates Imperial Cuisine (783 of 811) and Imperial Alchemy, and 79 of the 81 `900,000` rows are Heating, most of them Black Abyssal or Delphad Castillion's Carnage gear with Black Alloy, Obsidian Alloy or Targak Steel Shard. No client Lua reads a per-recipe value: the rate list window (`panel_alchemy_rateviewlist.luac`) gets its percentages from `ToClient_calculateManufacturePercent` through `FromClient_CalculateGroupPercent`, which reports per-item drop rates. calpheonlabs reads the field as a success rate in millionths, based on an archived `SuccessPercent` column, which is a lead but not client data.

Needs item: [Melted Copper Shard](https://bdocodex.com/us/item/4057/), 300 or more

1. Open the processing window and pick Heating.
2. Turn Mass Processing off.
3. Put in Melted Copper Shard (row 0, 10 per run, `unknown_10` = `700,000`).
4. Start processing and let it repeat 30 runs.
5. Count the runs that end in a failure message and give no item.

About 9 failures in 30 runs (30%) means `unknown_10` is the success chance in millionths. No failures means it is something else.
