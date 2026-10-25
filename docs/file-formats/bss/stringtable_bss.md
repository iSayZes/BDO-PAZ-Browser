# `stringtable.bss` Format

## Purpose

The Korean source of the client's keyed UI strings. Each row pairs a string key
(`LUA_WIDGET_TOWNNPCNAVI_NPCTYPETEXT_6`) with its Korean text and a 32-bit key
hash. The hash is the LOC type `37` `str_id1`, so this file is how a key the
client scripts use turns into the translated text in `languagedata_*.loc`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File              | Bytes     | Records                    | Row bytes |
| ------ | -------------- | ----------------- | --------- | -------------------------- | --------- |
| 1      | 1286 and later | `stringtable.bss` | 7,334,867 | 51,099 String Row, 8 Sheet | 16        |

| Layout | File              | Known               | Unknown          |
| ------ | ----------------- | ------------------- | ---------------- |
| 1      | `stringtable.bss` | 7,130,471 B (97.2%) | 204,396 B (2.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `e620d33b1fb8`  |
| 3482   | Layout 1             | `e620d33b1fb8`  |
| 3474   | Layout 1             | `e620d33b1fb8`  |
| 3473   | Layout 1             | `e620d33b1fb8`  |
| 3464   | Layout 1             | `e620d33b1fb8`  |
| 3458   | Layout 1             | `e620d33b1fb8`  |
| 3454   | Layout 1             | `e620d33b1fb8`  |
| 3444   | Layout 1             | `e620d33b1fb8`  |
| 3435   | Layout 1             | `e620d33b1fb8`  |
| 3426   | Layout 1             | `e620d33b1fb8`  |
| 3418   | Layout 1             | `e620d33b1fb8`  |
| 3412   | Layout 1             | `e620d33b1fb8`  |
| 3402   | Layout 1             | `e620d33b1fb8`  |
| 3396   | Layout 1             | `e620d33b1fb8`  |
| 3387   | Layout 1             | `e620d33b1fb8`  |
| 3381   | Layout 1             | `e620d33b1fb8`  |
| 3373   | Layout 1             | `e620d33b1fb8`  |
| 3364   | Layout 1             | `e620d33b1fb8`  |
| 3356   | Layout 1             | `e620d33b1fb8`  |
| 3349   | Layout 1             | `e620d33b1fb8`  |
| 3342   | Layout 1             | `e620d33b1fb8`  |
| 3335   | Layout 1             | `e620d33b1fb8`  |
| 3326   | Layout 1             | `e620d33b1fb8`  |
| 3321   | Layout 1             | `e620d33b1fb8`  |
| 3314   | Layout 1             | `e620d33b1fb8`  |
| 3303   | Layout 1             | `e620d33b1fb8`  |
| 3302   | Layout 1             | `e620d33b1fb8`  |
| 3293   | Layout 1             | `e620d33b1fb8`  |
| 3283   | Layout 1             | `e620d33b1fb8`  |
| 3275   | Layout 1             | `e620d33b1fb8`  |
| 3267   | Layout 1             | `e620d33b1fb8`  |
| 3258   | Layout 1             | `e620d33b1fb8`  |
| 3251   | Layout 1             | `e620d33b1fb8`  |
| 3242   | Layout 1             | `e620d33b1fb8`  |
| 3235   | Layout 1             | `e620d33b1fb8`  |
| 3229   | Layout 1             | `e620d33b1fb8`  |
| 3212   | Layout 1             | `e620d33b1fb8`  |
| 3203   | Layout 1             | `e620d33b1fb8`  |
| 3193   | Layout 1             | `e620d33b1fb8`  |
| 3186   | Layout 1             | `e620d33b1fb8`  |
| 3177   | Layout 1             | `e620d33b1fb8`  |
| 3169   | Layout 1             | `e620d33b1fb8`  |
| 3158   | Layout 1             | `e620d33b1fb8`  |
| 3151   | Layout 1             | `e620d33b1fb8`  |
| 3144   | Layout 1             | `e620d33b1fb8`  |
| 3133   | Layout 1             | `e620d33b1fb8`  |
| 3125   | Layout 1             | `e620d33b1fb8`  |
| 3118   | Layout 1             | `e620d33b1fb8`  |
| 3111   | Layout 1             | `e620d33b1fb8`  |
| 3103   | Layout 1             | `e620d33b1fb8`  |
| 3095   | Layout 1             | `e620d33b1fb8`  |
| 3086   | Layout 1             | `e620d33b1fb8`  |
| 3072   | Layout 1             | `e620d33b1fb8`  |
| 3062   | Layout 1             | `e620d33b1fb8`  |
| 3052   | Layout 1             | `e620d33b1fb8`  |
| 3045   | Layout 1             | `e620d33b1fb8`  |
| 3037   | Layout 1             | `e620d33b1fb8`  |
| 3030   | Layout 1             | `e620d33b1fb8`  |
| 3021   | Layout 1             | `e620d33b1fb8`  |
| 3012   | Layout 1             | `e620d33b1fb8`  |
| 3002   | Layout 1             | `e620d33b1fb8`  |
| 2995   | Layout 1             | `e620d33b1fb8`  |
| 2987   | Layout 1             | `e620d33b1fb8`  |
| 2978   | Layout 1             | `e620d33b1fb8`  |
| 2970   | Layout 1             | `e620d33b1fb8`  |
| 2959   | Layout 1             | `e620d33b1fb8`  |
| 2951   | Layout 1             | `e620d33b1fb8`  |
| 2942   | Layout 1             | `e620d33b1fb8`  |
| 2935   | Layout 1             | `e620d33b1fb8`  |
| 2932   | Layout 1             | `e620d33b1fb8`  |
| 2923   | Layout 1             | `e620d33b1fb8`  |
| 2919   | Layout 1             | `e620d33b1fb8`  |
| 2907   | Layout 1             | `e620d33b1fb8`  |
| 2900   | Layout 1             | `e620d33b1fb8`  |
| 2891   | Layout 1             | `e620d33b1fb8`  |
| 2882   | Layout 1             | `e620d33b1fb8`  |
| 2872   | Layout 1             | `e620d33b1fb8`  |
| 2863   | Layout 1             | `e620d33b1fb8`  |
| 2855   | Layout 1             | `e620d33b1fb8`  |
| 2849   | Layout 1             | `e620d33b1fb8`  |
| 2844   | Layout 1             | `e620d33b1fb8`  |
| 2834   | Layout 1             | `e620d33b1fb8`  |
| 2825   | Layout 1             | `e620d33b1fb8`  |
| 2819   | Layout 1             | `e620d33b1fb8`  |
| 2811   | Layout 1             | `e620d33b1fb8`  |
| 2803   | Layout 1             | `e620d33b1fb8`  |
| 2794   | Layout 1             | `e620d33b1fb8`  |
| 2783   | Layout 1             | `e620d33b1fb8`  |
| 2774   | Layout 1             | `e620d33b1fb8`  |
| 2765   | Layout 1             | `e620d33b1fb8`  |
| 2756   | Layout 1             | `e620d33b1fb8`  |
| 2750   | Layout 1             | `e620d33b1fb8`  |
| 2743   | Layout 1             | `e620d33b1fb8`  |
| 2736   | Layout 1             | `e620d33b1fb8`  |
| 2726   | Layout 1             | `e620d33b1fb8`  |
| 2717   | Layout 1             | `e620d33b1fb8`  |
| 2709   | Layout 1             | `e620d33b1fb8`  |
| 2703   | Layout 1             | `e620d33b1fb8`  |
| 2695   | Layout 1             | `e620d33b1fb8`  |
| 2684   | Layout 1             | `e620d33b1fb8`  |
| 2672   | Layout 1             | `e620d33b1fb8`  |
| 2665   | Layout 1             | `e620d33b1fb8`  |
| 2657   | Layout 1             | `e620d33b1fb8`  |
| 2649   | Layout 1             | `e620d33b1fb8`  |
| 2644   | Layout 1             | `e620d33b1fb8`  |
| 2637   | Layout 1             | `e620d33b1fb8`  |
| 2629   | Layout 1             | `e620d33b1fb8`  |
| 2619   | Layout 1             | `e620d33b1fb8`  |
| 2612   | Layout 1             | `e620d33b1fb8`  |
| 2606   | Layout 1             | `e620d33b1fb8`  |
| 2602   | Layout 1             | `e620d33b1fb8`  |
| 2601   | Layout 1             | `e620d33b1fb8`  |
| 2592   | Layout 1             | `e620d33b1fb8`  |
| 2583   | Layout 1             | `e620d33b1fb8`  |
| 2575   | Layout 1             | `e620d33b1fb8`  |
| 2567   | Layout 1             | `e620d33b1fb8`  |
| 2560   | Layout 1             | `e620d33b1fb8`  |
| 2553   | Layout 1             | `e620d33b1fb8`  |
| 2545   | Layout 1             | `e620d33b1fb8`  |
| 2538   | Layout 1             | `e620d33b1fb8`  |
| 2529   | Layout 1             | `e620d33b1fb8`  |
| 2519   | Layout 1             | `e620d33b1fb8`  |
| 2513   | Layout 1             | `e620d33b1fb8`  |
| 2510   | Layout 1             | `e620d33b1fb8`  |
| 2507   | Layout 1             | `e620d33b1fb8`  |
| 2503   | Layout 1             | `e620d33b1fb8`  |
| 2498   | Layout 1             | `e620d33b1fb8`  |
| 2492   | Layout 1             | `e620d33b1fb8`  |
| 2487   | Layout 1             | `e620d33b1fb8`  |
| 2480   | Layout 1             | `e620d33b1fb8`  |
| 2474   | Layout 1             | `e620d33b1fb8`  |
| 2468   | Layout 1             | `e620d33b1fb8`  |
| 2460   | Layout 1             | `e620d33b1fb8`  |
| 2453   | Layout 1             | `e620d33b1fb8`  |
| 2444   | Layout 1             | `e620d33b1fb8`  |
| 2438   | Layout 1             | `e620d33b1fb8`  |
| 2434   | Layout 1             | `e620d33b1fb8`  |
| 2429   | Layout 1             | `e620d33b1fb8`  |
| 2421   | Layout 1             | `e620d33b1fb8`  |
| 2414   | Layout 1             | `e620d33b1fb8`  |
| 2407   | Layout 1             | `e620d33b1fb8`  |
| 2401   | Layout 1             | `e620d33b1fb8`  |
| 2397   | Layout 1             | `e620d33b1fb8`  |
| 2393   | Layout 1             | `e620d33b1fb8`  |
| 2384   | Layout 1             | `e620d33b1fb8`  |
| 2378   | Layout 1             | `e620d33b1fb8`  |
| 2372   | Layout 1             | `e620d33b1fb8`  |
| 2358   | Layout 1             | `e620d33b1fb8`  |
| 2352   | Layout 1             | `e620d33b1fb8`  |
| 2347   | Layout 1             | `e620d33b1fb8`  |
| 2343   | Layout 1             | `e620d33b1fb8`  |
| 2335   | Layout 1             | `e620d33b1fb8`  |
| 2327   | Layout 1             | `e620d33b1fb8`  |
| 2324   | Layout 1             | `e620d33b1fb8`  |
| 2319   | Layout 1             | `e620d33b1fb8`  |
| 2313   | Layout 1             | `e620d33b1fb8`  |
| 2308   | Layout 1             | `e620d33b1fb8`  |
| 2302   | Layout 1             | `e620d33b1fb8`  |
| 2295   | Layout 1             | `e620d33b1fb8`  |
| 2290   | Layout 1             | `e620d33b1fb8`  |
| 2284   | Layout 1             | `e620d33b1fb8`  |
| 2276   | Layout 1             | `e620d33b1fb8`  |
| 2269   | Layout 1             | `e620d33b1fb8`  |
| 2259   | Layout 1             | `e620d33b1fb8`  |
| 2250   | Layout 1             | `e620d33b1fb8`  |
| 2243   | Layout 1             | `e620d33b1fb8`  |
| 2235   | Layout 1             | `e620d33b1fb8`  |
| 2229   | Layout 1             | `e620d33b1fb8`  |
| 2224   | Layout 1             | `e620d33b1fb8`  |
| 2218   | Layout 1             | `e620d33b1fb8`  |
| 2215   | Layout 1             | `e620d33b1fb8`  |
| 2207   | Layout 1             | `e620d33b1fb8`  |
| 2203   | Layout 1             | `e620d33b1fb8`  |
| 2196   | Layout 1             | `e620d33b1fb8`  |
| 2192   | Layout 1             | `e620d33b1fb8`  |
| 2189   | Layout 1             | `e620d33b1fb8`  |
| 2183   | Layout 1             | `e620d33b1fb8`  |
| 2179   | Layout 1             | `e620d33b1fb8`  |
| 2171   | Layout 1             | `e620d33b1fb8`  |
| 2163   | Layout 1             | `e620d33b1fb8`  |
| 2156   | Layout 1             | `e620d33b1fb8`  |
| 2151   | Layout 1             | `e620d33b1fb8`  |
| 2147   | Layout 1             | `e620d33b1fb8`  |
| 2142   | Layout 1             | `e620d33b1fb8`  |
| 2138   | Layout 1             | `e620d33b1fb8`  |
| 2134   | Layout 1             | `e620d33b1fb8`  |
| 2130   | Layout 1             | `e620d33b1fb8`  |
| 2122   | Layout 1             | `e620d33b1fb8`  |
| 2107   | Layout 1             | `e620d33b1fb8`  |
| 2098   | Layout 1             | `e620d33b1fb8`  |
| 2089   | Layout 1             | `e620d33b1fb8`  |
| 2081   | Layout 1             | `e620d33b1fb8`  |
| 2073   | Layout 1             | `e620d33b1fb8`  |
| 2067   | Layout 1             | `e620d33b1fb8`  |
| 2063   | Layout 1             | `e620d33b1fb8`  |
| 2059   | Layout 1             | `e620d33b1fb8`  |
| 2052   | Layout 1             | `e620d33b1fb8`  |
| 2044   | Layout 1             | `e620d33b1fb8`  |
| 2039   | Layout 1             | `e620d33b1fb8`  |
| 2032   | Layout 1             | `e620d33b1fb8`  |
| 2025   | Layout 1             | `e620d33b1fb8`  |
| 2011   | Layout 1             | `e620d33b1fb8`  |
| 2005   | Layout 1             | `e620d33b1fb8`  |
| 2000   | Layout 1             | `e620d33b1fb8`  |
| 1996   | Layout 1             | `e620d33b1fb8`  |
| 1991   | Layout 1             | `e620d33b1fb8`  |
| 1985   | Layout 1             | `e620d33b1fb8`  |
| 1980   | Layout 1             | `e620d33b1fb8`  |
| 1969   | Layout 1             | `e620d33b1fb8`  |
| 1964   | Layout 1             | `e620d33b1fb8`  |
| 1958   | Layout 1             | `e620d33b1fb8`  |
| 1950   | Layout 1             | `e620d33b1fb8`  |
| 1945   | Layout 1             | `e620d33b1fb8`  |
| 1937   | Layout 1             | `e620d33b1fb8`  |
| 1933   | Layout 1             | `e620d33b1fb8`  |
| 1927   | Layout 1             | `e620d33b1fb8`  |
| 1921   | Layout 1             | `e620d33b1fb8`  |
| 1914   | Layout 1             | `e620d33b1fb8`  |
| 1908   | Layout 1             | `e620d33b1fb8`  |
| 1897   | Layout 1             | `e620d33b1fb8`  |
| 1892   | Layout 1             | `e620d33b1fb8`  |
| 1886   | Layout 1             | `e620d33b1fb8`  |
| 1881   | Layout 1             | `e620d33b1fb8`  |
| 1871   | Layout 1             | `e620d33b1fb8`  |
| 1866   | Layout 1             | `e620d33b1fb8`  |
| 1862   | Layout 1             | `e620d33b1fb8`  |
| 1854   | Layout 1             | `e620d33b1fb8`  |
| 1846   | Layout 1             | `e620d33b1fb8`  |
| 1838   | Layout 1             | `e620d33b1fb8`  |
| 1832   | Layout 1             | `e620d33b1fb8`  |
| 1826   | Layout 1             | `e620d33b1fb8`  |
| 1822   | Layout 1             | `e620d33b1fb8`  |
| 1818   | Layout 1             | `e620d33b1fb8`  |
| 1804   | Layout 1             | `e620d33b1fb8`  |
| 1794   | Layout 1             | `e620d33b1fb8`  |
| 1790   | Layout 1             | `e620d33b1fb8`  |
| 1784   | Layout 1             | `e620d33b1fb8`  |
| 1774   | Layout 1             | `e620d33b1fb8`  |
| 1771   | Layout 1             | `e620d33b1fb8`  |
| 1762   | Layout 1             | `e620d33b1fb8`  |
| 1759   | Layout 1             | `e620d33b1fb8`  |
| 1754   | Layout 1             | `e620d33b1fb8`  |
| 1749   | Layout 1             | `e620d33b1fb8`  |
| 1743   | Layout 1             | `e620d33b1fb8`  |
| 1737   | Layout 1             | `e620d33b1fb8`  |
| 1731   | Layout 1             | `e620d33b1fb8`  |
| 1725   | Layout 1             | `e620d33b1fb8`  |
| 1717   | Layout 1             | `e620d33b1fb8`  |
| 1710   | Layout 1             | `e620d33b1fb8`  |
| 1704   | Layout 1             | `e620d33b1fb8`  |
| 1698   | Layout 1             | `e620d33b1fb8`  |
| 1690   | Layout 1             | `e620d33b1fb8`  |
| 1685   | Layout 1             | `e620d33b1fb8`  |
| 1680   | Layout 1             | `e620d33b1fb8`  |
| 1674   | Layout 1             | `e620d33b1fb8`  |
| 1668   | Layout 1             | `e620d33b1fb8`  |
| 1659   | Layout 1             | `e620d33b1fb8`  |
| 1649   | Layout 1             | `e620d33b1fb8`  |
| 1642   | Layout 1             | `e620d33b1fb8`  |
| 1636   | Layout 1             | `e620d33b1fb8`  |
| 1628   | Layout 1             | `e620d33b1fb8`  |
| 1622   | Layout 1             | `e620d33b1fb8`  |
| 1614   | Layout 1             | `e620d33b1fb8`  |
| 1608   | Layout 1             | `e620d33b1fb8`  |
| 1602   | Layout 1             | `e620d33b1fb8`  |
| 1598   | Layout 1             | `e620d33b1fb8`  |
| 1594   | Layout 1             | `e620d33b1fb8`  |
| 1590   | Layout 1             | `e620d33b1fb8`  |
| 1587   | Layout 1             | `e620d33b1fb8`  |
| 1584   | Layout 1             | `e620d33b1fb8`  |
| 1579   | Layout 1             | `e620d33b1fb8`  |
| 1572   | Layout 1             | `e620d33b1fb8`  |
| 1565   | Layout 1             | `e620d33b1fb8`  |
| 1559   | Layout 1             | `e620d33b1fb8`  |
| 1554   | Layout 1             | `e620d33b1fb8`  |
| 1547   | Layout 1             | `e620d33b1fb8`  |
| 1537   | Layout 1             | `e620d33b1fb8`  |
| 1529   | Layout 1             | `e620d33b1fb8`  |
| 1524   | Layout 1             | `e620d33b1fb8`  |
| 1519   | Layout 1             | `e620d33b1fb8`  |
| 1509   | Layout 1             | `e620d33b1fb8`  |
| 1506   | Layout 1             | `e620d33b1fb8`  |
| 1504   | Layout 1             | `e620d33b1fb8`  |
| 1500   | Layout 1             | `e620d33b1fb8`  |
| 1493   | Layout 1             | `e620d33b1fb8`  |
| 1489   | Layout 1             | `e620d33b1fb8`  |
| 1485   | Layout 1             | `e620d33b1fb8`  |
| 1481   | Layout 1             | `e620d33b1fb8`  |
| 1474   | Layout 1             | `e620d33b1fb8`  |
| 1466   | Layout 1             | `e620d33b1fb8`  |
| 1462   | Layout 1             | `e620d33b1fb8`  |
| 1459   | Layout 1             | `e620d33b1fb8`  |
| 1453   | Layout 1             | `e620d33b1fb8`  |
| 1450   | Layout 1             | `e620d33b1fb8`  |
| 1445   | Layout 1             | `e620d33b1fb8`  |
| 1439   | Layout 1             | `e620d33b1fb8`  |
| 1433   | Layout 1             | `e620d33b1fb8`  |
| 1430   | Layout 1             | `e620d33b1fb8`  |
| 1426   | Layout 1             | `e620d33b1fb8`  |
| 1421   | Layout 1             | `e620d33b1fb8`  |
| 1417   | Layout 1             | `e620d33b1fb8`  |
| 1416   | Layout 1             | `e620d33b1fb8`  |
| 1409   | Layout 1             | `e620d33b1fb8`  |
| 1405   | Layout 1             | `e620d33b1fb8`  |
| 1401   | Layout 1             | `e620d33b1fb8`  |
| 1396   | Layout 1             | `e620d33b1fb8`  |
| 1391   | Layout 1             | `e620d33b1fb8`  |
| 1390   | Layout 1             | `e620d33b1fb8`  |
| 1386   | Layout 1             | `e620d33b1fb8`  |
| 1381   | Layout 1             | `e620d33b1fb8`  |
| 1379   | Layout 1             | `e620d33b1fb8`  |
| 1372   | Layout 1             | `e620d33b1fb8`  |
| 1366   | Layout 1             | `e620d33b1fb8`  |
| 1364   | Layout 1             | `e620d33b1fb8`  |
| 1363   | Layout 1             | `e620d33b1fb8`  |
| 1360   | Layout 1             | `e620d33b1fb8`  |
| 1358   | Layout 1             | `e620d33b1fb8`  |
| 1355   | Layout 1             | `e620d33b1fb8`  |
| 1351   | Layout 1             | `e620d33b1fb8`  |
| 1348   | Layout 1             | `e620d33b1fb8`  |
| 1346   | Layout 1             | `e620d33b1fb8`  |
| 1341   | Layout 1             | `e620d33b1fb8`  |
| 1340   | Layout 1             | `e620d33b1fb8`  |
| 1338   | Layout 1             | `e620d33b1fb8`  |
| 1335   | Layout 1             | `e620d33b1fb8`  |
| 1333   | Layout 1             | `e620d33b1fb8`  |
| 1329   | Layout 1             | `e620d33b1fb8`  |
| 1327   | Layout 1             | `e620d33b1fb8`  |
| 1324   | Layout 1             | `e620d33b1fb8`  |
| 1321   | Layout 1             | `e620d33b1fb8`  |
| 1319   | Layout 1             | `e620d33b1fb8`  |
| 1318   | Layout 1             | `e620d33b1fb8`  |
| 1316   | Layout 1             | `e620d33b1fb8`  |
| 1313   | Layout 1             | `e620d33b1fb8`  |
| 1311   | Layout 1             | `e620d33b1fb8`  |
| 1309   | Layout 1             | `e620d33b1fb8`  |
| 1304   | Layout 1             | `e620d33b1fb8`  |
| 1292   | Layout 1             | `e620d33b1fb8`  |
| 1286   | Layout 1             | `e620d33b1fb8`  |
| 1280   | No documented layout | `e620d33b1fb8`  |
| 1276   | No documented layout | `e620d33b1fb8`  |
| 1267   | No documented layout | `e620d33b1fb8`  |
| 1261   | No documented layout | `e620d33b1fb8`  |
| 1256   | No documented layout | `e620d33b1fb8`  |
| 1250   | No documented layout | `e620d33b1fb8`  |
| 1246   | No documented layout | `e620d33b1fb8`  |
| 1239   | No documented layout | `e620d33b1fb8`  |
| 1230   | No documented layout | `e620d33b1fb8`  |
| 1226   | No documented layout | `e620d33b1fb8`  |
| 1220   | No documented layout | `e620d33b1fb8`  |
| 1217   | No documented layout | `e620d33b1fb8`  |
| 1211   | No documented layout | `e620d33b1fb8`  |
| 1210   | No documented layout | `e620d33b1fb8`  |
| 1208   | No documented layout | `e620d33b1fb8`  |
| 1203   | No documented layout | `e620d33b1fb8`  |
| 1197   | No documented layout | `e620d33b1fb8`  |
| 1194   | No documented layout | `e620d33b1fb8`  |
| 1192   | No documented layout | `e620d33b1fb8`  |
| 1187   | No documented layout | `e620d33b1fb8`  |
| 1183   | No documented layout | `e620d33b1fb8`  |
| 1177   | No documented layout | `e620d33b1fb8`  |
| 1173   | No documented layout | `e620d33b1fb8`  |
| 1167   | No documented layout | `e620d33b1fb8`  |
| 1164   | No documented layout | `e620d33b1fb8`  |
| 1156   | No documented layout | `e620d33b1fb8`  |
| 1149   | No documented layout | `e620d33b1fb8`  |
| 1144   | No documented layout | `e620d33b1fb8`  |
| 1137   | No documented layout | `e620d33b1fb8`  |
| 1132   | No documented layout | `e620d33b1fb8`  |
| 1127   | No documented layout | `e620d33b1fb8`  |
| 1122   | No documented layout | `e620d33b1fb8`  |
| 1118   | No documented layout | `e620d33b1fb8`  |
| 1114   | No documented layout | `e620d33b1fb8`  |
| 1109   | No documented layout | `e620d33b1fb8`  |
| 1102   | No documented layout | `e620d33b1fb8`  |
| 1096   | No documented layout | `e620d33b1fb8`  |
| 1088   | No documented layout | `e620d33b1fb8`  |
| 1081   | No documented layout | `e620d33b1fb8`  |
| 1076   | No documented layout | `e620d33b1fb8`  |
| 1069   | No documented layout | `e620d33b1fb8`  |
| 1064   | No documented layout | `e620d33b1fb8`  |
| 1058   | No documented layout | `e620d33b1fb8`  |
| 1051   | No documented layout | `e620d33b1fb8`  |
| 1044   | No documented layout | `e620d33b1fb8`  |
| 1036   | No documented layout | `e620d33b1fb8`  |
| 1026   | No documented layout | `e620d33b1fb8`  |
| 1016   | No documented layout | `e620d33b1fb8`  |
| 1009   | No documented layout | `e620d33b1fb8`  |
| 1005   | No documented layout | `e620d33b1fb8`  |
| 1000   | No documented layout | `e620d33b1fb8`  |
| 998    | No documented layout | `e620d33b1fb8`  |
| 990    | No documented layout | `e620d33b1fb8`  |
| 979    | No documented layout | `e620d33b1fb8`  |
| 972    | No documented layout | `e620d33b1fb8`  |
| 963    | No documented layout | `e620d33b1fb8`  |
| 955    | No documented layout | `e620d33b1fb8`  |
| 946    | No documented layout | `e620d33b1fb8`  |
| 938    | No documented layout | `e620d33b1fb8`  |
| 927    | No documented layout | `e620d33b1fb8`  |
| 911    | No documented layout | `e620d33b1fb8`  |
| 904    | No documented layout | `e620d33b1fb8`  |
| 899    | No documented layout | `e620d33b1fb8`  |
| 894    | No documented layout | `e620d33b1fb8`  |
| 885    | No documented layout | `e620d33b1fb8`  |
| 879    | No documented layout | `e620d33b1fb8`  |
| 872    | No documented layout | `e620d33b1fb8`  |
| 864    | No documented layout | `e620d33b1fb8`  |
| 855    | No documented layout | `e620d33b1fb8`  |
| 853    | No documented layout | `e620d33b1fb8`  |
| 845    | No documented layout | `e620d33b1fb8`  |
| 837    | No documented layout | `e620d33b1fb8`  |
| 829    | No documented layout | `e620d33b1fb8`  |
| 822    | No documented layout | `e620d33b1fb8`  |
| 814    | No documented layout | `e620d33b1fb8`  |
| 805    | No documented layout | `e620d33b1fb8`  |
| 794    | No documented layout | `e620d33b1fb8`  |
| 787    | No documented layout | `e620d33b1fb8`  |
| 780    | No documented layout | `e620d33b1fb8`  |
| 771    | No documented layout | `e620d33b1fb8`  |
| 760    | No documented layout | `e620d33b1fb8`  |
| 748    | No documented layout | `e620d33b1fb8`  |
| 741    | No documented layout | `e620d33b1fb8`  |
| 736    | No documented layout | `e620d33b1fb8`  |
| 731    | No documented layout | `e620d33b1fb8`  |
| 723    | No documented layout | `e620d33b1fb8`  |
| 711    | No documented layout | `e620d33b1fb8`  |
| 707    | No documented layout | `e620d33b1fb8`  |
| 697    | No documented layout | `e620d33b1fb8`  |
| 689    | No documented layout | `e620d33b1fb8`  |
| 683    | No documented layout | `e620d33b1fb8`  |
| 678    | No documented layout | `e620d33b1fb8`  |
| 670    | No documented layout | `e620d33b1fb8`  |
| 661    | No documented layout | `e620d33b1fb8`  |
| 656    | No documented layout | `e620d33b1fb8`  |
| 652    | No documented layout | `e620d33b1fb8`  |
| 643    | No documented layout | `e620d33b1fb8`  |
| 637    | No documented layout | `e620d33b1fb8`  |
| 630    | No documented layout | `e620d33b1fb8`  |
| 627    | No documented layout | `e620d33b1fb8`  |
| 621    | No documented layout | `e620d33b1fb8`  |
| 617    | No documented layout | `e620d33b1fb8`  |
| 615    | No documented layout | `e620d33b1fb8`  |
| 606    | No documented layout | `e620d33b1fb8`  |
| 599    | No documented layout | `e620d33b1fb8`  |
| 592    | No documented layout | `e620d33b1fb8`  |
| 586    | No documented layout | `e620d33b1fb8`  |
| 577    | No documented layout | `e620d33b1fb8`  |
| 569    | No documented layout | `e620d33b1fb8`  |
| 561    | No documented layout | `e620d33b1fb8`  |
| 554    | No documented layout | `e620d33b1fb8`  |
| 542    | No documented layout | `e620d33b1fb8`  |
| 532    | No documented layout | `e620d33b1fb8`  |
| 531    | No documented layout | `e620d33b1fb8`  |
| 526    | No documented layout | `e620d33b1fb8`  |
| 521    | No documented layout | `e620d33b1fb8`  |
| 517    | No documented layout | `e620d33b1fb8`  |
| 510    | No documented layout | `e620d33b1fb8`  |
| 508    | No documented layout | `e620d33b1fb8`  |
| 504    | No documented layout | `e620d33b1fb8`  |
| 497    | No documented layout | `e620d33b1fb8`  |
| 491    | No documented layout | `e620d33b1fb8`  |
| 485    | No documented layout | `e620d33b1fb8`  |
| 478    | No documented layout | `e620d33b1fb8`  |
| 472    | No documented layout | `e620d33b1fb8`  |
| 466    | No documented layout | `e620d33b1fb8`  |
| 457    | No documented layout | `e620d33b1fb8`  |
| 452    | No documented layout | `e620d33b1fb8`  |
| 449    | No documented layout | `e620d33b1fb8`  |
| 435    | No documented layout | `e620d33b1fb8`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                       |
| --------------------- | -------- | ---------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Translated text, type `37` keyed by the row hash and sheet |

All multi-byte values are little-endian unless noted otherwise.

## Layout 1

### File Layout

A PABR file of eight sheets, followed by the same counted string table and
8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings). Every
string in the table is UTF-16LE (`is_wide=1`).

