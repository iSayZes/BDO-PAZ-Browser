# `greatseaoption.bss` Format

## Purpose

One record of Great Ocean and island barter options: food use, the
explore cooldown, the ship management and barter ranges, barter exchange
and reset counts, discount values and two EXP values. The fields are the
client side of the `IslandExplore_Option` sheet (see Field Names).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | -------------- | --------- |
| 4      | 2717 and later | 3483    | `greatseaoption.bss` | 88    | 1 String Table | 4         |
| 3      | 1313 to 2709   | 2709    | `greatseaoption.bss` | 86    | 1 String Table | 4         |
| 2      | 1304 to 1311   | 1311    | `greatseaoption.bss` | 82    | 1 String Table | 4         |
| 1      | 1267 to 1292   | 1292    | `greatseaoption.bss` | 54    | 1 String Table | 4         |

| Layout | File                 | Known        | Unknown      |
| ------ | -------------------- | ------------ | ------------ |
| 4      | `greatseaoption.bss` | 75 B (85.2%) | 13 B (14.8%) |
| 3      | `greatseaoption.bss` | 73 B (84.9%) | 13 B (15.1%) |
| 2      | `greatseaoption.bss` | 73 B (89.0%) | 9 B (11.0%)  |
| 1      | `greatseaoption.bss` | 53 B (98.1%) | 1 B (1.9%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 4             |
| 3482   | Layout 4             |
| 3474   | Layout 4             |
| 3473   | Layout 4             |
| 3464   | Layout 4             |
| 3458   | Layout 4             |
| 3454   | Layout 4             |
| 3444   | Layout 4             |
| 3435   | Layout 4             |
| 3426   | Layout 4             |
| 3418   | Layout 4             |
| 3412   | Layout 4             |
| 3402   | Layout 4             |
| 3396   | Layout 4             |
| 3387   | Layout 4             |
| 3381   | Layout 4             |
| 3373   | Layout 4             |
| 3364   | Layout 4             |
| 3356   | Layout 4             |
| 3349   | Layout 4             |
| 3342   | Layout 4             |
| 3335   | Layout 4             |
| 3326   | Layout 4             |
| 3321   | Layout 4             |
| 3314   | Layout 4             |
| 3303   | Layout 4             |
| 3302   | Layout 4             |
| 3293   | Layout 4             |
| 3283   | Layout 4             |
| 3275   | Layout 4             |
| 3267   | Layout 4             |
| 3258   | Layout 4             |
| 3251   | Layout 4             |
| 3242   | Layout 4             |
| 3235   | Layout 4             |
| 3229   | Layout 4             |
| 3212   | Layout 4             |
| 3203   | Layout 4             |
| 3193   | Layout 4             |
| 3186   | Layout 4             |
| 3177   | Layout 4             |
| 3169   | Layout 4             |
| 3158   | Layout 4             |
| 3151   | Layout 4             |
| 3144   | Layout 4             |
| 3133   | Layout 4             |
| 3125   | Layout 4             |
| 3118   | Layout 4             |
| 3111   | Layout 4             |
| 3103   | Layout 4             |
| 3095   | Layout 4             |
| 3086   | Layout 4             |
| 3072   | Layout 4             |
| 3062   | Layout 4             |
| 3052   | Layout 4             |
| 3045   | Layout 4             |
| 3037   | Layout 4             |
| 3030   | Layout 4             |
| 3021   | Layout 4             |
| 3012   | Layout 4             |
| 3002   | Layout 4             |
| 2995   | Layout 4             |
| 2987   | Layout 4             |
| 2978   | Layout 4             |
| 2970   | Layout 4             |
| 2959   | Layout 4             |
| 2951   | Layout 4             |
| 2942   | Layout 4             |
| 2935   | Layout 4             |
| 2932   | Layout 4             |
| 2923   | Layout 4             |
| 2919   | Layout 4             |
| 2907   | Layout 4             |
| 2900   | Layout 4             |
| 2891   | Layout 4             |
| 2882   | Layout 4             |
| 2872   | Layout 4             |
| 2863   | Layout 4             |
| 2855   | Layout 4             |
| 2849   | Layout 4             |
| 2844   | Layout 4             |
| 2834   | Layout 4             |
| 2825   | Layout 4             |
| 2819   | Layout 4             |
| 2811   | Layout 4             |
| 2803   | Layout 4             |
| 2794   | Layout 4             |
| 2783   | Layout 4             |
| 2774   | Layout 4             |
| 2765   | Layout 4             |
| 2756   | Layout 4             |
| 2750   | Layout 4             |
| 2743   | Layout 4             |
| 2736   | Layout 4             |
| 2726   | Layout 4             |
| 2717   | Layout 4             |
| 2709   | Layout 3             |
| 2703   | Layout 3             |
| 2695   | Layout 3             |
| 2684   | Layout 3             |
| 2672   | Layout 3             |
| 2665   | Layout 3             |
| 2657   | Layout 3             |
| 2649   | Layout 3             |
| 2644   | Layout 3             |
| 2637   | Layout 3             |
| 2629   | Layout 3             |
| 2619   | Layout 3             |
| 2612   | Layout 3             |
| 2606   | Layout 3             |
| 2602   | Layout 3             |
| 2601   | Layout 3             |
| 2592   | Layout 3             |
| 2583   | Layout 3             |
| 2575   | Layout 3             |
| 2567   | Layout 3             |
| 2560   | Layout 3             |
| 2553   | Layout 3             |
| 2545   | Layout 3             |
| 2538   | Layout 3             |
| 2529   | Layout 3             |
| 2519   | Layout 3             |
| 2513   | Layout 3             |
| 2510   | Layout 3             |
| 2507   | Layout 3             |
| 2503   | Layout 3             |
| 2498   | Layout 3             |
| 2492   | Layout 3             |
| 2487   | Layout 3             |
| 2480   | Layout 3             |
| 2474   | Layout 3             |
| 2468   | Layout 3             |
| 2460   | Layout 3             |
| 2453   | Layout 3             |
| 2444   | Layout 3             |
| 2438   | Layout 3             |
| 2434   | Layout 3             |
| 2429   | Layout 3             |
| 2421   | Layout 3             |
| 2414   | Layout 3             |
| 2407   | Layout 3             |
| 2401   | Layout 3             |
| 2397   | Layout 3             |
| 2393   | Layout 3             |
| 2384   | Layout 3             |
| 2378   | Layout 3             |
| 2372   | Layout 3             |
| 2358   | Layout 3             |
| 2352   | Layout 3             |
| 2347   | Layout 3             |
| 2343   | Layout 3             |
| 2335   | Layout 3             |
| 2327   | Layout 3             |
| 2324   | Layout 3             |
| 2319   | Layout 3             |
| 2313   | Layout 3             |
| 2308   | Layout 3             |
| 2302   | Layout 3             |
| 2295   | Layout 3             |
| 2290   | Layout 3             |
| 2284   | Layout 3             |
| 2276   | Layout 3             |
| 2269   | Layout 3             |
| 2259   | Layout 3             |
| 2250   | Layout 3             |
| 2243   | Layout 3             |
| 2235   | Layout 3             |
| 2229   | Layout 3             |
| 2224   | Layout 3             |
| 2218   | Layout 3             |
| 2215   | Layout 3             |
| 2207   | Layout 3             |
| 2203   | Layout 3             |
| 2196   | Layout 3             |
| 2192   | Layout 3             |
| 2189   | Layout 3             |
| 2183   | Layout 3             |
| 2179   | Layout 3             |
| 2171   | Layout 3             |
| 2163   | Layout 3             |
| 2156   | Layout 3             |
| 2151   | Layout 3             |
| 2147   | Layout 3             |
| 2142   | Layout 3             |
| 2138   | Layout 3             |
| 2134   | Layout 3             |
| 2130   | Layout 3             |
| 2122   | Layout 3             |
| 2107   | Layout 3             |
| 2098   | Layout 3             |
| 2089   | Layout 3             |
| 2081   | Layout 3             |
| 2073   | Layout 3             |
| 2067   | Layout 3             |
| 2063   | Layout 3             |
| 2059   | Layout 3             |
| 2052   | Layout 3             |
| 2044   | Layout 3             |
| 2039   | Layout 3             |
| 2032   | Layout 3             |
| 2025   | Layout 3             |
| 2011   | Layout 3             |
| 2005   | Layout 3             |
| 2000   | Layout 3             |
| 1996   | Layout 3             |
| 1991   | Layout 3             |
| 1985   | Layout 3             |
| 1980   | Layout 3             |
| 1969   | Layout 3             |
| 1964   | Layout 3             |
| 1958   | Layout 3             |
| 1950   | Layout 3             |
| 1945   | Layout 3             |
| 1937   | Layout 3             |
| 1933   | Layout 3             |
| 1927   | Layout 3             |
| 1921   | Layout 3             |
| 1914   | Layout 3             |
| 1908   | Layout 3             |
| 1897   | Layout 3             |
| 1892   | Layout 3             |
| 1886   | Layout 3             |
| 1881   | Layout 3             |
| 1871   | Layout 3             |
| 1866   | Layout 3             |
| 1862   | Layout 3             |
| 1854   | Layout 3             |
| 1846   | Layout 3             |
| 1838   | Layout 3             |
| 1832   | Layout 3             |
| 1826   | Layout 3             |
| 1822   | Layout 3             |
| 1818   | Layout 3             |
| 1804   | Layout 3             |
| 1794   | Layout 3             |
| 1790   | Layout 3             |
| 1784   | Layout 3             |
| 1774   | Layout 3             |
| 1771   | Layout 3             |
| 1762   | Layout 3             |
| 1759   | Layout 3             |
| 1754   | Layout 3             |
| 1749   | Layout 3             |
| 1743   | Layout 3             |
| 1737   | Layout 3             |
| 1731   | Layout 3             |
| 1725   | Layout 3             |
| 1717   | Layout 3             |
| 1710   | Layout 3             |
| 1704   | Layout 3             |
| 1698   | Layout 3             |
| 1690   | Layout 3             |
| 1685   | Layout 3             |
| 1680   | Layout 3             |
| 1674   | Layout 3             |
| 1668   | Layout 3             |
| 1659   | Layout 3             |
| 1649   | Layout 3             |
| 1642   | Layout 3             |
| 1636   | Layout 3             |
| 1628   | Layout 3             |
| 1622   | Layout 3             |
| 1614   | Layout 3             |
| 1608   | Layout 3             |
| 1602   | Layout 3             |
| 1598   | Layout 3             |
| 1594   | Layout 3             |
| 1590   | Layout 3             |
| 1587   | Layout 3             |
| 1584   | Layout 3             |
| 1579   | Layout 3             |
| 1572   | Layout 3             |
| 1565   | Layout 3             |
| 1559   | Layout 3             |
| 1554   | Layout 3             |
| 1547   | Layout 3             |
| 1537   | Layout 3             |
| 1529   | Layout 3             |
| 1524   | Layout 3             |
| 1519   | Layout 3             |
| 1509   | Layout 3             |
| 1506   | Layout 3             |
| 1504   | Layout 3             |
| 1500   | Layout 3             |
| 1493   | Layout 3             |
| 1489   | Layout 3             |
| 1485   | Layout 3             |
| 1481   | Layout 3             |
| 1474   | Layout 3             |
| 1466   | Layout 3             |
| 1462   | Layout 3             |
| 1459   | Layout 3             |
| 1453   | Layout 3             |
| 1450   | Layout 3             |
| 1445   | Layout 3             |
| 1439   | Layout 3             |
| 1433   | Layout 3             |
| 1430   | Layout 3             |
| 1426   | Layout 3             |
| 1421   | Layout 3             |
| 1417   | Layout 3             |
| 1416   | Layout 3             |
| 1409   | Layout 3             |
| 1405   | Layout 3             |
| 1401   | Layout 3             |
| 1396   | Layout 3             |
| 1391   | Layout 3             |
| 1390   | Layout 3             |
| 1386   | Layout 3             |
| 1381   | Layout 3             |
| 1379   | Layout 3             |
| 1372   | Layout 3             |
| 1366   | Layout 3             |
| 1364   | Layout 3             |
| 1363   | Layout 3             |
| 1360   | Layout 3             |
| 1358   | Layout 3             |
| 1355   | Layout 3             |
| 1351   | Layout 3             |
| 1348   | Layout 3             |
| 1346   | Layout 3             |
| 1341   | Layout 3             |
| 1340   | Layout 3             |
| 1338   | Layout 3             |
| 1335   | Layout 3             |
| 1333   | Layout 3             |
| 1329   | Layout 3             |
| 1327   | Layout 3             |
| 1324   | Layout 3             |
| 1321   | Layout 3             |
| 1319   | Layout 3             |
| 1318   | Layout 3             |
| 1316   | Layout 3             |
| 1313   | Layout 3             |
| 1311   | Layout 2             |
| 1309   | Layout 2             |
| 1304   | Layout 2             |
| 1292   | Layout 1             |
| 1286   | Layout 1             |
| 1280   | Layout 1             |
| 1276   | Layout 1             |
| 1267   | Layout 1             |
| 1261   | No documented layout |
| 1256   | No documented layout |
| 1250   | No documented layout |
| 1246   | No documented layout |
| 1239   | No documented layout |
| 1230   | No file              |
| 1226   | No file              |
| 1220   | No file              |
| 1217   | No file              |
| 1211   | No file              |
| 1210   | No file              |
| 1208   | No file              |
| 1203   | No file              |
| 1197   | No file              |
| 1194   | No file              |
| 1192   | No file              |
| 1187   | No file              |
| 1183   | No file              |
| 1177   | No file              |
| 1173   | No file              |
| 1167   | No file              |
| 1164   | No file              |
| 1156   | No file              |
| 1149   | No file              |
| 1144   | No file              |
| 1137   | No file              |
| 1132   | No file              |
| 1127   | No file              |
| 1122   | No file              |
| 1118   | No file              |
| 1114   | No file              |
| 1109   | No file              |
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
| 829    | No file              |
| 822    | No file              |
| 814    | No file              |
| 805    | No file              |
| 794    | No file              |
| 787    | No file              |
| 780    | No file              |
| 771    | No file              |
| 760    | No file              |
| 748    | No file              |
| 741    | No file              |
| 736    | No file              |
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

None.

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset              | Type         | Field                 | Notes                                                               |
| ------------------- | ------------ | --------------------- | ------------------------------------------------------------------- |
| `+0x00`             | char[4]      | magic                 | ASCII `PABR`                                                        |
| `+0x04`             | u32          | food_consume          | `100000` on clients 1784 and 3482                                   |
| `+0x08`             | u32          | explore_cool_time     | `1200` on clients 1784 and 3482                                     |
| `+0x0C`             | f32          | ship_management_range | `15000` on client 1784, `20000` on client 3482                      |
| `+0x10`             | f32          | barter_range          | `5000` on clients 1784 and 3482                                     |
| `+0x14`             | u8           | reset_cool_time       | `4` on client 1784, `2` on client 3482                              |
| `+0x15`             | u8           | unknown_15            | `0` on every client checked                                         |
| `+0x16`             | u32          | max_exchange_count    | `1000000` on clients 1784 and 3482                                  |
| `+0x1A`             | u32          | over_max_count        | `1000000` on clients 1784 and 3482                                  |
| `+0x1E`             | u32          | max_reset_count       | `100` on clients 1784 and 3482                                      |
| `+0x22`             | u16          | barter_reset_time     | `6` on client 3482                                                  |
| `+0x24`             | u32          | discount_rate         | `100000` on clients 1784 and 3482                                   |
| `+0x28`             | u32          | add_reset_count       | `50` on clients 1784 and 3482                                       |
| `+0x2C`             | u32          | reset_need_count      | `30` on clients 1784 and 3482                                       |
| `+0x30`             | u32          | time_discount         | `10000` on clients 1784 and 3482                                    |
| `+0x34`             | u32          | time_discount_limit   | `50000` on clients 1784 and 3482                                    |
| `+0x38`             | u32          | sub_employee_exp      | `20` on clients 1784 and 3482                                       |
| `+0x3C`             | u32          | unknown_3c            | `0` on every client checked                                         |
| `+0x40`             | u32          | sub_trade_exp         | `499` on clients 1784 and 3482                                      |
| `+0x44`             | u32          | unknown_44            | `0` on every client checked                                         |
| `+0x48`             | u32          | unknown_48            | `500000` on every client checked; see Open Questions                |
| `+0x4C`             | String Table | string_table          | See String Table                                                    |
| `string_table+0x00` | u32          | table_start           | Offset of the string table; `0x4C`                                  |
| `string_table+0x04` | u32          | zero                  | Always `0`                                                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 3

No `barter_reset_time`.

### File Layout

| Offset              | Type         | Field                 | Notes                              |
| ------------------- | ------------ | --------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                 | ASCII `PABR`                       |
| `+0x04`             | u32          | food_consume          |                                    |
| `+0x08`             | u32          | explore_cool_time     |                                    |
| `+0x0C`             | f32          | ship_management_range |                                    |
| `+0x10`             | f32          | barter_range          |                                    |
| `+0x14`             | u8           | reset_cool_time       |                                    |
| `+0x15`             | u8           | unknown_15            |                                    |
| `+0x16`             | u32          | max_exchange_count    |                                    |
| `+0x1A`             | u32          | over_max_count        |                                    |
| `+0x1E`             | u32          | max_reset_count       |                                    |
| `+0x22`             | u32          | discount_rate         |                                    |
| `+0x26`             | u32          | add_reset_count       |                                    |
| `+0x2A`             | u32          | reset_need_count      |                                    |
| `+0x2E`             | u32          | time_discount         |                                    |
| `+0x32`             | u32          | time_discount_limit   |                                    |
| `+0x36`             | u32          | sub_employee_exp      |                                    |
| `+0x3A`             | u32          | unknown_3c            |                                    |
| `+0x3E`             | u32          | sub_trade_exp         |                                    |
| `+0x42`             | u32          | unknown_44            |                                    |
| `+0x46`             | u32          | unknown_48            |                                    |
| `+0x4A`             | String Table | string_table          | See String Table                   |
| `string_table+0x00` | u32          | table_start           | Offset of the string table; `0x4A` |
| `string_table+0x04` | u32          | zero                  | Always `0`                         |

## Layout 2

No `unknown_48`.

### File Layout

| Offset              | Type         | Field                 | Notes                              |
| ------------------- | ------------ | --------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                 | ASCII `PABR`                       |
| `+0x04`             | u32          | food_consume          |                                    |
| `+0x08`             | u32          | explore_cool_time     |                                    |
| `+0x0C`             | f32          | ship_management_range |                                    |
| `+0x10`             | f32          | barter_range          |                                    |
| `+0x14`             | u8           | reset_cool_time       |                                    |
| `+0x15`             | u8           | unknown_15            |                                    |
| `+0x16`             | u32          | max_exchange_count    |                                    |
| `+0x1A`             | u32          | over_max_count        |                                    |
| `+0x1E`             | u32          | max_reset_count       | `3` on client 1309                 |
| `+0x22`             | u32          | discount_rate         |                                    |
| `+0x26`             | u32          | add_reset_count       | `1` on client 1309                 |
| `+0x2A`             | u32          | reset_need_count      | `1` on client 1309                 |
| `+0x2E`             | u32          | time_discount         |                                    |
| `+0x32`             | u32          | time_discount_limit   |                                    |
| `+0x36`             | u32          | sub_employee_exp      |                                    |
| `+0x3A`             | u32          | unknown_3c            |                                    |
| `+0x3E`             | u32          | sub_trade_exp         |                                    |
| `+0x42`             | u32          | unknown_44            |                                    |
| `+0x46`             | String Table | string_table          | See String Table                   |
| `string_table+0x00` | u32          | table_start           | Offset of the string table; `0x46` |
| `string_table+0x04` | u32          | zero                  | Always `0`                         |

## Layout 1

The values end after `add_reset_count`.

### File Layout

| Offset              | Type         | Field                 | Notes                              |
| ------------------- | ------------ | --------------------- | ---------------------------------- |
| `+0x00`             | char[4]      | magic                 | ASCII `PABR`                       |
| `+0x04`             | u32          | food_consume          |                                    |
| `+0x08`             | u32          | explore_cool_time     |                                    |
| `+0x0C`             | f32          | ship_management_range |                                    |
| `+0x10`             | f32          | barter_range          |                                    |
| `+0x14`             | u8           | reset_cool_time       |                                    |
| `+0x15`             | u8           | unknown_15            |                                    |
| `+0x16`             | u32          | max_exchange_count    |                                    |
| `+0x1A`             | u32          | over_max_count        |                                    |
| `+0x1E`             | u32          | max_reset_count       |                                    |
| `+0x22`             | u32          | discount_rate         |                                    |
| `+0x26`             | u32          | add_reset_count       |                                    |
| `+0x2A`             | String Table | string_table          | See String Table                   |
| `string_table+0x00` | u32          | table_start           | Offset of the string table; `0x2A` |
| `string_table+0x04` | u32          | zero                  | Always `0`                         |

## Field Names

The `IslandExplore_Option` sheet of a private server's
`DataSheets.bexcel` on client 1784 has 24 columns and one row. The client
1784 file holds 19 values; 15 of them are sheet values, in close to sheet
order: `FoodConsume` (`100000`), `ExploreCoolTime` (`1200`),
`ShipManagementRange` (`15000`), `BarterRange` (`5000`), `ResetCoolTime`
(`4`), `MaxExchangeCount` and `OverMaxCount` (both `1000000`),
`MaxResetCount` (`100`), `DiscountRate` (`100000`), `AddResetCount`
(`50`), `ResetNeedCount` (`30`), `TimeDiscount` (`10000`),
`TimeDiscountLimit` (`50000`), `SubEmployeeExp` (`20`) and `SubTradeExp`
(`499`). `BarterResetTime` is `6` in that sheet and absent from the client
1784 file; Layout 4 adds a u16 `6` at `+0x22`, the only sheet column with
that value.

Three pairs share one value, so the sheet's column order decides:
`FoodConsume` and `DiscountRate` (`100000`), `MaxExchangeCount` and
`OverMaxCount` (`1000000`), and `BarterRange` and
`SpecialBarterInvokationCost` (`5000`), where the f32 type, the same as
`ShipManagementRange`, picks the range. That server's dump holds the
sheet's column names as UTF-16 strings in this order: `FoodConsume`, `ExploreCoolTime`,
`ShipManagementRange`, `VoyageExploreCoolTime`,
`SpecialBarterInvokationCost`, `BarterRange`, `MaxExchangeCount`,
`ResetCoolTime`, `MaxResetCount`, `OverMaxCount`, `AddResetCount`,
`BarterResetTime`, `TimeDiscount`, `ResetNeedCount`, `SubTradeExp`,
`TimeDiscountLimit`, then `KamasylveDiscount`, `SubEmployeeExp`,
`OceanPenaltyMin`, `OceanPenaltyRate` and `OceanPenaltyMax`.

The sheet's `VoyageExploreCoolTime` (`300`), `ResetBarter` (`45504`),
`SpecialBarterInvokationCost`, `ShipMoveEmployeeExp` (`1`) and the three
`OceanPenalty` columns (`1`, `1`, `500000`) have no other match in the
file.

## Notes

- Client 1286 holds Layout 1 (54 bytes), client 1309 Layout 2 (82
  bytes), clients 1316 to 2703 Layout 3 (86 bytes) and clients 2736 to
  3482 Layout 4 (88 bytes). Between them `reset_cool_time` drops from
  `4` to `2` (client 2519) and `ship_management_range` rises from `15000`
  to `20000` (client 3474).
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/greatsea_tables.py`: one
  row with every named field. It reads Layout 4 only.

## Open Questions

### The Client 1256 Record

Client 1256 holds a 42-byte file: `food_consume`, `explore_cool_time`,
`ship_management_range`, an f32 `8000`, a u8 `4`, a u8 `0` and two u32
(`100`, then `1000000`), 26 bytes of values. Which of the later fields
the last two are is open, so no layout covers that client.

### The Value After `sub_trade_exp`

`unknown_48` is `500000`, the value of two sheet columns,
`KamasylveDiscount` and `OceanPenaltyRate`, so the value alone does not
name it. The column strings put `KamasylveDiscount` next to
`SubEmployeeExp`, but the file stores `sub_trade_exp` between them.

### The Zero Fields

`unknown_15`, `unknown_3c` and `unknown_44` are `0` on every client
checked. No column of the sheet is `0`; `ShipMoveEmployeeExp`,
`OceanPenaltyMin` and `OceanPenaltyMax` are `1` there and may read `0` in
the client build.
