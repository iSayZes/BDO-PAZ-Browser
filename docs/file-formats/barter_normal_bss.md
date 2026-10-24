# `barter_normal.bss` Format

## Purpose

The barter slots of the Great Ocean barters, per barter region (the
island, port or ship of a [`barter_npclist.bss`](barter_npclist_bss.md)
row). The file holds two lists of regions: the trade item barters (the
`BarterData` sheet of client 1784) and the material barters (the
`MaterialBarterData` sheet). Every region of the first list has 40 slots
and every region of the second 41 (clients 1485 to 3474).

A slot is either an exchange of its own (the item the player hands over,
the item the player gets, their counts and the exchange limits) or a
reference to a sub group of [`bartersubgroup.bss`](bartersubgroup_bss.md)
in the same list, with its own exchange left zero. On client 3474 the two
lists hold 91 regions each, 3,640 and 3,731 slots; 511 trade item slots and
10 material slots name a sub group.

The barter windows read a region's exchanges at run time through
`ToClient_barterWrapper(RegionKey(regionKey))`
(`panel_window_barterinfosearch_2.luac`); see Open Questions.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes   | Records                                 | Row bytes |
| ------ | -------------- | ------- | ------------------- | ------- | --------------------------------------- | --------- |
| 3      | 2863 and later | 3483    | `barter_normal.bss` | 517,086 | 7,371 Exchange, 7,371 Entry, 182 Region | 56        |
| 2      | 1690 to 2855   | 2855    | `barter_normal.bss` | 440,583 | 6,561 Exchange, 6,561 Entry, 162 Region | 56        |
| 1      | 1351 to 1685   | 1685    | `barter_normal.bss` | 434,022 | 6,561 Exchange, 6,561 Entry, 162 Region | 56        |

| Layout | File                | Known              | Unknown    |
| ------ | ------------------- | ------------------ | ---------- |
| 3      | `barter_normal.bss` | 517,086 B (100.0%) | 0 B (0.0%) |
| 2      | `barter_normal.bss` | 440,583 B (100.0%) | 0 B (0.0%) |
| 1      | `barter_normal.bss` | 434,022 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 3             |
| 3482   | Layout 3             |
| 3474   | Layout 3             |
| 3473   | Layout 3             |
| 3464   | Layout 3             |
| 3458   | Layout 3             |
| 3454   | Layout 3             |
| 3444   | Layout 3             |
| 3435   | Layout 3             |
| 3426   | Layout 3             |
| 3418   | Layout 3             |
| 3412   | Layout 3             |
| 3402   | Layout 3             |
| 3396   | Layout 3             |
| 3387   | Layout 3             |
| 3381   | Layout 3             |
| 3373   | Layout 3             |
| 3364   | Layout 3             |
| 3356   | Layout 3             |
| 3349   | Layout 3             |
| 3342   | Layout 3             |
| 3335   | Layout 3             |
| 3326   | Layout 3             |
| 3321   | Layout 3             |
| 3314   | Layout 3             |
| 3303   | Layout 3             |
| 3302   | Layout 3             |
| 3293   | Layout 3             |
| 3283   | Layout 3             |
| 3275   | Layout 3             |
| 3267   | Layout 3             |
| 3258   | Layout 3             |
| 3251   | Layout 3             |
| 3242   | Layout 3             |
| 3235   | Layout 3             |
| 3229   | Layout 3             |
| 3212   | Layout 3             |
| 3203   | Layout 3             |
| 3193   | Layout 3             |
| 3186   | Layout 3             |
| 3177   | Layout 3             |
| 3169   | Layout 3             |
| 3158   | Layout 3             |
| 3151   | Layout 3             |
| 3144   | Layout 3             |
| 3133   | Layout 3             |
| 3125   | Layout 3             |
| 3118   | Layout 3             |
| 3111   | Layout 3             |
| 3103   | Layout 3             |
| 3095   | Layout 3             |
| 3086   | Layout 3             |
| 3072   | Layout 3             |
| 3062   | Layout 3             |
| 3052   | Layout 3             |
| 3045   | Layout 3             |
| 3037   | Layout 3             |
| 3030   | Layout 3             |
| 3021   | Layout 3             |
| 3012   | Layout 3             |
| 3002   | Layout 3             |
| 2995   | Layout 3             |
| 2987   | Layout 3             |
| 2978   | Layout 3             |
| 2970   | Layout 3             |
| 2959   | Layout 3             |
| 2951   | Layout 3             |
| 2942   | Layout 3             |
| 2935   | Layout 3             |
| 2932   | Layout 3             |
| 2923   | Layout 3             |
| 2919   | Layout 3             |
| 2907   | Layout 3             |
| 2900   | Layout 3             |
| 2891   | Layout 3             |
| 2882   | Layout 3             |
| 2872   | Layout 3             |
| 2863   | Layout 3             |
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

