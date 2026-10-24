# `employeecharactership.dbss` Format

## Purpose

Ship settings per boat character: one row per rowboat, raft, sailboat,
frigate, caravel, galleass, carrack and guild galley with its sailor limit,
the number of sailor positions, its rations, the ration and cannonball
recovery values, the cannon and ship skill bar flags and the manual cannon
fire setup. The client Lua reads it through
`ToClient_EmployeeCharacterShipStaticStatusWrapper(characterKey)`.
Companion `employeecharactershipoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes | Records       | Row bytes                |
| ------ | -------------- | ------- | ---------------------------------- | ----- | ------------- | ------------------------ |
| 2      | 1340 and later | 3483    | `employeecharactership.dbss`       | 3,348 | 38 Ship Row   | 76 to 114, 88 on average |
| 2      | 1340 and later | 3483    | `employeecharactershipoffset.dbss` | 384   | 38 Offset Row | 10                       |
| 1      | 1485 to 3133   | 3133    | `employeecharactership.dbss`       | 3,652 | 38 Ship Row   | 84 to 122, 96 on average |
| 1      | 1485 to 3133   | 3133    | `employeecharactershipoffset.dbss` | 384   | 38 Offset Row | 10                       |

| Layout | File                               | Known           | Unknown       |
| ------ | ---------------------------------- | --------------- | ------------- |
| 2      | `employeecharactership.dbss`       | 3,044 B (90.9%) | 304 B (9.1%)  |
| 2      | `employeecharactershipoffset.dbss` | 384 B (100.0%)  | 0 B (0.0%)    |
| 1      | `employeecharactership.dbss`       | 3,044 B (83.4%) | 608 B (16.6%) |
| 1      | `employeecharactershipoffset.dbss` | 384 B (100.0%)  | 0 B (0.0%)    |

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
| 1481   | Layout 2             |
| 1474   | Layout 2             |
| 1466   | Layout 2             |
| 1462   | Layout 2             |
| 1459   | Layout 2             |
| 1453   | Layout 2             |
| 1450   | Layout 2             |
| 1445   | Layout 2             |
| 1439   | Layout 2             |
| 1433   | Layout 2             |
| 1430   | Layout 2             |
| 1426   | Layout 2             |
| 1421   | Layout 2             |
| 1417   | Layout 2             |
| 1416   | Layout 2             |
| 1409   | Layout 2             |
| 1405   | Layout 2             |
| 1401   | Layout 2             |
| 1396   | Layout 2             |
| 1391   | Layout 2             |
| 1390   | Layout 2             |
| 1386   | Layout 2             |
| 1381   | Layout 2             |
| 1379   | Layout 2             |
| 1372   | Layout 2             |
| 1366   | Layout 2             |
| 1364   | Layout 2             |
| 1363   | Layout 2             |
| 1360   | Layout 2             |
| 1358   | Layout 2             |
| 1355   | Layout 2             |
| 1351   | Layout 2             |
| 1348   | Layout 2             |
| 1346   | Layout 2             |
| 1341   | Layout 2             |
| 1340   | Layout 2             |
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
| 1261   | No file              |
| 1256   | No file              |
| 1250   | No file              |
| 1246   | No file              |
| 1239   | No file              |
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

| File                                              | Required | Role                                                                 |
| ------------------------------------------------- | -------- | -------------------------------------------------------------------- |
| `employeecharactershipoffset.dbss`                | Optional | `character_key -> (data_offset, data_size)` of every row; the rows sit back to back and can be walked without it |
| [`characterstatic.dbss`](characterstatic_dbss.md) | Optional | The character a `character_key` names; the handler links each key to its row |

Ship names come from LOC type 6, `str_id1` = `character_key`, `str_id4` 0
("Epheria Caravel" for `31048`).

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type            | Field | Notes                                         |
| ------- | --------------- | ----- | --------------------------------------------- |
| `+0x00` | u32             | count | Number of rows; `38` on client 3474           |
| `+0x04` | Ship Row[count] | rows  | Back to back to the end of the file; see Ship Row |

### Ship Row (variable: 76 bytes + condition text)

| Offset    | Type  | Field                                           | Notes                                                                 |
| --------- | ----- | ----------------------------------------------- | --------------------------------------------------------------------- |
| `+0x00`   | u16   | character_key                                   | Boat character; unique per row, the index key                         |
| `+0x02`   | u32   | employee_max                                    | `0` to `150`; see Notes                                               |
| `+0x06`   | u32   | employee_spawn_count                            | `0`, `1`, `3` or `5`; see Notes                                       |
| `+0x0A`   | u32   | food_max                                        | `10000` to `3000000`                                                  |
| `+0x0E`   | u32   | ocean_ship_cannon_setup                         | `0` to `2000`; `0` on boats without cannons                            |
| `+0x12`   | f32   | ship_food_recovery                              | `0` to `5.0`; see Notes                                               |
| `+0x16`   | f32   | ship_cannon_recovery                            | `0` or `1000`; see Notes                                              |
| `+0x1A`   | f32   | damage_diagram_restoration_cost                 | Whole numbers from `100000` to `100000000`, `0` on boats without cannons |
| `+0x1E`   | u32   | unknown_1e                                      | `0` on every row; see Open Questions                                  |
| `+0x22`   | u32   | unknown_22                                      | `0` on every row; see Open Questions                                  |
| `+0x26`   | u8    | is_summon_full                                  | `0` or `1`                                                            |
| `+0x27`   | u8    | new_cannon_ship_ui                              | `0` or `1`                                                            |
| `+0x28`   | u8    | new_cannon_count                                | `0` to `18`                                                           |
| `+0x29`   | f32   | new_cannon_speed                                | Whole numbers from `10` to `17`, `0` on boats without cannons          |
| `+0x2D`   | u8    | ocean_ship_skill_ui                             | `0` or `1`                                                            |
| `+0x2E`   | u8    | manual_cannon_fire                              | `0` or `1`                                                            |
| `+0x2F`   | f32   | manual_cannon_fire_min_length                   | `0` or `3000`                                                         |
| `+0x33`   | f32   | manual_cannon_fire_max_length                   | `0`, `15000` or `20000`                                               |
| `+0x37`   | f32   | manual_cannon_fire_random_dist                  | `0` or `300`                                                          |
| `+0x3B`   | f32   | manual_cannon_fire_random_pos                   | `0` or `100`                                                          |
| `+0x3F`   | u32   | manual_cannon_fire_max_angle                    | `0` or `10`                                                           |
| `+0x43`   | u8    | manual_cannon_fire_decrease_cool_time           | `0` or `1`                                                            |
| `+0x44`   | str16 | manual_cannon_fire_decrease_cool_time_condition | Condition script, `getlifelevel(9)>80;` or empty; see Notes           |

The value ranges are from client 3474. A row with an empty condition is
76 bytes, one with `getlifelevel(9)>80;` 114 bytes. The rows are sorted
neither by key nor in index order.

### `employeecharactershipoffset.dbss`

| Offset  | Type              | Field | Notes                                       |
| ------- | ----------------- | ----- | ------------------------------------------- |
| `+0x00` | u32               | count | Equals the `employeecharactership.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row        |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                               |
| ------- | ---- | ------------- | --------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at                         |
| `+0x02` | u32  | data_offset   | Absolute offset of the row start, at `character_key` |
| `+0x06` | u32  | data_size     | Row size in bytes, key included                     |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in neither key nor file order (9048, 9032, 9096, 31048 on client
3474); on clients 1784 and 3474 every index row points at the row with its
key and covers it exactly.

