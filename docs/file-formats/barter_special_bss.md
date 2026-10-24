# `barter_special.bss` Format

## Purpose

The special barter offers of the Great Ocean barters: one row per offer,
with the item the player hands over, the item the player gets and their
count ranges. The special barter window
(`panel_window_barterinfosearch_special_1.luac`) opens only for a player
with the Value Pack (`isApplyChargeSkill(__eUserChargeType_PremiumPackage)`)
and shows one offer from `ToClient_specialBarterWrapper()`: its from item
and count, its to item and count, and the region and NPC where it can be
traded, which the wrapper gives at run time.

On client 3474 the 105 rows hand over Gold Bars (`3` to `5`) or
`[Level 4]` trade items (`800043` to `800056`) and give Crow Coins (`10`),
Manos accessories, Vell's and Khan's Concentrated Magic, Garmoth's Heart,
crystals, Sethra's Artifacts and other items.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                 | Bytes | Records               | Row bytes |
| ------ | -------------- | ------- | -------------------- | ----- | --------------------- | --------- |
| 3      | 1109 and later | 3483    | `barter_special.bss` | 7,370 | 105 Exchange, 105 Row | 56        |
| 2      | 1261 to 2855   | 2855    | `barter_special.bss` | 8,194 | 122 Exchange, 122 Row | 56        |
| 1      | 1304 to 1685   | 1685    | `barter_special.bss` | 9,788 | 148 Exchange, 148 Row | 56        |

| Layout | File                 | Known            | Unknown    |
| ------ | -------------------- | ---------------- | ---------- |
| 3      | `barter_special.bss` | 7,370 B (100.0%) | 0 B (0.0%) |
| 2      | `barter_special.bss` | 8,194 B (100.0%) | 0 B (0.0%) |
| 1      | `barter_special.bss` | 9,788 B (100.0%) | 0 B (0.0%) |

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
| 1292   | Layout 2             |
| 1286   | Layout 2             |
| 1280   | Layout 2             |
| 1276   | Layout 2             |
| 1267   | Layout 2             |
| 1261   | Layout 2             |
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
| 1127   | Layout 3             |
| 1122   | Layout 3             |
| 1118   | Layout 3             |
| 1114   | Layout 3             |
| 1109   | Layout 3             |
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

| File                 | Required | Role                     |
| -------------------- | -------- | ------------------------ |
| `languagedata_*.loc` | Optional | Item names (type 0)      |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset              | Type           | Field              | Notes                                                   |
| ------------------- | -------------- | ------------------ | ------------------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                            |
| `+0x04`             | u32            | row_count          | Number of `rows`; `105` on client 3474                  |
| `+0x08`             | Row[row_count] | rows               | See Row                                                 |
| `rows+0x00`         | String Table   | string_table       | The PABR string table, present but empty                |
| `string_table+0x00` | u32            | string_table_start | Absolute offset of `string_count`; equals `8 + 70 × row_count` |
| `string_table+0x04` | u32            | zero               | Always `0`                                              |

### Row (70 bytes)

The Entry of [`barter_normal.bss`](barter_normal_bss.md) has the same
layout; see Field Names for the three fields that are `0` here.

| Offset  | Type     | Field             | Notes                                                       |
| ------- | -------- | ----------------- | ----------------------------------------------------------- |
| `+0x00` | u16      | barter_region_key | `0` on every row (clients 1784 and 3474)                    |
| `+0x02` | u32      | select_rate       | `0` on every row (clients 1784 and 3474)                    |
| `+0x06` | Exchange | exchange          | See Exchange                                                |
| `+0x3e` | u32      | barter_sub_group  | `0` on every row (clients 1784 and 3474)                    |
| `+0x42` | u32      | barter_category   | Bit mask as in `bartersubgroup.bss`; `0` on every row (client 3474) |

### Exchange (56 bytes)

