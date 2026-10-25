# `jewelgroupstaticstatus.bss` Format

## Purpose

The crystal groups: one fixed row per group with its group number, the most
crystals of that group a crystal preset may hold, and its Korean name. A
crystal names its group in the last two bytes of its
[`itemenchant.dbss`](itemenchant_dbss.md) block. LOC type 121 names each
group under its group number and limit.
[`jewelspecialslotsgroupstaticstatus.bss`](jewelspecialslotsgroupstaticstatus_bss.md)
lists the groups each special preset slot accepts.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes | Records      | Row bytes |
| ------ | -------------- | ---------------------------- | ----- | ------------ | --------- |
| 1      | 2098 and later | `jewelgroupstaticstatus.bss` | 980   | 42 Group Row | 8         |

| Layout | File                         | Known          | Unknown    |
| ------ | ---------------------------- | -------------- | ---------- |
| 1      | `jewelgroupstaticstatus.bss` | 980 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `8c2be0aab762`  |
| 3482   | Layout 1             | `8c2be0aab762`  |
| 3474   | Layout 1             | `8c2be0aab762`  |
| 3473   | Layout 1             | `8c2be0aab762`  |
| 3464   | Layout 1             | `8c2be0aab762`  |
| 3458   | Layout 1             | `8c2be0aab762`  |
| 3454   | Layout 1             | `8c2be0aab762`  |
| 3444   | Layout 1             | `8c2be0aab762`  |
| 3435   | Layout 1             | `8c2be0aab762`  |
| 3426   | Layout 1             | `8c2be0aab762`  |
| 3418   | Layout 1             | `8c2be0aab762`  |
| 3412   | Layout 1             | `8c2be0aab762`  |
| 3402   | Layout 1             | `8c2be0aab762`  |
| 3396   | Layout 1             | `8c2be0aab762`  |
| 3387   | Layout 1             | `8c2be0aab762`  |
| 3381   | Layout 1             | `8c2be0aab762`  |
| 3373   | Layout 1             | `8c2be0aab762`  |
| 3364   | Layout 1             | `8c2be0aab762`  |
| 3356   | Layout 1             | `8c2be0aab762`  |
| 3349   | Layout 1             | `8c2be0aab762`  |
| 3342   | Layout 1             | `8c2be0aab762`  |
| 3335   | Layout 1             | `8c2be0aab762`  |
| 3326   | Layout 1             | `8c2be0aab762`  |
| 3321   | Layout 1             | `8c2be0aab762`  |
| 3314   | Layout 1             | `8c2be0aab762`  |
| 3303   | Layout 1             | `8c2be0aab762`  |
| 3302   | Layout 1             | `8c2be0aab762`  |
| 3293   | Layout 1             | `8c2be0aab762`  |
| 3283   | Layout 1             | `8c2be0aab762`  |
| 3275   | Layout 1             | `8c2be0aab762`  |
| 3267   | Layout 1             | `8c2be0aab762`  |
| 3258   | Layout 1             | `8c2be0aab762`  |
| 3251   | Layout 1             | `8c2be0aab762`  |
| 3242   | Layout 1             | `8c2be0aab762`  |
| 3235   | Layout 1             | `8c2be0aab762`  |
| 3229   | Layout 1             | `8c2be0aab762`  |
| 3212   | Layout 1             | `8c2be0aab762`  |
| 3203   | Layout 1             | `8c2be0aab762`  |
| 3193   | Layout 1             | `8c2be0aab762`  |
| 3186   | Layout 1             | `8c2be0aab762`  |
| 3177   | Layout 1             | `8c2be0aab762`  |
| 3169   | Layout 1             | `8c2be0aab762`  |
| 3158   | Layout 1             | `8c2be0aab762`  |
| 3151   | Layout 1             | `8c2be0aab762`  |
| 3144   | Layout 1             | `8c2be0aab762`  |
| 3133   | Layout 1             | `8c2be0aab762`  |
| 3125   | Layout 1             | `8c2be0aab762`  |
| 3118   | Layout 1             | `8c2be0aab762`  |
| 3111   | Layout 1             | `8c2be0aab762`  |
| 3103   | Layout 1             | `8c2be0aab762`  |
| 3095   | Layout 1             | `8c2be0aab762`  |
| 3086   | Layout 1             | `8c2be0aab762`  |
| 3072   | Layout 1             | `8c2be0aab762`  |
| 3062   | Layout 1             | `8c2be0aab762`  |
| 3052   | Layout 1             | `8c2be0aab762`  |
| 3045   | Layout 1             | `8c2be0aab762`  |
| 3037   | Layout 1             | `8c2be0aab762`  |
| 3030   | Layout 1             | `8c2be0aab762`  |
| 3021   | Layout 1             | `8c2be0aab762`  |
| 3012   | Layout 1             | `8c2be0aab762`  |
| 3002   | Layout 1             | `8c2be0aab762`  |
| 2995   | Layout 1             | `8c2be0aab762`  |
| 2987   | Layout 1             | `8c2be0aab762`  |
| 2978   | Layout 1             | `8c2be0aab762`  |
| 2970   | Layout 1             | `8c2be0aab762`  |
| 2959   | Layout 1             | `8c2be0aab762`  |
| 2951   | Layout 1             | `8c2be0aab762`  |
| 2942   | Layout 1             | `8c2be0aab762`  |
| 2935   | Layout 1             | `8c2be0aab762`  |
| 2932   | Layout 1             | `8c2be0aab762`  |
| 2923   | Layout 1             | `8c2be0aab762`  |
| 2919   | Layout 1             | `8c2be0aab762`  |
| 2907   | Layout 1             | `8c2be0aab762`  |
| 2900   | Layout 1             | `8c2be0aab762`  |
| 2891   | Layout 1             | `8c2be0aab762`  |
| 2882   | Layout 1             | `8c2be0aab762`  |
| 2872   | Layout 1             | `8c2be0aab762`  |
| 2863   | Layout 1             | `8c2be0aab762`  |
| 2855   | Layout 1             | `8c2be0aab762`  |
| 2849   | Layout 1             | `8c2be0aab762`  |
| 2844   | Layout 1             | `8c2be0aab762`  |
| 2834   | Layout 1             | `8c2be0aab762`  |
| 2825   | Layout 1             | `8c2be0aab762`  |
| 2819   | Layout 1             | `8c2be0aab762`  |
| 2811   | Layout 1             | `8c2be0aab762`  |
| 2803   | Layout 1             | `8c2be0aab762`  |
| 2794   | Layout 1             | `8c2be0aab762`  |
| 2783   | Layout 1             | `8c2be0aab762`  |
| 2774   | Layout 1             | `8c2be0aab762`  |
| 2765   | Layout 1             | `8c2be0aab762`  |
| 2756   | Layout 1             | `8c2be0aab762`  |
| 2750   | Layout 1             | `8c2be0aab762`  |
| 2743   | Layout 1             | `8c2be0aab762`  |
| 2736   | Layout 1             | `8c2be0aab762`  |
| 2726   | Layout 1             | `8c2be0aab762`  |
| 2717   | Layout 1             | `8c2be0aab762`  |
| 2709   | Layout 1             | `8c2be0aab762`  |
| 2703   | Layout 1             | `8c2be0aab762`  |
| 2695   | Layout 1             | `8c2be0aab762`  |
| 2684   | Layout 1             | `8c2be0aab762`  |
| 2672   | Layout 1             | `8c2be0aab762`  |
| 2665   | Layout 1             | `8c2be0aab762`  |
| 2657   | Layout 1             | `8c2be0aab762`  |
| 2649   | Layout 1             | `8c2be0aab762`  |
| 2644   | Layout 1             | `8c2be0aab762`  |
| 2637   | Layout 1             | `8c2be0aab762`  |
| 2629   | Layout 1             | `8c2be0aab762`  |
| 2619   | Layout 1             | `8c2be0aab762`  |
| 2612   | Layout 1             | `8c2be0aab762`  |
| 2606   | Layout 1             | `8c2be0aab762`  |
| 2602   | Layout 1             | `8c2be0aab762`  |
| 2601   | Layout 1             | `8c2be0aab762`  |
| 2592   | Layout 1             | `8c2be0aab762`  |
| 2583   | Layout 1             | `8c2be0aab762`  |
| 2575   | Layout 1             | `8c2be0aab762`  |
| 2567   | Layout 1             | `8c2be0aab762`  |
| 2560   | Layout 1             | `8c2be0aab762`  |
| 2553   | Layout 1             | `8c2be0aab762`  |
| 2545   | Layout 1             | `8c2be0aab762`  |
| 2538   | Layout 1             | `8c2be0aab762`  |
| 2529   | Layout 1             | `8c2be0aab762`  |
| 2519   | Layout 1             | `8c2be0aab762`  |
| 2513   | Layout 1             | `8c2be0aab762`  |
| 2510   | Layout 1             | `8c2be0aab762`  |
| 2507   | Layout 1             | `8c2be0aab762`  |
| 2503   | Layout 1             | `8c2be0aab762`  |
| 2498   | Layout 1             | `8c2be0aab762`  |
| 2492   | Layout 1             | `8c2be0aab762`  |
| 2487   | Layout 1             | `8c2be0aab762`  |
| 2480   | Layout 1             | `8c2be0aab762`  |
| 2474   | Layout 1             | `8c2be0aab762`  |
| 2468   | Layout 1             | `8c2be0aab762`  |
| 2460   | Layout 1             | `8c2be0aab762`  |
| 2453   | Layout 1             | `8c2be0aab762`  |
| 2444   | Layout 1             | `8c2be0aab762`  |
| 2438   | Layout 1             | `8c2be0aab762`  |
| 2434   | Layout 1             | `8c2be0aab762`  |
| 2429   | Layout 1             | `8c2be0aab762`  |
| 2421   | Layout 1             | `8c2be0aab762`  |
| 2414   | Layout 1             | `8c2be0aab762`  |
| 2407   | Layout 1             | `8c2be0aab762`  |
| 2401   | Layout 1             | `8c2be0aab762`  |
| 2397   | Layout 1             | `8c2be0aab762`  |
| 2393   | Layout 1             | `8c2be0aab762`  |
| 2384   | Layout 1             | `8c2be0aab762`  |
| 2378   | Layout 1             | `8c2be0aab762`  |
| 2372   | Layout 1             | `8c2be0aab762`  |
| 2358   | Layout 1             | `8c2be0aab762`  |
| 2352   | Layout 1             | `8c2be0aab762`  |
| 2347   | Layout 1             | `8c2be0aab762`  |
| 2343   | Layout 1             | `8c2be0aab762`  |
| 2335   | Layout 1             | `8c2be0aab762`  |
| 2327   | Layout 1             | `8c2be0aab762`  |
| 2324   | Layout 1             | `8c2be0aab762`  |
| 2319   | Layout 1             | `8c2be0aab762`  |
| 2313   | Layout 1             | `8c2be0aab762`  |
| 2308   | Layout 1             | `8c2be0aab762`  |
| 2302   | Layout 1             | `8c2be0aab762`  |
| 2295   | Layout 1             | `8c2be0aab762`  |
| 2290   | Layout 1             | `8c2be0aab762`  |
| 2284   | Layout 1             | `8c2be0aab762`  |
| 2276   | Layout 1             | `8c2be0aab762`  |
| 2269   | Layout 1             | `8c2be0aab762`  |
| 2259   | Layout 1             | `8c2be0aab762`  |
| 2250   | Layout 1             | `8c2be0aab762`  |
| 2243   | Layout 1             | `8c2be0aab762`  |
| 2235   | Layout 1             | `8c2be0aab762`  |
| 2229   | Layout 1             | `8c2be0aab762`  |
| 2224   | Layout 1             | `8c2be0aab762`  |
| 2218   | Layout 1             | `8c2be0aab762`  |
| 2215   | Layout 1             | `8c2be0aab762`  |
| 2207   | Layout 1             | `8c2be0aab762`  |
| 2203   | Layout 1             | `8c2be0aab762`  |
| 2196   | Layout 1             | `8c2be0aab762`  |
| 2192   | Layout 1             | `8c2be0aab762`  |
| 2189   | Layout 1             | `8c2be0aab762`  |
| 2183   | Layout 1             | `8c2be0aab762`  |
| 2179   | Layout 1             | `8c2be0aab762`  |
| 2171   | Layout 1             | `8c2be0aab762`  |
| 2163   | Layout 1             | `8c2be0aab762`  |
| 2156   | Layout 1             | `8c2be0aab762`  |
| 2151   | Layout 1             | `8c2be0aab762`  |
| 2147   | Layout 1             | `8c2be0aab762`  |
| 2142   | Layout 1             | `8c2be0aab762`  |
| 2138   | Layout 1             | `8c2be0aab762`  |
| 2134   | Layout 1             | `8c2be0aab762`  |
| 2130   | Layout 1             | `8c2be0aab762`  |
| 2122   | Layout 1             | `8c2be0aab762`  |
| 2107   | Layout 1             | `8c2be0aab762`  |
| 2098   | Layout 1             | `8c2be0aab762`  |
| 2089   | No documented layout | `8c2be0aab762`  |
| 2081   | No file              | `8c2be0aab762`  |
| 2073   | No file              | `8c2be0aab762`  |
| 2067   | No file              | `8c2be0aab762`  |
| 2063   | No file              | `8c2be0aab762`  |
| 2059   | No file              | `8c2be0aab762`  |
| 2052   | No file              | `8c2be0aab762`  |
| 2044   | No file              | `8c2be0aab762`  |
| 2039   | No file              | `8c2be0aab762`  |
| 2032   | No file              | `8c2be0aab762`  |
| 2025   | No file              | `8c2be0aab762`  |
| 2011   | No file              | `8c2be0aab762`  |
| 2005   | No file              | `8c2be0aab762`  |
| 2000   | No file              | `8c2be0aab762`  |
| 1996   | No file              | `8c2be0aab762`  |
| 1991   | No file              | `8c2be0aab762`  |
| 1985   | No file              | `8c2be0aab762`  |
| 1980   | No file              | `8c2be0aab762`  |
| 1969   | No file              | `8c2be0aab762`  |
| 1964   | No file              | `8c2be0aab762`  |
| 1958   | No file              | `8c2be0aab762`  |
| 1950   | No file              | `8c2be0aab762`  |
| 1945   | No file              | `8c2be0aab762`  |
| 1937   | No file              | `8c2be0aab762`  |
| 1933   | No file              | `8c2be0aab762`  |
| 1927   | No file              | `8c2be0aab762`  |
| 1921   | No file              | `8c2be0aab762`  |
| 1914   | No file              | `8c2be0aab762`  |
| 1908   | No file              | `8c2be0aab762`  |
| 1897   | No file              | `8c2be0aab762`  |
| 1892   | No file              | `8c2be0aab762`  |
| 1886   | No file              | `8c2be0aab762`  |
| 1881   | No file              | `8c2be0aab762`  |
| 1871   | No file              | `8c2be0aab762`  |
| 1866   | No file              | `8c2be0aab762`  |
| 1862   | No file              | `8c2be0aab762`  |
| 1854   | No file              | `8c2be0aab762`  |
| 1846   | No file              | `8c2be0aab762`  |
| 1838   | No file              | `8c2be0aab762`  |
| 1832   | No file              | `8c2be0aab762`  |
| 1826   | No file              | `8c2be0aab762`  |
| 1822   | No file              | `8c2be0aab762`  |
| 1818   | No file              | `8c2be0aab762`  |
| 1804   | No file              | `8c2be0aab762`  |
| 1794   | No file              | `8c2be0aab762`  |
| 1790   | No file              | `8c2be0aab762`  |
| 1784   | No file              | `8c2be0aab762`  |
| 1774   | No file              | `8c2be0aab762`  |
| 1771   | No file              | `8c2be0aab762`  |
| 1762   | No file              | `8c2be0aab762`  |
| 1759   | No file              | `8c2be0aab762`  |
| 1754   | No file              | `8c2be0aab762`  |
| 1749   | No file              | `8c2be0aab762`  |
| 1743   | No file              | `8c2be0aab762`  |
| 1737   | No file              | `8c2be0aab762`  |
| 1731   | No file              | `8c2be0aab762`  |
| 1725   | No file              | `8c2be0aab762`  |
| 1717   | No file              | `8c2be0aab762`  |
| 1710   | No file              | `8c2be0aab762`  |
| 1704   | No file              | `8c2be0aab762`  |
| 1698   | No file              | `8c2be0aab762`  |
| 1690   | No file              | `8c2be0aab762`  |
| 1685   | No file              | `8c2be0aab762`  |
| 1680   | No file              | `8c2be0aab762`  |
| 1674   | No file              | `8c2be0aab762`  |
| 1668   | No file              | `8c2be0aab762`  |
| 1659   | No file              | `8c2be0aab762`  |
| 1649   | No file              | `8c2be0aab762`  |
| 1642   | No file              | `8c2be0aab762`  |
| 1636   | No file              | `8c2be0aab762`  |
| 1628   | No file              | `8c2be0aab762`  |
| 1622   | No file              | `8c2be0aab762`  |
| 1614   | No file              | `8c2be0aab762`  |
| 1608   | No file              | `8c2be0aab762`  |
| 1602   | No file              | `8c2be0aab762`  |
| 1598   | No file              | `8c2be0aab762`  |
| 1594   | No file              | `8c2be0aab762`  |
| 1590   | No file              | `8c2be0aab762`  |
| 1587   | No file              | `8c2be0aab762`  |
| 1584   | No file              | `8c2be0aab762`  |
| 1579   | No file              | `8c2be0aab762`  |
| 1572   | No file              | `8c2be0aab762`  |
| 1565   | No file              | `8c2be0aab762`  |
| 1559   | No file              | `8c2be0aab762`  |
| 1554   | No file              | `8c2be0aab762`  |
| 1547   | No file              | `8c2be0aab762`  |
| 1537   | No file              | `8c2be0aab762`  |
| 1529   | No file              | `8c2be0aab762`  |
| 1524   | No file              | `8c2be0aab762`  |
| 1519   | No file              | `8c2be0aab762`  |
| 1509   | No file              | `8c2be0aab762`  |
| 1506   | No file              | `8c2be0aab762`  |
| 1504   | No file              | `8c2be0aab762`  |
| 1500   | No file              | `8c2be0aab762`  |
| 1493   | No file              | `8c2be0aab762`  |
| 1489   | No file              | `8c2be0aab762`  |
| 1485   | No file              | `8c2be0aab762`  |
| 1481   | No file              | `8c2be0aab762`  |
| 1474   | No file              | `8c2be0aab762`  |
| 1466   | No file              | `8c2be0aab762`  |
| 1462   | No file              | `8c2be0aab762`  |
| 1459   | No file              | `8c2be0aab762`  |
| 1453   | No file              | `8c2be0aab762`  |
| 1450   | No file              | `8c2be0aab762`  |
| 1445   | No file              | `8c2be0aab762`  |
| 1439   | No file              | `8c2be0aab762`  |
| 1433   | No file              | `8c2be0aab762`  |
| 1430   | No file              | `8c2be0aab762`  |
| 1426   | No file              | `8c2be0aab762`  |
| 1421   | No file              | `8c2be0aab762`  |
| 1417   | No file              | `8c2be0aab762`  |
| 1416   | No file              | `8c2be0aab762`  |
| 1409   | No file              | `8c2be0aab762`  |
| 1405   | No file              | `8c2be0aab762`  |
| 1401   | No file              | `8c2be0aab762`  |
| 1396   | No file              | `8c2be0aab762`  |
| 1391   | No file              | `8c2be0aab762`  |
| 1390   | No file              | `8c2be0aab762`  |
| 1386   | No file              | `8c2be0aab762`  |
| 1381   | No file              | `8c2be0aab762`  |
| 1379   | No file              | `8c2be0aab762`  |
| 1372   | No file              | `8c2be0aab762`  |
| 1366   | No file              | `8c2be0aab762`  |
| 1364   | No file              | `8c2be0aab762`  |
| 1363   | No file              | `8c2be0aab762`  |
| 1360   | No file              | `8c2be0aab762`  |
| 1358   | No file              | `8c2be0aab762`  |
| 1355   | No file              | `8c2be0aab762`  |
| 1351   | No file              | `8c2be0aab762`  |
| 1348   | No file              | `8c2be0aab762`  |
| 1346   | No file              | `8c2be0aab762`  |
| 1341   | No file              | `8c2be0aab762`  |
| 1340   | No file              | `8c2be0aab762`  |
| 1338   | No file              | `8c2be0aab762`  |
| 1335   | No file              | `8c2be0aab762`  |
| 1333   | No file              | `8c2be0aab762`  |
| 1329   | No file              | `8c2be0aab762`  |
| 1327   | No file              | `8c2be0aab762`  |
| 1324   | No file              | `8c2be0aab762`  |
| 1321   | No file              | `8c2be0aab762`  |
| 1319   | No file              | `8c2be0aab762`  |
| 1318   | No file              | `8c2be0aab762`  |
| 1316   | No file              | `8c2be0aab762`  |
| 1313   | No file              | `8c2be0aab762`  |
| 1311   | No file              | `8c2be0aab762`  |
| 1309   | No file              | `8c2be0aab762`  |
| 1304   | No file              | `8c2be0aab762`  |
| 1292   | No file              | `8c2be0aab762`  |
| 1286   | No file              | `8c2be0aab762`  |
| 1280   | No file              | `8c2be0aab762`  |
| 1276   | No file              | `8c2be0aab762`  |
| 1267   | No file              | `8c2be0aab762`  |
| 1261   | No file              | `8c2be0aab762`  |
| 1256   | No file              | `8c2be0aab762`  |
| 1250   | No file              | `8c2be0aab762`  |
| 1246   | No file              | `8c2be0aab762`  |
| 1239   | No file              | `8c2be0aab762`  |
| 1230   | No file              | `8c2be0aab762`  |
| 1226   | No file              | `8c2be0aab762`  |
| 1220   | No file              | `8c2be0aab762`  |
| 1217   | No file              | `8c2be0aab762`  |
| 1211   | No file              | `8c2be0aab762`  |
| 1210   | No file              | `8c2be0aab762`  |
| 1208   | No file              | `8c2be0aab762`  |
| 1203   | No file              | `8c2be0aab762`  |
| 1197   | No file              | `8c2be0aab762`  |
| 1194   | No file              | `8c2be0aab762`  |
| 1192   | No file              | `8c2be0aab762`  |
| 1187   | No file              | `8c2be0aab762`  |
| 1183   | No file              | `8c2be0aab762`  |
| 1177   | No file              | `8c2be0aab762`  |
| 1173   | No file              | `8c2be0aab762`  |
| 1167   | No file              | `8c2be0aab762`  |
| 1164   | No file              | `8c2be0aab762`  |
| 1156   | No file              | `8c2be0aab762`  |
| 1149   | No file              | `8c2be0aab762`  |
| 1144   | No file              | `8c2be0aab762`  |
| 1137   | No file              | `8c2be0aab762`  |
| 1132   | No file              | `8c2be0aab762`  |
| 1127   | No file              | `8c2be0aab762`  |
| 1122   | No file              | `8c2be0aab762`  |
| 1118   | No file              | `8c2be0aab762`  |
| 1114   | No file              | `8c2be0aab762`  |
| 1109   | No file              | `8c2be0aab762`  |
| 1102   | No file              | `8c2be0aab762`  |
| 1096   | No file              | `8c2be0aab762`  |
| 1088   | No file              | `8c2be0aab762`  |
| 1081   | No file              | `8c2be0aab762`  |
| 1076   | No file              | `8c2be0aab762`  |
| 1069   | No file              | `8c2be0aab762`  |
| 1064   | No file              | `8c2be0aab762`  |
| 1058   | No file              | `8c2be0aab762`  |
| 1051   | No file              | `8c2be0aab762`  |
| 1044   | No file              | `8c2be0aab762`  |
| 1036   | No file              | `8c2be0aab762`  |
| 1026   | No file              | `8c2be0aab762`  |
| 1016   | No file              | `8c2be0aab762`  |
| 1009   | No file              | `8c2be0aab762`  |
| 1005   | No file              | `8c2be0aab762`  |
| 1000   | No file              | `8c2be0aab762`  |
| 998    | No file              | `8c2be0aab762`  |
| 990    | No file              | `8c2be0aab762`  |
| 979    | No file              | `8c2be0aab762`  |
| 972    | No file              | `8c2be0aab762`  |
| 963    | No file              | `8c2be0aab762`  |
| 955    | No file              | `8c2be0aab762`  |
| 946    | No file              | `8c2be0aab762`  |
| 938    | No file              | `8c2be0aab762`  |
| 927    | No file              | `8c2be0aab762`  |
| 911    | No file              | `8c2be0aab762`  |
| 904    | No file              | `8c2be0aab762`  |
| 899    | No file              | `8c2be0aab762`  |
| 894    | No file              | `8c2be0aab762`  |
| 885    | No file              | `8c2be0aab762`  |
| 879    | No file              | `8c2be0aab762`  |
| 872    | No file              | `8c2be0aab762`  |
| 864    | No file              | `8c2be0aab762`  |
| 855    | No file              | `8c2be0aab762`  |
| 853    | No file              | `8c2be0aab762`  |
| 845    | No file              | `8c2be0aab762`  |
| 837    | No file              | `8c2be0aab762`  |
| 829    | No file              | `8c2be0aab762`  |
| 822    | No file              | `8c2be0aab762`  |
| 814    | No file              | `8c2be0aab762`  |
| 805    | No file              | `8c2be0aab762`  |
| 794    | No file              | `8c2be0aab762`  |
| 787    | No file              | `8c2be0aab762`  |
| 780    | No file              | `8c2be0aab762`  |
| 771    | No file              | `8c2be0aab762`  |
| 760    | No file              | `8c2be0aab762`  |
| 748    | No file              | `8c2be0aab762`  |
| 741    | No file              | `8c2be0aab762`  |
| 736    | No file              | `8c2be0aab762`  |
| 731    | No file              | `8c2be0aab762`  |
| 723    | No file              | `8c2be0aab762`  |
| 711    | No file              | `8c2be0aab762`  |
| 707    | No file              | `8c2be0aab762`  |
| 697    | No file              | `8c2be0aab762`  |
| 689    | No file              | `8c2be0aab762`  |
| 683    | No file              | `8c2be0aab762`  |
| 678    | No file              | `8c2be0aab762`  |
| 670    | No file              | `8c2be0aab762`  |
| 661    | No file              | `8c2be0aab762`  |
| 656    | No file              | `8c2be0aab762`  |
| 652    | No file              | `8c2be0aab762`  |
| 643    | No file              | `8c2be0aab762`  |
| 637    | No file              | `8c2be0aab762`  |
| 630    | No file              | `8c2be0aab762`  |
| 627    | No file              | `8c2be0aab762`  |
| 621    | No file              | `8c2be0aab762`  |
| 617    | No file              | `8c2be0aab762`  |
| 615    | No file              | `8c2be0aab762`  |
| 606    | No file              | `8c2be0aab762`  |
| 599    | No file              | `8c2be0aab762`  |
| 592    | No file              | `8c2be0aab762`  |
| 586    | No file              | `8c2be0aab762`  |
| 577    | No file              | `8c2be0aab762`  |
| 569    | No file              | `8c2be0aab762`  |
| 561    | No file              | `8c2be0aab762`  |
| 554    | No file              | `8c2be0aab762`  |
| 542    | No file              | `8c2be0aab762`  |
| 532    | No file              | `8c2be0aab762`  |
| 531    | No file              | `8c2be0aab762`  |
| 526    | No file              | `8c2be0aab762`  |
| 521    | No file              | `8c2be0aab762`  |
| 517    | No file              | `8c2be0aab762`  |
| 510    | No file              | `8c2be0aab762`  |
| 508    | No file              | `8c2be0aab762`  |
| 504    | No file              | `8c2be0aab762`  |
| 497    | No file              | `8c2be0aab762`  |
| 491    | No file              | `8c2be0aab762`  |
| 485    | No file              | `8c2be0aab762`  |
| 478    | No file              | `8c2be0aab762`  |
| 472    | No file              | `8c2be0aab762`  |
| 466    | No file              | `8c2be0aab762`  |
| 457    | No file              | `8c2be0aab762`  |
| 452    | No file              | `8c2be0aab762`  |
| 449    | No file              | `8c2be0aab762`  |
| 435    | No file              | `8c2be0aab762`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                   |
| --------------------- | -------- | ---------------------- |
| `languagedata_en.loc` | Optional | Group names (type 121) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR block of fixed 8-byte rows, followed by the same counted string table
and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). On client 3473 the string table holds 42 wide
strings, one Korean group name per row.