## Layout 1

### Ship Row (variable: 84 bytes + condition text)

| Offset                                                 | Type  | Field                                           | Notes                                       |
| ------------------------------------------------------ | ----- | ----------------------------------------------- | ------------------------------------------- |
| `+0x00`                                                | u16   | character_key                                   | Boat character                              |
| `+0x02`                                                | u32   | employee_max                                    |                                             |
| `+0x06`                                                | u32   | employee_spawn_count                            |                                             |
| `+0x0A`                                                | u32   | food_max                                        |                                             |
| `+0x0E`                                                | u32   | ocean_ship_cannon_setup                         |                                             |
| `+0x12`                                                | f32   | ship_food_recovery                              |                                             |
| `+0x16`                                                | f32   | ship_cannon_recovery                            |                                             |
| `+0x1A`                                                | f32   | damage_diagram_restoration_cost                 |                                             |
| `+0x1E`                                                | u32   | unknown_1e                                      | `0` on every row (client 1784)              |
| `+0x22`                                                | u32   | unknown_22                                      | `0` on every row (client 1784)              |
| `+0x26`                                                | u8    | is_summon_full                                  |                                             |
| `+0x27`                                                | u8    | new_cannon_ship_ui                              |                                             |
| `+0x28`                                                | u8    | new_cannon_count                                |                                             |
| `+0x29`                                                | f32   | new_cannon_speed                                |                                             |
| `+0x2D`                                                | u8    | ocean_ship_skill_ui                             |                                             |
| `+0x2E`                                                | u8    | manual_cannon_fire                              |                                             |
| `+0x2F`                                                | f32   | manual_cannon_fire_min_length                   |                                             |
| `+0x33`                                                | f32   | manual_cannon_fire_max_length                   |                                             |
| `+0x37`                                                | f32   | manual_cannon_fire_random_dist                  |                                             |
| `+0x3B`                                                | f32   | manual_cannon_fire_random_pos                   |                                             |
| `+0x3F`                                                | u32   | manual_cannon_fire_max_angle                    |                                             |
| `+0x43`                                                | u8    | manual_cannon_fire_decrease_cool_time           |                                             |
| `+0x44`                                                | str16 | manual_cannon_fire_decrease_cool_time_condition |                                             |
| `manual_cannon_fire_decrease_cool_time_condition+0x00` | f32   | unknown_tail_00                                 | Equal to `ship_food_recovery` on every row  |
| `manual_cannon_fire_decrease_cool_time_condition+0x04` | f32   | unknown_tail_04                                 | Equal to `ship_cannon_recovery` on every row |

