# `maid.dbss` Format

## Purpose

The maids and butlers a player can own: per character key the warehouse
and marketplace duties, the cooldown, the PC room flag, the head maid flags
and the list icons. Companion `maidoffset.dbss` lists where every row
sits. [`pcroommaid.bss`](pcroommaid_bss.md) lists the keys whose
`pc_room_type` is set.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes | Records                    | Row bytes                |
| ------ | -------------- | ------- | ----------------- | ----- | -------------------------- | ------------------------ |
| 2      | 1636 and later | 3483    | `maid.dbss`       | 2,566 | 27 Row, 27 Record, 15 Form | 34 to 140, 93 on average |
| 2      | 1636 and later | 3483    | `maidoffset.dbss` | 274   | 27 Offset Row              | 10                       |
| 1      | 1346 to 1590   | 1590    | `maid.dbss`       | 1,536 | 9 Form, 17 Row, 17 Record  | 32 to 138, 88 on average |
| 1      | 1346 to 1590   | 1590    | `maidoffset.dbss` | 174   | 17 Offset Row              | 10                       |

| Layout | File              | Known            | Unknown    |
| ------ | ----------------- | ---------------- | ---------- |
| 2      | `maid.dbss`       | 2,566 B (100.0%) | 0 B (0.0%) |
| 2      | `maidoffset.dbss` | 274 B (100.0%)   | 0 B (0.0%) |
| 1      | `maid.dbss`       | 1,536 B (100.0%) | 0 B (0.0%) |
| 1      | `maidoffset.dbss` | 174 B (100.0%)   | 0 B (0.0%) |

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
| 1784   | Layout 2             |
| 1774   | Layout 2             |
| 1771   | Layout 2             |
| 1762   | Layout 2             |
| 1759   | Layout 2             |
| 1754   | Layout 2             |
| 1749   | Layout 2             |
| 1743   | Layout 2             |
| 1737   | Layout 2             |
| 1731   | Layout 2             |
| 1725   | Layout 2             |
| 1717   | Layout 2             |
| 1710   | Layout 2             |
| 1704   | Layout 2             |
| 1698   | Layout 2             |
| 1690   | Layout 2             |
| 1685   | Layout 2             |
| 1680   | Layout 2             |
| 1674   | Layout 2             |
| 1668   | Layout 2             |
| 1659   | Layout 2             |
| 1649   | Layout 2             |
| 1642   | Layout 2             |
| 1636   | Layout 2             |
| 1628   | No documented layout |
| 1622   | No documented layout |
| 1614   | No documented layout |
| 1608   | No documented layout |
| 1602   | No documented layout |
| 1598   | No documented layout |
| 1594   | No documented layout |
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

| File                         | Required | Role                                                                                      |
| ---------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `maidoffset.dbss`            | Optional | `character_key -> (offset, size)` of every row; the parser walks the main file without it |
| `characterstaticoffset.dbss` | Optional | Tells which keys have a [`characterstatic.dbss`](characterstatic_dbss.md) row, for the key link |
| `languagedata_*.loc`         | Optional | Character names, LOC type 6, keyed by `character_key`                                     |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes          |
| ------- | ------------- | ------- | -------------- |
| `+0x00` | u32           | count   | Number of rows |
| `+0x04` | Record[count] | records | See Record     |

### Record (variable: 2 bytes + row)

| Offset  | Type | Field      | Notes                                                 |
| ------- | ---- | ---------- | ----------------------------------------------------- |
| `+0x00` | u16  | key_prefix | Equals the row's `character_key`                      |
| `+0x02` | Row  | row        | `maidoffset.dbss` points here, at the `character_key` |

### Row (variable: 34 bytes + forms)

