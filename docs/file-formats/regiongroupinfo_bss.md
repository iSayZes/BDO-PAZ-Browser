# `regiongroupinfo.bss` Format

## Purpose

Lists the region groups that map regions belong to. Every region in `regioninfo.bss` carries a `regionGroupKey` (`+104` of its record head) that joins one row here, and each row here is used by at least one region. A row names the worldmap node of the group's main town or area, a concurrent user limit, three enable flags and a display position near the node.

The region group key is the value the client reads with `getRegionGroupKey()` on a region (`panel_lobby_characterselect_all_2.luac`, where it picks the login queue of the character's region). bdo-data-extractor ([iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor), `FORMATS.md`, section 11) documents only the `regionGroupKey` join on the `regioninfo.bss` side; the layout below is my own reading of this file, with field names from the sources in Field Names.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes  | Records | Row bytes |
| ------ | -------------- | ------- | --------------------- | ------ | ------- | --------- |
| 2      | 2122 and later | 3483    | `regiongroupinfo.bss` | 12,770 | 250 Row | 51        |
| 1      | 805 to 2107    | 2107    | `regiongroupinfo.bss` | 8,595  | 175 Row | 49        |

| Layout | File                  | Known            | Unknown      |
| ------ | --------------------- | ---------------- | ------------ |
| 2      | `regiongroupinfo.bss` | 12,270 B (96.1%) | 500 B (3.9%) |
| 1      | `regiongroupinfo.bss` | 8,595 B (100.0%) | 0 B (0.0%)   |

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

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Node names (LOC type 29, keyed by `node_key`)         |

All multi-byte values are little-endian unless noted otherwise.

## Layout 2

### File Layout

| Offset              | Type              | Field              | Notes                                                          |
| ------------------- | ----------------- | ------------------ | -------------------------------------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR` (ASCII)                                                 |
| `+0x04`             | u32               | record_count       | Observed `250`                                                 |
| `+0x08`             | Row[record_count] | records            | `record_count` rows of 51 bytes, byte-packed                   |
| `records+0x00`      | String Table      | string_table       | Always empty: the PABR string table is present but empty       |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`; equals `8 + 51 × count`     |
| `string_table+0x04` | u32               | zero               | Always `0`                                                     |

The file is `8 + 51 × 250 + 12 = 12770` bytes. The parser rejects a file whose rows do not end exactly at `string_table_start`.

### Row (51 bytes)

| Offset  | Type   | Field            | Notes                                                                                              |
| ------- | ------ | ---------------- | -------------------------------------------------------------------------------------------------- |
| `+0x00` | u16    | region_group_key | Unique; joins `regionGroupKey` of `regioninfo.bss`; `0` to `302`, with gaps, not in key order      |
| `+0x02` | u8     | is_blocked_managing | Always `0`                                                                                      |
| `+0x03` | u16    | concurrent_playable_user_count | `500`, `999`, `1000`, `1300`, `2000`, `3000` (Velia) or `10000` (key 0), see below |
| `+0x05` | u32    | node_key         | Worldmap node (`exploration.bss` key, LOC type 29); `0` on 19 rows                                 |
| `+0x09` | u8     | enable_corp_productivity | `0` on 20 rows, nearly all without a node or position                                      |
| `+0x0A` | u8     | enable_fishing_productivity | Equals `enable_corp_productivity` on every row                                          |
| `+0x0B` | u8     | enable_loyalty   | `1` on 14 rows, all main towns, see below                                                          |
| `+0x0C` | f32[3] | display_graph_position | World `x, y, z`; all zero on 19 rows                                                         |
| `+0x18` | u8     | is_productivity_changed | Always `0`                                                                                  |
| `+0x19` | i32    | corp_productivity | Always `1000000`, the 2016 loader's default                                                       |
| `+0x1D` | i32    | fishing_productivity | Always `1000000`, the 2016 loader's default                                                    |
| `+0x21` | i32    | loyalty          | Always `1000000`, the 2016 loader's default                                                        |
| `+0x25` | i32[3] | varied_productivity | Always `0`: `_variedCorpProductivity`, `_variedFishingProductivity`, `_variedLoyalty`           |
| `+0x31` | u8     | unknown_31       | Always `1`; after the 2016 members, see Open Questions                                             |
| `+0x32` | u8     | unknown_32       | Always `0`                                                                                         |

Earlier versions of this doc read `+0x05` as a u16 with two bytes of padding and called the fields from `+0x03` to `+0x21` `unknown_03` to `unknown_21`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 1

On client 1784 a Row was 49 bytes: it ended after `varied_productivity`,
without `unknown_31` and `unknown_32`. Only the Row differs from Layout 2.
The file holds `170` rows on client 1784.

### Row (49 bytes)

| Offset  | Type   | Field                          | Notes |
| ------- | ------ | ------------------------------ | ----- |
| `+0x00` | u16    | region_group_key               |       |
| `+0x02` | u8     | is_blocked_managing            |       |
| `+0x03` | u16    | concurrent_playable_user_count |       |
| `+0x05` | u32    | node_key                       |       |
| `+0x09` | u8     | enable_corp_productivity       |       |
| `+0x0A` | u8     | enable_fishing_productivity    |       |
| `+0x0B` | u8     | enable_loyalty                 |       |
| `+0x0C` | f32[3] | display_graph_position         |       |
| `+0x18` | u8     | is_productivity_changed        |       |
| `+0x19` | i32    | corp_productivity              |       |
| `+0x1D` | i32    | fishing_productivity           |       |
| `+0x21` | i32    | loyalty                        |       |
| `+0x25` | i32[3] | varied_productivity            |       |

## Row Values

### `concurrent_playable_user_count` Values (client 3473)

| Value   | Rows | Groups |
| ------- | ---- | ------ |
| `10000` | 1    | Group 0 |
| `3000`  | 1    | Velia |
| `2000`  | 8    | Heidel, Calpheon, Calpheon Castle, Behr, Mediah Shore, Loopy Tree Forest, Valencia City and the node-less group 40 |
| `1300`  | 2    | Olvia and Olvia Academy |
| `1000`  | 41   | Kamasylvia, Drieghan and the newer regions |
| `999`   | 49   | Most of Mediah (Altinova included), Valencia and the open sea |
| `500`   | 148  | All other groups |

The character select screen asks for the login queue of a character's region group (`getTicketCountByRegion`), which fits a per-group user limit.

### `enable_loyalty` Groups

Set on 14 groups: Velia, Heidel, Glish, Calpheon, Trent, Keplan, Altinova, Olvia, Valencia City, Shakatu, Sand Grain Bazaar, Duvencrune, O'draxxia and Olvia Academy. Other main towns such as Iliya Island, Tarif, Port Epheria, Grána and Arehaza are not.

The parser stores `node_key` as `None` when it is `0`, and `display_graph_position` as `pos_x`, `pos_y`, `pos_z`, each `None` when all three are `0`. It keeps the fields with a value other than `0` and leaves out `is_blocked_managing`, `is_productivity_changed` and `varied_productivity`.

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::RegionGroupInfo` holds `_key`, `_isBlockedManaging`, `_concurrentPlayableUserCount`, `_waypointKey` (i32), `_enableCorpProductivity`, `_enableFishingProductivity`, `_enableLoyalty`, `_regionPosition`, `_isProductivityChanged`, `_corpProductivity`, `_fishingProductivity`, `_loyalty`, `_variedCorpProductivity`, `_variedFishingProductivity` and `_variedLoyalty` (all i32), with pointers in between. The row stores them in this order without the pointers or padding, from `+0x00` to `+0x30`. `GameCommonParameterLoaderFromExcel::LoadRegionGroupInformation` reads `RegionGroupKey`, `WaypointKey`, `DisplayGraphPositionX` to `Z`, `CorpProductivity`, `FishingProductivity`, `Loyalty` (as bools) and `ConcurrentPlayableUserCount` from `RegionGroup_Table` into those members, and sets `_corpProductivity`, `_fishingProductivity` and `_loyalty` to `1000000` and the three varied values to `0` for every row: the values this file stores.

The `RegionGroup_Table` sheet of a private server's `DataSheets.bexcel` on client 1784 and the same table of a second private server on client 519 match the file by value over the group keys each shares with client 3473:

| Column | Field | Equal (client 1784, 169 keys) | Equal (client 519, 150 keys) |
| ------ | ----- | ------------------------ | ------------------------ |
| `WaypointKey` | `node_key` | 168 | 148 |
| `CorpProductivity` | `enable_corp_productivity` | 168 | 149 |
| `FishingProductivity` | `enable_fishing_productivity` | 168 | 149 |
| `Loyalty` | `enable_loyalty` | 169 | 150 |
| `ConcurrentPlayableUserCount` | `concurrent_playable_user_count` | 139 | 118 |
| `DisplayGraphPositionX` to `Z` | `display_graph_position` | 168 | 149 |

The two productivity flags hold the same value on every row in all three sources, so they are told apart by the 2016 order alone. The other `ConcurrentPlayableUserCount` rows are raises (`500` to `1000` on 25 bexcel rows, `500` or `999` to `2000` on 5); the file and both tables use the same seven values. Group 179 has both productivity flags set here and clear in both tables. `is_blocked_managing` and `is_productivity_changed` have no column; they are named from their place in the 2016 member order.

## Notes

- Joining `regioninfo.bss` on `regionGroupKey` (record head `+104`) uses every one of the 250 keys and no other: no region points at a missing group and no group is unused.
- `node_key` is the `explorationKey` (`regioninfo.bss` head `+111`) of one of the group's own regions on 218 of the 231 groups that have a node. The other 13 are group `101` (node `1024`) and the open-sea groups `181` to `192` (nodes `1721` to `1733`, which have no LOC name), whose regions point at other sea nodes.
- The node is the group's main town or area: group 1 is Velia (node 1) and holds region 5 Velia (a town region), group 11 is Heidel (node 301) for Serendia, group 31 is Calpheon (node 601), group 55 Altinova (node 1101), group 202 Valencia City (node 1301).
- `display_graph_position` is near the node but is not the node's position from `mapdata_realexplore2.bwp`: the distance is usually 5,000 to 50,000 units (Velia: group `7542, -6548, 72626`, node `13800, -6715, 76996`). Groups 160 to 176 and 194 to 198 share one position (`-127640, 8789, -446513`) although their nodes lie far apart, and groups 215 to 220 share another. The sheet column is `DisplayGraphPosition` and the 2016 member `_regionPosition`.
- The file has no strings of its own and the client has no LOC type for region group names, so a group is shown by its node.
- The client Lua uses the group key in only three places: the login queue (`getRegionGroupKey`, `getTicketCountByRegion`), the NPC navigator filter (`regionGroup`) and a worker `RegionWork` result (`regionGroupInfo`). None of them reads a field of this file by name.
- The client 519 private server loads `CorpProductivity`, `FishingProductivity` and `Loyalty` but never reads them back. Every 15 minutes its `RegionProductivityService` picks a random value from 500,000 to 1,000,000 per group for each of `Loyalty`, `Farming` and `Fishing` and sends all groups in one packet, as fishing, farming, loyalty per group. It calls corp productivity "Farming", which is its own name and no client source confirms it.

## Open Questions

### What the Productivity and Loyalty Flags Drive

The client Lua reads none of the three enable flags or the productivity values. It registers `FromClient_NotifyChangeRegionProductivity`, which only refreshes the worker and node product windows (`new_worldmap_workmanager_plant.luac`, `panel_worldmap_nodeproduct_renew.luac`), so the server can change a region's productivity at run time. The 2016 `_varied*` members suggest it adjusts the `1000000` base per group; which game feature the corp, fishing and loyalty values stand for is unknown.

### unknown_31

A u8 of `1` on every row, after the last 2016 member. A constant cannot be told apart from the data alone, and no sheet column is left to match it.