| File                 | Required | Role                                                                    |
| -------------------- | -------- | ----------------------------------------------------------------------- |
| `barter_npclist.bss` | Optional | The barter NPC of each region key                                       |
| `languagedata_*.loc` | Optional | Region names (type 17), item names (type 0) and barter category names (type 37) |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset                  | Type                          | Field                 | Notes                                                        |
| ----------------------- | ----------------------------- | --------------------- | ------------------------------------------------------------ |
| `+0x00`                 | char[4]                       | magic                 | ASCII `PABR`                                                 |
| `+0x04`                 | u32                           | region_count          | Number of `regions`; `91` on client 3474                     |
| `+0x08`                 | Region[region_count]          | regions               | The trade item barter slots                                  |
| `regions+0x00`          | u32                           | material_region_count | Number of `material_regions`; `91` on client 3474            |
| `regions+0x04`          | Region[material_region_count] | material_regions      | The material barter slots                                    |
| `material_regions+0x00` | String Table                  | string_table          | The PABR string table, present but empty                     |
| `string_table+0x00`     | u32                           | string_table_start    | Absolute offset of `string_count`, where `material_regions` ends |
| `string_table+0x04`     | u32                           | zero                  | Always `0`                                                   |

Both lists hold the 91 region keys of `barter_npclist.bss` once each
(client 3474), in neither key order nor the order of that file, and the two
lists do not share one order.

### Region (variable: 6 bytes + entries)

| Offset  | Type               | Field       | Notes                                                       |
| ------- | ------------------ | ----------- | ----------------------------------------------------------- |
| `+0x00` | u16                | region_key  | `regioninfo.bss` region key; a `barter_npclist.bss` key     |
| `+0x02` | u32                | entry_count | Number of `entries`; `40` in `regions`, `41` in `material_regions` |
| `+0x06` | Entry[entry_count] | entries     | The region's slots; see Entry                               |

### Entry (70 bytes)

The row of [`barter_special.bss`](barter_special_bss.md) has the same
layout.

| Offset  | Type     | Field             | Notes                                                       |
| ------- | -------- | ----------------- | ----------------------------------------------------------- |
| `+0x00` | u16      | barter_region_key | Equals `region_key` on every entry (client 3474)            |
| `+0x02` | u32      | select_rate       | `0` on every sub group entry; see Open Questions            |
| `+0x06` | Exchange | exchange          | All `0` on every sub group entry; see Exchange              |
| `+0x3e` | u32      | barter_sub_group  | A `bartersubgroup.bss` group key in the same list, or `0` for an exchange of the slot's own |
| `+0x42` | u32      | barter_category   | Bit mask as in `bartersubgroup.bss`; `0` on every sub group entry and every material entry (client 3474) |

### Exchange (56 bytes)

