# `blizzardregioninfo.bss` Format

## Purpose

Lists the snow regions that the client ties to blizzards: every row names one `regioninfo.bss` region of the Mountain of Eternal Winter (territory 9) or Ulukita (territory 11) and holds the minimum and maximum chance that the blizzard effect spawns there and a wind vector.

The file is small (21 rows in client 3458) and has no strings. The client Lua never mentions it or a blizzard; the field names come from the developers' `Blizzard_Region_Table` sheet (see [Field Names](#field-names)).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ----- | ------- | --------- |
| 1      | 1862 and later | 3483    | `blizzardregioninfo.bss` | 566   | 21 Row  | 26        |

| Layout | File                     | Known          | Unknown    |
| ------ | ------------------------ | -------------- | ---------- |
| 1      | `blizzardregioninfo.bss` | 566 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 1 |
| 3482   | Layout 1 |
| 3474   | Layout 1 |
| 3473   | Layout 1 |
| 3464   | Layout 1 |
| 3458   | Layout 1 |
| 3454   | Layout 1 |
| 3444   | Layout 1 |
| 3435   | Layout 1 |
| 3426   | Layout 1 |
| 3418   | Layout 1 |
| 3412   | Layout 1 |
| 3402   | Layout 1 |
| 3396   | Layout 1 |
| 3387   | Layout 1 |
| 3381   | Layout 1 |
| 3373   | Layout 1 |
| 3364   | Layout 1 |
| 3356   | Layout 1 |
| 3349   | Layout 1 |
| 3342   | Layout 1 |
| 3335   | Layout 1 |
| 3326   | Layout 1 |
| 3321   | Layout 1 |
| 3314   | Layout 1 |
| 3303   | Layout 1 |
| 3302   | Layout 1 |
| 3293   | Layout 1 |
| 3283   | Layout 1 |
| 3275   | Layout 1 |
| 3267   | Layout 1 |
| 3258   | Layout 1 |
| 3251   | Layout 1 |
| 3242   | Layout 1 |
| 3235   | Layout 1 |
| 3229   | Layout 1 |
| 3212   | Layout 1 |
| 3203   | Layout 1 |
| 3193   | Layout 1 |
| 3186   | Layout 1 |
| 3177   | Layout 1 |
| 3169   | Layout 1 |
| 3158   | Layout 1 |
| 3151   | Layout 1 |
| 3144   | Layout 1 |
| 3133   | Layout 1 |
| 3125   | Layout 1 |
| 3118   | Layout 1 |
| 3111   | Layout 1 |
| 3103   | Layout 1 |
| 3095   | Layout 1 |
| 3086   | Layout 1 |
| 3072   | Layout 1 |
| 3062   | Layout 1 |
| 3052   | Layout 1 |
| 3045   | Layout 1 |
| 3037   | Layout 1 |
| 3030   | Layout 1 |
| 3021   | Layout 1 |
| 3012   | Layout 1 |
| 3002   | Layout 1 |
| 2995   | Layout 1 |
| 2987   | Layout 1 |
| 2978   | Layout 1 |
| 2970   | Layout 1 |
| 2959   | Layout 1 |
| 2951   | Layout 1 |
| 2942   | Layout 1 |
| 2935   | Layout 1 |
| 2932   | Layout 1 |
| 2923   | Layout 1 |
| 2919   | Layout 1 |
| 2907   | Layout 1 |
| 2900   | Layout 1 |
| 2891   | Layout 1 |
| 2882   | Layout 1 |
| 2872   | Layout 1 |
| 2863   | Layout 1 |
| 2855   | Layout 1 |
| 2849   | Layout 1 |
| 2844   | Layout 1 |
| 2834   | Layout 1 |
| 2825   | Layout 1 |
| 2819   | Layout 1 |
| 2811   | Layout 1 |
| 2803   | Layout 1 |
| 2794   | Layout 1 |
| 2783   | Layout 1 |
| 2774   | Layout 1 |
| 2765   | Layout 1 |
| 2756   | Layout 1 |
| 2750   | Layout 1 |
| 2743   | Layout 1 |
| 2736   | Layout 1 |
| 2726   | Layout 1 |
| 2717   | Layout 1 |
| 2709   | Layout 1 |
| 2703   | Layout 1 |
| 2695   | Layout 1 |
| 2684   | Layout 1 |
| 2672   | Layout 1 |
| 2665   | Layout 1 |
| 2657   | Layout 1 |
| 2649   | Layout 1 |
| 2644   | Layout 1 |
| 2637   | Layout 1 |
| 2629   | Layout 1 |
| 2619   | Layout 1 |
| 2612   | Layout 1 |
| 2606   | Layout 1 |
| 2602   | Layout 1 |
| 2601   | Layout 1 |
| 2592   | Layout 1 |
| 2583   | Layout 1 |
| 2575   | Layout 1 |
| 2567   | Layout 1 |
| 2560   | Layout 1 |
| 2553   | Layout 1 |
| 2545   | Layout 1 |
| 2538   | Layout 1 |
| 2529   | Layout 1 |
| 2519   | Layout 1 |
| 2513   | Layout 1 |
| 2510   | Layout 1 |
| 2507   | Layout 1 |
| 2503   | Layout 1 |
| 2498   | Layout 1 |
| 2492   | Layout 1 |
| 2487   | Layout 1 |
| 2480   | Layout 1 |
| 2474   | Layout 1 |
| 2468   | Layout 1 |
| 2460   | Layout 1 |
| 2453   | Layout 1 |
| 2444   | Layout 1 |
| 2438   | Layout 1 |
| 2434   | Layout 1 |
| 2429   | Layout 1 |
| 2421   | Layout 1 |
| 2414   | Layout 1 |
| 2407   | Layout 1 |
| 2401   | Layout 1 |
| 2397   | Layout 1 |
| 2393   | Layout 1 |
| 2384   | Layout 1 |
| 2378   | Layout 1 |
| 2372   | Layout 1 |
| 2358   | Layout 1 |
| 2352   | Layout 1 |
| 2347   | Layout 1 |
| 2343   | Layout 1 |
| 2335   | Layout 1 |
| 2327   | Layout 1 |
| 2324   | Layout 1 |
| 2319   | Layout 1 |
| 2313   | Layout 1 |
| 2308   | Layout 1 |
| 2302   | Layout 1 |
| 2295   | Layout 1 |
| 2290   | Layout 1 |
| 2284   | Layout 1 |
| 2276   | Layout 1 |
| 2269   | Layout 1 |
| 2259   | Layout 1 |
| 2250   | Layout 1 |
| 2243   | Layout 1 |
| 2235   | Layout 1 |
| 2229   | Layout 1 |
| 2224   | Layout 1 |
| 2218   | Layout 1 |
| 2215   | Layout 1 |
| 2207   | Layout 1 |
| 2203   | Layout 1 |
| 2196   | Layout 1 |
| 2192   | Layout 1 |
| 2189   | Layout 1 |
| 2183   | Layout 1 |
| 2179   | Layout 1 |
| 2171   | Layout 1 |
| 2163   | Layout 1 |
| 2156   | Layout 1 |
| 2151   | Layout 1 |
| 2147   | Layout 1 |
| 2142   | Layout 1 |
| 2138   | Layout 1 |
| 2134   | Layout 1 |
| 2130   | Layout 1 |
| 2122   | Layout 1 |
| 2107   | Layout 1 |
| 2098   | Layout 1 |
| 2089   | Layout 1 |
| 2081   | Layout 1 |
| 2073   | Layout 1 |
| 2067   | Layout 1 |
| 2063   | Layout 1 |
| 2059   | Layout 1 |
| 2052   | Layout 1 |
| 2044   | Layout 1 |
| 2039   | Layout 1 |
| 2032   | Layout 1 |
| 2025   | Layout 1 |
| 2011   | Layout 1 |
| 2005   | Layout 1 |
| 2000   | Layout 1 |
| 1996   | Layout 1 |
| 1991   | Layout 1 |
| 1985   | Layout 1 |
| 1980   | Layout 1 |
| 1969   | Layout 1 |
| 1964   | Layout 1 |
| 1958   | Layout 1 |
| 1950   | Layout 1 |
| 1945   | Layout 1 |
| 1937   | Layout 1 |
| 1933   | Layout 1 |
| 1927   | Layout 1 |
| 1921   | Layout 1 |
| 1914   | Layout 1 |
| 1908   | Layout 1 |
| 1897   | Layout 1 |
| 1892   | Layout 1 |
| 1886   | Layout 1 |
| 1881   | Layout 1 |
| 1871   | Layout 1 |
| 1866   | Layout 1 |
| 1862   | Layout 1 |
| 1854   | No file  |
| 1846   | No file  |
| 1838   | No file  |
| 1832   | No file  |
| 1826   | No file  |
| 1822   | No file  |
| 1818   | No file  |
| 1804   | No file  |
| 1794   | No file  |
| 1790   | No file  |
| 1784   | No file  |
| 1774   | No file  |
| 1771   | No file  |
| 1762   | No file  |
| 1759   | No file  |
| 1754   | No file  |
| 1749   | No file  |
| 1743   | No file  |
| 1737   | No file  |
| 1731   | No file  |
| 1725   | No file  |
| 1717   | No file  |
| 1710   | No file  |
| 1704   | No file  |
| 1698   | No file  |
| 1690   | No file  |
| 1685   | No file  |
| 1680   | No file  |
| 1674   | No file  |
| 1668   | No file  |
| 1659   | No file  |
| 1649   | No file  |
| 1642   | No file  |
| 1636   | No file  |
| 1628   | No file  |
| 1622   | No file  |
| 1614   | No file  |
| 1608   | No file  |
| 1602   | No file  |
| 1598   | No file  |
| 1594   | No file  |
| 1590   | No file  |
| 1587   | No file  |
| 1584   | No file  |
| 1579   | No file  |
| 1572   | No file  |
| 1565   | No file  |
| 1559   | No file  |
| 1554   | No file  |
| 1547   | No file  |
| 1537   | No file  |
| 1529   | No file  |
| 1524   | No file  |
| 1519   | No file  |
| 1509   | No file  |
| 1506   | No file  |
| 1504   | No file  |
| 1500   | No file  |
| 1493   | No file  |
| 1489   | No file  |
| 1485   | No file  |
| 1481   | No file  |
| 1474   | No file  |
| 1466   | No file  |
| 1462   | No file  |
| 1459   | No file  |
| 1453   | No file  |
| 1450   | No file  |
| 1445   | No file  |
| 1439   | No file  |
| 1433   | No file  |
| 1430   | No file  |
| 1426   | No file  |
| 1421   | No file  |
| 1417   | No file  |
| 1416   | No file  |
| 1409   | No file  |
| 1405   | No file  |
| 1401   | No file  |
| 1396   | No file  |
| 1391   | No file  |
| 1390   | No file  |
| 1386   | No file  |
| 1381   | No file  |
| 1379   | No file  |
| 1372   | No file  |
| 1366   | No file  |
| 1364   | No file  |
| 1363   | No file  |
| 1360   | No file  |
| 1358   | No file  |
| 1355   | No file  |
| 1351   | No file  |
| 1348   | No file  |
| 1346   | No file  |
| 1341   | No file  |
| 1340   | No file  |
| 1338   | No file  |
| 1335   | No file  |
| 1333   | No file  |
| 1329   | No file  |
| 1327   | No file  |
| 1324   | No file  |
| 1321   | No file  |
| 1319   | No file  |
| 1318   | No file  |
| 1316   | No file  |
| 1313   | No file  |
| 1311   | No file  |
| 1309   | No file  |
| 1304   | No file  |
| 1292   | No file  |
| 1286   | No file  |
| 1280   | No file  |
| 1276   | No file  |
| 1267   | No file  |
| 1261   | No file  |
| 1256   | No file  |
| 1250   | No file  |
| 1246   | No file  |
| 1239   | No file  |
| 1230   | No file  |
| 1226   | No file  |
| 1220   | No file  |
| 1217   | No file  |
| 1211   | No file  |
| 1210   | No file  |
| 1208   | No file  |
| 1203   | No file  |
| 1197   | No file  |
| 1194   | No file  |
| 1192   | No file  |
| 1187   | No file  |
| 1183   | No file  |
| 1177   | No file  |
| 1173   | No file  |
| 1167   | No file  |
| 1164   | No file  |
| 1156   | No file  |
| 1149   | No file  |
| 1144   | No file  |
| 1137   | No file  |
| 1132   | No file  |
| 1127   | No file  |
| 1122   | No file  |
| 1118   | No file  |
| 1114   | No file  |
| 1109   | No file  |
| 1102   | No file  |
| 1096   | No file  |
| 1088   | No file  |
| 1081   | No file  |
| 1076   | No file  |
| 1069   | No file  |
| 1064   | No file  |
| 1058   | No file  |
| 1051   | No file  |
| 1044   | No file  |
| 1036   | No file  |
| 1026   | No file  |
| 1016   | No file  |
| 1009   | No file  |
| 1005   | No file  |
| 1000   | No file  |
| 998    | No file  |
| 990    | No file  |
| 979    | No file  |
| 972    | No file  |
| 963    | No file  |
| 955    | No file  |
| 946    | No file  |
| 938    | No file  |
| 927    | No file  |
| 911    | No file  |
| 904    | No file  |
| 899    | No file  |
| 894    | No file  |
| 885    | No file  |
| 879    | No file  |
| 872    | No file  |
| 864    | No file  |
| 855    | No file  |
| 853    | No file  |
| 845    | No file  |
| 837    | No file  |
| 829    | No file  |
| 822    | No file  |
| 814    | No file  |
| 805    | No file  |
| 794    | No file  |
| 787    | No file  |
| 780    | No file  |
| 771    | No file  |
| 760    | No file  |
| 748    | No file  |
| 741    | No file  |
| 736    | No file  |
| 731    | No file  |
| 723    | No file  |
| 711    | No file  |
| 707    | No file  |
| 697    | No file  |
| 689    | No file  |
| 683    | No file  |
| 678    | No file  |
| 670    | No file  |
| 661    | No file  |
| 656    | No file  |
| 652    | No file  |
| 643    | No file  |
| 637    | No file  |
| 630    | No file  |
| 627    | No file  |
| 621    | No file  |
| 617    | No file  |
| 615    | No file  |
| 606    | No file  |
| 599    | No file  |
| 592    | No file  |
| 586    | No file  |
| 577    | No file  |
| 569    | No file  |
| 561    | No file  |
| 554    | No file  |
| 542    | No file  |
| 532    | No file  |
| 531    | No file  |
| 526    | No file  |
| 521    | No file  |
| 517    | No file  |
| 510    | No file  |
| 508    | No file  |
| 504    | No file  |
| 497    | No file  |
| 491    | No file  |
| 485    | No file  |
| 478    | No file  |
| 472    | No file  |
| 466    | No file  |
| 457    | No file  |
| 452    | No file  |
| 449    | No file  |
| 435    | No file  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Region names (LOC type 17, keyed by `region_key`)     |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

