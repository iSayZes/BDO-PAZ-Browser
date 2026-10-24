# `itemmaingroup.bss` Format

## Purpose

Item main groups: each group lists one or more [`itemsubgroup.dbss`](itemsubgroup_dbss.md) subgroups, each with an optional condition script. [`characterfunction.dbss`](characterfunction_dbss.md) points its shop, sell, guild shop and trade fields here, so a group is the item list an NPC window shows. The plain PABR file holds the groups, then a string table of the condition scripts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes   | Records                    | Row bytes |
| ------ | -------------- | ------- | ------------------- | ------- | -------------------------- | --------- |
| 2      | 2726 and later | 3483    | `itemmaingroup.bss` | 684,909 | 19,069 Entry, 16,664 Group | 10        |
| 1      | 805 to 2717    | 2717    | `itemmaingroup.bss` | 537,650 | 15,679 Entry, 13,671 Group | 10        |

| Layout | File                | Known             | Unknown           |
| ------ | ------------------- | ----------------- | ----------------- |
| 2      | `itemmaingroup.bss` | 342,009 B (49.9%) | 342,900 B (50.1%) |
| 1      | `itemmaingroup.bss` | 269,869 B (50.2%) | 267,781 B (49.8%) |

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
| 1267   | Layout 1             |
| 1261   | Layout 1             |
| 1256   | Layout 1             |
| 1250   | Layout 1             |
| 1246   | Layout 1             |
| 1239   | Layout 1             |
| 1230   | Layout 1             |
| 1226   | Layout 1             |
| 1220   | Layout 1             |
| 1217   | Layout 1             |
| 1211   | Layout 1             |
| 1210   | Layout 1             |
| 1208   | Layout 1             |
| 1203   | Layout 1             |
| 1197   | Layout 1             |
| 1194   | Layout 1             |
| 1192   | Layout 1             |
| 1187   | Layout 1             |
| 1183   | Layout 1             |
| 1177   | Layout 1             |
| 1173   | Layout 1             |
| 1167   | Layout 1             |
| 1164   | Layout 1             |
| 1156   | Layout 1             |
| 1149   | Layout 1             |
| 1144   | Layout 1             |
| 1137   | Layout 1             |
| 1132   | Layout 1             |
| 1127   | Layout 1             |
| 1122   | Layout 1             |
| 1118   | Layout 1             |
| 1114   | Layout 1             |
| 1109   | Layout 1             |
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
| 829    | Layout 1             |
| 822    | Layout 1             |
| 814    | Layout 1             |
| 805    | Layout 1             |
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

| File                      | Required | Role                                                      |
| ------------------------- | -------- | --------------------------------------------------------- |
| `itemsubgroup.dbss`       | Required | The items of each subgroup                                |
| `itemsubgroupoffset.dbss` | Required | Index into `itemsubgroup.dbss`                            |
| `languagedata_en.loc`     | Optional | Item names, LOC type 0 at `str_id1=item_id`               |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type          | Field              | Notes                                                        |
| ------------------- | ------------- | ------------------ | ------------------------------------------------------------ |
| `+0x00`             | char[4]       | magic              | ASCII `PABR`                                                 |
| `+0x04`             | u32           | count              | Number of groups; `16,501` on client 3464                    |
| `+0x08`             | Group[count]  | groups             | Variable-size groups, back to back; see Group                |
| `groups+0x00`       | String Table  | string_table       | See String Table                                             |
| `string_table+0x00` | u32           | string_table_start | Offset of `string_count`, where the groups end               |
| `string_table+0x04` | u32           | zero               | Always `0`                                                   |

The string table has the shape `exploration.bss` and `npcsimply.bss` use (`_common/pabr_strings.py`). Every string here is wide (UTF-16LE). Walking `count` groups ends exactly at `string_table_start`, and the string table ends exactly at the trailer.

### Group (variable: 29 bytes + entries)

| Offset  | Type               | Field              | Notes                                                                      |
| ------- | ------------------ | ------------------ | -------------------------------------------------------------------------- |
| `+0x00` | u32                | group_id           | Unique; `1,309` to `65,535`, not in key order                              |
| `+0x04` | u8                 | do_select_only_one | `1` when the group hands out one of its subgroups; `0` on 11,926 groups, `1` on 4,575 (client 3464) |
| `+0x05` | bytes[8]           | unknown_05         | Always zero; the 2016 `_pickCount` (i64) slot, see Field Names             |
| `+0x0D` | i32                | refresh_start_hour | `-1`, or `0` on group 50452 only (client 3464)                             |
| `+0x11` | bytes[8]           | unknown_11         | Always zero; the 2016 `_refreshInterval` (u64) slot, see Field Names       |
| `+0x19` | u32                | entry_count        | `1` to `4`; never `0` on client 3464                                       |
| `+0x1D` | Entry[entry_count] | entries            | See Entry                                                                  |

### Entry (10 bytes)

| Offset  | Type | Field         | Notes                                                               |
| ------- | ---- | ------------- | ------------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00    | Always `0`; the 2016 `_selectRate` slot, see Field Names            |
| `+0x04` | u32  | condition_ref | Index into the string table; string `0` is empty (no condition)     |
| `+0x08` | u16  | subgroup_key  | `itemsubgroup.dbss` subgroup key; every key is in its offset index  |

On client 3464 the 16,501 groups hold 18,906 entries: 15,608 groups have one entry, 121 two, 32 three and 740 four. 15,072 of the one-entry groups list the subgroup with their own key (group 50503 lists subgroup 50503).

