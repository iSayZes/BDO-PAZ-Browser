# `blizzardregioninfo.bss` Format

## Purpose

Lists the snow regions that the client ties to blizzards: every row names one `regioninfo.bss` region of the Mountain of Eternal Winter (territory 9) or Ulukita (territory 11) and holds the minimum and maximum chance that the blizzard effect spawns there and a wind vector.

The file is small (21 rows in client 3458) and has no strings. The client Lua never mentions it or a blizzard; the field names come from the developers' `Blizzard_Region_Table` sheet (see [Field Names](#field-names)).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------- | --------- |
| 1      | 2107 and later | 3474    | `blizzardregioninfo.bss` | 566   | 21 Row  | 26        |

| Layout | File                     | Known          | Unknown    |
| ------ | ------------------------ | -------------- | ---------- |
| 1      | `blizzardregioninfo.bss` | 566 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3473   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Region names (LOC type 17, keyed by `region_key`)     |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                                                    |
| ------------------- | ----------------- | ------------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                           |
| `+0x04`             | u32               | record_count       | Observed `21`                                            |
| `+0x08`             | Row[record_count] | records            | See Row; byte-packed                                     |
| `records+0x00`      | String Table      | string_table       | The PABR string table, present but empty                 |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 26 × count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                               |

The file is `8 + 26 × 21 + 12 = 566` bytes. The parser rejects a file whose rows do not end exactly at `string_table_start`.

### Row (26 bytes)

| Offset  | Type | Field                    | Notes                                                                                     |
| ------- | ---- | ------------------------ | ----------------------------------------------------------------------------------------- |
| `+0x00` | u32  | key                      | Unique, ascending, with gaps (`1`, `2`, `6` to `24`)                                      |
| `+0x04` | u16  | region_key               | `regioninfo.bss` region key; LOC type 17 names it. Every row resolves                     |
| `+0x06` | u32  | effect_spawn_percent_min | Lowest chance that the blizzard effect spawns, 1,000,000 = 100%; `50000` to `500000`      |
| `+0x0A` | u32  | effect_spawn_percent_max | Highest chance, same scale; `120000` to `800000`, always above the minimum                |
| `+0x0E` | f32  | wind_x                   | Wind vector, X; `1.0`, `2.0` or `3.0`                                                     |
| `+0x12` | f32  | wind_y                   | Wind vector, Y; `0.0` on every row                                                        |
| `+0x16` | f32  | wind_z                   | Wind vector, Z; `0.0` on every row                                                        |

The value ranges are from client 3473. The spawn chances and `wind_x` come in a few fixed sets per area (client 3458):

| effect_spawn_percent_min | effect_spawn_percent_max | wind_x | Regions                                                                      |
| ------------------------ | ------------------------ | ------ | ---------------------------------------------------------------------------- |
| `400000` (40%)           | `800000` (80%)           | `3.0`  | 1126 Mountain of Eternal Winter                                              |
| `250000` (25%)           | `500000` (50%)           | `2.0`  | 1175 Mountain of Eternal Winter; all Ulukita rows except Velandir            |
| `200000` (20%)           | `400000` (40%)           | `3.0`  | 1146, 1163 Mountain of Eternal Winter                                        |
| `100000` (10%)           | `250000` (25%)           | `2.0`  | Jade Starlight Forest (1127, 1147, 1164), Snowstorm Guard Post (1125, 1145)  |
| `50000` (5%)             | `120000` (12%)           | `1.0`  | Bronte's Bolt (1123, 1143, 1160)                                             |
| `500000` (50%)           | `800000` (80%)           | `3.0`  | 1382 Velandir                                                                |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Field Names

The names are the columns of the `Blizzard_Region_Table` sheet that a private server on client 1784 ships in its `DataSheets.bexcel` and in the developer workbook `datasheet_regiondatatable.xlsm`: `Index`, `RegionIndex`, `EffectSpawnPercentMin`, `EffectSpawnPercentMax`, `Wind_X`, `Wind_Y`, `Wind_Z`. The sheet holds 5 rows. The same private server's `blizzardregioninfo.bss`, built from that sheet, is 150 bytes: 5 rows of this 26-byte layout with the seven columns in sheet order, `Wind_X` to `Wind_Z` as f32. The column-to-offset match rests on that build, because the sheet and the client file share only keys 1 and 2:

| Key | Region | Sheet (client 1784)       | Client 3473               |
| --- | ------ | ------------------------- | ------------------------- |
| 1   | 1126   | `100000`, `300000`, `1.0` | `400000`, `800000`, `3.0` |
| 2   | 1175   | `250000`, `500000`, `2.0` | `250000`, `500000`, `2.0` |

The region keys of both rows and every column of key 2 match. `Wind_Y` and `Wind_Z` are `0` on every row of the sheet and of the client file.

The server dump of that private server holds the loader messages for `BlizzardRegionInfoStaticStatus` (sheet `Blizzard_Region_Table`, loader `loadBlizzardRegionInfo`). They reject an `EffectSpawnPercentMin` or `EffectSpawnPercentMax` outside "1~100%", a minimum above the maximum, and a `RegionIndex` with no region info. The sheet's largest value is `1000000` (key 5, both columns), so the chances are on the 1,000,000 = 100% scale.

Neither the 2016 client with debug symbols nor the tables of a private server on client 519 have a blizzard type or table. The client Lua has no blizzard text.

## Notes

- A region name can appear on several rows: LOC gives the same name to several region keys (1126, 1146, 1163 and 1175 are all Mountain of Eternal Winter).
- The keys skip `3`, `4` and `5`. On client 1784 the sheet has them for regions 1176, 1177 and 1178 (chances 50% to 80%, 70% to 100% and 100% to 100%, `wind_x` 3, 4 and 5). On client 3473 region 1176 is Snowfall Crasher: Alpine Glide, and 1177 and 1178 are not in `regioninfo.bss`.
- `wind_y` and `wind_z` are read as f32 because they are the other two axes of the `Wind_X` vector. Every row holds `0`, which reads the same as a u32.
- `edaniaregioninfo.bss` is the other small region-variant table. It is not the same layout (9-byte rows keyed by an Edania region value, no region key), so the two files have separate parsers.

## Open Questions

### What the Wind Vector Does

Only `wind_x` is set (`1.0` to `3.0`; the sheet on client 1784 goes up to `5.0`), with `wind_y` and `wind_z` at `0`. Whether the vector is a direction scaled by strength, a strength level on X only, or a push on the player is not shown by the sheet or the client Lua.

### What Rolls the Spawn Chance

The chance range says how likely the blizzard effect is, but not how often the client or server rolls it or what picks a value between the minimum and the maximum.

## In-Game Checks

### Blizzard Frequency per Region

Needs zone (all):

- Bronte's Bolt
- Mountain of Eternal Winter

Checks that the spawn chance sets how often a region has a blizzard. Bronte's Bolt rows hold 5% to 12%, the Mountain of Eternal Winter rows 20% to 80%.

1. Stand in Bronte's Bolt for 30 minutes and note how long a blizzard is visible.
2. Stand in the Mountain of Eternal Winter for 30 minutes and note the same. Four region keys carry that name (1126, 1146, 1163, 1175, at 20% to 80%), so the spot may be any of them.
3. Compare the two shares of time.

Expected result: the blizzard shows for a small share of the time in Bronte's Bolt and for a larger share in the Mountain of Eternal Winter. Equal shares would mean the chance does not set the frequency.