Same structure as the Exchange of
[`bartersubgroup.bss`](bartersubgroup_bss.md#exchange-56-bytes).

| Offset  | Type | Field              | Notes                                                              |
| ------- | ---- | ------------------ | ------------------------------------------------------------------ |
| `+0x00` | u32  | from_item_key      | The item the player hands over, `enchant_level << 24 \| item_id`; level `0` on every row (client 3474) |
| `+0x04` | u64  | from_min_count     | `1` to `10` (client 3474)                                          |
| `+0x0c` | u64  | from_max_count     | `1` to `10` (client 3474)                                          |
| `+0x14` | u32  | to_item_key        | The item the player gets; 20 rows give an enhanced item (client 3474) |
| `+0x18` | u64  | to_min_count       | `1` to `10000` (client 3474)                                       |
| `+0x20` | u64  | to_max_count       | `1` to `10000` (client 3474)                                       |
| `+0x28` | u32  | barter_need_point  | `0` on every row (clients 1784 and 3474)                           |
| `+0x2c` | u32  | exchange_max_count | `1` on every row (clients 1784 and 3474)                           |
| `+0x30` | u32  | exchange_min       | `1` on every row (client 3474), `15000` (client 1784)              |
| `+0x34` | u32  | exchange_max       | `1000000` on every row (client 3474)                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 2

### Row (67 bytes)

| Offset  | Type     | Field             | Notes                                              |
| ------- | -------- | ----------------- | -------------------------------------------------- |
| `+0x00` | u16      | barter_region_key |                                                    |
| `+0x02` | u32      | select_rate       |                                                    |
| `+0x06` | Exchange | exchange          |                                                    |
| `+0x3e` | u32      | barter_sub_group  |                                                    |
| `+0x42` | u8       | barter_category   | The category number; `8` on every row (client 1784), as on the material entries of `bartersubgroup.bss`, whose sheet has no category column either |

## Layout 1

The row ends after `barter_sub_group`: there is no `barter_category`.

### Row (66 bytes)

| Offset  | Type     | Field             | Notes |
| ------- | -------- | ----------------- | ----- |
| `+0x00` | u16      | barter_region_key |       |
| `+0x02` | u32      | select_rate       |       |
| `+0x06` | Exchange | exchange          |       |
| `+0x3e` | u32      | barter_sub_group  |       |

## Field Names

The row is the `SpecialBarterData` sheet of a private server's
`DataSheets.bexcel` on client 1784. The client 1784 file holds the 148
sheet rows in sheet order, and these columns match on all 148:
`SelectRate`, `GivedItemKey` with `GivedEnchantLevel` (one packed key),
`GivedMinCount`, `GivedMaxCount`, `TakedItemKey` with `TakedEnchantLevel`,
`TakedMinCount`, `TakedMaxCount`, `ExchangeMin` and `ExchangeMax`. The
sheet's `SpecialBarterIndex` (`1` to `148` in row order) is not stored;
`ContentsGroup` and `TradeEmployeeExp` are not in the file. The Exchange
field names and the `from` and `to` naming are explained in
[`bartersubgroup.bss`](bartersubgroup_bss.md#field-names).

The sheet has no column for `barter_region_key`, `barter_sub_group`,
`barter_category`, `barter_need_point` or `exchange_max_count`. The last two
are Exchange fields and take their names from `bartersubgroup.bss`. The
other three are named after the same slots of
[`barter_normal.bss`](barter_normal_bss.md#field-names), whose entries are
this 70-byte row (67 bytes on client 1784) grouped by region:

- `barter_region_key`: in `barter_normal.bss` the u16 equals the key of the
  region the entry sits in, on all 3,640 + 3,731 entries of client 3474.
- `barter_sub_group`: its values in `barter_normal.bss` are the
  `bartersubgroup.bss` keys, `1` to `197` in the trade item list and `1`
  to `5` in the material list (client 3474), and on client 1784 it matches
  the `BarterSubGroup` column of the `BarterData` and `MaterialBarterData`
  sheets on all 3,240 + 3,321 rows.
- `barter_category`: on client 1784 it matches the `BarterCategory` column
  of the `BarterData` sheet on the 2,958 rows without a sub group; on
  client 3474 it is the bit mask of
  [Barter Categories](bartersubgroup_bss.md#barter-categories).

## Notes

- The special barter window reads the region with
  `specialBarterWrapper:getRegionKey()`, but `barter_region_key` is `0` on
  every row, so the region is not taken from this file.
- The handler (`_bss/barter_special/`) shows one row per offer with its
  place in the file as the index, from `1`, the way the 1784 sheet
  numbers its rows. It reads the Exchange with the shared barter reader in
  `_bss/barter/`.
