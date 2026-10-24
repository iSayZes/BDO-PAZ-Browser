# `villagesiegeinfo.bss` Format

## Purpose

The areas of the Node War (village siege) region map, one row per colour
of `ui_texture/minimap/area/villagesiegemap_2024.bmp`: the colour, a copy
of it, the node war region the area covers and a u16 that numbers the
rows territory by territory. Client 3482 has 41 rows: 36 node war nodes,
the four capitals and the `0d0d0d` row with no region. The rows have the
shape of the [`oceansiegeinfo.bss`](oceansiegeinfo_bss.md) rows.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes | Records | Row bytes               |
| ------ | -------------- | ------- | ---------------------- | ----- | ------- | ----------------------- |
| 2      | 2978 and later | 3483    | `villagesiegeinfo.bss` | 674   | 41 Row  | 14 to 16, 16 on average |
| 1      | 1276 to 2970   | 2970    | `villagesiegeinfo.bss` | 1,820 | 59 Row  | 22 to 24, 24 on average |

| Layout | File                   | Known           | Unknown       |
| ------ | ---------------------- | --------------- | ------------- |
| 2      | `villagesiegeinfo.bss` | 510 B (75.7%)   | 164 B (24.3%) |
| 1      | `villagesiegeinfo.bss` | 1,112 B (61.1%) | 708 B (38.9%) |

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
| 3373   | Layout 2             |
| 3364   | Layout 2             |
| 3356   | Layout 2             |
| 3349   | Layout 2             |
| 3342   | Layout 2             |
| 3335   | Layout 2             |
| 3326   | Layout 2             |
| 3321   | Layout 2             |
| 3314   | Layout 2             |
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
| 3151   | Layout 2             |
| 3144   | Layout 2             |
| 3133   | Layout 2             |
| 3125   | Layout 2             |
| 3118   | Layout 2             |
| 3111   | Layout 2             |
| 3103   | Layout 2             |
| 3095   | Layout 2             |
| 3086   | Layout 2             |
| 3072   | Layout 2             |
| 3062   | Layout 2             |
| 3052   | Layout 2             |
| 3045   | Layout 2             |
| 3037   | Layout 2             |
| 3030   | Layout 2             |
| 3021   | Layout 2             |
| 3012   | Layout 2             |
| 3002   | Layout 2             |
| 2995   | Layout 2             |
| 2987   | Layout 2             |
| 2978   | Layout 2             |
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

| File                  | Required | Role                                                   |
| --------------------- | -------- | ------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Region names, LOC type 17, for the `region_keys` cell |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 14 bytes + region keys)

| Offset             | Type                  | Field                  | Notes                                                                      |
| ------------------ | --------------------- | ---------------------- | -------------------------------------------------------------------------- |
| `+0x00`            | bytes[3]              | map_color              | Region map colour, stored blue, green, red; unique per row. See Map Colours |
| `+0x03`            | u8                    | unknown_03             | Always `0`                                                                 |
| `+0x04`            | bytes[3]              | map_color_dup          | Equals `map_color` on every row; see Field Names                           |
| `+0x07`            | u8                    | unknown_07             | Always `0`                                                                 |
| `+0x08`            | u32                   | region_key_count       | Number of `region_keys`; `0` or `1` on client 3482                         |
| `+0x0C`            | u16[region_key_count] | region_keys            | `regioninfo.bss` region keys, LOC type 17 names. See Map Colours           |
| `region_keys+0x00` | u16                   | unknown_region_keys_00 | `0` to `40` on client 3482, unique per row. See Open Questions             |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3482, `27` on client 1784 |
| `+0x04` | pstr[string_count] | strings      | Read by `unknown_str_ref` in Layout 1 only                |

## Layout 1

### Row (variable: 22 bytes + region keys)

