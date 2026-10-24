# `lightuserbonus.bss` Format

## Purpose

The light user bonus: by its sheet's column names, bonus items by time
spent disconnected. A PABR list of bonus rows; each row has a key, ten
reward slots of an offline time and a bonus item, and the number of filled
slots. On client 3482 it holds one row, key `1`, with every slot empty and
a filled-slot count of `0`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients       | Checked | File                 | Bytes | Records   | Row bytes |
| ------ | ------------- | ------- | -------------------- | ----- | --------- | --------- |
| 3      | 805 and later | 3483    | `lightuserbonus.bss` | 146   | 10 Reward | 12        |
| 2      | 526 to 794    | 794     | `lightuserbonus.bss` | 130   | 10 Reward | 12        |
| 1      | 435 to 521    | 521     | `lightuserbonus.bss` | 132   | 10 Reward | 12        |

| Layout | File                 | Known          | Unknown    |
| ------ | -------------------- | -------------- | ---------- |
| 3      | `lightuserbonus.bss` | 146 B (100.0%) | 0 B (0.0%) |
| 2      | `lightuserbonus.bss` | 130 B (100.0%) | 0 B (0.0%) |
| 1      | `lightuserbonus.bss` | 130 B (98.5%)  | 2 B (1.5%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3483   | Layout 3 |
| 3482   | Layout 3 |
| 3474   | Layout 3 |
| 3473   | Layout 3 |
| 3464   | Layout 3 |
| 3458   | Layout 3 |
| 3454   | Layout 3 |
| 3444   | Layout 3 |
| 3435   | Layout 3 |
| 3426   | Layout 3 |
| 3418   | Layout 3 |
| 3412   | Layout 3 |
| 3402   | Layout 3 |
| 3396   | Layout 3 |
| 3387   | Layout 3 |
| 3381   | Layout 3 |
| 3373   | Layout 3 |
| 3364   | Layout 3 |
| 3356   | Layout 3 |
| 3349   | Layout 3 |
| 3342   | Layout 3 |
| 3335   | Layout 3 |
| 3326   | Layout 3 |
| 3321   | Layout 3 |
| 3314   | Layout 3 |
| 3303   | Layout 3 |
| 3302   | Layout 3 |
| 3293   | Layout 3 |
| 3283   | Layout 3 |
| 3275   | Layout 3 |
| 3267   | Layout 3 |
| 3258   | Layout 3 |
| 3251   | Layout 3 |
| 3242   | Layout 3 |
| 3235   | Layout 3 |
| 3229   | Layout 3 |
| 3212   | Layout 3 |
| 3203   | Layout 3 |
| 3193   | Layout 3 |
| 3186   | Layout 3 |
| 3177   | Layout 3 |
| 3169   | Layout 3 |
| 3158   | Layout 3 |
| 3151   | Layout 3 |
| 3144   | Layout 3 |
| 3133   | Layout 3 |
| 3125   | Layout 3 |
| 3118   | Layout 3 |
| 3111   | Layout 3 |
| 3103   | Layout 3 |
| 3095   | Layout 3 |
| 3086   | Layout 3 |
| 3072   | Layout 3 |
| 3062   | Layout 3 |
| 3052   | Layout 3 |
| 3045   | Layout 3 |
| 3037   | Layout 3 |
| 3030   | Layout 3 |
| 3021   | Layout 3 |
| 3012   | Layout 3 |
| 3002   | Layout 3 |
| 2995   | Layout 3 |
| 2987   | Layout 3 |
| 2978   | Layout 3 |
| 2970   | Layout 3 |
| 2959   | Layout 3 |
| 2951   | Layout 3 |
| 2942   | Layout 3 |
| 2935   | Layout 3 |
| 2932   | Layout 3 |
| 2923   | Layout 3 |
| 2919   | Layout 3 |
| 2907   | Layout 3 |
| 2900   | Layout 3 |
| 2891   | Layout 3 |
| 2882   | Layout 3 |
| 2872   | Layout 3 |
| 2863   | Layout 3 |
| 2855   | Layout 3 |
| 2849   | Layout 3 |
| 2844   | Layout 3 |
| 2834   | Layout 3 |
| 2825   | Layout 3 |
| 2819   | Layout 3 |
| 2811   | Layout 3 |
| 2803   | Layout 3 |
| 2794   | Layout 3 |
| 2783   | Layout 3 |
| 2774   | Layout 3 |
| 2765   | Layout 3 |
| 2756   | Layout 3 |
| 2750   | Layout 3 |
| 2743   | Layout 3 |
| 2736   | Layout 3 |
| 2726   | Layout 3 |
| 2717   | Layout 3 |
| 2709   | Layout 3 |
| 2703   | Layout 3 |
| 2695   | Layout 3 |
| 2684   | Layout 3 |
| 2672   | Layout 3 |
| 2665   | Layout 3 |
| 2657   | Layout 3 |
| 2649   | Layout 3 |
| 2644   | Layout 3 |
| 2637   | Layout 3 |
| 2629   | Layout 3 |
| 2619   | Layout 3 |
| 2612   | Layout 3 |
| 2606   | Layout 3 |
| 2602   | Layout 3 |
| 2601   | Layout 3 |
| 2592   | Layout 3 |
| 2583   | Layout 3 |
| 2575   | Layout 3 |
| 2567   | Layout 3 |
| 2560   | Layout 3 |
| 2553   | Layout 3 |
| 2545   | Layout 3 |
| 2538   | Layout 3 |
| 2529   | Layout 3 |
| 2519   | Layout 3 |
| 2513   | Layout 3 |
| 2510   | Layout 3 |
| 2507   | Layout 3 |
| 2503   | Layout 3 |
| 2498   | Layout 3 |
| 2492   | Layout 3 |
| 2487   | Layout 3 |
| 2480   | Layout 3 |
| 2474   | Layout 3 |
| 2468   | Layout 3 |
| 2460   | Layout 3 |
| 2453   | Layout 3 |
| 2444   | Layout 3 |
| 2438   | Layout 3 |
| 2434   | Layout 3 |
| 2429   | Layout 3 |
| 2421   | Layout 3 |
| 2414   | Layout 3 |
| 2407   | Layout 3 |
| 2401   | Layout 3 |
| 2397   | Layout 3 |
| 2393   | Layout 3 |
| 2384   | Layout 3 |
| 2378   | Layout 3 |
| 2372   | Layout 3 |
| 2358   | Layout 3 |
| 2352   | Layout 3 |
| 2347   | Layout 3 |
| 2343   | Layout 3 |
| 2335   | Layout 3 |
| 2327   | Layout 3 |
| 2324   | Layout 3 |
| 2319   | Layout 3 |
| 2313   | Layout 3 |
| 2308   | Layout 3 |
| 2302   | Layout 3 |
| 2295   | Layout 3 |
| 2290   | Layout 3 |
| 2284   | Layout 3 |
| 2276   | Layout 3 |
| 2269   | Layout 3 |
| 2259   | Layout 3 |
| 2250   | Layout 3 |
| 2243   | Layout 3 |
| 2235   | Layout 3 |
| 2229   | Layout 3 |
| 2224   | Layout 3 |
| 2218   | Layout 3 |
| 2215   | Layout 3 |
| 2207   | Layout 3 |
| 2203   | Layout 3 |
| 2196   | Layout 3 |
| 2192   | Layout 3 |
| 2189   | Layout 3 |
| 2183   | Layout 3 |
| 2179   | Layout 3 |
| 2171   | Layout 3 |
| 2163   | Layout 3 |
| 2156   | Layout 3 |
| 2151   | Layout 3 |
| 2147   | Layout 3 |
| 2142   | Layout 3 |
| 2138   | Layout 3 |
| 2134   | Layout 3 |
| 2130   | Layout 3 |
| 2122   | Layout 3 |
| 2107   | Layout 3 |
| 2098   | Layout 3 |
| 2089   | Layout 3 |
| 2081   | Layout 3 |
| 2073   | Layout 3 |
| 2067   | Layout 3 |
| 2063   | Layout 3 |
| 2059   | Layout 3 |
| 2052   | Layout 3 |
| 2044   | Layout 3 |
| 2039   | Layout 3 |
| 2032   | Layout 3 |
| 2025   | Layout 3 |
| 2011   | Layout 3 |
| 2005   | Layout 3 |
| 2000   | Layout 3 |
| 1996   | Layout 3 |
| 1991   | Layout 3 |
| 1985   | Layout 3 |
| 1980   | Layout 3 |
| 1969   | Layout 3 |
| 1964   | Layout 3 |
| 1958   | Layout 3 |
| 1950   | Layout 3 |
| 1945   | Layout 3 |
| 1937   | Layout 3 |
| 1933   | Layout 3 |
| 1927   | Layout 3 |
| 1921   | Layout 3 |
| 1914   | Layout 3 |
| 1908   | Layout 3 |
| 1897   | Layout 3 |
| 1892   | Layout 3 |
| 1886   | Layout 3 |
| 1881   | Layout 3 |
| 1871   | Layout 3 |
| 1866   | Layout 3 |
| 1862   | Layout 3 |
| 1854   | Layout 3 |
| 1846   | Layout 3 |
| 1838   | Layout 3 |
| 1832   | Layout 3 |
| 1826   | Layout 3 |
| 1822   | Layout 3 |
| 1818   | Layout 3 |
| 1804   | Layout 3 |
| 1794   | Layout 3 |
| 1790   | Layout 3 |
| 1784   | Layout 3 |
| 1774   | Layout 3 |
| 1771   | Layout 3 |
| 1762   | Layout 3 |
| 1759   | Layout 3 |
| 1754   | Layout 3 |
| 1749   | Layout 3 |
| 1743   | Layout 3 |
| 1737   | Layout 3 |
| 1731   | Layout 3 |
| 1725   | Layout 3 |
| 1717   | Layout 3 |
| 1710   | Layout 3 |
| 1704   | Layout 3 |
| 1698   | Layout 3 |
| 1690   | Layout 3 |
| 1685   | Layout 3 |
| 1680   | Layout 3 |
| 1674   | Layout 3 |
| 1668   | Layout 3 |
| 1659   | Layout 3 |
| 1649   | Layout 3 |
| 1642   | Layout 3 |
| 1636   | Layout 3 |
| 1628   | Layout 3 |
| 1622   | Layout 3 |
| 1614   | Layout 3 |
| 1608   | Layout 3 |
| 1602   | Layout 3 |
| 1598   | Layout 3 |
| 1594   | Layout 3 |
| 1590   | Layout 3 |
| 1587   | Layout 3 |
| 1584   | Layout 3 |
| 1579   | Layout 3 |
| 1572   | Layout 3 |
| 1565   | Layout 3 |
| 1559   | Layout 3 |
| 1554   | Layout 3 |
| 1547   | Layout 3 |
| 1537   | Layout 3 |
| 1529   | Layout 3 |
| 1524   | Layout 3 |
| 1519   | Layout 3 |
| 1509   | Layout 3 |
| 1506   | Layout 3 |
| 1504   | Layout 3 |
| 1500   | Layout 3 |
| 1493   | Layout 3 |
| 1489   | Layout 3 |
| 1485   | Layout 3 |
| 1481   | Layout 3 |
| 1474   | Layout 3 |
| 1466   | Layout 3 |
| 1462   | Layout 3 |
| 1459   | Layout 3 |
| 1453   | Layout 3 |
| 1450   | Layout 3 |
| 1445   | Layout 3 |
| 1439   | Layout 3 |
| 1433   | Layout 3 |
| 1430   | Layout 3 |
| 1426   | Layout 3 |
| 1421   | Layout 3 |
| 1417   | Layout 3 |
| 1416   | Layout 3 |
| 1409   | Layout 3 |
| 1405   | Layout 3 |
| 1401   | Layout 3 |
| 1396   | Layout 3 |
| 1391   | Layout 3 |
| 1390   | Layout 3 |
| 1386   | Layout 3 |
| 1381   | Layout 3 |
| 1379   | Layout 3 |
| 1372   | Layout 3 |
| 1366   | Layout 3 |
| 1364   | Layout 3 |
| 1363   | Layout 3 |
| 1360   | Layout 3 |
| 1358   | Layout 3 |
| 1355   | Layout 3 |
| 1351   | Layout 3 |
| 1348   | Layout 3 |
| 1346   | Layout 3 |
| 1341   | Layout 3 |
| 1340   | Layout 3 |
| 1338   | Layout 3 |
| 1335   | Layout 3 |
| 1333   | Layout 3 |
| 1329   | Layout 3 |
| 1327   | Layout 3 |
| 1324   | Layout 3 |
| 1321   | Layout 3 |
| 1319   | Layout 3 |
| 1318   | Layout 3 |
| 1316   | Layout 3 |
| 1313   | Layout 3 |
| 1311   | Layout 3 |
| 1309   | Layout 3 |
| 1304   | Layout 3 |
| 1292   | Layout 3 |
| 1286   | Layout 3 |
| 1280   | Layout 3 |
| 1276   | Layout 3 |
| 1267   | Layout 3 |
| 1261   | Layout 3 |
| 1256   | Layout 3 |
| 1250   | Layout 3 |
| 1246   | No file  |
| 1239   | No file  |
| 1230   | No file  |
| 1226   | No file  |
| 1220   | No file  |
| 1217   | No file  |
| 1211   | No file  |
| 1210   | No file  |
| 1208   | No file  |
| 1203   | No file  |
| 1197   | No file  |
| 1194   | No file  |
| 1192   | No file  |
| 1187   | No file  |
| 1183   | No file  |
| 1177   | No file  |
| 1173   | No file  |
| 1167   | No file  |
| 1164   | No file  |
| 1156   | No file  |
| 1149   | No file  |
| 1144   | No file  |
| 1137   | No file  |
| 1132   | No file  |
| 1127   | No file  |
| 1122   | No file  |
| 1118   | No file  |
| 1114   | No file  |
| 1109   | No file  |
| 1102   | No file  |
| 1096   | No file  |
| 1088   | No file  |
| 1081   | No file  |
| 1076   | No file  |
| 1069   | No file  |
| 1064   | No file  |
| 1058   | No file  |
| 1051   | No file  |
| 1044   | No file  |
| 1036   | No file  |
| 1026   | No file  |
| 1016   | No file  |
| 1009   | No file  |
| 1005   | No file  |
| 1000   | No file  |
| 998    | No file  |
| 990    | No file  |
| 979    | No file  |
| 972    | No file  |
| 963    | No file  |
| 955    | No file  |
| 946    | No file  |
| 938    | No file  |
| 927    | No file  |
| 911    | No file  |
| 904    | No file  |
| 899    | No file  |
| 894    | No file  |
| 885    | No file  |
| 879    | No file  |
| 872    | No file  |
| 864    | No file  |
| 855    | No file  |
| 853    | No file  |
| 845    | No file  |
| 837    | No file  |
| 829    | Layout 3 |
| 822    | Layout 3 |
| 814    | Layout 3 |
| 805    | Layout 3 |
| 794    | Layout 2 |
| 787    | Layout 2 |
| 780    | Layout 2 |
| 771    | Layout 2 |
| 760    | Layout 2 |
| 748    | Layout 2 |
| 741    | Layout 2 |
| 736    | Layout 2 |
| 731    | Layout 2 |
| 723    | Layout 2 |
| 711    | Layout 2 |
| 707    | Layout 2 |
| 697    | Layout 2 |
| 689    | Layout 2 |
| 683    | Layout 2 |
| 678    | Layout 2 |
| 670    | Layout 2 |
| 661    | Layout 2 |
| 656    | Layout 2 |
| 652    | Layout 2 |
| 643    | Layout 2 |
| 637    | Layout 2 |
| 630    | Layout 2 |
| 627    | Layout 2 |
| 621    | Layout 2 |
| 617    | Layout 2 |
| 615    | Layout 2 |
| 606    | Layout 2 |
| 599    | Layout 2 |
| 592    | Layout 2 |
| 586    | Layout 2 |
| 577    | Layout 2 |
| 569    | Layout 2 |
| 561    | Layout 2 |
| 554    | Layout 2 |
| 542    | Layout 2 |
| 532    | Layout 2 |
| 531    | Layout 2 |
| 526    | Layout 2 |
| 521    | Layout 1 |
| 517    | Layout 1 |
| 510    | Layout 1 |
| 508    | Layout 1 |
| 504    | Layout 1 |
| 497    | Layout 1 |
| 491    | Layout 1 |
| 485    | Layout 1 |
| 478    | Layout 1 |
| 472    | Layout 1 |
| 466    | Layout 1 |
| 457    | Layout 1 |
| 452    | Layout 1 |
| 449    | Layout 1 |
| 435    | Layout 1 |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of bonus rows; `1` on clients 1784 and 3482 |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (126 bytes)

| Offset  | Type        | Field              | Notes                                         |
| ------- | ----------- | ------------------ | --------------------------------------------- |
| `+0x00` | u16         | key                | Row key; `1`                                  |
| `+0x02` | Reward[10]  | rewards            | See Reward; slot N is `DisConnectedTimeN` and `BonusN` |
| `+0x7A` | u32         | valid_reward_count | Number of filled slots; `0`                   |

### Reward (12 bytes)

| Offset  | Type | Field             | Notes                                          |
| ------- | ---- | ----------------- | ---------------------------------------------- |
| `+0x00` | i64  | disconnected_time | Time offline that earns the slot; `0` (empty)  |
| `+0x08` | u32  | bonus             | Item enchant key of the bonus item; `0` (empty) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 2

The file has no PABR magic, string table or trailer; the rows are the
Layout 3 rows.

### File Layout

| Offset  | Type           | Field     | Notes                |
| ------- | -------------- | --------- | -------------------- |
| `+0x00` | u32            | row_count | Number of bonus rows |
| `+0x04` | Row[row_count] | rows      | See Row              |

## Layout 1

### Row (128 bytes)

| Offset  | Type       | Field              | Notes                                |
| ------- | ---------- | ------------------ | ------------------------------------ |
| `+0x00` | u16        | key                | Row key; `1`                         |
| `+0x02` | u16        | unknown_after_key  | `1` on client 521                    |
| `+0x04` | Reward[10] | rewards            | Same as Layout 3                     |
| `+0x7C` | u32        | valid_reward_count | `0`                                  |

## Field Names

The `LightUserBonus_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `Key`, then `DisConnectedTime1` and
`Bonus1` to `DisConnectedTime10` and `Bonus10`, and one row: key `1`
with every other column `<null>`. The client 1784 file holds that row, key
`1` and 124 zero bytes. The 2016 `gc::LightUserBonusStaticStatus` gives the
split of those bytes: a `KeyType<unsigned short>` `_key`, a
`pa::Array<gc::LightUserBonusReward,10>` `_reward` and an int
`_validRewardCount`, and each `gc::LightUserBonusReward` is an `__int64`
`_disconnectedTime` and a `gc::ItemEnchantKey` `_itemKey`. A u16, ten
12-byte slots and a u32 add up to the 126-byte row exactly. The slot
fields take the sheet's names, `valid_reward_count` the 2016 member's.

## Notes

- Every value but the key is `0` on clients 1784 and 3482, so the names
  rest on the sheet's column order and the 2016 struct, not on values.
- Layout 1 holds a u16 `1` between the key and the slots; the 2016 struct
  has only alignment there, so `unknown_after_key` stays unnamed.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/server_tables.py`; its
  Rewards cell lists only filled slots as `disconnected_time: bonus`.

## Open Questions

### The Unit of `disconnected_time`

No slot is filled on clients 521, 794, 1784 and 3482, and the client Lua
does not name the table, so whether `disconnected_time` counts seconds,
minutes or hours is open.
