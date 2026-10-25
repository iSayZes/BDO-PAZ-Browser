# `petfusionnew.dbss` Format

## Purpose

The result tiers of a pet exchange, one row per tier of the main pet (the
first pet registered in the exchange window): the tier the new pet gets on
a success with its base chance, and the tier it gets otherwise. The other
pets in the exchange raise the first chance by the add rates of
[`petfusionnewaddrateinfo.dbss`](petfusionnewaddrateinfo_dbss.md).
Companion `petfusionnewoffset.dbss` lists where every row sits. Tiers are
stored from 0, as `tier` of [`pet.dbss`](pet_dbss.md) stores them: `0` is
Tier 1. Rates are on the 1,000,000 = 100% scale.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                      | Bytes | Records      | Row bytes |
| ------ | -------------- | ------------------------- | ----- | ------------ | --------- |
| 1      | 1346 and later | `petfusionnew.dbss`       | 68    | 4 Row        | 17        |
| 1      | 1346 and later | `petfusionnewoffset.dbss` | 40    | 4 Offset Row | 9         |

| Layout | File                      | Known         | Unknown    |
| ------ | ------------------------- | ------------- | ---------- |
| 1      | `petfusionnew.dbss`       | 68 B (100.0%) | 0 B (0.0%) |
| 1      | `petfusionnewoffset.dbss` | 40 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `162da9ce01a3`  |
| 3482   | Layout 1             | `162da9ce01a3`  |
| 3474   | Layout 1             | `162da9ce01a3`  |
| 3473   | Layout 1             | `162da9ce01a3`  |
| 3464   | Layout 1             | `162da9ce01a3`  |
| 3458   | Layout 1             | `162da9ce01a3`  |
| 3454   | Layout 1             | `162da9ce01a3`  |
| 3444   | Layout 1             | `162da9ce01a3`  |
| 3435   | Layout 1             | `162da9ce01a3`  |
| 3426   | Layout 1             | `162da9ce01a3`  |
| 3418   | Layout 1             | `162da9ce01a3`  |
| 3412   | Layout 1             | `162da9ce01a3`  |
| 3402   | Layout 1             | `162da9ce01a3`  |
| 3396   | Layout 1             | `162da9ce01a3`  |
| 3387   | Layout 1             | `162da9ce01a3`  |
| 3381   | Layout 1             | `162da9ce01a3`  |
| 3373   | Layout 1             | `162da9ce01a3`  |
| 3364   | Layout 1             | `162da9ce01a3`  |
| 3356   | Layout 1             | `162da9ce01a3`  |
| 3349   | Layout 1             | `162da9ce01a3`  |
| 3342   | Layout 1             | `162da9ce01a3`  |
| 3335   | Layout 1             | `162da9ce01a3`  |
| 3326   | Layout 1             | `162da9ce01a3`  |
| 3321   | Layout 1             | `162da9ce01a3`  |
| 3314   | Layout 1             | `162da9ce01a3`  |
| 3303   | Layout 1             | `162da9ce01a3`  |
| 3302   | Layout 1             | `162da9ce01a3`  |
| 3293   | Layout 1             | `162da9ce01a3`  |
| 3283   | Layout 1             | `162da9ce01a3`  |
| 3275   | Layout 1             | `162da9ce01a3`  |
| 3267   | Layout 1             | `162da9ce01a3`  |
| 3258   | Layout 1             | `162da9ce01a3`  |
| 3251   | Layout 1             | `162da9ce01a3`  |
| 3242   | Layout 1             | `162da9ce01a3`  |
| 3235   | Layout 1             | `162da9ce01a3`  |
| 3229   | Layout 1             | `162da9ce01a3`  |
| 3212   | Layout 1             | `162da9ce01a3`  |
| 3203   | Layout 1             | `162da9ce01a3`  |
| 3193   | Layout 1             | `162da9ce01a3`  |
| 3186   | Layout 1             | `162da9ce01a3`  |
| 3177   | Layout 1             | `162da9ce01a3`  |
| 3169   | Layout 1             | `162da9ce01a3`  |
| 3158   | Layout 1             | `162da9ce01a3`  |
| 3151   | Layout 1             | `162da9ce01a3`  |
| 3144   | Layout 1             | `162da9ce01a3`  |
| 3133   | Layout 1             | `162da9ce01a3`  |
| 3125   | Layout 1             | `162da9ce01a3`  |
| 3118   | Layout 1             | `162da9ce01a3`  |
| 3111   | Layout 1             | `162da9ce01a3`  |
| 3103   | Layout 1             | `162da9ce01a3`  |
| 3095   | Layout 1             | `162da9ce01a3`  |
| 3086   | Layout 1             | `162da9ce01a3`  |
| 3072   | Layout 1             | `162da9ce01a3`  |
| 3062   | Layout 1             | `162da9ce01a3`  |
| 3052   | Layout 1             | `162da9ce01a3`  |
| 3045   | Layout 1             | `162da9ce01a3`  |
| 3037   | Layout 1             | `162da9ce01a3`  |
| 3030   | Layout 1             | `162da9ce01a3`  |
| 3021   | Layout 1             | `162da9ce01a3`  |
| 3012   | Layout 1             | `162da9ce01a3`  |
| 3002   | Layout 1             | `162da9ce01a3`  |
| 2995   | Layout 1             | `162da9ce01a3`  |
| 2987   | Layout 1             | `162da9ce01a3`  |
| 2978   | Layout 1             | `162da9ce01a3`  |
| 2970   | Layout 1             | `162da9ce01a3`  |
| 2959   | Layout 1             | `162da9ce01a3`  |
| 2951   | Layout 1             | `162da9ce01a3`  |
| 2942   | Layout 1             | `162da9ce01a3`  |
| 2935   | Layout 1             | `162da9ce01a3`  |
| 2932   | Layout 1             | `162da9ce01a3`  |
| 2923   | Layout 1             | `162da9ce01a3`  |
| 2919   | Layout 1             | `162da9ce01a3`  |
| 2907   | Layout 1             | `162da9ce01a3`  |
| 2900   | Layout 1             | `162da9ce01a3`  |
| 2891   | Layout 1             | `162da9ce01a3`  |
| 2882   | Layout 1             | `162da9ce01a3`  |
| 2872   | Layout 1             | `162da9ce01a3`  |
| 2863   | Layout 1             | `162da9ce01a3`  |
| 2855   | Layout 1             | `162da9ce01a3`  |
| 2849   | Layout 1             | `162da9ce01a3`  |
| 2844   | Layout 1             | `162da9ce01a3`  |
| 2834   | Layout 1             | `162da9ce01a3`  |
| 2825   | Layout 1             | `162da9ce01a3`  |
| 2819   | Layout 1             | `162da9ce01a3`  |
| 2811   | Layout 1             | `162da9ce01a3`  |
| 2803   | Layout 1             | `162da9ce01a3`  |
| 2794   | Layout 1             | `162da9ce01a3`  |
| 2783   | Layout 1             | `162da9ce01a3`  |
| 2774   | Layout 1             | `162da9ce01a3`  |
| 2765   | Layout 1             | `162da9ce01a3`  |
| 2756   | Layout 1             | `162da9ce01a3`  |
| 2750   | Layout 1             | `162da9ce01a3`  |
| 2743   | Layout 1             | `162da9ce01a3`  |
| 2736   | Layout 1             | `162da9ce01a3`  |
| 2726   | Layout 1             | `162da9ce01a3`  |
| 2717   | Layout 1             | `162da9ce01a3`  |
| 2709   | Layout 1             | `162da9ce01a3`  |
| 2703   | Layout 1             | `162da9ce01a3`  |
| 2695   | Layout 1             | `162da9ce01a3`  |
| 2684   | Layout 1             | `162da9ce01a3`  |
| 2672   | Layout 1             | `162da9ce01a3`  |
| 2665   | Layout 1             | `162da9ce01a3`  |
| 2657   | Layout 1             | `162da9ce01a3`  |
| 2649   | Layout 1             | `162da9ce01a3`  |
| 2644   | Layout 1             | `162da9ce01a3`  |
| 2637   | Layout 1             | `162da9ce01a3`  |
| 2629   | Layout 1             | `162da9ce01a3`  |
| 2619   | Layout 1             | `162da9ce01a3`  |
| 2612   | Layout 1             | `162da9ce01a3`  |
| 2606   | Layout 1             | `162da9ce01a3`  |
| 2602   | Layout 1             | `162da9ce01a3`  |
| 2601   | Layout 1             | `162da9ce01a3`  |
| 2592   | Layout 1             | `162da9ce01a3`  |
| 2583   | Layout 1             | `162da9ce01a3`  |
| 2575   | Layout 1             | `162da9ce01a3`  |
| 2567   | Layout 1             | `162da9ce01a3`  |
| 2560   | Layout 1             | `162da9ce01a3`  |
| 2553   | Layout 1             | `162da9ce01a3`  |
| 2545   | Layout 1             | `162da9ce01a3`  |
| 2538   | Layout 1             | `162da9ce01a3`  |
| 2529   | Layout 1             | `162da9ce01a3`  |
| 2519   | Layout 1             | `162da9ce01a3`  |
| 2513   | Layout 1             | `162da9ce01a3`  |
| 2510   | Layout 1             | `162da9ce01a3`  |
| 2507   | Layout 1             | `162da9ce01a3`  |
| 2503   | Layout 1             | `162da9ce01a3`  |
| 2498   | Layout 1             | `162da9ce01a3`  |
| 2492   | Layout 1             | `162da9ce01a3`  |
| 2487   | Layout 1             | `162da9ce01a3`  |
| 2480   | Layout 1             | `162da9ce01a3`  |
| 2474   | Layout 1             | `162da9ce01a3`  |
| 2468   | Layout 1             | `162da9ce01a3`  |
| 2460   | Layout 1             | `162da9ce01a3`  |
| 2453   | Layout 1             | `162da9ce01a3`  |
| 2444   | Layout 1             | `162da9ce01a3`  |
| 2438   | Layout 1             | `162da9ce01a3`  |
| 2434   | Layout 1             | `162da9ce01a3`  |
| 2429   | Layout 1             | `162da9ce01a3`  |
| 2421   | Layout 1             | `162da9ce01a3`  |
| 2414   | Layout 1             | `162da9ce01a3`  |
| 2407   | Layout 1             | `162da9ce01a3`  |
| 2401   | Layout 1             | `162da9ce01a3`  |
| 2397   | Layout 1             | `162da9ce01a3`  |
| 2393   | Layout 1             | `162da9ce01a3`  |
| 2384   | Layout 1             | `162da9ce01a3`  |
| 2378   | Layout 1             | `162da9ce01a3`  |
| 2372   | Layout 1             | `162da9ce01a3`  |
| 2358   | Layout 1             | `162da9ce01a3`  |
| 2352   | Layout 1             | `162da9ce01a3`  |
| 2347   | Layout 1             | `162da9ce01a3`  |
| 2343   | Layout 1             | `162da9ce01a3`  |
| 2335   | Layout 1             | `162da9ce01a3`  |
| 2327   | Layout 1             | `162da9ce01a3`  |
| 2324   | Layout 1             | `162da9ce01a3`  |
| 2319   | Layout 1             | `162da9ce01a3`  |
| 2313   | Layout 1             | `162da9ce01a3`  |
| 2308   | Layout 1             | `162da9ce01a3`  |
| 2302   | Layout 1             | `162da9ce01a3`  |
| 2295   | Layout 1             | `162da9ce01a3`  |
| 2290   | Layout 1             | `162da9ce01a3`  |
| 2284   | Layout 1             | `162da9ce01a3`  |
| 2276   | Layout 1             | `162da9ce01a3`  |
| 2269   | Layout 1             | `162da9ce01a3`  |
| 2259   | Layout 1             | `162da9ce01a3`  |
| 2250   | Layout 1             | `162da9ce01a3`  |
| 2243   | Layout 1             | `162da9ce01a3`  |
| 2235   | Layout 1             | `162da9ce01a3`  |
| 2229   | Layout 1             | `162da9ce01a3`  |
| 2224   | Layout 1             | `162da9ce01a3`  |
| 2218   | Layout 1             | `162da9ce01a3`  |
| 2215   | Layout 1             | `162da9ce01a3`  |
| 2207   | Layout 1             | `162da9ce01a3`  |
| 2203   | Layout 1             | `162da9ce01a3`  |
| 2196   | Layout 1             | `162da9ce01a3`  |
| 2192   | Layout 1             | `162da9ce01a3`  |
| 2189   | Layout 1             | `162da9ce01a3`  |
| 2183   | Layout 1             | `162da9ce01a3`  |
| 2179   | Layout 1             | `162da9ce01a3`  |
| 2171   | Layout 1             | `162da9ce01a3`  |
| 2163   | Layout 1             | `162da9ce01a3`  |
| 2156   | Layout 1             | `162da9ce01a3`  |
| 2151   | Layout 1             | `162da9ce01a3`  |
| 2147   | Layout 1             | `162da9ce01a3`  |
| 2142   | Layout 1             | `162da9ce01a3`  |
| 2138   | Layout 1             | `162da9ce01a3`  |
| 2134   | Layout 1             | `162da9ce01a3`  |
| 2130   | Layout 1             | `162da9ce01a3`  |
| 2122   | Layout 1             | `162da9ce01a3`  |
| 2107   | Layout 1             | `162da9ce01a3`  |
| 2098   | Layout 1             | `162da9ce01a3`  |
| 2089   | Layout 1             | `162da9ce01a3`  |
| 2081   | Layout 1             | `162da9ce01a3`  |
| 2073   | Layout 1             | `162da9ce01a3`  |
| 2067   | Layout 1             | `162da9ce01a3`  |
| 2063   | Layout 1             | `162da9ce01a3`  |
| 2059   | Layout 1             | `162da9ce01a3`  |
| 2052   | Layout 1             | `162da9ce01a3`  |
| 2044   | Layout 1             | `162da9ce01a3`  |
| 2039   | Layout 1             | `162da9ce01a3`  |
| 2032   | Layout 1             | `162da9ce01a3`  |
| 2025   | Layout 1             | `162da9ce01a3`  |
| 2011   | Layout 1             | `162da9ce01a3`  |
| 2005   | Layout 1             | `162da9ce01a3`  |
| 2000   | Layout 1             | `162da9ce01a3`  |
| 1996   | Layout 1             | `162da9ce01a3`  |
| 1991   | Layout 1             | `162da9ce01a3`  |
| 1985   | Layout 1             | `162da9ce01a3`  |
| 1980   | Layout 1             | `162da9ce01a3`  |
| 1969   | Layout 1             | `162da9ce01a3`  |
| 1964   | Layout 1             | `162da9ce01a3`  |
| 1958   | Layout 1             | `162da9ce01a3`  |
| 1950   | Layout 1             | `162da9ce01a3`  |
| 1945   | Layout 1             | `162da9ce01a3`  |
| 1937   | Layout 1             | `162da9ce01a3`  |
| 1933   | Layout 1             | `162da9ce01a3`  |
| 1927   | Layout 1             | `162da9ce01a3`  |
| 1921   | Layout 1             | `162da9ce01a3`  |
| 1914   | Layout 1             | `162da9ce01a3`  |
| 1908   | Layout 1             | `162da9ce01a3`  |
| 1897   | Layout 1             | `162da9ce01a3`  |
| 1892   | Layout 1             | `162da9ce01a3`  |
| 1886   | Layout 1             | `162da9ce01a3`  |
| 1881   | Layout 1             | `162da9ce01a3`  |
| 1871   | Layout 1             | `162da9ce01a3`  |
| 1866   | Layout 1             | `162da9ce01a3`  |
| 1862   | Layout 1             | `162da9ce01a3`  |
| 1854   | Layout 1             | `162da9ce01a3`  |
| 1846   | Layout 1             | `162da9ce01a3`  |
| 1838   | Layout 1             | `162da9ce01a3`  |
| 1832   | Layout 1             | `162da9ce01a3`  |
| 1826   | Layout 1             | `162da9ce01a3`  |
| 1822   | Layout 1             | `162da9ce01a3`  |
| 1818   | Layout 1             | `162da9ce01a3`  |
| 1804   | Layout 1             | `162da9ce01a3`  |
| 1794   | Layout 1             | `162da9ce01a3`  |
| 1790   | Layout 1             | `162da9ce01a3`  |
| 1784   | Layout 1             | `162da9ce01a3`  |
| 1774   | Layout 1             | `162da9ce01a3`  |
| 1771   | Layout 1             | `162da9ce01a3`  |
| 1762   | Layout 1             | `162da9ce01a3`  |
| 1759   | Layout 1             | `162da9ce01a3`  |
| 1754   | Layout 1             | `162da9ce01a3`  |
| 1749   | Layout 1             | `162da9ce01a3`  |
| 1743   | Layout 1             | `162da9ce01a3`  |
| 1737   | Layout 1             | `162da9ce01a3`  |
| 1731   | Layout 1             | `162da9ce01a3`  |
| 1725   | Layout 1             | `162da9ce01a3`  |
| 1717   | Layout 1             | `162da9ce01a3`  |
| 1710   | Layout 1             | `162da9ce01a3`  |
| 1704   | Layout 1             | `162da9ce01a3`  |
| 1698   | Layout 1             | `162da9ce01a3`  |
| 1690   | Layout 1             | `162da9ce01a3`  |
| 1685   | Layout 1             | `162da9ce01a3`  |
| 1680   | Layout 1             | `162da9ce01a3`  |
| 1674   | Layout 1             | `162da9ce01a3`  |
| 1668   | Layout 1             | `162da9ce01a3`  |
| 1659   | Layout 1             | `162da9ce01a3`  |
| 1649   | Layout 1             | `162da9ce01a3`  |
| 1642   | Layout 1             | `162da9ce01a3`  |
| 1636   | Layout 1             | `162da9ce01a3`  |
| 1628   | Layout 1             | `162da9ce01a3`  |
| 1622   | Layout 1             | `162da9ce01a3`  |
| 1614   | Layout 1             | `162da9ce01a3`  |
| 1608   | Layout 1             | `162da9ce01a3`  |
| 1602   | Layout 1             | `162da9ce01a3`  |
| 1598   | Layout 1             | `162da9ce01a3`  |
| 1594   | Layout 1             | `162da9ce01a3`  |
| 1590   | Layout 1             | `162da9ce01a3`  |
| 1587   | Layout 1             | `162da9ce01a3`  |
| 1584   | Layout 1             | `162da9ce01a3`  |
| 1579   | Layout 1             | `162da9ce01a3`  |
| 1572   | Layout 1             | `162da9ce01a3`  |
| 1565   | Layout 1             | `162da9ce01a3`  |
| 1559   | Layout 1             | `162da9ce01a3`  |
| 1554   | Layout 1             | `162da9ce01a3`  |
| 1547   | Layout 1             | `162da9ce01a3`  |
| 1537   | Layout 1             | `162da9ce01a3`  |
| 1529   | Layout 1             | `162da9ce01a3`  |
| 1524   | Layout 1             | `162da9ce01a3`  |
| 1519   | Layout 1             | `162da9ce01a3`  |
| 1509   | Layout 1             | `162da9ce01a3`  |
| 1506   | Layout 1             | `162da9ce01a3`  |
| 1504   | Layout 1             | `162da9ce01a3`  |
| 1500   | Layout 1             | `162da9ce01a3`  |
| 1493   | Layout 1             | `162da9ce01a3`  |
| 1489   | Layout 1             | `162da9ce01a3`  |
| 1485   | Layout 1             | `162da9ce01a3`  |
| 1481   | Layout 1             | `162da9ce01a3`  |
| 1474   | Layout 1             | `162da9ce01a3`  |
| 1466   | Layout 1             | `162da9ce01a3`  |
| 1462   | Layout 1             | `162da9ce01a3`  |
| 1459   | Layout 1             | `162da9ce01a3`  |
| 1453   | Layout 1             | `162da9ce01a3`  |
| 1450   | Layout 1             | `162da9ce01a3`  |
| 1445   | Layout 1             | `162da9ce01a3`  |
| 1439   | Layout 1             | `162da9ce01a3`  |
| 1433   | Layout 1             | `162da9ce01a3`  |
| 1430   | Layout 1             | `162da9ce01a3`  |
| 1426   | Layout 1             | `162da9ce01a3`  |
| 1421   | Layout 1             | `162da9ce01a3`  |
| 1417   | Layout 1             | `162da9ce01a3`  |
| 1416   | Layout 1             | `162da9ce01a3`  |
| 1409   | Layout 1             | `162da9ce01a3`  |
| 1405   | Layout 1             | `162da9ce01a3`  |
| 1401   | Layout 1             | `162da9ce01a3`  |
| 1396   | Layout 1             | `162da9ce01a3`  |
| 1391   | Layout 1             | `162da9ce01a3`  |
| 1390   | Layout 1             | `162da9ce01a3`  |
| 1386   | Layout 1             | `162da9ce01a3`  |
| 1381   | Layout 1             | `162da9ce01a3`  |
| 1379   | Layout 1             | `162da9ce01a3`  |
| 1372   | Layout 1             | `162da9ce01a3`  |
| 1366   | Layout 1             | `162da9ce01a3`  |
| 1364   | Layout 1             | `162da9ce01a3`  |
| 1363   | Layout 1             | `162da9ce01a3`  |
| 1360   | Layout 1             | `162da9ce01a3`  |
| 1358   | Layout 1             | `162da9ce01a3`  |
| 1355   | Layout 1             | `162da9ce01a3`  |
| 1351   | Layout 1             | `162da9ce01a3`  |
| 1348   | Layout 1             | `162da9ce01a3`  |
| 1346   | Layout 1             | `162da9ce01a3`  |
| 1341   | No documented layout | `162da9ce01a3`  |
| 1340   | No documented layout | `162da9ce01a3`  |
| 1338   | No documented layout | `162da9ce01a3`  |
| 1335   | No documented layout | `162da9ce01a3`  |
| 1333   | No documented layout | `162da9ce01a3`  |
| 1329   | No documented layout | `162da9ce01a3`  |
| 1327   | No documented layout | `162da9ce01a3`  |
| 1324   | No documented layout | `162da9ce01a3`  |
| 1321   | No documented layout | `162da9ce01a3`  |
| 1319   | No documented layout | `162da9ce01a3`  |
| 1318   | No documented layout | `162da9ce01a3`  |
| 1316   | No documented layout | `162da9ce01a3`  |
| 1313   | No documented layout | `162da9ce01a3`  |
| 1311   | No documented layout | `162da9ce01a3`  |
| 1309   | No documented layout | `162da9ce01a3`  |
| 1304   | No documented layout | `162da9ce01a3`  |
| 1292   | No documented layout | `162da9ce01a3`  |
| 1286   | No documented layout | `162da9ce01a3`  |
| 1280   | No file              | `162da9ce01a3`  |
| 1276   | No file              | `162da9ce01a3`  |
| 1267   | No documented layout | `162da9ce01a3`  |
| 1261   | No documented layout | `162da9ce01a3`  |
| 1256   | No file              | `162da9ce01a3`  |
| 1250   | No file              | `162da9ce01a3`  |
| 1246   | No file              | `162da9ce01a3`  |
| 1239   | No file              | `162da9ce01a3`  |
| 1230   | No file              | `162da9ce01a3`  |
| 1226   | No file              | `162da9ce01a3`  |
| 1220   | No file              | `162da9ce01a3`  |
| 1217   | No file              | `162da9ce01a3`  |
| 1211   | No file              | `162da9ce01a3`  |
| 1210   | No file              | `162da9ce01a3`  |
| 1208   | No file              | `162da9ce01a3`  |
| 1203   | No file              | `162da9ce01a3`  |
| 1197   | No file              | `162da9ce01a3`  |
| 1194   | No file              | `162da9ce01a3`  |
| 1192   | No file              | `162da9ce01a3`  |
| 1187   | No file              | `162da9ce01a3`  |
| 1183   | No file              | `162da9ce01a3`  |
| 1177   | No file              | `162da9ce01a3`  |
| 1173   | No file              | `162da9ce01a3`  |
| 1167   | No file              | `162da9ce01a3`  |
| 1164   | No file              | `162da9ce01a3`  |
| 1156   | No file              | `162da9ce01a3`  |
| 1149   | No file              | `162da9ce01a3`  |
| 1144   | No file              | `162da9ce01a3`  |
| 1137   | No file              | `162da9ce01a3`  |
| 1132   | No file              | `162da9ce01a3`  |
| 1127   | No file              | `162da9ce01a3`  |
| 1122   | No file              | `162da9ce01a3`  |
| 1118   | No file              | `162da9ce01a3`  |
| 1114   | No file              | `162da9ce01a3`  |
| 1109   | No file              | `162da9ce01a3`  |
| 1102   | No file              | `162da9ce01a3`  |
| 1096   | No file              | `162da9ce01a3`  |
| 1088   | No file              | `162da9ce01a3`  |
| 1081   | No file              | `162da9ce01a3`  |
| 1076   | No file              | `162da9ce01a3`  |
| 1069   | No file              | `162da9ce01a3`  |
| 1064   | No file              | `162da9ce01a3`  |
| 1058   | No file              | `162da9ce01a3`  |
| 1051   | No file              | `162da9ce01a3`  |
| 1044   | No file              | `162da9ce01a3`  |
| 1036   | No file              | `162da9ce01a3`  |
| 1026   | No file              | `162da9ce01a3`  |
| 1016   | No file              | `162da9ce01a3`  |
| 1009   | No file              | `162da9ce01a3`  |
| 1005   | No file              | `162da9ce01a3`  |
| 1000   | No file              | `162da9ce01a3`  |
| 998    | No file              | `162da9ce01a3`  |
| 990    | No file              | `162da9ce01a3`  |
| 979    | No file              | `162da9ce01a3`  |
| 972    | No file              | `162da9ce01a3`  |
| 963    | No file              | `162da9ce01a3`  |
| 955    | No file              | `162da9ce01a3`  |
| 946    | No file              | `162da9ce01a3`  |
| 938    | No file              | `162da9ce01a3`  |
| 927    | No file              | `162da9ce01a3`  |
| 911    | No file              | `162da9ce01a3`  |
| 904    | No file              | `162da9ce01a3`  |
| 899    | No file              | `162da9ce01a3`  |
| 894    | No file              | `162da9ce01a3`  |
| 885    | No file              | `162da9ce01a3`  |
| 879    | No file              | `162da9ce01a3`  |
| 872    | No file              | `162da9ce01a3`  |
| 864    | No file              | `162da9ce01a3`  |
| 855    | No file              | `162da9ce01a3`  |
| 853    | No file              | `162da9ce01a3`  |
| 845    | No file              | `162da9ce01a3`  |
| 837    | No file              | `162da9ce01a3`  |
| 829    | No file              | `162da9ce01a3`  |
| 822    | No file              | `162da9ce01a3`  |
| 814    | No file              | `162da9ce01a3`  |
| 805    | No file              | `162da9ce01a3`  |
| 794    | No file              | `162da9ce01a3`  |
| 787    | No file              | `162da9ce01a3`  |
| 780    | No file              | `162da9ce01a3`  |
| 771    | No file              | `162da9ce01a3`  |
| 760    | No file              | `162da9ce01a3`  |
| 748    | No file              | `162da9ce01a3`  |
| 741    | No file              | `162da9ce01a3`  |
| 736    | No file              | `162da9ce01a3`  |
| 731    | No file              | `162da9ce01a3`  |
| 723    | No file              | `162da9ce01a3`  |
| 711    | No file              | `162da9ce01a3`  |
| 707    | No file              | `162da9ce01a3`  |
| 697    | No file              | `162da9ce01a3`  |
| 689    | No file              | `162da9ce01a3`  |
| 683    | No file              | `162da9ce01a3`  |
| 678    | No file              | `162da9ce01a3`  |
| 670    | No file              | `162da9ce01a3`  |
| 661    | No file              | `162da9ce01a3`  |
| 656    | No file              | `162da9ce01a3`  |
| 652    | No file              | `162da9ce01a3`  |
| 643    | No file              | `162da9ce01a3`  |
| 637    | No file              | `162da9ce01a3`  |
| 630    | No file              | `162da9ce01a3`  |
| 627    | No file              | `162da9ce01a3`  |
| 621    | No file              | `162da9ce01a3`  |
| 617    | No file              | `162da9ce01a3`  |
| 615    | No file              | `162da9ce01a3`  |
| 606    | No file              | `162da9ce01a3`  |
| 599    | No file              | `162da9ce01a3`  |
| 592    | No file              | `162da9ce01a3`  |
| 586    | No file              | `162da9ce01a3`  |
| 577    | No file              | `162da9ce01a3`  |
| 569    | No file              | `162da9ce01a3`  |
| 561    | No file              | `162da9ce01a3`  |
| 554    | No file              | `162da9ce01a3`  |
| 542    | No file              | `162da9ce01a3`  |
| 532    | No file              | `162da9ce01a3`  |
| 531    | No file              | `162da9ce01a3`  |
| 526    | No file              | `162da9ce01a3`  |
| 521    | No file              | `162da9ce01a3`  |
| 517    | No file              | `162da9ce01a3`  |
| 510    | No file              | `162da9ce01a3`  |
| 508    | No file              | `162da9ce01a3`  |
| 504    | No file              | `162da9ce01a3`  |
| 497    | No file              | `162da9ce01a3`  |
| 491    | No file              | `162da9ce01a3`  |
| 485    | No file              | `162da9ce01a3`  |
| 478    | No file              | `162da9ce01a3`  |
| 472    | No file              | `162da9ce01a3`  |
| 466    | No file              | `162da9ce01a3`  |
| 457    | No file              | `162da9ce01a3`  |
| 452    | No file              | `162da9ce01a3`  |
| 449    | No file              | `162da9ce01a3`  |
| 435    | No file              | `162da9ce01a3`  |