| Offset             | Type                  | Field                  | Notes                                                              |
| ------------------ | --------------------- | ---------------------- | ------------------------------------------------------------------ |
| `+0x00`            | bytes[3]              | map_color              |                                                                    |
| `+0x03`            | u8                    | unknown_03             |                                                                    |
| `+0x04`            | bytes[3]              | map_color_dup          |                                                                    |
| `+0x07`            | u8                    | unknown_07             |                                                                    |
| `+0x08`            | u32                   | region_key_count       |                                                                    |
| `+0x0C`            | u16[region_key_count] | region_keys            |                                                                    |
| `region_keys+0x00` | u32                   | unknown_str_ref        | Index into the string table: 27 Korean town names on client 1784   |
| `region_keys+0x04` | u16                   | unknown_region_keys_00 | `0` to `81` on client 1784, unique per row                         |
| `region_keys+0x06` | u32                   | unknown_region_keys_06 | `0` on every row of client 1784                                    |

## Map Colours

Client 3482, in file order: `map_color` read as `rrggbb`, the region,
its territory in `regioninfo.bss` and the u16 after the list. The `.rid`
position is the colour's place in `villagesiegemap_2024.bmp.rid` (2024),
or for the four capitals in `villagesiegemap.bmp.rid` (old map).

| `map_color` | `region_keys`                 | Territory    | `unknown_region_keys_00` | Position in `.rid` |
| ----------- | ----------------------------- | ------------ | ------------------------ | ------------------ |
| `3c784b`    | 1556 Great Red Spot           | Outer Edania | 39                       | 2024: 5            |
| `781ecd`    | 12 Forest of Plunder          | Balenos      | 2                        | 2024: 16           |
| `0d0d0d`    | none                          |              | 0                        | 2024: 1            |
| `1ecdcd`    | 16 Bartali Farm               | Balenos      | 3                        | 2024: 20           |
| `3cc8c8`    | 1574 Great White Spot         | Outer Edania | 36                       | 2024: 6            |
| `d5ffa4`    | 32 Heidel                     | Serendia     | 26                       | old map: 19        |
| `1e2dcd`    | 15 Cron Castle                | Balenos      | 1                        | 2024: 14           |
| `a573cd`    | 343 Wolf Hills                | Balenos      | 4                        | 2024: 15           |
| `9696fa`    | 186 Quint Hill                | Calpheon     | 17                       | 2024: 18           |
| `7878fa`    | 113 Hexe Sanctuary            | Calpheon     | 16                       | 2024: 31           |
| `e6e6fa`    | 290 Longleaf Tree Sentry Post | Calpheon     | 15                       | 2024: 30           |
| `782dcd`    | 7 Altar of Agris              | Balenos      | 5                        | 2024: 17           |
| `78787d`    | 73 Biraghi Den                | Serendia     | 7                        | 2024: 24           |
| `6464cd`    | 9 Western Guard Camp          | Balenos      | 6                        | 2024: 19           |
| `5680c1`    | 1349 City of the Dead         | Ulukita      | 34                       | 2024: 35           |
| `4b4b7d`    | 37 Glish Swamp                | Serendia     | 12                       | 2024: 25           |
| `a5a57d`    | 60 Alejandro Farm             | Serendia     | 8                        | 2024: 22           |
| `e1e17d`    | 67 Bloody Monastery           | Serendia     | 9                        | 2024: 29           |
| `b4b47d`    | 71 Castle Ruins               | Serendia     | 10                       | 2024: 26           |
| `ffe4f6`    | 5 Velia                       | Balenos      | 25                       | old map: 7         |
| `c8c87d`    | 74 Orc Camp                   | Serendia     | 11                       | 2024: 27           |
| `b4b4fa`    | 198 Khuruto Cave              | Calpheon     | 13                       | 2024: 21           |
| `8c2323`    | 638 Altas Farmland            | Valencia     | 24                       | 2024: 9            |
| `fafafa`    | 247 Calpheon Castle Site      | Calpheon     | 14                       | 2024: 23           |
| `e1e1fa`    | 127 Trina Fort                | Calpheon     | 18                       | 2024: 28           |
| `8ce6e6`    | 616 Rakshan Observatory       | Valencia     | 23                       | 2024: 11           |
| `8c9696`    | 692 Areha Palm Forest         | Valencia     | 19                       | 2024: 12           |
| `8c5050`    | 682 Ancado Coast              | Valencia     | 20                       | 2024: 8            |
| `8ca5a5`    | 615 Pilgrim's Sanctum: Fast   | Valencia     | 21                       | 2024: 13           |
| `561e0c`    | 1379 Karasi Canyon            | Ulukita      | 32                       | 2024: 36           |
| `8cfafa`    | 617 Valencia Castle           | Valencia     | 22                       | 2024: 10           |
| `fefec7`    | 202 Altinova                  | Mediah       | 27                       | old map: 12        |
| `ffc8ff`    | 229 Valencia City             | Valencia     | 28                       | old map: 2         |
| `560032`    | 1347 Atessahra                | Ulukita      | 30                       | 2024: 32           |
| `563c96`    | 1367 Neruda Plain             | Ulukita      | 29                       | 2024: 33           |
| `5600c8`    | 1350 Tungrad Ruins            | Ulukita      | 31                       | 2024: 34           |
| `561e70`    | 1381 Shakhtar Wilds           | Ulukita      | 33                       | 2024: 37           |
| `3ca032`    | 1559 Neftak Outpost           | Outer Edania | 35                       | 2024: 4            |
| `3c6464`    | 1563 Escar Mountains          | Outer Edania | 37                       | 2024: 7            |
| `3cf0d2`    | 1599 Crossroads of Defiance   | Outer Edania | 38                       | 2024: 3            |
| `3cb4f0`    | 1584 Azure Battlefield        | Outer Edania | 40                       | 2024: 2            |