| Offset        | Type             | Field                 | Notes                                                                      |
| ------------- | ---------------- | --------------------- | -------------------------------------------------------------------------- |
| `+0x00`       | u16              | character_key         | Row key; a LOC type 6 character name                                       |
| `+0x02`       | u32              | max_action_index      | `0` on every row                                                           |
| `+0x06`       | i64              | cool_time             | Milliseconds; `1200000` (20 minutes) on every row                          |
| `+0x0E`       | u8               | is_able_in_warehouse  | `1` on the warehouse maids: stores items                                   |
| `+0x0F`       | u8               | is_able_out_warehouse | `1` on the warehouse maids: takes items out                                |
| `+0x10`       | u8               | is_able_submit_market | `1` on the marketplace maids: registers items                              |
| `+0x11`       | u8               | is_able_buy_market    | `1` on the marketplace maids                                               |
| `+0x12`       | u8               | is_able_repair        | `0` on every row                                                           |
| `+0x13`       | u8               | pc_room_type          | `1` on the PC room maids, the keys of `pcroommaid.bss`                     |
| `+0x14`       | u32              | skill_0               | `0` on every row (an empty sheet cell); see Field Names                    |
| `+0x18`       | u32              | skill_1               | `0` on every row (an empty sheet cell)                                     |
| `+0x1C`       | u32              | form_count            | `0` or `1`                                                                 |
| `+0x20`       | Form[form_count] | forms                 | See Form                                                                   |
| `forms+0x00`  | u8               | is_maid_chief         | `1` on the two warehouse head maids                                        |
| `forms+0x01`  | u8               | is_maid_chief_market  | `1` on the two marketplace head maids                                      |

A row without a form is 34 bytes and one with a form 140 bytes, the size
`maidoffset.dbss` gives (client 3474: 12 of 27 rows without, 15 with).

### Form (variable: 12 bytes + icon text)

| Offset  | Type  | Field        | Notes                                                                   |
| ------- | ----- | ------------ | ----------------------------------------------------------------------- |
| `+0x00` | i32   | action_index | `0` on every form                                                       |
| `+0x04` | str16 | icon_path    | Under `ui_texture/`, with backslashes: `New_UI_Common_forLua\Window\Stable\Horse_01.dds` |

### `maidoffset.dbss`

Bare offset table into `maid.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                         |
| ------- | ----------------- | ----- | ----------------------------- |
| `+0x00` | u32               | count | Equals the `maid.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                                                       |
| ------- | ---- | ------------- | --------------------------------------------------------------------------- |
| `+0x00` | u16  | character_key | Key of the row it points at                                                 |
| `+0x02` | u32  | offset        | Absolute byte offset of the row in `maid.dbss`, at its `character_key`      |
| `+0x06` | u32  | size          | The row without its key prefix: `34` or `140` on client 3474                |

Both files list the keys in the same order, neither sorted nor grouped by
duty: on client 3474 `18977`, `18976`, `18959` down to `18951`, `18975`
down to `18960`.

## Layout 1

### Row (variable: 32 bytes + forms)

The Layout 2 row without the two head maid flags at the end.

| Offset  | Type             | Field                 | Notes                                    |
| ------- | ---------------- | --------------------- | ---------------------------------------- |
| `+0x00` | u16              | character_key         | Row key; a LOC type 6 character name     |
| `+0x02` | u32              | max_action_index      | `0` on every row                         |
| `+0x06` | i64              | cool_time             | Milliseconds; `1200000` on every row     |
| `+0x0E` | u8               | is_able_in_warehouse  | `1` on the warehouse maids               |
| `+0x0F` | u8               | is_able_out_warehouse | `1` on the warehouse maids               |
| `+0x10` | u8               | is_able_submit_market | `1` on the marketplace maids             |
| `+0x11` | u8               | is_able_buy_market    | `1` on the marketplace maids             |
| `+0x12` | u8               | is_able_repair        | `0` on every row                         |
| `+0x13` | u8               | pc_room_type          | `1` on `18964` to `18967`                |
| `+0x14` | u32              | skill_0               | `0` on every row                         |
| `+0x18` | u32              | skill_1               | `0` on every row                         |
| `+0x1C` | u32              | form_count            | `0` or `1`                               |
| `+0x20` | Form[form_count] | forms                 | See Form                                 |

## Maids and Butlers

On client 3474 every row has `cool_time` `1200000`, and each key is either
a warehouse maid (`is_able_in_warehouse` and `is_able_out_warehouse` set)
or a marketplace maid (`is_able_submit_market` and `is_able_buy_market`
set). The names are LOC type 6 (client 3474).

