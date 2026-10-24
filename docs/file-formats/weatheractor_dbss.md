# `weatheractor.dbss` Format

## Purpose

Characters tied to the weather system: weather and time-of-day actors
(45381 Cloudy Day, 45378 Night, 27093 Typhoon, 27063 Sandstorm, 49641
Christmas Snow), Margoria storms, and monsters and bosses (24517 Small Altar
Imp, 27517 Kzarka, 23085 Vell). A row is the character key, a type byte, a
block of floats and small integers, and on three rows the skill the actor
casts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ------------- | --------- |
| 2      | 1790 and later | 3483    | `weatheractor.dbss`       | 7,579 | 101 Row       | 75        |
| 2      | 1790 and later | 3483    | `weatheractoroffset.dbss` | 1,014 | 101 Index Row | 10        |
| 1      | 1529 to 1784   | 1784    | `weatheractor.dbss`       | 4,960 | 84 Row        | 59        |
| 1      | 1529 to 1784   | 1784    | `weatheractoroffset.dbss` | 844   | 84 Index Row  | 10        |

| Layout | File                      | Known            | Unknown         |
| ------ | ------------------------- | ---------------- | --------------- |
| 2      | `weatheractor.dbss`       | 4,145 B (54.7%)  | 3,434 B (45.3%) |
| 2      | `weatheractoroffset.dbss` | 1,014 B (100.0%) | 0 B (0.0%)      |
| 1      | `weatheractor.dbss`       | 3,448 B (69.5%)  | 1,512 B (30.5%) |
| 1      | `weatheractoroffset.dbss` | 844 B (100.0%)   | 0 B (0.0%)      |

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
| 2970   | Layout 2             |
| 2959   | Layout 2             |
| 2951   | Layout 2             |
| 2942   | Layout 2             |
| 2935   | Layout 2             |
| 2932   | Layout 2             |
| 2923   | Layout 2             |
| 2919   | Layout 2             |
| 2907   | Layout 2             |
| 2900   | Layout 2             |
| 2891   | Layout 2             |
| 2882   | Layout 2             |
| 2872   | Layout 2             |
| 2863   | Layout 2             |
| 2855   | Layout 2             |
| 2849   | Layout 2             |
| 2844   | Layout 2             |
| 2834   | Layout 2             |
| 2825   | Layout 2             |
| 2819   | Layout 2             |
| 2811   | Layout 2             |
| 2803   | Layout 2             |
| 2794   | Layout 2             |
| 2783   | Layout 2             |
| 2774   | Layout 2             |
| 2765   | Layout 2             |
| 2756   | Layout 2             |
| 2750   | Layout 2             |
| 2743   | Layout 2             |
| 2736   | Layout 2             |
| 2726   | Layout 2             |
| 2717   | Layout 2             |
| 2709   | Layout 2             |
| 2703   | Layout 2             |
| 2695   | Layout 2             |
| 2684   | Layout 2             |
| 2672   | Layout 2             |
| 2665   | Layout 2             |
| 2657   | Layout 2             |
| 2649   | Layout 2             |
| 2644   | Layout 2             |
| 2637   | Layout 2             |
| 2629   | Layout 2             |
| 2619   | Layout 2             |
| 2612   | Layout 2             |
| 2606   | Layout 2             |
| 2602   | Layout 2             |
| 2601   | Layout 2             |
| 2592   | Layout 2             |
| 2583   | Layout 2             |
| 2575   | Layout 2             |
| 2567   | Layout 2             |
| 2560   | Layout 2             |
| 2553   | Layout 2             |
| 2545   | Layout 2             |
| 2538   | Layout 2             |
| 2529   | Layout 2             |
| 2519   | Layout 2             |
| 2513   | Layout 2             |
| 2510   | Layout 2             |
| 2507   | Layout 2             |
| 2503   | Layout 2             |
| 2498   | Layout 2             |
| 2492   | Layout 2             |
| 2487   | Layout 2             |
| 2480   | Layout 2             |
| 2474   | Layout 2             |
| 2468   | Layout 2             |
| 2460   | Layout 2             |
| 2453   | Layout 2             |
| 2444   | Layout 2             |
| 2438   | Layout 2             |
| 2434   | Layout 2             |
| 2429   | Layout 2             |
| 2421   | Layout 2             |
| 2414   | Layout 2             |
| 2407   | Layout 2             |
| 2401   | Layout 2             |
| 2397   | Layout 2             |
| 2393   | Layout 2             |
| 2384   | Layout 2             |
| 2378   | Layout 2             |
| 2372   | Layout 2             |
| 2358   | Layout 2             |
| 2352   | Layout 2             |
| 2347   | Layout 2             |
| 2343   | Layout 2             |
| 2335   | Layout 2             |
| 2327   | Layout 2             |
| 2324   | Layout 2             |
| 2319   | Layout 2             |
| 2313   | Layout 2             |
| 2308   | Layout 2             |
| 2302   | Layout 2             |
| 2295   | Layout 2             |
| 2290   | Layout 2             |
| 2284   | Layout 2             |
| 2276   | Layout 2             |
| 2269   | Layout 2             |
| 2259   | Layout 2             |
| 2250   | Layout 2             |
| 2243   | Layout 2             |
| 2235   | Layout 2             |
| 2229   | Layout 2             |
| 2224   | Layout 2             |
| 2218   | Layout 2             |
| 2215   | Layout 2             |
| 2207   | Layout 2             |
| 2203   | Layout 2             |
| 2196   | Layout 2             |
| 2192   | Layout 2             |
| 2189   | Layout 2             |
| 2183   | Layout 2             |
| 2179   | Layout 2             |
| 2171   | Layout 2             |
| 2163   | Layout 2             |
| 2156   | Layout 2             |
| 2151   | Layout 2             |
| 2147   | Layout 2             |
| 2142   | Layout 2             |
| 2138   | Layout 2             |
| 2134   | Layout 2             |
| 2130   | Layout 2             |
| 2122   | Layout 2             |
| 2107   | Layout 2             |
| 2098   | Layout 2             |
| 2089   | Layout 2             |
| 2081   | Layout 2             |
| 2073   | Layout 2             |
| 2067   | Layout 2             |
| 2063   | Layout 2             |
| 2059   | Layout 2             |
| 2052   | Layout 2             |
| 2044   | Layout 2             |
| 2039   | Layout 2             |
| 2032   | Layout 2             |
| 2025   | Layout 2             |
| 2011   | Layout 2             |
| 2005   | Layout 2             |
| 2000   | Layout 2             |
| 1996   | Layout 2             |
| 1991   | Layout 2             |
| 1985   | Layout 2             |
| 1980   | Layout 2             |
| 1969   | Layout 2             |
| 1964   | Layout 2             |
| 1958   | Layout 2             |
| 1950   | Layout 2             |
| 1945   | Layout 2             |
| 1937   | Layout 2             |
| 1933   | Layout 2             |
| 1927   | Layout 2             |
| 1921   | Layout 2             |
| 1914   | Layout 2             |
| 1908   | Layout 2             |
| 1897   | Layout 2             |
| 1892   | Layout 2             |
| 1886   | Layout 2             |
| 1881   | Layout 2             |
| 1871   | Layout 2             |
| 1866   | Layout 2             |
| 1862   | Layout 2             |
| 1854   | Layout 2             |
| 1846   | Layout 2             |
| 1838   | Layout 2             |
| 1832   | Layout 2             |
| 1826   | Layout 2             |
| 1822   | Layout 2             |
| 1818   | Layout 2             |
| 1804   | Layout 2             |
| 1794   | Layout 2             |
| 1790   | Layout 2             |
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
| 1524   | No documented layout |
| 1519   | No documented layout |
| 1509   | No documented layout |
| 1506   | No documented layout |
| 1504   | No documented layout |
| 1500   | No documented layout |
| 1493   | No documented layout |
| 1489   | No documented layout |
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

