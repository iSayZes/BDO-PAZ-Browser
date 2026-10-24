# `auction.dbss` Format

## Purpose

The static auction table. Each row is one auction: its number, its goods type
(guild house, villa, item, worker and so on, the client's
`CppEnums.AuctionType`), two tick counts, a Korean description and the goods
the auction offers from the start. The guild house and villa auctions list
their houses by character key with a lower price; the masterpiece auctions
(`1001` to `1003`) have room for items with a price, an exhibitor name and a
description, but hold none on client 3474. `auctionoffset.dbss` indexes the
rows by auction number.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records          | Row bytes                |
| ------ | -------------- | ------- | -------------------- | ----- | ---------------- | ------------------------ |
| 2      | 2575 and later | 3483    | `auction.dbss`       | 2,142 | 36 Row, 37 House | 10                       |
| 2      | 2575 and later | 3483    | `auctionoffset.dbss` | 380   | 36 Index Row     | 10                       |
| 1      | 1276 to 2567   | 2567    | `auction.dbss`       | 2,714 | 40 Row, 37 House | 53 to 213, 68 on average |
| 1      | 1276 to 2567   | 2567    | `auctionoffset.dbss` | 420   | 40 Index Row     | 10                       |

| Layout | File                 | Known           | Unknown       |
| ------ | -------------------- | --------------- | ------------- |
| 2      | `auction.dbss`       | 1,854 B (86.6%) | 288 B (13.4%) |
| 2      | `auctionoffset.dbss` | 380 B (100.0%)  | 0 B (0.0%)    |
| 1      | `auction.dbss`       | 2,394 B (88.2%) | 320 B (11.8%) |
| 1      | `auctionoffset.dbss` | 420 B (100.0%)  | 0 B (0.0%)    |

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

| File                         | Required | Role                                                                          |
| ---------------------------- | -------- | ----------------------------------------------------------------------------- |
| `auctionoffset.dbss`         | Optional | Maps `auction_no` to its row; the main file can be walked without it          |
| `languagedata_en.loc`        | Optional | House names (LOC type 6, keyed by `character_key`) and item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                                   |
| ------- | ---------- | ----- | ------------------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; equals the `auctionoffset.dbss` count   |
| `+0x04` | Row[count] | rows  | See Row; the rows follow each other with no gap          |

### Row (variable: 43 bytes + description, houses and items)

| Offset         | Type               | Field               | Notes                                                                 |
| -------------- | ------------------ | ------------------- | --------------------------------------------------------------------- |
| `+0x00`        | u16                | auction_no          | Unique; equals the offset-table key                                   |
| `+0x02`        | u64                | start_tick_count    | `5,184,000,000` on the house, villa and masterpiece auctions, else `0` (client 3474) |
| `+0x0A`        | u64                | interval_tick_count | `7,776,000,000` where `start_tick_count` is set, else `0` (client 3474) |
| `+0x12`        | str16              | desc_kr             | Korean description, `발렌시아 고급 빌라`; empty on 23 of the 36 rows (client 3474) |
| `desc_kr+0x00` | u8                 | auction_type        | `CppEnums.AuctionType`; see Auction Types                             |
| `desc_kr+0x01` | u32                | unknown_desc_kr_01  | `0` on every row (client 3474); see Open Questions                    |
| `desc_kr+0x05` | u32                | house_count         | Houses the auction starts with; `0` outside types `2` and `6`         |
| `desc_kr+0x09` | House[house_count] | houses              | See House                                                             |
| `houses+0x00`  | u32                | item_count          | `0` on every row (client 3474)                                        |
| `houses+0x04`  | Item[item_count]   | items               | See Item                                                              |
| `items+0x00`   | u32                | unknown_items_00    | `0` on every row (client 3474)                                        |

### House (10 bytes)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | character_key | The house's character; LOC type 6 names it, `3371` Kunid's Villa      |
| `+0x02` | i64  | lower_price   | `100,000` on every guild house, `1,000,000` on every villa (client 3474) |

### Item (variable: 32 bytes + exhibitor and description text)

On client 3474 no row holds an item. The layout comes from the three items
of auction `1001` on client 1784 (Layout 1).