| character_key | Name                     | Duty        | Other flags            | Icon           |
| ------------- | ------------------------ | ----------- | ---------------------- | -------------- |
| `18951`       | Fairy Irene              | Warehouse   |                        | `Horse_01.dds` |
| `18952`       | Fairy Irene              | Marketplace |                        | `Horse_02.dds` |
| `18953`       | Fairy Risty              | Warehouse   |                        | `Horse_03.dds` |
| `18954`       | Fairy Risty              | Marketplace |                        | `Horse_04.dds` |
| `18955`       | Fairy Chiara             | Warehouse   |                        | `Horse_05.dds` |
| `18956`       | Fairy Chiara             | Marketplace |                        | `Horse_06.dds` |
| `18957`       | Sandbag                  | Warehouse   |                        | `Horse_01.dds` |
| `18958`       | Goblin Butler            | Warehouse   |                        | `Horse_06.dds` |
| `18959`       | Goblin Butler            | Marketplace |                        | `Horse_01.dds` |
| `18960`       | Ethan the Butler         | Warehouse   |                        | None           |
| `18961`       | Ethan the Butler         | Marketplace |                        | None           |
| `18962`       | Pietro the Butler        | Warehouse   |                        | None           |
| `18963`       | Pietro the Butler        | Marketplace |                        | None           |
| `18964`       | [Oasis] Fairy Chiara     | Warehouse   | `pc_room_type`         | None           |
| `18965`       | [Oasis] Fairy Chiara     | Marketplace | `pc_room_type`         | None           |
| `18966`       | [Oasis] Ethan the Butler | Warehouse   | `pc_room_type`         | None           |
| `18967`       | [Oasis] Ethan the Butler | Marketplace | `pc_room_type`         | None           |
| `18968`       | Cecilia the Maid         | Warehouse   | `is_maid_chief`        | `Horse_06.dds` |
| `18969`       | Sebastian the Butler     | Warehouse   | `is_maid_chief`        | `Horse_01.dds` |
| `18970`       | Cecilia the Maid         | Marketplace | `is_maid_chief_market` | `Horse_06.dds` |
| `18971`       | Butler Sebastian         | Marketplace | `is_maid_chief_market` | `Horse_01.dds` |
| `18972`       | No LOC name              | Warehouse   |                        | `Horse_01.dds` |
| `18973`       | No LOC name              | Marketplace |                        | `Horse_02.dds` |
| `18974`       | [Oasis] Fairy Chiara     | Warehouse   | `pc_room_type`         | None           |
| `18975`       | [Oasis] Fairy Chiara     | Marketplace | `pc_room_type`         | None           |
| `18976`       | [Oasis] Ethan the Butler | Warehouse   | `pc_room_type`         | None           |
| `18977`       | [Oasis] Ethan the Butler | Marketplace | `pc_room_type`         | None           |

