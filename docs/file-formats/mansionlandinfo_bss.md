# `mansionlandinfo.bss` Format

## Purpose

The manors a player rents by the day: one fixed 93-byte row per manor with
the land and building house keys, the contribution points the land costs,
the manor's region, its area as a sector box, the quest that unlocks the
rental and the daily price. Client 3474 lists Blue Maned Lion's Manor and
the three Land of the Morning Light manors Shimhyangje, Solbaram Neowa
House and Hyeollokdang. The manor contract window
(`panel_window_mansioncontract_all_1.luac`) knows the four land keys as
`_eMansionKey` and reads the contribution cost with
`ToClient_getNeenPointMansion(characterKey)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records               | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | --------------------- | --------- |
| 3      | 3002 and later | 3474    | `mansionlandinfo.bss` | 392   | 4 Row                 | 93        |
| 2      | 2519           | 2519    | `mansionlandinfo.bss` | 251   | 3 Row                 | 77        |
| 1      | 1784 to 2107   | 2107    | `mansionlandinfo.bss` | 88    | 1 Row, 1 String Table | 68        |

| Layout | File                  | Known         | Unknown       |
| ------ | --------------------- | ------------- | ------------- |
| 3      | `mansionlandinfo.bss` | 180 B (45.9%) | 212 B (54.1%) |
| 2      | `mansionlandinfo.bss` | 140 B (55.8%) | 111 B (44.2%) |
| 1      | `mansionlandinfo.bss` | 60 B (68.2%)  | 28 B (31.8%)  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                   |
| ---------------------------- | -------- | -------------------------------------------------------------------------------------- |
| `mansionpartinfo.bss`        | Optional | The installation mode parts of each manor building; see [`mansionpartinfo.bss`](mansionpartinfo_bss.md) |
| `languagedata_en.loc`        | Optional | Manor names (type 6), region names (type 17), quest titles (type 18)                   |

All multi-byte values are little-endian.

## Layout 3

### File Layout

The PABR frame of `buffsimply.bss` with fixed rows and an empty string
table.

| Offset              | Type          | Field        | Notes                                          |
| ------------------- | ------------- | ------------ | ---------------------------------------------- |
| `+0x00`             | char[4]       | magic        | ASCII `PABR`                                   |
| `+0x04`             | u32           | count        | Number of rows; 4 on client 3474               |
| `+0x08`             | Row[count]    | rows         | See Row                                        |
| `rows+0x00`         | String Table  | string_table | See String Table                               |
| `string_table+0x00` | u32           | table_start  | Offset of the string table, where the rows end |
| `string_table+0x04` | u32           | zero         | Always 0                                       |

### Row (93 bytes)

| Offset  | Type   | Field                    | Notes                                                                                     |
| ------- | ------ | ------------------------ | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16    | land_character_key       | Row key: the manor land, a [`houseinfo.bss`](houseinfo_bss.md) house and `characterstatic.dbss` character |
| `+0x02` | u16    | building_character_key   | The manor building, a `houseinfo.bss` house; the manor key of `mansionpartinfo.bss`       |
| `+0x04` | u16    | need_point               | Contribution points to rent the manor; `5` on every row (client 3474)                     |
| `+0x06` | u16    | region_key               | `regioninfo.bss` region of the manor; its LOC type 17 name is the manor's name            |
| `+0x08` | i32[3] | sector_start             | Lowest sector (x, y, z) of the manor area, 12,800 units a sector                          |
| `+0x14` | i32[3] | sector_end               | Highest sector (x, y, z), inclusive                                                       |
| `+0x20` | i32[3] | unknown_20               | `sector_start` times 3 on every row; see Open Questions                                   |
| `+0x2C` | i32[3] | unknown_2c               | `sector_end` times 3 on every row                                                         |
| `+0x38` | u16    | condition_quest_chain_id | Quest that unlocks the rental: chain (LOC type 18 `str_id1`)                              |
| `+0x3A` | u16    | condition_quest_id       | Quest number in the chain (LOC type 18 `str_id2`)                                         |
| `+0x3C` | u32    | day_pay                  | Silver per day of rent; `1,000,000` or `100,000` (client 3474)                            |
| `+0x40` | f32    | unknown_40               | `0` on every row (clients 1784 and 3474)                                                  |
| `+0x44` | f32    | unknown_44               | `1000`, `0`, `500`, `0` in row order (client 3474)                                        |
| `+0x48` | f32    | unknown_48               | `0`, `0`, `0`, `600`                                                                      |
| `+0x4C` | f32    | unknown_4c               | `500`, `0`, `500`, `500`                                                                  |
| `+0x50` | u8     | unknown_50               | `1`, `2`, `0`, `3`                                                                        |
| `+0x51` | f32[3] | unknown_51               | A world position (x, y, z) inside the row's sector box on every row                       |

Rows on client 3474 in file order: Shimhyangje (land 3841), Solbaram Neowa
House (3843), Blue Maned Lion's Manor (3814), Hyeollokdang (3847).

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3474          |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries; none in the file |

## Layout 2

Client 2519 rows have no `unknown_48` and no `unknown_51`: 77 bytes. The
file holds Shimhyangje, Solbaram Neowa House and Blue Maned Lion's Manor.
Only the Row differs from Layout 3.

### Row (77 bytes)

| Offset  | Type   | Field                    | Notes                                    |
| ------- | ------ | ------------------------ | ---------------------------------------- |
| `+0x00` | u16    | land_character_key       |                                          |
| `+0x02` | u16    | building_character_key   |                                          |
| `+0x04` | u16    | need_point               |                                          |
| `+0x06` | u16    | region_key               |                                          |
| `+0x08` | i32[3] | sector_start             |                                          |
| `+0x14` | i32[3] | sector_end               |                                          |
| `+0x20` | i32[3] | unknown_20               |                                          |
| `+0x2C` | i32[3] | unknown_2c               |                                          |
| `+0x38` | u16    | condition_quest_chain_id |                                          |
| `+0x3A` | u16    | condition_quest_id       |                                          |
| `+0x3C` | u32    | day_pay                  |                                          |
| `+0x40` | f32    | unknown_40               |                                          |
| `+0x44` | f32    | unknown_44               | Same values as client 3474 for the 3 rows |
| `+0x48` | f32    | unknown_4c               | Same values as client 3474 for the 3 rows |
| `+0x4C` | u8     | unknown_50               | Same values as client 3474 for the 3 rows |

## Layout 1

Rows of clients 1784 and 2107 end after `unknown_40`: 68 bytes, with no
`unknown_44`, `unknown_4c` and `unknown_50`. The file holds Blue Maned
Lion's Manor alone. Only the Row differs from Layout 2.

### Row (68 bytes)

| Offset  | Type   | Field                    | Notes                  |
| ------- | ------ | ------------------------ | ---------------------- |
| `+0x00` | u16    | land_character_key       |                        |
| `+0x02` | u16    | building_character_key   |                        |
| `+0x04` | u16    | need_point               |                        |
| `+0x06` | u16    | region_key               |                        |
| `+0x08` | i32[3] | sector_start             |                        |
| `+0x14` | i32[3] | sector_end               |                        |
| `+0x20` | i32[3] | unknown_20               |                        |
| `+0x2C` | i32[3] | unknown_2c               |                        |
| `+0x38` | u16    | condition_quest_chain_id |                        |
| `+0x3A` | u16    | condition_quest_id       |                        |
| `+0x3C` | u32    | day_pay                  |                        |
| `+0x40` | f32    | unknown_40               | `0` on client 1784     |

## Field Names

The `MansionLand_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has one row with the columns `LandCharacterKey` (3814),
`BuildingCharacterKey` (3815), `NeedPoint` (5), `Region` (1095),
`SectorStartPosion` (`6, -1, -4`), `SectorEndPosition` (`8, 0, -2`),
`Condition` (`2063,8;`) and `DayPay` (1000000). The one row of client 1784
and the Blue Maned Lion's Manor row of client 3474 hold these values in
this order, 1 of 1 keys on both clients. The sheet has no column for
`unknown_20` to `unknown_51`.

