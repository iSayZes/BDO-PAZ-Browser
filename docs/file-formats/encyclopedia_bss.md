# `encyclopedia.bss` Format

## Purpose

The entries of the Fishing Encyclopedia (`panel_window_fishencyclopedia_renewal_all`):
one fixed 104-byte row per fish with its item, category tab, rareness, base
size, Korean description and artwork path. The window reads a row through
`ToClient_GetFishEncyclopedia(index)` (`getKey()`, `getName()`,
`getImagePath()`, `getDesc()`, `getGradeType()`, `getAverageValue()`) and lists a tab with
`ToClient_GetFishCountByCategory(category)`. The source sheet is
`Encyclopedia_Table`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes   | Records             | Row bytes |
| ------ | -------------- | ------- | ------------------ | ------- | ------------------- | --------- |
| 2      | 2849 and later | 3483    | `encyclopedia.bss` | 129,560 | 1,510 Dice, 302 Row | 12        |
| 1      | 1280 to 2844   | 2844    | `encyclopedia.bss` | 102,675 | 1,390 Dice, 278 Row | 12        |

| Layout | File               | Known             | Unknown        |
| ------ | ------------------ | ----------------- | -------------- |
| 2      | `encyclopedia.bss` | 127,144 B (98.1%) | 2,416 B (1.9%) |
| 1      | `encyclopedia.bss` | 101,563 B (98.9%) | 1,112 B (1.1%) |

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

None. LOC type 30 holds the description by `key` (`str_id1`, `str_id4` 0),
and LOC type 0 names the item of `item_id`.

All multi-byte values are little-endian.

## Layout 2

### File Layout

PABR block of fixed rows, followed by the same counted string table and
8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). The string table holds two strings per row, the
description and the artwork path.

| Offset              | Type         | Field              | Notes                              |
| ------------------- | ------------ | ------------------ | ---------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                       |
| `+0x04`             | u32          | count              | Number of rows; 302 on client 3473 |
| `+0x08`             | Row[count]   | rows               | See Row                            |
| `rows+0x00`         | String Table | string_table       | 604 wide strings on client 3473    |
| `string_table+0x00` | u32          | string_table_start | Where the rows end                 |
| `string_table+0x04` | u32          | zero               | Always `0`                         |

Rows are sorted by key. On client 3473 the keys run from 1 to 305 with 3
gaps.

### Row (104 bytes)

| Offset  | Type    | Field         | Notes                                                                                   |
| ------- | ------- | ------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u16     | key           | Entry key (`Key`, `getKey()`); LOC type 30 `str_id1` of the description                  |
| `+0x02` | u32     | item_id       | The fish item (`TypeKey`), an `Item_Table` key; LOC type 0 names it                      |
| `+0x06` | u32     | type          | Encyclopedia kind (`Type`): `0` fish on every row                                        |
| `+0x0A` | u8      | category      | Tab of the window (`Category`); see Categories                                          |
| `+0x0B` | u8      | rareness      | `1` to `10` (`Rareness`); see Rareness                                                  |
| `+0x0C` | f32     | base_size     | Smallest size in cm (`BaseSize`)                                                        |
| `+0x10` | f32     | unknown_10    | Whole numbers, 9 to 169 on client 3473; see Average Size                                |
| `+0x14` | u64     | fish_exp_rate | `0` on every row (`FishExpRate`, server only)                                            |
| `+0x1C` | u32     | fish_exp_type | `0` on every row (`FishExpType`, server only)                                            |
| `+0x20` | u32     | desc_ref      | String table index of the Korean description (`Desc`)                                   |
| `+0x24` | u32     | image_ref     | String table index of the artwork path (`Image`), relative to `ui_texture/`             |
| `+0x28` | Dice[5] | vary_sizes    | `VarySize_0` to `VarySize_4`, server only: `1D1+0` on every row                          |
| `+0x64` | u32     | unknown_64    | `0` on every row                                                                        |

### Dice (12 bytes)

A size roll written `<count>D<sides>+<bonus>` in the sheet (`1D2+2` rolls
one two-sided die and adds 2).