<!-- versions:end -->

## Companion Files

| File                      | Required | Role                                                                     |
| ------------------------- | -------- | ------------------------------------------------------------------------ |
| `petfusionnewoffset.dbss` | Optional | `tier -> (offset, size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type      | Field | Notes                                 |
| ------- | --------- | ----- | ------------------------------------- |
| `+0x00` | Row[..end] | rows | See Row; no count, the rows fill the file |

On client 3474 the file is 4 x 17 = 68 bytes.

### Row (17 bytes)

| Offset  | Type     | Field         | Notes                                                                            |
| ------- | -------- | ------------- | -------------------------------------------------------------------------------- |
| `+0x00` | u8       | tier          | Row key: the main pet's tier, from 0                                             |
| `+0x01` | u8       | select_tier_0 | Tier of the new pet on a success, from 0                                         |
| `+0x02` | bytes[3] | padding_02    | Alignment bytes of the `select_tier_0` entry, see Notes                          |
| `+0x05` | u32      | select_rate_0 | Base chance of `select_tier_0`: `100` (0.01%) for main tiers 0 to 2, `1000000` for tier 3 (client 3474) |
| `+0x09` | u8       | select_tier_1 | Tier of the new pet otherwise, from 0; `0` with `select_rate_1` `0` on tier 3     |
| `+0x0A` | bytes[3] | padding_0a    | Alignment bytes of the `select_tier_1` entry, see Notes                          |
| `+0x0D` | u32      | select_rate_1 | `1000000` on main tiers 0 to 2, `0` on tier 3 (client 3474)                       |

### `petfusionnewoffset.dbss`

Bare offset table into `petfusionnew.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                   |
| ------- | ----------------- | ----- | --------------------------------------- |
| `+0x00` | u32               | count | Number of rows in `petfusionnew.dbss`   |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                          |

