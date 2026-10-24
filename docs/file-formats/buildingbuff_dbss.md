# `buildingbuff.dbss` Format

## Purpose

The villa buffs a player buys with silver in the villa buff window
(`Panel_Window_BuildingBuff_All`, `panel_window_camp_villabuff_all_1.luac`).
Each row is one skill, `[Villa] Turning Gates (60 min)` for example, and its
silver cost. The rows sit in four lists; list `i` holds the rows whose
`Count_Villa` is `i + 1`, and only the first list has rows. Companion
`buildingbuffoffset.dbss` lists where every row sits.

On client 3474 the 10 rows are two buffs at five durations each:

| Skill                      | 60 min    | 90 min    | 120 min   | 180 min   | 300 min    |
| -------------------------- | --------- | --------- | --------- | --------- | ---------- |
| `[Villa] Turning Gates`    | 200,000   | 300,000   | 450,000   | 900,000   | 2,000,000  |
| `[Villa] Body Enhancement` | 1,000,000 | 1,500,000 | 2,250,000 | 4,500,000 | 10,000,000 |

Skill numbers in the same order: Turning Gates `55744`, `53657`, `55747`,
`53660`, `52906`; Body Enhancement `55746`, `53659`, `55749`, `53662`,
`52908`. LOC type 10 gives Turning Gates "Energy Recovery +1, Amity +10%,
Life EXP +10%" and Body Enhancement "All AP +10, All Damage Reduction +10,
Max HP +200, ...". Client 1784 has 12 rows: the 60 to 180 minute rows of both buffs
and a third buff, `[Villa] Skill and Experience` (`55745`, `53658`,
`55748`, `53661`), which client 3474 names "- Not in Use" and no longer
lists.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records                      | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | ---------------------------- | --------- |
| 1      | 1346 and later | 3483    | `buildingbuff.dbss`       | 140   | 10 Row, 4 Villa List         | 12        |
| 1      | 1346 and later | 3483    | `buildingbuffoffset.dbss` | 120   | 10 Offset Row, 4 Offset List | 10        |

