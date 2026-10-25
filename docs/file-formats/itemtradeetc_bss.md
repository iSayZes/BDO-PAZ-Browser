# `itemtradeetc.bss` Format

## Purpose

The desert trade buff per pair of trade group types: for each pair of the
trade goods' group and the buying trade NPC's group, a distance and a buff
rate. The trade sell list shows the `Desert Buff Applied` icon from these two
values. A second table of five 12-byte rows follows: the trade stock limit
threshold and rate (Field Names).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File               | Bytes | Records                | Row bytes |
| ------ | -------------- | ------------------ | ----- | ---------------------- | --------- |
| 1      | 1239 and later | `itemtradeetc.bss` | 184   | 8 Pair, 4 Group, 5 Row | 10        |

| Layout | File               | Known          | Unknown    |
| ------ | ------------------ | -------------- | ---------- |
| 1      | `itemtradeetc.bss` | 184 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `8ee02924e82e`  |
| 3482   | Layout 1 | `8ee02924e82e`  |
| 3474   | Layout 1 | `8ee02924e82e`  |
| 3473   | Layout 1 | `8ee02924e82e`  |
| 3464   | Layout 1 | `8ee02924e82e`  |
| 3458   | Layout 1 | `8ee02924e82e`  |
| 3454   | Layout 1 | `8ee02924e82e`  |
| 3444   | Layout 1 | `8ee02924e82e`  |
| 3435   | Layout 1 | `8ee02924e82e`  |
| 3426   | Layout 1 | `8ee02924e82e`  |
| 3418   | Layout 1 | `8ee02924e82e`  |
| 3412   | Layout 1 | `8ee02924e82e`  |
| 3402   | Layout 1 | `8ee02924e82e`  |
| 3396   | Layout 1 | `8ee02924e82e`  |
| 3387   | Layout 1 | `8ee02924e82e`  |
| 3381   | Layout 1 | `8ee02924e82e`  |
| 3373   | Layout 1 | `8ee02924e82e`  |
| 3364   | Layout 1 | `8ee02924e82e`  |
| 3356   | Layout 1 | `8ee02924e82e`  |
| 3349   | Layout 1 | `8ee02924e82e`  |
| 3342   | Layout 1 | `8ee02924e82e`  |
| 3335   | Layout 1 | `8ee02924e82e`  |
| 3326   | Layout 1 | `8ee02924e82e`  |
| 3321   | Layout 1 | `8ee02924e82e`  |
| 3314   | Layout 1 | `8ee02924e82e`  |
| 3303   | Layout 1 | `8ee02924e82e`  |
| 3302   | Layout 1 | `8ee02924e82e`  |
| 3293   | Layout 1 | `8ee02924e82e`  |
| 3283   | Layout 1 | `8ee02924e82e`  |
| 3275   | Layout 1 | `8ee02924e82e`  |
| 3267   | Layout 1 | `8ee02924e82e`  |
| 3258   | Layout 1 | `8ee02924e82e`  |
| 3251   | Layout 1 | `8ee02924e82e`  |
| 3242   | Layout 1 | `8ee02924e82e`  |
| 3235   | Layout 1 | `8ee02924e82e`  |
| 3229   | Layout 1 | `8ee02924e82e`  |
| 3212   | Layout 1 | `8ee02924e82e`  |
| 3203   | Layout 1 | `8ee02924e82e`  |
| 3193   | Layout 1 | `8ee02924e82e`  |
| 3186   | Layout 1 | `8ee02924e82e`  |
| 3177   | Layout 1 | `8ee02924e82e`  |
| 3169   | Layout 1 | `8ee02924e82e`  |
| 3158   | Layout 1 | `8ee02924e82e`  |
| 3151   | Layout 1 | `8ee02924e82e`  |
| 3144   | Layout 1 | `8ee02924e82e`  |
| 3133   | Layout 1 | `8ee02924e82e`  |
| 3125   | Layout 1 | `8ee02924e82e`  |
| 3118   | Layout 1 | `8ee02924e82e`  |
| 3111   | Layout 1 | `8ee02924e82e`  |
| 3103   | Layout 1 | `8ee02924e82e`  |
| 3095   | Layout 1 | `8ee02924e82e`  |
| 3086   | Layout 1 | `8ee02924e82e`  |
| 3072   | Layout 1 | `8ee02924e82e`  |
| 3062   | Layout 1 | `8ee02924e82e`  |
| 3052   | Layout 1 | `8ee02924e82e`  |
| 3045   | Layout 1 | `8ee02924e82e`  |
| 3037   | Layout 1 | `8ee02924e82e`  |
| 3030   | Layout 1 | `8ee02924e82e`  |
| 3021   | Layout 1 | `8ee02924e82e`  |
| 3012   | Layout 1 | `8ee02924e82e`  |
| 3002   | Layout 1 | `8ee02924e82e`  |
| 2995   | Layout 1 | `8ee02924e82e`  |
| 2987   | Layout 1 | `8ee02924e82e`  |
| 2978   | Layout 1 | `8ee02924e82e`  |
| 2970   | Layout 1 | `8ee02924e82e`  |
| 2959   | Layout 1 | `8ee02924e82e`  |
| 2951   | Layout 1 | `8ee02924e82e`  |
| 2942   | Layout 1 | `8ee02924e82e`  |
| 2935   | Layout 1 | `8ee02924e82e`  |
| 2932   | Layout 1 | `8ee02924e82e`  |
| 2923   | Layout 1 | `8ee02924e82e`  |
| 2919   | Layout 1 | `8ee02924e82e`  |
| 2907   | Layout 1 | `8ee02924e82e`  |
| 2900   | Layout 1 | `8ee02924e82e`  |
| 2891   | Layout 1 | `8ee02924e82e`  |
| 2882   | Layout 1 | `8ee02924e82e`  |
| 2872   | Layout 1 | `8ee02924e82e`  |
| 2863   | Layout 1 | `8ee02924e82e`  |
| 2855   | Layout 1 | `8ee02924e82e`  |
| 2849   | Layout 1 | `8ee02924e82e`  |
| 2844   | Layout 1 | `8ee02924e82e`  |
| 2834   | Layout 1 | `8ee02924e82e`  |
| 2825   | Layout 1 | `8ee02924e82e`  |
| 2819   | Layout 1 | `8ee02924e82e`  |
| 2811   | Layout 1 | `8ee02924e82e`  |
| 2803   | Layout 1 | `8ee02924e82e`  |
| 2794   | Layout 1 | `8ee02924e82e`  |
| 2783   | Layout 1 | `8ee02924e82e`  |
| 2774   | Layout 1 | `8ee02924e82e`  |
| 2765   | Layout 1 | `8ee02924e82e`  |
| 2756   | Layout 1 | `8ee02924e82e`  |
| 2750   | Layout 1 | `8ee02924e82e`  |
| 2743   | Layout 1 | `8ee02924e82e`  |
| 2736   | Layout 1 | `8ee02924e82e`  |
| 2726   | Layout 1 | `8ee02924e82e`  |
| 2717   | Layout 1 | `8ee02924e82e`  |
| 2709   | Layout 1 | `8ee02924e82e`  |
| 2703   | Layout 1 | `8ee02924e82e`  |
| 2695   | Layout 1 | `8ee02924e82e`  |
| 2684   | Layout 1 | `8ee02924e82e`  |
| 2672   | Layout 1 | `8ee02924e82e`  |
| 2665   | Layout 1 | `8ee02924e82e`  |
| 2657   | Layout 1 | `8ee02924e82e`  |
| 2649   | Layout 1 | `8ee02924e82e`  |
| 2644   | Layout 1 | `8ee02924e82e`  |
| 2637   | Layout 1 | `8ee02924e82e`  |
| 2629   | Layout 1 | `8ee02924e82e`  |
| 2619   | Layout 1 | `8ee02924e82e`  |
| 2612   | Layout 1 | `8ee02924e82e`  |
| 2606   | Layout 1 | `8ee02924e82e`  |
| 2602   | Layout 1 | `8ee02924e82e`  |
| 2601   | Layout 1 | `8ee02924e82e`  |
| 2592   | Layout 1 | `8ee02924e82e`  |
| 2583   | Layout 1 | `8ee02924e82e`  |
| 2575   | Layout 1 | `8ee02924e82e`  |
| 2567   | Layout 1 | `8ee02924e82e`  |
| 2560   | Layout 1 | `8ee02924e82e`  |
| 2553   | Layout 1 | `8ee02924e82e`  |
| 2545   | Layout 1 | `8ee02924e82e`  |
| 2538   | Layout 1 | `8ee02924e82e`  |
| 2529   | Layout 1 | `8ee02924e82e`  |
| 2519   | Layout 1 | `8ee02924e82e`  |
| 2513   | Layout 1 | `8ee02924e82e`  |
| 2510   | Layout 1 | `8ee02924e82e`  |
| 2507   | Layout 1 | `8ee02924e82e`  |
| 2503   | Layout 1 | `8ee02924e82e`  |
| 2498   | Layout 1 | `8ee02924e82e`  |
| 2492   | Layout 1 | `8ee02924e82e`  |
| 2487   | Layout 1 | `8ee02924e82e`  |
| 2480   | Layout 1 | `8ee02924e82e`  |
| 2474   | Layout 1 | `8ee02924e82e`  |
| 2468   | Layout 1 | `8ee02924e82e`  |
| 2460   | Layout 1 | `8ee02924e82e`  |
| 2453   | Layout 1 | `8ee02924e82e`  |
| 2444   | Layout 1 | `8ee02924e82e`  |
| 2438   | Layout 1 | `8ee02924e82e`  |
| 2434   | Layout 1 | `8ee02924e82e`  |
| 2429   | Layout 1 | `8ee02924e82e`  |
| 2421   | Layout 1 | `8ee02924e82e`  |
| 2414   | Layout 1 | `8ee02924e82e`  |
| 2407   | Layout 1 | `8ee02924e82e`  |
| 2401   | Layout 1 | `8ee02924e82e`  |
| 2397   | Layout 1 | `8ee02924e82e`  |
| 2393   | Layout 1 | `8ee02924e82e`  |
| 2384   | Layout 1 | `8ee02924e82e`  |
| 2378   | Layout 1 | `8ee02924e82e`  |
| 2372   | Layout 1 | `8ee02924e82e`  |
| 2358   | Layout 1 | `8ee02924e82e`  |
| 2352   | Layout 1 | `8ee02924e82e`  |
| 2347   | Layout 1 | `8ee02924e82e`  |
| 2343   | Layout 1 | `8ee02924e82e`  |
| 2335   | Layout 1 | `8ee02924e82e`  |
| 2327   | Layout 1 | `8ee02924e82e`  |
| 2324   | Layout 1 | `8ee02924e82e`  |
| 2319   | Layout 1 | `8ee02924e82e`  |
| 2313   | Layout 1 | `8ee02924e82e`  |
| 2308   | Layout 1 | `8ee02924e82e`  |
| 2302   | Layout 1 | `8ee02924e82e`  |
| 2295   | Layout 1 | `8ee02924e82e`  |
| 2290   | Layout 1 | `8ee02924e82e`  |
| 2284   | Layout 1 | `8ee02924e82e`  |
| 2276   | Layout 1 | `8ee02924e82e`  |
| 2269   | Layout 1 | `8ee02924e82e`  |
| 2259   | Layout 1 | `8ee02924e82e`  |
| 2250   | Layout 1 | `8ee02924e82e`  |
| 2243   | Layout 1 | `8ee02924e82e`  |
| 2235   | Layout 1 | `8ee02924e82e`  |
| 2229   | Layout 1 | `8ee02924e82e`  |
| 2224   | Layout 1 | `8ee02924e82e`  |
| 2218   | Layout 1 | `8ee02924e82e`  |
| 2215   | Layout 1 | `8ee02924e82e`  |
| 2207   | Layout 1 | `8ee02924e82e`  |
| 2203   | Layout 1 | `8ee02924e82e`  |
| 2196   | Layout 1 | `8ee02924e82e`  |
| 2192   | Layout 1 | `8ee02924e82e`  |
| 2189   | Layout 1 | `8ee02924e82e`  |
| 2183   | Layout 1 | `8ee02924e82e`  |
| 2179   | Layout 1 | `8ee02924e82e`  |
| 2171   | Layout 1 | `8ee02924e82e`  |
| 2163   | Layout 1 | `8ee02924e82e`  |
| 2156   | Layout 1 | `8ee02924e82e`  |
| 2151   | Layout 1 | `8ee02924e82e`  |
| 2147   | Layout 1 | `8ee02924e82e`  |
| 2142   | Layout 1 | `8ee02924e82e`  |
| 2138   | Layout 1 | `8ee02924e82e`  |
| 2134   | Layout 1 | `8ee02924e82e`  |
| 2130   | Layout 1 | `8ee02924e82e`  |
| 2122   | Layout 1 | `8ee02924e82e`  |
| 2107   | Layout 1 | `8ee02924e82e`  |
| 2098   | Layout 1 | `8ee02924e82e`  |
| 2089   | Layout 1 | `8ee02924e82e`  |
| 2081   | Layout 1 | `8ee02924e82e`  |
| 2073   | Layout 1 | `8ee02924e82e`  |
| 2067   | Layout 1 | `8ee02924e82e`  |
| 2063   | Layout 1 | `8ee02924e82e`  |
| 2059   | Layout 1 | `8ee02924e82e`  |
| 2052   | Layout 1 | `8ee02924e82e`  |
| 2044   | Layout 1 | `8ee02924e82e`  |
| 2039   | Layout 1 | `8ee02924e82e`  |
| 2032   | Layout 1 | `8ee02924e82e`  |
| 2025   | Layout 1 | `8ee02924e82e`  |
| 2011   | Layout 1 | `8ee02924e82e`  |
| 2005   | Layout 1 | `8ee02924e82e`  |
| 2000   | Layout 1 | `8ee02924e82e`  |
| 1996   | Layout 1 | `8ee02924e82e`  |
| 1991   | Layout 1 | `8ee02924e82e`  |
| 1985   | Layout 1 | `8ee02924e82e`  |
| 1980   | Layout 1 | `8ee02924e82e`  |
| 1969   | Layout 1 | `8ee02924e82e`  |
| 1964   | Layout 1 | `8ee02924e82e`  |
| 1958   | Layout 1 | `8ee02924e82e`  |
| 1950   | Layout 1 | `8ee02924e82e`  |
| 1945   | Layout 1 | `8ee02924e82e`  |
| 1937   | Layout 1 | `8ee02924e82e`  |
| 1933   | Layout 1 | `8ee02924e82e`  |
| 1927   | Layout 1 | `8ee02924e82e`  |
| 1921   | Layout 1 | `8ee02924e82e`  |
| 1914   | Layout 1 | `8ee02924e82e`  |
| 1908   | Layout 1 | `8ee02924e82e`  |
| 1897   | Layout 1 | `8ee02924e82e`  |
| 1892   | Layout 1 | `8ee02924e82e`  |
| 1886   | Layout 1 | `8ee02924e82e`  |
| 1881   | Layout 1 | `8ee02924e82e`  |
| 1871   | Layout 1 | `8ee02924e82e`  |
| 1866   | Layout 1 | `8ee02924e82e`  |
| 1862   | Layout 1 | `8ee02924e82e`  |
| 1854   | Layout 1 | `8ee02924e82e`  |
| 1846   | Layout 1 | `8ee02924e82e`  |
| 1838   | Layout 1 | `8ee02924e82e`  |
| 1832   | Layout 1 | `8ee02924e82e`  |
| 1826   | Layout 1 | `8ee02924e82e`  |
| 1822   | Layout 1 | `8ee02924e82e`  |
| 1818   | Layout 1 | `8ee02924e82e`  |
| 1804   | Layout 1 | `8ee02924e82e`  |
| 1794   | Layout 1 | `8ee02924e82e`  |
| 1790   | Layout 1 | `8ee02924e82e`  |
| 1784   | Layout 1 | `8ee02924e82e`  |
| 1774   | Layout 1 | `8ee02924e82e`  |
| 1771   | Layout 1 | `8ee02924e82e`  |
| 1762   | Layout 1 | `8ee02924e82e`  |
| 1759   | Layout 1 | `8ee02924e82e`  |
| 1754   | Layout 1 | `8ee02924e82e`  |
| 1749   | Layout 1 | `8ee02924e82e`  |
| 1743   | Layout 1 | `8ee02924e82e`  |
| 1737   | Layout 1 | `8ee02924e82e`  |
| 1731   | Layout 1 | `8ee02924e82e`  |
| 1725   | Layout 1 | `8ee02924e82e`  |
| 1717   | Layout 1 | `8ee02924e82e`  |
| 1710   | Layout 1 | `8ee02924e82e`  |
| 1704   | Layout 1 | `8ee02924e82e`  |
| 1698   | Layout 1 | `8ee02924e82e`  |
| 1690   | Layout 1 | `8ee02924e82e`  |
| 1685   | Layout 1 | `8ee02924e82e`  |
| 1680   | Layout 1 | `8ee02924e82e`  |
| 1674   | Layout 1 | `8ee02924e82e`  |
| 1668   | Layout 1 | `8ee02924e82e`  |
| 1659   | Layout 1 | `8ee02924e82e`  |
| 1649   | Layout 1 | `8ee02924e82e`  |
| 1642   | Layout 1 | `8ee02924e82e`  |
| 1636   | Layout 1 | `8ee02924e82e`  |
| 1628   | Layout 1 | `8ee02924e82e`  |
| 1622   | Layout 1 | `8ee02924e82e`  |
| 1614   | Layout 1 | `8ee02924e82e`  |
| 1608   | Layout 1 | `8ee02924e82e`  |
| 1602   | Layout 1 | `8ee02924e82e`  |
| 1598   | Layout 1 | `8ee02924e82e`  |
| 1594   | Layout 1 | `8ee02924e82e`  |
| 1590   | Layout 1 | `8ee02924e82e`  |
| 1587   | Layout 1 | `8ee02924e82e`  |
| 1584   | Layout 1 | `8ee02924e82e`  |
| 1579   | Layout 1 | `8ee02924e82e`  |
| 1572   | Layout 1 | `8ee02924e82e`  |
| 1565   | Layout 1 | `8ee02924e82e`  |
| 1559   | Layout 1 | `8ee02924e82e`  |
| 1554   | Layout 1 | `8ee02924e82e`  |
| 1547   | Layout 1 | `8ee02924e82e`  |
| 1537   | Layout 1 | `8ee02924e82e`  |
| 1529   | Layout 1 | `8ee02924e82e`  |
| 1524   | Layout 1 | `8ee02924e82e`  |
| 1519   | Layout 1 | `8ee02924e82e`  |
| 1509   | Layout 1 | `8ee02924e82e`  |
| 1506   | Layout 1 | `8ee02924e82e`  |
| 1504   | Layout 1 | `8ee02924e82e`  |
| 1500   | Layout 1 | `8ee02924e82e`  |
| 1493   | Layout 1 | `8ee02924e82e`  |
| 1489   | Layout 1 | `8ee02924e82e`  |
| 1485   | Layout 1 | `8ee02924e82e`  |
| 1481   | Layout 1 | `8ee02924e82e`  |
| 1474   | Layout 1 | `8ee02924e82e`  |
| 1466   | Layout 1 | `8ee02924e82e`  |
| 1462   | Layout 1 | `8ee02924e82e`  |
| 1459   | Layout 1 | `8ee02924e82e`  |
| 1453   | Layout 1 | `8ee02924e82e`  |
| 1450   | Layout 1 | `8ee02924e82e`  |
| 1445   | Layout 1 | `8ee02924e82e`  |
| 1439   | Layout 1 | `8ee02924e82e`  |
| 1433   | Layout 1 | `8ee02924e82e`  |
| 1430   | Layout 1 | `8ee02924e82e`  |
| 1426   | Layout 1 | `8ee02924e82e`  |
| 1421   | Layout 1 | `8ee02924e82e`  |
| 1417   | Layout 1 | `8ee02924e82e`  |
| 1416   | Layout 1 | `8ee02924e82e`  |
| 1409   | Layout 1 | `8ee02924e82e`  |
| 1405   | Layout 1 | `8ee02924e82e`  |
| 1401   | Layout 1 | `8ee02924e82e`  |
| 1396   | Layout 1 | `8ee02924e82e`  |
| 1391   | Layout 1 | `8ee02924e82e`  |
| 1390   | Layout 1 | `8ee02924e82e`  |
| 1386   | Layout 1 | `8ee02924e82e`  |
| 1381   | Layout 1 | `8ee02924e82e`  |
| 1379   | Layout 1 | `8ee02924e82e`  |
| 1372   | Layout 1 | `8ee02924e82e`  |
| 1366   | Layout 1 | `8ee02924e82e`  |
| 1364   | Layout 1 | `8ee02924e82e`  |
| 1363   | Layout 1 | `8ee02924e82e`  |
| 1360   | Layout 1 | `8ee02924e82e`  |
| 1358   | Layout 1 | `8ee02924e82e`  |
| 1355   | Layout 1 | `8ee02924e82e`  |
| 1351   | Layout 1 | `8ee02924e82e`  |
| 1348   | Layout 1 | `8ee02924e82e`  |
| 1346   | Layout 1 | `8ee02924e82e`  |
| 1341   | Layout 1 | `8ee02924e82e`  |
| 1340   | Layout 1 | `8ee02924e82e`  |
| 1338   | Layout 1 | `8ee02924e82e`  |
| 1335   | Layout 1 | `8ee02924e82e`  |
| 1333   | Layout 1 | `8ee02924e82e`  |
| 1329   | Layout 1 | `8ee02924e82e`  |
| 1327   | Layout 1 | `8ee02924e82e`  |
| 1324   | Layout 1 | `8ee02924e82e`  |
| 1321   | Layout 1 | `8ee02924e82e`  |
| 1319   | Layout 1 | `8ee02924e82e`  |
| 1318   | Layout 1 | `8ee02924e82e`  |
| 1316   | Layout 1 | `8ee02924e82e`  |
| 1313   | Layout 1 | `8ee02924e82e`  |
| 1311   | Layout 1 | `8ee02924e82e`  |
| 1309   | Layout 1 | `8ee02924e82e`  |
| 1304   | Layout 1 | `8ee02924e82e`  |
| 1292   | Layout 1 | `8ee02924e82e`  |
| 1286   | Layout 1 | `8ee02924e82e`  |
| 1280   | Layout 1 | `8ee02924e82e`  |
| 1276   | Layout 1 | `8ee02924e82e`  |
| 1267   | Layout 1 | `8ee02924e82e`  |
| 1261   | Layout 1 | `8ee02924e82e`  |
| 1256   | Layout 1 | `8ee02924e82e`  |
| 1250   | Layout 1 | `8ee02924e82e`  |
| 1246   | Layout 1 | `8ee02924e82e`  |
| 1239   | Layout 1 | `8ee02924e82e`  |
| 1230   | No file  | `8ee02924e82e`  |
| 1226   | No file  | `8ee02924e82e`  |
| 1220   | No file  | `8ee02924e82e`  |
| 1217   | No file  | `8ee02924e82e`  |
| 1211   | No file  | `8ee02924e82e`  |
| 1210   | No file  | `8ee02924e82e`  |
| 1208   | No file  | `8ee02924e82e`  |
| 1203   | No file  | `8ee02924e82e`  |
| 1197   | No file  | `8ee02924e82e`  |
| 1194   | No file  | `8ee02924e82e`  |
| 1192   | No file  | `8ee02924e82e`  |
| 1187   | No file  | `8ee02924e82e`  |
| 1183   | No file  | `8ee02924e82e`  |
| 1177   | No file  | `8ee02924e82e`  |
| 1173   | No file  | `8ee02924e82e`  |
| 1167   | No file  | `8ee02924e82e`  |
| 1164   | No file  | `8ee02924e82e`  |
| 1156   | No file  | `8ee02924e82e`  |
| 1149   | No file  | `8ee02924e82e`  |
| 1144   | No file  | `8ee02924e82e`  |
| 1137   | No file  | `8ee02924e82e`  |
| 1132   | No file  | `8ee02924e82e`  |
| 1127   | No file  | `8ee02924e82e`  |
| 1122   | No file  | `8ee02924e82e`  |
| 1118   | No file  | `8ee02924e82e`  |
| 1114   | No file  | `8ee02924e82e`  |
| 1109   | No file  | `8ee02924e82e`  |
| 1102   | No file  | `8ee02924e82e`  |
| 1096   | No file  | `8ee02924e82e`  |
| 1088   | No file  | `8ee02924e82e`  |
| 1081   | No file  | `8ee02924e82e`  |
| 1076   | No file  | `8ee02924e82e`  |
| 1069   | No file  | `8ee02924e82e`  |
| 1064   | No file  | `8ee02924e82e`  |
| 1058   | No file  | `8ee02924e82e`  |
| 1051   | No file  | `8ee02924e82e`  |
| 1044   | No file  | `8ee02924e82e`  |
| 1036   | No file  | `8ee02924e82e`  |
| 1026   | No file  | `8ee02924e82e`  |
| 1016   | No file  | `8ee02924e82e`  |
| 1009   | No file  | `8ee02924e82e`  |
| 1005   | No file  | `8ee02924e82e`  |
| 1000   | No file  | `8ee02924e82e`  |
| 998    | No file  | `8ee02924e82e`  |
| 990    | No file  | `8ee02924e82e`  |
| 979    | No file  | `8ee02924e82e`  |
| 972    | No file  | `8ee02924e82e`  |
| 963    | No file  | `8ee02924e82e`  |
| 955    | No file  | `8ee02924e82e`  |
| 946    | No file  | `8ee02924e82e`  |
| 938    | No file  | `8ee02924e82e`  |
| 927    | No file  | `8ee02924e82e`  |
| 911    | No file  | `8ee02924e82e`  |
| 904    | No file  | `8ee02924e82e`  |
| 899    | No file  | `8ee02924e82e`  |
| 894    | No file  | `8ee02924e82e`  |
| 885    | No file  | `8ee02924e82e`  |
| 879    | No file  | `8ee02924e82e`  |
| 872    | No file  | `8ee02924e82e`  |
| 864    | No file  | `8ee02924e82e`  |
| 855    | No file  | `8ee02924e82e`  |
| 853    | No file  | `8ee02924e82e`  |
| 845    | No file  | `8ee02924e82e`  |
| 837    | No file  | `8ee02924e82e`  |
| 829    | No file  | `8ee02924e82e`  |
| 822    | No file  | `8ee02924e82e`  |
| 814    | No file  | `8ee02924e82e`  |
| 805    | No file  | `8ee02924e82e`  |
| 794    | No file  | `8ee02924e82e`  |
| 787    | No file  | `8ee02924e82e`  |
| 780    | No file  | `8ee02924e82e`  |
| 771    | No file  | `8ee02924e82e`  |
| 760    | No file  | `8ee02924e82e`  |
| 748    | No file  | `8ee02924e82e`  |
| 741    | No file  | `8ee02924e82e`  |
| 736    | No file  | `8ee02924e82e`  |
| 731    | No file  | `8ee02924e82e`  |
| 723    | No file  | `8ee02924e82e`  |
| 711    | No file  | `8ee02924e82e`  |
| 707    | No file  | `8ee02924e82e`  |
| 697    | No file  | `8ee02924e82e`  |
| 689    | No file  | `8ee02924e82e`  |
| 683    | No file  | `8ee02924e82e`  |
| 678    | No file  | `8ee02924e82e`  |
| 670    | No file  | `8ee02924e82e`  |
| 661    | No file  | `8ee02924e82e`  |
| 656    | No file  | `8ee02924e82e`  |
| 652    | No file  | `8ee02924e82e`  |
| 643    | No file  | `8ee02924e82e`  |
| 637    | No file  | `8ee02924e82e`  |
| 630    | No file  | `8ee02924e82e`  |
| 627    | No file  | `8ee02924e82e`  |
| 621    | No file  | `8ee02924e82e`  |
| 617    | No file  | `8ee02924e82e`  |
| 615    | No file  | `8ee02924e82e`  |
| 606    | No file  | `8ee02924e82e`  |
| 599    | No file  | `8ee02924e82e`  |
| 592    | No file  | `8ee02924e82e`  |
| 586    | No file  | `8ee02924e82e`  |
| 577    | No file  | `8ee02924e82e`  |
| 569    | No file  | `8ee02924e82e`  |
| 561    | No file  | `8ee02924e82e`  |
| 554    | No file  | `8ee02924e82e`  |
| 542    | No file  | `8ee02924e82e`  |
| 532    | No file  | `8ee02924e82e`  |
| 531    | No file  | `8ee02924e82e`  |
| 526    | No file  | `8ee02924e82e`  |
| 521    | No file  | `8ee02924e82e`  |
| 517    | No file  | `8ee02924e82e`  |
| 510    | No file  | `8ee02924e82e`  |
| 508    | No file  | `8ee02924e82e`  |
| 504    | No file  | `8ee02924e82e`  |
| 497    | No file  | `8ee02924e82e`  |
| 491    | No file  | `8ee02924e82e`  |
| 485    | No file  | `8ee02924e82e`  |
| 478    | No file  | `8ee02924e82e`  |
| 472    | No file  | `8ee02924e82e`  |
| 466    | No file  | `8ee02924e82e`  |
| 457    | No file  | `8ee02924e82e`  |
| 452    | No file  | `8ee02924e82e`  |
| 449    | No file  | `8ee02924e82e`  |
| 435    | No file  | `8ee02924e82e`  |

