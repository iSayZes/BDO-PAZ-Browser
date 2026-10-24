# `actionexp.dbss` Format

## Purpose

One row per class type and level with EXP amounts for action kinds: quests, gathering, processing, alchemy, fishing, horse taming, study, trade and farming on client 1784, where the client 3473 row has 8 bytes more. Every EXP byte is `0` on client 3473 and on client 1784, so the table holds the grid of class types and levels and nothing else. The 2016 client loads it into `gc::ActionExpStaticStatus` from the `ActionEXP_Table` sheet; no client Lua file names it. Companion `actionexpoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                   | Bytes   | Records                                             | Row bytes |
| ------ | -------------- | ------- | ---------------------- | ------- | --------------------------------------------------- | --------- |
| 2      | 2171 and later | 3483    | `actionexp.dbss`       | 577,128 | 6,480 Level Row, 6,480 Level Entry, 102 Class Block | 85        |
| 2      | 2171 and later | 3483    | `actionexpoffset.dbss` | 78,164  | 6,480 Offset Row, 101 Offset Block                  | 12        |
| 1      | 1346 to 2163   | 2163    | `actionexp.dbss`       | 316,308 | 3,900 Level Row, 3,900 Level Entry, 102 Class Block | 77        |
| 1      | 1346 to 2163   | 2163    | `actionexpoffset.dbss` | 47,204  | 3,900 Offset Row, 101 Offset Block                  | 12        |

| Layout | File                   | Known              | Unknown           |
| ------ | ---------------------- | ------------------ | ----------------- |
| 2      | `actionexp.dbss`       | 58,728 B (10.2%)   | 518,400 B (89.8%) |
| 2      | `actionexpoffset.dbss` | 78,164 B (100.0%)  | 0 B (0.0%)        |
| 1      | `actionexp.dbss`       | 316,308 B (100.0%) | 0 B (0.0%)        |
| 1      | `actionexpoffset.dbss` | 47,204 B (100.0%)  | 0 B (0.0%)        |

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
| 1267   | No file              |
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

| File                   | Required | Role                                               |
| ---------------------- | -------- | -------------------------------------------------- |
| `actionexpoffset.dbss` | Required | `(class type, level) -> (offset, size)` of every row |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type               | Field  | Notes                                                  |
| ------- | ------------------ | ------ | ------------------------------------------------------ |
| `+0x00` | Class Block[..end] | blocks | One block per class type, from class type 0 up; see Class Block |

The file stores no block count. On client 3473 it holds 102 blocks: 36 with 180 rows (class types 0 to 36 without 18) and 66 empty ones (class type 18 and 37 to 101), 36 x (4 + 180 x 89) + 66 x 4 = 577,128 bytes.

### Class Block (variable: 4 bytes + entries)

| Offset  | Type                     | Field       | Notes                                              |
| ------- | ------------------------ | ----------- | -------------------------------------------------- |
| `+0x00` | u32                      | level_count | Rows in this block; `180` or `0` on client 3473    |
| `+0x04` | Level Entry[level_count] | entries     | See Level Entry                                    |

### Level Entry (89 bytes)

| Offset  | Type      | Field      | Notes                                         |
| ------- | --------- | ---------- | --------------------------------------------- |
| `+0x00` | u32       | key_prefix | Equals `level` of the row after it            |
| `+0x04` | Level Row | row        | See Level Row; the offset file points here    |

### Level Row (85 bytes)

| Offset  | Type      | Field      | Notes                                                        |
| ------- | --------- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u8        | class_type | Class type, the number `getClassType()` returns; equals the block index |
| `+0x01` | u32       | level      | `1` to `level_count`, ascending inside a block               |
| `+0x05` | bytes[80] | unknown_05 | Every byte `0` on client 3473; see Open Questions            |

### `actionexpoffset.dbss`

Index into `actionexp.dbss`, with the same block shape as the main file.

| Offset  | Type                | Field  | Notes                                     |
| ------- | ------------------- | ------ | ----------------------------------------- |
| `+0x00` | Offset Block[..end] | blocks | Blocks repeated until the end of the file |

The block index is the class type; the file stores no class type field. On client 3473 it holds 101 blocks (class types 0 to 100), one fewer than the main file: 36 x (4 + 180 x 12) + 65 x 4 = 78,164 bytes.

### Offset Block (variable: 4 bytes + rows)

| Offset  | Type                    | Field       | Notes                                       |
| ------- | ----------------------- | ----------- | ------------------------------------------- |
| `+0x00` | u32                     | level_count | Equals the main file block's `level_count`  |
| `+0x04` | Offset Row[level_count] | rows        | See Offset Row                              |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                              |
| ------- | ---- | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | level       | Level of the row it points at                                      |
| `+0x04` | u32  | data_offset | Absolute byte offset of the Level Row in `actionexp.dbss`, just past its `key_prefix` |
| `+0x08` | u32  | data_size   | Always the Level Row size, `85` on client 3473                     |

The first row of class type 0 sits at `0x08`, after its block's `level_count` and the row's `key_prefix`. The parser reads the main file through these rows and checks that each row's `key_prefix`, `class_type` and `level` match the offset row's level and block.

## Layout 1

On client 1784 the Level Row holds nine i64 EXP fields (72 bytes) where Layout 2 has 80 bytes. The blocks keep their shape: 102 in the main file and 101 in `actionexpoffset.dbss`, 28 of them with 130 rows (class types 0 to 5, 7 to 12, 15 to 17 and 19 to 31), and `data_size` is `77`.

### Level Entry (81 bytes)

| Offset  | Type      | Field      | Notes                                         |
| ------- | --------- | ---------- | --------------------------------------------- |
| `+0x00` | u32       | key_prefix | Equals `level` of the row after it            |
| `+0x04` | Level Row | row        | See Level Row; the offset file points here    |

### Level Row (77 bytes)

| Offset  | Type | Field            | Notes                        |
| ------- | ---- | ---------------- | ---------------------------- |
| `+0x00` | u8   | class_type       | Equals the block index       |
| `+0x01` | u32  | level            | `1` to `130`                 |
| `+0x05` | i64  | quest_exp        | `0` on every row (client 1784) |
| `+0x0D` | i64  | collect_exp      | `0` on every row (client 1784) |
| `+0x15` | i64  | manufacture_exp  | `0` on every row (client 1784) |
| `+0x1D` | i64  | alchemy_exp      | `0` on every row (client 1784) |
| `+0x25` | i64  | fishing_exp      | `0` on every row (client 1784) |
| `+0x2D` | i64  | horse_taming_exp | `0` on every row (client 1784) |
| `+0x35` | i64  | study_exp        | `0` on every row (client 1784) |
| `+0x3D` | i64  | trade_exp        | `0` on every row (client 1784) |
| `+0x45` | i64  | farming_exp      | `0` on every row (client 1784) |

## Field Names

The 2016 `gc::ActionExpStaticStatus` (80 bytes in memory) holds `_class` (`gc::ClassType`, 1 byte), 3 bytes of alignment, `int _level` and nine `__int64` members `_questExp`, `_collectExp`, `_manufactureExp`, `_alchemytExp` (spelled so), `_fishingExp`, `_horseTamingExp`, `_studyExp`, `_tradeExp` and `_farmingExp`. The file packs these members without the alignment: 1 + 4 + 9 x 8 = 77 bytes, the client 1784 row size. The `ActionEXP_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 has the columns `Class`, `Level`, `Quest`, `Collect`, `Manufacture`, `Alchemy`, `Fishing`, `HorseTaming`, `Study`, `Trade` and `Farming` in the same order, and 3,640 rows (28 classes x 130 levels), as many as the client 1784 file.

