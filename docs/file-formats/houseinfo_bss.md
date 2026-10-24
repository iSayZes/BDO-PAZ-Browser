# `houseinfo.bss` Format

## Purpose

The node houses of the world map: one variable-length row per house with
the house's character key, the contribution points it costs, its town and
worldmap node, its house group and floor, the houses that must be bought
before it, and its uses ("crafts": a `houseinforeceipe.dbss` receipe and the
highest level the house reaches with it). After the rows comes a product
list that maps each item to the houses whose uses make it. The client Lua
reads a row through `ToClient_GetHouseInfoStaticStatusWrapper(houseKey)`.

On client 3474 the 823 rows cover 32 towns and 78 nodes; the product list
holds 2,521 items.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes   | Records                                   | Row bytes |
| ------ | -------------- | ------- | --------------- | ------- | ----------------------------------------- | --------- |
| 2      | 2429 and later | 3483    | `houseinfo.bss` | 172,181 | 3,056 Craft, 823 House Row, 2,521 Product | 8         |
| 1      | 805 to 2163    | 2163    | `houseinfo.bss` | 48,608  | 2,866 Craft, 766 House Row                | 8         |

| Layout | File            | Known             | Unknown        |
| ------ | --------------- | ----------------- | -------------- |
| 2      | `houseinfo.bss` | 169,712 B (98.6%) | 2,469 B (1.4%) |
| 1      | `houseinfo.bss` | 47,076 B (96.8%)  | 1,532 B (3.2%) |

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

| File                         | Required | Role                                                                                             |
| ---------------------------- | -------- | ------------------------------------------------------------------------------------------------ |
| `houseinforeceipe.dbss`      | Optional | Korean receipe names for the uses when LOC has none; see [`houseinforeceipe.dbss`](houseinforeceipe_dbss.md) |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a house key without a row shows as plain text                |
| `languagedata_en.loc`        | Optional | House names (type 6), town names (type 17), node names (type 29), receipe names (type 16), item names (type 0) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

The PABR frame of `buffsimply.bss`: magic, row count, rows, string table and
an 8-byte trailer. The string table is empty; between the rows and the
string table sits the product list.

| Offset              | Type                    | Field         | Notes                                                    |
| ------------------- | ----------------------- | ------------- | -------------------------------------------------------- |
| `+0x00`             | char[4]                 | magic         | ASCII `PABR`                                             |
| `+0x04`             | u32                     | count         | Number of house rows; 823 on client 3474                 |
| `+0x08`             | House Row[count]        | rows          | See House Row                                            |
| `rows+0x00`         | u32                     | product_count | Number of product entries; 2,521 on client 3474          |
| `rows+0x04`         | Product[product_count]  | products      | See Product                                              |
| `products+0x00`     | String Table            | string_table  | See String Table                                         |
| `string_table+0x00` | u32                     | table_start   | Offset of the string table, where the product list ends  |
| `string_table+0x04` | u32                     | zero          | Always 0                                                 |

The rows are not sorted by key; client 3474 opens with 3823, 3822, 3821.

### House Row (variable: 33 bytes + need house keys and crafts)

| Offset                 | Type                    | Field                | Notes                                                                                   |
| ---------------------- | ----------------------- | -------------------- | --------------------------------------------------------------------------------------- |
| `+0x00`                | i16                     | need_explore_point   | Contribution points to buy the house; `getNeedExplorePoint()`, `1` to `3` on client 3474 |
| `+0x02`                | u16                     | affiliated_town      | Town the house belongs to, a `regioninfo.bss` region key (LOC type 17: `5` Velia, `32` Heidel) |
| `+0x04`                | u32                     | parent_node_key      | Worldmap node of the house (LOC type 29); `getParentNodeKey()`                          |
| `+0x08`                | u16                     | character_key        | Row key: the house's `characterstatic.dbss` character; `getHouseKey()`                  |
| `+0x0A`                | u16                     | unknown_0a           | `0xFFFF` on every row (clients 1784 and 3474); see Field Names                          |
| `+0x0C`                | u32                     | house_group          | Building the house is a floor of, `0` for a house of its own; see House Groups          |
| `+0x10`                | i32                     | house_floor          | Floor in the building, `1` up, `-1` on 3 rows; `0` when `house_group` is `0`            |
| `+0x14`                | u64                     | need_house_count     | Number of `need_house_keys`; `0` or `1` on every row (client 3474)                      |
| `+0x1C`                | u16[need_house_count]   | need_house_keys      | Houses to own before this one can be bought, keys of other rows                         |
| `need_house_keys+0x00` | u32                     | craft_count          | Number of `crafts`                                                                      |
| `need_house_keys+0x04` | Craft[craft_count]      | crafts               | The uses the house can be set to; see Craft                                             |
| `crafts+0x00`          | u8                      | unknown_after_crafts | `1` on the four Dokkebi Jar houses (3837 to 3840), `0` on every other row (client 3474) |

