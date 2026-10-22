# `oceansiegeinfo.bss` Format

## Purpose

The areas of the Blue Battlefield (ocean siege) region map, one row per
colour of `ui_texture/minimap/area/oceansiegemap.bmp`: the colour, a copy
of it, the islands (region keys) the area covers and a u16 that numbers
the rows. The rows open like the 9-byte rows of
[`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md) and its siblings,
with a counted region list and the u16 in place of their last u8.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | ----------------------- |
| 1      | 3002 and later | 3482    | `oceansiegeinfo.bss` | 480   | 29 Row  | 14 to 16, 16 on average |

| Layout | File                 | Known         | Unknown       |
| ------ | -------------------- | ------------- | ------------- |
| 1      | `oceansiegeinfo.bss` | 277 B (57.7%) | 203 B (42.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | No file  |
| 2519   | No file  |
| 2107   | No file  |
| 1937   | No file  |
| 1784   | No file  |
| 1636   | No file  |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                              |
| --------------------- | -------- | ------------------------------------------------- |
| `languagedata_en.loc` | Optional | Region names, LOC type 17, for the `region_keys` cell |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 14 bytes + region keys)

| Offset             | Type                   | Field                  | Notes                                                                                   |
| ------------------ | ---------------------- | ---------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`            | bytes[3]               | map_color              | Region map colour, stored blue, green, red; unique per row. See Map Colours             |
| `+0x03`            | u8                     | unknown_03             | Always `0`                                                                              |
| `+0x04`            | bytes[3]               | unknown_04             | Equals `map_color` on every row                                                         |
| `+0x07`            | u8                     | unknown_07             | Always `0`                                                                              |
| `+0x08`            | u32                    | region_key_count       | Number of `region_keys`; `0` or `1` on every client checked                             |
| `+0x0C`            | u16[region_key_count]  | region_keys            | `regioninfo.bss` region keys, LOC type 17 names; each an island. See Map Colours         |
| `region_keys+0x00` | u16                    | unknown_region_keys_00 | `0` to `28` on client 3482, unique per row. See Open Questions                           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Map Colours

Client 3482, in file order: `map_color` read as `rrggbb`, the island,
its territory in `regioninfo.bss` and the u16 after the list. The `.rid`
position is the colour's place in `oceansiegemap.bmp.rid`.

| `map_color` | `region_keys`            | Territory | `unknown_region_keys_00` | Position in `.rid` |
| ----------- | ------------------------ | --------- | ------------------------ | ------------------ |
| `dd0b0b`    | 365 Balvege Island       | Balenos   | 7                        | 10                 |
| `100d10`    | none                     |           | 0                        | 1                  |
| `59d1c9`    | 394 Louruve Island       | Balenos   | 4                        | 13                 |
| `739bd7`    | none                     |           | 1                        | not listed         |
| `0f735f`    | 373 Invernen Island      | Balenos   | 2                        | 4                  |
| `9bb642`    | 392 Narvo Island         | Balenos   | 3                        | 2                  |
| `f6f340`    | 393 Marka Island         | Balenos   | 5                        | 12                 |
| `f06432`    | 407 Theonil Island       | Calpheon  | 26                       | 25                 |
| `1334b9`    | 366 Angie Island         | Balenos   | 6                        | 14                 |
| `617ac3`    | 364 Marlene Island       | Balenos   | 8                        | 7                  |
| `eea342`    | 367 Duch Island          | Balenos   | 9                        | 21                 |
| `61c3a9`    | 368 Eveto Island         | Balenos   | 10                       | 19                 |
| `c3b061`    | 371 Mariveno Island      | Balenos   | 11                       | 18                 |
| `ef4ccb`    | 369 Luivano Island       | Balenos   | 12                       | 22                 |
| `71c361`    | 377 Baremi Island        | Balenos   | 13                       | 5                  |
| `a661c3`    | 378 Weita Island         | Balenos   | 14                       | 11                 |
| `96c83c`    | 403 Albresser Island     | Calpheon  | 20                       | 20                 |
| `42ee7e`    | 379 Paratama Island      | Balenos   | 15                       | 15                 |
| `3c3834`    | 388 Al-Naha Island       | Balenos   | 16                       | 3                  |
| `aa321e`    | 566 Arita Island         | Calpheon  | 17                       | 6                  |
| `fabe64`    | 564 Padix Island         | Calpheon  | 18                       | 8                  |
| `1ec80a`    | 400 Oben Island          | Calpheon  | 21                       | 17                 |
| `fafa64`    | 565 Teste Island         | Calpheon  | 19                       | 9                  |
| `50fac8`    | 398 Daton Island         | Calpheon  | 22                       | 16                 |
| `0aaaf0`    | 396 Randis Island        | Calpheon  | 23                       | 26                 |
| `0a32f0`    | 405 Ginburrey Island     | Calpheon  | 24                       | 24                 |
| `c80af0`    | 409 Baeza Island         | Calpheon  | 25                       | 27                 |
| `f00aaa`    | 406 Rameda Island        | Calpheon  | 27                       | 23                 |
| `e62850`    | 410 Teyamal Island       | Calpheon  | 28                       | 28                 |

## Field Names

The Blue Battlefield is newer than client 1784: the file is not in its
archives and no sheet of a private server's `DataSheets.bexcel` on that
client has `Ocean` and `Siege` in its name. `map_color` follows
[`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md), Field Names: on
client 3482 `oceansiegemap.bmp.rid` lists 28 colours, and all 28 are
`map_color` values of this file, `10 0D 10` first. `region_keys` are
`regioninfo.bss` keys: all 27 are islands (region type Hunting, node war
day Friday), 15 in Balenos and 12 in Calpheon, the two territories of
`CppEnums.OceanSiegeTerritoryName` in `global_define_cpp_enum.luac`
(client 3482).

## Notes

- Clients 3002 and 3251 hold 17 rows (288 bytes): the `100d10` and
  `739bd7` rows and the 15 Balenos islands, each with the same values as on
  client 3482. Client 3482 adds the 12 Calpheon island rows.
- The `100d10` row, first in every region map palette, has no region and
  `unknown_region_keys_00` `0`, as the shared `10 0D 10` row of the other
  map colour tables has `0`. The `739bd7` row has no region either and is
  the one colour the `.rid` does not list.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/oceansiege_tables.py`: `map_color` as `rrggbb` and the
  region keys with their names.

## Open Questions

### The u16 After the Region List

`unknown_region_keys_00` is `0` to `28` on client 3482, one value per
row, but not in file order (`7, 0, 4, 1, 2, ...`) and not in `.rid`
order. The Lua walks the ocean siege territories with
`ToClient_GetOceanSiegeTerritoryByIndex(groupIdx, territory_idx)` and
reads no area or island index, so what the number counts is open.

### Why the Colour Is Stored Twice

`unknown_04` equals `map_color` on every row, as in the 9-byte-row
tables, and `unknown_03` and `unknown_07` are always `0`. No source names
the copy.