| Offset              | Type             | Field              | Notes                            |
| ------------------- | ---------------- | ------------------ | -------------------------------- |
| `+0x00`             | char[4]          | magic              | ASCII `PABR`                     |
| `+0x04`             | u32              | count              | Number of rows; 42 on client 3473 |
| `+0x08`             | Group Row[count] | rows               | See Group Row                    |
| `rows+0x00`         | String Table     | string_table       | One Korean name per row          |
| `string_table+0x00` | u32              | string_table_start | Where the rows end               |
| `string_table+0x04` | u32              | zero               | Always `0`                       |

The rows are not sorted by group number.

### Group Row (8 bytes)

| Offset  | Type | Field     | Notes                                                                 |
| ------- | ---- | --------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | name_ref  | String table index of the Korean name; equal to the row index on client 3473 |
| `+0x04` | u16  | group     | Crystal group number; LOC type 121 `str_id1`                         |
| `+0x06` | u16  | max_count | Most crystals of this group one preset holds; LOC type 121 `str_id2`  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Groups

On client 3473:

| Group | Korean          | LOC type 121                    | Max count |
| ----- | --------------- | ------------------------------- | --------- |
| 1     | 게르비슈        | Gervish                         | 1000      |
| 2     | 마칼로드        | Macalod                         | 1000      |
| 3     | 훔              | Hoom                            | 1000      |
| 4     | 적중            | Accuracy                        | 2         |
| 5     | 정령            | Spirit                          | 2         |
| 6     | 추가 피해 증가  | Increased Extra Damage          | 2         |
| 7     | 특정 저항 무시  | Ignore Certain Resistance       | 2         |
| 8     | 올루카스        | Olucas                          | 2         |
| 9     | 아크라드        | Ah'krad                         | 2         |
| 10    | 최대 생명력     | Max HP                          | 2         |
| 11    | 저항 증가 I     | Increased Resistance I          | 2         |
| 12    | 회피력 증가     | Increased Evasion               | 2         |
| 13    | 카르메          | Carmae                          | 2         |
| 14    | 아디스          | Addis                           | 2         |
| 15    | 피해 감소 증가  | Increases Damage Reduction      | 2         |
| 16    | 살무사          | Viper                           | 2         |
| 17    | 히스트리아      | Hystria                         | 2         |
| 18    | 붉은 전장 I     | Red Battlefield I               | 2         |
| 19    | 붉은 전장 II    | Red Battlefield II              | 2         |
| 20    | 낙하 피해 감소  | Fall Damage Reduction           | 2         |
| 21    | 점프력          | Jump Height                     | 2         |
| 22    | 내구도 감소 저항 | Durability Reduction Resistance | 2         |
| 23    | 공격시 회복     | Recovery on Attack              | 2         |
| 24    | 공성 무기 회피율 | Siege Weapon Evasion Rate       | 2         |
| 25    | 잠수 시간 증가  | Submergence                     | 2         |
| 26    | 은은한 마력     | Dim Magic                       | 6         |
| 27    | 최대 기운       | Max Energy                      | 2         |
| 28    | 검붉은 용장     | Dark Red Valor                  | 2         |
| 30    | 저항 증가 II    | Increased Resistance II         | 2         |
| 31    | 생활 특수 효과  | Life Skill Special Effect       | 2         |
| 32    | 낙원            | Paradise                        | 4         |
| 33    | 극 게르비슈     | Ultimate Gervish                | 4         |
| 34    | 극 마칼로드     | Ultimate Macalod                | 4         |
| 35    | 극 훔           | Ultimate Hoom                   | 4         |
| 36    | 혹한            | Bitterness                      | 2         |
| 37    | 척살            | Decimation                      | 2         |
| 38    | 파괴            | Destruction                     | 2         |
| 39    | 에다니아        | Edania                          | 1         |
| 100   | 없음            | No Group                        | 1000      |
| 101   | 고대 정령       | Ancient Spirit                  | 1         |
| 102   | 태초            | Primordial                      | 1         |
| 103   | 새벽            | Dawn                            | 6         |