| Layout | File                      | Known          | Unknown    |
| ------ | ------------------------- | -------------- | ---------- |
| 1      | `buildingbuff.dbss`       | 140 B (100.0%) | 0 B (0.0%) |
| 1      | `buildingbuffoffset.dbss` | 120 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `beb461f94ae4`  |
| 3482   | Layout 1             | `beb461f94ae4`  |
| 3474   | Layout 1             | `beb461f94ae4`  |
| 3473   | Layout 1             | `beb461f94ae4`  |
| 3464   | Layout 1             | `beb461f94ae4`  |
| 3458   | Layout 1             | `beb461f94ae4`  |
| 3454   | Layout 1             | `beb461f94ae4`  |
| 3444   | Layout 1             | `beb461f94ae4`  |
| 3435   | Layout 1             | `beb461f94ae4`  |
| 3426   | Layout 1             | `beb461f94ae4`  |
| 3418   | Layout 1             | `beb461f94ae4`  |
| 3412   | Layout 1             | `beb461f94ae4`  |
| 3402   | Layout 1             | `beb461f94ae4`  |
| 3396   | Layout 1             | `beb461f94ae4`  |
| 3387   | Layout 1             | `beb461f94ae4`  |
| 3381   | Layout 1             | `beb461f94ae4`  |
| 3373   | Layout 1             | `beb461f94ae4`  |
| 3364   | Layout 1             | `beb461f94ae4`  |
| 3356   | Layout 1             | `beb461f94ae4`  |
| 3349   | Layout 1             | `beb461f94ae4`  |
| 3342   | Layout 1             | `beb461f94ae4`  |
| 3335   | Layout 1             | `beb461f94ae4`  |
| 3326   | Layout 1             | `beb461f94ae4`  |
| 3321   | Layout 1             | `beb461f94ae4`  |
| 3314   | Layout 1             | `beb461f94ae4`  |
| 3303   | Layout 1             | `beb461f94ae4`  |
| 3302   | Layout 1             | `beb461f94ae4`  |
| 3293   | Layout 1             | `beb461f94ae4`  |
| 3283   | Layout 1             | `beb461f94ae4`  |
| 3275   | Layout 1             | `beb461f94ae4`  |
| 3267   | Layout 1             | `beb461f94ae4`  |
| 3258   | Layout 1             | `beb461f94ae4`  |
| 3251   | Layout 1             | `beb461f94ae4`  |
| 3242   | Layout 1             | `beb461f94ae4`  |
| 3235   | Layout 1             | `beb461f94ae4`  |
| 3229   | Layout 1             | `beb461f94ae4`  |
| 3212   | Layout 1             | `beb461f94ae4`  |
| 3203   | Layout 1             | `beb461f94ae4`  |
| 3193   | Layout 1             | `beb461f94ae4`  |
| 3186   | Layout 1             | `beb461f94ae4`  |
| 3177   | Layout 1             | `beb461f94ae4`  |
| 3169   | Layout 1             | `beb461f94ae4`  |
| 3158   | Layout 1             | `beb461f94ae4`  |
| 3151   | Layout 1             | `beb461f94ae4`  |
| 3144   | Layout 1             | `beb461f94ae4`  |
| 3133   | Layout 1             | `beb461f94ae4`  |
| 3125   | Layout 1             | `beb461f94ae4`  |
| 3118   | Layout 1             | `beb461f94ae4`  |
| 3111   | Layout 1             | `beb461f94ae4`  |
| 3103   | Layout 1             | `beb461f94ae4`  |
| 3095   | Layout 1             | `beb461f94ae4`  |
| 3086   | Layout 1             | `beb461f94ae4`  |
| 3072   | Layout 1             | `beb461f94ae4`  |
| 3062   | Layout 1             | `beb461f94ae4`  |
| 3052   | Layout 1             | `beb461f94ae4`  |
| 3045   | Layout 1             | `beb461f94ae4`  |
| 3037   | Layout 1             | `beb461f94ae4`  |
| 3030   | Layout 1             | `beb461f94ae4`  |
| 3021   | Layout 1             | `beb461f94ae4`  |
| 3012   | Layout 1             | `beb461f94ae4`  |
| 3002   | Layout 1             | `beb461f94ae4`  |
| 2995   | Layout 1             | `beb461f94ae4`  |
| 2987   | Layout 1             | `beb461f94ae4`  |
| 2978   | Layout 1             | `beb461f94ae4`  |
| 2970   | Layout 1             | `beb461f94ae4`  |
| 2959   | Layout 1             | `beb461f94ae4`  |
| 2951   | Layout 1             | `beb461f94ae4`  |
| 2942   | Layout 1             | `beb461f94ae4`  |
| 2935   | Layout 1             | `beb461f94ae4`  |
| 2932   | Layout 1             | `beb461f94ae4`  |
| 2923   | Layout 1             | `beb461f94ae4`  |
| 2919   | Layout 1             | `beb461f94ae4`  |
| 2907   | Layout 1             | `beb461f94ae4`  |
| 2900   | Layout 1             | `beb461f94ae4`  |
| 2891   | Layout 1             | `beb461f94ae4`  |
| 2882   | Layout 1             | `beb461f94ae4`  |
| 2872   | Layout 1             | `beb461f94ae4`  |
| 2863   | Layout 1             | `beb461f94ae4`  |
| 2855   | Layout 1             | `beb461f94ae4`  |
| 2849   | Layout 1             | `beb461f94ae4`  |
| 2844   | Layout 1             | `beb461f94ae4`  |
| 2834   | Layout 1             | `beb461f94ae4`  |
| 2825   | Layout 1             | `beb461f94ae4`  |
| 2819   | Layout 1             | `beb461f94ae4`  |
| 2811   | Layout 1             | `beb461f94ae4`  |
| 2803   | Layout 1             | `beb461f94ae4`  |
| 2794   | Layout 1             | `beb461f94ae4`  |
| 2783   | Layout 1             | `beb461f94ae4`  |
| 2774   | Layout 1             | `beb461f94ae4`  |
| 2765   | Layout 1             | `beb461f94ae4`  |
| 2756   | Layout 1             | `beb461f94ae4`  |
| 2750   | Layout 1             | `beb461f94ae4`  |
| 2743   | Layout 1             | `beb461f94ae4`  |
| 2736   | Layout 1             | `beb461f94ae4`  |
| 2726   | Layout 1             | `beb461f94ae4`  |
| 2717   | Layout 1             | `beb461f94ae4`  |
| 2709   | Layout 1             | `beb461f94ae4`  |
| 2703   | Layout 1             | `beb461f94ae4`  |
| 2695   | Layout 1             | `beb461f94ae4`  |
| 2684   | Layout 1             | `beb461f94ae4`  |
| 2672   | Layout 1             | `beb461f94ae4`  |
| 2665   | Layout 1             | `beb461f94ae4`  |
| 2657   | Layout 1             | `beb461f94ae4`  |
| 2649   | Layout 1             | `beb461f94ae4`  |
| 2644   | Layout 1             | `beb461f94ae4`  |
| 2637   | Layout 1             | `beb461f94ae4`  |
| 2629   | Layout 1             | `beb461f94ae4`  |
| 2619   | Layout 1             | `beb461f94ae4`  |
| 2612   | Layout 1             | `beb461f94ae4`  |
| 2606   | Layout 1             | `beb461f94ae4`  |
| 2602   | Layout 1             | `beb461f94ae4`  |
| 2601   | Layout 1             | `beb461f94ae4`  |
| 2592   | Layout 1             | `beb461f94ae4`  |
| 2583   | Layout 1             | `beb461f94ae4`  |
| 2575   | Layout 1             | `beb461f94ae4`  |
| 2567   | Layout 1             | `beb461f94ae4`  |
| 2560   | Layout 1             | `beb461f94ae4`  |
| 2553   | Layout 1             | `beb461f94ae4`  |
| 2545   | Layout 1             | `beb461f94ae4`  |
| 2538   | Layout 1             | `beb461f94ae4`  |
| 2529   | Layout 1             | `beb461f94ae4`  |
| 2519   | Layout 1             | `beb461f94ae4`  |
| 2513   | Layout 1             | `beb461f94ae4`  |
| 2510   | Layout 1             | `beb461f94ae4`  |
| 2507   | Layout 1             | `beb461f94ae4`  |
| 2503   | Layout 1             | `beb461f94ae4`  |
| 2498   | Layout 1             | `beb461f94ae4`  |
| 2492   | Layout 1             | `beb461f94ae4`  |
| 2487   | Layout 1             | `beb461f94ae4`  |
| 2480   | Layout 1             | `beb461f94ae4`  |
| 2474   | Layout 1             | `beb461f94ae4`  |
| 2468   | Layout 1             | `beb461f94ae4`  |
| 2460   | Layout 1             | `beb461f94ae4`  |
| 2453   | Layout 1             | `beb461f94ae4`  |
| 2444   | Layout 1             | `beb461f94ae4`  |
| 2438   | Layout 1             | `beb461f94ae4`  |
| 2434   | Layout 1             | `beb461f94ae4`  |
| 2429   | Layout 1             | `beb461f94ae4`  |
| 2421   | Layout 1             | `beb461f94ae4`  |
| 2414   | Layout 1             | `beb461f94ae4`  |
| 2407   | Layout 1             | `beb461f94ae4`  |
| 2401   | Layout 1             | `beb461f94ae4`  |
| 2397   | Layout 1             | `beb461f94ae4`  |
| 2393   | Layout 1             | `beb461f94ae4`  |
| 2384   | Layout 1             | `beb461f94ae4`  |
| 2378   | Layout 1             | `beb461f94ae4`  |
| 2372   | Layout 1             | `beb461f94ae4`  |
| 2358   | Layout 1             | `beb461f94ae4`  |
| 2352   | Layout 1             | `beb461f94ae4`  |
| 2347   | Layout 1             | `beb461f94ae4`  |
| 2343   | Layout 1             | `beb461f94ae4`  |
| 2335   | Layout 1             | `beb461f94ae4`  |
| 2327   | Layout 1             | `beb461f94ae4`  |
| 2324   | Layout 1             | `beb461f94ae4`  |
| 2319   | Layout 1             | `beb461f94ae4`  |
| 2313   | Layout 1             | `beb461f94ae4`  |
| 2308   | Layout 1             | `beb461f94ae4`  |
| 2302   | Layout 1             | `beb461f94ae4`  |
| 2295   | Layout 1             | `beb461f94ae4`  |
| 2290   | Layout 1             | `beb461f94ae4`  |
| 2284   | Layout 1             | `beb461f94ae4`  |
| 2276   | Layout 1             | `beb461f94ae4`  |
| 2269   | Layout 1             | `beb461f94ae4`  |
| 2259   | Layout 1             | `beb461f94ae4`  |
| 2250   | Layout 1             | `beb461f94ae4`  |
| 2243   | Layout 1             | `beb461f94ae4`  |
| 2235   | Layout 1             | `beb461f94ae4`  |
| 2229   | Layout 1             | `beb461f94ae4`  |
| 2224   | Layout 1             | `beb461f94ae4`  |
| 2218   | Layout 1             | `beb461f94ae4`  |
| 2215   | Layout 1             | `beb461f94ae4`  |
| 2207   | Layout 1             | `beb461f94ae4`  |
| 2203   | Layout 1             | `beb461f94ae4`  |
| 2196   | Layout 1             | `beb461f94ae4`  |
| 2192   | Layout 1             | `beb461f94ae4`  |
| 2189   | Layout 1             | `beb461f94ae4`  |
| 2183   | Layout 1             | `beb461f94ae4`  |
| 2179   | Layout 1             | `beb461f94ae4`  |
| 2171   | Layout 1             | `beb461f94ae4`  |
| 2163   | Layout 1             | `beb461f94ae4`  |
| 2156   | Layout 1             | `beb461f94ae4`  |
| 2151   | Layout 1             | `beb461f94ae4`  |
| 2147   | Layout 1             | `beb461f94ae4`  |
| 2142   | Layout 1             | `beb461f94ae4`  |
| 2138   | Layout 1             | `beb461f94ae4`  |
| 2134   | Layout 1             | `beb461f94ae4`  |
| 2130   | Layout 1             | `beb461f94ae4`  |
| 2122   | Layout 1             | `beb461f94ae4`  |
| 2107   | Layout 1             | `beb461f94ae4`  |
| 2098   | Layout 1             | `beb461f94ae4`  |
| 2089   | Layout 1             | `beb461f94ae4`  |
| 2081   | Layout 1             | `beb461f94ae4`  |
| 2073   | Layout 1             | `beb461f94ae4`  |
| 2067   | Layout 1             | `beb461f94ae4`  |
| 2063   | Layout 1             | `beb461f94ae4`  |
| 2059   | Layout 1             | `beb461f94ae4`  |
| 2052   | Layout 1             | `beb461f94ae4`  |
| 2044   | Layout 1             | `beb461f94ae4`  |
| 2039   | Layout 1             | `beb461f94ae4`  |
| 2032   | Layout 1             | `beb461f94ae4`  |
| 2025   | Layout 1             | `beb461f94ae4`  |
| 2011   | Layout 1             | `beb461f94ae4`  |
| 2005   | Layout 1             | `beb461f94ae4`  |
| 2000   | Layout 1             | `beb461f94ae4`  |
| 1996   | Layout 1             | `beb461f94ae4`  |
| 1991   | Layout 1             | `beb461f94ae4`  |
| 1985   | Layout 1             | `beb461f94ae4`  |
| 1980   | Layout 1             | `beb461f94ae4`  |
| 1969   | Layout 1             | `beb461f94ae4`  |
| 1964   | Layout 1             | `beb461f94ae4`  |
| 1958   | Layout 1             | `beb461f94ae4`  |
| 1950   | Layout 1             | `beb461f94ae4`  |
| 1945   | Layout 1             | `beb461f94ae4`  |
| 1937   | Layout 1             | `beb461f94ae4`  |
| 1933   | Layout 1             | `beb461f94ae4`  |
| 1927   | Layout 1             | `beb461f94ae4`  |
| 1921   | Layout 1             | `beb461f94ae4`  |
| 1914   | Layout 1             | `beb461f94ae4`  |
| 1908   | Layout 1             | `beb461f94ae4`  |
| 1897   | Layout 1             | `beb461f94ae4`  |
| 1892   | Layout 1             | `beb461f94ae4`  |
| 1886   | Layout 1             | `beb461f94ae4`  |
| 1881   | Layout 1             | `beb461f94ae4`  |
| 1871   | Layout 1             | `beb461f94ae4`  |
| 1866   | Layout 1             | `beb461f94ae4`  |
| 1862   | Layout 1             | `beb461f94ae4`  |
| 1854   | Layout 1             | `beb461f94ae4`  |
| 1846   | Layout 1             | `beb461f94ae4`  |
| 1838   | Layout 1             | `beb461f94ae4`  |
| 1832   | Layout 1             | `beb461f94ae4`  |
| 1826   | Layout 1             | `beb461f94ae4`  |
| 1822   | Layout 1             | `beb461f94ae4`  |
| 1818   | Layout 1             | `beb461f94ae4`  |
| 1804   | Layout 1             | `beb461f94ae4`  |
| 1794   | Layout 1             | `beb461f94ae4`  |
| 1790   | Layout 1             | `beb461f94ae4`  |
| 1784   | Layout 1             | `beb461f94ae4`  |
| 1774   | Layout 1             | `beb461f94ae4`  |
| 1771   | Layout 1             | `beb461f94ae4`  |
| 1762   | Layout 1             | `beb461f94ae4`  |
| 1759   | Layout 1             | `beb461f94ae4`  |
| 1754   | Layout 1             | `beb461f94ae4`  |
| 1749   | Layout 1             | `beb461f94ae4`  |
| 1743   | Layout 1             | `beb461f94ae4`  |
| 1737   | Layout 1             | `beb461f94ae4`  |
| 1731   | Layout 1             | `beb461f94ae4`  |
| 1725   | Layout 1             | `beb461f94ae4`  |
| 1717   | Layout 1             | `beb461f94ae4`  |
| 1710   | Layout 1             | `beb461f94ae4`  |
| 1704   | Layout 1             | `beb461f94ae4`  |
| 1698   | Layout 1             | `beb461f94ae4`  |
| 1690   | Layout 1             | `beb461f94ae4`  |
| 1685   | Layout 1             | `beb461f94ae4`  |
| 1680   | Layout 1             | `beb461f94ae4`  |
| 1674   | Layout 1             | `beb461f94ae4`  |
| 1668   | Layout 1             | `beb461f94ae4`  |
| 1659   | Layout 1             | `beb461f94ae4`  |
| 1649   | Layout 1             | `beb461f94ae4`  |
| 1642   | Layout 1             | `beb461f94ae4`  |
| 1636   | Layout 1             | `beb461f94ae4`  |
| 1628   | Layout 1             | `beb461f94ae4`  |
| 1622   | Layout 1             | `beb461f94ae4`  |
| 1614   | Layout 1             | `beb461f94ae4`  |
| 1608   | Layout 1             | `beb461f94ae4`  |
| 1602   | Layout 1             | `beb461f94ae4`  |
| 1598   | Layout 1             | `beb461f94ae4`  |
| 1594   | Layout 1             | `beb461f94ae4`  |
| 1590   | Layout 1             | `beb461f94ae4`  |
| 1587   | Layout 1             | `beb461f94ae4`  |
| 1584   | Layout 1             | `beb461f94ae4`  |
| 1579   | Layout 1             | `beb461f94ae4`  |
| 1572   | Layout 1             | `beb461f94ae4`  |
| 1565   | Layout 1             | `beb461f94ae4`  |
| 1559   | Layout 1             | `beb461f94ae4`  |
| 1554   | Layout 1             | `beb461f94ae4`  |
| 1547   | Layout 1             | `beb461f94ae4`  |
| 1537   | Layout 1             | `beb461f94ae4`  |
| 1529   | Layout 1             | `beb461f94ae4`  |
| 1524   | Layout 1             | `beb461f94ae4`  |
| 1519   | Layout 1             | `beb461f94ae4`  |
| 1509   | Layout 1             | `beb461f94ae4`  |
| 1506   | Layout 1             | `beb461f94ae4`  |
| 1504   | Layout 1             | `beb461f94ae4`  |
| 1500   | Layout 1             | `beb461f94ae4`  |
| 1493   | Layout 1             | `beb461f94ae4`  |
| 1489   | Layout 1             | `beb461f94ae4`  |
| 1485   | Layout 1             | `beb461f94ae4`  |
| 1481   | Layout 1             | `beb461f94ae4`  |
| 1474   | Layout 1             | `beb461f94ae4`  |
| 1466   | Layout 1             | `beb461f94ae4`  |
| 1462   | Layout 1             | `beb461f94ae4`  |
| 1459   | Layout 1             | `beb461f94ae4`  |
| 1453   | Layout 1             | `beb461f94ae4`  |
| 1450   | Layout 1             | `beb461f94ae4`  |
| 1445   | Layout 1             | `beb461f94ae4`  |
| 1439   | Layout 1             | `beb461f94ae4`  |
| 1433   | Layout 1             | `beb461f94ae4`  |
| 1430   | Layout 1             | `beb461f94ae4`  |
| 1426   | Layout 1             | `beb461f94ae4`  |
| 1421   | Layout 1             | `beb461f94ae4`  |
| 1417   | Layout 1             | `beb461f94ae4`  |
| 1416   | Layout 1             | `beb461f94ae4`  |
| 1409   | Layout 1             | `beb461f94ae4`  |
| 1405   | Layout 1             | `beb461f94ae4`  |
| 1401   | Layout 1             | `beb461f94ae4`  |
| 1396   | Layout 1             | `beb461f94ae4`  |
| 1391   | Layout 1             | `beb461f94ae4`  |
| 1390   | Layout 1             | `beb461f94ae4`  |
| 1386   | Layout 1             | `beb461f94ae4`  |
| 1381   | Layout 1             | `beb461f94ae4`  |
| 1379   | Layout 1             | `beb461f94ae4`  |
| 1372   | Layout 1             | `beb461f94ae4`  |
| 1366   | Layout 1             | `beb461f94ae4`  |
| 1364   | Layout 1             | `beb461f94ae4`  |
| 1363   | Layout 1             | `beb461f94ae4`  |
| 1360   | Layout 1             | `beb461f94ae4`  |
| 1358   | Layout 1             | `beb461f94ae4`  |
| 1355   | Layout 1             | `beb461f94ae4`  |
| 1351   | Layout 1             | `beb461f94ae4`  |
| 1348   | Layout 1             | `beb461f94ae4`  |
| 1346   | Layout 1             | `beb461f94ae4`  |
| 1341   | No documented layout | `beb461f94ae4`  |
| 1340   | No documented layout | `beb461f94ae4`  |
| 1338   | No documented layout | `beb461f94ae4`  |
| 1335   | No documented layout | `beb461f94ae4`  |
| 1333   | No documented layout | `beb461f94ae4`  |
| 1329   | No documented layout | `beb461f94ae4`  |
| 1327   | No documented layout | `beb461f94ae4`  |
| 1324   | No documented layout | `beb461f94ae4`  |
| 1321   | No documented layout | `beb461f94ae4`  |
| 1319   | No documented layout | `beb461f94ae4`  |
| 1318   | No documented layout | `beb461f94ae4`  |
| 1316   | No documented layout | `beb461f94ae4`  |
| 1313   | No documented layout | `beb461f94ae4`  |
| 1311   | No documented layout | `beb461f94ae4`  |
| 1309   | No documented layout | `beb461f94ae4`  |
| 1304   | No documented layout | `beb461f94ae4`  |
| 1292   | No documented layout | `beb461f94ae4`  |
| 1286   | No documented layout | `beb461f94ae4`  |
| 1280   | No documented layout | `beb461f94ae4`  |
| 1276   | No file              | `beb461f94ae4`  |
| 1267   | No file              | `beb461f94ae4`  |
| 1261   | No file              | `beb461f94ae4`  |
| 1256   | No file              | `beb461f94ae4`  |
| 1250   | No file              | `beb461f94ae4`  |
| 1246   | No file              | `beb461f94ae4`  |
| 1239   | No file              | `beb461f94ae4`  |
| 1230   | No file              | `beb461f94ae4`  |
| 1226   | No file              | `beb461f94ae4`  |
| 1220   | No file              | `beb461f94ae4`  |
| 1217   | No file              | `beb461f94ae4`  |
| 1211   | No file              | `beb461f94ae4`  |
| 1210   | No file              | `beb461f94ae4`  |
| 1208   | No file              | `beb461f94ae4`  |
| 1203   | No file              | `beb461f94ae4`  |
| 1197   | No file              | `beb461f94ae4`  |
| 1194   | No file              | `beb461f94ae4`  |
| 1192   | No file              | `beb461f94ae4`  |
| 1187   | No file              | `beb461f94ae4`  |
| 1183   | No file              | `beb461f94ae4`  |
| 1177   | No file              | `beb461f94ae4`  |
| 1173   | No file              | `beb461f94ae4`  |
| 1167   | No file              | `beb461f94ae4`  |
| 1164   | No file              | `beb461f94ae4`  |
| 1156   | No file              | `beb461f94ae4`  |
| 1149   | No file              | `beb461f94ae4`  |
| 1144   | No file              | `beb461f94ae4`  |
| 1137   | No file              | `beb461f94ae4`  |
| 1132   | No file              | `beb461f94ae4`  |
| 1127   | No file              | `beb461f94ae4`  |
| 1122   | No file              | `beb461f94ae4`  |
| 1118   | No file              | `beb461f94ae4`  |
| 1114   | No file              | `beb461f94ae4`  |
| 1109   | No file              | `beb461f94ae4`  |
| 1102   | No file              | `beb461f94ae4`  |
| 1096   | No file              | `beb461f94ae4`  |
| 1088   | No file              | `beb461f94ae4`  |
| 1081   | No file              | `beb461f94ae4`  |
| 1076   | No file              | `beb461f94ae4`  |
| 1069   | No file              | `beb461f94ae4`  |
| 1064   | No file              | `beb461f94ae4`  |
| 1058   | No file              | `beb461f94ae4`  |
| 1051   | No file              | `beb461f94ae4`  |
| 1044   | No file              | `beb461f94ae4`  |
| 1036   | No file              | `beb461f94ae4`  |
| 1026   | No file              | `beb461f94ae4`  |
| 1016   | No file              | `beb461f94ae4`  |
| 1009   | No file              | `beb461f94ae4`  |
| 1005   | No file              | `beb461f94ae4`  |
| 1000   | No file              | `beb461f94ae4`  |
| 998    | No file              | `beb461f94ae4`  |
| 990    | No file              | `beb461f94ae4`  |
| 979    | No file              | `beb461f94ae4`  |
| 972    | No file              | `beb461f94ae4`  |
| 963    | No file              | `beb461f94ae4`  |
| 955    | No file              | `beb461f94ae4`  |
| 946    | No file              | `beb461f94ae4`  |
| 938    | No file              | `beb461f94ae4`  |
| 927    | No file              | `beb461f94ae4`  |
| 911    | No file              | `beb461f94ae4`  |
| 904    | No file              | `beb461f94ae4`  |
| 899    | No file              | `beb461f94ae4`  |
| 894    | No file              | `beb461f94ae4`  |
| 885    | No file              | `beb461f94ae4`  |
| 879    | No file              | `beb461f94ae4`  |
| 872    | No file              | `beb461f94ae4`  |
| 864    | No file              | `beb461f94ae4`  |
| 855    | No file              | `beb461f94ae4`  |
| 853    | No file              | `beb461f94ae4`  |
| 845    | No file              | `beb461f94ae4`  |
| 837    | No file              | `beb461f94ae4`  |
| 829    | No file              | `beb461f94ae4`  |
| 822    | No file              | `beb461f94ae4`  |
| 814    | No file              | `beb461f94ae4`  |
| 805    | No file              | `beb461f94ae4`  |
| 794    | No file              | `beb461f94ae4`  |
| 787    | No file              | `beb461f94ae4`  |
| 780    | No file              | `beb461f94ae4`  |
| 771    | No file              | `beb461f94ae4`  |
| 760    | No file              | `beb461f94ae4`  |
| 748    | No file              | `beb461f94ae4`  |
| 741    | No file              | `beb461f94ae4`  |
| 736    | No file              | `beb461f94ae4`  |
| 731    | No file              | `beb461f94ae4`  |
| 723    | No file              | `beb461f94ae4`  |
| 711    | No file              | `beb461f94ae4`  |
| 707    | No file              | `beb461f94ae4`  |
| 697    | No file              | `beb461f94ae4`  |
| 689    | No file              | `beb461f94ae4`  |
| 683    | No file              | `beb461f94ae4`  |
| 678    | No file              | `beb461f94ae4`  |
| 670    | No file              | `beb461f94ae4`  |
| 661    | No file              | `beb461f94ae4`  |
| 656    | No file              | `beb461f94ae4`  |
| 652    | No file              | `beb461f94ae4`  |
| 643    | No file              | `beb461f94ae4`  |
| 637    | No file              | `beb461f94ae4`  |
| 630    | No file              | `beb461f94ae4`  |
| 627    | No file              | `beb461f94ae4`  |
| 621    | No file              | `beb461f94ae4`  |
| 617    | No file              | `beb461f94ae4`  |
| 615    | No file              | `beb461f94ae4`  |
| 606    | No file              | `beb461f94ae4`  |
| 599    | No file              | `beb461f94ae4`  |
| 592    | No file              | `beb461f94ae4`  |
| 586    | No file              | `beb461f94ae4`  |
| 577    | No file              | `beb461f94ae4`  |
| 569    | No file              | `beb461f94ae4`  |
| 561    | No file              | `beb461f94ae4`  |
| 554    | No file              | `beb461f94ae4`  |
| 542    | No file              | `beb461f94ae4`  |
| 532    | No file              | `beb461f94ae4`  |
| 531    | No file              | `beb461f94ae4`  |
| 526    | No file              | `beb461f94ae4`  |
| 521    | No file              | `beb461f94ae4`  |
| 517    | No file              | `beb461f94ae4`  |
| 510    | No file              | `beb461f94ae4`  |
| 508    | No file              | `beb461f94ae4`  |
| 504    | No file              | `beb461f94ae4`  |
| 497    | No file              | `beb461f94ae4`  |
| 491    | No file              | `beb461f94ae4`  |
| 485    | No file              | `beb461f94ae4`  |
| 478    | No file              | `beb461f94ae4`  |
| 472    | No file              | `beb461f94ae4`  |
| 466    | No file              | `beb461f94ae4`  |
| 457    | No file              | `beb461f94ae4`  |
| 452    | No file              | `beb461f94ae4`  |
| 449    | No file              | `beb461f94ae4`  |
| 435    | No file              | `beb461f94ae4`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                 |
| ------------------------- | -------- | -------------------------------------------------------------------- |
| `buildingbuffoffset.dbss` | Optional | `(list, buff_index) -> (offset, size)` of every row; the rows are fixed size and can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic and no string table. A list count, then the lists back to
back; the file ends after the last list.