| Offset              | Type               | Field              | Notes                                                |
| ------------------- | ------------------ | ------------------ | ---------------------------------------------------- |
| `+0x00`             | char[4]            | magic              | ASCII `PABR`                                         |
| `+0x04`             | u32                | sheet_count        | `8` on client 3458                                   |
| `+0x08`             | Sheet[sheet_count] | sheets             | Sheets back to back, see Sheet                       |
| `sheets+0x00`       | String Table       | string_table       | See String Table                                     |
| `string_table+0x00` | u32                | string_table_start | Where the last sheet ends (`0xC6DD8` on client 3458) |
| `string_table+0x04` | u32                | zero               | Always `0`                                           |

### Sheet (variable: 12 bytes + rows)

A 12-byte sheet header, then the sheet's rows.

| Offset  | Type                  | Field      | Notes                                                          |
| ------- | --------------------- | ---------- | -------------------------------------------------------------- |
| `+0x00` | u32                   | sheet_hash | Key hash of the sheet name (see Key Hash)                      |
| `+0x04` | u32                   | name_ref   | String table index of the sheet name (`GAME`, `RESOURCE`, ...) |
| `+0x08` | u32                   | row_count  | Number of 16-byte rows that follow                             |
| `+0x0C` | String Row[row_count] | rows       | See String Row                                                 |

