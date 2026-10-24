# `pcgrowthdefaultcharacterkey.bss` Format

## Purpose

An 18-byte PABR file holding one u16 character key, `47` on client 3464. It sits next to [pcgrowth](pcgrowth_dbss.md) and [pcgrowthsimply](pcgrowthsimply_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | -------------- | --------- |
| 1      | 1250 and later | 3483    | `pcgrowthdefaultcharacterkey.bss` | 18    | 1 String Table | 4         |

| Layout | File                              | Known         | Unknown    |
| ------ | --------------------------------- | ------------- | ---------- |
| 1      | `pcgrowthdefaultcharacterkey.bss` | 18 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `093199a5ef3c`  |
| 3482   | Layout 1 | `093199a5ef3c`  |
| 3474   | Layout 1 | `093199a5ef3c`  |
| 3473   | Layout 1 | `093199a5ef3c`  |
| 3464   | Layout 1 | `093199a5ef3c`  |
| 3458   | Layout 1 | `093199a5ef3c`  |
| 3454   | Layout 1 | `093199a5ef3c`  |
| 3444   | Layout 1 | `093199a5ef3c`  |
| 3435   | Layout 1 | `093199a5ef3c`  |
| 3426   | Layout 1 | `093199a5ef3c`  |
| 3418   | Layout 1 | `093199a5ef3c`  |
| 3412   | Layout 1 | `093199a5ef3c`  |
| 3402   | Layout 1 | `093199a5ef3c`  |
| 3396   | Layout 1 | `093199a5ef3c`  |
| 3387   | Layout 1 | `093199a5ef3c`  |
| 3381   | Layout 1 | `093199a5ef3c`  |
| 3373   | Layout 1 | `093199a5ef3c`  |
| 3364   | Layout 1 | `093199a5ef3c`  |
| 3356   | Layout 1 | `093199a5ef3c`  |
| 3349   | Layout 1 | `093199a5ef3c`  |
| 3342   | Layout 1 | `093199a5ef3c`  |
| 3335   | Layout 1 | `093199a5ef3c`  |
| 3326   | Layout 1 | `093199a5ef3c`  |
| 3321   | Layout 1 | `093199a5ef3c`  |
| 3314   | Layout 1 | `093199a5ef3c`  |
| 3303   | Layout 1 | `093199a5ef3c`  |
| 3302   | Layout 1 | `093199a5ef3c`  |
| 3293   | Layout 1 | `093199a5ef3c`  |
| 3283   | Layout 1 | `093199a5ef3c`  |
| 3275   | Layout 1 | `093199a5ef3c`  |
| 3267   | Layout 1 | `093199a5ef3c`  |
| 3258   | Layout 1 | `093199a5ef3c`  |
| 3251   | Layout 1 | `093199a5ef3c`  |
| 3242   | Layout 1 | `093199a5ef3c`  |
| 3235   | Layout 1 | `093199a5ef3c`  |
| 3229   | Layout 1 | `093199a5ef3c`  |
| 3212   | Layout 1 | `093199a5ef3c`  |
| 3203   | Layout 1 | `093199a5ef3c`  |
| 3193   | Layout 1 | `093199a5ef3c`  |
| 3186   | Layout 1 | `093199a5ef3c`  |
| 3177   | Layout 1 | `093199a5ef3c`  |
| 3169   | Layout 1 | `093199a5ef3c`  |
| 3158   | Layout 1 | `093199a5ef3c`  |
| 3151   | Layout 1 | `093199a5ef3c`  |
| 3144   | Layout 1 | `093199a5ef3c`  |
| 3133   | Layout 1 | `093199a5ef3c`  |
| 3125   | Layout 1 | `093199a5ef3c`  |
| 3118   | Layout 1 | `093199a5ef3c`  |
| 3111   | Layout 1 | `093199a5ef3c`  |
| 3103   | Layout 1 | `093199a5ef3c`  |
| 3095   | Layout 1 | `093199a5ef3c`  |
| 3086   | Layout 1 | `093199a5ef3c`  |
| 3072   | Layout 1 | `093199a5ef3c`  |
| 3062   | Layout 1 | `093199a5ef3c`  |
| 3052   | Layout 1 | `093199a5ef3c`  |
| 3045   | Layout 1 | `093199a5ef3c`  |
| 3037   | Layout 1 | `093199a5ef3c`  |
| 3030   | Layout 1 | `093199a5ef3c`  |
| 3021   | Layout 1 | `093199a5ef3c`  |
| 3012   | Layout 1 | `093199a5ef3c`  |
| 3002   | Layout 1 | `093199a5ef3c`  |
| 2995   | Layout 1 | `093199a5ef3c`  |
| 2987   | Layout 1 | `093199a5ef3c`  |
| 2978   | Layout 1 | `093199a5ef3c`  |
| 2970   | Layout 1 | `093199a5ef3c`  |
| 2959   | Layout 1 | `093199a5ef3c`  |
| 2951   | Layout 1 | `093199a5ef3c`  |
| 2942   | Layout 1 | `093199a5ef3c`  |
| 2935   | Layout 1 | `093199a5ef3c`  |
| 2932   | Layout 1 | `093199a5ef3c`  |
| 2923   | Layout 1 | `093199a5ef3c`  |
| 2919   | Layout 1 | `093199a5ef3c`  |
| 2907   | Layout 1 | `093199a5ef3c`  |
| 2900   | Layout 1 | `093199a5ef3c`  |
| 2891   | Layout 1 | `093199a5ef3c`  |
| 2882   | Layout 1 | `093199a5ef3c`  |
| 2872   | Layout 1 | `093199a5ef3c`  |
| 2863   | Layout 1 | `093199a5ef3c`  |
| 2855   | Layout 1 | `093199a5ef3c`  |
| 2849   | Layout 1 | `093199a5ef3c`  |
| 2844   | Layout 1 | `093199a5ef3c`  |
| 2834   | Layout 1 | `093199a5ef3c`  |
| 2825   | Layout 1 | `093199a5ef3c`  |
| 2819   | Layout 1 | `093199a5ef3c`  |
| 2811   | Layout 1 | `093199a5ef3c`  |
| 2803   | Layout 1 | `093199a5ef3c`  |
| 2794   | Layout 1 | `093199a5ef3c`  |
| 2783   | Layout 1 | `093199a5ef3c`  |
| 2774   | Layout 1 | `093199a5ef3c`  |
| 2765   | Layout 1 | `093199a5ef3c`  |
| 2756   | Layout 1 | `093199a5ef3c`  |
| 2750   | Layout 1 | `093199a5ef3c`  |
| 2743   | Layout 1 | `093199a5ef3c`  |
| 2736   | Layout 1 | `093199a5ef3c`  |
| 2726   | Layout 1 | `093199a5ef3c`  |
| 2717   | Layout 1 | `093199a5ef3c`  |
| 2709   | Layout 1 | `093199a5ef3c`  |
| 2703   | Layout 1 | `093199a5ef3c`  |
| 2695   | Layout 1 | `093199a5ef3c`  |
| 2684   | Layout 1 | `093199a5ef3c`  |
| 2672   | Layout 1 | `093199a5ef3c`  |
| 2665   | Layout 1 | `093199a5ef3c`  |
| 2657   | Layout 1 | `093199a5ef3c`  |
| 2649   | Layout 1 | `093199a5ef3c`  |
| 2644   | Layout 1 | `093199a5ef3c`  |
| 2637   | Layout 1 | `093199a5ef3c`  |
| 2629   | Layout 1 | `093199a5ef3c`  |
| 2619   | Layout 1 | `093199a5ef3c`  |
| 2612   | Layout 1 | `093199a5ef3c`  |
| 2606   | Layout 1 | `093199a5ef3c`  |
| 2602   | Layout 1 | `093199a5ef3c`  |
| 2601   | Layout 1 | `093199a5ef3c`  |
| 2592   | Layout 1 | `093199a5ef3c`  |
| 2583   | Layout 1 | `093199a5ef3c`  |
| 2575   | Layout 1 | `093199a5ef3c`  |
| 2567   | Layout 1 | `093199a5ef3c`  |
| 2560   | Layout 1 | `093199a5ef3c`  |
| 2553   | Layout 1 | `093199a5ef3c`  |
| 2545   | Layout 1 | `093199a5ef3c`  |
| 2538   | Layout 1 | `093199a5ef3c`  |
| 2529   | Layout 1 | `093199a5ef3c`  |
| 2519   | Layout 1 | `093199a5ef3c`  |
| 2513   | Layout 1 | `093199a5ef3c`  |
| 2510   | Layout 1 | `093199a5ef3c`  |
| 2507   | Layout 1 | `093199a5ef3c`  |
| 2503   | Layout 1 | `093199a5ef3c`  |
| 2498   | Layout 1 | `093199a5ef3c`  |
| 2492   | Layout 1 | `093199a5ef3c`  |
| 2487   | Layout 1 | `093199a5ef3c`  |
| 2480   | Layout 1 | `093199a5ef3c`  |
| 2474   | Layout 1 | `093199a5ef3c`  |
| 2468   | Layout 1 | `093199a5ef3c`  |
| 2460   | Layout 1 | `093199a5ef3c`  |
| 2453   | Layout 1 | `093199a5ef3c`  |
| 2444   | Layout 1 | `093199a5ef3c`  |
| 2438   | Layout 1 | `093199a5ef3c`  |
| 2434   | Layout 1 | `093199a5ef3c`  |
| 2429   | Layout 1 | `093199a5ef3c`  |
| 2421   | Layout 1 | `093199a5ef3c`  |
| 2414   | Layout 1 | `093199a5ef3c`  |
| 2407   | Layout 1 | `093199a5ef3c`  |
| 2401   | Layout 1 | `093199a5ef3c`  |
| 2397   | Layout 1 | `093199a5ef3c`  |
| 2393   | Layout 1 | `093199a5ef3c`  |
| 2384   | Layout 1 | `093199a5ef3c`  |
| 2378   | Layout 1 | `093199a5ef3c`  |
| 2372   | Layout 1 | `093199a5ef3c`  |
| 2358   | Layout 1 | `093199a5ef3c`  |
| 2352   | Layout 1 | `093199a5ef3c`  |
| 2347   | Layout 1 | `093199a5ef3c`  |
| 2343   | Layout 1 | `093199a5ef3c`  |
| 2335   | Layout 1 | `093199a5ef3c`  |
| 2327   | Layout 1 | `093199a5ef3c`  |
| 2324   | Layout 1 | `093199a5ef3c`  |
| 2319   | Layout 1 | `093199a5ef3c`  |
| 2313   | Layout 1 | `093199a5ef3c`  |
| 2308   | Layout 1 | `093199a5ef3c`  |
| 2302   | Layout 1 | `093199a5ef3c`  |
| 2295   | Layout 1 | `093199a5ef3c`  |
| 2290   | Layout 1 | `093199a5ef3c`  |
| 2284   | Layout 1 | `093199a5ef3c`  |
| 2276   | Layout 1 | `093199a5ef3c`  |
| 2269   | Layout 1 | `093199a5ef3c`  |
| 2259   | Layout 1 | `093199a5ef3c`  |
| 2250   | Layout 1 | `093199a5ef3c`  |
| 2243   | Layout 1 | `093199a5ef3c`  |
| 2235   | Layout 1 | `093199a5ef3c`  |
| 2229   | Layout 1 | `093199a5ef3c`  |
| 2224   | Layout 1 | `093199a5ef3c`  |
| 2218   | Layout 1 | `093199a5ef3c`  |
| 2215   | Layout 1 | `093199a5ef3c`  |
| 2207   | Layout 1 | `093199a5ef3c`  |
| 2203   | Layout 1 | `093199a5ef3c`  |
| 2196   | Layout 1 | `093199a5ef3c`  |
| 2192   | Layout 1 | `093199a5ef3c`  |
| 2189   | Layout 1 | `093199a5ef3c`  |
| 2183   | Layout 1 | `093199a5ef3c`  |
| 2179   | Layout 1 | `093199a5ef3c`  |
| 2171   | Layout 1 | `093199a5ef3c`  |
| 2163   | Layout 1 | `093199a5ef3c`  |
| 2156   | Layout 1 | `093199a5ef3c`  |
| 2151   | Layout 1 | `093199a5ef3c`  |
| 2147   | Layout 1 | `093199a5ef3c`  |
| 2142   | Layout 1 | `093199a5ef3c`  |
| 2138   | Layout 1 | `093199a5ef3c`  |
| 2134   | Layout 1 | `093199a5ef3c`  |
| 2130   | Layout 1 | `093199a5ef3c`  |
| 2122   | Layout 1 | `093199a5ef3c`  |
| 2107   | Layout 1 | `093199a5ef3c`  |
| 2098   | Layout 1 | `093199a5ef3c`  |
| 2089   | Layout 1 | `093199a5ef3c`  |
| 2081   | Layout 1 | `093199a5ef3c`  |
| 2073   | Layout 1 | `093199a5ef3c`  |
| 2067   | Layout 1 | `093199a5ef3c`  |
| 2063   | Layout 1 | `093199a5ef3c`  |
| 2059   | Layout 1 | `093199a5ef3c`  |
| 2052   | Layout 1 | `093199a5ef3c`  |
| 2044   | Layout 1 | `093199a5ef3c`  |
| 2039   | Layout 1 | `093199a5ef3c`  |
| 2032   | Layout 1 | `093199a5ef3c`  |
| 2025   | Layout 1 | `093199a5ef3c`  |
| 2011   | Layout 1 | `093199a5ef3c`  |
| 2005   | Layout 1 | `093199a5ef3c`  |
| 2000   | Layout 1 | `093199a5ef3c`  |
| 1996   | Layout 1 | `093199a5ef3c`  |
| 1991   | Layout 1 | `093199a5ef3c`  |
| 1985   | Layout 1 | `093199a5ef3c`  |
| 1980   | Layout 1 | `093199a5ef3c`  |
| 1969   | Layout 1 | `093199a5ef3c`  |
| 1964   | Layout 1 | `093199a5ef3c`  |
| 1958   | Layout 1 | `093199a5ef3c`  |
| 1950   | Layout 1 | `093199a5ef3c`  |
| 1945   | Layout 1 | `093199a5ef3c`  |
| 1937   | Layout 1 | `093199a5ef3c`  |
| 1933   | Layout 1 | `093199a5ef3c`  |
| 1927   | Layout 1 | `093199a5ef3c`  |
| 1921   | Layout 1 | `093199a5ef3c`  |
| 1914   | Layout 1 | `093199a5ef3c`  |
| 1908   | Layout 1 | `093199a5ef3c`  |
| 1897   | Layout 1 | `093199a5ef3c`  |
| 1892   | Layout 1 | `093199a5ef3c`  |
| 1886   | Layout 1 | `093199a5ef3c`  |
| 1881   | Layout 1 | `093199a5ef3c`  |
| 1871   | Layout 1 | `093199a5ef3c`  |
| 1866   | Layout 1 | `093199a5ef3c`  |
| 1862   | Layout 1 | `093199a5ef3c`  |
| 1854   | Layout 1 | `093199a5ef3c`  |
| 1846   | Layout 1 | `093199a5ef3c`  |
| 1838   | Layout 1 | `093199a5ef3c`  |
| 1832   | Layout 1 | `093199a5ef3c`  |
| 1826   | Layout 1 | `093199a5ef3c`  |
| 1822   | Layout 1 | `093199a5ef3c`  |
| 1818   | Layout 1 | `093199a5ef3c`  |
| 1804   | Layout 1 | `093199a5ef3c`  |
| 1794   | Layout 1 | `093199a5ef3c`  |
| 1790   | Layout 1 | `093199a5ef3c`  |
| 1784   | Layout 1 | `093199a5ef3c`  |
| 1774   | Layout 1 | `093199a5ef3c`  |
| 1771   | Layout 1 | `093199a5ef3c`  |
| 1762   | Layout 1 | `093199a5ef3c`  |
| 1759   | Layout 1 | `093199a5ef3c`  |
| 1754   | Layout 1 | `093199a5ef3c`  |
| 1749   | Layout 1 | `093199a5ef3c`  |
| 1743   | Layout 1 | `093199a5ef3c`  |
| 1737   | Layout 1 | `093199a5ef3c`  |
| 1731   | Layout 1 | `093199a5ef3c`  |
| 1725   | Layout 1 | `093199a5ef3c`  |
| 1717   | Layout 1 | `093199a5ef3c`  |
| 1710   | Layout 1 | `093199a5ef3c`  |
| 1704   | Layout 1 | `093199a5ef3c`  |
| 1698   | Layout 1 | `093199a5ef3c`  |
| 1690   | Layout 1 | `093199a5ef3c`  |
| 1685   | Layout 1 | `093199a5ef3c`  |
| 1680   | Layout 1 | `093199a5ef3c`  |
| 1674   | Layout 1 | `093199a5ef3c`  |
| 1668   | Layout 1 | `093199a5ef3c`  |
| 1659   | Layout 1 | `093199a5ef3c`  |
| 1649   | Layout 1 | `093199a5ef3c`  |
| 1642   | Layout 1 | `093199a5ef3c`  |
| 1636   | Layout 1 | `093199a5ef3c`  |
| 1628   | Layout 1 | `093199a5ef3c`  |
| 1622   | Layout 1 | `093199a5ef3c`  |
| 1614   | Layout 1 | `093199a5ef3c`  |
| 1608   | Layout 1 | `093199a5ef3c`  |
| 1602   | Layout 1 | `093199a5ef3c`  |
| 1598   | Layout 1 | `093199a5ef3c`  |
| 1594   | Layout 1 | `093199a5ef3c`  |
| 1590   | Layout 1 | `093199a5ef3c`  |
| 1587   | Layout 1 | `093199a5ef3c`  |
| 1584   | Layout 1 | `093199a5ef3c`  |
| 1579   | Layout 1 | `093199a5ef3c`  |
| 1572   | Layout 1 | `093199a5ef3c`  |
| 1565   | Layout 1 | `093199a5ef3c`  |
| 1559   | Layout 1 | `093199a5ef3c`  |
| 1554   | Layout 1 | `093199a5ef3c`  |
| 1547   | Layout 1 | `093199a5ef3c`  |
| 1537   | Layout 1 | `093199a5ef3c`  |
| 1529   | Layout 1 | `093199a5ef3c`  |
| 1524   | Layout 1 | `093199a5ef3c`  |
| 1519   | Layout 1 | `093199a5ef3c`  |
| 1509   | Layout 1 | `093199a5ef3c`  |
| 1506   | Layout 1 | `093199a5ef3c`  |
| 1504   | Layout 1 | `093199a5ef3c`  |
| 1500   | Layout 1 | `093199a5ef3c`  |
| 1493   | Layout 1 | `093199a5ef3c`  |
| 1489   | Layout 1 | `093199a5ef3c`  |
| 1485   | Layout 1 | `093199a5ef3c`  |
| 1481   | Layout 1 | `093199a5ef3c`  |
| 1474   | Layout 1 | `093199a5ef3c`  |
| 1466   | Layout 1 | `093199a5ef3c`  |
| 1462   | Layout 1 | `093199a5ef3c`  |
| 1459   | Layout 1 | `093199a5ef3c`  |
| 1453   | Layout 1 | `093199a5ef3c`  |
| 1450   | Layout 1 | `093199a5ef3c`  |
| 1445   | Layout 1 | `093199a5ef3c`  |
| 1439   | Layout 1 | `093199a5ef3c`  |
| 1433   | Layout 1 | `093199a5ef3c`  |
| 1430   | Layout 1 | `093199a5ef3c`  |
| 1426   | Layout 1 | `093199a5ef3c`  |
| 1421   | Layout 1 | `093199a5ef3c`  |
| 1417   | Layout 1 | `093199a5ef3c`  |
| 1416   | Layout 1 | `093199a5ef3c`  |
| 1409   | Layout 1 | `093199a5ef3c`  |
| 1405   | Layout 1 | `093199a5ef3c`  |
| 1401   | Layout 1 | `093199a5ef3c`  |
| 1396   | Layout 1 | `093199a5ef3c`  |
| 1391   | Layout 1 | `093199a5ef3c`  |
| 1390   | Layout 1 | `093199a5ef3c`  |
| 1386   | Layout 1 | `093199a5ef3c`  |
| 1381   | Layout 1 | `093199a5ef3c`  |
| 1379   | Layout 1 | `093199a5ef3c`  |
| 1372   | Layout 1 | `093199a5ef3c`  |
| 1366   | Layout 1 | `093199a5ef3c`  |
| 1364   | Layout 1 | `093199a5ef3c`  |
| 1363   | Layout 1 | `093199a5ef3c`  |
| 1360   | Layout 1 | `093199a5ef3c`  |
| 1358   | Layout 1 | `093199a5ef3c`  |
| 1355   | Layout 1 | `093199a5ef3c`  |
| 1351   | Layout 1 | `093199a5ef3c`  |
| 1348   | Layout 1 | `093199a5ef3c`  |
| 1346   | Layout 1 | `093199a5ef3c`  |
| 1341   | Layout 1 | `093199a5ef3c`  |
| 1340   | Layout 1 | `093199a5ef3c`  |
| 1338   | Layout 1 | `093199a5ef3c`  |
| 1335   | Layout 1 | `093199a5ef3c`  |
| 1333   | Layout 1 | `093199a5ef3c`  |
| 1329   | Layout 1 | `093199a5ef3c`  |
| 1327   | Layout 1 | `093199a5ef3c`  |
| 1324   | Layout 1 | `093199a5ef3c`  |
| 1321   | Layout 1 | `093199a5ef3c`  |
| 1319   | Layout 1 | `093199a5ef3c`  |
| 1318   | Layout 1 | `093199a5ef3c`  |
| 1316   | Layout 1 | `093199a5ef3c`  |
| 1313   | Layout 1 | `093199a5ef3c`  |
| 1311   | Layout 1 | `093199a5ef3c`  |
| 1309   | Layout 1 | `093199a5ef3c`  |
| 1304   | Layout 1 | `093199a5ef3c`  |
| 1292   | Layout 1 | `093199a5ef3c`  |
| 1286   | Layout 1 | `093199a5ef3c`  |
| 1280   | Layout 1 | `093199a5ef3c`  |
| 1276   | Layout 1 | `093199a5ef3c`  |
| 1267   | Layout 1 | `093199a5ef3c`  |
| 1261   | Layout 1 | `093199a5ef3c`  |
| 1256   | Layout 1 | `093199a5ef3c`  |
| 1250   | Layout 1 | `093199a5ef3c`  |
| 1246   | No file  | `093199a5ef3c`  |
| 1239   | No file  | `093199a5ef3c`  |
| 1230   | No file  | `093199a5ef3c`  |
| 1226   | No file  | `093199a5ef3c`  |
| 1220   | No file  | `093199a5ef3c`  |
| 1217   | No file  | `093199a5ef3c`  |
| 1211   | No file  | `093199a5ef3c`  |
| 1210   | No file  | `093199a5ef3c`  |
| 1208   | No file  | `093199a5ef3c`  |
| 1203   | No file  | `093199a5ef3c`  |
| 1197   | No file  | `093199a5ef3c`  |
| 1194   | No file  | `093199a5ef3c`  |
| 1192   | No file  | `093199a5ef3c`  |
| 1187   | No file  | `093199a5ef3c`  |
| 1183   | No file  | `093199a5ef3c`  |
| 1177   | No file  | `093199a5ef3c`  |
| 1173   | No file  | `093199a5ef3c`  |
| 1167   | No file  | `093199a5ef3c`  |
| 1164   | No file  | `093199a5ef3c`  |
| 1156   | No file  | `093199a5ef3c`  |
| 1149   | No file  | `093199a5ef3c`  |
| 1144   | No file  | `093199a5ef3c`  |
| 1137   | No file  | `093199a5ef3c`  |
| 1132   | No file  | `093199a5ef3c`  |
| 1127   | No file  | `093199a5ef3c`  |
| 1122   | No file  | `093199a5ef3c`  |
| 1118   | No file  | `093199a5ef3c`  |
| 1114   | No file  | `093199a5ef3c`  |
| 1109   | No file  | `093199a5ef3c`  |
| 1102   | No file  | `093199a5ef3c`  |
| 1096   | No file  | `093199a5ef3c`  |
| 1088   | No file  | `093199a5ef3c`  |
| 1081   | No file  | `093199a5ef3c`  |
| 1076   | No file  | `093199a5ef3c`  |
| 1069   | No file  | `093199a5ef3c`  |
| 1064   | No file  | `093199a5ef3c`  |
| 1058   | No file  | `093199a5ef3c`  |
| 1051   | No file  | `093199a5ef3c`  |
| 1044   | No file  | `093199a5ef3c`  |
| 1036   | No file  | `093199a5ef3c`  |
| 1026   | No file  | `093199a5ef3c`  |
| 1016   | No file  | `093199a5ef3c`  |
| 1009   | No file  | `093199a5ef3c`  |
| 1005   | No file  | `093199a5ef3c`  |
| 1000   | No file  | `093199a5ef3c`  |
| 998    | No file  | `093199a5ef3c`  |
| 990    | No file  | `093199a5ef3c`  |
| 979    | No file  | `093199a5ef3c`  |
| 972    | No file  | `093199a5ef3c`  |
| 963    | No file  | `093199a5ef3c`  |
| 955    | No file  | `093199a5ef3c`  |
| 946    | No file  | `093199a5ef3c`  |
| 938    | No file  | `093199a5ef3c`  |
| 927    | No file  | `093199a5ef3c`  |
| 911    | No file  | `093199a5ef3c`  |
| 904    | No file  | `093199a5ef3c`  |
| 899    | No file  | `093199a5ef3c`  |
| 894    | No file  | `093199a5ef3c`  |
| 885    | No file  | `093199a5ef3c`  |
| 879    | No file  | `093199a5ef3c`  |
| 872    | No file  | `093199a5ef3c`  |
| 864    | No file  | `093199a5ef3c`  |
| 855    | No file  | `093199a5ef3c`  |
| 853    | No file  | `093199a5ef3c`  |
| 845    | No file  | `093199a5ef3c`  |
| 837    | No file  | `093199a5ef3c`  |
| 829    | No file  | `093199a5ef3c`  |
| 822    | No file  | `093199a5ef3c`  |
| 814    | No file  | `093199a5ef3c`  |
| 805    | No file  | `093199a5ef3c`  |
| 794    | No file  | `093199a5ef3c`  |
| 787    | No file  | `093199a5ef3c`  |
| 780    | No file  | `093199a5ef3c`  |
| 771    | No file  | `093199a5ef3c`  |
| 760    | No file  | `093199a5ef3c`  |
| 748    | No file  | `093199a5ef3c`  |
| 741    | No file  | `093199a5ef3c`  |
| 736    | No file  | `093199a5ef3c`  |
| 731    | No file  | `093199a5ef3c`  |
| 723    | No file  | `093199a5ef3c`  |
| 711    | No file  | `093199a5ef3c`  |
| 707    | No file  | `093199a5ef3c`  |
| 697    | No file  | `093199a5ef3c`  |
| 689    | No file  | `093199a5ef3c`  |
| 683    | No file  | `093199a5ef3c`  |
| 678    | No file  | `093199a5ef3c`  |
| 670    | No file  | `093199a5ef3c`  |
| 661    | No file  | `093199a5ef3c`  |
| 656    | No file  | `093199a5ef3c`  |
| 652    | No file  | `093199a5ef3c`  |
| 643    | No file  | `093199a5ef3c`  |
| 637    | No file  | `093199a5ef3c`  |
| 630    | No file  | `093199a5ef3c`  |
| 627    | No file  | `093199a5ef3c`  |
| 621    | No file  | `093199a5ef3c`  |
| 617    | No file  | `093199a5ef3c`  |
| 615    | No file  | `093199a5ef3c`  |
| 606    | No file  | `093199a5ef3c`  |
| 599    | No file  | `093199a5ef3c`  |
| 592    | No file  | `093199a5ef3c`  |
| 586    | No file  | `093199a5ef3c`  |
| 577    | No file  | `093199a5ef3c`  |
| 569    | No file  | `093199a5ef3c`  |
| 561    | No file  | `093199a5ef3c`  |
| 554    | No file  | `093199a5ef3c`  |
| 542    | No file  | `093199a5ef3c`  |
| 532    | No file  | `093199a5ef3c`  |
| 531    | No file  | `093199a5ef3c`  |
| 526    | No file  | `093199a5ef3c`  |
| 521    | No file  | `093199a5ef3c`  |
| 517    | No file  | `093199a5ef3c`  |
| 510    | No file  | `093199a5ef3c`  |
| 508    | No file  | `093199a5ef3c`  |
| 504    | No file  | `093199a5ef3c`  |
| 497    | No file  | `093199a5ef3c`  |
| 491    | No file  | `093199a5ef3c`  |
| 485    | No file  | `093199a5ef3c`  |
| 478    | No file  | `093199a5ef3c`  |
| 472    | No file  | `093199a5ef3c`  |
| 466    | No file  | `093199a5ef3c`  |
| 457    | No file  | `093199a5ef3c`  |
| 452    | No file  | `093199a5ef3c`  |
| 449    | No file  | `093199a5ef3c`  |
| 435    | No file  | `093199a5ef3c`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes               |
| ------------------- | ------------ | ------------------ | ------------------- |
| `+0x00`             | char[4]      | magic              | `PABR`              |
| `+0x04`             | u16          | character_key      | `47` on client 3464 |
| `+0x06`             | String Table | string_table       | See String Table    |
| `string_table+0x00` | u32          | string_table_start | `6`                 |
| `string_table+0x04` | u32          | zero               | `0`                 |

The string table starts at `+0x06`, so the rows end after the single u16.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Notes

- `47` is the character key of class type 46 (`PYFW5`, LOC type 6 `PYFW5`) in `pcgrowth.dbss`, and also the row count of `pcgrowth.dbss`, `pcgrowthoffset.dbss` and `pcgrowthsimply.bss`.
- On client 1784 the file holds `65050`, a key of that client's `characterstaticoffset.dbss`, while its `pcgrowthoffset.dbss` declares 82 rows. The value is a character key on both clients; the match with the class count on client 3464 does not hold on client 1784.