| Offset  | Type                   | Field      | Notes                                                       |
| ------- | ---------------------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32                    | list_count | `4` on clients 1784 and 3474                                |
| `+0x04` | Villa List[list_count] | lists      | List `i` holds `villa_count` `i + 1`; see Villa List        |

### Villa List (variable: 4 bytes + rows)

| Offset  | Type           | Field     | Notes                                                    |
| ------- | -------------- | --------- | -------------------------------------------------------- |
| `+0x00` | u32            | row_count | `0` for lists 1 to 3 on clients 1784 and 3474            |
| `+0x04` | Row[row_count] | rows      | See Row                                                  |

### Row (12 bytes)

| Offset  | Type | Field      | Notes                                                              |
| ------- | ---- | ---------- | ------------------------------------------------------------------ |
| `+0x00` | u16  | buff_index | Position in the list, `0` up; the key within the list              |
| `+0x02` | u16  | skill_no   | The buff skill; LOC type 10 holds its name and effect text         |
| `+0x04` | i64  | cost       | Price in silver                                                    |

### `buildingbuffoffset.dbss`

The same list walk as the main file: a u32 list count, then per list a u32
row count and 10-byte rows. A row leaves out the list number; its list
stands for it.

| Offset  | Type                          | Field      | Notes                                       |
| ------- | ----------------------------- | ---------- | ------------------------------------------- |
| `+0x00` | u32                           | list_count | Equals the main file's `list_count`         |
| `+0x04` | Offset List[list_count]       | lists      | List `i` indexes main list `i`; see Offset List |

