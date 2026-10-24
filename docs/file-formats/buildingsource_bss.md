# `buildingsource.bss` Format

## Purpose

The guild building kits placed for Node and Conquest Wars: forts, command
posts, field HQs, Indomitable Flags and wooden fence gates. Each row names
the kit by its item key and holds its build time, its work animation, and
the items, percent and time a repair of the placed building takes. The
siege buildings placed around them (Barricades, Hwachas, Flame Towers)
upgrade through [`buildingupgrade.dbss`](buildingupgrade_dbss.md).

On client 3474 the 78 rows fall into five repair groups; names are LOC type
0:

| Repair items          | `repair_time` | Rows | Kits                                                                                           |
| --------------------- | ------------- | ---- | ---------------------------------------------------------------------------------------------- |
| Polished Stone x1     | `40000`       | 39   | Square Forts, the regional Forts (Tier 1 to 5), Indomitable Flags, the `[Node]` forts          |
| Polished Stone x1     | `120000`      | 16   | Command Posts, Field HQs and Field Command Posts (Tier 1, Tier 2, Unlimited, `[Conquest]`)     |
| Usable Scantling x2   | `40000`       | 11   | Wooden Fence Gates and `[Guild] [Tier 1] Wooden Fence (Conquest War)` (`56071`)                |
| Polished Stone x1     | `60000`       | 9    | Strong Square and Sturdy Octagonal Forts, `[Conquest] Square Fort` (`56005`)                   |
| Polished Stone x1     | `3000000`     | 3    | `[Guild] Blue Battlefield Fort` (Tier 3 to 5, `761710` to `761712`)                            |

Every row on client 3474 has one repair item at `repair_percents` `10000`.
Seven keys (`56521` to `56525`, `56535`, `56537`) are `[장미 전쟁]` (War of
the Roses) kits with a Korean name only, and three (`59792`, `59793`,
`59795`) have no item in `itemenchant.dbss` and no LOC type 0 name. Client
1784 has 37 rows, all of them in client 3474. 22 take Impeccably Polished
Stone x1 at `7500` and Polished Stone x1 to x5 at `5000`, 5 (the command
posts and field HQs) Fine Black Stone Powder x1 at `7500` and Black Stone
Powder x5 at `5000`, and the other 10 one item at `5000`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | ------- | --------- |
| 1      | 1602 and later | 3483    | `buildingsource.bss` | 5,250 | 78 Row  | 67        |