| Offset  | Type | Field  | Notes                                          |
| ------- | ---- | ------ | ---------------------------------------------- |
| `+0x00` | u32  | count  | Number of dice; `1` on every row of the client |
| `+0x04` | u32  | sides  | Sides per die; `1` on every row of the client  |
| `+0x08` | i32  | bonus  | Added to the roll; `0` on every row of the client |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                       |
| ------- | ------------------ | ------------ | ------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                           |
| `+0x04` | pstr[string_count] | strings      | `desc_ref` and `image_ref` index this list  |

## Layout 1

On client 1784 `base_size` is a u16 and there is no `unknown_10`, so the row
is 98 bytes. Only the Row differs from Layout 2.

### Row (98 bytes)

| Offset  | Type    | Field         | Notes                       |
| ------- | ------- | ------------- | --------------------------- |
| `+0x00` | u16     | key           |                             |
| `+0x02` | u32     | item_id       |                             |
| `+0x06` | u32     | type          |                             |
| `+0x0A` | u8      | category      |                             |
| `+0x0B` | u8      | rareness      |                             |
| `+0x0C` | u16     | base_size     | `0` on every row (server only on client 1784) |
| `+0x0E` | u64     | fish_exp_rate |                             |
| `+0x16` | u32     | fish_exp_type |                             |
| `+0x1A` | u32     | desc_ref      |                             |
| `+0x1E` | u32     | image_ref     |                             |
| `+0x22` | Dice[5] | vary_sizes    |                             |
| `+0x5E` | u32     | unknown_64    |                             |

Client 1784 has 202 rows, keys 1 to 202.

## Categories

`category` selects the tab. The window maps its four tabs to the values
`1`, `2`, `3`, `0` (`_categoryMapping` in
`panel_window_fishencyclopedia_renewal_all.lua`) and labels them with
`PANEL_FISH_RADIO_1` to `_4`. The source workbook's `#참조` sheet lists the
same names.

| Value | Tab                | Rows (client 3473) |
| ----- | ------------------ | ------------------ |
| 0     | 기타 (Others)       | 23                 |
| 1     | 민물고기 (Freshwater) | 106                |
| 2     | 바다물고기 (Saltwater) | 163                |
| 3     | 갑각류 (Crustacean)  | 10                 |

The workbook comment reserves 6 to 12 (herbs, stone, wood, mushrooms, sap,
hide, meat) for a gathering encyclopedia (`type` 1) that no row of this
file uses.

## Rareness

`rareness` is the workbook's rarity grade, 1 to 10, higher is harder to get.
The workbook comment ties it to which `VarySize_N` roll a catch uses by the
number of that fish caught so far (grade 1: 1 to 150 catches use
`VarySize_0`, 151 to 300 `VarySize_1`, and so on). The old encyclopedia
window (`panel_window_fishencyclopedia_all`) drew up to five stars from
`getRareness()`; the current window colours the name by `getGradeType()`,
which is not a field of this file.

## Average Size

The window prints Average Size from `getAverageValue()` of the entry
(`panel_window_fishencyclopedia_renewal_all.lua`), for caught and uncaught
fish alike. On client 3474 it matched `(base_size + unknown_10) / 2` on four
fish, two of them with `unknown_10` below `base_size`:

| Fish       | base_size | unknown_10 | Average Size |
| ---------- | --------- | ---------- | ------------ |
| Mudskipper | 7         | 9          | 8.000        |
| Tuna       | 40        | 169        | 104.500      |
| Sunfish    | 280       | 99         | 189.500      |
| Notch Jaw  | 25        | 9          | 17.000       |

The handler shows that value as the Average Size column. What `unknown_10`
is on its own stays open; see Open Questions.

## Field Names

The fields are the columns of the `Encyclopedia_Table` sheet that a private
server on client 1784 ships in its `DataSheets.bexcel` and in the developer
workbook `DataSheet_Encyclopedia.xlsm`. Against client 3473 the workbook
shares 202 keys:

| Field       | Column     | Matches (client 3473) |
| ----------- | ---------- | --------------------- |
| `item_id`   | `TypeKey`  | 202 of 202            |
| `type`      | `Type`     | 202 of 202 (all `0`)  |
| `category`  | `Category` | 180 of 202            |
| `rareness`  | `Rareness` | 202 of 202            |
| `base_size` | `BaseSize` | 202 of 202            |
| `desc_ref`  | `Desc`     | 183 of 202 by text    |
| `image_ref` | `Image`    | 114 of 202 by path    |

The 22 `category` misses are entries moved to another tab since. 13 of
them (keys 177 to 202, among them the sharks) are `0` in the workbook and
`2` now, and the octopus and squid rows (12, 133, 141, 151) went from `2`
to `0`. The description misses are rewritten texts. All 88 image misses are
rows whose workbook path is the `Fish_unknown.dds` placeholder; the other
114 differ only in the `Encyclopedia/` folder the client path adds.

The workbook marks `BaseSize`, `VarySize_0` to `_4`, `FishExpType` and
`FishExpRate` with `%`, server only: the client 1784 file writes `0` in
`base_size` and the default roll `1D1+0` in each `vary_sizes`. Client 3473
fills `base_size` again (7 for the Mudskipper, 40 for the Tuna, the workbook
values) and keeps the other server-only columns empty.

The private server's own `encyclopedia.bss` built from that sheet is
byte-identical to the client 1784 file. The field widths and their order
come from the private server's server dump: its `Encyclopedia_Table` loader
reads `TypeKey` and `Type` as u32, `Category` and `Rareness` as u8,
`BaseSize` as u16, `FishExpRate` as 8 bytes and `FishExpType` as u32, and
stores them in that order, the order of the client row. That fixes the
14 bytes at `+0x0C` of client 1784 (2 + 8 + 4) and so the
`fish_exp_rate` and `fish_exp_type` slots, which are `0` in both clients.
The same loader parses each `VarySize_N` string with the pattern
`(d)|(D)|(\+)|(\-)` into three 4-byte values in text order (count, sides,
bonus, negated after a `-`), and turns the string `0` into `1, 1, 0`: the
`1D1+0` of every client row.

Neither the 2016 client with debug symbols nor the server code of a private
server on client 519 has an encyclopedia type; that server's
`Encyclopedia_Table` holds 189 rows with `0` in every server-only column.

## Notes

- The Korean descriptions in the string table use real line breaks. LOC type
  30 has an entry for each of the 302 keys on client 3473, the translated
  description (key 1: "Mudskippers are known for their strong obsession with
  food. ...").
- Each `image_ref` path (`UI_Artwork/Encyclopedia/IC_08501.dds`) is a whole
  texture under `ui_texture/`, lower-cased:
  `ui_texture/ui_artwork/encyclopedia/ic_08501.dds`. All 302 exist on client
  3473. An empty slot of the window shows `fish_undiscover.dds`, which the
  Lua sets itself.
- The window search (`ToClient_SetFishListByKeyword(keyword, category)`),
  the size ranking (`ToClient_RequestFishTopRankingBody(key)`) and My
  Information's Max Size (`getMaxValue()`) and Capture Count (`getCount()`)
  come from the server; no field of this file holds a caught size. Average
  Size (`getAverageValue()`) is a value of the entry, set for caught and
  uncaught fish alike; see Average Size.
- bdo-data-extractor's FORMATS.md lists this file as 300 rows of 104 bytes
  with `id`, `knowledgeCode`, a two-f32 `sizeRange` and two string
  references. There is no knowledge field; the two f32s are `base_size` and
  `unknown_10`.

## Open Questions

### unknown_10

`unknown_10` is a whole-number f32 from 9 to 169 on client 3473, new since
client 1784. On all 202 keys the workbook shares it equals the dice count
times the sides of `VarySize_4` (`3D3+7` gives 9, `13D13+92` gives 169), the
largest roll without its bonus. No sheet column has that value, and the
only client use found is Average Size. The windows of four fish rule out
two readings:

- A size range from `base_size` to `base_size + unknown_10`: the ranking's
  top Mudskipper is 28.507 and its top Tuna 326.866, above 16 and 209.
- An upper bound: `unknown_10` is below `base_size` on 176 of 302 rows
  (client 3474), the Sunfish has 280 and 99.