### String Row (16 bytes)

| Offset  | Type | Field      | Notes                                                                  |
| ------- | ---- | ---------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | key_hash   | Key hash of the key string (see Key Hash); the LOC type `37` `str_id1` |
| `+0x04` | u32  | key_ref    | String table index of the key, e.g. `NPCSHOP_BUY`                      |
| `+0x08` | u32  | value_ref  | String table index of the Korean text; never empty, 7 are one space    |
| `+0x0C` | u32  | unknown_0c | Always `0`                                                             |

Rows are not sorted by hash or key. The string table is interned: each string
is stored once, in the order the sheets first use it (sheet name, then key
and value of each row), and later uses point back. No key repeats within a
sheet; 6,553 values reuse an earlier text such as `"확인"`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                 |
| ------- | ------------------ | ------------ | ------------------------------------- |
| `+0x00` | u32                | string_count | `95,195` strings on client 3458       |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries, all UTF-16LE     |

## Key Hash

`key_hash` and `sheet_hash` are Bob Jenkins' lookup3 `hashlittle()` over the
UTF-16LE string without a terminator, seed `0xC5EDE`:
`LUA_GROWTHPASS_WIDGET_ICON_NOTICE_NEW_DESC` -> `1517777731`, `GAME` ->
`3183609639`. It matches all 50,992 key hashes and all 8 sheet hashes on
client 3464 (`test_every_key_hash_is_the_key_hash_of_its_key` and
`test_every_sheet_hash_is_the_key_hash_of_its_name`). The same function keys
the LOC type 59 TextBind texts (see `languagedata_loc.md`, Type 59). The
browser computes it with `key_hash()` in `_common/string_hash.py`.

