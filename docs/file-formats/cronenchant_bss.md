# `cronenchant.bss` Format

## Purpose

The Caphras enhancement table: for each gear category and each of TRI, TET
and PEN, the 20 Caphras levels with the total Caphras Stones needed to reach
the level and the stat bonus the item has at that level.

The file name is the system's old name. The KR patch that added Caphras
Stones replaced the "Cron Energy" system with Caphras enhancement
([Inven Global](https://www.invenglobal.com/blackdesertonline/articles/4822/100-pen-is-not-going-to-be-that-easy-the-caphras-stone-and-caphras-enhancement-added-in-kr)),
and the client still calls it cron enchant: `panel_tooltip_item.luac` reads
the item's level with `ToClient_GetCronEnchantWrapper` and labels it with
`LUA_TOOLTIP_CRONENCHANTGRADE_CAPHRAS`.

Cron Stones are a separate item that is still in the game: they protect an
item from downgrading when an enhancement attempt fails. This file does not
hold their counts; the client reads those through
`ToClient_GetCronStoneStaticStatus`, from a table I have not found yet (see
[enchantstaticstatus.dbss](enchantstaticstatus_dbss.md), Notes).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File              | Bytes  | Records                                     | Row bytes |
| ------ | ------------- | ------- | ----------------- | ------ | ------------------------------------------- | --------- |
| 1      | 805 and later | 3483    | `cronenchant.bss` | 23,580 | 600 Step, 30 Grade Block, 10 Category Block | 39        |

| Layout | File              | Known             | Unknown    |
| ------ | ----------------- | ----------------- | ---------- |
| 1      | `cronenchant.bss` | 23,580 B (100.0%) | 0 B (0.0%) |

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

None. All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                            | Field              | Notes                                                    |
| ------------------- | ------------------------------- | ------------------ | -------------------------------------------------------- |
| `+0x00`             | char[4]                         | magic              | `PABR` (ASCII)                                           |
| `+0x04`             | u32                             | category_count     | `10` on client 3464                                      |
| `+0x08`             | Category Block[category_count]  | categories         | See Category Block                                       |
| `categories+0x00`   | String Table                    | string_table       | The PABR string table, present but empty                 |
| `string_table+0x00` | u32                             | string_table_start | Absolute offset of `string_count`, where the categories end |
| `string_table+0x04` | u32                             | zero               | Always `0`                                               |

On client 3464 the file is `8 + 10 × (4 + 3 × (4 + 20 × 39)) + 12 = 23,580`
bytes. The parser rejects a file whose categories do not end exactly at
`string_table_start`.

### Category Block (variable: 4 bytes + grade blocks)

| Offset  | Type                     | Field       | Notes                                     |
| ------- | ------------------------ | ----------- | ----------------------------------------- |
| `+0x00` | u32                      | grade_count | `3` in every category (TRI, TET and PEN)  |
| `+0x04` | Grade Block[grade_count] | grades      | See Grade Block                           |

### Grade Block (variable: 4 bytes + steps)

| Offset  | Type             | Field      | Notes                                    |
| ------- | ---------------- | ---------- | ---------------------------------------- |
| `+0x00` | u32              | step_count | `20` in every grade, one per Caphras level |
| `+0x04` | Step[step_count] | steps      | See Step; byte-packed                    |

### Step (39 bytes)

| Offset  | Type | Field                   | Notes |
| ------- | ---- | ----------------------- | ----- |
| `+0x00` | u16  | category                | The category key, `1` to `10`; the same on every step of a category block |
| `+0x02` | u8   | enchant_level           | Item enhancement level the step applies to: `18` TRI, `19` TET, `20` PEN |
| `+0x03` | u32  | total_stones            | Caphras Stones from level 0 to this level; rises on every step |
| `+0x07` | f32  | ap                      | AP bonus at this level |
| `+0x0B` | f32  | accuracy                | |
| `+0x0F` | f32  | evasion                 | |
| `+0x13` | f32  | hidden_evasion          | |
| `+0x17` | f32  | damage_reduction        | |
| `+0x1B` | f32  | hidden_damage_reduction | |
| `+0x1F` | f32  | hp                      | Max HP bonus |
| `+0x23` | u32  | mp                      | Max MP (and other resource) bonus; an integer, unlike the other stats |

The Caphras level is not stored: it is the step's position in its grade
block, 1 to 20. The stats are the totals at that level, not the gain from
the previous one (category 1 at TRI: AP 1, 2, 3, 4, 4, 4, 4, 5, ...). The
stones for one level are `total_stones` minus the previous step's.

The eight stats follow the order of the tooltip keys in
`panel_tooltip_item.luac`: `LUA_TOOLTIP_CRONENCHANT_ATTACK`, `_HIT`,
`_DODGE`, `_DODGEB`, `_REDUCE`, `_REDUCEB`, `_HP`, `_MP`. Every f32 holds a
whole number on client 3464, and `mp` is `0` to `30` in steps of 5.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Categories

The file has no names for the categories, and I have not found the field
that gives an item its category, see Open Questions. The names come from the
Caphras sheets on [grumpygreen.cricket](https://grumpygreen.cricket/caphras-sheet/)
(PEN totals and stats) and its
[TRI page](https://grumpygreen.cricket/caphras-sheet-tri/) (per-level costs,
2021-06-01), and from bdocodex item pages at TRI with Caphras 20/20
(2026-10-11) where the sheet is out of date.

TRI columns are the stones for one level, as the TRI sheet lists them; the
TET and PEN columns are totals to level 20. All from client 3464.

| Key | Gear                  | TRI level 1 | TRI level 20 | TET total | PEN total | Checked against |
| --: | --------------------- | ----------: | -----------: | --------: | --------: | ----- |
| 1   | Boss main weapon      | 20 | 105 | 15,378 | 29,403 | Sheet: boss main weapon: TRI 20 / 105, PEN total 29,403 |
| 2   | Boss awakening weapon | 20 | 105 | 15,378 | 29,403 | bdocodex: [Dandelion Lancia](https://bdocodex.com/us/item/14752/) TRI 20/20 is AP 8, accuracy 12, 1,590 stones in total (the sheet lists TRI 24 / 128) |
| 3   | Blue weapon           | 12 | 118 | 10,763 | 20,964 | Sheet: blue main and awakening weapon: TRI 16 / 118 |
| 4   | Green weapon          | 4  | 59  | 3,990  | 9,615  | bdocodex: [Yuria Longsword](https://bdocodex.com/us/item/10014/) TRI 20/20 is AP 8, accuracy 12, 494 stones in total; the sheet lists green awakening weapons as TRI 4 / 59 and green main weapons as TRI 4 / 39 |
| 5   | Boss sub-weapon       | 20 | 105 | 15,378 | 29,403 | Sheet: boss and Fiery sub-weapon: TRI 20 / 105, PEN total 29,403 |
| 6   | Green sub-weapon      | 4  | 59  | 3,990  | 9,615  | Sheet: green sub-weapon: TRI 4 / 59, PEN total 9,615 |
| 7   | Boss armor            | 19 | 103 | 9,729  | 21,744 | Sheet: boss armor: TRI 19 / 103, PEN total 21,744 |
| 8   | Dim Tree armor        | 19 | 103 | 9,729  | 21,744 | bdocodex: [Dim Tree Spirit's Armor](https://bdocodex.com/us/item/11017/) TRI 20/20 is evasion 3 (+8), damage reduction 1 (+3), HP 80, MP 30, 1,483 stones in total (the sheet lists TRI 22 / 116) |
| 9   | Blue armor            | 6  | 40  | 3,630  | 10,104 | Sheet: blue armor: TRI 6 / 40 |
| 10  | Green armor           | 3  | 30  | 1,950  | 6,612  | Sheet: green armor: TRI 3 / 30, PEN total 6,612 |

The stats of every category match the sheet's gear of that kind. Categories
1, 5, 6, 7, 9 and 10 match the sheet's costs exactly. Category 4 holds both
green main and green awakening weapons: Yuria Longsword, a main weapon,
costs the sheet's green awakening values. Categories
1 and 2 are identical in every step, and so are 7 and 8: the boss awakening
weapon and Dim Tree armor now cost what the boss main weapon and boss armor
do, while the 2021 sheet still lists them higher.

Stats at Caphras level 20 per stat group (client 3464):

| Categories | Grade    | AP | Accuracy | Evasion | Hidden evasion | DR | Hidden DR | HP  | MP |
| ---------- | -------- | -: | -------: | ------: | -------------: | -: | --------: | --: | -: |
| 1 to 4     | TRI, TET | 8  | 12       | 0       | 0              | 0  | 0         | 0   | 0  |
| 1 to 4     | PEN      | 10 | 12       | 0       | 0              | 0  | 0         | 0   | 0  |
| 5, 6       | TRI, TET | 2  | 8        | 1       | 5              | 0  | 2         | 30  | 25 |
| 5, 6       | PEN      | 2  | 12       | 3       | 9              | 3  | 3         | 60  | 0  |
| 7 to 10    | TRI, TET | 0  | 0        | 3       | 8              | 1  | 3         | 80  | 30 |
| 7, 8       | PEN      | 0  | 0        | 8       | 8              | 8  | 8         | 160 | 0  |
| 9, 10      | PEN      | 0  | 0        | 5       | 5              | 5  | 5         | 100 | 0  |

## Notes

- How the client reads the file (`panel_tooltip_item.luac`, decompiled with
  unluac): `ToClient_GetCronEnchnatInfoCount(cronKey, enchantLevel)` is the
  step count of one grade block, and
  `ToClient_GetCronEnchantWrapper(cronKey, enchantLevel, index):getCount()`
  is that step's `total_stones`. The item itself stores only the stones put
  into it (`getCronEnchantFailCount()`); its Caphras level is the number of
  steps whose `total_stones` is at most that count. The stat bonus in the
  tooltip comes from the item (`getAddedDD()`, `getCronHDV()`,
  `getCronHPV()`, ...), not from this file directly.
- The enhancement window asks for the next and current step with
  `ToClient_GetNextLevelCronEnchantForLua` and
  `ToClient_GetCurrentLevelCronEnchantForLua`
  (`panel_widget_enchant_main_all_1.luac`).
- Caphras costs change with patches: the 2019-03-20 KR patch cut the stones
  for PEN gear by 25%
  ([Inven Global](https://www.invenglobal.com/articles/7846/bdo-kr-patch-notes-march-20th-new-areaitems-added-devour-and-caphras-enhancement-improved)),
  so the totals above are a snapshot of client 3464.
- bdocodex writes a hidden stat in brackets after the visible one:
  "Evasion: 3 (+8)" is `evasion` 3 and `hidden_evasion` 8.
- No category has blue sub-weapon costs or stats of its own; they share a
  category with other gear, but which one is not in this file.

## Open Questions

### Item to Category Link

The tooltip reads the category with `itemSSW:getCronKey()`, on the static
status of the item at its enhancement level (`panel_tooltip_item.luac`),
and passes it straight to `ToClient_GetCronEnchantWrapper` with that
level. The static status is what `itemenchant.dbss` holds, but the key is
not stored there as a plain byte: a byte-level diff of Liverto Longsword (3)
against Yuria Longsword (4) and of Lemoria Helmet (9) against Grunil Helmet
(10) at TRI finds no byte that holds the two categories at matching
positions. A byte scan found no field that holds the
expected key for Kzarka Longsword (1), Liverto Longsword (3), Yuria Longsword
(4), Kutum Shield (5), Griffon's Helmet (7), Dim Tree Spirit's Armor (8) and
Grunil Helmet (10): not at any offset from the block start, the block end or
the icon string end of their `itemenchant.dbss` blocks (levels 0 and 18), nor
from the start or end of their `enchantstaticstatus.dbss` blocks (levels 0
and 17 to 20), nor at a fixed offset in their `itemenchantbackend.dbss`
blocks. A second scan over all 772 tables in `gamecommondata/binary`
(client 3464) looked within 512 bytes of each sample's item ID, TRI item key
and enchant key, as u16 and u32, for a byte that holds the category for
every sample; none does. The scans also catch the low byte of a u16 or u32,
so the item side either stores other values that the client maps to these
keys, or the client works the category out from other item fields. Grade
plus gear type (main, awakening, sub-weapon, armor) would explain every
sample except Dim Tree armor, which has a key of its own. Until the link is found, the table cannot list the items
per category.