| Offset                | Type  | Field                     | Notes                                                   |
| --------------------- | ----- | ------------------------- | ------------------------------------------------------- |
| `+0x00`               | u32   | item_key                  | Item ID; `320009` on client 1784                        |
| `+0x04`               | i64   | price                     | `1,000,000,000` on all three items of client 1784       |
| `+0x0C`               | str16 | exhibitor_kr              | Korean exhibitor name, `리베 루쏘` on client 1784        |
| `exhibitor_kr+0x00`   | str16 | description_kr            | Korean item description with `<PAColor>` tags and stored `\n` escapes |
| `description_kr+0x00` | u32   | unknown_description_kr_00 | `0` on all three items of client 1784                   |

### `auctionoffset.dbss`

| Offset              | Type             | Field          | Notes                                               |
| ------------------- | ---------------- | -------------- | --------------------------------------------------- |
| `+0x00`             | char[4]          | magic          | `PABR` (ASCII)                                      |
| `+0x04`             | u32              | count          | Number of index rows; equals the main file's `count` |
| `+0x08`             | Index Row[count] | records        | See Index Row                                       |
| `records+0x00`      | String Table     | string_table   | The 12-byte trailer starts here; see String Table   |
| `string_table+0x00` | u32              | end_of_records | Byte offset of the end of `records` in this file    |
| `string_table+0x04` | u32              | zero           | Always `0`                                          |

### Index Row (10 bytes)

| Offset  | Type | Field      | Notes                                                           |
| ------- | ---- | ---------- | --------------------------------------------------------------- |
| `+0x00` | u16  | auction_no | Equals the row's own `auction_no`                               |
| `+0x02` | u32  | offset     | Byte offset of the row in `auction.dbss`, at its `auction_no`   |
| `+0x06` | u32  | size       | Row byte count, from `auction_no` to the end of `unknown_items_00` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 1

On client 1784 the row holds a territory trade good between `auction_type`
and `unknown_desc_kr_01`: a territory key and its lower price, 10 bytes. The
2016 `gc::AuctionStaticStatus` has the same pair as `_territoryTrade`
(`_territoryKey`, `_lowerPrice`). Only the Row differs from Layout 2.

### Row (variable: 53 bytes + description, houses and items)

| Offset         | Type               | Field                 | Notes                                                        |
| -------------- | ------------------ | --------------------- | ------------------------------------------------------------ |
| `+0x00`        | u16                | auction_no            |                                                              |
| `+0x02`        | u64                | start_tick_count      | `5,184,000,000` on the type `5` rows too                     |
| `+0x0A`        | u64                | interval_tick_count   | `518,400,000` on the type `5` rows                           |
| `+0x12`        | str16              | desc_kr               |                                                              |
| `desc_kr+0x00` | u8                 | auction_type          |                                                              |
| `desc_kr+0x01` | i16                | territory_key         | `0` to `3` on the four type `5` rows (`109`, `119`, `129`, `139`), `-1` on the others |
| `desc_kr+0x03` | i64                | territory_lower_price | `10,000` on the type `5` rows, `0` on the others             |
| `desc_kr+0x0B` | u32                | unknown_desc_kr_01    | `0` on every row                                             |
| `desc_kr+0x0F` | u32                | house_count           |                                                              |
| `desc_kr+0x13` | House[house_count] | houses                |                                                              |
| `houses+0x00`  | u32                | item_count            | `3` on auction `1001`, `0` on the others                     |
| `houses+0x04`  | Item[item_count]   | items                 | Items `320009`, `320010` and `320011` on auction `1001`      |
| `items+0x00`   | u32                | unknown_items_00      | `0` on every row                                             |

## Auction Types

`auction_type` is `CppEnums.AuctionType` in
`luacscript/x64/include/global_define_cpp_enum.luac` on client 3474. The
2016 `gc::AuctionGoodsType` has the same values to `7`, with `5` named
`AuctionGoods_TerritoryTrade`; client 3474 renamed it `AuctionGoods_Temp`
and has no type `5` row. Rows per type on client 3474:

| Value | Name (client 3474)          | Rows | Auctions                                        |
| ----: | --------------------------- | ---: | ----------------------------------------------- |
| 0     | `AuctionGoods_Item`         | 5    | `103`, `113`, `1001` to `1003`                  |
| 1     | `AuctionGoods_WorkerNpc`    | 1    | `140`                                           |
| 2     | `AuctionGoods_House`        | 8    | `101`, `102`, `112`, `122`, `131`, `132`, `141`, `143` |
| 3     | `AuctionGoods_ServantMating` | 10  | `104`, `106`, `114`, `116`, `124`, `126`, `134`, `144`, `154`, `164` |
| 4     | `AuctionGoods_ServantMarket` | 10  | `105`, `107`, `115`, `117`, `125`, `127`, `135`, `145`, `155`, `165` |
| 5     | `AuctionGoods_Temp`         | 0    | Client 1784: `109`, `119`, `129`, `139`         |
| 6     | `AuctionGoods_Villa`        | 1    | `142`                                           |
| 7     | `AuctionGoods_Pet`          | 1    | `207`                                           |
| 8     | `AuctionGoods_ServantRent`  | 0    |                                                 |
| 9     | `AuctionGoods_ServantReturn` | 0   |                                                 |