### Offset List (variable: 4 bytes + rows)

| Offset  | Type                  | Field     | Notes                                 |
| ------- | --------------------- | --------- | ------------------------------------- |
| `+0x00` | u32                   | row_count | Equals the main list's `row_count`    |
| `+0x04` | Offset Row[row_count] | rows      | See Offset Row                        |

### Offset Row (10 bytes)

| Offset  | Type | Field      | Notes                                                           |
| ------- | ---- | ---------- | --------------------------------------------------------------- |
| `+0x00` | u16  | buff_index | Key of the row it points at, together with the list             |
| `+0x02` | u32  | offset     | Start of the row's `skill_no` in `buildingbuff.dbss`, past its `buff_index` |
| `+0x06` | u32  | size       | `10`, `skill_no` and `cost`                                     |

On clients 1784 and 3474 every index row points at the row with its list
and `buff_index`.

## Field Names

The names are the columns of the `Villa_Skill` sheet: `SkillNo`,
`Count_Villa` and `Cost`. The sheet is in a private server's
`DataSheet_AuctionDataTable.xlsm` and `DataSheets.bexcel` on client 1784 and
in the `Villa_Skill` table of a private server on client 519.

| Source              | Rows | Shared skills with client 1784 | Shared skills with client 3474 |
| ------------------- | ---- | ------------------------------ | ------------------------------ |
| Client 519 table    | 6    | 6 of 6, same cost              | 4 of 4, same cost              |
| Client 1784 `.xlsm` | 8    | 3 of 3, same cost              | 2 of 2, same cost              |