### Craft (8 bytes)

| Offset  | Type | Field       | Notes                                                                                      |
| ------- | ---- | ----------- | ------------------------------------------------------------------------------------------ |
| `+0x00` | u32  | receipe_key | [`houseinforeceipe.dbss`](houseinforeceipe_dbss.md) receipe key; all 106 keys used have a row (client 3474) |
| `+0x04` | u32  | level       | Highest level of the use in this house, `1` to `5`                                         |

The first craft of every row (client 3474) is receipe `2` (Storage); 777 of
the 823 rows hold receipe `0` (Residence) at level `1`, as their last craft.

### Product (variable: 12 bytes + house keys)

| Offset  | Type               | Field       | Notes                                                                  |
| ------- | ------------------ | ----------- | ---------------------------------------------------------------------- |
| `+0x00` | u32                | item_key    | Item the houses make; entries sorted by `item_key`, unique            |
| `+0x04` | u64                | house_count | Number of `house_keys`                                                 |
| `+0x0C` | u16[house_count]   | house_keys  | `character_key` of a house row, once per exchange that makes the item |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3474          |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries; none in the file |

## Layout 1

Clients 1230 to 2107 have no product list: the string table follows the
rows. The House Row ends after `crafts`, with no `unknown_after_crafts`.
Only the File Layout and the House Row differ from Layout 2.

### File Layout

| Offset              | Type             | Field        | Notes                                           |
| ------------------- | ---------------- | ------------ | ----------------------------------------------- |
| `+0x00`             | char[4]          | magic        | ASCII `PABR`                                    |
| `+0x04`             | u32              | count        | 759 on client 1784                              |
| `+0x08`             | House Row[count] | rows         | See House Row                                   |
| `rows+0x00`         | String Table     | string_table | See String Table                                |
| `string_table+0x00` | u32              | table_start  | Offset of the string table, where the rows end  |
| `string_table+0x04` | u32              | zero         | Always 0                                        |

### House Row (variable: 32 bytes + need house keys and crafts)

| Offset                 | Type                  | Field              | Notes                                   |
| ---------------------- | --------------------- | ------------------ | --------------------------------------- |
| `+0x00`                | i16                   | need_explore_point | `1` to `15` on client 1784              |
| `+0x02`                | u16                   | affiliated_town    |                                         |
| `+0x04`                | u32                   | parent_node_key    |                                         |
| `+0x08`                | u16                   | character_key      |                                         |
| `+0x0A`                | u16                   | unknown_0a         |                                         |
| `+0x0C`                | u32                   | house_group        |                                         |
| `+0x10`                | i32                   | house_floor        |                                         |
| `+0x14`                | u64                   | need_house_count   |                                         |
| `+0x1C`                | u16[need_house_count] | need_house_keys    |                                         |
| `need_house_keys+0x00` | u32                   | craft_count        |                                         |
| `need_house_keys+0x04` | Craft[craft_count]    | crafts             |                                         |

## House Groups