Every row is 8 bytes longer than in Layout 2: the two f32 after the
condition are gone on client 3474. Client 1784 has 36 rows; client 3474
adds `9124` (Improved Galley) and `31025` (Panokseon).

## Field Names

The row is the `CharacterShip_Setup` sheet of a private server's
`DataSheets.bexcel` on client 1784, matched by `CharacterKey`. All 36 sheet
keys are rows on both clients. The f32 fields hold the sheet's numbers as
floats (`DamageDiagramRestorationCost` `1000000` is `1000000.0`), and an
empty sheet cell is `0` in the file.

| Field                                           | Column                                      | Same value (client 1784) | Same value (client 3474) |
| ----------------------------------------------- | ------------------------------------------- | ------------------------ | ------------------------ |
| employee_max                                    | `EmployeeMax`                               | 29 of 36                 | 29 of 36                 |
| employee_spawn_count                            | `EmployeeSpawnCount`                        | 36 of 36                 | 36 of 36                 |
| food_max                                        | `FoodMax`                                   | 36 of 36                 | 36 of 36                 |
| ocean_ship_cannon_setup                         | `OceanShipCannonSetup`                      | 36 of 36                 | 35 of 36                 |
| ship_food_recovery                              | `ShipFoodRecovery`                          | 36 of 36                 | 35 of 36                 |
| ship_cannon_recovery                            | `ShipCannonRecovery`                        | 36 of 36                 | 36 of 36                 |
| damage_diagram_restoration_cost                 | `DamageDiagramRestorationCost`              | 36 of 36                 | 35 of 36                 |
| is_summon_full                                  | `IsSummonFull`                              | 36 of 36                 | 36 of 36                 |
| new_cannon_ship_ui                              | `NewCannonShipUI`                           | 36 of 36                 | 36 of 36                 |
| new_cannon_count                                | `NewCannonCount`                            | 36 of 36                 | 35 of 36                 |
| new_cannon_speed                                | `NewCannonSpeed`                            | 36 of 36                 | 35 of 36                 |
| ocean_ship_skill_ui                             | `OceanShipSkillUI`                          | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire                              | `ManualCannonFire`                          | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire_min_length                   | `ManualCannonFireMinLength`                 | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire_max_length                   | `ManualCannonFireMaxLength`                 | 36 of 36                 | 35 of 36                 |
| manual_cannon_fire_random_dist                  | `ManualCannonFireRandomDist`                | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire_random_pos                   | `ManualCannonFireRandomPos`                 | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire_max_angle                    | `ManualCannonFireMaxAngle`                  | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire_decrease_cool_time           | `ManualCannonFireDecreaseCoolTime`          | 36 of 36                 | 36 of 36                 |
| manual_cannon_fire_decrease_cool_time_condition | `ManualCannonFireDecreaseCoolTimeCondition` | 36 of 36                 | 36 of 36                 |

