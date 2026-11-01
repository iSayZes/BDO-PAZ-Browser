# `petfusionnewaddrateinfo.dbss` Format

## Purpose

The add rates of a pet exchange: how much each other pet raises the success
chance of the main pet (the first pet registered in the exchange window), by
the main pet's tier and the other pet's tier. The base chance and the result
tiers are in [`petfusionnew.dbss`](petfusionnew_dbss.md). Tiers are stored
from 0, as `tier` of [`pet.dbss`](pet_dbss.md) stores them: `0` is Tier 1.
Rates are on the 1,000,000 = 100% scale. The file has no PABR magic, no
count and no trailer: four rows of add rates, then one more array of four
values.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                           | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------------------ | ----- | ------- | --------- |
| 1      | 1261 and later | `petfusionnewaddrateinfo.dbss` | 80    | 4 Row   | 16        |

| Layout | File                           | Known         | Unknown    |
| ------ | ------------------------------ | ------------- | ---------- |
| 1      | `petfusionnewaddrateinfo.dbss` | 80 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `e09d2a677a06`  |
| 3482   | Layout 1 | `e09d2a677a06`  |
| 3474   | Layout 1 | `e09d2a677a06`  |
| 3473   | Layout 1 | `e09d2a677a06`  |
| 3464   | Layout 1 | `e09d2a677a06`  |
| 3458   | Layout 1 | `e09d2a677a06`  |
| 3454   | Layout 1 | `e09d2a677a06`  |
| 3444   | Layout 1 | `e09d2a677a06`  |
| 3435   | Layout 1 | `e09d2a677a06`  |
| 3426   | Layout 1 | `e09d2a677a06`  |
| 3418   | Layout 1 | `e09d2a677a06`  |
| 3412   | Layout 1 | `e09d2a677a06`  |
| 3402   | Layout 1 | `e09d2a677a06`  |
| 3396   | Layout 1 | `e09d2a677a06`  |
| 3387   | Layout 1 | `e09d2a677a06`  |
| 3381   | Layout 1 | `e09d2a677a06`  |
| 3373   | Layout 1 | `e09d2a677a06`  |
| 3364   | Layout 1 | `e09d2a677a06`  |
| 3356   | Layout 1 | `e09d2a677a06`  |
| 3349   | Layout 1 | `e09d2a677a06`  |
| 3342   | Layout 1 | `e09d2a677a06`  |
| 3335   | Layout 1 | `e09d2a677a06`  |
| 3326   | Layout 1 | `e09d2a677a06`  |
| 3321   | Layout 1 | `e09d2a677a06`  |
| 3314   | Layout 1 | `e09d2a677a06`  |
| 3303   | Layout 1 | `e09d2a677a06`  |
| 3302   | Layout 1 | `e09d2a677a06`  |
| 3293   | Layout 1 | `e09d2a677a06`  |
| 3283   | Layout 1 | `e09d2a677a06`  |
| 3275   | Layout 1 | `e09d2a677a06`  |
| 3267   | Layout 1 | `e09d2a677a06`  |
| 3258   | Layout 1 | `e09d2a677a06`  |
| 3251   | Layout 1 | `e09d2a677a06`  |
| 3242   | Layout 1 | `e09d2a677a06`  |
| 3235   | Layout 1 | `e09d2a677a06`  |
| 3229   | Layout 1 | `e09d2a677a06`  |
| 3212   | Layout 1 | `e09d2a677a06`  |
| 3203   | Layout 1 | `e09d2a677a06`  |
| 3193   | Layout 1 | `e09d2a677a06`  |
| 3186   | Layout 1 | `e09d2a677a06`  |
| 3177   | Layout 1 | `e09d2a677a06`  |
| 3169   | Layout 1 | `e09d2a677a06`  |
| 3158   | Layout 1 | `e09d2a677a06`  |
| 3151   | Layout 1 | `e09d2a677a06`  |
| 3144   | Layout 1 | `e09d2a677a06`  |
| 3133   | Layout 1 | `e09d2a677a06`  |
| 3125   | Layout 1 | `e09d2a677a06`  |
| 3118   | Layout 1 | `e09d2a677a06`  |
| 3111   | Layout 1 | `e09d2a677a06`  |
| 3103   | Layout 1 | `e09d2a677a06`  |
| 3095   | Layout 1 | `e09d2a677a06`  |
| 3086   | Layout 1 | `e09d2a677a06`  |
| 3072   | Layout 1 | `e09d2a677a06`  |
| 3062   | Layout 1 | `e09d2a677a06`  |
| 3052   | Layout 1 | `e09d2a677a06`  |
| 3045   | Layout 1 | `e09d2a677a06`  |
| 3037   | Layout 1 | `e09d2a677a06`  |
| 3030   | Layout 1 | `e09d2a677a06`  |
| 3021   | Layout 1 | `e09d2a677a06`  |
| 3012   | Layout 1 | `e09d2a677a06`  |
| 3002   | Layout 1 | `e09d2a677a06`  |
| 2995   | Layout 1 | `e09d2a677a06`  |
| 2987   | Layout 1 | `e09d2a677a06`  |
| 2978   | Layout 1 | `e09d2a677a06`  |
| 2970   | Layout 1 | `e09d2a677a06`  |
| 2959   | Layout 1 | `e09d2a677a06`  |
| 2951   | Layout 1 | `e09d2a677a06`  |
| 2942   | Layout 1 | `e09d2a677a06`  |
| 2935   | Layout 1 | `e09d2a677a06`  |
| 2932   | Layout 1 | `e09d2a677a06`  |
| 2923   | Layout 1 | `e09d2a677a06`  |
| 2919   | Layout 1 | `e09d2a677a06`  |
| 2907   | Layout 1 | `e09d2a677a06`  |
| 2900   | Layout 1 | `e09d2a677a06`  |
| 2891   | Layout 1 | `e09d2a677a06`  |
| 2882   | Layout 1 | `e09d2a677a06`  |
| 2872   | Layout 1 | `e09d2a677a06`  |
| 2863   | Layout 1 | `e09d2a677a06`  |
| 2855   | Layout 1 | `e09d2a677a06`  |
| 2849   | Layout 1 | `e09d2a677a06`  |
| 2844   | Layout 1 | `e09d2a677a06`  |
| 2834   | Layout 1 | `e09d2a677a06`  |
| 2825   | Layout 1 | `e09d2a677a06`  |
| 2819   | Layout 1 | `e09d2a677a06`  |
| 2811   | Layout 1 | `e09d2a677a06`  |
| 2803   | Layout 1 | `e09d2a677a06`  |
| 2794   | Layout 1 | `e09d2a677a06`  |
| 2783   | Layout 1 | `e09d2a677a06`  |
| 2774   | Layout 1 | `e09d2a677a06`  |
| 2765   | Layout 1 | `e09d2a677a06`  |
| 2756   | Layout 1 | `e09d2a677a06`  |
| 2750   | Layout 1 | `e09d2a677a06`  |
| 2743   | Layout 1 | `e09d2a677a06`  |
| 2736   | Layout 1 | `e09d2a677a06`  |
| 2726   | Layout 1 | `e09d2a677a06`  |
| 2717   | Layout 1 | `e09d2a677a06`  |
| 2709   | Layout 1 | `e09d2a677a06`  |
| 2703   | Layout 1 | `e09d2a677a06`  |
| 2695   | Layout 1 | `e09d2a677a06`  |
| 2684   | Layout 1 | `e09d2a677a06`  |
| 2672   | Layout 1 | `e09d2a677a06`  |
| 2665   | Layout 1 | `e09d2a677a06`  |
| 2657   | Layout 1 | `e09d2a677a06`  |
| 2649   | Layout 1 | `e09d2a677a06`  |
| 2644   | Layout 1 | `e09d2a677a06`  |
| 2637   | Layout 1 | `e09d2a677a06`  |
| 2629   | Layout 1 | `e09d2a677a06`  |
| 2619   | Layout 1 | `e09d2a677a06`  |
| 2612   | Layout 1 | `e09d2a677a06`  |
| 2606   | Layout 1 | `e09d2a677a06`  |
| 2602   | Layout 1 | `e09d2a677a06`  |
| 2601   | Layout 1 | `e09d2a677a06`  |
| 2592   | Layout 1 | `e09d2a677a06`  |
| 2583   | Layout 1 | `e09d2a677a06`  |
| 2575   | Layout 1 | `e09d2a677a06`  |
| 2567   | Layout 1 | `e09d2a677a06`  |
| 2560   | Layout 1 | `e09d2a677a06`  |
| 2553   | Layout 1 | `e09d2a677a06`  |
| 2545   | Layout 1 | `e09d2a677a06`  |
| 2538   | Layout 1 | `e09d2a677a06`  |
| 2529   | Layout 1 | `e09d2a677a06`  |
| 2519   | Layout 1 | `e09d2a677a06`  |
| 2513   | Layout 1 | `e09d2a677a06`  |
| 2510   | Layout 1 | `e09d2a677a06`  |
| 2507   | Layout 1 | `e09d2a677a06`  |
| 2503   | Layout 1 | `e09d2a677a06`  |
| 2498   | Layout 1 | `e09d2a677a06`  |
| 2492   | Layout 1 | `e09d2a677a06`  |
| 2487   | Layout 1 | `e09d2a677a06`  |
| 2480   | Layout 1 | `e09d2a677a06`  |
| 2474   | Layout 1 | `e09d2a677a06`  |
| 2468   | Layout 1 | `e09d2a677a06`  |
| 2460   | Layout 1 | `e09d2a677a06`  |
| 2453   | Layout 1 | `e09d2a677a06`  |
| 2444   | Layout 1 | `e09d2a677a06`  |
| 2438   | Layout 1 | `e09d2a677a06`  |
| 2434   | Layout 1 | `e09d2a677a06`  |
| 2429   | Layout 1 | `e09d2a677a06`  |
| 2421   | Layout 1 | `e09d2a677a06`  |
| 2414   | Layout 1 | `e09d2a677a06`  |
| 2407   | Layout 1 | `e09d2a677a06`  |
| 2401   | Layout 1 | `e09d2a677a06`  |
| 2397   | Layout 1 | `e09d2a677a06`  |
| 2393   | Layout 1 | `e09d2a677a06`  |
| 2384   | Layout 1 | `e09d2a677a06`  |
| 2378   | Layout 1 | `e09d2a677a06`  |
| 2372   | Layout 1 | `e09d2a677a06`  |
| 2358   | Layout 1 | `e09d2a677a06`  |
| 2352   | Layout 1 | `e09d2a677a06`  |
| 2347   | Layout 1 | `e09d2a677a06`  |
| 2343   | Layout 1 | `e09d2a677a06`  |
| 2335   | Layout 1 | `e09d2a677a06`  |
| 2327   | Layout 1 | `e09d2a677a06`  |
| 2324   | Layout 1 | `e09d2a677a06`  |
| 2319   | Layout 1 | `e09d2a677a06`  |
| 2313   | Layout 1 | `e09d2a677a06`  |
| 2308   | Layout 1 | `e09d2a677a06`  |
| 2302   | Layout 1 | `e09d2a677a06`  |
| 2295   | Layout 1 | `e09d2a677a06`  |
| 2290   | Layout 1 | `e09d2a677a06`  |
| 2284   | Layout 1 | `e09d2a677a06`  |
| 2276   | Layout 1 | `e09d2a677a06`  |
| 2269   | Layout 1 | `e09d2a677a06`  |
| 2259   | Layout 1 | `e09d2a677a06`  |
| 2250   | Layout 1 | `e09d2a677a06`  |
| 2243   | Layout 1 | `e09d2a677a06`  |
| 2235   | Layout 1 | `e09d2a677a06`  |
| 2229   | Layout 1 | `e09d2a677a06`  |
| 2224   | Layout 1 | `e09d2a677a06`  |
| 2218   | Layout 1 | `e09d2a677a06`  |
| 2215   | Layout 1 | `e09d2a677a06`  |
| 2207   | Layout 1 | `e09d2a677a06`  |
| 2203   | Layout 1 | `e09d2a677a06`  |
| 2196   | Layout 1 | `e09d2a677a06`  |
| 2192   | Layout 1 | `e09d2a677a06`  |
| 2189   | Layout 1 | `e09d2a677a06`  |
| 2183   | Layout 1 | `e09d2a677a06`  |
| 2179   | Layout 1 | `e09d2a677a06`  |
| 2171   | Layout 1 | `e09d2a677a06`  |
| 2163   | Layout 1 | `e09d2a677a06`  |
| 2156   | Layout 1 | `e09d2a677a06`  |
| 2151   | Layout 1 | `e09d2a677a06`  |
| 2147   | Layout 1 | `e09d2a677a06`  |
| 2142   | Layout 1 | `e09d2a677a06`  |
| 2138   | Layout 1 | `e09d2a677a06`  |
| 2134   | Layout 1 | `e09d2a677a06`  |
| 2130   | Layout 1 | `e09d2a677a06`  |
| 2122   | Layout 1 | `e09d2a677a06`  |
| 2107   | Layout 1 | `e09d2a677a06`  |
| 2098   | Layout 1 | `e09d2a677a06`  |
| 2089   | Layout 1 | `e09d2a677a06`  |
| 2081   | Layout 1 | `e09d2a677a06`  |
| 2073   | Layout 1 | `e09d2a677a06`  |
| 2067   | Layout 1 | `e09d2a677a06`  |
| 2063   | Layout 1 | `e09d2a677a06`  |
| 2059   | Layout 1 | `e09d2a677a06`  |
| 2052   | Layout 1 | `e09d2a677a06`  |
| 2044   | Layout 1 | `e09d2a677a06`  |
| 2039   | Layout 1 | `e09d2a677a06`  |
| 2032   | Layout 1 | `e09d2a677a06`  |
| 2025   | Layout 1 | `e09d2a677a06`  |
| 2011   | Layout 1 | `e09d2a677a06`  |
| 2005   | Layout 1 | `e09d2a677a06`  |
| 2000   | Layout 1 | `e09d2a677a06`  |
| 1996   | Layout 1 | `e09d2a677a06`  |
| 1991   | Layout 1 | `e09d2a677a06`  |
| 1985   | Layout 1 | `e09d2a677a06`  |
| 1980   | Layout 1 | `e09d2a677a06`  |
| 1969   | Layout 1 | `e09d2a677a06`  |
| 1964   | Layout 1 | `e09d2a677a06`  |
| 1958   | Layout 1 | `e09d2a677a06`  |
| 1950   | Layout 1 | `e09d2a677a06`  |
| 1945   | Layout 1 | `e09d2a677a06`  |
| 1937   | Layout 1 | `e09d2a677a06`  |
| 1933   | Layout 1 | `e09d2a677a06`  |
| 1927   | Layout 1 | `e09d2a677a06`  |
| 1921   | Layout 1 | `e09d2a677a06`  |
| 1914   | Layout 1 | `e09d2a677a06`  |
| 1908   | Layout 1 | `e09d2a677a06`  |
| 1897   | Layout 1 | `e09d2a677a06`  |
| 1892   | Layout 1 | `e09d2a677a06`  |
| 1886   | Layout 1 | `e09d2a677a06`  |
| 1881   | Layout 1 | `e09d2a677a06`  |
| 1871   | Layout 1 | `e09d2a677a06`  |
| 1866   | Layout 1 | `e09d2a677a06`  |
| 1862   | Layout 1 | `e09d2a677a06`  |
| 1854   | Layout 1 | `e09d2a677a06`  |
| 1846   | Layout 1 | `e09d2a677a06`  |
| 1838   | Layout 1 | `e09d2a677a06`  |
| 1832   | Layout 1 | `e09d2a677a06`  |
| 1826   | Layout 1 | `e09d2a677a06`  |
| 1822   | Layout 1 | `e09d2a677a06`  |
| 1818   | Layout 1 | `e09d2a677a06`  |
| 1804   | Layout 1 | `e09d2a677a06`  |
| 1794   | Layout 1 | `e09d2a677a06`  |
| 1790   | Layout 1 | `e09d2a677a06`  |
| 1784   | Layout 1 | `e09d2a677a06`  |
| 1774   | Layout 1 | `e09d2a677a06`  |
| 1771   | Layout 1 | `e09d2a677a06`  |
| 1762   | Layout 1 | `e09d2a677a06`  |
| 1759   | Layout 1 | `e09d2a677a06`  |
| 1754   | Layout 1 | `e09d2a677a06`  |
| 1749   | Layout 1 | `e09d2a677a06`  |
| 1743   | Layout 1 | `e09d2a677a06`  |
| 1737   | Layout 1 | `e09d2a677a06`  |
| 1731   | Layout 1 | `e09d2a677a06`  |
| 1725   | Layout 1 | `e09d2a677a06`  |
| 1717   | Layout 1 | `e09d2a677a06`  |
| 1710   | Layout 1 | `e09d2a677a06`  |
| 1704   | Layout 1 | `e09d2a677a06`  |
| 1698   | Layout 1 | `e09d2a677a06`  |
| 1690   | Layout 1 | `e09d2a677a06`  |
| 1685   | Layout 1 | `e09d2a677a06`  |
| 1680   | Layout 1 | `e09d2a677a06`  |
| 1674   | Layout 1 | `e09d2a677a06`  |
| 1668   | Layout 1 | `e09d2a677a06`  |
| 1659   | Layout 1 | `e09d2a677a06`  |
| 1649   | Layout 1 | `e09d2a677a06`  |
| 1642   | Layout 1 | `e09d2a677a06`  |
| 1636   | Layout 1 | `e09d2a677a06`  |
| 1628   | Layout 1 | `e09d2a677a06`  |
| 1622   | Layout 1 | `e09d2a677a06`  |
| 1614   | Layout 1 | `e09d2a677a06`  |
| 1608   | Layout 1 | `e09d2a677a06`  |
| 1602   | Layout 1 | `e09d2a677a06`  |
| 1598   | Layout 1 | `e09d2a677a06`  |
| 1594   | Layout 1 | `e09d2a677a06`  |
| 1590   | Layout 1 | `e09d2a677a06`  |
| 1587   | Layout 1 | `e09d2a677a06`  |
| 1584   | Layout 1 | `e09d2a677a06`  |
| 1579   | Layout 1 | `e09d2a677a06`  |
| 1572   | Layout 1 | `e09d2a677a06`  |
| 1565   | Layout 1 | `e09d2a677a06`  |
| 1559   | Layout 1 | `e09d2a677a06`  |
| 1554   | Layout 1 | `e09d2a677a06`  |
| 1547   | Layout 1 | `e09d2a677a06`  |
| 1537   | Layout 1 | `e09d2a677a06`  |
| 1529   | Layout 1 | `e09d2a677a06`  |
| 1524   | Layout 1 | `e09d2a677a06`  |
| 1519   | Layout 1 | `e09d2a677a06`  |
| 1509   | Layout 1 | `e09d2a677a06`  |
| 1506   | Layout 1 | `e09d2a677a06`  |
| 1504   | Layout 1 | `e09d2a677a06`  |
| 1500   | Layout 1 | `e09d2a677a06`  |
| 1493   | Layout 1 | `e09d2a677a06`  |
| 1489   | Layout 1 | `e09d2a677a06`  |
| 1485   | Layout 1 | `e09d2a677a06`  |
| 1481   | Layout 1 | `e09d2a677a06`  |
| 1474   | Layout 1 | `e09d2a677a06`  |
| 1466   | Layout 1 | `e09d2a677a06`  |
| 1462   | Layout 1 | `e09d2a677a06`  |
| 1459   | Layout 1 | `e09d2a677a06`  |
| 1453   | Layout 1 | `e09d2a677a06`  |
| 1450   | Layout 1 | `e09d2a677a06`  |
| 1445   | Layout 1 | `e09d2a677a06`  |
| 1439   | Layout 1 | `e09d2a677a06`  |
| 1433   | Layout 1 | `e09d2a677a06`  |
| 1430   | Layout 1 | `e09d2a677a06`  |
| 1426   | Layout 1 | `e09d2a677a06`  |
| 1421   | Layout 1 | `e09d2a677a06`  |
| 1417   | Layout 1 | `e09d2a677a06`  |
| 1416   | Layout 1 | `e09d2a677a06`  |
| 1409   | Layout 1 | `e09d2a677a06`  |
| 1405   | Layout 1 | `e09d2a677a06`  |
| 1401   | Layout 1 | `e09d2a677a06`  |
| 1396   | Layout 1 | `e09d2a677a06`  |
| 1391   | Layout 1 | `e09d2a677a06`  |
| 1390   | Layout 1 | `e09d2a677a06`  |
| 1386   | Layout 1 | `e09d2a677a06`  |
| 1381   | Layout 1 | `e09d2a677a06`  |
| 1379   | Layout 1 | `e09d2a677a06`  |
| 1372   | Layout 1 | `e09d2a677a06`  |
| 1366   | Layout 1 | `e09d2a677a06`  |
| 1364   | Layout 1 | `e09d2a677a06`  |
| 1363   | Layout 1 | `e09d2a677a06`  |
| 1360   | Layout 1 | `e09d2a677a06`  |
| 1358   | Layout 1 | `e09d2a677a06`  |
| 1355   | Layout 1 | `e09d2a677a06`  |
| 1351   | Layout 1 | `e09d2a677a06`  |
| 1348   | Layout 1 | `e09d2a677a06`  |
| 1346   | Layout 1 | `e09d2a677a06`  |
| 1341   | Layout 1 | `e09d2a677a06`  |
| 1340   | Layout 1 | `e09d2a677a06`  |
| 1338   | Layout 1 | `e09d2a677a06`  |
| 1335   | Layout 1 | `e09d2a677a06`  |
| 1333   | Layout 1 | `e09d2a677a06`  |
| 1329   | Layout 1 | `e09d2a677a06`  |
| 1327   | Layout 1 | `e09d2a677a06`  |
| 1324   | Layout 1 | `e09d2a677a06`  |
| 1321   | Layout 1 | `e09d2a677a06`  |
| 1319   | Layout 1 | `e09d2a677a06`  |
| 1318   | Layout 1 | `e09d2a677a06`  |
| 1316   | Layout 1 | `e09d2a677a06`  |
| 1313   | Layout 1 | `e09d2a677a06`  |
| 1311   | Layout 1 | `e09d2a677a06`  |
| 1309   | Layout 1 | `e09d2a677a06`  |
| 1304   | Layout 1 | `e09d2a677a06`  |
| 1292   | Layout 1 | `e09d2a677a06`  |
| 1286   | Layout 1 | `e09d2a677a06`  |
| 1280   | No file  | `e09d2a677a06`  |
| 1276   | No file  | `e09d2a677a06`  |
| 1267   | Layout 1 | `e09d2a677a06`  |
| 1261   | Layout 1 | `e09d2a677a06`  |
| 1256   | No file  | `e09d2a677a06`  |
| 1250   | No file  | `e09d2a677a06`  |
| 1246   | No file  | `e09d2a677a06`  |
| 1239   | No file  | `e09d2a677a06`  |
| 1230   | No file  | `e09d2a677a06`  |
| 1226   | No file  | `e09d2a677a06`  |
| 1220   | No file  | `e09d2a677a06`  |
| 1217   | No file  | `e09d2a677a06`  |
| 1211   | No file  | `e09d2a677a06`  |
| 1210   | No file  | `e09d2a677a06`  |
| 1208   | No file  | `e09d2a677a06`  |
| 1203   | No file  | `e09d2a677a06`  |
| 1197   | No file  | `e09d2a677a06`  |
| 1194   | No file  | `e09d2a677a06`  |
| 1192   | No file  | `e09d2a677a06`  |
| 1187   | No file  | `e09d2a677a06`  |
| 1183   | No file  | `e09d2a677a06`  |
| 1177   | No file  | `e09d2a677a06`  |
| 1173   | No file  | `e09d2a677a06`  |
| 1167   | No file  | `e09d2a677a06`  |
| 1164   | No file  | `e09d2a677a06`  |
| 1156   | No file  | `e09d2a677a06`  |
| 1149   | No file  | `e09d2a677a06`  |
| 1144   | No file  | `e09d2a677a06`  |
| 1137   | No file  | `e09d2a677a06`  |
| 1132   | No file  | `e09d2a677a06`  |
| 1127   | No file  | `e09d2a677a06`  |
| 1122   | No file  | `e09d2a677a06`  |
| 1118   | No file  | `e09d2a677a06`  |
| 1114   | No file  | `e09d2a677a06`  |
| 1109   | No file  | `e09d2a677a06`  |
| 1102   | No file  | `e09d2a677a06`  |
| 1096   | No file  | `e09d2a677a06`  |
| 1088   | No file  | `e09d2a677a06`  |
| 1081   | No file  | `e09d2a677a06`  |
| 1076   | No file  | `e09d2a677a06`  |
| 1069   | No file  | `e09d2a677a06`  |
| 1064   | No file  | `e09d2a677a06`  |
| 1058   | No file  | `e09d2a677a06`  |
| 1051   | No file  | `e09d2a677a06`  |
| 1044   | No file  | `e09d2a677a06`  |
| 1036   | No file  | `e09d2a677a06`  |
| 1026   | No file  | `e09d2a677a06`  |
| 1016   | No file  | `e09d2a677a06`  |
| 1009   | No file  | `e09d2a677a06`  |
| 1005   | No file  | `e09d2a677a06`  |
| 1000   | No file  | `e09d2a677a06`  |
| 998    | No file  | `e09d2a677a06`  |
| 990    | No file  | `e09d2a677a06`  |
| 979    | No file  | `e09d2a677a06`  |
| 972    | No file  | `e09d2a677a06`  |
| 963    | No file  | `e09d2a677a06`  |
| 955    | No file  | `e09d2a677a06`  |
| 946    | No file  | `e09d2a677a06`  |
| 938    | No file  | `e09d2a677a06`  |
| 927    | No file  | `e09d2a677a06`  |
| 911    | No file  | `e09d2a677a06`  |
| 904    | No file  | `e09d2a677a06`  |
| 899    | No file  | `e09d2a677a06`  |
| 894    | No file  | `e09d2a677a06`  |
| 885    | No file  | `e09d2a677a06`  |
| 879    | No file  | `e09d2a677a06`  |
| 872    | No file  | `e09d2a677a06`  |
| 864    | No file  | `e09d2a677a06`  |
| 855    | No file  | `e09d2a677a06`  |
| 853    | No file  | `e09d2a677a06`  |
| 845    | No file  | `e09d2a677a06`  |
| 837    | No file  | `e09d2a677a06`  |
| 829    | No file  | `e09d2a677a06`  |
| 822    | No file  | `e09d2a677a06`  |
| 814    | No file  | `e09d2a677a06`  |
| 805    | No file  | `e09d2a677a06`  |
| 794    | No file  | `e09d2a677a06`  |
| 787    | No file  | `e09d2a677a06`  |
| 780    | No file  | `e09d2a677a06`  |
| 771    | No file  | `e09d2a677a06`  |
| 760    | No file  | `e09d2a677a06`  |
| 748    | No file  | `e09d2a677a06`  |
| 741    | No file  | `e09d2a677a06`  |
| 736    | No file  | `e09d2a677a06`  |
| 731    | No file  | `e09d2a677a06`  |
| 723    | No file  | `e09d2a677a06`  |
| 711    | No file  | `e09d2a677a06`  |
| 707    | No file  | `e09d2a677a06`  |
| 697    | No file  | `e09d2a677a06`  |
| 689    | No file  | `e09d2a677a06`  |
| 683    | No file  | `e09d2a677a06`  |
| 678    | No file  | `e09d2a677a06`  |
| 670    | No file  | `e09d2a677a06`  |
| 661    | No file  | `e09d2a677a06`  |
| 656    | No file  | `e09d2a677a06`  |
| 652    | No file  | `e09d2a677a06`  |
| 643    | No file  | `e09d2a677a06`  |
| 637    | No file  | `e09d2a677a06`  |
| 630    | No file  | `e09d2a677a06`  |
| 627    | No file  | `e09d2a677a06`  |
| 621    | No file  | `e09d2a677a06`  |
| 617    | No file  | `e09d2a677a06`  |
| 615    | No file  | `e09d2a677a06`  |
| 606    | No file  | `e09d2a677a06`  |
| 599    | No file  | `e09d2a677a06`  |
| 592    | No file  | `e09d2a677a06`  |
| 586    | No file  | `e09d2a677a06`  |
| 577    | No file  | `e09d2a677a06`  |
| 569    | No file  | `e09d2a677a06`  |
| 561    | No file  | `e09d2a677a06`  |
| 554    | No file  | `e09d2a677a06`  |
| 542    | No file  | `e09d2a677a06`  |
| 532    | No file  | `e09d2a677a06`  |
| 531    | No file  | `e09d2a677a06`  |
| 526    | No file  | `e09d2a677a06`  |
| 521    | No file  | `e09d2a677a06`  |
| 517    | No file  | `e09d2a677a06`  |
| 510    | No file  | `e09d2a677a06`  |
| 508    | No file  | `e09d2a677a06`  |
| 504    | No file  | `e09d2a677a06`  |
| 497    | No file  | `e09d2a677a06`  |
| 491    | No file  | `e09d2a677a06`  |
| 485    | No file  | `e09d2a677a06`  |
| 478    | No file  | `e09d2a677a06`  |
| 472    | No file  | `e09d2a677a06`  |
| 466    | No file  | `e09d2a677a06`  |
| 457    | No file  | `e09d2a677a06`  |
| 452    | No file  | `e09d2a677a06`  |
| 449    | No file  | `e09d2a677a06`  |
| 435    | No file  | `e09d2a677a06`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type   | Field      | Notes                                                           |
| ------- | ------ | ---------- | --------------------------------------------------------------- |
| `+0x00` | Row[4] | rows       | See Row; the row index is the main pet's tier, from 0           |
| `+0x40` | u32[4] | gosphy_add_rate | Added by a Wizard Gosphy as the other pet, one rate per main pet tier, from 0 |