| Offset              | Type              | Field              | Notes                                                    |
| ------------------- | ----------------- | ------------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                           |
| `+0x04`             | u32               | record_count       | Observed `21`                                            |
| `+0x08`             | Row[record_count] | records            | See Row; byte-packed                                     |
| `records+0x00`      | String Table      | string_table       | The PABR string table, present but empty                 |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 26 × count` |
| `string_table+0x04` | u32               | zero               | Always `0`                                               |

The file is `8 + 26 × 21 + 12 = 566` bytes. The parser rejects a file whose rows do not end exactly at `string_table_start`.

### Row (26 bytes)

| Offset  | Type | Field                    | Notes                                                                                     |
| ------- | ---- | ------------------------ | ----------------------------------------------------------------------------------------- |
| `+0x00` | u32  | key                      | Unique, ascending, with gaps (`1`, `2`, `6` to `24`)                                      |
| `+0x04` | u16  | region_key               | `regioninfo.bss` region key; LOC type 17 names it. Every row resolves                     |
| `+0x06` | u32  | effect_spawn_percent_min | Lowest chance that the blizzard effect spawns, 1,000,000 = 100%; `50000` to `500000`      |
| `+0x0A` | u32  | effect_spawn_percent_max | Highest chance, same scale; `120000` to `800000`, always above the minimum                |
| `+0x0E` | f32  | wind_x                   | Wind vector, X; `1.0`, `2.0` or `3.0`                                                     |
| `+0x12` | f32  | wind_y                   | Wind vector, Y; `0.0` on every row                                                        |
| `+0x16` | f32  | wind_z                   | Wind vector, Z; `0.0` on every row                                                        |

The value ranges are from client 3473. The spawn chances and `wind_x` come in a few fixed sets per area (client 3458):

| effect_spawn_percent_min | effect_spawn_percent_max | wind_x | Regions                                                                      |
| ------------------------ | ------------------------ | ------ | ---------------------------------------------------------------------------- |
| `400000` (40%)           | `800000` (80%)           | `3.0`  | 1126 Mountain of Eternal Winter                                              |
| `250000` (25%)           | `500000` (50%)           | `2.0`  | 1175 Mountain of Eternal Winter; all Ulukita rows except Velandir            |
| `200000` (20%)           | `400000` (40%)           | `3.0`  | 1146, 1163 Mountain of Eternal Winter                                        |
| `100000` (10%)           | `250000` (25%)           | `2.0`  | Jade Starlight Forest (1127, 1147, 1164), Snowstorm Guard Post (1125, 1145)  |
| `50000` (5%)             | `120000` (12%)           | `1.0`  | Bronte's Bolt (1123, 1143, 1160)                                             |
| `500000` (50%)           | `800000` (80%)           | `3.0`  | 1382 Velandir                                                                |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Field Names

The names are the columns of the `Blizzard_Region_Table` sheet that a private server on client 1784 ships in its `DataSheets.bexcel` and in the developer workbook `datasheet_regiondatatable.xlsm`: `Index`, `RegionIndex`, `EffectSpawnPercentMin`, `EffectSpawnPercentMax`, `Wind_X`, `Wind_Y`, `Wind_Z`. The sheet holds 5 rows. The same private server's `blizzardregioninfo.bss`, built from that sheet, is 150 bytes: 5 rows of this 26-byte layout with the seven columns in sheet order, `Wind_X` to `Wind_Z` as f32. The column-to-offset match rests on that build, because the sheet and the client file share only keys 1 and 2:

| Key | Region | Sheet (client 1784)       | Client 3473               |
| --- | ------ | ------------------------- | ------------------------- |
| 1   | 1126   | `100000`, `300000`, `1.0` | `400000`, `800000`, `3.0` |
| 2   | 1175   | `250000`, `500000`, `2.0` | `250000`, `500000`, `2.0` |

The region keys of both rows and every column of key 2 match. `Wind_Y` and `Wind_Z` are `0` on every row of the sheet and of the client file.

The server dump of that private server holds the loader messages for `BlizzardRegionInfoStaticStatus` (sheet `Blizzard_Region_Table`, loader `loadBlizzardRegionInfo`). They reject an `EffectSpawnPercentMin` or `EffectSpawnPercentMax` outside "1~100%", a minimum above the maximum, and a `RegionIndex` with no region info. The sheet's largest value is `1000000` (key 5, both columns), so the chances are on the 1,000,000 = 100% scale.

Neither the 2016 client with debug symbols nor the tables of a private server on client 519 have a blizzard type or table. The client Lua has no blizzard text.

## Notes

- A region name can appear on several rows: LOC gives the same name to several region keys (1126, 1146, 1163 and 1175 are all Mountain of Eternal Winter).
- The keys skip `3`, `4` and `5`. On client 1784 the sheet has them for regions 1176, 1177 and 1178 (chances 50% to 80%, 70% to 100% and 100% to 100%, `wind_x` 3, 4 and 5). On client 3473 region 1176 is Snowfall Crasher: Alpine Glide, and 1177 and 1178 are not in `regioninfo.bss`.
- `wind_y` and `wind_z` are read as f32 because they are the other two axes of the `Wind_X` vector. Every row holds `0`, which reads the same as a u32.
- `edaniaregioninfo.bss` is the other small region-variant table. It is not the same layout (9-byte rows keyed by an Edania region value, no region key), so the two files have separate parsers.

## Open Questions

### What the Wind Vector Does

Only `wind_x` is set (`1.0` to `3.0`; the sheet on client 1784 goes up to `5.0`), with `wind_y` and `wind_z` at `0`. Whether the vector is a direction scaled by strength, a strength level on X only, or a push on the player is not shown by the sheet or the client Lua.

### What Rolls the Spawn Chance

The chance range says how likely the blizzard effect is, but not how often the client or server rolls it or what picks a value between the minimum and the maximum.

## In-Game Checks

### Blizzard Frequency per Region

Needs zone (all):

- Bronte's Bolt
- Mountain of Eternal Winter

Checks that the spawn chance sets how often a region has a blizzard. Bronte's Bolt rows hold 5% to 12%, the Mountain of Eternal Winter rows 20% to 80%.

1. Stand in Bronte's Bolt for 30 minutes and note how long a blizzard is visible.
2. Stand in the Mountain of Eternal Winter for 30 minutes and note the same. Four region keys carry that name (1126, 1146, 1163, 1175, at 20% to 80%), so the spot may be any of them.
3. Compare the two shares of time.

Expected result: the blizzard shows for a small share of the time in Bronte's Bolt and for a larger share in the Mountain of Eternal Winter. Equal shares would mean the chance does not set the frequency.
