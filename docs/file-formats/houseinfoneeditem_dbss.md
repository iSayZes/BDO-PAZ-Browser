# `houseinfoneeditem.dbss` Format

## Purpose

What it costs to set a node house to a use and to raise that use a level.
A row is one need item group, the `need_item_key` that
[`houseinforeceipe.dbss`](houseinforeceipe_dbss.md) rows point at, with six
level slots: slot 0 is level 0 and holds nothing, slots 1 to 5 hold the
transfer time and the items house levels 1 to 5 take. On client 3474 every
item is Silver.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records                        | Row bytes               |
| ------ | -------------- | ------- | ------------------------------ | ----- | ------------------------------ | ----------------------- |
| 1      | 1292 and later | 3483    | `houseinfoneeditem.dbss`       | 1,322 | 66 Level, 42 Need Item, 11 Row | 12 to 24, 20 on average |
| 1      | 1292 and later | 3483    | `houseinfoneeditemoffset.dbss` | 114   | 11 Index Row                   | 10                      |

| Layout | File                           | Known            | Unknown    |
| ------ | ------------------------------ | ---------------- | ---------- |
| 1      | `houseinfoneeditem.dbss`       | 1,322 B (100.0%) | 0 B (0.0%) |
| 1      | `houseinfoneeditemoffset.dbss` | 114 B (100.0%)   | 0 B (0.0%) |

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
| 1854   | Layout 1 |
| 1846   | Layout 1 |
| 1838   | Layout 1 |
| 1832   | Layout 1 |
| 1826   | Layout 1 |
| 1822   | Layout 1 |
| 1818   | Layout 1 |
| 1804   | Layout 1 |
| 1794   | Layout 1 |
| 1790   | Layout 1 |
| 1784   | Layout 1 |
| 1774   | Layout 1 |
| 1771   | Layout 1 |
| 1762   | Layout 1 |
| 1759   | Layout 1 |
| 1754   | Layout 1 |
| 1749   | Layout 1 |
| 1743   | Layout 1 |
| 1737   | Layout 1 |
| 1731   | Layout 1 |
| 1725   | Layout 1 |
| 1717   | Layout 1 |
| 1710   | Layout 1 |
| 1704   | Layout 1 |
| 1698   | Layout 1 |
| 1690   | Layout 1 |
| 1685   | Layout 1 |
| 1680   | Layout 1 |
| 1674   | Layout 1 |
| 1668   | Layout 1 |
| 1659   | Layout 1 |
| 1649   | Layout 1 |
| 1642   | Layout 1 |
| 1636   | Layout 1 |
| 1628   | Layout 1 |
| 1622   | Layout 1 |
| 1614   | Layout 1 |
| 1608   | Layout 1 |
| 1602   | Layout 1 |
| 1598   | Layout 1 |
| 1594   | Layout 1 |
| 1590   | Layout 1 |
| 1587   | Layout 1 |
| 1584   | Layout 1 |
| 1579   | Layout 1 |
| 1572   | Layout 1 |
| 1565   | Layout 1 |
| 1559   | Layout 1 |
| 1554   | Layout 1 |
| 1547   | Layout 1 |
| 1537   | Layout 1 |
| 1529   | Layout 1 |
| 1524   | Layout 1 |
| 1519   | Layout 1 |
| 1509   | Layout 1 |
| 1506   | Layout 1 |
| 1504   | Layout 1 |
| 1500   | Layout 1 |
| 1493   | Layout 1 |
| 1489   | Layout 1 |
| 1485   | Layout 1 |
| 1481   | Layout 1 |
| 1474   | Layout 1 |
| 1466   | Layout 1 |
| 1462   | Layout 1 |
| 1459   | Layout 1 |
| 1453   | Layout 1 |
| 1450   | Layout 1 |
| 1445   | Layout 1 |
| 1439   | Layout 1 |
| 1433   | Layout 1 |
| 1430   | Layout 1 |
| 1426   | Layout 1 |
| 1421   | Layout 1 |
| 1417   | Layout 1 |
| 1416   | Layout 1 |
| 1409   | Layout 1 |
| 1405   | Layout 1 |
| 1401   | Layout 1 |
| 1396   | Layout 1 |
| 1391   | Layout 1 |
| 1390   | Layout 1 |
| 1386   | Layout 1 |
| 1381   | Layout 1 |
| 1379   | Layout 1 |
| 1372   | Layout 1 |
| 1366   | Layout 1 |
| 1364   | Layout 1 |
| 1363   | Layout 1 |
| 1360   | Layout 1 |
| 1358   | Layout 1 |
| 1355   | Layout 1 |
| 1351   | Layout 1 |
| 1348   | Layout 1 |
| 1346   | Layout 1 |
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

