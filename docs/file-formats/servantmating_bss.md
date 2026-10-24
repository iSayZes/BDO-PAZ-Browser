# `servantmating.bss` Format

## Purpose

Horse breeding grade table: one row per band of the parents' average grade,
with the lowest and highest grade a foal of that band can get. Client 3474
adds the Imperial Steed and the band's chance to breed it (Breeding
Results). On client 3474 the file has 34 rows, keys 1 to 36 without 29 and
30.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | -------------------------- | ----- | ------------- | --------- |
| 2      | 2794 and later | 3483    | `servantmating.bss`        | 684   | 34 Row        | 20        |
| 1      | 435 to 794     | 794     | `servantmating.bss`        | 298   | 21 Row        | 14        |
| 1      | 1346 to 2460   | 2460    | `servantmating.dbss`       | 340   | 24 Row        | 14        |
| 1      | 1346 to 2460   | 2460    | `servantmatingoffset.dbss` | 292   | 24 Offset Row | 12        |

| Layout | File                       | Known          | Unknown    |
| ------ | -------------------------- | -------------- | ---------- |
| 2      | `servantmating.bss`        | 684 B (100.0%) | 0 B (0.0%) |
| 1      | `servantmating.bss`        | 298 B (100.0%) | 0 B (0.0%) |
| 1      | `servantmating.dbss`       | 340 B (100.0%) | 0 B (0.0%) |
| 1      | `servantmatingoffset.dbss` | 292 B (100.0%) | 0 B (0.0%) |

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
| 794    | Layout 1             |
| 787    | Layout 1             |
| 780    | Layout 1             |
| 771    | Layout 1             |
| 760    | Layout 1             |
| 748    | Layout 1             |
| 741    | Layout 1             |
| 736    | Layout 1             |
| 731    | Layout 1             |
| 723    | Layout 1             |
| 711    | Layout 1             |
| 707    | Layout 1             |
| 697    | Layout 1             |
| 689    | Layout 1             |
| 683    | Layout 1             |
| 678    | Layout 1             |
| 670    | Layout 1             |
| 661    | Layout 1             |
| 656    | Layout 1             |
| 652    | Layout 1             |
| 643    | Layout 1             |
| 637    | Layout 1             |
| 630    | Layout 1             |
| 627    | Layout 1             |
| 621    | Layout 1             |
| 617    | Layout 1             |
| 615    | Layout 1             |
| 606    | Layout 1             |
| 599    | Layout 1             |
| 592    | Layout 1             |
| 586    | Layout 1             |
| 577    | Layout 1             |
| 569    | Layout 1             |
| 561    | Layout 1             |
| 554    | Layout 1             |
| 542    | Layout 1             |
| 532    | Layout 1             |
| 531    | Layout 1             |
| 526    | Layout 1             |
| 521    | Layout 1             |
| 517    | Layout 1             |
| 510    | Layout 1             |
| 508    | Layout 1             |
| 504    | Layout 1             |
| 497    | Layout 1             |
| 491    | Layout 1             |
| 485    | Layout 1             |
| 478    | Layout 1             |
| 472    | Layout 1             |
| 466    | Layout 1             |
| 457    | Layout 1             |
| 452    | Layout 1             |
| 449    | Layout 1             |
| 435    | Layout 1             |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role |
| ---------------------------- | -------- | ---- |
| `languagedata_en.loc`        | Optional | The Imperial Steed's name (LOC type 6, `str_id1` = `imperial_steed_character_id`) |
| `characterstaticoffset.dbss` | Optional | Every `characterstatic.dbss` key, so an `imperial_steed_character_id` without a row shows as plain text instead of a link |

Client 1784 ships the table as `servantmating.dbss` with the index
`servantmatingoffset.dbss` (Layout 1).

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                   |
| ------- | ---------- | ----- | --------------------------------------- |
| `+0x00` | u32        | count | 34 on client 3474                       |
| `+0x04` | Row[count] | rows  | `count` rows of 20 bytes, ending at EOF |

### Row (20 bytes)

