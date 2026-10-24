# `plantexchangegroup.bss` Format

## Purpose

Worker production groups. Each row is one production key: `plantzone.dbss` points at it from `production_key`, and the row names the [`itemexchangesource.bss`](itemexchangesource_bss.md) exchange the node works, whose product and luck drop groups list the items it produces. Each row also carries a Korean label of the form "node - work type".

The row size and the join fields match [iDevelopThings/bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor) (`FORMATS.md`, "Worker-production item tables"), which leaves the `+0x5A` tail unmapped; it is the label's string table index.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes  | Records                  | Row bytes |
| ------ | -------------- | ------- | ------------------------ | ------ | ------------------------ | --------- |
| 2      | 2726 and later | 3483    | `plantexchangegroup.bss` | 45,631 | 403 Production Group Row | 94        |
| 1      | 805 to 2717    | 2717    | `plantexchangegroup.bss` | 24,665 | 350 Production Group Row | 52        |

| Layout | File                     | Known            | Unknown          |
| ------ | ------------------------ | ---------------- | ---------------- |
| 2      | `plantexchangegroup.bss` | 11,779 B (25.8%) | 33,852 B (74.2%) |
| 1      | `plantexchangegroup.bss` | 9,965 B (40.4%)  | 14,700 B (59.6%) |

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

| File                   | Required | Role                                                              |
| ---------------------- | -------- | ----------------------------------------------------------------- |
| `plantzone.dbss`       | Optional | The zones that use each production key, for the English name      |
| `plantzoneoffset.dbss` | Optional | Index into `plantzone.dbss`                                       |
| `languagedata_en.loc`  | Optional | Node names (LOC type 29) and item names (LOC type 0)              |

Each zone's parent node comes from the `NODE_PARENT` lookup index (see `docs/handler.md`), built from `exploration.bss` and the worldmap links, so the preview opens no worldmap companion. The exchange key is resolved through [`itemexchangesource.bss`](itemexchangesource_bss.md), [`itemmaingroup.bss`](itemmaingroup_bss.md) and [`itemsubgroup.dbss`](itemsubgroup_dbss.md) (see Field Names); the preview reads the items from the `PRODUCTION_ITEMS` and `PRODUCTION_LUCK_ITEMS` lookup indexes and the exchange name from `EXCHANGE_NAME_KR` (see `docs/handler.md`) instead of opening the 3 MB and 13 MB tables as companions.

All multi-byte values are little-endian unless noted otherwise.

## Layout 2

### File Layout

PABR block with fixed 94-byte rows followed by the same counted string table and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md).