## Notes

- `max_count` is the limit the crystal inventory window checks
  (`panel_window_jewelinven_all_1.luac`): for a crystal whose
  `getJewelGroupMaxCount()` is above 0, it counts the crystals with the same
  `getJewelGroupNumber()` in all `__eJewelSlotMaxCount` slots of the selected
  preset and greys the crystal out once that count reaches `max_count`. The
  preset has 23 slots (12 normal and 11 special controls in
  `panel_window_jewelpreset_all.xml`), so `1000` sets no limit in practice.
- LOC type 121 keys each group name by `(group, max_count)`: all 42 rows find
  their name under that pair on client 3473. LOC also holds `(26, 2)` Dim
  Magic next to `(26, 6)`, and `(29, 2)` Dark Red Armor, a group with no row
  here.
- The u16 at `end-0x02` of each [`itemenchant.dbss`](itemenchant_dbss.md)
  base block (`crystal_group` there) is this group number. On client
  3473 it is `0xFFFF` except in 481 crystals, and every value they store is
  a group here: Crystal of Frozen Bitterness (`15255`, 얼어붙은 혹한의
  수정) stores 36 혹한, the 21 Dawn crystals 103 새벽, and 187 crystals 100
  (No Group), among them Magic Crystal of Infinity - Valor (`768751`).
  Groups 7, 31 and 32 have no crystal.
- Neither the 2016 PDB nor a private server's `DataSheets.bexcel` on client
  1784 has this table, and the client 1784 PAZ has no
  `jewelgroupstaticstatus.bss`. The field names come from the Lua getters
  `getJewelGroupNumber()` and `getJewelGroupMaxCount()`.
