# `worldmap*typedata.bss` and `worldmap*forconquest.bss` Format

## Purpose

Seven world map grids, one byte per 1,600 x 1,600 world-unit cell over
the whole map: each file is a 2,176 x 1,984 image whose cell value names
the territory, region group or siege area under that cell. The 2016
client already held a field type and a territory byte grid for its world
map textures (see [Field Names](#field-names)). All seven files have the same
layout and size (4,317,200 bytes); they differ only in what a cell value
joins to:

| File                                       | Grid                              | Cell value                                                          |
| ------------------------------------------ | --------------------------------- | ------------------------------------------------------------------- |
| `worldmapterritorytypedata.bss`            | Territories                       | `territoryinfo.bss` territory key                                   |
| `worldmapfieldtypedata.bss`                | Region groups                     | Low byte of a `regiongroupinfo.bss` region group key                |
| `worldmapmajorsiegeregiontypedata.bss`     | Conquest War areas                | Territory key; `255` outside the areas                              |
| `worldmapmajorsiegeterritorytypedata.bss`  | Conquest War areas                | Same bytes as `worldmapmajorsiegeregiontypedata.bss`                |
| `worldmapterritorytypedataforconquest.bss` | Node War territories              | Territory key + 1; `255` outside the territories                    |
| `worldmapsiegeregionforconquest.bss`       | Node War areas                    | Area number of a [`villagesiegeinfo.bss`](villagesiegeinfo_bss.md) row; `0` outside |
| `worldmapoceansiegeregionforconquest.bss`  | Blue Battlefield areas            | Area number of an [`oceansiegeinfo.bss`](oceansiegeinfo_bss.md) row; `255` outside |

[Cell Values](#cell-values) gives the evidence for each join.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                       | Bytes     | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------------------ | --------- | -------------- | --------- |
| 1      | 805 and later  | 3483    | `worldmapfieldtypedata.bss`                | 4,317,200 | 1 String Table | 4         |
| 1      | 1749 and later | 3483    | `worldmapmajorsiegeregiontypedata.bss`     | 4,317,200 | 1 String Table | 4         |
| 1      | 1749 and later | 3483    | `worldmapmajorsiegeterritorytypedata.bss`  | 4,317,200 | 1 String Table | 4         |
| 1      | 3111 and later | 3483    | `worldmapoceansiegeregionforconquest.bss`  | 4,317,200 | 1 String Table | 4         |
| 1      | 1524 and later | 3483    | `worldmapsiegeregionforconquest.bss`       | 4,317,200 | 1 String Table | 4         |
| 1      | 805 and later  | 3483    | `worldmapterritorytypedata.bss`            | 4,317,200 | 1 String Table | 4         |
| 1      | 1524 and later | 3483    | `worldmapterritorytypedataforconquest.bss` | 4,317,200 | 1 String Table | 4         |

| Layout | File                                       | Known                | Unknown    |
| ------ | ------------------------------------------ | -------------------- | ---------- |
| 1      | `worldmapfieldtypedata.bss`                | 4,317,200 B (100.0%) | 0 B (0.0%) |
| 1      | `worldmapmajorsiegeregiontypedata.bss`     | 4,317,200 B (100.0%) | 0 B (0.0%) |
| 1      | `worldmapmajorsiegeterritorytypedata.bss`  | 4,317,200 B (100.0%) | 0 B (0.0%) |
| 1      | `worldmapoceansiegeregionforconquest.bss`  | 4,317,200 B (100.0%) | 0 B (0.0%) |
| 1      | `worldmapsiegeregionforconquest.bss`       | 4,317,200 B (100.0%) | 0 B (0.0%) |
| 1      | `worldmapterritorytypedata.bss`            | 4,317,200 B (100.0%) | 0 B (0.0%) |
| 1      | `worldmapterritorytypedataforconquest.bss` | 4,317,200 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 1             |
| 3482   | Layout 1             |
| 3474   | Layout 1             |
| 3473   | Layout 1             |
| 3464   | Layout 1             |
| 3458   | Layout 1             |
| 3454   | Layout 1             |
| 3444   | Layout 1             |
| 3435   | Layout 1             |
| 3426   | Layout 1             |
| 3418   | Layout 1             |
| 3412   | Layout 1             |
| 3402   | Layout 1             |
| 3396   | Layout 1             |
| 3387   | Layout 1             |
| 3381   | Layout 1             |
| 3373   | Layout 1             |
| 3364   | Layout 1             |
| 3356   | Layout 1             |
| 3349   | Layout 1             |
| 3342   | Layout 1             |
| 3335   | Layout 1             |
| 3326   | Layout 1             |
| 3321   | Layout 1             |
| 3314   | Layout 1             |
| 3303   | Layout 1             |
| 3302   | Layout 1             |
| 3293   | Layout 1             |
| 3283   | Layout 1             |
| 3275   | Layout 1             |
| 3267   | Layout 1             |
| 3258   | Layout 1             |
| 3251   | Layout 1             |
| 3242   | Layout 1             |
| 3235   | Layout 1             |
| 3229   | Layout 1             |
| 3212   | Layout 1             |
| 3203   | Layout 1             |
| 3193   | Layout 1             |
| 3186   | Layout 1             |
| 3177   | Layout 1             |
| 3169   | Layout 1             |
| 3158   | Layout 1             |
| 3151   | Layout 1             |
| 3144   | Layout 1             |
| 3133   | Layout 1             |
| 3125   | Layout 1             |
| 3118   | Layout 1             |
| 3111   | Layout 1             |
| 3103   | Layout 1             |
| 3095   | Layout 1             |
| 3086   | Layout 1             |
| 3072   | Layout 1             |
| 3062   | Layout 1             |
| 3052   | Layout 1             |
| 3045   | Layout 1             |
| 3037   | Layout 1             |
| 3030   | Layout 1             |
| 3021   | Layout 1             |
| 3012   | Layout 1             |
| 3002   | Layout 1             |
| 2995   | Layout 1             |
| 2987   | Layout 1             |
| 2978   | Layout 1             |
| 2970   | Layout 1             |
| 2959   | Layout 1             |
| 2951   | Layout 1             |
| 2942   | Layout 1             |
| 2935   | Layout 1             |
| 2932   | Layout 1             |
| 2923   | Layout 1             |
| 2919   | Layout 1             |
| 2907   | Layout 1             |
| 2900   | Layout 1             |
| 2891   | Layout 1             |
| 2882   | Layout 1             |
| 2872   | Layout 1             |
| 2863   | Layout 1             |
| 2855   | Layout 1             |
| 2849   | Layout 1             |
| 2844   | Layout 1             |
| 2834   | Layout 1             |
| 2825   | Layout 1             |
| 2819   | Layout 1             |
| 2811   | Layout 1             |
| 2803   | Layout 1             |
| 2794   | Layout 1             |
| 2783   | Layout 1             |
| 2774   | Layout 1             |
| 2765   | Layout 1             |
| 2756   | Layout 1             |
| 2750   | Layout 1             |
| 2743   | Layout 1             |
| 2736   | Layout 1             |
| 2726   | Layout 1             |
| 2717   | Layout 1             |
| 2709   | Layout 1             |
| 2703   | Layout 1             |
| 2695   | Layout 1             |
| 2684   | Layout 1             |
| 2672   | Layout 1             |
| 2665   | Layout 1             |
| 2657   | Layout 1             |
| 2649   | Layout 1             |
| 2644   | Layout 1             |
| 2637   | Layout 1             |
| 2629   | Layout 1             |
| 2619   | Layout 1             |
| 2612   | Layout 1             |
| 2606   | Layout 1             |
| 2602   | Layout 1             |
| 2601   | Layout 1             |
| 2592   | Layout 1             |
| 2583   | Layout 1             |
| 2575   | Layout 1             |
| 2567   | Layout 1             |
| 2560   | Layout 1             |
| 2553   | Layout 1             |
| 2545   | Layout 1             |
| 2538   | Layout 1             |
| 2529   | Layout 1             |
| 2519   | Layout 1             |
| 2513   | Layout 1             |
| 2510   | Layout 1             |
| 2507   | Layout 1             |
| 2503   | Layout 1             |
| 2498   | Layout 1             |
| 2492   | Layout 1             |
| 2487   | Layout 1             |
| 2480   | Layout 1             |
| 2474   | Layout 1             |
| 2468   | Layout 1             |
| 2460   | Layout 1             |
| 2453   | Layout 1             |
| 2444   | Layout 1             |
| 2438   | Layout 1             |
| 2434   | Layout 1             |
| 2429   | Layout 1             |
| 2421   | Layout 1             |
| 2414   | Layout 1             |
| 2407   | Layout 1             |
| 2401   | Layout 1             |
| 2397   | Layout 1             |
| 2393   | Layout 1             |
| 2384   | Layout 1             |
| 2378   | Layout 1             |
| 2372   | Layout 1             |
| 2358   | Layout 1             |
| 2352   | Layout 1             |
| 2347   | Layout 1             |
| 2343   | Layout 1             |
| 2335   | Layout 1             |
| 2327   | Layout 1             |
| 2324   | Layout 1             |
| 2319   | Layout 1             |
| 2313   | Layout 1             |
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
| 1485   | Layout 1             |
| 1481   | Layout 1             |
| 1474   | Layout 1             |
| 1466   | Layout 1             |
| 1462   | Layout 1             |
| 1459   | Layout 1             |
| 1453   | Layout 1             |
| 1450   | Layout 1             |
| 1445   | Layout 1             |
| 1439   | Layout 1             |
| 1433   | Layout 1             |
| 1430   | Layout 1             |
| 1426   | Layout 1             |
| 1421   | Layout 1             |
| 1417   | Layout 1             |
| 1416   | Layout 1             |
| 1409   | Layout 1             |
| 1405   | Layout 1             |
| 1401   | Layout 1             |
| 1396   | Layout 1             |
| 1391   | Layout 1             |
| 1390   | Layout 1             |
| 1386   | Layout 1             |
| 1381   | Layout 1             |
| 1379   | Layout 1             |
| 1372   | Layout 1             |
| 1366   | Layout 1             |
| 1364   | Layout 1             |
| 1363   | Layout 1             |
| 1360   | Layout 1             |
| 1358   | Layout 1             |
| 1355   | Layout 1             |
| 1351   | Layout 1             |
| 1348   | Layout 1             |
| 1346   | Layout 1             |
| 1341   | Layout 1             |
| 1340   | Layout 1             |
| 1338   | Layout 1             |
| 1335   | Layout 1             |
| 1333   | Layout 1             |
| 1329   | Layout 1             |
| 1327   | Layout 1             |
| 1324   | Layout 1             |
| 1321   | Layout 1             |
| 1319   | Layout 1             |
| 1318   | Layout 1             |
| 1316   | Layout 1             |
| 1313   | Layout 1             |
| 1311   | Layout 1             |
| 1309   | Layout 1             |
| 1304   | Layout 1             |
| 1292   | Layout 1             |
| 1286   | Layout 1             |
| 1280   | Layout 1             |
| 1276   | Layout 1             |
| 1267   | Layout 1             |
| 1261   | Layout 1             |
| 1256   | Layout 1             |
| 1250   | Layout 1             |
| 1246   | Layout 1             |
| 1239   | Layout 1             |
| 1230   | Layout 1             |
| 1226   | Layout 1             |
| 1220   | Layout 1             |
| 1217   | Layout 1             |
| 1211   | Layout 1             |
| 1210   | Layout 1             |
| 1208   | Layout 1             |
| 1203   | Layout 1             |
| 1197   | Layout 1             |
| 1194   | Layout 1             |
| 1192   | Layout 1             |
| 1187   | Layout 1             |
| 1183   | Layout 1             |
| 1177   | Layout 1             |
| 1173   | Layout 1             |
| 1167   | Layout 1             |
| 1164   | Layout 1             |
| 1156   | Layout 1             |
| 1149   | Layout 1             |
| 1144   | Layout 1             |
| 1137   | Layout 1             |
| 1132   | Layout 1             |
| 1127   | Layout 1             |
| 1122   | Layout 1             |
| 1118   | Layout 1             |
| 1114   | Layout 1             |
| 1109   | Layout 1             |
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
| 829    | Layout 1             |
| 822    | Layout 1             |
| 814    | Layout 1             |
| 805    | Layout 1             |
| 794    | No documented layout |
| 787    | No documented layout |
| 780    | No documented layout |
| 771    | No documented layout |
| 760    | No documented layout |
| 748    | No documented layout |
| 741    | No documented layout |
| 736    | No documented layout |
| 731    | No file              |
| 723    | No file              |
| 711    | No file              |
| 707    | No file              |
| 697    | No file              |
| 689    | No file              |
| 683    | No file              |
| 678    | No file              |
| 670    | No file              |
| 661    | No file              |
| 656    | No file              |
| 652    | No file              |
| 643    | No file              |
| 637    | No file              |
| 630    | No file              |
| 627    | No file              |
| 621    | No file              |
| 617    | No file              |
| 615    | No file              |
| 606    | No file              |
| 599    | No file              |
| 592    | No file              |
| 586    | No file              |
| 577    | No file              |
| 569    | No file              |
| 561    | No file              |
| 554    | No file              |
| 542    | No file              |
| 532    | No file              |
| 531    | No file              |
| 526    | No file              |
| 521    | No file              |
| 517    | No file              |
| 510    | No file              |
| 508    | No file              |
| 504    | No file              |
| 497    | No file              |
| 491    | No file              |
| 485    | No file              |
| 478    | No file              |
| 472    | No file              |
| 466    | No file              |
| 457    | No file              |
| 452    | No file              |
| 449    | No file              |
| 435    | No file              |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                                                     |
| ---------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `regiongroupinfo.bss`  | Optional | Region groups of `worldmapfieldtypedata.bss`, named by their worldmap node (LOC type 29) |
| `villagesiegeinfo.bss` | Optional | Region keys of each Node War area number, for `worldmapsiegeregionforconquest.bss`       |
| `oceansiegeinfo.bss`   | Optional | Island region keys of each Blue Battlefield area number, for `worldmapoceansiegeregionforconquest.bss` |
| `languagedata_en.loc`  | Optional | Territory names (type 12), region names (type 17), node names (type 29)                  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A PABR file with the shared empty string table and 8-byte trailer (see
[`npcsimply.bss` String Table](npcsimply_bss.md#string-table-variable-4-bytes--strings)).
The grid has no row count: the cells start right after the magic, so a
reader that takes `+0x04` as a PABR count reads the first four cells (`0`
in every file).

| Offset              | Type           | Field        | Notes                                                                       |
| ------------------- | -------------- | ------------ | --------------------------------------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                                                |
| `+0x04`             | u8[1984][2176] | cells        | 1,984 rows of 2,176 cells, row 0 at the south edge; see Grid                |
| `+0x41E004`         | String Table   | string_table | See String Table                                                            |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where the cells end: `0x41E004`                 |
| `string_table+0x04` | u32            | zero         | Always `0`                                                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | `0` in every file on clients 1784 and 3482 |
| `+0x04` | pstr[string_count] | strings      | Empty                                     |

## Grid

Cell `(column, row)` sits at byte `0x04 + row * 2176 + column` and
covers world x `-2,048,000 + 1,600 * column` to 1,600 units east of it,
and world z `-1,126,400 + 1,600 * row` to 1,600 units north of it. A
12,800-unit world sector is 8 x 8 cells, so the grid spans sectors x
`-160` to `111` and z `-88` to `159`.

I found the transform by fitting the territory grid to the waypoints of
`mapdata_realexplore2.bwp`: on client 3482, 556 of the 557 regions of
`regioninfo.bss` outside Balenos whose `waypoint_key` has a waypoint lie
on a cell with their own `territory_key` under this transform, with the
cell size tried at 1,600 and 3,200 units and the origin in 6,400-unit
steps. The next best origin, one sector west, reaches 552.

The outermost 8 cells on each side (one sector) are `0` in every file on
clients 1784 and 3482, also in the files that fill the rest of the map
with `255`: 66,304 cells.

## Cell Values

Evidence on client 3482: each region of `regioninfo.bss` with a waypoint
in `mapdata_realexplore2.bwp` was looked up at its waypoint's cell (628
regions).

| File                                       | Check                                                       | Result |
| ------------------------------------------ | ----------------------------------------------------------- | ------ |
| `worldmapterritorytypedata.bss`            | Cell value equals the region's `territory_key`              | 627 of 628; Duvencrune (territory 7) reads `5` |
| `worldmapfieldtypedata.bss`                | Cell value equals `region_group_key & 0xFF`                 | 604 of 628; 20 of the misses read `0`, 3 a neighbouring group, and Duvencrune (group `0`) reads `220` |
| `worldmapmajorsiegeregiontypedata.bss`     | Cell value equals `territory_key`, cells other than `255`   | 13 of 13 |
| `worldmapterritorytypedataforconquest.bss` | Cell value equals `territory_key + 1`, cells other than `255` | 147 of 148; Serendia Western Gateway (Calpheon) reads `2` (Serendia) |
| `worldmapsiegeregionforconquest.bss`       | Each `villagesiegeinfo.bss` row's region reads the row's `area_number` | 30 of 40; the 4 capitals (`25` to `28`) are not in the grid, the other 6 waypoints read `0` |
| `worldmapoceansiegeregionforconquest.bss`  | Each `oceansiegeinfo.bss` island reads its row's `area_number` | 15 of the 15 islands whose number the grid holds |

Values present on client 3482:

| File                                       | Values                                                                 |
| ------------------------------------------ | ---------------------------------------------------------------------- |
| `worldmapterritorytypedata.bss`            | `0` to `13`, all 14 territories; `0` is also every cell off the map    |
| `worldmapfieldtypedata.bss`                | 208 values; `0` off the map                                            |
| `worldmapmajorsiegeregiontypedata.bss`     | `0` (Balenos, and the frame), `1` Serendia, `3` Mediah, `4` Valencia, `255` |
| `worldmapterritorytypedataforconquest.bss` | `0` (the frame), `1` Balenos, `2` Serendia, `3` Calpheon, `5` Valencia, `12` Ulukita, `13` Outer Edania, `255`: the six territories of the `villagesiegeinfo.bss` node war nodes |
| `worldmapsiegeregionforconquest.bss`       | `0`, `1` to `24` and `29` to `40`: the 36 node war nodes of `villagesiegeinfo.bss` |
| `worldmapoceansiegeregionforconquest.bss`  | `0` (the frame), `2` to `16` (the Balenos islands), `255`              |

A region group key above 255 shares its byte with the key 256 lower: on
client 3482, 39 of the values `0` to `46` stand for two groups each, `2`
for the Altar of Agris group (`2`) and the Unjongga Street group (`258`)
in the Land of the Morning Light.

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its
`PAWorldMapManager` holds `_fieldTypeData` and `_territoryTypeData`, both
`unsigned char*`, with `createFieldTypeData`, `getFieldTypeDataSize` and
`updateFieldTypeDataToTexture` (and the same three for the territory
data), and its shaders read the textures `WorldMapFieldTypeTexture` and
`WorldMapTerritoryTypeTexture`, with `fSelectedFieldType` and
`fFieldDataResolution` in `WorldmapTerrainShaderConst`. I name the cell
array `cells`; the 2016 names cover two of the seven files only.

## Notes

- `worldmapmajorsiegeregiontypedata.bss` and
  `worldmapmajorsiegeterritorytypedata.bss` are byte for byte equal on
  clients 1784 and 3482.
- Client 1784 has six of the files; `worldmapoceansiegeregionforconquest.bss`
  is missing there. Between client 1784 and 3482 the territory grid
  differs in 352,681 cells and the region group grid in 366,269.

## Open Questions

### Why the Node War Territory Grid Adds One

`worldmapterritorytypedataforconquest.bss` stores the territory key plus
one, while `worldmapmajorsiegeregiontypedata.bss` stores the key itself
and so cannot tell Balenos (`0`) from its frame. The shift is read from
the data only (147 of 148 waypoints); no Lua or symbol names it.

### Region and Territory Major Siege Grids

`worldmapmajorsiegeregiontypedata.bss` and
`worldmapmajorsiegeterritorytypedata.bss` hold the same bytes on both
clients checked. In the client 3482 Lua (`grand_worldmap_mainpanel_new.luac`,
`GuildWar_SetTerritoryKey`) the world map's siege filter passes a
territory key to `ToClient_setVisibleMajorSiegeTerritoryKey` when
`ToClient_SetMajorSiegeViewMode` is on, else to
`ToClient_setVisibleVillageTerritoryKey`. Which grid each call draws,
and why both major siege files exist, is open.

### Region Groups Above 255

The field type grid keeps only the low byte of a region group key, so
groups `256` to `302` share values with groups `0` to `46`. Whether the
client tells them apart (by the territory grid, say) or highlights both
is open.
