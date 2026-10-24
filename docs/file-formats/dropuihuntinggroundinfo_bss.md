# `dropuihuntinggroundinfo.bss` Format

## Purpose

The hunting grounds of the drop item window (Monster Zone Info): one
variable-length row per zone with its region tab, filter categories, Korean
name, monsters, repeat and sudden quests, drop items, tags, regions, titles,
navigation position, recommended and Total Stat AP / DP, node and the Max AP
Limit. LOC type 116 names the zones by key.

`worldmapmonster.dbss` points at these keys from its hunting zone markers (see
[`worldmapmonster_dbss.md`](worldmapmonster_dbss.md) Notes).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                          | Bytes  | Records                | Row bytes                  |
| ------ | -------------- | ------- | ----------------------------- | ------ | ---------------------- | -------------------------- |
| 1      | 3321 and later | 3483    | `dropuihuntinggroundinfo.bss` | 28,350 | 112 Hunting Ground Row | 103 to 325, 218 on average |

| Layout | File                          | Known             | Unknown    |
| ------ | ----------------------------- | ----------------- | ---------- |
| 1      | `dropuihuntinggroundinfo.bss` | 28,350 B (100.0%) | 0 B (0.0%) |

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
| 3314   | No documented layout |
| 3303   | No documented layout |
| 3302   | No documented layout |
| 3293   | No documented layout |
| 3283   | No documented layout |
| 3275   | No documented layout |
| 3267   | No documented layout |
| 3258   | No documented layout |
| 3251   | No documented layout |
| 3242   | No documented layout |
| 3235   | No documented layout |
| 3229   | No documented layout |
| 3212   | No documented layout |
| 3203   | No documented layout |
| 3193   | No documented layout |
| 3186   | No documented layout |
| 3177   | No documented layout |
| 3169   | No documented layout |
| 3158   | No documented layout |
| 3151   | No documented layout |
| 3144   | No documented layout |
| 3133   | No documented layout |
| 3125   | No documented layout |
| 3118   | No documented layout |
| 3111   | No documented layout |
| 3103   | No documented layout |
| 3095   | No documented layout |
| 3086   | No documented layout |
| 3072   | No documented layout |
| 3062   | No documented layout |
| 3052   | No documented layout |
| 3045   | No documented layout |
| 3037   | No documented layout |
| 3030   | No documented layout |
| 3021   | No documented layout |
| 3012   | No documented layout |
| 3002   | No documented layout |
| 2995   | No documented layout |
| 2987   | No documented layout |
| 2978   | No documented layout |
| 2970   | No documented layout |
| 2959   | No documented layout |
| 2951   | No documented layout |
| 2942   | No documented layout |
| 2935   | No documented layout |
| 2932   | No documented layout |
| 2923   | No documented layout |
| 2919   | No documented layout |
| 2907   | No documented layout |
| 2900   | No documented layout |
| 2891   | No documented layout |
| 2882   | No documented layout |
| 2872   | No documented layout |
| 2863   | No documented layout |
| 2855   | No documented layout |
| 2849   | No documented layout |
| 2844   | No documented layout |
| 2834   | No documented layout |
| 2825   | No documented layout |
| 2819   | No documented layout |
| 2811   | No documented layout |
| 2803   | No documented layout |
| 2794   | No documented layout |
| 2783   | No documented layout |
| 2774   | No documented layout |
| 2765   | No documented layout |
| 2756   | No documented layout |
| 2750   | No documented layout |
| 2743   | No documented layout |
| 2736   | No documented layout |
| 2726   | No documented layout |
| 2717   | No documented layout |
| 2709   | No documented layout |
| 2703   | No documented layout |
| 2695   | No documented layout |
| 2684   | No documented layout |
| 2672   | No documented layout |
| 2665   | No documented layout |
| 2657   | No documented layout |
| 2649   | No documented layout |
| 2644   | No documented layout |
| 2637   | No documented layout |
| 2629   | No documented layout |
| 2619   | No documented layout |
| 2612   | No documented layout |
| 2606   | No documented layout |
| 2602   | No documented layout |
| 2601   | No documented layout |
| 2592   | No documented layout |
| 2583   | No documented layout |
| 2575   | No documented layout |
| 2567   | No documented layout |
| 2560   | No documented layout |
| 2553   | No documented layout |
| 2545   | No documented layout |
| 2538   | No documented layout |
| 2529   | No documented layout |
| 2519   | No documented layout |
| 2513   | No documented layout |
| 2510   | No documented layout |
| 2507   | No documented layout |
| 2503   | No documented layout |
| 2498   | No documented layout |
| 2492   | No documented layout |
| 2487   | No documented layout |
| 2480   | No documented layout |
| 2474   | No documented layout |
| 2468   | No documented layout |
| 2460   | No documented layout |
| 2453   | No documented layout |
| 2444   | No documented layout |
| 2438   | No documented layout |
| 2434   | No documented layout |
| 2429   | No documented layout |
| 2421   | No documented layout |
| 2414   | No documented layout |
| 2407   | No documented layout |
| 2401   | No documented layout |
| 2397   | No documented layout |
| 2393   | No documented layout |
| 2384   | No documented layout |
| 2378   | No documented layout |
| 2372   | No documented layout |
| 2358   | No documented layout |
| 2352   | No documented layout |
| 2347   | No documented layout |
| 2343   | No documented layout |
| 2335   | No documented layout |
| 2327   | No documented layout |
| 2324   | No documented layout |
| 2319   | No documented layout |
| 2313   | No documented layout |
| 2308   | No documented layout |
| 2302   | No documented layout |
| 2295   | No documented layout |
| 2290   | No documented layout |
| 2284   | No documented layout |
| 2276   | No documented layout |
| 2269   | No documented layout |
| 2259   | No documented layout |
| 2250   | No documented layout |
| 2243   | No documented layout |
| 2235   | No documented layout |
| 2229   | No documented layout |
| 2224   | No documented layout |
| 2218   | No documented layout |
| 2215   | No documented layout |
| 2207   | No documented layout |
| 2203   | No documented layout |
| 2196   | No documented layout |
| 2192   | No documented layout |
| 2189   | No documented layout |
| 2183   | No documented layout |
| 2179   | No documented layout |
| 2171   | No documented layout |
| 2163   | No documented layout |
| 2156   | No documented layout |
| 2151   | No documented layout |
| 2147   | No documented layout |
| 2142   | No documented layout |
| 2138   | No documented layout |
| 2134   | No documented layout |
| 2130   | No documented layout |
| 2122   | No documented layout |
| 2107   | No documented layout |
| 2098   | No documented layout |
| 2089   | No documented layout |
| 2081   | No documented layout |
| 2073   | No documented layout |
| 2067   | No documented layout |
| 2063   | No documented layout |
| 2059   | No documented layout |
| 2052   | No documented layout |
| 2044   | No documented layout |
| 2039   | No documented layout |
| 2032   | No documented layout |
| 2025   | No documented layout |
| 2011   | No documented layout |
| 2005   | No documented layout |
| 2000   | No documented layout |
| 1996   | No documented layout |
| 1991   | No documented layout |
| 1985   | No documented layout |
| 1980   | No documented layout |
| 1969   | No documented layout |
| 1964   | No documented layout |
| 1958   | No documented layout |
| 1950   | No documented layout |
| 1945   | No documented layout |
| 1937   | No documented layout |
| 1933   | No documented layout |
| 1927   | No documented layout |
| 1921   | No documented layout |
| 1914   | No documented layout |
| 1908   | No file              |
| 1897   | No file              |
| 1892   | No file              |
| 1886   | No file              |
| 1881   | No file              |
| 1871   | No file              |
| 1866   | No file              |
| 1862   | No file              |
| 1854   | No file              |
| 1846   | No file              |
| 1838   | No file              |
| 1832   | No file              |
| 1826   | No file              |
| 1822   | No file              |
| 1818   | No file              |
| 1804   | No file              |
| 1794   | No file              |
| 1790   | No file              |
| 1784   | No file              |
| 1774   | No file              |
| 1771   | No file              |
| 1762   | No file              |
| 1759   | No file              |
| 1754   | No file              |
| 1749   | No file              |
| 1743   | No file              |
| 1737   | No file              |
| 1731   | No file              |
| 1725   | No file              |
| 1717   | No file              |
| 1710   | No file              |
| 1704   | No file              |
| 1698   | No file              |
| 1690   | No file              |
| 1685   | No file              |
| 1680   | No file              |
| 1674   | No file              |
| 1668   | No file              |
| 1659   | No file              |
| 1649   | No file              |
| 1642   | No file              |
| 1636   | No file              |
| 1628   | No file              |
| 1622   | No file              |
| 1614   | No file              |
| 1608   | No file              |
| 1602   | No file              |
| 1598   | No file              |
| 1594   | No file              |
| 1590   | No file              |
| 1587   | No file              |
| 1584   | No file              |
| 1579   | No file              |
| 1572   | No file              |
| 1565   | No file              |
| 1559   | No file              |
| 1554   | No file              |
| 1547   | No file              |
| 1537   | No file              |
| 1529   | No file              |
| 1524   | No file              |
| 1519   | No file              |
| 1509   | No file              |
| 1506   | No file              |
| 1504   | No file              |
| 1500   | No file              |
| 1493   | No file              |
| 1489   | No file              |
| 1485   | No file              |
| 1481   | No file              |
| 1474   | No file              |
| 1466   | No file              |
| 1462   | No file              |
| 1459   | No file              |
| 1453   | No file              |
| 1450   | No file              |
| 1445   | No file              |
| 1439   | No file              |
| 1433   | No file              |
| 1430   | No file              |
| 1426   | No file              |
| 1421   | No file              |
| 1417   | No file              |
| 1416   | No file              |
| 1409   | No file              |
| 1405   | No file              |
| 1401   | No file              |
| 1396   | No file              |
| 1391   | No file              |
| 1390   | No file              |
| 1386   | No file              |
| 1381   | No file              |
| 1379   | No file              |
| 1372   | No file              |
| 1366   | No file              |
| 1364   | No file              |
| 1363   | No file              |
| 1360   | No file              |
| 1358   | No file              |
| 1355   | No file              |
| 1351   | No file              |
| 1348   | No file              |
| 1346   | No file              |
| 1341   | No file              |
| 1340   | No file              |
| 1338   | No file              |
| 1335   | No file              |
| 1333   | No file              |
| 1329   | No file              |
| 1327   | No file              |
| 1324   | No file              |
| 1321   | No file              |
| 1319   | No file              |
| 1318   | No file              |
| 1316   | No file              |
| 1313   | No file              |
| 1311   | No file              |
| 1309   | No file              |
| 1304   | No file              |
| 1292   | No file              |
| 1286   | No file              |
| 1280   | No file              |
| 1276   | No file              |
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