## Sheets

The sheet order is fixed on client 3458. `loc str_id2` is the LOC type `37`
`str_id2` that every LOC row of that sheet's keys carries.

| # | Name          | Hash         | Rows   | `loc str_id2` | Holds                                                      |
| - | ------------- | ------------ | ------ | ------------- | ---------------------------------------------------------- |
| 0 | `GAME`        | `0xBDC20727` | 22,936 | `1`           | Lua UI strings (`LUA_*`, `WEBHELPER_*`), labels and tooltips |
| 1 | `SymbolNo`    | `0xA9B8EA3C` | 4,529  | `6`           | Server error and result messages (`eErrNo*`)               |
| 2 | `IMAGESLIDE`  | `0x8AD0A01B` | 204    | `7`           | Image slide subtitles (`SEQUENCE_SUBTITLE_IMAGE_SLIDE_*`)  |
| 3 | `ACTIONCHART` | `0x138A8C63` | 2,000  | `3`           | Speech bubbles and action lines (`Bubble_*`, `Trade_*`)     |
| 4 | `RESOURCE`    | `0x9C44332D` | 9,525  | `2`           | UI panel resources (`PANEL_*`)                             |
| 5 | `CUTSCENE`    | `0x08342431` | 8,564  | `0`           | Cutscene subtitles (`CS_*`)                                |
| 6 | `TOOL`        | `0xE09F9402` | 785    | `4`           | Enum labels (`eSymNo*`), e.g. chat types, log reasons      |
| 7 | `WEB`         | `0xA5AA1B9E` | 2,360  | `5`           | In-game web page strings (`WEB_*`)                         |