| Offset              | Type                        | Field              | Notes                                                 |
| ------------------- | --------------------------- | ------------------ | ----------------------------------------------------- |
| `+0x00`             | char[4]                     | magic              | ASCII `PABR`                                          |
| `+0x04`             | u32                         | count              | Number of rows; `403` on the 2026-09-27 client        |
| `+0x08`             | Production Group Row[count] | rows               | 94-byte rows repeated `count` times                   |
| `rows+0x00`         | String Table                | string_table       | Counted string table, see [`npcsimply.bss` String Table](npcsimply_bss.md#string-table-variable-4-bytes--strings) |
| `string_table+0x00` | u32                         | string_table_start | Equals `8 + count * 94` (`37,890`)                    |
| `string_table+0x04` | u32                         | zero               | Always `0`                                            |

Rows are not sorted by key; the file opens with key 1775 and ends with keys 1, 31, 23, 22, 21.

### Production Group Row (94 bytes)

| Offset  | Type      | Field              | Notes                                                                   |
| ------- | --------- | ------------------ | ----------------------------------------------------------------------- |
| `+0x00` | u16       | production_key     | Join from `plantzone.dbss` `production_key`; unique, observed `1`-`2044` |
| `+0x02` | u16       | unknown_02         | Equals `production_key` on all 403 rows                                  |
| `+0x04` | u16       | unknown_04         | Always `0`                                                              |
| `+0x06` | u32       | exchange_key       | First item exchange key, an `itemexchangesource.bss` row; observed `40001`-`45019`, see Field Names |
| `+0x0A` | bytes[80] | unknown_0a         | Always all zero; exchange key slots 2 to 21, see Field Names            |
| `+0x5A` | u32       | name_ref           | String table index of the Korean group label; unaligned                 |

`name_ref` covers every one of the 275 strings. Rows that share a label share the index (keys 1773 and 1774 are both "마지막 순례길 - 채집"). Most labels are "node - work type"; some use one phrase with no dash, such as "고대인의 석실 발굴" or "생선 건조장".

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                |
| ------- | ------------------ | ------------ | ------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings                    |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries, Korean labels   |

## Layout 1

On client 1784 a row is 52 bytes: `unknown_0a` is 38 bytes instead of 80, so
`name_ref` sits at `+0x30`. Only the Production Group Row differs from
Layout 2.

### Production Group Row (52 bytes)

| Offset  | Type      | Field             | Notes                                   |
| ------- | --------- | ----------------- | --------------------------------------- |
| `+0x00` | u16       | production_key    |                                         |
| `+0x02` | u16       | unknown_02        | Equals `production_key` on client 1784  |
| `+0x04` | u16       | unknown_04        | Always `0` on client 1784               |
| `+0x06` | u32       | exchange_key      |                                         |
| `+0x0A` | bytes[38] | unknown_0a        | Always all zero on client 1784          |
| `+0x30` | u32       | name_ref          | String table index of the Korean group label |

## `exchange_key` Values

On client 3474, 401 of the 403 exchange keys are distinct; 42170 is shared by keys 1541 and 1542, 43165 by 1505 and 1930. Every one is an `itemexchangesource.bss` row of `exchange_type` 4 (Plant). The thousands band loosely follows the work type of the label, but every band holds exceptions, so it is not a rule:

| Band    | Mostly                                      |
| ------- | ------------------------------------------- |
| `40xxx` | Farming (재배, 농장) and crop specialties    |
| `41xxx` | Mining (채광, 광산, 광맥)                    |
| `42xxx` | Lumbering (벌목)                            |
| `43xxx` | Gathering (채집)                            |
| `44xxx` | Excavation, drying yards, finance, specialties |
| `45xxx` | Keys 1929 (통발) and 1931 (발굴)               |

The exchange key, its product drop group and that group's subgroup often share one number, but not always: 37 exchange keys have no `itemsubgroup.dbss` subgroup of the same number (client 3474). 36 of them are the exchanges of the 36 `plantzone.dbss` zones that showed no items while the handler read `+0x06` as a subgroup key; the 37th is exchange 45019 of key 1931, which no zone uses. All 37 have a product drop group.

## English Names

No LOC type holds the labels, and the EU client ships no Korean LOC to match them against. The worker manager (`new_worldmap_workmanager_plant.luac`) reads a per-group description through `ToClient_getPlantWorkableItemExchangeDescriptionByIndex` into `_workName` but never shows it; the panel shows the product's item name. The two halves of the label can be rebuilt in English from the worldmap nodes:

```text
production_key -> plantzone.dbss zone record_id (a sub-node) -> LOC type 29 "Lumbering"
zone -> NODE_PARENT (its one link in mapdata_realexplore2.bwp) -> LOC type 29 "Platerra Mountains"
1928 -> "Platerra Mountains - Lumbering"  (Korean: 플라테르 산맥 - 벌목)
```

Every one of the 439 zones is an `exploration.bss` sub-node with exactly one worldmap link (see [`*.bwp`](waypoint_bwp.md)), so `NODE_PARENT` holds all of them and the preview names a zone with `node_with_parent_name()` from `_common/node.py`. A key gets a name only when every zone using it gives the same one; on client 3458 that is 365 of the 403 keys. The rest keep the Korean label: keys no zone uses (1931 and seven more), and keys shared by zones under different nodes, where the Korean label names a region instead (1231 칼페온 채집, Calpheon gathering, over Karanda Ridge and Longleaf Tree Sentry Post). The `exploration.bss` manager family was used before the links and named 324: it has no main node for some families (Godu Village, 1880) and the wrong one for Specialties 1563 (Areha Palm Forest instead of Arehaza, key 992 아레하자 마을 - 특산품). Investment banks read "Altinova - Gulabi Investment Bank" where the Korean label is only the bank name (928 굴라비 자산 관리소). The English halves follow the worldmap names, not the Korean wording: 1545 "가비냐 대분화구 - 티타늄" (titanium) becomes "Gavinya Great Crater - Mining", and 1203 "칼페온 파프리카 재배" (Calpheon paprika farming) becomes "Northern Wheat Plantation - Paprika Farming".

## Notes

- All 439 `plantzone.dbss` zones on the 2026-09-27 client resolve to a row. 8 keys are not used by any zone: 1503, 1675, 1676, 1931, 2015, 2021, 2036, 2037.
- `production_key` equals the zone's `record_id` for 157 of the 439 zones; the two are separate key spaces, and several zones share one key (1521 and 1934 are used by four zones each).
- LOC type 29 at `str_id1=production_key` gives a node name only by coincidence, when the key equals a node key; use the zone's `record_id` for the node name. That name is the sub-node, the work-type half of the label ("Lumbering", "Teff"); see English Names for the node half.
- bdo-data-extractor calls `+0x06` the "normal-output subgroup". The luck drops are not in this file: they hang off the item exchange (see Field Names).

## Field Names

The 2016 client (build of 2016-01-11) ships with debug symbols. Its `gc::PlantExchangeGroupStaticStatus` holds `_key`, `_isBlockedNpcWork`, `_name` and `_exchangeKeyGroup`, an array of 21 item exchange keys. The server-side `PlantExchangeGroup_Table` of a private server on client 519 has the columns `Index`, `ExchangeGroupName`, `ExchangeKey_0` to `ExchangeKey_20` and `ContentsGroupKey`. It shares 273 production keys with client 3464; on 265 of them `ExchangeKey_0` equals `+0x06`, no other exchange key is set, and `ExchangeGroupName` equals the Korean label. `+0x06` and the 80 zero bytes after it are 21 u32 slots, so `+0x06` is the first exchange key.

The exchange key is the key of an [`itemexchangesource.bss`](itemexchangesource_bss.md) row (`gc::ItemExchangeSourceStaticStatus`, server `ItemExchangeSource`), not an item subgroup. That struct holds `_productItemDropKey` and `_npcWorkerDropKeyForLuck` (`product_drop_key` and `luck_drop_key` in the reader), both keys of [`itemmaingroup.bss`](itemmaingroup_bss.md) groups, and each group lists the subgroups. The client chain, which the handler follows, is:

```text
production_key -> exchange_key (+0x06)
  -> itemexchangesource.bss row -> product_drop_key, luck_drop_key
  -> itemmaingroup.bss group -> itemsubgroup.dbss subgroups -> items
1928 -> exchange 42356 -> product group 42356 (Elder Tree Timber, Bloody Tree Knot, Elder Tree Sap), luck group 44961
```

Earlier versions of the handler read `+0x06` as an `itemsubgroup.dbss` key. That gave the right items on most rows because the exchange key, its drop group and the group's subgroup often share one number, as for 1928 above. On client 3474 the chain changes this against the subgroup reading:

| Rows (client 3474) | Effect of the chain                                                        |
| ------------------ | -------------------------------------------------------------------------- |
| 37                 | Gain items where the subgroup reading found none: the 36 zones of `plantzone.dbss` Open Questions and key 1931 |
| 18                 | Get other items: 1899 "Neruda Plain - Lumbering" (exchange 42194) showed Coal and drops Acacia Timber; 12, 22 and 23 (Excavation) drop group 44013, 44023 and 44025 instead of subgroup 44012, 44022 and 44023 |
| 348                | Keep the same items                                                        |
| 335                | Gain a luck drop group with items                                          |

All 403 exchange keys have a product drop group with items, the Investment Bank rows (keys 901 to 936, 1689, 1690) included. The preview shows the exchange name and links it to its `itemexchangesource.bss` row, then the product items and the luck items.

`+0x02` (equal to `production_key`) and `+0x04` keep their offsets: `+0x04` is `0` on every row while the server's `ContentsGroupKey` is set on 194 of the shared rows.
