# `olviaacademyseasonss.bss` Format

## Purpose

The current Olvia Academy class (season): its number, four Unix times, the
enrollment and graduation quests and the class title. The file holds one
class only, the one running on the client it ships with: class 3 on client
3474 (2026-07-30 to 2026-11-12), class 1 on client 3251. It has no PABR
magic and no string table. The quest lists of the same academy are in
[`olviaacademy*questlist.bss`](olviaacademyquestlist_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                       | Bytes | Records | Row bytes |
| ------ | -------------- | -------------------------- | ----- | ------- | --------- |
| 1      | 3186 and later | `olviaacademyseasonss.bss` | 48    | -       | -         |

| Layout | File                       | Known         | Unknown    |
| ------ | -------------------------- | ------------- | ---------- |
| 1      | `olviaacademyseasonss.bss` | 48 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `6d0f8a94b490`  |
| 3482   | Layout 1 | `6d0f8a94b490`  |
| 3474   | Layout 1 | `6d0f8a94b490`  |
| 3473   | Layout 1 | `6d0f8a94b490`  |
| 3464   | Layout 1 | `6d0f8a94b490`  |
| 3458   | Layout 1 | `6d0f8a94b490`  |
| 3454   | Layout 1 | `6d0f8a94b490`  |
| 3444   | Layout 1 | `6d0f8a94b490`  |
| 3435   | Layout 1 | `6d0f8a94b490`  |
| 3426   | Layout 1 | `6d0f8a94b490`  |
| 3418   | Layout 1 | `6d0f8a94b490`  |
| 3412   | Layout 1 | `6d0f8a94b490`  |
| 3402   | Layout 1 | `6d0f8a94b490`  |
| 3396   | Layout 1 | `6d0f8a94b490`  |
| 3387   | Layout 1 | `6d0f8a94b490`  |
| 3381   | Layout 1 | `6d0f8a94b490`  |
| 3373   | Layout 1 | `6d0f8a94b490`  |
| 3364   | Layout 1 | `6d0f8a94b490`  |
| 3356   | Layout 1 | `6d0f8a94b490`  |
| 3349   | Layout 1 | `6d0f8a94b490`  |
| 3342   | Layout 1 | `6d0f8a94b490`  |
| 3335   | Layout 1 | `6d0f8a94b490`  |
| 3326   | Layout 1 | `6d0f8a94b490`  |
| 3321   | Layout 1 | `6d0f8a94b490`  |
| 3314   | Layout 1 | `6d0f8a94b490`  |
| 3303   | Layout 1 | `6d0f8a94b490`  |
| 3302   | Layout 1 | `6d0f8a94b490`  |
| 3293   | Layout 1 | `6d0f8a94b490`  |
| 3283   | Layout 1 | `6d0f8a94b490`  |
| 3275   | Layout 1 | `6d0f8a94b490`  |
| 3267   | Layout 1 | `6d0f8a94b490`  |
| 3258   | Layout 1 | `6d0f8a94b490`  |
| 3251   | Layout 1 | `6d0f8a94b490`  |
| 3242   | Layout 1 | `6d0f8a94b490`  |
| 3235   | Layout 1 | `6d0f8a94b490`  |
| 3229   | Layout 1 | `6d0f8a94b490`  |
| 3212   | Layout 1 | `6d0f8a94b490`  |
| 3203   | Layout 1 | `6d0f8a94b490`  |
| 3193   | Layout 1 | `6d0f8a94b490`  |
| 3186   | Layout 1 | `6d0f8a94b490`  |
| 3177   | No file  | `6d0f8a94b490`  |
| 3169   | No file  | `6d0f8a94b490`  |
| 3158   | No file  | `6d0f8a94b490`  |
| 3151   | No file  | `6d0f8a94b490`  |
| 3144   | No file  | `6d0f8a94b490`  |
| 3133   | No file  | `6d0f8a94b490`  |
| 3125   | No file  | `6d0f8a94b490`  |
| 3118   | No file  | `6d0f8a94b490`  |
| 3111   | No file  | `6d0f8a94b490`  |
| 3103   | No file  | `6d0f8a94b490`  |
| 3095   | No file  | `6d0f8a94b490`  |
| 3086   | No file  | `6d0f8a94b490`  |
| 3072   | No file  | `6d0f8a94b490`  |
| 3062   | No file  | `6d0f8a94b490`  |
| 3052   | No file  | `6d0f8a94b490`  |
| 3045   | No file  | `6d0f8a94b490`  |
| 3037   | No file  | `6d0f8a94b490`  |
| 3030   | No file  | `6d0f8a94b490`  |
| 3021   | No file  | `6d0f8a94b490`  |
| 3012   | No file  | `6d0f8a94b490`  |
| 3002   | No file  | `6d0f8a94b490`  |
| 2995   | No file  | `6d0f8a94b490`  |
| 2987   | No file  | `6d0f8a94b490`  |
| 2978   | No file  | `6d0f8a94b490`  |
| 2970   | No file  | `6d0f8a94b490`  |
| 2959   | No file  | `6d0f8a94b490`  |
| 2951   | No file  | `6d0f8a94b490`  |
| 2942   | No file  | `6d0f8a94b490`  |
| 2935   | No file  | `6d0f8a94b490`  |
| 2932   | No file  | `6d0f8a94b490`  |
| 2923   | No file  | `6d0f8a94b490`  |
| 2919   | No file  | `6d0f8a94b490`  |
| 2907   | No file  | `6d0f8a94b490`  |
| 2900   | No file  | `6d0f8a94b490`  |
| 2891   | No file  | `6d0f8a94b490`  |
| 2882   | No file  | `6d0f8a94b490`  |
| 2872   | No file  | `6d0f8a94b490`  |
| 2863   | No file  | `6d0f8a94b490`  |
| 2855   | No file  | `6d0f8a94b490`  |
| 2849   | No file  | `6d0f8a94b490`  |
| 2844   | No file  | `6d0f8a94b490`  |
| 2834   | No file  | `6d0f8a94b490`  |
| 2825   | No file  | `6d0f8a94b490`  |
| 2819   | No file  | `6d0f8a94b490`  |
| 2811   | No file  | `6d0f8a94b490`  |
| 2803   | No file  | `6d0f8a94b490`  |
| 2794   | No file  | `6d0f8a94b490`  |
| 2783   | No file  | `6d0f8a94b490`  |
| 2774   | No file  | `6d0f8a94b490`  |
| 2765   | No file  | `6d0f8a94b490`  |
| 2756   | No file  | `6d0f8a94b490`  |
| 2750   | No file  | `6d0f8a94b490`  |
| 2743   | No file  | `6d0f8a94b490`  |
| 2736   | No file  | `6d0f8a94b490`  |
| 2726   | No file  | `6d0f8a94b490`  |
| 2717   | No file  | `6d0f8a94b490`  |
| 2709   | No file  | `6d0f8a94b490`  |
| 2703   | No file  | `6d0f8a94b490`  |
| 2695   | No file  | `6d0f8a94b490`  |
| 2684   | No file  | `6d0f8a94b490`  |
| 2672   | No file  | `6d0f8a94b490`  |
| 2665   | No file  | `6d0f8a94b490`  |
| 2657   | No file  | `6d0f8a94b490`  |
| 2649   | No file  | `6d0f8a94b490`  |
| 2644   | No file  | `6d0f8a94b490`  |
| 2637   | No file  | `6d0f8a94b490`  |
| 2629   | No file  | `6d0f8a94b490`  |
| 2619   | No file  | `6d0f8a94b490`  |
| 2612   | No file  | `6d0f8a94b490`  |
| 2606   | No file  | `6d0f8a94b490`  |
| 2602   | No file  | `6d0f8a94b490`  |
| 2601   | No file  | `6d0f8a94b490`  |
| 2592   | No file  | `6d0f8a94b490`  |
| 2583   | No file  | `6d0f8a94b490`  |
| 2575   | No file  | `6d0f8a94b490`  |
| 2567   | No file  | `6d0f8a94b490`  |
| 2560   | No file  | `6d0f8a94b490`  |
| 2553   | No file  | `6d0f8a94b490`  |
| 2545   | No file  | `6d0f8a94b490`  |
| 2538   | No file  | `6d0f8a94b490`  |
| 2529   | No file  | `6d0f8a94b490`  |
| 2519   | No file  | `6d0f8a94b490`  |
| 2513   | No file  | `6d0f8a94b490`  |
| 2510   | No file  | `6d0f8a94b490`  |
| 2507   | No file  | `6d0f8a94b490`  |
| 2503   | No file  | `6d0f8a94b490`  |
| 2498   | No file  | `6d0f8a94b490`  |
| 2492   | No file  | `6d0f8a94b490`  |
| 2487   | No file  | `6d0f8a94b490`  |
| 2480   | No file  | `6d0f8a94b490`  |
| 2474   | No file  | `6d0f8a94b490`  |
| 2468   | No file  | `6d0f8a94b490`  |
| 2460   | No file  | `6d0f8a94b490`  |
| 2453   | No file  | `6d0f8a94b490`  |
| 2444   | No file  | `6d0f8a94b490`  |
| 2438   | No file  | `6d0f8a94b490`  |
| 2434   | No file  | `6d0f8a94b490`  |
| 2429   | No file  | `6d0f8a94b490`  |
| 2421   | No file  | `6d0f8a94b490`  |
| 2414   | No file  | `6d0f8a94b490`  |
| 2407   | No file  | `6d0f8a94b490`  |
| 2401   | No file  | `6d0f8a94b490`  |
| 2397   | No file  | `6d0f8a94b490`  |
| 2393   | No file  | `6d0f8a94b490`  |
| 2384   | No file  | `6d0f8a94b490`  |
| 2378   | No file  | `6d0f8a94b490`  |
| 2372   | No file  | `6d0f8a94b490`  |
| 2358   | No file  | `6d0f8a94b490`  |
| 2352   | No file  | `6d0f8a94b490`  |
| 2347   | No file  | `6d0f8a94b490`  |
| 2343   | No file  | `6d0f8a94b490`  |
| 2335   | No file  | `6d0f8a94b490`  |
| 2327   | No file  | `6d0f8a94b490`  |
| 2324   | No file  | `6d0f8a94b490`  |
| 2319   | No file  | `6d0f8a94b490`  |
| 2313   | No file  | `6d0f8a94b490`  |
| 2308   | No file  | `6d0f8a94b490`  |
| 2302   | No file  | `6d0f8a94b490`  |
| 2295   | No file  | `6d0f8a94b490`  |
| 2290   | No file  | `6d0f8a94b490`  |
| 2284   | No file  | `6d0f8a94b490`  |
| 2276   | No file  | `6d0f8a94b490`  |
| 2269   | No file  | `6d0f8a94b490`  |
| 2259   | No file  | `6d0f8a94b490`  |
| 2250   | No file  | `6d0f8a94b490`  |
| 2243   | No file  | `6d0f8a94b490`  |
| 2235   | No file  | `6d0f8a94b490`  |
| 2229   | No file  | `6d0f8a94b490`  |
| 2224   | No file  | `6d0f8a94b490`  |
| 2218   | No file  | `6d0f8a94b490`  |
| 2215   | No file  | `6d0f8a94b490`  |
| 2207   | No file  | `6d0f8a94b490`  |
| 2203   | No file  | `6d0f8a94b490`  |
| 2196   | No file  | `6d0f8a94b490`  |
| 2192   | No file  | `6d0f8a94b490`  |
| 2189   | No file  | `6d0f8a94b490`  |
| 2183   | No file  | `6d0f8a94b490`  |
| 2179   | No file  | `6d0f8a94b490`  |
| 2171   | No file  | `6d0f8a94b490`  |
| 2163   | No file  | `6d0f8a94b490`  |
| 2156   | No file  | `6d0f8a94b490`  |
| 2151   | No file  | `6d0f8a94b490`  |
| 2147   | No file  | `6d0f8a94b490`  |
| 2142   | No file  | `6d0f8a94b490`  |
| 2138   | No file  | `6d0f8a94b490`  |
| 2134   | No file  | `6d0f8a94b490`  |
| 2130   | No file  | `6d0f8a94b490`  |
| 2122   | No file  | `6d0f8a94b490`  |
| 2107   | No file  | `6d0f8a94b490`  |
| 2098   | No file  | `6d0f8a94b490`  |
| 2089   | No file  | `6d0f8a94b490`  |
| 2081   | No file  | `6d0f8a94b490`  |
| 2073   | No file  | `6d0f8a94b490`  |
| 2067   | No file  | `6d0f8a94b490`  |
| 2063   | No file  | `6d0f8a94b490`  |
| 2059   | No file  | `6d0f8a94b490`  |
| 2052   | No file  | `6d0f8a94b490`  |
| 2044   | No file  | `6d0f8a94b490`  |
| 2039   | No file  | `6d0f8a94b490`  |
| 2032   | No file  | `6d0f8a94b490`  |
| 2025   | No file  | `6d0f8a94b490`  |
| 2011   | No file  | `6d0f8a94b490`  |
| 2005   | No file  | `6d0f8a94b490`  |
| 2000   | No file  | `6d0f8a94b490`  |
| 1996   | No file  | `6d0f8a94b490`  |
| 1991   | No file  | `6d0f8a94b490`  |
| 1985   | No file  | `6d0f8a94b490`  |
| 1980   | No file  | `6d0f8a94b490`  |
| 1969   | No file  | `6d0f8a94b490`  |
| 1964   | No file  | `6d0f8a94b490`  |
| 1958   | No file  | `6d0f8a94b490`  |
| 1950   | No file  | `6d0f8a94b490`  |
| 1945   | No file  | `6d0f8a94b490`  |
| 1937   | No file  | `6d0f8a94b490`  |
| 1933   | No file  | `6d0f8a94b490`  |
| 1927   | No file  | `6d0f8a94b490`  |
| 1921   | No file  | `6d0f8a94b490`  |
| 1914   | No file  | `6d0f8a94b490`  |
| 1908   | No file  | `6d0f8a94b490`  |
| 1897   | No file  | `6d0f8a94b490`  |
| 1892   | No file  | `6d0f8a94b490`  |
| 1886   | No file  | `6d0f8a94b490`  |
| 1881   | No file  | `6d0f8a94b490`  |
| 1871   | No file  | `6d0f8a94b490`  |
| 1866   | No file  | `6d0f8a94b490`  |
| 1862   | No file  | `6d0f8a94b490`  |
| 1854   | No file  | `6d0f8a94b490`  |
| 1846   | No file  | `6d0f8a94b490`  |
| 1838   | No file  | `6d0f8a94b490`  |
| 1832   | No file  | `6d0f8a94b490`  |
| 1826   | No file  | `6d0f8a94b490`  |
| 1822   | No file  | `6d0f8a94b490`  |
| 1818   | No file  | `6d0f8a94b490`  |
| 1804   | No file  | `6d0f8a94b490`  |
| 1794   | No file  | `6d0f8a94b490`  |
| 1790   | No file  | `6d0f8a94b490`  |
| 1784   | No file  | `6d0f8a94b490`  |
| 1774   | No file  | `6d0f8a94b490`  |
| 1771   | No file  | `6d0f8a94b490`  |
| 1762   | No file  | `6d0f8a94b490`  |
| 1759   | No file  | `6d0f8a94b490`  |
| 1754   | No file  | `6d0f8a94b490`  |
| 1749   | No file  | `6d0f8a94b490`  |
| 1743   | No file  | `6d0f8a94b490`  |
| 1737   | No file  | `6d0f8a94b490`  |
| 1731   | No file  | `6d0f8a94b490`  |
| 1725   | No file  | `6d0f8a94b490`  |
| 1717   | No file  | `6d0f8a94b490`  |
| 1710   | No file  | `6d0f8a94b490`  |
| 1704   | No file  | `6d0f8a94b490`  |
| 1698   | No file  | `6d0f8a94b490`  |
| 1690   | No file  | `6d0f8a94b490`  |
| 1685   | No file  | `6d0f8a94b490`  |
| 1680   | No file  | `6d0f8a94b490`  |
| 1674   | No file  | `6d0f8a94b490`  |
| 1668   | No file  | `6d0f8a94b490`  |
| 1659   | No file  | `6d0f8a94b490`  |
| 1649   | No file  | `6d0f8a94b490`  |
| 1642   | No file  | `6d0f8a94b490`  |
| 1636   | No file  | `6d0f8a94b490`  |
| 1628   | No file  | `6d0f8a94b490`  |
| 1622   | No file  | `6d0f8a94b490`  |
| 1614   | No file  | `6d0f8a94b490`  |
| 1608   | No file  | `6d0f8a94b490`  |
| 1602   | No file  | `6d0f8a94b490`  |
| 1598   | No file  | `6d0f8a94b490`  |
| 1594   | No file  | `6d0f8a94b490`  |
| 1590   | No file  | `6d0f8a94b490`  |
| 1587   | No file  | `6d0f8a94b490`  |
| 1584   | No file  | `6d0f8a94b490`  |
| 1579   | No file  | `6d0f8a94b490`  |
| 1572   | No file  | `6d0f8a94b490`  |
| 1565   | No file  | `6d0f8a94b490`  |
| 1559   | No file  | `6d0f8a94b490`  |
| 1554   | No file  | `6d0f8a94b490`  |
| 1547   | No file  | `6d0f8a94b490`  |
| 1537   | No file  | `6d0f8a94b490`  |
| 1529   | No file  | `6d0f8a94b490`  |
| 1524   | No file  | `6d0f8a94b490`  |
| 1519   | No file  | `6d0f8a94b490`  |
| 1509   | No file  | `6d0f8a94b490`  |
| 1506   | No file  | `6d0f8a94b490`  |
| 1504   | No file  | `6d0f8a94b490`  |
| 1500   | No file  | `6d0f8a94b490`  |
| 1493   | No file  | `6d0f8a94b490`  |
| 1489   | No file  | `6d0f8a94b490`  |
| 1485   | No file  | `6d0f8a94b490`  |
| 1481   | No file  | `6d0f8a94b490`  |
| 1474   | No file  | `6d0f8a94b490`  |
| 1466   | No file  | `6d0f8a94b490`  |
| 1462   | No file  | `6d0f8a94b490`  |
| 1459   | No file  | `6d0f8a94b490`  |
| 1453   | No file  | `6d0f8a94b490`  |
| 1450   | No file  | `6d0f8a94b490`  |
| 1445   | No file  | `6d0f8a94b490`  |
| 1439   | No file  | `6d0f8a94b490`  |
| 1433   | No file  | `6d0f8a94b490`  |
| 1430   | No file  | `6d0f8a94b490`  |
| 1426   | No file  | `6d0f8a94b490`  |
| 1421   | No file  | `6d0f8a94b490`  |
| 1417   | No file  | `6d0f8a94b490`  |
| 1416   | No file  | `6d0f8a94b490`  |
| 1409   | No file  | `6d0f8a94b490`  |
| 1405   | No file  | `6d0f8a94b490`  |
| 1401   | No file  | `6d0f8a94b490`  |
| 1396   | No file  | `6d0f8a94b490`  |
| 1391   | No file  | `6d0f8a94b490`  |
| 1390   | No file  | `6d0f8a94b490`  |
| 1386   | No file  | `6d0f8a94b490`  |
| 1381   | No file  | `6d0f8a94b490`  |
| 1379   | No file  | `6d0f8a94b490`  |
| 1372   | No file  | `6d0f8a94b490`  |
| 1366   | No file  | `6d0f8a94b490`  |
| 1364   | No file  | `6d0f8a94b490`  |
| 1363   | No file  | `6d0f8a94b490`  |
| 1360   | No file  | `6d0f8a94b490`  |
| 1358   | No file  | `6d0f8a94b490`  |
| 1355   | No file  | `6d0f8a94b490`  |
| 1351   | No file  | `6d0f8a94b490`  |
| 1348   | No file  | `6d0f8a94b490`  |
| 1346   | No file  | `6d0f8a94b490`  |
| 1341   | No file  | `6d0f8a94b490`  |
| 1340   | No file  | `6d0f8a94b490`  |
| 1338   | No file  | `6d0f8a94b490`  |
| 1335   | No file  | `6d0f8a94b490`  |
| 1333   | No file  | `6d0f8a94b490`  |
| 1329   | No file  | `6d0f8a94b490`  |
| 1327   | No file  | `6d0f8a94b490`  |
| 1324   | No file  | `6d0f8a94b490`  |
| 1321   | No file  | `6d0f8a94b490`  |
| 1319   | No file  | `6d0f8a94b490`  |
| 1318   | No file  | `6d0f8a94b490`  |
| 1316   | No file  | `6d0f8a94b490`  |
| 1313   | No file  | `6d0f8a94b490`  |
| 1311   | No file  | `6d0f8a94b490`  |
| 1309   | No file  | `6d0f8a94b490`  |
| 1304   | No file  | `6d0f8a94b490`  |
| 1292   | No file  | `6d0f8a94b490`  |
| 1286   | No file  | `6d0f8a94b490`  |
| 1280   | No file  | `6d0f8a94b490`  |
| 1276   | No file  | `6d0f8a94b490`  |
| 1267   | No file  | `6d0f8a94b490`  |
| 1261   | No file  | `6d0f8a94b490`  |
| 1256   | No file  | `6d0f8a94b490`  |
| 1250   | No file  | `6d0f8a94b490`  |
| 1246   | No file  | `6d0f8a94b490`  |
| 1239   | No file  | `6d0f8a94b490`  |
| 1230   | No file  | `6d0f8a94b490`  |
| 1226   | No file  | `6d0f8a94b490`  |
| 1220   | No file  | `6d0f8a94b490`  |
| 1217   | No file  | `6d0f8a94b490`  |
| 1211   | No file  | `6d0f8a94b490`  |
| 1210   | No file  | `6d0f8a94b490`  |
| 1208   | No file  | `6d0f8a94b490`  |
| 1203   | No file  | `6d0f8a94b490`  |
| 1197   | No file  | `6d0f8a94b490`  |
| 1194   | No file  | `6d0f8a94b490`  |
| 1192   | No file  | `6d0f8a94b490`  |
| 1187   | No file  | `6d0f8a94b490`  |
| 1183   | No file  | `6d0f8a94b490`  |
| 1177   | No file  | `6d0f8a94b490`  |
| 1173   | No file  | `6d0f8a94b490`  |
| 1167   | No file  | `6d0f8a94b490`  |
| 1164   | No file  | `6d0f8a94b490`  |
| 1156   | No file  | `6d0f8a94b490`  |
| 1149   | No file  | `6d0f8a94b490`  |
| 1144   | No file  | `6d0f8a94b490`  |
| 1137   | No file  | `6d0f8a94b490`  |
| 1132   | No file  | `6d0f8a94b490`  |
| 1127   | No file  | `6d0f8a94b490`  |
| 1122   | No file  | `6d0f8a94b490`  |
| 1118   | No file  | `6d0f8a94b490`  |
| 1114   | No file  | `6d0f8a94b490`  |
| 1109   | No file  | `6d0f8a94b490`  |
| 1102   | No file  | `6d0f8a94b490`  |
| 1096   | No file  | `6d0f8a94b490`  |
| 1088   | No file  | `6d0f8a94b490`  |
| 1081   | No file  | `6d0f8a94b490`  |
| 1076   | No file  | `6d0f8a94b490`  |
| 1069   | No file  | `6d0f8a94b490`  |
| 1064   | No file  | `6d0f8a94b490`  |
| 1058   | No file  | `6d0f8a94b490`  |
| 1051   | No file  | `6d0f8a94b490`  |
| 1044   | No file  | `6d0f8a94b490`  |
| 1036   | No file  | `6d0f8a94b490`  |
| 1026   | No file  | `6d0f8a94b490`  |
| 1016   | No file  | `6d0f8a94b490`  |
| 1009   | No file  | `6d0f8a94b490`  |
| 1005   | No file  | `6d0f8a94b490`  |
| 1000   | No file  | `6d0f8a94b490`  |
| 998    | No file  | `6d0f8a94b490`  |
| 990    | No file  | `6d0f8a94b490`  |
| 979    | No file  | `6d0f8a94b490`  |
| 972    | No file  | `6d0f8a94b490`  |
| 963    | No file  | `6d0f8a94b490`  |
| 955    | No file  | `6d0f8a94b490`  |
| 946    | No file  | `6d0f8a94b490`  |
| 938    | No file  | `6d0f8a94b490`  |
| 927    | No file  | `6d0f8a94b490`  |
| 911    | No file  | `6d0f8a94b490`  |
| 904    | No file  | `6d0f8a94b490`  |
| 899    | No file  | `6d0f8a94b490`  |
| 894    | No file  | `6d0f8a94b490`  |
| 885    | No file  | `6d0f8a94b490`  |
| 879    | No file  | `6d0f8a94b490`  |
| 872    | No file  | `6d0f8a94b490`  |
| 864    | No file  | `6d0f8a94b490`  |
| 855    | No file  | `6d0f8a94b490`  |
| 853    | No file  | `6d0f8a94b490`  |
| 845    | No file  | `6d0f8a94b490`  |
| 837    | No file  | `6d0f8a94b490`  |
| 829    | No file  | `6d0f8a94b490`  |
| 822    | No file  | `6d0f8a94b490`  |
| 814    | No file  | `6d0f8a94b490`  |
| 805    | No file  | `6d0f8a94b490`  |
| 794    | No file  | `6d0f8a94b490`  |
| 787    | No file  | `6d0f8a94b490`  |
| 780    | No file  | `6d0f8a94b490`  |
| 771    | No file  | `6d0f8a94b490`  |
| 760    | No file  | `6d0f8a94b490`  |
| 748    | No file  | `6d0f8a94b490`  |
| 741    | No file  | `6d0f8a94b490`  |
| 736    | No file  | `6d0f8a94b490`  |
| 731    | No file  | `6d0f8a94b490`  |
| 723    | No file  | `6d0f8a94b490`  |
| 711    | No file  | `6d0f8a94b490`  |
| 707    | No file  | `6d0f8a94b490`  |
| 697    | No file  | `6d0f8a94b490`  |
| 689    | No file  | `6d0f8a94b490`  |
| 683    | No file  | `6d0f8a94b490`  |
| 678    | No file  | `6d0f8a94b490`  |
| 670    | No file  | `6d0f8a94b490`  |
| 661    | No file  | `6d0f8a94b490`  |
| 656    | No file  | `6d0f8a94b490`  |
| 652    | No file  | `6d0f8a94b490`  |
| 643    | No file  | `6d0f8a94b490`  |
| 637    | No file  | `6d0f8a94b490`  |
| 630    | No file  | `6d0f8a94b490`  |
| 627    | No file  | `6d0f8a94b490`  |
| 621    | No file  | `6d0f8a94b490`  |
| 617    | No file  | `6d0f8a94b490`  |
| 615    | No file  | `6d0f8a94b490`  |
| 606    | No file  | `6d0f8a94b490`  |
| 599    | No file  | `6d0f8a94b490`  |
| 592    | No file  | `6d0f8a94b490`  |
| 586    | No file  | `6d0f8a94b490`  |
| 577    | No file  | `6d0f8a94b490`  |
| 569    | No file  | `6d0f8a94b490`  |
| 561    | No file  | `6d0f8a94b490`  |
| 554    | No file  | `6d0f8a94b490`  |
| 542    | No file  | `6d0f8a94b490`  |
| 532    | No file  | `6d0f8a94b490`  |
| 531    | No file  | `6d0f8a94b490`  |
| 526    | No file  | `6d0f8a94b490`  |
| 521    | No file  | `6d0f8a94b490`  |
| 517    | No file  | `6d0f8a94b490`  |
| 510    | No file  | `6d0f8a94b490`  |
| 508    | No file  | `6d0f8a94b490`  |
| 504    | No file  | `6d0f8a94b490`  |
| 497    | No file  | `6d0f8a94b490`  |
| 491    | No file  | `6d0f8a94b490`  |
| 485    | No file  | `6d0f8a94b490`  |
| 478    | No file  | `6d0f8a94b490`  |
| 472    | No file  | `6d0f8a94b490`  |
| 466    | No file  | `6d0f8a94b490`  |
| 457    | No file  | `6d0f8a94b490`  |
| 452    | No file  | `6d0f8a94b490`  |
| 449    | No file  | `6d0f8a94b490`  |
| 435    | No file  | `6d0f8a94b490`  |

<!-- versions:end -->

## Companion Files

None. The handler names both quests with their LOC type 18 titles and the
title with its LOC type 1 name from `languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type | Field            | Notes                                                                     |
| ------- | ---- | ---------------- | ------------------------------------------------------------------------- |
| `+0x00` | u32  | season_no        | Class number; `3` on client 3474, `1` on client 3251                      |
| `+0x04` | u64  | start_time       | Unix seconds; enrollment opens, `2026-07-30 09:00 UTC` on client 3474     |
| `+0x0c` | u64  | graduation_time  | Unix seconds; graduation opens, `2026-11-05 09:00 UTC` on client 3474     |
| `+0x14` | u64  | close_time       | Unix seconds; enrollment closes, `2026-08-20 09:00 UTC` on client 3474    |
| `+0x1c` | u64  | end_time         | Unix seconds; graduation and the class end, `2026-11-12 09:00 UTC` on client 3474 |
| `+0x24` | u32  | enter_quest      | Packed quest ID `(quest_id << 16) \| quest_chain_id`; `2308/1` "[Olvia Academy] Your First Steps In" |
| `+0x28` | u32  | graduation_quest | Packed quest ID; `2309/1` "[Olvia Academy] Graduation with Honor"         |
| `+0x2c` | u32  | title_id         | Class title, LOC type 1; `3687` "Olvia Academy Class 3" on client 3474    |

The fields fill the 48-byte file exactly.

## Field Names

No reference source has the file: it first appears on client 3186 (absent
on client 3177), and a private server's `DataSheets.bexcel` on client 1784
has no sheet with `Olvia` or `Academy` in its name. The names come from the
client Lua and LOC of client 3474:

- `season_no`: the Lua reads `ToClient_GetOlviaAcademyCurrentSeasonNo()`
  into `seasonNo` for the invitation letter (`LUA_OLVIAACADEMY_INVITATION_MESSAGE`,
  "Class {seasonNo} Enrollment Period"), the pass window and
  `panel_widget_localquestalert_1.luac` (`olviaAcademySeasonNo`). The value
  matches `title_id` on both clients: `1` with title `3685` "Olvia Academy
  Class 1" on client 3251, `3` with title `3687` "Olvia Academy Class 3" on
  client 3474 (title `3686` is "Olvia Academy Class 2").
- The four times: `panel_window_olviaacademy_main_all_1.luac` reads
  `ToClient_GetOlviaAcademyStartTime()`, `...CloseTime()`,
  `...GraduateTime()` and `...EndTime()` and fills
  `LUA_OLVIA_ACADEMY_MAINPAGE_SEASON_ENTER` ("Enrolled: {starttime} after
  maintenance - {closetime} before maintenance") and
  `LUA_OLVIA_ACADEMY_MAINPAGE_SEASON_GRADUATION` ("Graduation:
  {gradutiontime} after maintenance - {endtime} before maintenance").
  Enrollment closes before graduation opens, so the four times order as
  `start_time` <= `close_time` < `graduation_time` <= `end_time`. That order
  fits the stored values one way only on both clients: `+0x04` is the
  earliest (`start_time`), `+0x14` the second (`close_time`), `+0x0c` the
  third (`graduation_time`) and `+0x1c` the latest (`end_time`). The file
  stores them as start, graduation, close, end.
- `enter_quest`: `PaGlobalFunc_OlviaAcademy_Main_Open`
  (`panel_window_olviaacademy_main_all_2.luac`) reads
  `ToClient_GetOlviaAcademyEnterQuestNo()` and opens the window only when
  that quest is cleared. The LOC text of quest 4472/1 says to "complete
  "[Olvia Academy] Your First Steps In" to enroll", which is `2308/1`.
- `graduation_quest`: no Lua reads it. Its quest `2309/1` is "[Olvia
  Academy] Graduation with Honor" ("attend the graduation ceremony, and
  claim your glorious diploma").

## Notes

- Raw bytes on client 3474: `03 00 00 00 90 12 6B 6A 00 00 00 00 90 45 EC 6A
  00 00 00 00 10 C2 86 6A 00 00 00 00 10 80 F5 6A 00 00 00 00 04 09 01 00
  05 09 01 00 67 0E 00 00`.
- Client 3251 holds class 1 in the same 48 bytes: `start_time`
  `2026-01-22`, `graduation_time` `2026-04-09`, `close_time` `2026-02-12`,
  `end_time` `2026-04-16` (all 09:00 UTC), the same two quests and title
  `3685`. On both clients every time is a Thursday at 09:00 UTC,
  enrollment runs 3 weeks and graduation the last week. Class 1 runs 12
  weeks, class 3 runs 15.
- The two quests are the only quests of chains 2308 and 2309 in
  `olviaacademycurriculumquestlist.bss`.
- The handler for the option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`. It shows the times as UTC date and time and the quests as
  `chain/quest` with their titles; the record keeps the stored values.
- The curricula are in
  [`olviaacademycurriculumss.bss`](olviaacademycurriculumss_bss.md), the
  pass tabs in
  [`olviaacademypassstaticstatusmanager.bss`](olviaacademypassstaticstatusmanager_bss.md).
  Neither holds a class number, and no subject lists `enter_quest` or
  `graduation_quest`, so this view has no link to them.