The conditions use the script calls of `characterfunction.dbss` conditions (`getIntimacy`, `getLevel`, `clearQuest`, `checkexplore`, `isContentsGroupOpen`), joined with `;` and alternatives split by `<or>`. On client 3464, 16,422 entries have no condition, 2,140 have the text `0`, and 118 have `checkexplore(103, 1)`, node 103 being Bahar Investment Bank.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                   |
| ------- | ------------------ | ------------ | --------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `197` on client 3464 |
| `+0x04` | pstr[string_count] | strings      | Every string here is wide (UTF-16LE)    |

## Layout 1

Client 1784 groups have 7 bytes between `group_id` and `refresh_start_hour`,
where client 3473 has `do_select_only_one` and the 8-byte `unknown_05`. All 7
are zero in every group of client 1784, so which two bytes the newer layout
added is open. Only the Group differs from Layout 2.

### Group (variable: 27 bytes + entries)

| Offset  | Type               | Field              | Notes                                                     |
| ------- | ------------------ | ------------------ | --------------------------------------------------------- |
| `+0x00` | u32                | group_id           |                                                           |
| `+0x04` | bytes[7]           | unknown_04         | Zero in all 14,305 groups (client 1784)                   |
| `+0x0B` | i32                | refresh_start_hour |                                                           |
| `+0x0F` | bytes[8]           | unknown_11         | Always zero                                               |
| `+0x17` | u32                | entry_count        |                                                           |
| `+0x1B` | Entry[entry_count] | entries            |                                                           |

## Notes

- `characterfunction.dbss` stores five group IDs per NPC: `shop_buy_group`, `shop_sell_group`, `guild_shop_buy_group`, `guild_shop_sell_group` and `trade_group`. All 884, 743, 63, 61 and 125 non-zero values on client 3464 are group IDs here; that doc names the fields.
- The trade groups are the 62 IDs from 54002 to 54146 (client 3464). Each has one entry: subgroup 54001 (item 55151, the only subgroup besides 55000 that sets the trade price fields in `itemsubgroup.dbss`) under `checkexplore(103, 1)`. Subgroup 55000 (the trade crates) is in no group.
- A group can list one subgroup more than once: group 57996 lists 57771, then 57357 three times with the condition `0`.
- Worker production reaches groups through item exchanges: in the 2016 client a `plantexchangegroup.bss` row lists item exchange keys, and each `gc::ItemExchangeSourceStaticStatus` points at two groups here, `_productItemDropKey` (the product) and `_npcWorkerDropKeyForLuck` (the luck drop). `plantexchangegroup.bss` keeps the exchange key where earlier docs read a subgroup key; see [its Field Names](plantexchangegroup_bss.md#field-names). Group IDs 44059 and 44060 (Tungrad Ruins excavation) point at subgroups 42339 and 42340 (Trace of Nature with a Rough Translucent or Rough Blue Crystal), which is why those two zones resolve here and not in `itemsubgroup.dbss`.
- On client 3464, 4 of the 893 groups with more than one entry set `do_select_only_one`; the other 4,571 are one-entry groups.

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::ItemMainGroupStaticStatus` holds `_key`, the entry list, `_doSelectOnlyOne` (bool), `_pickCount` (i64), `_refreshStartHour` (i32) and `_refreshInterval` (u64); each entry (`value_type`) holds `_selectRate` (i32), `_conditionString`, a parsed condition list and `_itemSubGroupKey` (u16). The file stores the scalars in that order between `group_id` and `entry_count`, with the list moved to the end, and the entry stores `_selectRate`, the condition string index and `_itemSubGroupKey` in that order. The server-side `ItemMainGroup_Table` of a private server on client 519 shares 6,168 group IDs with client 3464:

| Field              | `ItemMainGroup_Table` column | Matching groups                                    |
| ------------------ | ---------------------------- | -------------------------------------------------- |
| do_select_only_one | `DoSelectOnlyOne`            | 5,703 of 6,168; see below                          |
| refresh_start_hour | `RefreshStartHour`           | `-1` on both sides for every shared group but 50452, the one group set on both (server `12`, client `0`) |
| subgroup_key       | `ItemSubGroupKey0` to `3`    | 6,296 of 7,802 entries                             |

The 465 `do_select_only_one` mismatches sit in key bands: 357 groups the server has at `0` and the client at `1` (1347 to 64037), and 108 the other way, all from 46001 up (46001 to 46015 and on, 65021, 65213 to 65219). 455 of them list the same subgroups on both sides; I read them as flags changed by patches since the server data.

`unknown_05`, `unknown_11` and the entry `unknown_00` sit where the 2016 struct has `_pickCount`, `_refreshInterval` and `_selectRate`, but they keep their offsets: the client stores `0` on every group and entry, while the server sets `SelectRate0` to `1,000,000` on 10,745 of its 11,098 groups and `RefreshInterval` to `-1` on 9,274. The selection weights of a `do_select_only_one` group are not in the client file.

## Open Questions

### Condition `0`

2,140 entries carry the condition text `0` (client 3464), often on the second to fourth entry of a group that repeats one subgroup. It may be a script that never passes, which would turn the entry off, but no client code that evaluates these conditions has been found.

### `refresh_start_hour` on Group 50452

`refresh_start_hour` is `-1` on every group but 50452, a furniture list (Four-legged Dining Table and five more) where it is `0`. The server sets `RefreshStartHour` and `RefreshInterval` to `12` on the same group, so it is a list that refreshes on a timer, but the client keeps no interval (`unknown_11` is zero). What the client does with the start hour alone is open.