## Field Names

The names come from two sheets of a private server's `DataSheets.bexcel` on
client 1784, and from the 2016 `gc::AuctionStaticStatus`:

| Field                 | Sheet column                                       | 2016 member          |
| --------------------- | -------------------------------------------------- | -------------------- |
| `auction_no`          | `Auction_InfoTable` `AuctionNo`                    |                      |
| `auction_type`        | `Auction_InfoTable` `AuctionType`                  | `_auctionType`       |
| `start_tick_count`    | `Auction_InfoTable` `AuctionStartCumulatedTickCount` | `_startTickCount`  |
| `interval_tick_count` | `Auction_InfoTable` `AuctionInterval`              | `_intervalTickCount` |
| `desc_kr`             | `Auction_InfoTable` `AuctionDesc`                  | `_auctionDesc`       |
| `character_key`       | `Auction_Table` `Key`                              | `_houseList[]._character` |
| `lower_price`         | `Auction_Table` `Price`                            | `_houseList[]._lowerPrice` |
| `territory_key`       | `Auction_Table` `Key`                              | `_territoryTrade._territoryKey` |
| `territory_lower_price` | `Auction_Table` `Price`                          | `_territoryTrade._lowerPrice` |
| `item_key`, `price`, `exhibitor_kr`, `description_kr` | `Auction_Table` `Key`, `Price`, `Exhibitor`, `Description` | |

`Auction_InfoTable` has 38 rows. The client 1784 file holds the same 38
auctions, and all five columns match on every row. The client 3474 file
shares 34 of them and they match there too; it drops the four type `5` rows
and adds `1002` and `1003`, the two masterpiece auctions `카쿠오의 명품관` and
`파라푸라의 명품관`.

`Auction_Table` lists the goods per `AuctionNo`. Its 37 house and villa rows
are the `houses` of both clients, in the same order and with the same price.
Its four type `5` rows are the `territory_key` and `territory_lower_price` of
client 1784. Its item rows all belong to auction `1001` and carry a
`PA_GAME_SERVICE_TYPE`; client 1784 holds three of them, items `320009` to
`320011` with the exhibitor `리베 루쏘`, and client 3474 none.

## Notes

- Rows are not sorted by `auction_no` in either file, and the two files use
  different orders. Each index row's `offset` points at its row's
  `auction_no` and `size` covers the whole row, so the index rows tile the
  main file from byte 4 to its end.
- Every house `character_key` has a LOC type 6 name on client 3474: auction
  `143` holds the four Cadry guild houses `3351` to `3354`, auction `142` the
  14 Valencia villas `3371` to `3384`.
- The masterpiece auctions are type `0` and the client shows them in
  `panel_masterpiece_auction_all`; the guild house and villa auctions use
  `panel_guildhouse_auction_all` and `panel_villa_auction`, which label the
  house price `LUA_GUILDHOUSE_AUCTION_LOWPRICE`.

## Open Questions

### Tick Count Unit

`start_tick_count` and `interval_tick_count` are `5,184,000,000` and
`7,776,000,000`, which would be 60 and 90 days in milliseconds; the client
1784 type `5` interval `518,400,000` would be 6 days. Neither the unit nor
what the client counts the start from is in the file or the auction Lua.

### Worker List Count

The 2016 `gc::AuctionStaticStatus` holds `_workerList` (character key and
lower price, like a house) before `_houseList`. `unknown_desc_kr_01` sits in
that place and is `0` on every row of both clients, so it may be the worker
list count; with no row holding a worker, its entry layout cannot be read.

### Trailing u32 Fields

`unknown_items_00` after the items and `unknown_description_kr_00` after
each item are `0` wherever they occur. Neither sheet has a column left for
them: the item rows' `PA_GAME_SERVICE_TYPE` is non-zero on every row, so the
item field is not that column.