| Layout | File                 | Known           | Unknown      |
| ------ | -------------------- | --------------- | ------------ |
| 1      | `buildingsource.bss` | 4,778 B (91.0%) | 472 B (9.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               |
| ------ | -------------------- |
| 3483   | Layout 1             |
| 3482   | Layout 1             |
| 3474   | Layout 1             |
| 3473   | Layout 1             |
| 3464   | Layout 1             |
| 3458   | Layout 1             |
| 3454   | Layout 1             |
| 3444   | Layout 1             |
| 3435   | Layout 1             |
| 3426   | Layout 1             |
| 3418   | Layout 1             |
| 3412   | Layout 1             |
| 3402   | Layout 1             |
| 3396   | Layout 1             |
| 3387   | Layout 1             |
| 3381   | Layout 1             |
| 3373   | Layout 1             |
| 3364   | Layout 1             |
| 3356   | Layout 1             |
| 3349   | Layout 1             |
| 3342   | Layout 1             |
| 3335   | Layout 1             |
| 3326   | Layout 1             |
| 3321   | Layout 1             |
| 3314   | Layout 1             |
| 3303   | Layout 1             |
| 3302   | Layout 1             |
| 3293   | Layout 1             |
| 3283   | Layout 1             |
| 3275   | Layout 1             |
| 3267   | Layout 1             |
| 3258   | Layout 1             |
| 3251   | Layout 1             |
| 3242   | Layout 1             |
| 3235   | Layout 1             |
| 3229   | Layout 1             |
| 3212   | Layout 1             |
| 3203   | Layout 1             |
| 3193   | Layout 1             |
| 3186   | Layout 1             |
| 3177   | Layout 1             |
| 3169   | Layout 1             |
| 3158   | Layout 1             |
| 3151   | Layout 1             |
| 3144   | Layout 1             |
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
| 1598   | No documented layout |
| 1594   | No documented layout |
| 1590   | No documented layout |
| 1587   | No documented layout |
| 1584   | No documented layout |
| 1579   | No documented layout |
| 1572   | No documented layout |
| 1565   | No documented layout |
| 1559   | No documented layout |
| 1554   | No documented layout |
| 1547   | No documented layout |
| 1537   | No documented layout |
| 1529   | No documented layout |
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
| 1256   | No documented layout |
| 1250   | No documented layout |
| 1246   | No documented layout |
| 1239   | No documented layout |
| 1230   | No documented layout |
| 1226   | No documented layout |
| 1220   | No documented layout |
| 1217   | No documented layout |
| 1211   | No documented layout |
| 1210   | No documented layout |
| 1208   | No documented layout |
| 1203   | No documented layout |
| 1197   | No documented layout |
| 1194   | No documented layout |
| 1192   | No documented layout |
| 1187   | No documented layout |
| 1183   | No documented layout |
| 1177   | No documented layout |
| 1173   | No documented layout |
| 1167   | No documented layout |
| 1164   | No documented layout |
| 1156   | No documented layout |
| 1149   | No documented layout |
| 1144   | No documented layout |
| 1137   | No documented layout |
| 1132   | No documented layout |
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
| 829    | No documented layout |
| 822    | No documented layout |
| 814    | No documented layout |
| 805    | No documented layout |
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

None. The handler names each kit and repair item through the LOC and the
item lookup index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

A `PABR` table of variable rows with an empty string table.

| Offset      | Type       | Field              | Notes                                                    |
| ----------- | ---------- | ------------------ | -------------------------------------------------------- |
| `+0x00`     | char[4]    | magic              | `PABR`                                                   |
| `+0x04`     | u32        | count              | Number of rows                                           |
| `+0x08`     | Row[count] | rows               | See Row                                                  |
| `rows+0x00` | u32        | unknown_after_rows | `0` on clients 1784 and 3474; see Open Questions         |
| `rows+0x04` | u32        | string_count       | `0`: the empty PABR string table                         |
| `rows+0x08` | u32        | table_start        | Offset of `string_count`                                 |
| `rows+0x0C` | u32        | zero               | Always `0`                                               |

### Row (variable: 51 bytes + repair lists)

| Offset                    | Type                          | Field                      | Notes                                                                      |
| ------------------------- | ----------------------------- | -------------------------- | -------------------------------------------------------------------------- |
| `+0x00`                   | u32                           | item_key                   | The kit, an item enchant key (`enchant_level << 24 \| item_id`); level `0` on every row of clients 1784 and 3474; unique |
| `+0x04`                   | u32                           | item_key_dup               | Equals `item_key` on every row of clients 1784 and 3474                    |
| `+0x08`                   | u16                           | unknown_08                 | `0` on every row of clients 1784 and 3474; see Open Questions              |
| `+0x0A`                   | u32                           | build_time                 | `50000` on every row of clients 1784 and 3474; see In-Game Checks          |
| `+0x0E`                   | u8                            | work_ani_type              | 2016 `gc::EWorkAniType`; `5` (Architecture) on every row of clients 1784 and 3474 |
| `+0x0F`                   | u64                           | repair_item_keys_count     | Number of repair items                                                     |
| `+0x17`                   | u32[repair_item_keys_count]   | repair_item_keys           | Item enchant keys, level `0` on clients 1784 and 3474                      |
| `repair_item_keys+0x00`   | u64                           | repair_item_counts_count   | Equals `repair_item_keys_count` on clients 1784 and 3474                   |
| `repair_item_keys+0x08`   | i64[repair_item_counts_count] | repair_item_counts         | How many of the repair item at the same index                              |
| `repair_item_counts+0x00` | u64                           | repair_time                | See the table in Purpose and In-Game Checks                                |
| `repair_item_counts+0x08` | u64                           | repair_percents_count      | Equals `repair_item_keys_count` on clients 1784 and 3474                   |
| `repair_item_counts+0x10` | u32[repair_percents_count]    | repair_percents            | One per repair item; see Open Questions                                    |
| `repair_percents+0x00`    | u32                           | unknown_repair_percents_00 | `0` on every row of clients 1784 and 3474; see Open Questions              |

## Work Animations

`work_ani_type` values, named after the 2016 `gc::EWorkAniType` enum, the
same enum as the `work_ani_type` of
[`itemexchangesource.bss`](itemexchangesource_bss.md#work-animations).
Every row of clients 1784 and 3474 has `5`, `eWorkAniType_Architecture`;
the enum runs from `0` Mining to `8` Breeding, and `9` is
`eWorkAniType_Count`, the value the server loader sets before it reads the
`WorkAniType` cell.

## Field Names

The names are the columns of the `BuildingSource_Table` sheet: `Index`,
`IndexType`, `WorkAniType`, `BuildTime`, `SourceItemKey00` to
`SourceItemKey04` with `ItemCount00` to `ItemCount04`, `RepairItemKey`,
`RepairItemCount`, `RepairPercent` and `RepairTime`. `Index` holds the
kit's item key, so the field is `item_key`; `RepairItemKey`,
`RepairItemCount` and `RepairPercent` are comma lists and become
`repair_item_keys`, `repair_item_counts` and `repair_percents`.

| Source                                          | Rows | Matches                                                                            |
| ----------------------------------------------- | ---- | ---------------------------------------------------------------------------------- |
| Private server `DataSheets.bexcel`, client 1784 | 37   | 37 of 37 client 1784 rows in every column; client 1784's file is byte for byte the private server's compiled `buildingsource.bss`. Client 3474 holds all 37 keys, with the same `BuildTime` and `WorkAniType` on 37 and the same `RepairTime` on 36 |
| Private server `BuildingSource_Table`, client 519 | 12 | `44294`, `56005`, `56006`, `56010`, `56011`, `56039`, `56060`, `56061`, `56070`, `56071`, `56073` and `56118`: `BuildTime`, `WorkAniType` and `RepairTime` as in the client 1784 file on all 12; one `RepairItemKey` and `RepairItemCount` per row, the last of the client 1784 lists, and no `RepairPercent` column |

On client 3474 the repair lists of the 37 shared keys differ from the
sheet: each holds one item at `10000` (see Purpose). `56775`, `[Guild]
[Tier 1] Field Command Post (Conquest War)`, has `RepairTime` `60000` in
the sheet and `120000` on client 3474. `IndexType` is `0` and every
`SourceItemKey` cell is empty in both server tables.

The server dump of the same private server on client 1784 loads the sheet
at VA `0x1409336f0` (named `Load_ServantRepair_Table` by the loader label
script, which matches three column names; the only sheet name it references
is `BuildingSource_Table`). It reads `IndexType`, then `Index` as an int:
with `IndexType` `1` it keeps the low u16 as a character key, otherwise the
u32 as an item key, and it inserts the row through a different function for
each (VA `0x140728570` and `0x140940060`). It reads `SourceItemKey%02d` and
`ItemCount%02d` for 0 to 4 into 8-byte (item key, int) pairs, `WorkAniType`
as a byte (preset `9`), `BuildTime` as an int, `RepairItemKey` and
`RepairItemCount` as comma lists into a u32 and an int64 vector,
`RepairTime` as an int into an int64, and `RepairPercent` as an int list.
The 2016 `gc::BuildingSourceStaticStatus` has `_key`
(`gc::ItemEnchantKey`), `_isBlockedBuilding` (bool), `_sourceItemKey`
(`pa_vector<std::pair<gc::ItemEnchantKey,int>>`), `_sourceItemStatic`,
`_totalPoint` (int), `_buildTime` (unsigned int), `_workAniType`
(`gc::EWorkAniType`), one `_repairItemKey`, `_repairItemCount` (`__int64`)
and `_repairTime` (unsigned `__int64`). The file stores no
`_isBlockedBuilding` and no source item list.

## Notes

- The client 3474 Lua has no reader for this table. The progress bar of
  `panel_widget_progressbar_renew.luac` shows `LUA_PROGRESSBAR_REPAIR` for
  bar type 11 while the player's action is `COMMAND_REPAIR`
  (`checkRepairKingOrLordTentAction`), and `PANEL_PROGRESSBAR_INSTALL_TENT`
  for bar type 3 while it is `BUILD_TENT`; the server sends the bar's time.
- The LOC type 0 description of `[Guild] [Tier 2] Field Command Post
  (Conquest War)` (`767208`) says the post "will be completed automatically
  after 1 hour"; its `build_time` is `50000`, as on every row.

## Open Questions

### What `unknown_08` and `unknown_after_rows` Hold

The server loader keeps `Index` as a u16 character key when `IndexType` is
`1` and inserts such a row into a second container. `unknown_08` is a u16
right after the item key, and `unknown_after_rows` is a u32 between the
rows and the string table, where a second row block would start with its
count. No row of clients 519, 1784 or 3474 has `IndexType` `1`, so both
stay `0` and neither reading can be checked. The parser rejects a non-zero
`unknown_after_rows`.

### What `unknown_repair_percents_00` Holds

The last u32 of every row is `0` on clients 1784 and 3474. The 2016 struct
has two members the file does not otherwise show, `_totalPoint` (int) and
the source item list; with no source items both would be `0`. The other
lists of the row have u64 counts, so a u32 source item count would break
the pattern.

### What `repair_percents` Measures

Client 1784 pairs Impeccably Polished Stone and Fine Black Stone Powder
with `7500`, and Polished Stone, Black Stone Powder and Usable Scantling
with `5000`; client 3474 has `10000` on every repair item. A scale of 10,000 for 100% fits, as a share of the building's
durability one repair restores per item, but no Lua or UI text reads the
value.

## In-Game Checks

### Build and Repair Time in Milliseconds

Needs item (all):

- [[Guild] Indomitable Flag](https://bdocodex.com/us/item/44294/)
- [Polished Stone](https://bdocodex.com/us/item/4068/) x1

Needs zone: a Node War or Conquest War where your guild has placed a Square
Fort

This checks whether `build_time` and `repair_time` are in milliseconds.

1. Use the Indomitable Flag at a spot where it can be installed.
2. Time the install progress bar from start to end.
3. Interact with the damaged Square Fort and pick Repair.
4. Time the Repair progress bar from start to end.

Expected result: the install bar takes about 50 seconds (`build_time`
`50000`) and the Repair bar about 40 seconds (`repair_time` `40000` for
`[Node] Square Fort` and the `[Guild] Square Fort` tiers). Bars of 50,000
and 40,000 seconds or bars that end at once mean another unit.
