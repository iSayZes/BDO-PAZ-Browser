# `worldmapdecostaticstatusmanager.bss` Format

## Purpose

The decoration models of the world map: per row a `.pam` model (town
houses, castles, farms, temples) with its world position, scale and
rotation. The world map draws these models over the terrain.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                  | Bytes  | Records | Row bytes               |
| ------ | -------------- | ------- | ------------------------------------- | ------ | ------- | ----------------------- |
| 1      | 3002 and later | 3482    | `worldmapdecostaticstatusmanager.bss` | 41,058 | 657 Row | 49 to 78, 62 on average |

| Layout | File                                  | Known            | Unknown        |
| ------ | ------------------------------------- | ---------------- | -------------- |
| 1      | `worldmapdecostaticstatusmanager.bss` | 39,744 B (96.8%) | 1,314 B (3.2%) |

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
| 2959   | No file  |
| 2923   | No file  |
| 2900   | No file  |
| 2872   | No file  |
| 2834   | No file  |
| 2803   | No file  |
| 2765   | No file  |
| 2736   | No file  |
| 2703   | No file  |
| 2665   | No file  |
| 2637   | No file  |
| 2606   | No file  |
| 2583   | No file  |
| 2545   | No file  |
| 2519   | No file  |
| 2498   | No file  |
| 2468   | No file  |
| 2438   | No file  |
| 2414   | No file  |
| 2384   | No file  |
| 2358   | No file  |
| 2335   | No file  |
| 2313   | No file  |
| 2290   | No file  |
| 2250   | No file  |
| 2224   | No file  |
| 2203   | No file  |
| 2179   | No file  |
| 2151   | No file  |
| 2134   | No file  |
| 2107   | No file  |
| 2073   | No file  |
| 2052   | No file  |
| 2011   | No file  |
| 1996   | No file  |
| 1969   | No file  |
| 1937   | No file  |
| 1914   | No file  |
| 1886   | No file  |
| 1866   | No file  |
| 1838   | No file  |
| 1818   | No file  |
| 1794   | No file  |
| 1784   | No file  |
| 1749   | No file  |
| 1717   | No file  |
| 1698   | No file  |
| 1674   | No file  |
| 1636   | No file  |
| 1608   | No file  |
| 1587   | No file  |
| 1565   | No file  |
| 1537   | No file  |
| 1509   | No file  |
| 1485   | No file  |
| 1466   | No file  |
| 1445   | No file  |
| 1426   | No file  |
| 1409   | No file  |
| 1390   | No file  |
| 1372   | No file  |
| 1360   | No file  |
| 1348   | No file  |
| 1338   | No file  |
| 1324   | No file  |
| 1316   | No file  |
| 1309   | No file  |
| 1286   | No file  |
| 1256   | No file  |
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

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table: a row count, then the rows back to
back to the end of the file.

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 32 bytes + model name)

| Offset                       | Type | Field                            | Notes                                                                    |
| ---------------------------- | ---- | -------------------------------- | ------------------------------------------------------------------------ |
| `+0x00`                      | u16  | deco_index                       | Row key; each key once                                                   |
| `+0x02`                      | str8 | world_map_object_file            | Model file name (`WofldMap_Velia_House_01.pam`, sic)                     |
| `world_map_object_file+0x00` | f32  | location_x                       | World position                                                           |
| `world_map_object_file+0x04` | f32  | location_y                       | World position, height                                                   |
| `world_map_object_file+0x08` | f32  | location_z                       | World position                                                           |
| `world_map_object_file+0x0C` | f32  | scale                            | Percent: `100` on 600 of 657 rows (client 3482), also `50`, `70`, `80`, `150` |
| `world_map_object_file+0x10` | f32  | rotation                         | Degrees (`96.27`, `-93`, `180`); `0` on 419 of 657 rows (client 3482)    |
| `world_map_object_file+0x14` | u16  | unknown_world_map_object_file_14 | `1` on every row of clients 3002 and 3482                                |

The rows are in no key order: client 3482 opens with keys 2049, 1, 1025,
513 and 2050. Keys run from 1 to 2187 with gaps.

## Field Names

The `WorlmapDeco_Table` sheet (sic) of a private server's
`DataSheets.bexcel` on client 1784 has the columns `Index`,
`WorldMapObjectFile`, `LocationX`, `LocationY`, `LocationZ`, `Rotation`
and `Scale`. Joined on `Index` = `deco_index`, every column matches on 488
of 488 shared keys (client 3482); the file stores `Scale` before
`Rotation`. The table of the same name of a private server on client 519
matches on 453 of 455 keys for the position and on 455 of 455 for scale
and rotation; its keys `1975` and `1976` hold other models or positions.
No column of either source holds the trailing u16.

## Notes

- Client 3002 is the first test client with the file, 605 rows; client
  2959 and older have none.

## Open Questions

### Trailing U16

`unknown_world_map_object_file_14` is `1` on every row and neither source
has a column for it. A visibility flag or a layer number would both fit; a
row with another value would tell them apart.