Each icon sits in `New_UI_Common_forLua\Window\Stable\`, the stable
window's horse portraits; every one of them is in the client 3474 PAZ.

## Field Names

The `Maid_Table` sheet of a private server's `DataSheets.bexcel` on client
1784 has the columns `CharacterKey`, `CoolTime`, `IsAbleInWareHouse`,
`IsAbleOutWareHouse`, `IsAbleSubmitMarket`, `IsAbleBuyMarket`,
`IsAbleRepair`, `PcRoomType`, `IsMaidChief`, `IsMaidChiefMarket`,
`MaxActionIndex`, `Skill_0` and `Skill_1`, and four `IsAble*CoolTime`
columns. The `MaidFormList_Table` sheet has `CharacterKey`, `ActionIndex`
and `IconImageFile1`, one row per form. Matched by value over the 21 keys
both hold, on clients 1784 (21 of 21 rows) and 3474 (21 of 27 rows; the
sheet lacks `18972` to `18977`):

| Field                   | Column               | Rows matching |
| ----------------------- | -------------------- | ------------- |
| `character_key`         | `CharacterKey`       | 21 of 21      |
| `max_action_index`      | `MaxActionIndex`     | 21 of 21, all `0` |
| `cool_time`             | `CoolTime`           | 21 of 21      |
| `is_able_in_warehouse`  | `IsAbleInWareHouse`  | 21 of 21      |
| `is_able_out_warehouse` | `IsAbleOutWareHouse` | 21 of 21      |
| `is_able_submit_market` | `IsAbleSubmitMarket` | 21 of 21      |
| `is_able_buy_market`    | `IsAbleBuyMarket`    | 21 of 21      |
| `is_able_repair`        | `IsAbleRepair`       | 21 of 21, all `0` |
| `pc_room_type`          | `PcRoomType`         | 21 of 21      |
| `skill_0`, `skill_1`    | `Skill_0`, `Skill_1` | 21 of 21, all empty cells and `0` |
| `forms`                 | `MaidFormList_Table` | 21 of 21 (13 keys with one form, 8 with none) |
| `is_maid_chief`         | `IsMaidChief`        | 21 of 21      |
| `is_maid_chief_market`  | `IsMaidChiefMarket`  | 21 of 21      |

The client 1784 server dump has the loader of `Maid_Table` (VA
`0x140866390`). It reads `CharacterKey` with `ReadCellInt` and keeps the
low u16, then `MaxActionIndex` (`ReadColumnInt32B`), `CoolTime`
(`ReadColumnTime`, 8 bytes), the six bools `IsAbleInWareHouse` to
`PcRoomType`, `Skill_0` and `Skill_1` (a `Skill_%d` loop with
`ReadColumnInt`, the cell optional), then `IsMaidChief` and
`IsMaidChiefMarket`. The file holds the fields in that order, with the
forms between the skills and the head maid flags. `max_action_index`,
`is_able_repair`, `skill_0` and `skill_1` match only as zeros, so their
names rest on that read order. The four `IsAble*CoolTime` columns are not
read and have no bytes in the file. The `MaidFormList_Table` loader (VA
`0x140866ea0`) reads `ActionIndex` with `ReadColumnInt` and
`IconImageFile1` with `ReadColumnWString`. The 2016 client's debug symbols
have no maid type.

## Notes

- Clients 1784, 2107, 2519, 3002, 3251 and 3474 fit Layout 2; client 1485
  fits Layout 1, the 17 keys `18951` to `18967` with no head maid flags.
  Client 2107 adds `18972` and `18973`, client 2519 `18974` to `18977`.
  Clients 794 and 1230 have no `maid.dbss`; they ship a `maid.bss`
  (`gamecommondata/binary/en/maid.bss` on client 794), which has no doc.
- The private server's own compiled `maid.dbss` and `maidoffset.dbss`
  (client 1784) are the same bytes as the client files.
- `18974` to `18977` are the bytes of `18964` to `18967` with only the key
  changed, as [`pcroommaid.bss`](pcroommaid_bss.md) notes.
- The client Lua of the maid list (`panel_window_maidlist_all`) sorts each
  maid into the warehouse tab when `isAbleInWarehouse()` or
  `isAbleOutWarehouse()` is true and into the marketplace tab when
  `isAbleSubmitMarket()` is, and marks it as head maid when
  `isMaidChief()` or `isMaidChiefMarket()` is true. Its `getCoolTime()` is
  the time left on an owned maid, not this table's value. No client Lua
  reads the skills, the action index or the icon.

## Open Questions

### What the Skills and the Action Index Hold

`skill_0`, `skill_1`, `max_action_index` and every form's `action_index`
are `0` on all rows of every client checked. The client 1784 server
loader stores a set `Skill_N` cell as `(value << 16) | 1` in a 4-byte
slot, so a set skill would read as an odd u32 here; with no set cell in
any sheet row or file, neither that encoding in the client file nor what
the skill numbers point at can be confirmed.

### What the Form Icons Are For

The forms of 15 rows name a horse portrait of the stable window
(`Horse_01.dds` to `Horse_06.dds`) and 12 rows, among them all PC room
maids and the butlers Ethan and Pietro, have none. No client Lua of the
maid windows (`panel_window_maidlist_all`, `panel_widget_topicon_maid`)
reads the icon, so where the game shows it is not known.