None. The handler reads the rows in file order and does not need
`weatheractoroffset.dbss` (see below). Character names and titles come from
LOC type 6, else the Korean `characterstatic.dbss` ones, skill names from LOC
type 10 and skill icons from the
`SKILL_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

No `PABR` magic and no string table. A row count, then 75-byte rows; the
file ends after the last row.

| Offset  | Type           | Field     | Notes                |
| ------- | -------------- | --------- | -------------------- |
| `+0x00` | u32            | row_count | `101` on client 3464 |
| `+0x04` | Row[row_count] | rows      | See Row              |

### Row (75 bytes)

Value spreads are from client 3464.

| Offset  | Type    | Field         | Notes                                                        |
| ------- | ------- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u16     | key           | Row key; equals `character_key` on every row                 |
| `+0x02` | u8      | unknown_02    | `1` on every row                                             |
| `+0x03` | u16     | character_key | Character key, LOC type 6 names it                           |
| `+0x05` | u8      | weather_type  | `gc::EWeatherType`, see Weather Types; `3` on 93 rows          |
| `+0x06` | f32     | radius        | `4000` to `192000`; `10000` on 71 rows, `150000` on the four time-of-day actors |
| `+0x0A` | f32     | rain_amount   | `0`, `0.3`, `0.8` or `1.0`                                   |
| `+0x0E` | f32     | cloud_rate    | `0`, `0.2`, `0.3` or `1.0`                                   |
| `+0x12` | f32     | damage_max    | `10.0` on 2 rows, else `0`                                   |
| `+0x16` | f32     | damage_radius | `12000` or `120000` on 7 rows, else `0`                      |
| `+0x1A` | f32     | damage_radius_rate | `1.0` on 2 rows, else `0`                               |
| `+0x1E` | f32     | push_pull_speed | Always `0`                                                 |
| `+0x22` | u32     | skill_key     | `skill_no << 16 \| level`, the `skill.dbss` key; `0` on 98 rows |
| `+0x26` | u32     | skill_apply_rate | `5000`, `50000` or `1000000` on the skill rows, else `0`  |
| `+0x2A` | u32     | unknown_2a    | `1000000` on 23400 Erebjork, else `0`                        |
| `+0x2E` | f32     | unknown_2e    | `5.0` on 23400 Erebjork, else `0`                            |
| `+0x32` | bytes[12] | unknown_32    | All zero                                                     |
| `+0x3E` | u16     | unknown_3e    | `0` to `99`; `29` on 74 rows                                 |
| `+0x40` | f32     | unknown_40    | `0` to `23.0`; `13.0` on 75 rows                             |
| `+0x44` | u16     | unknown_44    | `99` on 89 rows; `0`, `2` or `10` on the others              |
| `+0x46` | bytes[4] | unknown_46    | All zero                                                     |
| `+0x4A` | u8      | unknown_4a    | `0` or `1` (78 rows)                                         |

The skill rows on client 3464:

| character_key            | skill_key           | Skill                     | skill_apply_rate |
| ------------------------ | ------------------- | ------------------------- | ---------------- |
| 27063 Sandstorm          | 40337 rank 1        | Debuff Sandstorm          | `1000000`  |
| 27109 Margoria Typhoon   | 40438 rank 1        | Typhoon Lightning         | `5000`     |
| 20759 Margoria Storm     | 40438 rank 1        | Typhoon Lightning         | `50000`    |

71 rows share one byte pattern (`radius` `10000`, `unknown_3e` `29`,
`unknown_40` `13.0`, `unknown_44` `99`, `unknown_4a` `1`): monsters from
24405 Red Orc to 24517 Small Altar Imp.

### `weatheractoroffset.dbss`

A row count equal to the main file's, then one index row per main row.

| Offset  | Type                 | Field     | Notes                              |
| ------- | -------------------- | --------- | ---------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main file's `row_count` |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                      |

### Index Row (10 bytes)

| Offset  | Type | Field         | Notes                                                       |
| ------- | ---- | ------------- | ----------------------------------------------------------- |
| `+0x00` | u16  | character_key | Row key, the main row's `key`                               |
| `+0x02` | u32  | offset        | Start of the row in `weatheractor.dbss` plus 2, past its key |
| `+0x06` | u32  | size          | Always `73`, the row size minus the 2-byte `key`            |

Every index row points at the main row with the same key. The index rows are
not in the main file's order (the first one points at main row 21).

## Layout 1

On client 1784 a Row was 59 bytes: between `skill_apply_rate` and
`unknown_3e` it held 4 bytes where Layout 2 holds 20 (`unknown_2a`,
`unknown_2e`, `unknown_32`), so every later field sat 16 bytes earlier. Only
the Row differs from Layout 2; the index rows' `size` is `57` on client 1784.
Field names keep Layout 2's offsets, so `unknown_3e` sits at `+0x2E` here.

### Row (59 bytes)

| Offset  | Type     | Field              | Notes                                                         |
| ------- | -------- | ------------------ | ------------------------------------------------------------- |
| `+0x00` | u16      | key                |                                                               |
| `+0x02` | u8       | unknown_02         |                                                               |
| `+0x03` | u16      | character_key      |                                                               |
| `+0x05` | u8       | weather_type       |                                                               |
| `+0x06` | f32      | radius             |                                                               |
| `+0x0A` | f32      | rain_amount        |                                                               |
| `+0x0E` | f32      | cloud_rate         |                                                               |
| `+0x12` | f32      | damage_max         |                                                               |
| `+0x16` | f32      | damage_radius      |                                                               |
| `+0x1A` | f32      | damage_radius_rate |                                                               |
| `+0x1E` | f32      | push_pull_speed    |                                                               |
| `+0x22` | u32      | skill_key          |                                                               |
| `+0x26` | u32      | skill_apply_rate   |                                                               |
| `+0x2A` | bytes[4] | unknown_old_2a     | All zero on client 1784; which Layout 2 field it became is not known |
| `+0x2E` | u16      | unknown_3e         |                                                               |
| `+0x30` | f32      | unknown_40         |                                                               |
| `+0x34` | u16      | unknown_44         |                                                               |
| `+0x36` | bytes[4] | unknown_46         |                                                               |
| `+0x3A` | u8       | unknown_4a         |                                                               |

## Notes

- `skill_key` reads as a skill key because both of its skills name the
  weather of their row: 27063 Sandstorm holds 40337 "Debuff Sandstorm" and
  the Margoria Typhoon and Storm hold 40438 "Typhoon Lightning". The level
  half is `1` on all three rows.
- The client Lua holds the weather factor enum `WEATHER_SYSTEM_FACTOR_TYPE`
  (humidity, celsius, cloud rate, rain amount, wind direction and force,
  water, oil, grass) in `global_define_cpp_enum`, but no Lua reads this
  file or names a weather actor field.

## Weather Types

`weather_type` follows `gc::EWeatherType` of the 2016 client (the debug symbols, see Field Names). No current client Lua names the values, and 3 and 4 came after 2016. Rows per value on client 3464:

| Value | Name       | Rows | Actors                                                         |
| ----- | ---------- | ---: | -------------------------------------------------------------- |
| `0`   | Cyclone    | 1    | 27006 Typhoon                                                  |
| `1`   | DesertWind | 1    | 27063 Sandstorm                                                |
| `2`   | Weather    | 5    | Typhoon, Margoria Typhoon, Margoria Storm, Christmas Snow, Blizzard of Christmas |
| `3`   | -          | 93   | Time-of-day actors (Dawn, Morning, Cloudy Day, Night), monsters and objects |
| `4`   | -          | 1    | 23400 Erebjork                                                 |

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::WeatherActorStaticStatus` lists `_key`, `_weatherApplyType`, `_weatherApplyRadius`, `_weatherRainAmount`, `_weatherCloudRate`, `_weatherDamageMax`, `_weatherDamageRadiusMax`, `_weatherDamageRadiusRate`, `_weatherPushPullSpeed`, `_weatherSkillKey` and `_weatherSkillApplyRate` in the order this row stores them from `+0x03`. The server-side `WeatherActor_Table` of a private server on client 519 holds 11 of the 101 actors (the storms, Sandstorm, Vell, Kzarka and the Margoria actors), and on all 11 its columns `Type`, `Radius`, `DamageMax`, `DamageRadius`, `DamageRadiusRate`, `SkillNo` and `SkillApplyRate` equal the fields named after them. Its `RainAmount` and `CloudRate` are the same values in millionths (`800000` for `0.8`), and `PushPullSpeed` is `0` like `push_pull_speed`.

## Open Questions

### unknown_2a and unknown_2e

`unknown_2a` (`1000000`) and `unknown_2e` (`5.0`) are set only on 23400 Erebjork, the only actor of weather type `4`. The server table has `WaveScale` and `Time` after the skill columns, but both are `0` on its 11 rows, so neither can be matched.

### unknown_3e, unknown_40 and unknown_44

`unknown_3e` (u16), `unknown_40` (f32) and `unknown_44` (u16) are set together. `unknown_44` is `99` on 89 rows; on 27517 Kzarka (`2`), 20755 Margoria Phantom Ship (`10`) and 23085 Vell (`99`) it equals `unknown_3e`, and on 10 rows both are `0`. The server's `WeatherColorTable` equals both of them on its 11 rows, so one of the two is the colour table index, but those rows cannot tell which. `unknown_40` (`13.0` on 75 rows, at most `23.0`) fits an hour of the day.
