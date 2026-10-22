# `siegeoccupycolor.bss` Format

## Purpose

A numbered colour palette for sieges ("occupy colour"): rows of an index
counting up from `1` and a four-byte colour. Client 3482 has 90 rows, all
colours unique and fully opaque. What the client paints with them is
open (see Open Questions).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ----- | ------- | --------- |
| 1      | 1636 and later | 3482    | `siegeoccupycolor.bss` | 740   | 90 Row  | 8         |

| Layout | File                   | Known          | Unknown    |
| ------ | ---------------------- | -------------- | ---------- |
| 1      | `siegeoccupycolor.bss` | 740 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2765   | Layout 1 |
| 2519   | Layout 1 |
| 2313   | Layout 1 |
| 2107   | Layout 1 |
| 1937   | Layout 1 |
| 1784   | Layout 1 |
| 1636   | Layout 1 |
| 1485   | No file  |
| 1348   | No file  |
| 1230   | No file  |
| 1058   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler reads only this file.

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

### Row (8 bytes)

| Offset  | Type     | Field | Notes                                                                    |
| ------- | -------- | ----- | ------------------------------------------------------------------------ |
| `+0x00` | u32      | index | `1` to `row_count` in file order                                         |
| `+0x04` | bytes[4] | color | Stored blue, green, red, alpha; alpha `ff` on every row of client 3482   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 holds
these rows. That server's dump (client 1784) names the loader
`GameCommonParameterLoaderFromExcel::loadMain(loadSiegeOccupyColor)`, the
table `SiegeOccupyColorStaticStatusManager` and the two members
`SiegeOccupyColorStaticStatus _index` and `SiegeOccupyColorStaticStatus
_color`, one per field of the 8-byte row.

## Notes

- Client 1784 holds the first 65 rows of client 3482 (540 bytes), each
  with the same colour; client 3482 adds indexes `66` to `90`.
- The colours are pale and mid tones (`3c3c3c` first, then `d5ffea`,
  `f3fed6`, ...), none of them in the `siegemap.bmp.rid` or
  `villagesiegemap_2024.bmp.rid` palettes.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/siege_tables.py`: `color` as `aarrggbb`.

## Open Questions

### What the Colours Paint

No client Lua of client 3482 names `OccupyColor`. The name and the 90
distinct colours fit one colour per occupying guild on the node war or
conquest war map, but nothing ties an index to a guild yet.