| File                           | Required | Role                                                                                   |
| ------------------------------ | -------- | -------------------------------------------------------------------------------------- |
| `houseinfoneeditemoffset.dbss` | Optional | Index `need_item_key -> (offset, size)`, see below; the handler walks the rows in order and does not load it |
| `houseinforeceipe.dbss`        | Optional | The house uses whose `need_item_key` names each group                                  |
| `languagedata_en.loc`          | Optional | LOC type 16 house use names, LOC type 0 item names                                     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A row count, then the rows back to
back; the file ends after the last row.

| Offset  | Type           | Field     | Notes               |
| ------- | -------------- | --------- | ------------------- |
| `+0x00` | u32            | row_count | `11` on client 3474 |
| `+0x04` | Row[row_count] | rows      | See Row             |

The rows run from key 11 down to key 1 (client 3474).

### Row (variable: 2 bytes + levels)

| Offset  | Type     | Field         | Notes                                                    |
| ------- | -------- | ------------- | -------------------------------------------------------- |
| `+0x00` | u16      | need_item_key | Unique row key; `houseinforeceipe.dbss` `need_item_key` |
| `+0x02` | Level[6] | levels        | Slots 0 to 5, see Level                                  |

### Level (variable: 12 bytes + items)

| Offset  | Type                   | Field         | Notes                                                    |
| ------- | ---------------------- | ------------- | -------------------------------------------------------- |
| `+0x00` | i32                    | level         | The slot number, `0` to `5`                              |
| `+0x04` | i32                    | transfer_time | Seconds, see Transfer Time                               |
| `+0x08` | u32                    | item_count    | Number of need items                                     |
| `+0x0C` | Need Item[item_count]  | items         | See Need Item                                            |

Slot 0 holds level `0`, transfer time `0` and no items on every row of
clients 1784 and 3474, so every row is at least 74 bytes (`2 + 6 x 12`).

### Need Item (12 bytes)

| Offset  | Type | Field    | Notes                                                       |
| ------- | ---- | -------- | ----------------------------------------------------------- |
| `+0x00` | u32  | item_key | Item enchant key, see Notes; `1` (Silver, LOC type 0) on every item (client 3474) |
| `+0x04` | i64  | count    | Number of that item                                         |

No level holds more than one item on client 3474.

### `houseinfoneeditemoffset.dbss`

| Offset  | Type                 | Field     | Notes                                                    |
| ------- | -------------------- | --------- | -------------------------------------------------------- |
| `+0x00` | u32                  | row_count | Equals the main file's `row_count`; `11` on client 3474 |
| `+0x04` | Index Row[row_count] | rows      | See Index Row                                            |

Every index row points at the main row with the same key, in the main
file's order, and the rows tile the main file from `0x04` to the end with
no gap.

### Index Row (10 bytes)

| Offset  | Type | Field         | Notes                                                        |
| ------- | ---- | ------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | need_item_key | The main row's `need_item_key`                               |
| `+0x02` | u32  | offset        | Start of the row in `houseinfoneeditem.dbss`, at its `need_item_key` |
| `+0x06` | u32  | size          | Full row length, key included                                |

## Costs