This settles which LOC type `37` `str_id2` is which sheet (the old
"Type 37 sheet names" question in
[`languagedata_loc.md`](../other/languagedata_loc.md)).

## LOC Join

Look up a key's translated text as LOC type `37`, `str_id1 = key_hash`,
`str_id2 = ` the sheet's `loc str_id2`, `str_id3 = 0`, `str_id4 = 0`.

- 50,779 of the 50,903 rows have a LOC row on client 3458. The other 124
  (62 `GAME`, 33 `CUTSCENE`, 17 `RESOURCE`, 12 `SymbolNo`) have Korean text
  only; they read like newer content not yet translated, so fall back to
  the Korean `value_ref` text.
- 44 keys sit in two sheets (`NPCSHOP_BUY` in `GAME` and `RESOURCE`). Both
  rows carry the same hash and share the key string, and LOC keeps them
  apart by `str_id2`, which can hold different text (`ALCHEMY_MANUFACTURE_BTN_MANUFACTURE`:
  `GAME` "Start", `RESOURCE` "Start Crafting"). So the hash depends on the
  key alone, not on the sheet.
- 3,027 LOC type `37` `str_id1` values have no row here; keys dropped from
  the client whose translations LOC still carries.
- 352 LOC rows use `str_id3 = 1` as a second variant of a key, mostly
  regional URLs (`WEBHELPER_*_EN`) and date lines (`*_GMT`, `*_UTC`). 164 keys
  have only the `str_id3 = 1` row, so a lookup should try `str_id3 = 0` first
  and then `1`. `str_id4` is always `0`.