`house_group` joins the floors of one building, each floor a house row of
its own with `house_floor` `1`, `2` and up. On client 3474, 375 rows sit in
179 groups (162 of two floors, 17 of three) and 448 rows have group `0`.
The second floor of group 1, house 2109, needs 2108, the first floor. The
three rows with floor `-1` are 2190 (group 64), 2612 (group 126) and 2696
(group 101); the private server sheet holds `-1` for the same three keys.

## Field Names

The `HouseInfo_New` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `CharacterKey`, `HouseGroup`, `HouseFloor`,
`NeedExplorePoint`, `NeedHouseKey`, `AffiliatedTown`, `ParentNode` and
`CraftList` (`2:5, 1:3, 1556:2, 0:1`, receipe and level pairs). Matched by
`CharacterKey`:

| Field                                  | Client 1784  | Client 3474 | Misses                                                              |
| -------------------------------------- | ------------ | ----------- | ------------------------------------------------------------------- |
| `need_explore_point`                   | 759 of 759   | 306 of 766  | Client 3474 lowers the points to `1` to `3`; the sheet holds up to `15` |
| `affiliated_town`, `parent_node_key`   | 759 of 759   | 766 of 766  |                                                                     |
| `house_group`, `house_floor`           | 759 of 759   | 766 of 766  | The sheet's `<null>` reads as `0`                                   |
| `need_house_keys`                      | 759 of 759   | 766 of 766  | The sheet's single `NeedHouseKey`, `<null>` for an empty list       |
| `crafts`                               | 758 of 759   | 745 of 766  | 1784: house 3133 holds receipe 1207 at level 3, the sheet 4; 3474: rebalanced uses |

The sheet has 766 keys; the client 1784 file holds 759 of them, the client
3474 file all 766 and 57 more.

The 2016 `gc::HouseInfoStaticStatus` declares `_needExplorePoint` (short),
`_affiliatedTown`, `_parentNodeKey` (int), `_needHouseKeyList`,
`_nextHouseList`, `_houseCraftList`, `_key`, `_isBlockedNpcWork` (bool),
`_territoryKey` (`KeyType<short,-1>`), `_houseGroup` (unsigned int) and
`_houseFloor` (int); `gc::HouseInfoCraft` holds `_receipeKey` and `_level`.
The file keeps that order for the fields it stores, with the two lists
moved to the end. The client Lua calls `getNeedExplorePoint()`,
`getParentNodeKey()`, `getHouseKey()`, `getNextHouseCount()`,
`getReceipeCount()` and `getReceipeByIndex()` on the row. `unknown_0a`
sits where the 2016 struct puts `_territoryKey` after `_key`, and `-1` is
that key's unset value; with `0xFFFF` on every row nothing confirms it.

`products` is in neither the sheet nor the 2016 struct. On client 3474 the
`house_keys` of each of the 2,521 entries equal, as a multiset, the houses
reached by walking every craft of every row through the
`houseinforeceipe.dbss` level lists up to the craft's `level` and taking
the `product_item_keys` of each [`itemexchangesource.bss`](itemexchangesource_bss.md)
exchange there. A house is listed once per such exchange, so 142 entries
repeat a house. 110 rows have no entry.

## Notes

- `need_house_keys` and `products` name only keys of house rows in the same
  file (580 and 44,569 keys, client 3474).
- The four manor lands and buildings of
  [`mansionlandinfo.bss`](mansionlandinfo_bss.md) are house rows here, each
  with Storage and Residence at level 1 only. The client Lua shows a manor
  land's contribution cost from `ToClient_getNeenPointMansion()` in place
  of `getNeedExplorePoint()` (`panel_window_explorepoint_usinginfo_1.luac`).
- `unknown_after_crafts` and the product list first appear on client 2519;
  client 2107 has neither.

## Open Questions

### What does `unknown_after_crafts` hold?

The byte is `1` on the four Dokkebi Jar houses of Dokkebi Forest (3837 to
3840, town 1210 Dalbeol Village, node 1788) and `0` on the other 819 rows
(client 3474). One of them holds receipe 2002 (Dokkebi Tool Workshop). The
2016 struct's `_isBlockedNpcWork` bool is a lead only; no Lua getter reads a
per-house flag that fits these four houses.