| Offset  | Type | Field            | Notes |
| ------- | ---- | ---------------- | ----- |
| `+0x00` | u32  | key              | Band index; not in key order (36 to 32, 15 to 1, 31 to 16 on client 3474) |
| `+0x04` | u32  | key_dup          | Equals `key` on every row |
| `+0x08` | u16  | average_grade    | Lower end of the band: 0 to 1,150 in steps of 50 for keys 1 to 24, then 1,160 to 1,250 in steps of 10 (client 3474) |
| `+0x0A` | u16  | result_max_grade | 520 to 660 on client 3474 |
| `+0x0C` | u16  | result_min_grade | 460 to 615 on client 3474 |
| `+0x0E` | u16  | imperial_steed_character_id | 31594 on every row (client 3474), the Imperial Steed in `servant.bss` |
| `+0x10` | u32  | imperial_steed_rate | Millionths: 1,600 (0.16%) to 70,000 (7%), rising with `average_grade` (client 3474) |

## Layout 1

### `servantmating.dbss`

| Offset  | Type       | Field | Notes                                   |
| ------- | ---------- | ----- | --------------------------------------- |
| `+0x00` | u32        | count | 24 on client 1784                       |
| `+0x04` | Row[count] | rows  | `count` rows of 14 bytes, ending at EOF |

### Row (14 bytes)

| Offset  | Type | Field            | Notes |
| ------- | ---- | ---------------- | ----- |
| `+0x00` | u32  | key              | 15 down to 1, then 24 down to 16 |
| `+0x04` | u32  | key_dup          | Equals `key` on every row |
| `+0x08` | u16  | average_grade    | |
| `+0x0A` | u16  | result_max_grade | |
| `+0x0C` | u16  | result_min_grade | |

### `servantmatingoffset.dbss`

| Offset  | Type              | Field   | Notes                           |
| ------- | ----------------- | ------- | ------------------------------- |
| `+0x00` | u32               | count   | Equals the `servantmating.dbss` count |
| `+0x04` | Offset Row[count] | entries | `count` entries of 12 bytes     |

### Offset Row (12 bytes)

| Offset  | Type | Field  | Notes                                               |
| ------- | ---- | ------ | --------------------------------------------------- |
| `+0x00` | u32  | key    | The row's `key`                                     |
| `+0x04` | u32  | offset | Where the row's `key_dup` starts, 4 bytes into the row |
| `+0x08` | u32  | size   | 10 on every entry: the row from `key_dup` on        |

## Breeding Results

Checked in game on client 3474 (2026-10-20) in the Horse Growth Info
Breed/Exchange Calculator with a tier 8 mare of grade 650 (9890) and a
stallion that puts the pair in band key 12 (`average_grade` 550,
`result_min_grade` 462, `result_max_grade` 535, `imperial_steed_rate`
3,200, the only band with that rate):

- The result grid holds 40 horses in pairs of 2.037% (mare) and 2.963%
  (stallion). `servant.bss` has exactly 40 breeding-result horses
  (`is_mating_result` 1) with a `grade` from 462 to 535: 20 tier 6 mares
  and 20 tier 6 stallions, at grades 490 and 520.
- Under the heading Imperial Steed it shows one mare at 0.32%: 3,200
  millionths, `imperial_steed_rate` of the band. 31594 is a mare
  (`is_male` 0); the calculators' horse list shows it with 31565 under the
  same heading.

The 40 pair chances add up to 100% without the Imperial Steed's 0.32%. How
the client splits mare and stallion chances (40.74% to 59.26% of each
pair here) is not in this file.

## Field Names

The names follow the `ServantMating_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (24 rows, `Index`, `AverageGrade`,
`ResultMinGrade`, `ResultMaxGrade`), matched value by value:

| Column | Field | Equal (client 1784) | Equal (client 3474) |
| ------ | ----- | ------------------- | ------------------- |
| `Index` | `key` | 24 of 24 | 24 of 24 |
| `AverageGrade` | `average_grade` | 24 | 24 |
| `ResultMaxGrade` | `result_max_grade` | 24 | 10 |
| `ResultMinGrade` | `result_min_grade` | 24 | 8 |

The client 3474 misses are rebalances: band 15 (average 700) gives 468 to
600 against 435 to 600 on client 1784, and keys 1 to 11 all give 460 to 520
where client 1784 starts at 155 to 166. The 2016 `gc::ServantMatingStaticStatus`
holds `_key`, `_grade`, `_gradeByMin` and `_gradeByMax`; the file stores the
maximum before the minimum. The sheet has no column for
`imperial_steed_character_id` and `imperial_steed_rate`; their names come
from the in-game check in Breeding Results.