The Silver each level takes (client 3474). A dash is a level with no items.
The [`houseinforeceipe.dbss`](houseinforeceipe_dbss.md#need-item-join) Need
Item Join lists the house uses of each group.

| need_item_key | Lv 1  | Lv 2      | Lv 3   | Lv 4   | Lv 5    |
| ------------- | ----- | --------- | ------ | ------ | ------- |
| 1             | 500   | 1,000     | 2,500  | 5,000  | 10,000  |
| 2             | 2,000 | 3,500     | 7,000  | 10,000 | 15,000  |
| 3             | -     | -         | -      | -      | -       |
| 4             | -     | 1,000     | 3,000  | 7,000  | 15,000  |
| 5             | 2,000 | 1,000,000 | -      | -      | -       |
| 6             | 500   | 10,000    | 30,000 | -      | -       |
| 7             | 5,000 | 25,000    | 45,000 | 70,000 | 100,000 |
| 8             | 3,000 | 6,000     | 10,000 | 15,000 | 25,000  |
| 9             | 5,000 | 15,000    | 25,000 | 35,000 | -       |
| 10            | 1,000 | 3,000     | 7,000  | 18,000 | -       |
| 11            | 1,000 | 2,500     | 5,000  | 10,000 | 20,000  |

## Transfer Time

`transfer_time` is `5` on every priced level from 2 up and `0` on level 1
and on every level with no items (client 3474). On client 1784 it is `60`
times the level (`60` to `300`), `600` on group 5 level 2, `60` on the
empty level 1 of group 4, and `0` on group 3 and on the levels past the
last one groups 5, 6, 9 and 10 price. The house window reads it with
`getTransperTime(receipeKey, fromLevel, toLevel)`, names it `needTime_sec`
and passes it to `Util.Time.timeFormatting`; at `0` it shows `--`
(`panel_new_housecontrol.lua`). So the field is seconds, and a level change
on client 3474 takes 5 seconds. That matches the live game, where a level
change takes a few seconds; on older clients it took longer, as the 1784
values show.

## Field Names

The names follow the 2016 `gc::HouseInfoNeedItemStaticStatus`: `_key`
(u16), then `pa::Array<gc::HouseInfoNeedItemLevelGroup,6> _houseInfoList`.
A `HouseInfoNeedItemLevelGroup` is `int _level`, `int _transferTime` and a
vector of `gc::ItemStaticInformation`, whose `_key` is a
`gc::ItemEnchantKey` and `_count` an `__int64`. The six-slot array is why a
row holds slot 0.

The values match the `House_Transfer_New` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `TransferKey` and `Level`:

| Field         | Column                     | Same value (client 1784) | Same value (client 3474) |
| ------------- | -------------------------- | ------------------------ | ------------------------ |
| need_item_key | `TransferKey`              | 11 of 11 keys            | 11 of 11 keys            |
| level         | `Level`                    | 55 of 55 levels          | 55 of 55 levels          |
| transfer_time | `Time`                     | 55 of 55                 | 12 of 55                 |
| items         | `Itemkey1` to `ItemCount3` | 55 of 55                 | 55 of 55                 |

The sheet has no level 0 row; slot 0 is not compiled from it. Client 3474
sets the time to `0` or `5` (see Transfer Time); the 12 levels that still
match are the ones at `0` on both clients. The sheet holds three item
columns per level and fills only the first; the file counts its items.
The `ReceipeForTown_New` sheet of the same workbook names the
`houseinforeceipe.dbss` `need_item_key` column `TransferKey`: Residence
`3`, Lodging `1`, Storage `4` and Horse Ranch `1`, as on client 3474.

## Notes

- The house window asks for the items by receipe key and level
  (`getNeedItemListCount`, `getNeedItemListItemKey`,
  `getNeedItemListItemCount` in `panel_new_housecontrol.lua`), so the client
  goes from the receipe to its `need_item_key` row. It passes each item key
  to `getItemEnchantStaticStatus`, which takes an item enchant key
  (`enchant_level << 24 | item_id`, the packing `itemenchant.dbss` uses).
- `getNeedAllItemListCount(receipeKey, fromLevel, toLevel)` and the
  `fromLevel, toLevel` pair of `getTransperTime` read a range of levels, for
  a house raised several levels at once.
- Group 9 is the one no `houseinforeceipe.dbss` row names (client 3474).
- The level 2 price of group 5 (1,000,000 Silver) is the same on clients
  1784 and 3474.
- The offset file is the same 114 bytes on clients 1784 and 3474.