### Offset Row (9 bytes)

| Offset  | Type | Field  | Notes                                                                    |
| ------- | ---- | ------ | ------------------------------------------------------------------------ |
| `+0x00` | u8   | tier   | Key of the row it points at                                              |
| `+0x01` | u32  | offset | Absolute byte offset of the row in `petfusionnew.dbss`, at its `tier`    |
| `+0x05` | u32  | size   | The whole row: always `17`                                               |

## Exchange Results

On client 3474, with tiers as the game numbers them:

| Main pet | Success     | Base chance | Otherwise |
| -------- | ----------- | ----------- | --------- |
| Tier 1   | Tier 3      | 0.01%       | Tier 2    |
| Tier 2   | Tier 3      | 0.01%       | Tier 2    |
| Tier 3   | Tier 4      | 0.01%       | Tier 3    |
| Tier 4   | Tier 4      | 100%        | none      |

The base chance plus the add rates of the other pets is the success chance
the exchange window shows. Garmoth's
[pets guide](https://garmoth.com/guides/post/bdo-basics-pets) lists six
chances that match this sum for one other pet, rounded to a whole percent:
55% for Tier 1 + Tier 1, 65% for Tier 2 + Tier 1, 80% for Tier 2 + Tier 2,
15% for Tier 3 + Tier 1, 25% for Tier 3 + Tier 2 and 35% for Tier 3 +
Tier 3. See [`petfusionnewaddrateinfo.dbss`](petfusionnewaddrateinfo_dbss.md)
for the add rates.

## Field Names

The `Pet_Fusion_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Tier`, `SelectRate_0`, `SelectTier_0`,
`SelectRate_1` and `SelectTier_1`, and its 4 rows match the file on all 4
keys and all four value columns (clients 1784 and 3474). The file stores
each tier before its rate; the sheet lists the rate first. The empty
`SelectRate_1` and `SelectTier_1` cells of tier `3` (`<null>`) are the
zeros of the file. The developer workbook (`datasheet_petdatatable.xlsm`)
adds the note columns `#SelectCharacterName_0` and
`#SelectCharacterName_1`, which name each select tier as a generation
(`세대`): `3세대` for `2`, `4세대` for `3`, `2세대` for `1`, so the stored
tier plus 1 is the game's tier. A third note column reads `#참조 : 합성 세대
정보` ("reference: fusion generation info").

The client Lua of the exchange window (`panel_window_petfusion_all_1.luac`,
`setRate`) reads `ToClient_getMainFusionRate(mainPetTier) / 10000` as the
base chance in percent, which is `select_rate_0` on the 1,000,000 = 100%
scale. It shows the target tier as Tier 3 for a Tier 1 or Tier 2 main pet
and as Tier 4 for a Tier 3 or Tier 4 one (`setTargetTier`), the
`select_tier_0` column plus 1, and the second bar as the tier below it, the
`select_tier_1` column plus 1. For a Tier 4 main pet it hides the second
bar, the row whose `select_rate_1` is `0`.

## Notes

- The success chance in the window is `select_rate_0` plus, for each of
  up to four other pets (`_subPetMaxTableCount = 4`), its add rate by the
  main pet's tier and its own tier, capped at 100% and rounded to a whole
  percent (`math.floor(totalRate + 0.5)`). The other result gets the rest.
  At 100% the window takes no more pets (`LUA_PETFUSION_100PERCENT_TEXT`,
  "You can no longer increase the probability of pet tier increase.").
- The window takes no other pet of a higher tier than the main pet
  (`PANEL_RENEWAL_PETLIST_TEMP_3`) and no Tier 5 pet
  (`LUA_PETFUSION_LEADERPET`), so tier `4` has no row.
- `padding_02` and `padding_0a` are the 3 bytes between a u8 tier and its
  4-byte aligned rate: each select is an 8-byte entry (u8, 3 alignment
  bytes, u32) copied whole. The bytes differ between builds while every
  sheet value stays the same: `00 00 00` and `00 00 00` on client 1485,
  `7F 00 00` and `00 00 00` on clients 1784 and 2519, `00 00 00` and
  `02 00 00` on client 3002, `00 00 00` and `01 00 00` on clients 3251 and
  3474, in every row of the file.
- Clients 1485 to 3474 ship `petfusionnew.dbss`, `petfusionnewoffset.dbss`
  and `petfusionnewaddrateinfo.dbss` with the same values. Client 1230 has
  none of the three and ships `petfusionnew.bss` instead: PABR, then these
  68 bytes, the 80 bytes of `petfusionnewaddrateinfo.dbss`, an empty
  string table and the trailer. Client 794 has `en/petfusion.bss`.
- Both files list the tiers in the same order, `0` to `3`. The offset
  points at the row's own `tier`.
- The older pet exchange table [`petoldfusion.dbss`](petoldfusion_dbss.md)
  (sheet `Pet_OldFusion_Table`) keys its result tiers by fusion key
  (variant, species and tier) in place of the tier alone.