| File                                                          | Required | Role                                                      |
| ------------------------------------------------------------- | -------- | --------------------------------------------------------- |
| [`dropuimaincategoryinfo.bss`](dropuimaincategoryinfo_bss.md) | Optional | Region tabs: tab key -> territory, for the Region column  |
| [`dropuitaginfo.bss`](dropuitaginfo_bss.md)                   | Optional | Tag pill colours for the Tags column                      |
| `languagedata_en.loc`                                         | Optional | Zone names (116), categories (115), tags (117), territories (12), monsters (6), items (0), quests (18), regions (17), titles (1), nodes (29) |

[`dropuisubcategoryinfo.bss`](dropuisubcategoryinfo_bss.md) holds the filter
categories of `sub_category_keys`; the handler names them from LOC type 115
alone.

`dropuiurlinfo.bss` (20 bytes) is an empty PABR table on client 3458 (count
0); see [empty](empty_bss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR block with variable-length rows, followed by the same counted string
table and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`).

| Offset              | Type                      | Field              | Notes                                        |
| ------------------- | ------------------------- | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]                   | magic              | ASCII `PABR`                                 |
| `+0x04`             | u32                       | count              | Number of rows; 112 on client 3458           |
| `+0x08`             | Hunting Ground Row[count] | rows               | Variable-length rows, read in order          |
| `rows+0x00`         | String Table              | string_table       | 112 wide strings, one Korean name per row    |
| `string_table+0x00` | u32                       | string_table_start | Where the rows end (`0x5FD8` on client 3458) |
| `string_table+0x04` | u32                       | zero               | Always `0`                                   |

Rows are sorted by key, which runs from 0 to 119 with gaps (2, 4, 7, 8, 14,
15, 16 and 49 are missing).

### Hunting Ground Row (variable: 85 bytes + lists)

A list is a u32 count followed by that many values.

| Offset                   | Type                        | Field                    | Notes                                                                 |
| ------------------------ | --------------------------- | ------------------------ | --------------------------------------------------------------------- |
| `+0x00`                  | u32                         | key                      | Hunting ground key; LOC type 116 `str_id1`                            |
| `+0x04`                  | u32                         | main_category_key        | Region tab, 1 to 13, a `dropuimaincategoryinfo.bss` key               |
| `+0x08`                  | u32                         | sub_category_key_count   | Number of `sub_category_keys`                                         |
| `+0x0C`                  | u32[sub_category_key_count] | sub_category_keys        | Filter categories (`dropuisubcategoryinfo.bss` keys, LOC type 115); empty on 13 rows |
| `sub_category_keys+0x00` | u32                         | name_ref                 | String table index of the Korean name; unique per row                 |
| `sub_category_keys+0x04` | u32                         | monster_id_count         | Number of `monster_ids`                                               |
| `sub_category_keys+0x08` | u16[monster_id_count]       | monster_ids              | Character IDs (LOC type 6), 1 to 17 per row                           |
| `monster_ids+0x00`       | u32                         | repeat_quest_key_count   | Number of `repeat_quest_keys`                                         |
| `monster_ids+0x04`       | u32[repeat_quest_key_count] | repeat_quest_keys        | Packed quest keys: low u16 quest chain, high u16 quest (LOC type 18 `str_id1` / `str_id2`), as in `allquestlist.bss`; repeat, daily and weekly quests |
| `repeat_quest_keys+0x00` | u32                         | sudden_quest_key_count   | Number of `sudden_quest_keys`                                         |
| `repeat_quest_keys+0x04` | u32[sudden_quest_key_count] | sudden_quest_keys        | Packed like `repeat_quest_keys`; subjugation and season quests, on 27 rows (13 of them in Valencia) |
| `sudden_quest_keys+0x00` | u32                         | drop_item_count          | Number of `drop_item_ids`                                             |
| `sudden_quest_keys+0x04` | u32[drop_item_count]        | drop_item_ids            | Item IDs (LOC type 0), plain IDs with no enchant level, in the window's display order |
| `drop_item_ids+0x00`     | u32                         | tag_key_count            | Number of `tag_keys`                                                  |
| `drop_item_ids+0x04`     | u32[tag_key_count]          | tag_keys                 | Tag keys, LOC type 117 (`#LotsOfMobs`, `#CombatEXP`)                  |
| `tag_keys+0x00`          | u32                         | region_key_count         | Number of `region_keys`                                               |
| `tag_keys+0x04`          | u16[region_key_count]       | region_keys              | Region keys, LOC type 17; a zone can span several regions (Mansha Forest: 289 and 523) |
| `region_keys+0x00`       | u32                         | title_key_count          | Number of `title_keys`                                                |
| `region_keys+0x04`       | u32[title_key_count]        | title_keys               | Titles earned in the zone, LOC type 1 (`Mansha Slayer`)               |
| `title_keys+0x00`        | f32[3]                      | position                 | World position for the navigation guide; `0, 0, 0` on 21 rows         |
| `title_keys+0x0C`        | f32                         | recommended_ap           | The "Recommended AP" of the worldmap marker label                     |
| `title_keys+0x10`        | f32                         | recommended_dp           | Recommended DP                                                        |
| `title_keys+0x14`        | u32                         | node_key                 | `exploration.bss` node key (LOC type 29); `0` on 6 rows               |
| `title_keys+0x18`        | f32                         | total_ap                 | The "AP (Total Stat)" of the worldmap marker label                    |
| `title_keys+0x1C`        | f32                         | total_dp                 | Recommended DP (Total Stat)                                           |
| `title_keys+0x20`        | u32                         | limited_ap               | Max AP Limit                                                          |
| `title_keys+0x24`        | u32                         | limited_ap_apply_percent | Percent of the AP above `limited_ap` that still applies; `0` on 13 rows |
| `title_keys+0x28`        | u8                          | tribe_type               | Monster species, 0 to 4; see `tribe_type` Values                      |

All 112 rows walk to exactly `string_table_start` with this layout on client
3458.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                      |
| ------- | ------------------ | ------------ | ------------------------------------------ |
| `+0x00` | u32                | string_count | 112 on client 3458                         |
| `+0x04` | pstr[string_count] | strings      | Korean zone names; `name_ref` indexes them |

## `tribe_type` Values

The client enum `__eNewTribeType_*`; the drop window labels each value with a
`GAME` sheet string (LOC type 37) and says which Extra AP applies
(`LUA_DROPITEM_<X>_TOOLTIP_DESC`).

| Value | Enum         | Label key                              | Label                 | Rows | Extra AP that applies             |
| ----- | ------------ | -------------------------------------- | --------------------- | ---- | --------------------------------- |
| 0     | `Human`      | `LUA_DROPITEM_HUMAN_TOOLTIP_NAME`      | Humans                | 21   | Extra AP Against Humans           |
| 1     | `NonHuman`   | `LUA_DROPITEM_AIN_TOOLTIP_NAME`        | Demihumans            | 34   | Extra AP Against Demihumans       |
| 2     | `Others`     | `LUA_DROPITEM_NORMAL_TOOLTIP_NAME`     | Normal                | 22   | Extra AP Against Monsters         |
| 3     | `Kamasilvia` | `LUA_DROPITEM_KAMASILVIA_TOOLTIP_NAME` | Kamasylvian Monsters  | 21   | Extra AP Against Kamasylvian Monsters |
| 4     | `Edania`     | `LUA_DROPITEM_EDANIA_TOOLTIP_NAME`     | Edanian Monsters      | 14   | Extra AP Against Edanian Monsters |

The Lua lists the five enum names with their label keys in this order, and the
zones match: `0` bandits, pirates, Abandoned Monastery and the Elvia human
zones; `1` Mansha Forest, Catfishman Camp, Rhutum Outstation; `2` Hexe
Sanctuary, Soldier's Grave, Cyclops Land; `3` Polly's Forest, Navarn Steppe,
Ash Forest, Olun's Valley; `4` Aetherion Castle to Scales of Judgment.

## Notes

- Since client 3464 every one of the 112 names opens with a level, in the
  Korean string table (`Lv.74 아레시온 신전`) and in LOC type 116
  (`Lv. 74 Aresion Temple`). The node names (LOC type 29) carry none. The
  handler shows the names as stored.
- The drop item window Lua (`window/dropitem/panel_window_renewdropitem_all_1`)
  reads the row through `ToClient_getDropUIHuntingGroundStaticStatusWrapper`;
  its getters match the fields: `getMainCategoryKey`,
  `getSubCategoryKeyByIndex`, `getName`, `getRepeatQuestNoByIndex`,
  `getSuddenQuestNoByIndex`, `getDropItemStaticStatusWrapper`,
  `getTagKeyByIndex`, `getRegionKeyRawByIndex`,
  `getDropTitleStaticStatusWrapper`, `getWayPointKey`, `getLimitedAP`,
  `getLAPApplyPercent` and `getTribeType`.
- The Max AP Limit text is `LUA_DROPINFO_MAXAP` (`{appoint}({appercent}%)`)
  or, when the percent is 0, `LUA_DROPINFO_MAXAP_NONE_PERCENT` (`{appoint}
  effective limit`); `LUA_DROPINFO_MAXAP_DESC` explains that only that share of
  the AP above the limit applies.
- The AP values equal the worldmap marker labels of the same zone: Aresion
  Temple stores 415 and 2455, and its marker reads "Recommended AP: 415" and
  "AP (Total Stat): 2455". `limited_ap` sits 30 above `total_ap` on 67 rows
  (2455 -> 2485, 2570 -> 2600).
- LOC type 116 names all 112 rows and has one more key, 49, with no row.
  Every monster, item, tag, region, title, node and quest ID in the file has
  LOC text on client 3458.
- The `CHARACTER_HUNTING_GROUNDS` lookup index inverts `monster_ids`
  (character key -> the keys of the rows that list it), and
  `HUNTING_GROUND_NAME_KR` holds `name_kr` by key, the fallback when LOC type
  116 has no name. The [`monstergroup.dbss`](monstergroup_dbss.md) Hunting
  Grounds column reads both and links each zone to its row here.
- `drop_item_ids` holds plain item IDs (`28` Prognyl Silver Bar, `721002`
  Ancient Spirit Dust), not the packed `itemenchant.dbss` key.
- bdo-viewer (built on bdo-data-extractor) counts 105 zones; the file holds
  112 rows.