<!-- versions:end -->

## Companion Files

None. The trade group type codes are the `trade_group_type` codes of
[`itemtradegrouptonpc.dbss`](itemtradegrouptonpc_dbss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

A PABR file with variable-size groups and an empty string table. 184 bytes on
client 3464.

| Offset              | Type               | Field        | Notes                                                  |
| ------------------- | ------------------ | ------------ | ------------------------------------------------------ |
| `+0x00`             | char[4]            | magic        | `PABR`                                                 |
| `+0x04`             | u32                | group_count  | Number of groups; `4` on client 3464                   |
| `+0x08`             | Group[group_count] | groups       | `group_count` groups, one per from group               |
| `groups+0x00`       | u32                | row_count    | Number of 12-byte rows; `5` on client 3464             |
| `groups+0x04`       | Row[row_count]     | rows         | `row_count` rows                                       |
| `rows+0x00`         | String Table       | string_table | See String Table                                       |
| `string_table+0x00` | u32                | table_start  | Offset of `string_count`; `0xAC` on client 3464        |
| `string_table+0x04` | u32                | zero         | `0`                                                    |

The last eight bytes are the PABR trailer that `_common/pabr_strings.py`
reads. The rows end where `table_start` points.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                    |
| ------- | ------------------ | ------------ | ---------------------------------------- |
| `+0x00` | u32                | string_count | `0`: the string table holds no strings   |
| `+0x04` | pstr[string_count] | strings      | Empty                                    |

### Group (variable: 5 bytes + pairs)

A group is `5 + 10 * pair_count` bytes.

| Offset  | Type             | Field      | Notes                                  |
| ------- | ---------------- | ---------- | -------------------------------------- |
| `+0x00` | u8               | from_group | Trade group type of the goods          |
| `+0x01` | u32              | pair_count | Number of pairs                        |
| `+0x05` | Pair[pair_count] | pairs      | `pair_count` pairs of 10 bytes         |

### Pair (10 bytes)

| Offset  | Type | Field      | Notes                                                        |
| ------- | ---- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u8   | from_group | Repeats the group's `from_group`                             |
| `+0x01` | u8   | to_group   | Trade group type of the buying trade NPC                     |
| `+0x02` | f32  | distance   | Distance the goods must travel; `700,000.0` on every pair on client 3464 |
| `+0x06` | u32  | add_rate   | Desert buff rate; `1,000,000` or `500,000` on client 3464    |

The bytes at `+0x02` are `00 E6 2A 49` on every pair, which is exactly
`700000.0` as an f32.

`distance` and `add_rate` are the sheet columns `MinDistance` and
`PriceRate` (Field Names). The Lua reads them through
`ToClient_TradeGroupFromToDistance` and
`ToClient_TradeGroupFromToAddPercent`.

### Row (12 bytes)

| Offset  | Type | Field                 | Notes                                       |
| ------- | ---- | --------------------- | ------------------------------------------- |
| `+0x00` | i64  | accumulated_advantage | Trade stock limit threshold; rises from `0` |
| `+0x08` | u32  | discount_rate         | Trade stock limit rate; falls from `1,000,000` |

On client 3464 the five rows are (`0`, `1,000,000`), (`4,500,000`,
`750,000`), (`9,000,000`, `500,000`), (`13,500,000`, `250,000`) and
(`18,000,000`, `180,000`). See Field Names.

## Trade Group Types

The client does not name the codes; no Lua enum or string key covers them.
[Trade Group Types](itemtradegrouptonpc_dbss.md#trade-group-types) in the
`itemtradegrouptonpc.dbss` doc lists the trade NPCs and goods that hold each
one. In short: `2` is the Valencia City trade managers, `3` the Ibellab Oasis
trade manager, `1` the other trade NPCs and the regional trade goods, `99`
the rest of the shared Fish Dad list (relics, fish, crates, trash loot).

LOC text places the NPCs: quest 5053 names "Yis Kunjamin of Capital
Valencia", item 8175 sends the player to "Burita Allon in Valencia City", and
quest 5801 names "Shuriar the trade manager at Ibellab Oasis".

### Pairs on Client 3464

| From | To | Distance | Desert Buff Rate |
| ---- | -- | -------- | ---------------- |
| 1    | 2  | 700,000  | 1,000,000        |
| 1    | 3  | 700,000  | 1,000,000        |
| 2    | 1  | 700,000  | 1,000,000        |
| 3    | 1  | 700,000  | 1,000,000        |
| 2    | 99 | 700,000  | 500,000          |
| 3    | 99 | 700,000  | 500,000          |
| 99   | 2  | 700,000  | 500,000          |
| 99   | 3  | 700,000  | 500,000          |

Every pair links Valencia City or Ibellab Oasis with the rest of the world;
no pair links 2 and 3, and none links 1 and 99. The matrix is symmetric, so
this client's data cannot tell which of the two bytes is the goods' group;
I follow the Lua's argument order (goods first, NPC second) in the names.

## Field Names

The file is two sheets of a private server on client 1784,
`TradeGroupPriceTable` (the pairs) and `TradeAdvantageTable` (the rows).
That server's dump (`Instance_dumpFull.exe`) loads both into one manager and
has no reader for the client file, so the names rest on the struct order of
its two sheet loaders and on the data.

| Field                   | Struct member | Sheet column           |
| ----------------------- | ------------- | ---------------------- |
| Pair `from_group`       | u8 `+0`       | `FromTradeGroup`       |
| Pair `to_group`         | u8 `+1`       | `ToTradeGroup`         |
| Pair `distance`         | f32 `+4`      | `MinDistance`          |
| Pair `add_rate`         | u32 `+8`      | `PriceRate`            |
| `accumulated_advantage` | i64 `+0`      | `AccumulatedAdvantage` |
| `discount_rate`         | u32 `+8`      | `DiscountRate`         |

The pair loader (from VA `0x1408b80d6`) reads `MinDistance` as an integer
and converts it to f32, and keys the pairs by `FromTradeGroup`, which is why
the file groups them by `from_group`. It logs "무역 그룹 인덱스틑 1부터
사용해야합니다" ("trade group indices must start from 1") for a group of `0`.
The row loader (from VA `0x1408b8b66`) reads `AccumulatedAdvantage` as a
signed value into an 8-byte member, and its check (VA `0x140b82bd0`) rejects
a `DiscountRate` above 1,000,000 with "무역 재고량 제한 비율이 잘못
되었습니다" ("the trade stock quantity limit rate is wrong") and a negative
`AccumulatedAdvantage` with "무역 재고량 제한 기준이 음수가 될 수는
없습니다" ("the trade stock quantity limit threshold cannot be negative").

That private server's own `itemtradeetc.bss` holds the 8 sheet pairs and
the 5 sheet rows with equal values, and it is byte-identical to the client
3474 file.

## Notes

- `panel_dialog_trade_mybasket_all_1.luac` (the trade sell list) is the only
  client Lua that reads these values. Per item it calls
  `ToClient_TradeGroupFromToAddPercent(tradeItemWrapper:getTradeGroupType(),
  characterStaticStatus:getTradeGroupType())` and
  `ToClient_TradeGroupFromToDistance(...)` with the same two arguments: the
  trade item's group type and the trade NPC's. It shows the `Desert Buff
  Applied` icon (`LUA_TRADEMARKET_DESERTBUFF`) when the player's
  `getSellTradeItemPricePercent()` is above `0`, the add percent is above
  `100` and the item's travel distance (`getFromToDistanceTradeShop()`) is at
  least the pair's distance.
- The client's own text matches the pairs: knowledge 9239 (Token of Desert
  Trading) says validated trade goods trade "exclusively at Valencia City"
  and only for goods carried a long distance through the desert, and a
  dialog line (LOC type 39, 110639) reads "You can sell trade goods from
  other regions for a higher price in Valencia City and Ibellab Oasis.
  However, you must cross the great desert in order to get there." Dialog
  116155 requires Trading Artisan 2 and the quest `To the Wild Desert!` for
  the desert trade buff.
- The third-party project calpheonlabs reads `+0x02` as a zero byte followed
  by a 3-byte marker `E6 2A 49`; the f32 reading covers the same four bytes.

## Open Questions

### What Scale add_rate and distance Use

The Lua compares the add percent with `100`, but the file stores `1,000,000`
and `500,000`, both far above it, so the native getter converts the value.
Elsewhere in the same Lua `_CONST_CALCULATE_PERCENT_VALUE` is `10000`, which
makes `1,000,000` read as 100% and `500,000` as 50%; whether that is the
price added to the sale or something else is open. The unit of the `700,000`
distance against `getFromToDistanceTradeShop()` is open too.

### Where the NPC's Trade Group Type Comes From

The Lua reads the NPC's code from `characterStaticStatus:getTradeGroupType()`.
In `itemtradegrouptonpc.dbss` the one-item group of each trade NPC carries
the NPC's code (`2` for the Valencia City managers), but whether the client
takes it from there or from a field of `characterstatic.dbss` is open.

## In-Game Checks

### Big Hand Stock Rate

Needs zone: Valencia City or Port Ratt (limited trade goods)

The server calls the rows the trade stock quantity limit (Field Names),
which fits the Big Hand rule of `panel_dialog_trade_function_all.xml`
(`PANEL_TRADEMARKETBUYLIST_DESC`): a player who buys limited trade goods
past a set amount in a day is offered less stock. This checks that
`accumulated_advantage` is that day's purchase total in silver and
`discount_rate` the stock rate.

1. Buy limited trade goods for more than 4,500,000 silver in one day.
2. Watch the stock the trade manager offers as the total passes 4,500,000
   and 9,000,000.

Expected: the stock drops to three quarters past 4,500,000 and to half past
9,000,000.

### Desert Buff Rate

Needs NPC (any one):

- [Yis Kunjamin](https://bdocodex.com/us/npc/45011/)
- [Burita Allon](https://bdocodex.com/us/npc/45012/)

Needs quest: To the Wild Desert!

With the desert trade buff, sell a Calpheon trade good (group `1`, rate
`1,000,000`) at Valencia City and note the price with and without the
`Desert Buff Applied` icon. A doubled price means `1,000,000` adds 100%; a
50% rise means the rate is applied another way.