### Town NPC Navigation Types

The `GAME` sheet holds the town NPC navigation labels as
`LUA_WIDGET_TOWNNPCNAVI_NPCTYPETEXT_1` to `_39`, one per number with no gaps.
The client picks them by `SpawnType`, and the suffix is not always the
`SpawnType` value; the full mapping is the Navi label column of
[`characterspawntype.dbss` SpawnType](../dbss/characterspawntype_dbss.md#spawntype).
A few, as the English LOC text:

| Key suffix | Korean        | English (LOC)              | SpawnType          |
| ---------- | ------------- | -------------------------- | ------------------ |
| `_1`       | 기술 교관     | Skill Instructor           | `SkillTrainer` (1) |
| `_6`       | 창고          | Storage                    | `WareHouse` (6)    |
| `_25`      | 아이템 거래소 | Central Market             | `ItemMarket` (25)  |
| `_35`      | 악기 상인     | Instruments                | `Instrument` (40)  |
| `_39`      | 황실제작 납품 | Imperial Crafting Delivery | `SupplyShop` (33)  |

The client reads these through `PAGetString(Defines.StringSheet_GAME, key)`,
so a script's `StringSheet_<name>` picks the sheet and with it the LOC
`str_id2`.

## Notes

- Seven `GAME` values are a single space (`LUA_JOIN_LOCALWAR_RULE7`,
  `LUA_LOCALWARINFO_DESC_RULETEXT_9` and others on client 3458), unused rule
  and condition lines; the table shows them as a dash when LOC has no text.
- Some values forward to another text rather than holding it, e.g.
  `ALCHEMY_COOK_TEXT_DESCRPITION` = `{TextBind:TEXTBIND_ALCHEMY_COOK_TEXT_DESCRPITION}`,
  and the LOC text keeps the same placeholder. The text it names is LOC type
  59, keyed by the key hash of the name (`languagedata_loc.md`, Type 59), or
  the Korean `textbind.dbss` record of that key. The Text column shows it
  filled; the Korean column keeps the value as stored. 460 values hold a
  placeholder on client 3464. Values also carry `<PAColor...>` tags and
  `{name}` placeholders.
- bdo-data-extractor names the sheets `GAME`, `RESOURCE`, `ACTIONCHART` and
  others; the names are stored in this file, so that part is now confirmed.

## Open Questions

### `str_id3 = 1` Variants

352 LOC type `37` rows use `str_id3 = 1`. Most look like a second,
region-specific text of the key (a newer URL, a UTC instead of GMT date line),
but some keys have only the `str_id3 = 1` row. Which condition makes the client
pick variant `1` is not known.
