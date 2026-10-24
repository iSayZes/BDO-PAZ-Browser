# `fieldinfo.bss` Format

## Purpose

The fields the game runs: the open world (field `1`), the test and story
instance fields and the 66 `A1_` fields of The Magnus. Each row is keyed by
the field number that [instancefield.dbss](instancefield_dbss.md) and
[instancedungeoninfo.dbss](instancedungeoninfo_dbss.md) store as
`field_no`, and holds the field's world-editor name, its resource folder, a
spawn point, its area as a sector box (in three units), its field type, the
keys of the [regionmapinfo.bss](regionmapinfo_bss.md) maps it uses (see
[Map Index Fields](#map-index-fields)) and its entry rules (players,
mounts, item drop rate). The file is the client copy
of the developers' `Field_Table` sheet (see [Field Names](#field-names)).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes  | Records | Row bytes |
| ------ | -------------- | ------- | --------------- | ------ | ------- | --------- |
| 2      | 2919 and later | 3483    | `fieldinfo.bss` | 23,620 | 122 Row | 157       |
| 1      | 1489 to 2308   | 2308    | `fieldinfo.bss` | 22,156 | 122 Row | 145       |

| Layout | File            | Known             | Unknown        |
| ------ | --------------- | ----------------- | -------------- |
| 2      | `fieldinfo.bss` | 22,156 B (93.8%)  | 1,464 B (6.2%) |
| 1      | `fieldinfo.bss` | 22,156 B (100.0%) | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 2             |
| 3482   | Layout 2             |
| 3474   | Layout 2             |
| 3473   | Layout 2             |
| 3464   | Layout 2             |
| 3458   | Layout 2             |
| 3454   | Layout 2             |
| 3444   | Layout 2             |
| 3435   | Layout 2             |
| 3426   | Layout 2             |
| 3418   | Layout 2             |
| 3412   | Layout 2             |
| 3402   | Layout 2             |
| 3396   | Layout 2             |
| 3387   | Layout 2             |
| 3381   | Layout 2             |
| 3373   | No documented layout |
| 3364   | No documented layout |
| 3356   | No documented layout |
| 3349   | No documented layout |
| 3342   | No documented layout |
| 3335   | No documented layout |
| 3326   | No documented layout |
| 3321   | No documented layout |
| 3314   | No documented layout |
| 3303   | Layout 2             |
| 3302   | Layout 2             |
| 3293   | Layout 2             |
| 3283   | Layout 2             |
| 3275   | Layout 2             |
| 3267   | Layout 2             |
| 3258   | Layout 2             |
| 3251   | Layout 2             |
| 3242   | Layout 2             |
| 3235   | Layout 2             |
| 3229   | Layout 2             |
| 3212   | Layout 2             |
| 3203   | Layout 2             |
| 3193   | Layout 2             |
| 3186   | Layout 2             |
| 3177   | Layout 2             |
| 3169   | Layout 2             |
| 3158   | Layout 2             |
| 3151   | No documented layout |
| 3144   | No documented layout |
| 3133   | No documented layout |
| 3125   | No documented layout |
| 3118   | No documented layout |
| 3111   | No documented layout |
| 3103   | No documented layout |
| 3095   | No documented layout |
| 3086   | No documented layout |
| 3072   | No documented layout |
| 3062   | No documented layout |
| 3052   | No documented layout |
| 3045   | No documented layout |
| 3037   | No documented layout |
| 3030   | No documented layout |
| 3021   | No documented layout |
| 3012   | No documented layout |
| 3002   | No documented layout |
| 2995   | No documented layout |
| 2987   | No documented layout |
| 2978   | No documented layout |
| 2970   | No documented layout |
| 2959   | Layout 2             |
| 2951   | Layout 2             |
| 2942   | Layout 2             |
| 2935   | Layout 2             |
| 2932   | Layout 2             |
| 2923   | Layout 2             |
| 2919   | Layout 2             |
| 2907   | No documented layout |
| 2900   | No documented layout |
| 2891   | No documented layout |
| 2882   | No documented layout |
| 2872   | No documented layout |
| 2863   | No documented layout |
| 2855   | No documented layout |
| 2849   | No documented layout |
| 2844   | No documented layout |
| 2834   | No documented layout |
| 2825   | No documented layout |
| 2819   | No documented layout |
| 2811   | No documented layout |
| 2803   | No documented layout |
| 2794   | No documented layout |
| 2783   | No documented layout |
| 2774   | No documented layout |
| 2765   | No documented layout |
| 2756   | No documented layout |
| 2750   | No documented layout |
| 2743   | No documented layout |
| 2736   | No documented layout |
| 2726   | No documented layout |
| 2717   | No documented layout |
| 2709   | No documented layout |
| 2703   | No documented layout |
| 2695   | No documented layout |
| 2684   | No documented layout |
| 2672   | No documented layout |
| 2665   | No documented layout |
| 2657   | No documented layout |
| 2649   | No documented layout |
| 2644   | No documented layout |
| 2637   | No documented layout |
| 2629   | No documented layout |
| 2619   | No documented layout |
| 2612   | No documented layout |
| 2606   | No documented layout |
| 2602   | No documented layout |
| 2601   | No documented layout |
| 2592   | No documented layout |
| 2583   | No documented layout |
| 2575   | No documented layout |
| 2567   | No documented layout |
| 2560   | No documented layout |
| 2553   | No documented layout |
| 2545   | No documented layout |
| 2538   | No documented layout |
| 2529   | No documented layout |
| 2519   | No documented layout |
| 2513   | No documented layout |
| 2510   | No documented layout |
| 2507   | No documented layout |
| 2503   | No documented layout |
| 2498   | No documented layout |
| 2492   | No documented layout |
| 2487   | No documented layout |
| 2480   | No documented layout |
| 2474   | No documented layout |
| 2468   | No documented layout |
| 2460   | No documented layout |
| 2453   | No documented layout |
| 2444   | No documented layout |
| 2438   | No documented layout |
| 2434   | No documented layout |
| 2429   | No documented layout |
| 2421   | No documented layout |
| 2414   | No documented layout |
| 2407   | No documented layout |
| 2401   | No documented layout |
| 2397   | No documented layout |
| 2393   | No documented layout |
| 2384   | No documented layout |
| 2378   | No documented layout |
| 2372   | No documented layout |
| 2358   | No documented layout |
| 2352   | No documented layout |
| 2347   | No documented layout |
| 2343   | No documented layout |
| 2335   | No documented layout |
| 2327   | No documented layout |
| 2324   | No documented layout |
| 2319   | No documented layout |
| 2313   | No documented layout |
| 2308   | Layout 1             |
| 2302   | Layout 1             |
| 2295   | Layout 1             |
| 2290   | Layout 1             |
| 2284   | Layout 1             |
| 2276   | Layout 1             |
| 2269   | Layout 1             |
| 2259   | Layout 1             |
| 2250   | Layout 1             |
| 2243   | Layout 1             |
| 2235   | Layout 1             |
| 2229   | Layout 1             |
| 2224   | Layout 1             |
| 2218   | Layout 1             |
| 2215   | Layout 1             |
| 2207   | Layout 1             |
| 2203   | Layout 1             |
| 2196   | Layout 1             |
| 2192   | Layout 1             |
| 2189   | Layout 1             |
| 2183   | Layout 1             |
| 2179   | Layout 1             |
| 2171   | Layout 1             |
| 2163   | Layout 1             |
| 2156   | Layout 1             |
| 2151   | Layout 1             |
| 2147   | Layout 1             |
| 2142   | Layout 1             |
| 2138   | Layout 1             |
| 2134   | Layout 1             |
| 2130   | Layout 1             |
| 2122   | Layout 1             |
| 2107   | Layout 1             |
| 2098   | Layout 1             |
| 2089   | Layout 1             |
| 2081   | Layout 1             |
| 2073   | Layout 1             |
| 2067   | Layout 1             |
| 2063   | Layout 1             |
| 2059   | Layout 1             |
| 2052   | Layout 1             |
| 2044   | Layout 1             |
| 2039   | Layout 1             |
| 2032   | Layout 1             |
| 2025   | Layout 1             |
| 2011   | Layout 1             |
| 2005   | Layout 1             |
| 2000   | Layout 1             |
| 1996   | Layout 1             |
| 1991   | Layout 1             |
| 1985   | Layout 1             |
| 1980   | Layout 1             |
| 1969   | Layout 1             |
| 1964   | Layout 1             |
| 1958   | Layout 1             |
| 1950   | Layout 1             |
| 1945   | Layout 1             |
| 1937   | Layout 1             |
| 1933   | Layout 1             |
| 1927   | Layout 1             |
| 1921   | Layout 1             |
| 1914   | Layout 1             |
| 1908   | Layout 1             |
| 1897   | Layout 1             |
| 1892   | Layout 1             |
| 1886   | Layout 1             |
| 1881   | Layout 1             |
| 1871   | Layout 1             |
| 1866   | Layout 1             |
| 1862   | Layout 1             |
| 1854   | Layout 1             |
| 1846   | Layout 1             |
| 1838   | Layout 1             |
| 1832   | Layout 1             |
| 1826   | Layout 1             |
| 1822   | Layout 1             |
| 1818   | Layout 1             |
| 1804   | Layout 1             |
| 1794   | Layout 1             |
| 1790   | Layout 1             |
| 1784   | Layout 1             |
| 1774   | Layout 1             |
| 1771   | Layout 1             |
| 1762   | Layout 1             |
| 1759   | Layout 1             |
| 1754   | Layout 1             |
| 1749   | Layout 1             |
| 1743   | Layout 1             |
| 1737   | Layout 1             |
| 1731   | Layout 1             |
| 1725   | Layout 1             |
| 1717   | Layout 1             |
| 1710   | Layout 1             |
| 1704   | Layout 1             |
| 1698   | Layout 1             |
| 1690   | Layout 1             |
| 1685   | Layout 1             |
| 1680   | Layout 1             |
| 1674   | Layout 1             |
| 1668   | Layout 1             |
| 1659   | Layout 1             |
| 1649   | Layout 1             |
| 1642   | Layout 1             |
| 1636   | Layout 1             |
| 1628   | Layout 1             |
| 1622   | Layout 1             |
| 1614   | Layout 1             |
| 1608   | Layout 1             |
| 1602   | Layout 1             |
| 1598   | Layout 1             |
| 1594   | Layout 1             |
| 1590   | Layout 1             |
| 1587   | Layout 1             |
| 1584   | Layout 1             |
| 1579   | Layout 1             |
| 1572   | Layout 1             |
| 1565   | Layout 1             |
| 1559   | Layout 1             |
| 1554   | Layout 1             |
| 1547   | Layout 1             |
| 1537   | Layout 1             |
| 1529   | Layout 1             |
| 1524   | Layout 1             |
| 1519   | Layout 1             |
| 1509   | Layout 1             |
| 1506   | Layout 1             |
| 1504   | Layout 1             |
| 1500   | Layout 1             |
| 1493   | Layout 1             |
| 1489   | Layout 1             |
| 1485   | No documented layout |
| 1481   | No documented layout |
| 1474   | No documented layout |
| 1466   | No documented layout |
| 1462   | No documented layout |
| 1459   | No documented layout |
| 1453   | No documented layout |
| 1450   | No documented layout |
| 1445   | No documented layout |
| 1439   | No documented layout |
| 1433   | No documented layout |
| 1430   | No documented layout |
| 1426   | No documented layout |
| 1421   | No documented layout |
| 1417   | No documented layout |
| 1416   | No documented layout |
| 1409   | No documented layout |
| 1405   | No documented layout |
| 1401   | No documented layout |
| 1396   | No documented layout |
| 1391   | No documented layout |
| 1390   | No documented layout |
| 1386   | No documented layout |
| 1381   | No documented layout |
| 1379   | No documented layout |
| 1372   | No documented layout |
| 1366   | No documented layout |
| 1364   | No documented layout |
| 1363   | No documented layout |
| 1360   | No documented layout |
| 1358   | No documented layout |
| 1355   | No documented layout |
| 1351   | No documented layout |
| 1348   | No documented layout |
| 1346   | No documented layout |
| 1341   | No documented layout |
| 1340   | No documented layout |
| 1338   | No documented layout |
| 1335   | No documented layout |
| 1333   | No documented layout |
| 1329   | No documented layout |
| 1327   | No documented layout |
| 1324   | No documented layout |
| 1321   | No documented layout |
| 1319   | No documented layout |
| 1318   | No documented layout |
| 1316   | No documented layout |
| 1313   | No documented layout |
| 1311   | No documented layout |
| 1309   | No documented layout |
| 1304   | No documented layout |
| 1292   | No documented layout |
| 1286   | No documented layout |
| 1280   | No documented layout |
| 1276   | No documented layout |
| 1267   | No documented layout |
| 1261   | No documented layout |
| 1256   | No documented layout |
| 1250   | No documented layout |
| 1246   | No documented layout |
| 1239   | No documented layout |
| 1230   | No documented layout |
| 1226   | No documented layout |
| 1220   | No documented layout |
| 1217   | No documented layout |
| 1211   | No documented layout |
| 1210   | No documented layout |
| 1208   | No documented layout |
| 1203   | No documented layout |
| 1197   | No documented layout |
| 1194   | No documented layout |
| 1192   | No documented layout |
| 1187   | No documented layout |
| 1183   | No documented layout |
| 1177   | No documented layout |
| 1173   | No documented layout |
| 1167   | No documented layout |
| 1164   | No documented layout |
| 1156   | No documented layout |
| 1149   | No documented layout |
| 1144   | No documented layout |
| 1137   | No documented layout |
| 1132   | No documented layout |
| 1127   | No documented layout |
| 1122   | No documented layout |
| 1118   | No documented layout |
| 1114   | No documented layout |
| 1109   | No documented layout |
| 1102   | No file              |
| 1096   | No file              |
| 1088   | No file              |
| 1081   | No file              |
| 1076   | No file              |
| 1069   | No file              |
| 1064   | No file              |
| 1058   | No file              |
| 1051   | No file              |
| 1044   | No file              |
| 1036   | No file              |
| 1026   | No file              |
| 1016   | No file              |
| 1009   | No file              |
| 1005   | No file              |
| 1000   | No file              |
| 998    | No file              |
| 990    | No file              |
| 979    | No file              |
| 972    | No file              |
| 963    | No file              |
| 955    | No file              |
| 946    | No file              |
| 938    | No file              |
| 927    | No file              |
| 911    | No file              |
| 904    | No file              |
| 899    | No file              |
| 894    | No file              |
| 885    | No file              |
| 879    | No file              |
| 872    | No file              |
| 864    | No file              |
| 855    | No file              |
| 853    | No file              |
| 845    | No file              |
| 837    | No file              |
| 829    | No documented layout |
| 822    | No documented layout |
| 814    | No documented layout |
| 805    | No documented layout |
| 794    | No documented layout |
| 787    | No documented layout |
| 780    | No documented layout |
| 771    | No documented layout |
| 760    | No documented layout |
| 748    | No documented layout |
| 741    | No documented layout |
| 736    | No documented layout |
| 731    | No documented layout |
| 723    | No documented layout |
| 711    | No documented layout |
| 707    | No documented layout |
| 697    | No documented layout |
| 689    | No documented layout |
| 683    | No documented layout |
| 678    | No documented layout |
| 670    | No documented layout |
| 661    | No documented layout |
| 656    | No documented layout |
| 652    | No documented layout |
| 643    | No documented layout |
| 637    | No documented layout |
| 630    | No documented layout |
| 627    | No documented layout |
| 621    | No documented layout |
| 617    | No documented layout |
| 615    | No documented layout |
| 606    | No documented layout |
| 599    | No documented layout |
| 592    | No documented layout |
| 586    | No documented layout |
| 577    | No documented layout |
| 569    | No documented layout |
| 561    | No documented layout |
| 554    | No documented layout |
| 542    | No documented layout |
| 532    | No documented layout |
| 531    | No documented layout |
| 526    | No documented layout |
| 521    | No documented layout |
| 517    | No documented layout |
| 510    | No documented layout |
| 508    | No documented layout |
| 504    | No documented layout |
| 497    | No documented layout |
| 491    | No documented layout |
| 485    | No documented layout |
| 478    | No documented layout |
| 472    | No documented layout |
| 466    | No documented layout |
| 457    | No documented layout |
| 452    | No documented layout |
| 449    | No documented layout |
| 435    | No documented layout |

<!-- versions:end -->

## Companion Files

| File                | Required | Role                                                                 |
| ------------------- | -------- | -------------------------------------------------------------------- |
| `regionmapinfo.bss` | Optional | The image name of each map key (see [Map Index Fields](#map-index-fields)); without it the Maps column is empty |

The handler also reads two lookup indexes to name the `A1_` fields (see
Notes).

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type              | Field              | Notes                                                       |
| ------------------- | ----------------- | ------------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                              |
| `+0x04`             | u32               | record_count       | Number of rows; `122` on client 3474                        |
| `+0x08`             | Row[record_count] | records            | See Row; not sorted by `field_no`                           |
| `records+0x00`      | String Table      | string_table       | See String Table                                            |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 157 x count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                                  |

The parser rejects a file whose rows do not end at `string_table_start`.

### Row (157 bytes)

| Offset  | Type | Field                            | Notes |
| ------- | ---- | -------------------------------- | ----- |
| `+0x00` | u16  | field_no                         | Unique; the `field_no` of `instancefield.dbss` and `instancedungeoninfo.dbss` |
| `+0x02` | u32  | field_name_ref                   | String-table index of `field_name`, the name the world editor shows: Korean (`월드` "World", `칼페온 크자카 인던` "Calpheon Kzarka instance dungeon") or the instance field's internal name (`A1_001`) |
| `+0x06` | u32  | resource_name_ref                | String-table index of `resource_name`, the map resource folder: `_real`, `_empty` (field `0`) or `_instancedungeon/<field_no>` on the `A1_` fields |
| `+0x0A` | u32  | display_name_ref                 | String-table index of `display_name`; the empty string on every row of clients 1784 and 3474 |
| `+0x0E` | f32  | spawn_x                          | Spawn point, world X; `0` on the 51 rows of client 3474 whose sheet has no point |
| `+0x12` | f32  | spawn_y                          | Spawn point, world Y (height) |
| `+0x16` | f32  | spawn_z                          | Spawn point, world Z |
| `+0x1A` | i32  | sector_start_x                   | Field box, lower corner, in 12,800-unit sectors |
| `+0x1E` | i32  | sector_start_y                   | |
| `+0x22` | i32  | sector_start_z                   | |
| `+0x26` | i32  | sector_end_x                     | Field box, upper corner, inclusive; never below the matching start |
| `+0x2A` | i32  | sector_end_y                     | |
| `+0x2E` | i32  | sector_end_z                     | |
| `+0x32` | f32  | world_start_x                    | `sector_start_x x 12800` on every row |
| `+0x36` | f32  | world_start_y                    | `sector_start_y x 12800` |
| `+0x3A` | f32  | world_start_z                    | `sector_start_z x 12800` |
| `+0x3E` | f32  | world_end_x                      | `(sector_end_x + 1) x 12800` on every row: the far edge of the last sector |
| `+0x42` | f32  | world_end_y                      | `(sector_end_y + 1) x 12800` |
| `+0x46` | f32  | world_end_z                      | `(sector_end_z + 1) x 12800` |
| `+0x4A` | i32  | obstacle_precision               | `4` on every row; the sheet comment gives `1` = 128 m down to `128` = 1 m |
| `+0x4E` | i32  | server_sector_start_x            | `sector_start_x x 3` on every row |
| `+0x52` | i32  | server_sector_start_y            | `sector_start_y x 3` |
| `+0x56` | i32  | server_sector_start_z            | `sector_start_z x 3` |
| `+0x5A` | i32  | server_sector_end_x              | `sector_end_x x 3` on every row |
| `+0x5E` | i32  | server_sector_end_y              | `sector_end_y x 3` |
| `+0x62` | i32  | server_sector_end_z              | `sector_end_z x 3` |
| `+0x66` | u8   | field_type                       | See [Field Types](#field-types) |
| `+0x67` | u16  | region_map_index                 | `regionmapinfo.bss` key; see [Map Index Fields](#map-index-fields) |
| `+0x69` | u16  | fishing_map_index                | |
| `+0x6B` | u16  | water_info_map_index             | |
| `+0x6D` | u16  | siege_info_map_index             | |
| `+0x6F` | u16  | village_siege_info_map_index     | |
| `+0x71` | u16  | village_siege_info_map_index_new | |
| `+0x73` | u16  | unknown_73                       | `12` on every row, the `regionmapinfo.bss` key of `VillageSiegemap_2024.bmp`; not in the client 1784 row |
| `+0x75` | u16  | underground_map_index            | |
| `+0x77` | u16  | audio_map_index                  | |
| `+0x79` | u8   | is_save_complete                 | `0` on every row; the sheet comment: count dungeon clears, `0` false, `1` true |
| `+0x7A` | u32  | field_level                      | `0` on every row; the sheet comment: the level players are scaled to, `0` for none |
| `+0x7E` | u8   | is_ridable                       | `1` when a mount may be summoned in the field; fields 1, 700, 701, 1238 and 1239 on client 3474 |
| `+0x7F` | u16  | enter_enable_user_count          | Players who may enter: `2` on the `A1_` fields, `1` elsewhere (client 3474) |
| `+0x81` | u8   | use_range_spawn                  | `1` when the field spawns the world's spawns inside its sector box (the sheet comment names the tutorial); the `A1_` fields on client 3474 |
| `+0x82` | u8   | use_return_position              | `0` on every row; the sheet comment: `1` sends a player back to where they entered from |
| `+0x83` | i32  | item_drop_rate                   | Added item drop rate on the 1,000,000 = 100% scale: `-1000000` (no drops) on the `A1_` fields, `0` elsewhere (client 3474) |
| `+0x87` | u32  | bank_no_music                    | Music bank; `1` on the five rows that have `is_ridable` on client 3474 |
| `+0x8B` | u32  | bank_no_environment              | Ambient sound bank; `0` on every row |
| `+0x8F` | u16  | great_sea_map_index              | |
| `+0x91` | u16  | horse_race_course_map_index      | |
| `+0x93` | u16  | unknown_93                       | `11` on every row, the key of `ElfWar_SiegeMap.bmp` |
| `+0x95` | u16  | unknown_95                       | `14` on every row, the key of `HardCoreChannelMap.bmp` |
| `+0x97` | u16  | unknown_97                       | `15` on every row, the key of `SnowBoardCourseMap.bmp` |
| `+0x99` | u16  | unknown_99                       | `17` on every row, the key of `OceanSiegemap.bmp` |
| `+0x9B` | u16  | unknown_9b                       | `16` on every row, the key of `EdaniaRegionMap.bmp` |

The `*_ref` fields index the string table from `0`; the parser stores each
string under the field name without `_ref`. The value notes are from
client 3474 unless they name another client.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | `144` on client 3474                           |
| `+0x04` | pstr[string_count] | strings      | Counted entries, indexed from `0`; entry `2` is the empty string |

## Layout 1

The client 1784 row is 12 bytes shorter: it lacks `unknown_73` and the five
u16 fields after `horse_race_course_map_index`, so every field from
`underground_map_index` on sits 2 bytes earlier.

### Row (145 bytes)

| Offset  | Type | Field                            | Notes |
| ------- | ---- | -------------------------------- | ----- |
| `+0x00` | u16  | field_no                         | |
| `+0x02` | u32  | field_name_ref                   | |
| `+0x06` | u32  | resource_name_ref                | |
| `+0x0A` | u32  | display_name_ref                 | |
| `+0x0E` | f32  | spawn_x                          | |
| `+0x12` | f32  | spawn_y                          | |
| `+0x16` | f32  | spawn_z                          | |
| `+0x1A` | i32  | sector_start_x                   | |
| `+0x1E` | i32  | sector_start_y                   | |
| `+0x22` | i32  | sector_start_z                   | |
| `+0x26` | i32  | sector_end_x                     | |
| `+0x2A` | i32  | sector_end_y                     | |
| `+0x2E` | i32  | sector_end_z                     | |
| `+0x32` | f32  | world_start_x                    | |
| `+0x36` | f32  | world_start_y                    | |
| `+0x3A` | f32  | world_start_z                    | |
| `+0x3E` | f32  | world_end_x                      | |
| `+0x42` | f32  | world_end_y                      | |
| `+0x46` | f32  | world_end_z                      | |
| `+0x4A` | i32  | obstacle_precision               | |
| `+0x4E` | i32  | server_sector_start_x            | |
| `+0x52` | i32  | server_sector_start_y            | |
| `+0x56` | i32  | server_sector_start_z            | |
| `+0x5A` | i32  | server_sector_end_x              | |
| `+0x5E` | i32  | server_sector_end_y              | |
| `+0x62` | i32  | server_sector_end_z              | |
| `+0x66` | u8   | field_type                       | `0` to `5` on client 1784, see [Field Types](#field-types) |
| `+0x67` | u16  | region_map_index                 | |
| `+0x69` | u16  | fishing_map_index                | |
| `+0x6B` | u16  | water_info_map_index             | |
| `+0x6D` | u16  | siege_info_map_index             | |
| `+0x6F` | u16  | village_siege_info_map_index     | |
| `+0x71` | u16  | village_siege_info_map_index_new | |
| `+0x73` | u16  | underground_map_index            | |
| `+0x75` | u16  | audio_map_index                  | |
| `+0x77` | u8   | is_save_complete                 | |
| `+0x78` | u32  | field_level                      | `30` on 149 rows of client 1784 (102 of `field_type` `1`, 47 of `3`), `0` on the rest |
| `+0x7C` | u8   | is_ridable                       | |
| `+0x7D` | u16  | enter_enable_user_count          | |
| `+0x7F` | u8   | use_range_spawn                  | |
| `+0x80` | u8   | use_return_position              | |
| `+0x81` | i32  | item_drop_rate                   | |
| `+0x85` | u32  | bank_no_music                    | |
| `+0x89` | u32  | bank_no_environment              | |
| `+0x8D` | u16  | great_sea_map_index              | |
| `+0x8F` | u16  | horse_race_course_map_index      | |

## Field Types

`field_type` is the 2016 client's `gc::FieldInfo::FieldType` (a u8 enum).
The `Field_Table` sheet comment on client 1784 lists `0` to `3` with the
same meaning.

| Value | 2016 name              | Sheet comment (client 1784) | Rows on client 1784 | Rows on client 3474 |
| ----- | ---------------------- | --------------------------- | ------------------- | ------------------- |
| `0`   | `OpenField`            | 오픈필드 (open field)       | 2                   | 2 (`0` Empty, `1` 월드) |
| `1`   | `InstanceField`        | 인스턴스필드 (instance field) | 181               | 54                  |
| `2`   | `Nightmare`            | 나이트메어 (nightmare)      | 24                  | 0                   |
| `3`   | `InstanceDungeon`      | 인스턴스던전 (instance dungeon) | 63              | 0                   |
| `4`   | `ChannelInstanceField` | none                        | 1 (`20000`)         | 0                   |
| `5`   | none                   | none                        | 35 (`A1_001` to `A1_035`) | 66 (`A1_001` to `A1_066`) |

## Map Index Fields

The `*_map_index` fields and `unknown_73`, `unknown_93` to `unknown_9b`
hold the same value on every row of a client: the `map_index` of one map
in [regionmapinfo.bss](regionmapinfo_bss.md), which names its image.

The handler stores the image of each named map key field under the field
name with `_image` for `_index` (`region_map_index` 1 gives
`region_map_image` `RegionMap_New.bmp`), `''` for a key without a
`regionmapinfo.bss` row, and lists the images once each in the Maps column.
The `unknown_*` map keys get no image field.

| Field                              | Value | `regionmapinfo.bss` image (client 3474) |
| ---------------------------------- | ----- | --------------------------------------- |
| `region_map_index`                 | `1`   | `RegionMap_New.bmp`                     |
| `fishing_map_index`                | `2`   | none                                    |
| `water_info_map_index`             | `3`   | none                                    |
| `siege_info_map_index`             | `4`   | `Siegemap.bmp`                          |
| `village_siege_info_map_index`     | `5`   | `VillageSiegemap.bmp`                   |
| `village_siege_info_map_index_new` | `10`  | `VillageSiegemap_New.bmp`               |
| `unknown_73`                       | `12`  | `VillageSiegemap_2024.bmp`              |
| `underground_map_index`            | `6`   | none                                    |
| `audio_map_index`                  | `7`   | `AudioMap.bmp`                          |
| `great_sea_map_index`              | `8`   | `GreatSeaMap.bmp`                       |
| `horse_race_course_map_index`      | `9`   | `HorseRaceCourseMap.bmp`                |
| `unknown_93`                       | `11`  | `ElfWar_SiegeMap.bmp`                   |
| `unknown_95`                       | `14`  | `HardCoreChannelMap.bmp`                |
| `unknown_97`                       | `15`  | `SnowBoardCourseMap.bmp`                |
| `unknown_99`                       | `17`  | `OceanSiegemap.bmp`                     |
| `unknown_9b`                       | `16`  | `EdaniaRegionMap.bmp`                   |

On client 1784 the `RegionMap_Table` sheet of the same source lists keys
`1` to `10`: `2` is `FishingMap.bmp`, `3` `WaterMap.bmp` and `6`
`Undergroundmap.bmp`, three keys that no `regionmapinfo.bss` from client
1230 to 3482 holds.

## Field Names

The row is the `Field_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (306 rows, developer workbook
`datasheet_regiondatatable.xlsm`). The `fieldinfo.bss` of the client 1784
test client is byte for byte the private server's build of that sheet: 306
rows of Layout 1. Over its 306 field numbers every column below matches on
every row, except `ResourceName` on field `0` (`_empty` in the file,
`_real` in the sheet):

| Field                                  | Sheet column                                   |
| -------------------------------------- | ---------------------------------------------- |
| `field_no`                             | `FieldNo`                                      |
| `field_name`                           | `FieldName`                                    |
| `resource_name`                        | `ResourceName`                                 |
| `spawn_x`, `spawn_y`, `spawn_z`        | `StartPositionX`, `StartPositionY`, `StartPositionZ` |
| `sector_start_*`, `sector_end_*`       | `MapSectorStartX` to `MapSectorEndZ`           |
| `field_type`                           | `FieldType`                                    |
| `obstacle_precision`                   | `ObstaclePrecision`                            |
| `region_map_index` to `audio_map_index`, `great_sea_map_index`, `horse_race_course_map_index` | `RegionMapIndex`, `FishingMapIndex`, `WaterInfoMapIndex`, `SiegeInfoMapIndex`, `VillageSiegeInfoMapIndex`, `VillageSiegeInfoMapIndexNew`, `UndergroundMapIndex`, `AudioMapIndex`, `GreatSeaMapIndex`, `HorseRaceCourseMapIndex` |
| `is_save_complete`                     | `isSaveComplete`                               |
| `field_level`                          | `FieldLevel`                                   |
| `is_ridable`                           | `IsRidable`                                    |
| `enter_enable_user_count`              | `EnterEnableUserCount`                         |
| `use_range_spawn`                      | `UseRangeSpawn`                                |
| `use_return_position`                  | `UseReturnPosition`                            |
| `item_drop_rate`                       | `ItemDropRate`                                 |
| `bank_no_music`                        | `BankNo_Music`                                 |
| `bank_no_environment`                  | `BankNo_Environment`                           |

Several columns hold one value on all 306 rows (`ObstaclePrecision`,
`isSaveComplete`, `BankNo_Environment` and every map index), so their match
alone places nothing. The 2016 client's `gc::FieldInfo` places them: its
members run `_fieldNo`, `_fieldName`, `_resourceName`, `_displayName`,
`_spawnPosition`, `_startSector`, `_endSector`, `_startPosition`,
`_endPosition`, `_obstaclePrecision`, `_startSector_Server`,
`_endSector_Server`, `_fieldType`, `_regionMapID`, `_fishingMapID`,
`_waterInfoMapID`, `_siegeInfoMapID`, `_viliageSiegeInfoMapID`,
`_undergroundInfoMapID`, `_isSaveComplete`, `_fieldCorrectLevel`,
`_isRidable`, `_enterEnableUserCount`, `_useRangeSpawn`,
`_useReturnPosition`, `_addItemDropRate`, `_bankNo_Music`,
`_bankNo_Environment`, the row order with the later map indexes added.
`display_name`, `world_*` and `server_sector_*` have no sheet column and
take their names from those members. The sheet's `MiniMapIndex` (`1` on
every row) and `StartPositionDir` (7 values) are in neither the struct nor
the file.

On client 3474 the file shares 91 field numbers with the sheet. `field_no`,
`field_name`, the sector box, `field_type`, `is_ridable`,
`enter_enable_user_count`, `use_range_spawn`, `item_drop_rate` and
`bank_no_music` match on all 91, except `sector_end_y` of field `1`
(`6`, the sheet `5`). `resource_name` matches on all 91 without case: 34
`A1_` fields write `_instancedungeon/40NN` where the sheet has
`_InstanceDungeon/40NN`. The spawn point matches on 82; fields 4001, 4006,
4010, 4011, 4026, 4027, 4033, 4034 and 4035 have new points.

The sheet comments on client 1784 give the meaning of `FieldName` (the name
shown in the world editor), `ResourceName` (`real` for open fields and
dungeons that need no loading), `FieldType`, `ObstaclePrecision`,
`isSaveComplete`, `FieldLevel`, `IsRidable`, `EnterEnableUserCount`,
`UseRangeSpawn`, `UseReturnPosition` and `ItemDropRate` ("-100% to 200%",
`-1000000` to `2000000`), as the Row notes quote them.

## Notes

- The handler names an `A1_` field with the title of its
  [instancefieldmapinfo.bss](instancefieldmapinfo_bss.md) map, read in the
  loaded LOC language: `A1_001` reads `The Magnus: The Great Single Path
  (A1_001)`. It takes the title only when the `instancefield.dbss` record
  with the same key has the same name, which holds for the 66 `A1_` fields
  (key `40NN`, name `A1_0NN`, `field_no` `40NN`); field `1`, `월드`, is not
  instance field `1` (`Shadow_Ser_Main`). Every other field shows its
  `field_name`.
- The `FIELD_NAME` lookup index maps each `field_no` to its name, so the
  `instancefield.dbss` and `instancedungeoninfo.dbss` tables show a Field
  column without opening this file. On client 3474 every `field_no` of both
  tables has a row here: `1` and `4001` to `4066` in `instancefield.dbss`,
  `700`, `701`, `1238` and `1239` in `instancedungeoninfo.dbss`.
- Fields `700`, `701`, `1238` and `1239` copy field `1`: the same sector
  box, spawn point, `is_ridable` and `bank_no_music`, with `field_type` `1`.
- Field numbers `9001` to `9050` (client 3474) are named `테스트 인던`
  ("test instance dungeon", 10 rows), `자렛과 클리프` (20) and `조르다인
  이소벨` (20), all `field_type` `1` without a spawn point.
- The 66 `A1_` fields share the box `-3..3` on every axis, as their
  `instancefield.dbss` records do.

## Open Questions

### What Field Type 5 Is

The 2016 enum ends at `4` (`ChannelInstanceField`) and the client 1784
sheet comment at `3`. Type `5` is on every `A1_` field (35 on client 1784,
66 on client 3474) and on no other row, so it names the kind of field The
Magnus runs in. No string in the client 3474 `.luac` files names a field
type.

### Which Maps the Newer Map Index Fields Select

`unknown_73` and `unknown_93` to `unknown_9b` hold the `regionmapinfo.bss`
keys of the 2024 node war map, the Elf War siege map, the hardcore channel
map, the snowboard course map, the ocean siege map and the Edania region
map (see [Map Index Fields](#map-index-fields)). They have no sheet column
on client 1784, so their names and the order of the five trailing fields
are not confirmed.

### Why the Server Box Is Three Times the Sector Box

`server_sector_*` is the sector box times three on every row of clients
1784 and 3474, both corners included, so the server box ends two server
sectors before the field box's far edge. What the server divides a sector
into, and whether the end corner is exclusive there, is open.
