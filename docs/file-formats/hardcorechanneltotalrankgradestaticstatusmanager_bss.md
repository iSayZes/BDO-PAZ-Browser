# `hardcorechanneltotalrankgradestaticstatusmanager.bss` Format

## Purpose

The grades of the Hardcore channel's total ranking: how many players the
ranking lists, then one row per grade. Grades 1 to 3 (Transcendent,
Conqueror, Reaper) go to ranks 1 to 3, grades 4 to 9 (Honorblade to Adept)
to the top 1, 5, 10, 30, 50 and 100 percent, and grade 0 is Novice, the
unranked grade (client 3474). The Hardcore Box items of LOC type 0 carry the
same tier names ("Transcendent's Hardcore Box" ... "Adept's Hardcore Box",
items 965002 to 965010), but no field of this file points at them.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                                   | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------------------------------------ | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `hardcorechanneltotalrankgradestaticstatusmanager.bss` | 128   | 10 Row  | 10        |

| Layout | File                                                   | Known         | Unknown    |
| ------ | ------------------------------------------------------ | ------------- | ---------- |
| 1      | `hardcorechanneltotalrankgradestaticstatusmanager.bss` | 124 B (96.9%) | 4 B (3.1%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | No file  |
| 2107   | No file  |
| 1784   | No file  |
| 1485   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                  |
| --------------------- | -------- | --------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Grade names, LOC type 37 under the RESOURCE sheet key hash            |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field          | Notes                                                              |
| ------------------- | -------------- | -------------- | ------------------------------------------------------------------ |
| `+0x00`             | char[4]        | magic          | ASCII `PABR`                                                       |
| `+0x04`             | u32            | rank_threshold | Number of players the ranking lists; `100` on client 3474          |
| `+0x08`             | u32            | unknown_08     | `3` on client 3474                                                 |
| `+0x0C`             | u32            | row_count      | Number of rows                                                     |
| `+0x10`             | Row[row_count] | rows           | See Row; byte-packed                                               |
| `rows+0x00`         | String Table   | string_table   | See String Table                                                   |
| `string_table+0x00` | u32            | table_start    | Offset of the string table, where `rows` ends                      |
| `string_table+0x04` | u32            | zero           | Always `0`                                                         |

### Row (10 bytes)

| Offset  | Type | Field     | Notes                                                                           |
| ------- | ---- | --------- | ------------------------------------------------------------------------------- |
| `+0x00` | u16  | grade_key | Grade, `0` to `9`, unique; see Grades                                           |
| `+0x02` | u32  | rank      | The one rank that holds the grade; `0` for a grade by percentage and for `0`    |
| `+0x06` | f32  | percent   | Top percentage of the grade; `0` for a grade by rank and for `0`                |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Grades

The ranking window names each grade with a RESOURCE sheet key
(`panel_widget_ranking_hardcore_1.luac`, `initTierList`): grade keys 1 to 3
the `PANEL_HARDCOE_RANKING_TIER_0_<key>` keys of its first row, grade keys 4
to 9 `PANEL_HARDCOE_RANKING_TIERNAME_<key - 3>`, and grade 0 (no grade)
`PANEL_HARDCOE_RANKING_TIERNAME_7`. Its `_totalGradeCount` is `10`, and the
tier icon of a grade is the texture `HardcoreServer_Tier<key - 1>` (grade 0
uses the last one, `HardcoreServer_Tier09`). Client 3474:

| `grade_key` | `rank` | `percent` | Name (LOC type 37) |
| ----------- | ------ | --------- | ------------------ |
| `0`         | `0`    | `0`       | Novice             |
| `1`         | `1`    | `0`       | Transcendent       |
| `2`         | `2`    | `0`       | Conqueror          |
| `3`         | `3`    | `0`       | Reaper             |
| `4`         | `0`    | `1`       | Honorblade         |
| `5`         | `0`    | `5`       | Dawnblade          |
| `6`         | `0`    | `10`      | Flameblade         |
| `7`         | `0`    | `30`      | Duskblade          |
| `8`         | `0`    | `50`      | Veteran            |
| `9`         | `0`    | `100`     | Adept              |

## Field Names

The Hardcore channel is newer than client 1784: no sheet of a private
server's `DataSheets.bexcel` on that client and no string of its server
dump has `HardCore` in the name. The names follow the client Lua of client
3474 (`panel_widget_ranking_hardcore_1.luac`):

| Field            | Lua                                                                                                   |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| `rank_threshold` | `ToClient_GetHardCoreTotalRankThreshold()`, the number of ranking slots the window builds (`_highRankerMaxCount`); the window scrolls, and `100` is the only head value that fits |
| `grade_key`      | `ToClient_GetHardCoreTotalRankGradeKeyByRank(rank)` returns it, and the window indexes its tiers by it |
| `rank`           | Grades 1 to 3 hold ranks 1 to 3, the three top ranks the window draws with the `1st`, `2nd` and `3rd` slots (`_topRankerCount = 3`) |
| `percent`        | `ToClient_GetHardCoreTotalRankGradePercentByKey(key)` for keys 4 to 9, shown as "Top {percent}%"     |

## Notes

- The file is byte-identical on clients 3002, 3251 and 3474; clients 1784
  and 2519 do not ship it.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/hardcore_tables.py`:
  one row per grade with its name, and `rank_threshold` on every row.

## Open Questions

### The Second Head Value

What `unknown_08` (`3`) is. It equals the number of grades held by one rank
and the ranking window's own `_topRankerCount`, but the window sets that
count in its Lua and calls no getter for it.