The seven `EmployeeMax` misses are the Carracks `31045`, `31054` to `31057`,
`31084` and `31085`: the bexcel holds `50` where the
`DataSheet_EmployeeDataTable.xlsx` sheet of the same private server and
the client 1784 file hold `100`. Client 3474 keeps `100` on `31045` and
raises the other six to `110`. The other client 3474 misses are all
`31020` (Epheria Galleon), retuned after client 1784: cannon setup `1800`
to `2000`, ration recovery `1.25` to `1.5`, restoration cost `100000` to
`100000000`, `12` to `8` cannons, cannon speed `16` to `10` and maximum
fire length `20000` to `15000`.

`NewCannonShipUI` and `ManualCannonFire` hold the same value on every row,
and so do `ManualCannonFireDecreaseCoolTime` and both of them on all but
one row. From `is_summon_full` on, the row keeps the sheet's column order,
which places `new_cannon_ship_ui` at `+0x27` and `manual_cannon_fire` at
`+0x2E`.

The sheet also has `ShipFoodTentRecovery` and `ShipCannonTentRecovery`,
equal to `ShipFoodRecovery` and `ShipCannonRecovery` on every row, so the
values cannot tell the two pairs apart; see Open Questions. The client Lua
names its getters `getRecoveryFoodCount()` and `getRecoveryCannonCount()`,
without the tent. `OceanShipAngle` and `OceanShipWind` are empty in every
row. `ContentsGroupKey` has no place in the row.

## Notes

- The client Lua calls these getters on the wrapper:
  `getEmployeeMaxCost()` (the sailor manager menu of the wharf shows only
  for a ship above `0`, `panel_dialog_servantlist_all_1.luac`),
  `getRecoveryFoodCount()` and `getRecoveryCannonCount()` (the repair and
  supply price is missing rations times the first plus missing cannonballs
  times the second, `panel_dialog_servantlist_all_2.luac`),
  `getIsSummonFull()`, `getOceanShipSkillUI()` (the ship skill bar for the
  captain's seat, `horsemp.luac`), `getCannonCount()` and
  `getCannonReloadSec()` (the ship upgrade window,
  `panel_window_servantupgradeinfo_1.luac`). The Lua does not show which
  field a getter reads; by name, `getEmployeeMaxCost()` is `employee_max`
  and the two recovery getters are `ship_food_recovery` and
  `ship_cannon_recovery`.
- The condition `getlifelevel(9)>80;` tests life type 9, `sail` in
  `CppEnums.LifeExperienceType` (`global_define_cpp_enum.luac`): Sailing
  level above 80. On client 3474 the 12 rows with a condition are the 12
  rows with manual cannon fire lengths.
- `employee_spawn_count` equals the number of rows per `CharacterKey` in the
  `EmployeeShipSpawnPosition_Table` sheet of the same private server (1 for
  the Epheria Sailboat, 3 for the Caravel and Galleass, 5 for the Carracks).
  The client compiles that sheet to
  [`employeeclientspawn.dbss`](employeeclientspawn_dbss.md), where 12 of
  the 13 ships with a count above `0` have that many rows on client 3474;
  the Panokseon (`31025`, count 5) has none.
- On client 3474, 15 rows hold only `food_max` and `is_summon_full`: the
  rowboats, rafts, fishing boats, the three Epheria Cogs and the Trader
  (`9096`). `is_summon_full` is `1` on all of them but the Trader, and on
  the Old Bartali Sailboat (`31015`), and `0` everywhere else.

## Open Questions

### Which Recovery Pair the Live File Keeps

Client 1784 stores four recovery values: one pair at `+0x12` and a second
pair after the condition text. The sheet has `ShipFoodRecovery`,
`ShipCannonRecovery`, `ShipFoodTentRecovery` and `ShipCannonTentRecovery`,
and on every row the tent pair equals the plain pair, in the sheet and in
both clients. Client 3474 dropped the tail pair. The names `ship_food_recovery`
and `ship_cannon_recovery` follow the sheet's column order and the Lua getter
names; a row where the sheet's two pairs differ would confirm which pair sits
where.

### unknown_1e and unknown_22

Both u32 values are `0` on every row of both clients. The sheet's
`OceanShipAngle` and `OceanShipWind` are empty in every row and would compile
to `0`, but nothing ties them to these bytes, and they could be floats.
