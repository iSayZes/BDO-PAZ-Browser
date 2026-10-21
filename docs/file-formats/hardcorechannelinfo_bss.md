# `hardcorechannelinfo.bss` Format

## Purpose

The colours of the Hardcore channel's region map, one 9-byte row each: the
colour, a copy of it, and a u8 from `0` to `4`. The 15 colours on client
3474 are the 15 that `ui_texture/minimap/area/hardcorechannelmap.bmp.rid`
lists for the map bitmap of the same name, so each row ties one area of that
map to a value. The rows have the shape of
[`edaniaregioninfo.bss`](edaniaregioninfo_bss.md),
[`rosewarinfo.bss`](rosewarinfo_bss.md) and
[`snowboardcourseinfo.bss`](snowboardcourseinfo_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `hardcorechannelinfo.bss` | 155   | 15 Row  | 9         |

| Layout | File                      | Known        | Unknown      |
| ------ | ------------------------- | ------------ | ------------ |
| 1      | `hardcorechannelinfo.bss` | 65 B (41.9%) | 90 B (58.1%) |

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

None.

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

### Row (9 bytes)

| Offset  | Type     | Field      | Notes                                                                                   |
| ------- | -------- | ---------- | --------------------------------------------------------------------------------------- |
| `+0x00` | bytes[3] | map_color  | Region map colour, stored blue, green, red; unique per row. See Map Colours             |
| `+0x03` | u8       | unknown_03 | Always `0`                                                                              |
| `+0x04` | bytes[3] | unknown_04 | Equals `map_color` on every row                                                         |
| `+0x07` | u8       | unknown_07 | Always `0`                                                                              |
| `+0x08` | u8       | unknown_08 | `0` to `4`; several rows share a value. See Open Questions                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Map Colours

`map_color` read as `rrggbb`, with `unknown_08`, in file order (client
3474). The `.rid` order is the order of the region map's palette file.

| `map_color` | `unknown_08` | Position in `hardcorechannelmap.bmp.rid` |
| ----------- | ------------ | ---------------------------------------- |
| `ff14ff`    | `3`          | 4                                        |
| `14ff14`    | `3`          | 9                                        |
| `ffff14`    | `3`          | 12                                       |
| `14ffff`    | `3`          | 13                                       |
| `c800ff`    | `4`          | 11                                       |
| `6414ff`    | `3`          | 6                                        |
| `1464ff`    | `3`          | 10                                       |
| `c80000`    | `4`          | 8                                        |
| `c8c800`    | `4`          | 5                                        |
| `00c8ff`    | `4`          | 14                                       |
| `000096`    | `4`          | 3                                        |
| `009696`    | `4`          | 7                                        |
| `6464ff`    | `2`          | 15                                       |
| `181be8`    | `1`          | 2                                        |
| `100d10`    | `0`          | 1                                        |

## Field Names

The Hardcore channel is newer than client 1784: no sheet of a private
server's `DataSheets.bexcel` on that client and no string of its server
dump has `HardCore` in the name. `map_color` follows the region map files.
The client has one `<name>map.bmp.bkd` and `<name>map.bmp.rid` pair per
region map in `ui_texture/minimap/area/`, and each `.rid` is a PABR file
holding a u32 count and that many 4-byte colours (the 3 colour bytes and a
zero byte, in this file's byte order). On client 3474 four `.rid` files list
exactly the colours of the four 9-byte-row tables:

| Map file                  | Colours | Table                                                  |
| ------------------------- | ------- | ------------------------------------------------------ |
| `hardcorechannelmap.bmp`  | 15      | `hardcorechannelinfo.bss`                              |
| `edaniaregionmap.bmp`     | 11      | [`edaniaregioninfo.bss`](edaniaregioninfo_bss.md)       |
| `elfwar_siegemap.bmp`     | 2       | [`rosewarinfo.bss`](rosewarinfo_bss.md) (the Rose War is `ElfWar` in the client's file names) |
| `snowboardcoursemap.bmp`  | 2       | [`snowboardcourseinfo.bss`](snowboardcourseinfo_bss.md) |

Every `.rid` lists `10 0D 10` first. This file, `rosewarinfo.bss` and
`snowboardcourseinfo.bss` give it the u8 `0`, `edaniaregioninfo.bss` the
`_Count` value `10` ("no Edania region").

## Notes

- The file is byte-identical on clients 3002, 3251 and 3474; clients 1784
  and 2519 do not ship it.
- The `rosewarinfo.bss` row `E8 1B 18` with `1` and the shared `10 0D 10`
  row with `0` are the last two rows here as well.
- Only `000096` equals a `regioninfo.bss` `color`, that of region 264
  (Epheria Valley).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/hardcore_tables.py`:
  `map_color` as `rrggbb`.

## Open Questions

### The Value of Each Colour

What `unknown_08` stands for. The client Lua of client 3474 checks the
player's area with `ToClient_HardCoreSelfplayerRegionCheck(__eHardCoreChannelRegionSafe)`
(`ui_widget_skillcommand.luac`), so the value may be an
`__eHardCoreChannelRegion*` area type, but `Safe` is the only member the Lua
names and none of the values. Five rows hold `3`, seven `4`, one each `0`,
`1` and `2`.

### Why the Colour Is Stored Twice

`unknown_04` equals `map_color` on every row, as the second copy does in
the three other 9-byte-row tables, and `unknown_03` and `unknown_07` are
always `0`. No source names the copy.