The client 519 rows are skills `53657` to `53662` (90 and 180 minutes of
the three client 1784 buffs). The client 1784 sheet adds five private
server rows (`59790` to `59792`, `54132`, `56845`), and its compiled
`buildingbuff.dbss` holds the same eight rows in the same shape as this
layout. Every row of both sheets has `Count_Villa` `1`, and every file has
its rows in list 0.

The client 1784 server dump of the same private server loads the sheet into
`BuildingBuffStaticStatusManager`. Its loader reads `Count_Villa` as an int
and subtracts 1, logs "별채버프 인덱스는 최대 (%#)을 넘을 수 없습니다" (the
villa buff index cannot exceed %#) for a result above 3, reads `SkillNo` as
an int16 and `Cost` as an int64, and adds the row to the one of four maps
that result picks, keyed by that map's size before the insert. That is the
four lists, `buff_index` counting from 0 in each, and `villa_count` = list
number + 1. Its getter logs `getXXX villaCount : %#, index : %#`. The client
Lua reads the same pair: `ToClient_GetBuildingBuffCount()` lists, then
`ToClient_GetCountPerBuffKeyCount(keyCount)` rows each,
`ToClient_GetBuildingBuff(keyCount, buffIndex)` for the skill and
`ToClient_GetBuildingBuffCost(keyCount, buffIndex)` for the price. The 2016
PDB has no building buff struct.

## Notes

- The window groups the rows into one box per buff by skill name and puts
  each duration on a buy button: it cuts the name at `(` for the box title
  and takes the text between the brackets (`60 min`) as the button label,
  with the cost below it (`panel_window_camp_villabuff_all_1.luac`). The
  box icons are `WisdomOfLife_Up.dds` and `SkillAndExp_Up.dds`.
- Buying calls `ToClient_ApplyBuildingBuff(keyCount, buffIndex, true)` after
  the `LUA_CAMP_BUILDINGBUFF_MESSAGEBOX_DESC` confirmation.
  The window's footer, `LUA_BUILDINGBUFF_BOTTOMDESC`, says a Villa Scroll
  needs a Villa Invitation from the Villa Manager and an orange-grade tent
  equipped.
- The server dump's row object is 24 bytes: the skill number, the cost and
  an 8-byte field the loader sets to `0`. The file stores only the first two.
- The client 1784 and 3474 files differ only in their rows; the list count,
  the empty lists and the index shape are the same.

## Open Questions

### What `Count_Villa` Counts

Every known row, in the client 519 and 1784 sheets and in the client 1784
and 3474 files, has `Count_Villa` `1`, so lists 1 to 3 are always empty.
The server allows values 1 to 4, and the Lua calls the list number
`keyCount` and the client counts lists with `ToClient_GetBuildingBuffCount()`.
It may be the number of villa invitations (keys) a buff needs, but no row
uses a value above 1 to test that.