### Row (16 bytes)

| Offset  | Type | Field           | Notes                                                  |
| ------- | ---- | --------------- | ------------------------------------------------------ |
| `+0x00` | u32  | add_rate_tier_0 | Added by an other pet of tier `0` (Tier 1)             |
| `+0x04` | u32  | add_rate_tier_1 | Added by an other pet of tier `1` (Tier 2)             |
| `+0x08` | u32  | add_rate_tier_2 | Added by an other pet of tier `2` (Tier 3)             |
| `+0x0C` | u32  | add_rate_tier_3 | Added by an other pet of tier `3` (Tier 4)             |

## Add Rates

On client 3474, with tiers as the game numbers them:

| Main pet | + Tier 1 | + Tier 2 | + Tier 3 | + Tier 4 | + Wizard Gosphy |
| -------- | -------- | -------- | -------- | -------- | --------------- |
| Tier 1   | 55%      | 0%       | 0%       | 0%       | 65%             |
| Tier 2   | 65%      | 80%      | 0%       | 0%       | 75%             |
| Tier 3   | 15%      | 25%      | 35%      | 0%       | 20%             |
| Tier 4   | 0%       | 0%       | 0%       | 0%       | 0%              |

The zeros above the diagonal are pairs the window refuses: it takes no
other pet of a higher tier than the main pet (`PANEL_RENEWAL_PETLIST_TEMP_3`,
"The pet cannot have a higher tier than main pet."). A Tier 4 main pet
keeps its tier at 100% (see `petfusionnew.dbss`), so its row adds nothing.

