# `siegeinfo.bss` Format

## Purpose

The areas of the Conquest War (siege) region map, one row per colour of
`ui_texture/minimap/area/siegemap.bmp`: the colour, a copy of it, whether
the area is a siege area and the territory it belongs to. Client 3482 has
six rows: one per territory from Balenos to Valencia and the `c8c8c8`
row with no territory. The rows open like the 9-byte rows of
[`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md) and its siblings,
with a u8 and a u16 territory key in place of their last u8.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------- | ----- | ------- | --------- |
| 1      | 1784 and later | 3482    | `siegeinfo.bss` | 86    | 6 Row   | 11        |

| Layout | File            | Known        | Unknown      |
| ------ | --------------- | ------------ | ------------ |
| 1      | `siegeinfo.bss` | 74 B (86.0%) | 12 B (14.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3482   | Layout 1             |
| 3474   | Layout 1             |
| 3251   | Layout 1             |
| 3002   | Layout 1             |
| 2765   | Layout 1             |
| 2519   | Layout 1             |
| 2313   | Layout 1             |
| 2107   | Layout 1             |
| 1937   | Layout 1             |
| 1784   | Layout 1             |
| 1636   | No documented layout |
| 1485   | No documented layout |
| 1348   | No documented layout |
| 1230   | No documented layout |
| 1058   | No file              |
| 794    | No documented layout |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12 |

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

### Row (11 bytes)

| Offset  | Type     | Field         | Notes                                                                      |
| ------- | -------- | ------------- | -------------------------------------------------------------------------- |
| `+0x00` | bytes[3] | map_color     | Region map colour, stored blue, green, red; unique per row. See Map Colours |
| `+0x03` | u8       | unknown_03    | Always `0`                                                                 |
| `+0x04` | bytes[3] | map_color_dup | Equals `map_color` on every row; see Field Names                           |
| `+0x07` | u8       | unknown_07    | Always `0`                                                                 |
| `+0x08` | u8       | is_siege      | `1` on the five territory rows, `0` on the `c8c8c8` row                    |
| `+0x09` | i16      | territory_key | `territoryinfo.bss` key, LOC type 12 name; `-1` on the `c8c8c8` row        |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Map Colours

Client 3482, in file order: `map_color` read as `rrggbb`. The `.rid`
position is the colour's place in `siegemap.bmp.rid`, which lists the six
colours in the same order as this file.

| `map_color` | `is_siege` | `territory_key` | Position in `.rid` |
| ----------- | ---------- | --------------- | ------------------ |
| `c8c8c8`    | 0          | -1              | 1                  |
| `323264`    | 1          | 4 Valencia      | 2                  |
| `643232`    | 1          | 3 Mediah        | 3                  |
| `0a0a64`    | 1          | 2 Calpheon      | 4                  |
| `0a640a`    | 1          | 1 Serendia      | 5                  |
| `640a0a`    | 1          | 0 Balenos       | 6                  |

## Field Names

The `Siege_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `R`, `G`, `B`, `IsSiege` and `TerritoryKey`
and six rows. The file is byte-identical on clients 1784 and 3482, and
every sheet row matches one file row by its colour (6 of 6): `B`, `G`, `R`
are the three `map_color` bytes in file order, and `IsSiege` and
`TerritoryKey` (`<null>` on the `200, 200, 200` row) are the last two
fields. The sheet lists the rows in another order (territory 0 first).

The 2016 `gc::SiegeInfo` starts with `pa::Color _colorKey` (members `b`,
`g`, `r`, `a`) and holds `bool _canSiegeInstall`; it has no territory key
yet. So the row is the colour the table is keyed by, then the struct's own
`_colorKey` (`map_color_dup`, with `unknown_07` its `a` byte) and its
members packed. `map_color` follows
[`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md), Field Names: on
client 3482 `siegemap.bmp.rid` lists exactly the six `map_color` values.

## Notes

- The file is byte-identical on clients 1784 and 3482. Clients 1230 to
  1636 hold a row that no layout here reads yet.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/siege_tables.py`: `map_color` as `rrggbb`, `is_siege`
  and the territory with its name.
