# `greatsea.bss` Format

## Purpose

The areas of the Great Ocean map: one row per colour of
`ui_texture/minimap/area/greatseamap.bmp`, with three f32 values, a
magnification, a list of vehicle types, a restricted area state and a
wind impact value. On client 3482 two rows list vehicle types, the same
five ship types of `CppEnums.VehicleType` from `Type_Carrack` to
`Type_SailingBoat`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File           | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | -------------- | ----- | ------- | ----------------------- |
| 1      | 1256 and later | 3482    | `greatsea.bss` | 5,173 | 139 Row | 37 to 42, 37 on average |

| Layout | File           | Known           | Unknown       |
| ------ | -------------- | --------------- | ------------- |
| 1      | `greatsea.bss` | 4,478 B (86.6%) | 695 B (13.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3454   | Layout 1 |
| 3412   | Layout 1 |
| 3381   | Layout 1 |
| 3349   | Layout 1 |
| 3314   | Layout 1 |
| 3283   | Layout 1 |
| 3251   | Layout 1 |
| 3212   | Layout 1 |
| 3177   | Layout 1 |
| 3144   | Layout 1 |
| 3103   | Layout 1 |
| 3062   | Layout 1 |
| 3037   | Layout 1 |
| 3002   | Layout 1 |
| 2959   | Layout 1 |
| 2923   | Layout 1 |
| 2900   | Layout 1 |
| 2872   | Layout 1 |
| 2834   | Layout 1 |
| 2803   | Layout 1 |
| 2765   | Layout 1 |
| 2736   | Layout 1 |
| 2703   | Layout 1 |
| 2665   | Layout 1 |
| 2637   | Layout 1 |
| 2606   | Layout 1 |
| 2583   | Layout 1 |
| 2545   | Layout 1 |
| 2519   | Layout 1 |
| 2498   | Layout 1 |
| 2468   | Layout 1 |
| 2438   | Layout 1 |
| 2414   | Layout 1 |
| 2384   | Layout 1 |
| 2358   | Layout 1 |
| 2335   | Layout 1 |
| 2313   | Layout 1 |
| 2290   | Layout 1 |
| 2250   | Layout 1 |
| 2224   | Layout 1 |
| 2203   | Layout 1 |
| 2179   | Layout 1 |
| 2151   | Layout 1 |
| 2134   | Layout 1 |
| 2107   | Layout 1 |
| 2073   | Layout 1 |
| 2052   | Layout 1 |
| 2011   | Layout 1 |
| 1996   | Layout 1 |
| 1969   | Layout 1 |
| 1937   | Layout 1 |
| 1914   | Layout 1 |
| 1886   | Layout 1 |
| 1866   | Layout 1 |
| 1838   | Layout 1 |
| 1818   | Layout 1 |
| 1794   | Layout 1 |
| 1784   | Layout 1 |
| 1749   | Layout 1 |
| 1717   | Layout 1 |
| 1698   | Layout 1 |
| 1674   | Layout 1 |
| 1636   | Layout 1 |
| 1608   | Layout 1 |
| 1587   | Layout 1 |
| 1565   | Layout 1 |
| 1537   | Layout 1 |
| 1509   | Layout 1 |
| 1485   | Layout 1 |
| 1466   | Layout 1 |
| 1445   | Layout 1 |
| 1426   | Layout 1 |
| 1409   | Layout 1 |
| 1390   | Layout 1 |
| 1372   | Layout 1 |
| 1360   | Layout 1 |
| 1348   | Layout 1 |
| 1338   | Layout 1 |
| 1324   | Layout 1 |
| 1316   | Layout 1 |
| 1309   | Layout 1 |
| 1286   | Layout 1 |
| 1256   | Layout 1 |
| 1230   | No file  |
| 1211   | No file  |
| 1194   | No file  |
| 1177   | No file  |
| 1156   | No file  |
| 1127   | No file  |
| 1109   | No file  |
| 1076   | No file  |
| 1058   | No file  |
| 1016   | No file  |
| 990    | No file  |
| 955    | No file  |
| 911    | No file  |
| 885    | No file  |
| 855    | No file  |
| 822    | No file  |
| 794    | No file  |
| 748    | No file  |
| 711    | No file  |
| 683    | No file  |
| 656    | No file  |
| 630    | No file  |
| 606    | No file  |
| 577    | No file  |
| 542    | No file  |
| 526    | No file  |
| 508    | No file  |
| 485    | No file  |
| 457    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

None. The handler names each vehicle type with its `CppEnums.VehicleType`
member name.

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

### Row (variable: 37 bytes + vehicle types)

| Offset               | Type                    | Field                 | Notes                                                                                 |
| -------------------- | ----------------------- | --------------------- | ------------------------------------------------------------------------------------- |
| `+0x00`              | bytes[3]                | map_color             | Great Ocean map colour, stored blue, green, red; unique per row                       |
| `+0x03`              | u8                      | unknown_03            | Always `0`                                                                            |
| `+0x04`              | bytes[3]                | unknown_04            | Equals `map_color` on every row                                                       |
| `+0x07`              | u8                      | unknown_07            | Always `0`                                                                            |
| `+0x08`              | f32                     | x                     | `-6` to `6` on client 3482                                                            |
| `+0x0C`              | f32                     | y                     | `0` to `71` on client 3482                                                            |
| `+0x10`              | f32                     | z                     | `-6` to `6` on client 3482                                                            |
| `+0x14`              | f32                     | magnification         | `1`, `1.25` or `1.7` on client 3482                                                   |
| `+0x18`              | u64                     | vehicle_type_count    | Number of `vehicle_types`; `0` or `5` on client 3482                                  |
| `+0x20`              | u8[vehicle_type_count]  | vehicle_types         | `CppEnums.VehicleType` values; `60, 56, 46, 44, 34` on both rows that have a list     |
| `vehicle_types+0x00` | u8                      | restricted_area_state | `0` on 137 rows, `1` and `2` on the two rows with vehicle types (client 3482)         |
| `vehicle_types+0x01` | u32                     | wind_impact           | Six values from `20000` to `500000` on client 3482                                    |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The `GreatSea_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `R`, `G`, `B`, `X`, `Y`, `Z`,
`Magnification`, `VehicleType`, `RestrictedAreaState` and `WindImpact` and
139 rows. Keyed by colour, all 139 rows of the client 1784 file match the
sheet on every column (139 of 139). `VehicleType` holds the list as text,
`60,56,46,44,34`. That server's dump names the members `GreatSeaStaticStatus
x`, `z`, `magnitude`, `WindImpact` and `State` in its check messages; the
field names follow the sheet columns.

On client 3482 the same 139 colours carry the same values except
`magnification`: seven rows read `1.25` where the sheet and the client
1784 file have `1`.

## Vehicle Types

The two rows with a list name the same five ships, in this order
(`global_define_cpp_enum.luac`, client 3482):

| Value | `CppEnums.VehicleType` |
| ----- | ---------------------- |
| 60    | `Type_Carrack`         |
| 56    | `Type_CashPersonalTradeShip` |
| 46    | `Type_PersonTradeShip` |
| 44    | `Type_PersonalBattleShip` |
| 34    | `Type_SailingBoat`     |

## Notes

- `map_color` follows the region map files, as in
  [`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md#field-names):
  on client 3482 `greatseamap.bmp.rid` lists 103 colours, `32 FF 00`
  first, and all 103 are `map_color` values of this file; the other 36
  rows are colours the `.rid` does not list.
- The two rows with vehicle types are `e0bfbf` (`restricted_area_state`
  `2`) and `e0cccc` (`1`), both with `x`, `y` and `z` `0` and the lowest
  `wind_impact`, `20000`.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/greatsea_tables.py`:
  `map_color` as `rrggbb`, the f32 values, the vehicle types with their
  names and the two values after them.

## Open Questions

### What `x`, `y` and `z` Hold

The three f32 values are small (`-6` to `6`, `0` to `71`), far below world
coordinates, and `y` grows where `x` and `z` move away from `0`. They may
be a wind or current vector per area, which `wind_impact` scales; no
client Lua names a getter for them.

### What the Restricted Area States Mean

Only the two rows with vehicle types have a `restricted_area_state`
(`1` and `2`). Whether the list names the ships allowed into the area or
the ones kept out is not in the client data checked.

### Why the Colour Is Stored Twice

`unknown_04` equals `map_color` on every row, and `unknown_03` and
`unknown_07` are always `0`, as in the other region map colour tables.
The sheet has one `R`, `G`, `B` set only.