Same structure as the Exchange of
[`bartersubgroup.bss`](bartersubgroup_bss.md#exchange-56-bytes). The notes
count the entries without a sub group (client 3474).

| Offset  | Type | Field              | Notes                                                              |
| ------- | ---- | ------------------ | ------------------------------------------------------------------ |
| `+0x00` | u32  | from_item_key      | The item the player hands over, `enchant_level << 24 \| item_id`; level `0` on every entry |
| `+0x04` | u64  | from_min_count     | Fewest of `from_item_key` the exchange asks for                    |
| `+0x0c` | u64  | from_max_count     | Equals `from_min_count` on every entry                             |
| `+0x14` | u32  | to_item_key        | The item the player gets, `enchant_level << 24 \| item_id`; level `0` on every entry |
| `+0x18` | u64  | to_min_count       | Fewest of `to_item_key` the exchange gives                         |
| `+0x20` | u64  | to_max_count       | Most of `to_item_key` the exchange gives                           |
| `+0x28` | u32  | barter_need_point  | `14286` or `21650` in the trade item list, `61430` or `29430` in the material list |
| `+0x2c` | u32  | exchange_max_count | `1` to `10` in the trade item list, `1` to `3` in the material list |
| `+0x30` | u32  | exchange_min       | `0` to `1000000`                                                   |
| `+0x34` | u32  | exchange_max       | `1000000`, or `0` on 410 material entries                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 2

`barter_category` is one byte that holds the category number itself.

### Entry (67 bytes)

| Offset  | Type     | Field             | Notes                                              |
| ------- | -------- | ----------------- | -------------------------------------------------- |
| `+0x00` | u16      | barter_region_key |                                                    |
| `+0x02` | u32      | select_rate       |                                                    |
| `+0x06` | Exchange | exchange          |                                                    |
| `+0x3e` | u32      | barter_sub_group  |                                                    |
| `+0x42` | u8       | barter_category   | The category number: `1` to `7` on the trade item entries without a sub group, `8` on every sub group entry and every material entry (client 1784) |

## Layout 1

The entry ends after `barter_sub_group`: there is no `barter_category`.

### Entry (66 bytes)

| Offset  | Type     | Field             | Notes |
| ------- | -------- | ----------------- | ----- |
| `+0x00` | u16      | barter_region_key |       |
| `+0x02` | u32      | select_rate       |       |
| `+0x06` | Exchange | exchange          |       |
| `+0x3e` | u32      | barter_sub_group  |       |

## Sub Group Entries

On client 3474 the 511 trade item entries with a `barter_sub_group` name
186 of the 197 trade item sub groups, keys `1` to `197`; 9 regions hold
only such entries. The 10 material entries with one sit at slots 6 and 11
of the ship regions `995`, `997`, `999`, `1002` and `1004` and name the
material sub groups `1` to `5`, one per region. A trade item entry names a
group of the first list of `bartersubgroup.bss`, a material entry one of
the second, and every key exists there.

## Field Names

The two lists are the `BarterData` and `MaterialBarterData` sheets of a
private server's `DataSheets.bexcel` on client 1784. Each list holds the
sheet's region keys (`RegionIndex`) once, 81 on client 1784, and a region's
entries are that region's sheet rows in sheet order: matched by region and
place in the region, all 3,240 and 3,321 rows line up. The regions
themselves are in another order than the sheet's.

On the 2,958 trade item rows and 3,316 material rows without a
`BarterSubGroup`, every column matches: `RegionIndex`, `SelectRate`,
`GivedItemKey` with `GivedEnchantLevel` (one packed key), `GivedMinCount`,
`GivedMaxCount`, `TakedItemKey` with `TakedEnchantLevel`, `TakedMinCount`,
`TakedMaxCount`, `BarterNeedPoint`, `ExchangeMaxCount`, `ExchangeMin`,
`ExchangeMax`, `BarterSubGroup` and, in the trade item list,
`BarterCategory`. On the 282 and 5 rows with a `BarterSubGroup`, the
`BarterSubGroup` matches and the file holds `0` in `select_rate` and the
whole Exchange and `8` in `barter_category`, where the sheet fills the
exchange on 120 and 5 of them and leaves `BarterCategory` empty on 162. The
sheet columns `BarterCost`, `ContentsGroup`, `TradeEmployeeExp` and
`BarterTradeExp` are not in the file.

`region_key` and `barter_region_key` both hold the row's `RegionIndex`;
`barter_region_key` takes its name from `barter_npclist.bss`, whose rows
key the same regions. The Exchange field names and the `from` and `to`
naming are explained in
[`bartersubgroup.bss`](bartersubgroup_bss.md#field-names), and the category
values in [Barter Categories](bartersubgroup_bss.md#barter-categories).

## Notes

- On client 3474 the trade item entries without a sub group have one
  category bit set on 2,742 entries and two on 387 (bits 7 and 8 on 369,
  bits 6 and 8 on 18); categories `1` to `9` occur, `10` does not.
- The handler (`_bss/barter_normal/`) shows one row per entry with its
  region's name, the region's NPC from `barter_npclist.bss` and the slot,
  the entry's place in its region from `1`. A sub group entry links to the
  first entry of its group in `bartersubgroup.bss`. The Exchange is read
  with the shared barter reader in `_bss/barter/`, which also walks the two
  lists of `bartersubgroup.bss`.

## Open Questions

### Slot Selection

A region has 40 trade item slots and 41 material slots. The barter windows
read a region's exchanges only through `ToClient_barterWrapper()` and
`ToClient_barterRegionList()`, so which slots a region offers at a time,
and how a sub group entry picks one of its group's exchanges, is not in the
client data read so far. `select_rate` is the lead: `1000000` on 3,084 of the
3,129 trade item slots with an exchange of their own, other values
(`1`, `10000` to `900000`) on 45, and `0` on 1,660 of the 3,721 material
slots with one (client 3474), the same reading as the `select_rate` of
`bartersubgroup.bss` (see its Open Questions).