Every EXP value is `0` in the sheet and in both client files, so the values cannot tell the slots apart; the Layout 1 names rest on the slot count and the member order. The sheet's class set differs from the client file's (it has classes 6 and 18 and lacks 7 and 15), a private server edit.

## Enum Values

### Class Type

`class_type` and the block index are class types, named by LOC type 21 (`str_id1` = class type, `str_id4` = `0`). On client 3473 the main file has rows for class types 0 to 36 except 18 (`Shai Male`), including types no character can pick: 13 and 36 (`PBM`), 14 (`Ain (No Use)`) and 22 (`Temp Maehwa`). LOC type 21 numbers class types 0 to 100, the 101 blocks of `actionexpoffset.dbss`.

## Notes

- The level range follows the life skill levels of [lifeexp](lifeexp_dbss.md): levels 1 to 130 here and 0 to 130 there on client 1784, 1 to 180 here and 0 to 180 there on client 3473.
- The main file ends with one more empty block than the offset file on both clients (102 against 101). The parser reads the main file only through the offset rows, so the extra `level_count` of `0` is never read.
- The 2016 client keeps the rows in `gc::ActionExpStaticStatusManager` as an array of 32 maps, one per class type, keyed by level. Its loader is `GameCommonParameterLoaderFromExcel::LoadActionExpStaticInformation`.
- [lifeexp](lifeexp_dbss.md) and [fitnesslevel](fitnesslevel_dbss.md) use the same block shape, but their offset rows point at the row itself; here each row has a u32 `key_prefix` before it.

## Open Questions

### Which EXP Slot Is New in the 80-Byte Payload

The Layout 2 row has 80 bytes after `level`, 8 more than the nine i64 fields of client 1784, the size of one more i64 EXP slot. Every byte is `0` on client 3473, and no newer struct or sheet than client 1784 names the columns, so neither the new slot's position nor its action kind is known. The nine old fields stay unnamed in Layout 2 until a client fills a value or a newer source lists the columns.
