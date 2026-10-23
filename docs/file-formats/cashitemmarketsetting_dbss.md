# `cashitemmarketsetting.dbss` Format

## Purpose

The Central Market settings of Pearl Shop items: per item a base price in
silver, two percent values, and how many of the item may be registered.
One 46-byte row per item, keyed by item ID. On client 3483 the file holds
10,061 items, among them every class's copy of an outfit set
(`[Nova] All Howls' Eve Outfit Set B`, 3,565,397,750 silver), pets
(`[Pet] Prankkebi`), dyes and buff items (`Value Pack (30 Days)`,
`Blessing of Kamasylve (15 Days)`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                               | Bytes   | Records           | Row bytes |
| ------ | -------------- | ------- | ---------------------------------- | ------- | ----------------- | --------- |
| 2      | 1346 and later | 3483    | `cashitemmarketsetting.dbss`       | 462,826 | 10,061 Row        | 46        |
| 2      | 1346 and later | 3483    | `cashitemmarketsettingoffset.dbss` | 120,752 | 10,061 Offset Row | 12        |
| 1      | 1250 to 1341   | 1341    | `cashitemmarketsetting.dbss`       | 241,520 | 5,750 Row         | 42        |
| 1      | 1250 to 1341   | 1341    | `cashitemmarketsettingoffset.dbss` | 69,020  | 5,750 Offset Row  | 12        |

| Layout | File                               | Known              | Unknown          |
| ------ | ---------------------------------- | ------------------ | ---------------- |
| 2      | `cashitemmarketsetting.dbss`       | 402,460 B (87.0%)  | 60,366 B (13.0%) |
| 2      | `cashitemmarketsettingoffset.dbss` | 120,752 B (100.0%) | 0 B (0.0%)       |
| 1      | `cashitemmarketsetting.dbss`       | 207,020 B (85.7%)  | 34,500 B (14.3%) |
| 1      | `cashitemmarketsettingoffset.dbss` | 69,020 B (100.0%)  | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 2 |
| 3482   | Layout 2 |
| 3474   | Layout 2 |
| 3473   | Layout 2 |
| 3464   | Layout 2 |
| 3458   | Layout 2 |
| 3454   | Layout 2 |
| 3444   | Layout 2 |
| 3435   | Layout 2 |
| 3426   | Layout 2 |
| 3418   | Layout 2 |
| 3412   | Layout 2 |
| 3402   | Layout 2 |
| 3396   | Layout 2 |
| 3387   | Layout 2 |
| 3381   | Layout 2 |
| 3373   | Layout 2 |
| 3364   | Layout 2 |
| 3356   | Layout 2 |
| 3349   | Layout 2 |
| 3342   | Layout 2 |
| 3335   | Layout 2 |
| 3326   | Layout 2 |
| 3321   | Layout 2 |
| 3314   | Layout 2 |
| 3303   | Layout 2 |
| 3302   | Layout 2 |
| 3293   | Layout 2 |
| 3283   | Layout 2 |
| 3275   | Layout 2 |
| 3267   | Layout 2 |
| 3258   | Layout 2 |
| 3251   | Layout 2 |
| 3242   | Layout 2 |
| 3235   | Layout 2 |
| 3229   | Layout 2 |
| 3212   | Layout 2 |
| 3203   | Layout 2 |
| 3193   | Layout 2 |
| 3186   | Layout 2 |
| 3177   | Layout 2 |
| 3169   | Layout 2 |
| 3158   | Layout 2 |
| 3151   | Layout 2 |
| 3144   | Layout 2 |
| 3133   | Layout 2 |
| 3125   | Layout 2 |
| 3118   | Layout 2 |
| 3111   | Layout 2 |
| 3103   | Layout 2 |
| 3095   | Layout 2 |
| 3086   | Layout 2 |
| 3072   | Layout 2 |
| 3062   | Layout 2 |
| 3052   | Layout 2 |
| 3045   | Layout 2 |
| 3037   | Layout 2 |
| 3030   | Layout 2 |
| 3021   | Layout 2 |
| 3012   | Layout 2 |
| 3002   | Layout 2 |
| 2995   | Layout 2 |
| 2987   | Layout 2 |
| 2978   | Layout 2 |
| 2970   | Layout 2 |
| 2959   | Layout 2 |
| 2951   | Layout 2 |
| 2942   | Layout 2 |
| 2935   | Layout 2 |
| 2932   | Layout 2 |
| 2923   | Layout 2 |
| 2919   | Layout 2 |
| 2907   | Layout 2 |
| 2900   | Layout 2 |
| 2891   | Layout 2 |
| 2882   | Layout 2 |
| 2872   | Layout 2 |
| 2863   | Layout 2 |
| 2855   | Layout 2 |
| 2849   | Layout 2 |
| 2844   | Layout 2 |
| 2834   | Layout 2 |
| 2825   | Layout 2 |
| 2819   | Layout 2 |
| 2811   | Layout 2 |
| 2803   | Layout 2 |
| 2794   | Layout 2 |
| 2783   | Layout 2 |
| 2774   | Layout 2 |
| 2765   | Layout 2 |
| 2756   | Layout 2 |
| 2750   | Layout 2 |
| 2743   | Layout 2 |
| 2736   | Layout 2 |
| 2726   | Layout 2 |
| 2717   | Layout 2 |
| 2709   | Layout 2 |
| 2703   | Layout 2 |
| 2695   | Layout 2 |
| 2684   | Layout 2 |
| 2672   | Layout 2 |
| 2665   | Layout 2 |
| 2657   | Layout 2 |
| 2649   | Layout 2 |
| 2644   | Layout 2 |
| 2637   | Layout 2 |
| 2629   | Layout 2 |
| 2619   | Layout 2 |
| 2612   | Layout 2 |
| 2606   | Layout 2 |
| 2602   | Layout 2 |
| 2601   | Layout 2 |
| 2592   | Layout 2 |
| 2583   | Layout 2 |
| 2575   | Layout 2 |
| 2567   | Layout 2 |
| 2560   | Layout 2 |
| 2553   | Layout 2 |
| 2545   | Layout 2 |
| 2538   | Layout 2 |
| 2529   | Layout 2 |
| 2519   | Layout 2 |
| 2513   | Layout 2 |
| 2510   | Layout 2 |
| 2507   | Layout 2 |
| 2503   | Layout 2 |
| 2498   | Layout 2 |
| 2492   | Layout 2 |
| 2487   | Layout 2 |
| 2480   | Layout 2 |
| 2474   | Layout 2 |
| 2468   | Layout 2 |
| 2460   | Layout 2 |
| 2453   | Layout 2 |
| 2444   | Layout 2 |
| 2438   | Layout 2 |
| 2434   | Layout 2 |
| 2429   | Layout 2 |
| 2421   | Layout 2 |
| 2414   | Layout 2 |
| 2407   | Layout 2 |
| 2401   | Layout 2 |
| 2397   | Layout 2 |
| 2393   | Layout 2 |
| 2384   | Layout 2 |
| 2378   | Layout 2 |
| 2372   | Layout 2 |
| 2358   | Layout 2 |
| 2352   | Layout 2 |
| 2347   | Layout 2 |
| 2343   | Layout 2 |
| 2335   | Layout 2 |
| 2327   | Layout 2 |
| 2324   | Layout 2 |
| 2319   | Layout 2 |
| 2313   | Layout 2 |
| 2308   | Layout 2 |
| 2302   | Layout 2 |
| 2295   | Layout 2 |
| 2290   | Layout 2 |
| 2284   | Layout 2 |
| 2276   | Layout 2 |
| 2269   | Layout 2 |
| 2259   | Layout 2 |
| 2250   | Layout 2 |
| 2243   | Layout 2 |
| 2235   | Layout 2 |
| 2229   | Layout 2 |
| 2224   | Layout 2 |
| 2218   | Layout 2 |
| 2215   | Layout 2 |
| 2207   | Layout 2 |
| 2203   | Layout 2 |
| 2196   | Layout 2 |
| 2192   | Layout 2 |
| 2189   | Layout 2 |
| 2183   | Layout 2 |
| 2179   | Layout 2 |
| 2171   | Layout 2 |
| 2163   | Layout 2 |
| 2156   | Layout 2 |
| 2151   | Layout 2 |
| 2147   | Layout 2 |
| 2142   | Layout 2 |
| 2138   | Layout 2 |
| 2134   | Layout 2 |
| 2130   | Layout 2 |
| 2122   | Layout 2 |
| 2107   | Layout 2 |
| 2098   | Layout 2 |
| 2089   | Layout 2 |
| 2081   | Layout 2 |
| 2073   | Layout 2 |
| 2067   | Layout 2 |
| 2063   | Layout 2 |
| 2059   | Layout 2 |
| 2052   | Layout 2 |
| 2044   | Layout 2 |
| 2039   | Layout 2 |
| 2032   | Layout 2 |
| 2025   | Layout 2 |
| 2011   | Layout 2 |
| 2005   | Layout 2 |
| 2000   | Layout 2 |
| 1996   | Layout 2 |
| 1991   | Layout 2 |
| 1985   | Layout 2 |
| 1980   | Layout 2 |
| 1969   | Layout 2 |
| 1964   | Layout 2 |
| 1958   | Layout 2 |
| 1950   | Layout 2 |
| 1945   | Layout 2 |
| 1937   | Layout 2 |
| 1933   | Layout 2 |
| 1927   | Layout 2 |
| 1921   | Layout 2 |
| 1914   | Layout 2 |
| 1908   | Layout 2 |
| 1897   | Layout 2 |
| 1892   | Layout 2 |
| 1886   | Layout 2 |
| 1881   | Layout 2 |
| 1871   | Layout 2 |
| 1866   | Layout 2 |
| 1862   | Layout 2 |
| 1854   | Layout 2 |
| 1846   | Layout 2 |
| 1838   | Layout 2 |
| 1832   | Layout 2 |
| 1826   | Layout 2 |
| 1822   | Layout 2 |
| 1818   | Layout 2 |
| 1804   | Layout 2 |
| 1794   | Layout 2 |
| 1790   | Layout 2 |
| 1784   | Layout 2 |
| 1774   | Layout 2 |
| 1771   | Layout 2 |
| 1762   | Layout 2 |
| 1759   | Layout 2 |
| 1754   | Layout 2 |
| 1749   | Layout 2 |
| 1743   | Layout 2 |
| 1737   | Layout 2 |
| 1731   | Layout 2 |
| 1725   | Layout 2 |
| 1717   | Layout 2 |
| 1710   | Layout 2 |
| 1704   | Layout 2 |
| 1698   | Layout 2 |
| 1690   | Layout 2 |
| 1685   | Layout 2 |
| 1680   | Layout 2 |
| 1674   | Layout 2 |
| 1668   | Layout 2 |
| 1659   | Layout 2 |
| 1649   | Layout 2 |
| 1642   | Layout 2 |
| 1636   | Layout 2 |
| 1628   | Layout 2 |
| 1622   | Layout 2 |
| 1614   | Layout 2 |
| 1608   | Layout 2 |
| 1602   | Layout 2 |
| 1598   | Layout 2 |
| 1594   | Layout 2 |
| 1590   | Layout 2 |
| 1587   | Layout 2 |
| 1584   | Layout 2 |
| 1579   | Layout 2 |
| 1572   | Layout 2 |
| 1565   | Layout 2 |
| 1559   | Layout 2 |
| 1554   | Layout 2 |
| 1547   | Layout 2 |
| 1537   | Layout 2 |
| 1529   | Layout 2 |
| 1524   | Layout 2 |
| 1519   | Layout 2 |
| 1509   | Layout 2 |
| 1506   | Layout 2 |
| 1504   | Layout 2 |
| 1500   | Layout 2 |
| 1493   | Layout 2 |
| 1489   | Layout 2 |
| 1485   | Layout 2 |
| 1481   | Layout 2 |
| 1474   | Layout 2 |
| 1466   | Layout 2 |
| 1462   | Layout 2 |
| 1459   | Layout 2 |
| 1453   | Layout 2 |
| 1450   | Layout 2 |
| 1445   | Layout 2 |
| 1439   | Layout 2 |
| 1433   | Layout 2 |
| 1430   | Layout 2 |
| 1426   | Layout 2 |
| 1421   | Layout 2 |
| 1417   | Layout 2 |
| 1416   | Layout 2 |
| 1409   | Layout 2 |
| 1405   | Layout 2 |
| 1401   | Layout 2 |
| 1396   | Layout 2 |
| 1391   | Layout 2 |
| 1390   | Layout 2 |
| 1386   | Layout 2 |
| 1381   | Layout 2 |
| 1379   | Layout 2 |
| 1372   | Layout 2 |
| 1366   | Layout 2 |
| 1364   | Layout 2 |
| 1363   | Layout 2 |
| 1360   | Layout 2 |
| 1358   | Layout 2 |
| 1355   | Layout 2 |
| 1351   | Layout 2 |
| 1348   | Layout 2 |
| 1346   | Layout 2 |
| 1341   | Layout 1 |
| 1340   | Layout 1 |
| 1338   | Layout 1 |
| 1335   | Layout 1 |
| 1333   | Layout 1 |
| 1329   | Layout 1 |
| 1327   | Layout 1 |
| 1324   | Layout 1 |
| 1321   | Layout 1 |
| 1319   | Layout 1 |
| 1318   | Layout 1 |
| 1316   | Layout 1 |
| 1313   | Layout 1 |
| 1311   | Layout 1 |
| 1309   | Layout 1 |
| 1304   | Layout 1 |
| 1292   | Layout 1 |
| 1286   | Layout 1 |
| 1280   | Layout 1 |
| 1276   | Layout 1 |
| 1267   | Layout 1 |
| 1261   | Layout 1 |
| 1256   | Layout 1 |
| 1250   | Layout 1 |
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

| File                               | Required | Role                                                                           |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------ |
| `cashitemmarketsettingoffset.dbss` | Optional | `item_id -> data_offset` of every row; the parser reads the rows in file order without it |
| `languagedata_en.loc`              | Optional | Item names (LOC type 0)                                                        |

Item icons come from the `ITEM_ICON` lookup index.

All multi-byte values are little-endian.

## Layout 2

### File Layout

A `PABR` table of fixed rows with an empty string table, read by
`fixed_row_offsets()` in `_common/pabr_strings.py`.

| Offset      | Type       | Field        | Notes                                         |
| ----------- | ---------- | ------------ | --------------------------------------------- |
| `+0x00`     | char[4]    | magic        | `PABR`                                        |
| `+0x04`     | u32        | count        | Number of rows                                |
| `+0x08`     | Row[count] | rows         | See Row                                       |
| `rows+0x00` | u32        | string_count | `0`: the empty PABR string table              |
| `rows+0x04` | u32        | table_start  | End of the rows (`8 + 46 * count`)            |
| `rows+0x08` | u32        | zero         | Always `0`                                    |

### Row (46 bytes)

| Offset  | Type     | Field                                  | Notes                                                                    |
| ------- | -------- | -------------------------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u32      | item_id                                | Item ID (LOC type 0); unique, the rows are not in ID order               |
| `+0x04` | u64      | base_price_for_item_market             | Silver; 34 distinct values on client 3483, `0` only on item 45332        |
| `+0x0C` | u64      | base_price_for_item_market_dup         | Equals `base_price_for_item_market` on every row                         |
| `+0x14` | u32      | maxest_percent_for_item_market         | `150000`, `400000`, `7000000` or `0`, see Values                         |
| `+0x18` | u32      | maxest_percent_for_item_market_dup     | Equals `maxest_percent_for_item_market` on every row                     |
| `+0x1C` | u32      | minest_percent_for_item_market         | `700000`, or `0` on the rows where `maxest_percent_for_item_market` is `0` |
| `+0x20` | u32      | minest_percent_for_item_market_dup     | Equals `minest_percent_for_item_market` on every row                     |
| `+0x24` | u16      | max_register_count_for_item_market     | `1` or `0`                                                               |
| `+0x26` | u16      | max_register_count_for_item_market_dup | Equals `max_register_count_for_item_market` on every row                 |
| `+0x28` | bytes[6] | unknown_28                             | `0` on every row of clients 1784 and 3483                                |

The `_dup` copies equal their field on every row of clients 1784 and 3483;
`test_every_copy_equals_its_field` checks it on the installed client.

### `cashitemmarketsettingoffset.dbss`

The `PABR` index layout of `skilloffset.dbss`, read by
`parse_pabr_u32_offset_rows()` in `_common/pabr_offset.py`.

| Offset      | Type              | Field        | Notes                                        |
| ----------- | ----------------- | ------------ | -------------------------------------------- |
| `+0x00`     | char[4]           | magic        | `PABR`                                       |
| `+0x04`     | u32               | count        | Equals the `cashitemmarketsetting.dbss` count |
| `+0x08`     | Offset Row[count] | rows         | See Offset Row                               |
| `rows+0x00` | u32               | string_count | `0`: the empty PABR string table             |
| `rows+0x04` | u32               | table_start  | End of the rows (`8 + 12 * count`)           |
| `rows+0x08` | u32               | zero         | Always `0`                                   |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                                                   |
| ------- | ---- | ----------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u32  | item_id     | Key of the row it points at                                                             |
| `+0x04` | u32  | data_offset | Offset in `cashitemmarketsetting.dbss` of the row's `base_price_for_item_market`, 4 bytes past its `item_id` |
| `+0x08` | u32  | data_size   | Always `0`                                                                              |

The index rows are in another order than the file. On clients 1784 and
3483 every index row points 4 bytes into the row with its key, and the
rows those offsets mark tile the file from byte 8 to `table_start`
(`test_every_offset_row_points_just_past_its_rows_item_id`).

## Layout 1

Older rows store no `item_id`: the row starts with
`base_price_for_item_market`, and only the index names the item. The
index has the same layout as in Layout 2; its `data_offset` points at the
row start, which is again `base_price_for_item_market` (8, 50, 92 and so
on: client 1341 holds 5,750 rows of 42 bytes). Only the Row differs from
Layout 2.

### Row (42 bytes)

| Offset  | Type     | Field                                  | Notes |
| ------- | -------- | -------------------------------------- | ----- |
| `+0x00` | u64      | base_price_for_item_market             |       |
| `+0x08` | u64      | base_price_for_item_market_dup         |       |
| `+0x10` | u32      | maxest_percent_for_item_market         |       |
| `+0x14` | u32      | maxest_percent_for_item_market_dup     |       |
| `+0x18` | u32      | minest_percent_for_item_market         |       |
| `+0x1C` | u32      | minest_percent_for_item_market_dup     |       |
| `+0x20` | u16      | max_register_count_for_item_market     |       |
| `+0x22` | u16      | max_register_count_for_item_market_dup |       |
| `+0x24` | bytes[6] | unknown_28                             | `0` on every row of clients 1250 and 1341 |

## Values

Counts on client 3483.

| `maxest_percent_for_item_market` | `minest_percent_for_item_market` | Rows  | Items                                                                       |
| -------------------------------- | -------------------------------- | ----- | --------------------------------------------------------------------------- |
| `150000`                         | `700000`                         | 9,944 | Outfits, pets and most other items                                          |
| `7000000`                        | `700000`                         | 84    | `[Valencian Dye]` dyes, all at base price 2,801,340                         |
| `400000`                         | `700000`                         | 24    | Time-limited buffs and coupons (`Value Pack (30 Days)`, `Secret Book of Old Moon (15 Days)`) |
| `0`                              | `0`                              | 9     | Items 17481 to 17488 (Karlstein and Cavaro weapons) and 45332 (`Vell's Heart`, base price `0`) |

`max_register_count_for_item_market` is `1` on 8,554 rows and `0` on
1,507. 722 of the 1,507 rows with `0` have base price 410,500, the lowest
nonzero price in the file; the Canape outfits (`[Corsair] Canape Classic
Set`) are among them.

## Field Names

The names come from the `CashItemMarketSetting` sheet of a private
server's `DataSheets.bexcel` on client 1784. The sheet has one
`basePriceForItemMarket` and `maxRegisterCountForItemMarket` column per
service (`_3` to `_99` suffixes, plus one without a suffix) and one
`minestPercentForItemMarket` and `maxestPercentForItemMarket` column for
all; the file holds the `_12` columns. 12 is also the service code under
which the en, de, fr and sp LOC files hold the Pearl Shop product names
(LOC type 50, see `_dbss/cashproduct/text.py`). The sheet has 6,971 rows;
6,863 are in the client 1784 file, which has no other keys.

| Field                                | Sheet column                       | Match (client 1784, 6,863 keys) | Match (client 3483, 6,537 shared keys) |
| ------------------------------------ | ---------------------------------- | ------------------------------- | -------------------------------------- |
| `item_id`                            | `ItemKey`                          | 6,863 of 6,863                  | 6,537 of 6,537                         |
| `base_price_for_item_market`         | `basePriceForItemMarket_12`        | 6,863                           | 84                                     |
| `maxest_percent_for_item_market`     | `maxestPercentForItemMarket`       | 6,863                           | 6,537                                  |
| `minest_percent_for_item_market`     | `minestPercentForItemMarket`       | 6,863                           | 6,537                                  |
| `max_register_count_for_item_market` | `maxRegisterCountForItemMarket_12` | 6,863                           | 6,537                                  |

The column without a suffix matches less: `basePriceForItemMarket` 0 of
6,863 keys and `maxRegisterCountForItemMarket` 6,496 (client 1784). On
client 3483 the base price changed on all shared keys but the 84 dyes:
6,427 of them hold 4.5917 times the client 1784 price (44,700,000 became
205,250,000), the other 26 hold 2.755 to 6.6121 times it.

The `CashItemMarketSetting` table of a private server on client 519 has the
same columns (without the `_32` and `_34` services) and 4,747 rows. The
2016 PDB has no struct for the table; its `gc::ItemEnchantStaticStatus`
holds an `__int64 _basePriceForItemMarket`, the width of
`base_price_for_item_market`.

## Notes

- Every `item_id` of client 3483 has a LOC type 0 name and an item icon.
- 8,547 of the 10,061 items are the item of at least one
  [`cashproduct.dbss`](cashproduct_dbss.md) product (12,222 products,
  client 3483); the 1,514 that no product grants include items 17128,
  17200 and 17272.
- The client 1784 file holds 6,863 rows; 326 of its keys are gone from the
  client 3483 file, which adds 3,524.
- The Central Market Lua names `maxRegisterCount`
  (`panel_window_marketplace_sell.luac`) and calls
  `getMaxRegisterCountForWorldMarket()` (`panel_window_marketplace_buy.luac`),
  but no client 3482 Lua names this file or its percent and price columns.

## Open Questions

### What the Two Percent Values Do

`minest_percent_for_item_market` is `700000` and
`maxest_percent_for_item_market` mostly `150000`, which on the 1,000,000 =
100% scale of other tables would read as 70% and 15%. Whether they bound
the Central Market price of a Pearl item relative to
`base_price_for_item_market`, and on which scale, is not confirmed by the
client data.

### What a Register Count of 0 Means

`max_register_count_for_item_market` is `0` on 1,507 items (client 3483).
Whether those items cannot be registered on the Central Market at all, or
`0` means no limit, is open.

### Why Each Value Is Stored Twice

Each of the four values sits in two adjacent fields with the same value on
every row of clients 1784 and 3483. The sheet has one column per value, so
the second copy is filled by the build; what the client reads from it is
unknown.

### What unknown_28 Holds

The last 6 bytes of every row are `0` on clients 1784 and 3483. No sheet
column is left over for them.