## Field Names

The 2016 `gc::VillageSiegeInfo` holds `pa::Color _colorKey` (members `b`,
`g`, `r`, `a`) and `gc::KeyType<unsigned short> _regionKey`. The row is
the colour the table is keyed by, then the struct's own `_colorKey`
(`map_color_dup`, with `unknown_07` its `a` byte), then the region keys,
now a u32-counted list. `map_color` follows
[`hardcorechannelinfo.bss`](hardcorechannelinfo_bss.md), Field Names: on
client 3482 `villagesiegemap_2024.bmp.rid` lists 37 colours, and all 37
are `map_color` values of this file; the other four rows are the capitals
Velia, Heidel, Altinova and Valencia City, whose colours
`villagesiegemap.bmp.rid` lists. `villagesiegemap_2024.bmp` is the map
`fieldinfo.bss` names in `unknown_73` (`regionmapinfo.bss` key 12).
`region_keys` are `regioninfo.bss` keys: on client 3482 all 40 are regions
with a `max_participants` above `0`, the node war regions and the four
capitals.

The `VillageSiege_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 (`VillageSiegeKey`, `R`, `G`, `B`, `RegionKey`,
`RegionName`) holds 33 rows with up to six region keys each, while the
client 1784 file has 82 rows with one region each; the sheet does not
match the file and names no field here.

## Notes

- Layout 1 (clients 1348 to 2765) adds a u32 string-table index and a u32 that is
  always `0` around the u16, and its string table holds 27 Korean town
  names (`타리프 마을`, `벨리아 마을`, `알티노바`, ...). Layout 2 drops
  both and the strings.
- The `0d0d0d` row, first in the 2024 palette, has no region and
  `unknown_region_keys_00` `0`, as the shared first-palette row of the
  other map colour tables.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/siege_tables.py`: `map_color` as `rrggbb` and the
  region keys with their names.

## Open Questions

### The u16 After the Region List

`unknown_region_keys_00` numbers the rows territory by territory on client
3482: `1` to `6` the Balenos nodes, `7` to `12` Serendia, `13` to `18`
Calpheon, `19` to `24` Valencia, `25` to `28` the capitals Velia, Heidel,
Altinova and Valencia City, `29` to `34` Ulukita and `35` to `40` Outer
Edania. The sheet's `VillageSiegeKey` column is a lead, but its client
1784 values do not match the file's. What reads the number is open.

### The Town Names of Client 1784

In Layout 1, `unknown_str_ref` points 82 rows at 27 town names. Which
town a node gets (the nearest town, its supply town or its tax town) is
open, and so is why Layout 2 dropped it.
