# `rosewarinfo.bss` Format

## Purpose

The two colours of the Rose War region map
(`ui_texture/minimap/area/elfwar_siegemap.bmp`; the Rose War is `ElfWar` in
the client's file names), one 9-byte row each. A u32 count follows the PABR
magic. Each row has the shape of an
[`edaniaregioninfo.bss`](edaniaregioninfo_bss.md) row: the colour and a
zero byte twice, then a u8. On client 3474 the rows are `10 0D 10` with `0`
and `E8 1B 18` with `1`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ----------------- | ----- | ------- | --------- |
| 1      | 3002 and later | 3474    | `rosewarinfo.bss` | 38    | 2 Row   | 9         |

| Layout | File              | Known        | Unknown      |
| ------ | ----------------- | ------------ | ------------ |
| 1      | `rosewarinfo.bss` | 26 B (68.4%) | 12 B (31.6%) |

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
| 794    | No file  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type            | Field        | Notes                                                      |
| ------------------- | --------------- | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]         | magic        | ASCII `PABR`                                               |
| `+0x04`             | u32             | row_count    | Number of rows                                             |
| `+0x08`             | Row[row_count]  | rows         | See Row; byte-packed                                       |
| `rows+0x00`         | String Table    | string_table | See String Table                                           |
| `string_table+0x00` | u32             | table_start  | Offset of the string table, where `rows` ends              |
| `string_table+0x04` | u32             | zero         | Always `0`                                                 |

### Row (9 bytes)

| Offset  | Type     | Field      | Notes                                                              |
| ------- | -------- | ---------- | ------------------------------------------------------------------ |
| `+0x00` | bytes[3] | map_color  | Region map colour, stored blue, green, red; `10 0D 10` and `E8 1B 18` on client 3474 |
| `+0x03` | u8       | unknown_03 | Always `0`                                                         |
| `+0x04` | bytes[3] | unknown_04 | Equals `map_color` on every row                                    |
| `+0x07` | u8       | unknown_07 | Always `0`                                                         |
| `+0x08` | u8       | unknown_08 | `0` and `1`, one per row                                           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Notes

- Raw bytes on clients 3002 to 3474:
  `50 41 42 52 02 00 00 00 10 0D 10 00 10 0D 10 00 00 E8 1B 18 00 E8 1B 18 00 01 00 00 00 00 1A 00 00 00 00 00 00 00`
  (38 bytes). The file is not in the archives of clients 794 to 2519.
- The same two rows close `hardcorechannelinfo.bss` on client 3474, a
  15-row file of this row shape: `E8 1B 18` with `1`, then `10 0D 10`
  with `0`. `10 0D 10` is also the colour of the `_Count` row of
  `edaniaregioninfo.bss`.
- `map_color` follows `ui_texture/minimap/area/elfwar_siegemap.bmp.rid`, the
  palette of the Rose War region map, which lists exactly these two colours
  (`100d10` first) on client 3474; the same holds for the region maps of
  three other tables of this row shape
  ([`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md#field-names)
  Field Names). Read as `rrggbb` the rows are `100d10` (near black) and
  `181be8` (blue).
- The file is newer than client 1784: no sheet of a private server's
  `DataSheets.bexcel` on that client and no string of its server dump has
  `RoseWar` in the name.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`:
  `map_color` as `rrggbb`.

## Open Questions

### The Value of Each Colour

What `unknown_08` stands for, and what the second copy of the colour is
for. The Rose War region map has one colour besides the `100d10` that
every region map palette lists first, so `unknown_08` (`1` for it, `0` for
`100d10`) marks the one area and does not pick between the Kamasylvia and
O'dyllita teams of
[`rosewarteamnostaticstatus.bss`](rosewarteamnostaticstatus_bss.md). The
client 3474 Lua has `getRoseWarTeamNo` and the two `__eRoseWarTeam_*`
names, and no call that returns a colour.