With the base chance of 0.01% from `petfusionnew.dbss`, one other pet gives
the success chances Garmoth's
[pets guide](https://garmoth.com/guides/post/bdo-basics-pets) lists for the
six tier pairs of the first three rows: 55%, 65%, 80%, 15%, 25% and 35%.

## Field Names

The `Pet_Fusion_AddRate_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 has the columns `Tier`, `Tier0`,
`Tier1`, `Tier2` and `Tier3`, and 8 rows. Rows `Tier` `0` to `3` match
`rows` on all 16 values, `Tier0` to `Tier3` in column order (clients 1784
and 3474); their empty cells (`<null>`) are the zeros of the file. Rows
`Tier` `10` to `13` fill only `Tier0`, with `650000`, `750000`, `200000`
and `0`: the four values of `gosphy_add_rate`, in row order. The developer
workbook (`datasheet_petdatatable.xlsm`) has no note column on this sheet.

The client Lua of the exchange window (`panel_window_petfusion_all_1.luac`,
`setRate`) adds `ToClient_getAddFusionRate(mainPetTier, subTier, subRace)
/ 10000` percent for each other pet, which names the row as the main pet's
tier and the column as the other pet's tier. Both tiers are the stored
`getPetTier()` values, the same ones the window shows plus 1 (`LUA_SERVANT_TIER`).

## Notes

- Clients 1485, 1784, 2107, 2519, 3002, 3251 and 3474 ship the same 80
  bytes. Client 1230 stores them inside `petfusionnew.bss` after the
  `petfusionnew.dbss` rows (see [`petfusionnew.dbss`](petfusionnew_dbss.md)),
  so `gosphy_add_rate` is a separate array there too, not a fifth row.
- The window sums the add rates of up to four other pets, adds the base
  chance and caps the total at 100%.
- `gosphy_add_rate` is the add rate of [Wizard
  Gosphy](https://bdocodex.com/us/item/18423/), the pet
  `ToClient_getAddFusionRate` gets race `99` for. The Lua passes the other
  pet's race (`getPetRace()`, `species` in `pet.dbss`) to the add rate
  lookup, and race `99` is the one race the window treats apart: it cannot
  be the main pet (`PANEL_RENEWAL_PETLIST_TEMP_9`, "Wizard Gosphy cannot be
  the main pet.") and goes in only when the main pet has `is_joker_pet_use`
  set. The only race `99` record in `pet.dbss` is Wizard Gosphy (`55175`,
  tier `0`). In game on client 3474 my Tier 3 main pet with one Tier 1
  Wizard Gosphy shows "Tier 4 20%" and "Tier 3 80%", and with four Wizard
  Gosphys "Tier 4 80%": 0.01% base plus one or four times `200000`, where a
  normal Tier 1 pet adds `150000` (15%). Garmoth's pets guide says Wizard
  Gosphy "has increased chances of success for enhancing other pets".
