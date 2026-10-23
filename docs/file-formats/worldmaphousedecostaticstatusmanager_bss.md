# `worldmaphousedecostaticstatusmanager.bss` Format

## Purpose

The world map models of the guild siege buildings: per building character
(the command post and the four fortresses, `2008` to `2012`) the model the
world map draws at its place and the object change level the model stands
for.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                       | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | ------------------------------------------ | ----- | ------- | ----------------------- |
| 1      | 3002 and later | 3482    | `worldmaphousedecostaticstatusmanager.bss` | 210   | 5 Row   | 37 to 49, 41 on average |

| Layout | File                                       | Known          | Unknown    |
| ------ | ------------------------------------------ | -------------- | ---------- |
| 1      | `worldmaphousedecostaticstatusmanager.bss` | 210 B (100.0%) | 0 B (0.0%) |

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

None. The handler names the building through the character name lookup
(LOC type 6, then the Korean name).

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table: a row count, then the rows back to
back to the end of the file.

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 16 bytes + model name)

| Offset                        | Type | Field                 | Notes                                                                            |
| ----------------------------- | ---- | --------------------- | -------------------------------------------------------------------------------- |
| `+0x00`                       | u16  | character_key         | Building character (`2008` 지휘소, the command post); each key once               |
| `+0x02`                       | u16  | character_key_dup     | Equals `character_key` on every row                                              |
| `+0x04`                       | str8 | world_map_object_file | World map model name without extension (`Worldmap_Guild_Citadel_C`)             |
| `world_map_object_file+0x00`  | u32  | object_change_level   | `1` on every row                                                                 |

On client 3482 the five rows are in sheet order: `2008`, `2010`, `2011`,
`2012`, `2009`. Characters `2010` to `2012` share the model
`Worldmap_Guild_Citadel_C`.

## Field Names

The `WorlmapHouse_Table` sheet (sic) of a private server's
`DataSheets.bexcel` on client 1784 and the table of the same name of a
private server on client 519 have the columns `CharacterKey`,
`ObjectChangeLevel` and `WorldMapObjectFile`, in that order. All three
match on 5 of 5 keys (client 3482), and both u16 values equal
`CharacterKey`.

## Notes

- Client 3002 is the first test client with the file; client 2959 and
  older have none.