- `land_character_key`: the four keys are the `_eMansionKey` values of the
  manor contract window (`_hidelOut` 3814, `_simHayngOut` 3841,
  `_neoWhaOut` 3843, `_hyunRokOut` 3847). The window passes the visited
  house's character key to `ToClient_getNeenPointMansion()` and stops on
  `-1`, "house info not found".
- `condition_quest_chain_id`, `condition_quest_id`: the sheet's `Condition`
  pair. Each row's pair is a quest (client 3474): 2063/8 "[Manor] A
  Father's Heart" on Blue Maned Lion's Manor, 8516/1 "[LoML] Ruler of
  Taebaek", 8510/9 "[LoML] Dokkebi's Gift" and 8541/3 "[Traveler] Dawn That
  Banishes Darkness" on the other three.
- `region_key`: 1095, 1214, 1228 and 1431 are named Blue Maned Lion's
  Manor, Shimhyangje, Solbaram Neowa House and Hyeollokdang in LOC type 17.
- `sector_start` and `sector_end`: `unknown_51` of each row lies inside the
  box when divided by 12,800 (Blue Maned Lion's Manor: `97168, -2120,
  -30883`, sector `7, -1, -3`).

## Notes

- Each `building_character_key` is a manor of
  [`mansionpartinfo.bss`](mansionpartinfo_bss.md) (3815, 3842, 3844,
  3848), and both keys of every row are house rows of `houseinfo.bss`.
- The land and the building share one LOC type 6 name per manor.
- The contract window reads the daily price from
  `ToClient_GetMansionPricePerDay()`, which takes no manor key; whether it
  returns `day_pay` of the visited manor is not shown by the Lua.

## Open Questions

### What is the second sector box?

`unknown_20` and `unknown_2c` hold `sector_start` and `sector_end` times 3
on all four rows (client 3474) and on the row of client 1784: a box in
units of a third of a sector (4,266.67). Nothing in the client Lua reads
it, and the sheet has no column for it.

### What do `unknown_40` to `unknown_51` hold?

Client 3474 adds four f32 values, a u8 and three f32 values to each row.
The last three are a world position inside the manor's sector box; the u8
is `0` on Blue Maned Lion's Manor and `1` to `3` on the three Land of the
Morning Light manors in the order of their land keys. The four f32 values
are `0`, `500`, `600` or `1000`. No client Lua getter names them.
