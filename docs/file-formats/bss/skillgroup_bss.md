# `skillgroup.bss` Format

## Purpose

The rank chains of player skills. A skill group is one entry of the skill
window, such as "Grave Digging", and lists the skill key of every rank in
order. The skill window grids in [`ui_skillgroup_*.bss`](ui_skillgroup_bss.md)
place groups, not single skills.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File             | Bytes  | Records           | Row bytes               |
| ------ | -------------- | ---------------- | ------ | ----------------- | ----------------------- |
| 1      | 1338 and later | `skillgroup.bss` | 65,078 | 3,517 Skill Group | 14 to 90, 19 on average |

| Layout | File             | Known             | Unknown    |
| ------ | ---------------- | ----------------- | ---------- |
| 1      | `skillgroup.bss` | 65,078 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `95607b65fe5a`  |
| 3482   | Layout 1 | `95607b65fe5a`  |
| 3474   | Layout 1 | `95607b65fe5a`  |
| 3473   | Layout 1 | `95607b65fe5a`  |
| 3464   | Layout 1 | `95607b65fe5a`  |
| 3458   | Layout 1 | `95607b65fe5a`  |
| 3454   | Layout 1 | `95607b65fe5a`  |
| 3444   | Layout 1 | `95607b65fe5a`  |
| 3435   | Layout 1 | `95607b65fe5a`  |
| 3426   | Layout 1 | `95607b65fe5a`  |
| 3418   | Layout 1 | `95607b65fe5a`  |
| 3412   | Layout 1 | `95607b65fe5a`  |
| 3402   | Layout 1 | `95607b65fe5a`  |
| 3396   | Layout 1 | `95607b65fe5a`  |
| 3387   | Layout 1 | `95607b65fe5a`  |
| 3381   | Layout 1 | `95607b65fe5a`  |
| 3373   | Layout 1 | `95607b65fe5a`  |
| 3364   | Layout 1 | `95607b65fe5a`  |
| 3356   | Layout 1 | `95607b65fe5a`  |
| 3349   | Layout 1 | `95607b65fe5a`  |
| 3342   | Layout 1 | `95607b65fe5a`  |
| 3335   | Layout 1 | `95607b65fe5a`  |
| 3326   | Layout 1 | `95607b65fe5a`  |
| 3321   | Layout 1 | `95607b65fe5a`  |
| 3314   | Layout 1 | `95607b65fe5a`  |
| 3303   | Layout 1 | `95607b65fe5a`  |
| 3302   | Layout 1 | `95607b65fe5a`  |
| 3293   | Layout 1 | `95607b65fe5a`  |
| 3283   | Layout 1 | `95607b65fe5a`  |
| 3275   | Layout 1 | `95607b65fe5a`  |
| 3267   | Layout 1 | `95607b65fe5a`  |
| 3258   | Layout 1 | `95607b65fe5a`  |
| 3251   | Layout 1 | `95607b65fe5a`  |
| 3242   | Layout 1 | `95607b65fe5a`  |
| 3235   | Layout 1 | `95607b65fe5a`  |
| 3229   | Layout 1 | `95607b65fe5a`  |
| 3212   | Layout 1 | `95607b65fe5a`  |
| 3203   | Layout 1 | `95607b65fe5a`  |
| 3193   | Layout 1 | `95607b65fe5a`  |
| 3186   | Layout 1 | `95607b65fe5a`  |
| 3177   | Layout 1 | `95607b65fe5a`  |
| 3169   | Layout 1 | `95607b65fe5a`  |
| 3158   | Layout 1 | `95607b65fe5a`  |
| 3151   | Layout 1 | `95607b65fe5a`  |
| 3144   | Layout 1 | `95607b65fe5a`  |
| 3133   | Layout 1 | `95607b65fe5a`  |
| 3125   | Layout 1 | `95607b65fe5a`  |
| 3118   | Layout 1 | `95607b65fe5a`  |
| 3111   | Layout 1 | `95607b65fe5a`  |
| 3103   | Layout 1 | `95607b65fe5a`  |
| 3095   | Layout 1 | `95607b65fe5a`  |
| 3086   | Layout 1 | `95607b65fe5a`  |
| 3072   | Layout 1 | `95607b65fe5a`  |
| 3062   | Layout 1 | `95607b65fe5a`  |
| 3052   | Layout 1 | `95607b65fe5a`  |
| 3045   | Layout 1 | `95607b65fe5a`  |
| 3037   | Layout 1 | `95607b65fe5a`  |
| 3030   | Layout 1 | `95607b65fe5a`  |
| 3021   | Layout 1 | `95607b65fe5a`  |
| 3012   | Layout 1 | `95607b65fe5a`  |
| 3002   | Layout 1 | `95607b65fe5a`  |
| 2995   | Layout 1 | `95607b65fe5a`  |
| 2987   | Layout 1 | `95607b65fe5a`  |
| 2978   | Layout 1 | `95607b65fe5a`  |
| 2970   | Layout 1 | `95607b65fe5a`  |
| 2959   | Layout 1 | `95607b65fe5a`  |
| 2951   | Layout 1 | `95607b65fe5a`  |
| 2942   | Layout 1 | `95607b65fe5a`  |
| 2935   | Layout 1 | `95607b65fe5a`  |
| 2932   | Layout 1 | `95607b65fe5a`  |
| 2923   | Layout 1 | `95607b65fe5a`  |
| 2919   | Layout 1 | `95607b65fe5a`  |
| 2907   | Layout 1 | `95607b65fe5a`  |
| 2900   | Layout 1 | `95607b65fe5a`  |
| 2891   | Layout 1 | `95607b65fe5a`  |
| 2882   | Layout 1 | `95607b65fe5a`  |
| 2872   | Layout 1 | `95607b65fe5a`  |
| 2863   | Layout 1 | `95607b65fe5a`  |
| 2855   | Layout 1 | `95607b65fe5a`  |
| 2849   | Layout 1 | `95607b65fe5a`  |
| 2844   | Layout 1 | `95607b65fe5a`  |
| 2834   | Layout 1 | `95607b65fe5a`  |
| 2825   | Layout 1 | `95607b65fe5a`  |
| 2819   | Layout 1 | `95607b65fe5a`  |
| 2811   | Layout 1 | `95607b65fe5a`  |
| 2803   | Layout 1 | `95607b65fe5a`  |
| 2794   | Layout 1 | `95607b65fe5a`  |
| 2783   | Layout 1 | `95607b65fe5a`  |
| 2774   | Layout 1 | `95607b65fe5a`  |
| 2765   | Layout 1 | `95607b65fe5a`  |
| 2756   | Layout 1 | `95607b65fe5a`  |
| 2750   | Layout 1 | `95607b65fe5a`  |
| 2743   | Layout 1 | `95607b65fe5a`  |
| 2736   | Layout 1 | `95607b65fe5a`  |
| 2726   | Layout 1 | `95607b65fe5a`  |
| 2717   | Layout 1 | `95607b65fe5a`  |
| 2709   | Layout 1 | `95607b65fe5a`  |
| 2703   | Layout 1 | `95607b65fe5a`  |
| 2695   | Layout 1 | `95607b65fe5a`  |
| 2684   | Layout 1 | `95607b65fe5a`  |
| 2672   | Layout 1 | `95607b65fe5a`  |
| 2665   | Layout 1 | `95607b65fe5a`  |
| 2657   | Layout 1 | `95607b65fe5a`  |
| 2649   | Layout 1 | `95607b65fe5a`  |
| 2644   | Layout 1 | `95607b65fe5a`  |
| 2637   | Layout 1 | `95607b65fe5a`  |
| 2629   | Layout 1 | `95607b65fe5a`  |
| 2619   | Layout 1 | `95607b65fe5a`  |
| 2612   | Layout 1 | `95607b65fe5a`  |
| 2606   | Layout 1 | `95607b65fe5a`  |
| 2602   | Layout 1 | `95607b65fe5a`  |
| 2601   | Layout 1 | `95607b65fe5a`  |
| 2592   | Layout 1 | `95607b65fe5a`  |
| 2583   | Layout 1 | `95607b65fe5a`  |
| 2575   | Layout 1 | `95607b65fe5a`  |
| 2567   | Layout 1 | `95607b65fe5a`  |
| 2560   | Layout 1 | `95607b65fe5a`  |
| 2553   | Layout 1 | `95607b65fe5a`  |
| 2545   | Layout 1 | `95607b65fe5a`  |
| 2538   | Layout 1 | `95607b65fe5a`  |
| 2529   | Layout 1 | `95607b65fe5a`  |
| 2519   | Layout 1 | `95607b65fe5a`  |
| 2513   | Layout 1 | `95607b65fe5a`  |
| 2510   | Layout 1 | `95607b65fe5a`  |
| 2507   | Layout 1 | `95607b65fe5a`  |
| 2503   | Layout 1 | `95607b65fe5a`  |
| 2498   | Layout 1 | `95607b65fe5a`  |
| 2492   | Layout 1 | `95607b65fe5a`  |
| 2487   | Layout 1 | `95607b65fe5a`  |
| 2480   | Layout 1 | `95607b65fe5a`  |
| 2474   | Layout 1 | `95607b65fe5a`  |
| 2468   | Layout 1 | `95607b65fe5a`  |
| 2460   | Layout 1 | `95607b65fe5a`  |
| 2453   | Layout 1 | `95607b65fe5a`  |
| 2444   | Layout 1 | `95607b65fe5a`  |
| 2438   | Layout 1 | `95607b65fe5a`  |
| 2434   | Layout 1 | `95607b65fe5a`  |
| 2429   | Layout 1 | `95607b65fe5a`  |
| 2421   | Layout 1 | `95607b65fe5a`  |
| 2414   | Layout 1 | `95607b65fe5a`  |
| 2407   | Layout 1 | `95607b65fe5a`  |
| 2401   | Layout 1 | `95607b65fe5a`  |
| 2397   | Layout 1 | `95607b65fe5a`  |
| 2393   | Layout 1 | `95607b65fe5a`  |
| 2384   | Layout 1 | `95607b65fe5a`  |
| 2378   | Layout 1 | `95607b65fe5a`  |
| 2372   | Layout 1 | `95607b65fe5a`  |
| 2358   | Layout 1 | `95607b65fe5a`  |
| 2352   | Layout 1 | `95607b65fe5a`  |
| 2347   | Layout 1 | `95607b65fe5a`  |
| 2343   | Layout 1 | `95607b65fe5a`  |
| 2335   | Layout 1 | `95607b65fe5a`  |
| 2327   | Layout 1 | `95607b65fe5a`  |
| 2324   | Layout 1 | `95607b65fe5a`  |
| 2319   | Layout 1 | `95607b65fe5a`  |
| 2313   | Layout 1 | `95607b65fe5a`  |
| 2308   | Layout 1 | `95607b65fe5a`  |
| 2302   | Layout 1 | `95607b65fe5a`  |
| 2295   | Layout 1 | `95607b65fe5a`  |
| 2290   | Layout 1 | `95607b65fe5a`  |
| 2284   | Layout 1 | `95607b65fe5a`  |
| 2276   | Layout 1 | `95607b65fe5a`  |
| 2269   | Layout 1 | `95607b65fe5a`  |
| 2259   | Layout 1 | `95607b65fe5a`  |
| 2250   | Layout 1 | `95607b65fe5a`  |
| 2243   | Layout 1 | `95607b65fe5a`  |
| 2235   | Layout 1 | `95607b65fe5a`  |
| 2229   | Layout 1 | `95607b65fe5a`  |
| 2224   | Layout 1 | `95607b65fe5a`  |
| 2218   | Layout 1 | `95607b65fe5a`  |
| 2215   | Layout 1 | `95607b65fe5a`  |
| 2207   | Layout 1 | `95607b65fe5a`  |
| 2203   | Layout 1 | `95607b65fe5a`  |
| 2196   | Layout 1 | `95607b65fe5a`  |
| 2192   | Layout 1 | `95607b65fe5a`  |
| 2189   | Layout 1 | `95607b65fe5a`  |
| 2183   | Layout 1 | `95607b65fe5a`  |
| 2179   | Layout 1 | `95607b65fe5a`  |
| 2171   | Layout 1 | `95607b65fe5a`  |
| 2163   | Layout 1 | `95607b65fe5a`  |
| 2156   | Layout 1 | `95607b65fe5a`  |
| 2151   | Layout 1 | `95607b65fe5a`  |
| 2147   | Layout 1 | `95607b65fe5a`  |
| 2142   | Layout 1 | `95607b65fe5a`  |
| 2138   | Layout 1 | `95607b65fe5a`  |
| 2134   | Layout 1 | `95607b65fe5a`  |
| 2130   | Layout 1 | `95607b65fe5a`  |
| 2122   | Layout 1 | `95607b65fe5a`  |
| 2107   | Layout 1 | `95607b65fe5a`  |
| 2098   | Layout 1 | `95607b65fe5a`  |
| 2089   | Layout 1 | `95607b65fe5a`  |
| 2081   | Layout 1 | `95607b65fe5a`  |
| 2073   | Layout 1 | `95607b65fe5a`  |
| 2067   | Layout 1 | `95607b65fe5a`  |
| 2063   | Layout 1 | `95607b65fe5a`  |
| 2059   | Layout 1 | `95607b65fe5a`  |
| 2052   | Layout 1 | `95607b65fe5a`  |
| 2044   | Layout 1 | `95607b65fe5a`  |
| 2039   | Layout 1 | `95607b65fe5a`  |
| 2032   | Layout 1 | `95607b65fe5a`  |
| 2025   | Layout 1 | `95607b65fe5a`  |
| 2011   | Layout 1 | `95607b65fe5a`  |
| 2005   | Layout 1 | `95607b65fe5a`  |
| 2000   | Layout 1 | `95607b65fe5a`  |
| 1996   | Layout 1 | `95607b65fe5a`  |
| 1991   | Layout 1 | `95607b65fe5a`  |
| 1985   | Layout 1 | `95607b65fe5a`  |
| 1980   | Layout 1 | `95607b65fe5a`  |
| 1969   | Layout 1 | `95607b65fe5a`  |
| 1964   | Layout 1 | `95607b65fe5a`  |
| 1958   | Layout 1 | `95607b65fe5a`  |
| 1950   | Layout 1 | `95607b65fe5a`  |
| 1945   | Layout 1 | `95607b65fe5a`  |
| 1937   | Layout 1 | `95607b65fe5a`  |
| 1933   | Layout 1 | `95607b65fe5a`  |
| 1927   | Layout 1 | `95607b65fe5a`  |
| 1921   | Layout 1 | `95607b65fe5a`  |
| 1914   | Layout 1 | `95607b65fe5a`  |
| 1908   | Layout 1 | `95607b65fe5a`  |
| 1897   | Layout 1 | `95607b65fe5a`  |
| 1892   | Layout 1 | `95607b65fe5a`  |
| 1886   | Layout 1 | `95607b65fe5a`  |
| 1881   | Layout 1 | `95607b65fe5a`  |
| 1871   | Layout 1 | `95607b65fe5a`  |
| 1866   | Layout 1 | `95607b65fe5a`  |
| 1862   | Layout 1 | `95607b65fe5a`  |
| 1854   | Layout 1 | `95607b65fe5a`  |
| 1846   | Layout 1 | `95607b65fe5a`  |
| 1838   | Layout 1 | `95607b65fe5a`  |
| 1832   | Layout 1 | `95607b65fe5a`  |
| 1826   | Layout 1 | `95607b65fe5a`  |
| 1822   | Layout 1 | `95607b65fe5a`  |
| 1818   | Layout 1 | `95607b65fe5a`  |
| 1804   | Layout 1 | `95607b65fe5a`  |
| 1794   | Layout 1 | `95607b65fe5a`  |
| 1790   | Layout 1 | `95607b65fe5a`  |
| 1784   | Layout 1 | `95607b65fe5a`  |
| 1774   | Layout 1 | `95607b65fe5a`  |
| 1771   | Layout 1 | `95607b65fe5a`  |
| 1762   | Layout 1 | `95607b65fe5a`  |
| 1759   | Layout 1 | `95607b65fe5a`  |
| 1754   | Layout 1 | `95607b65fe5a`  |
| 1749   | Layout 1 | `95607b65fe5a`  |
| 1743   | Layout 1 | `95607b65fe5a`  |
| 1737   | Layout 1 | `95607b65fe5a`  |
| 1731   | Layout 1 | `95607b65fe5a`  |
| 1725   | Layout 1 | `95607b65fe5a`  |
| 1717   | Layout 1 | `95607b65fe5a`  |
| 1710   | Layout 1 | `95607b65fe5a`  |
| 1704   | Layout 1 | `95607b65fe5a`  |
| 1698   | Layout 1 | `95607b65fe5a`  |
| 1690   | Layout 1 | `95607b65fe5a`  |
| 1685   | Layout 1 | `95607b65fe5a`  |
| 1680   | Layout 1 | `95607b65fe5a`  |
| 1674   | Layout 1 | `95607b65fe5a`  |
| 1668   | Layout 1 | `95607b65fe5a`  |
| 1659   | Layout 1 | `95607b65fe5a`  |
| 1649   | Layout 1 | `95607b65fe5a`  |
| 1642   | Layout 1 | `95607b65fe5a`  |
| 1636   | Layout 1 | `95607b65fe5a`  |
| 1628   | Layout 1 | `95607b65fe5a`  |
| 1622   | Layout 1 | `95607b65fe5a`  |
| 1614   | Layout 1 | `95607b65fe5a`  |
| 1608   | Layout 1 | `95607b65fe5a`  |
| 1602   | Layout 1 | `95607b65fe5a`  |
| 1598   | Layout 1 | `95607b65fe5a`  |
| 1594   | Layout 1 | `95607b65fe5a`  |
| 1590   | Layout 1 | `95607b65fe5a`  |
| 1587   | Layout 1 | `95607b65fe5a`  |
| 1584   | Layout 1 | `95607b65fe5a`  |
| 1579   | Layout 1 | `95607b65fe5a`  |
| 1572   | Layout 1 | `95607b65fe5a`  |
| 1565   | Layout 1 | `95607b65fe5a`  |
| 1559   | Layout 1 | `95607b65fe5a`  |
| 1554   | Layout 1 | `95607b65fe5a`  |
| 1547   | Layout 1 | `95607b65fe5a`  |
| 1537   | Layout 1 | `95607b65fe5a`  |
| 1529   | Layout 1 | `95607b65fe5a`  |
| 1524   | Layout 1 | `95607b65fe5a`  |
| 1519   | Layout 1 | `95607b65fe5a`  |
| 1509   | Layout 1 | `95607b65fe5a`  |
| 1506   | Layout 1 | `95607b65fe5a`  |
| 1504   | Layout 1 | `95607b65fe5a`  |
| 1500   | Layout 1 | `95607b65fe5a`  |
| 1493   | Layout 1 | `95607b65fe5a`  |
| 1489   | Layout 1 | `95607b65fe5a`  |
| 1485   | Layout 1 | `95607b65fe5a`  |
| 1481   | Layout 1 | `95607b65fe5a`  |
| 1474   | Layout 1 | `95607b65fe5a`  |
| 1466   | Layout 1 | `95607b65fe5a`  |
| 1462   | Layout 1 | `95607b65fe5a`  |
| 1459   | Layout 1 | `95607b65fe5a`  |
| 1453   | Layout 1 | `95607b65fe5a`  |
| 1450   | Layout 1 | `95607b65fe5a`  |
| 1445   | Layout 1 | `95607b65fe5a`  |
| 1439   | Layout 1 | `95607b65fe5a`  |
| 1433   | Layout 1 | `95607b65fe5a`  |
| 1430   | Layout 1 | `95607b65fe5a`  |
| 1426   | Layout 1 | `95607b65fe5a`  |
| 1421   | Layout 1 | `95607b65fe5a`  |
| 1417   | Layout 1 | `95607b65fe5a`  |
| 1416   | Layout 1 | `95607b65fe5a`  |
| 1409   | Layout 1 | `95607b65fe5a`  |
| 1405   | Layout 1 | `95607b65fe5a`  |
| 1401   | Layout 1 | `95607b65fe5a`  |
| 1396   | Layout 1 | `95607b65fe5a`  |
| 1391   | Layout 1 | `95607b65fe5a`  |
| 1390   | Layout 1 | `95607b65fe5a`  |
| 1386   | Layout 1 | `95607b65fe5a`  |
| 1381   | Layout 1 | `95607b65fe5a`  |
| 1379   | Layout 1 | `95607b65fe5a`  |
| 1372   | Layout 1 | `95607b65fe5a`  |
| 1366   | Layout 1 | `95607b65fe5a`  |
| 1364   | Layout 1 | `95607b65fe5a`  |
| 1363   | Layout 1 | `95607b65fe5a`  |
| 1360   | Layout 1 | `95607b65fe5a`  |
| 1358   | Layout 1 | `95607b65fe5a`  |
| 1355   | Layout 1 | `95607b65fe5a`  |
| 1351   | Layout 1 | `95607b65fe5a`  |
| 1348   | Layout 1 | `95607b65fe5a`  |
| 1346   | Layout 1 | `95607b65fe5a`  |
| 1341   | Layout 1 | `95607b65fe5a`  |
| 1340   | Layout 1 | `95607b65fe5a`  |
| 1338   | Layout 1 | `95607b65fe5a`  |
| 1335   | No file  | `95607b65fe5a`  |
| 1333   | No file  | `95607b65fe5a`  |
| 1329   | No file  | `95607b65fe5a`  |
| 1327   | No file  | `95607b65fe5a`  |
| 1324   | No file  | `95607b65fe5a`  |
| 1321   | No file  | `95607b65fe5a`  |
| 1319   | No file  | `95607b65fe5a`  |
| 1318   | No file  | `95607b65fe5a`  |
| 1316   | No file  | `95607b65fe5a`  |
| 1313   | No file  | `95607b65fe5a`  |
| 1311   | No file  | `95607b65fe5a`  |
| 1309   | No file  | `95607b65fe5a`  |
| 1304   | No file  | `95607b65fe5a`  |
| 1292   | No file  | `95607b65fe5a`  |
| 1286   | No file  | `95607b65fe5a`  |
| 1280   | No file  | `95607b65fe5a`  |
| 1276   | No file  | `95607b65fe5a`  |
| 1267   | No file  | `95607b65fe5a`  |
| 1261   | No file  | `95607b65fe5a`  |
| 1256   | No file  | `95607b65fe5a`  |
| 1250   | No file  | `95607b65fe5a`  |
| 1246   | No file  | `95607b65fe5a`  |
| 1239   | No file  | `95607b65fe5a`  |
| 1230   | No file  | `95607b65fe5a`  |
| 1226   | No file  | `95607b65fe5a`  |
| 1220   | No file  | `95607b65fe5a`  |
| 1217   | No file  | `95607b65fe5a`  |
| 1211   | No file  | `95607b65fe5a`  |
| 1210   | No file  | `95607b65fe5a`  |
| 1208   | No file  | `95607b65fe5a`  |
| 1203   | No file  | `95607b65fe5a`  |
| 1197   | No file  | `95607b65fe5a`  |
| 1194   | No file  | `95607b65fe5a`  |
| 1192   | No file  | `95607b65fe5a`  |
| 1187   | No file  | `95607b65fe5a`  |
| 1183   | No file  | `95607b65fe5a`  |
| 1177   | No file  | `95607b65fe5a`  |
| 1173   | No file  | `95607b65fe5a`  |
| 1167   | No file  | `95607b65fe5a`  |
| 1164   | No file  | `95607b65fe5a`  |
| 1156   | No file  | `95607b65fe5a`  |
| 1149   | No file  | `95607b65fe5a`  |
| 1144   | No file  | `95607b65fe5a`  |
| 1137   | No file  | `95607b65fe5a`  |
| 1132   | No file  | `95607b65fe5a`  |
| 1127   | No file  | `95607b65fe5a`  |
| 1122   | No file  | `95607b65fe5a`  |
| 1118   | No file  | `95607b65fe5a`  |
| 1114   | No file  | `95607b65fe5a`  |
| 1109   | No file  | `95607b65fe5a`  |
| 1102   | No file  | `95607b65fe5a`  |
| 1096   | No file  | `95607b65fe5a`  |
| 1088   | No file  | `95607b65fe5a`  |
| 1081   | No file  | `95607b65fe5a`  |
| 1076   | No file  | `95607b65fe5a`  |
| 1069   | No file  | `95607b65fe5a`  |
| 1064   | No file  | `95607b65fe5a`  |
| 1058   | No file  | `95607b65fe5a`  |
| 1051   | No file  | `95607b65fe5a`  |
| 1044   | No file  | `95607b65fe5a`  |
| 1036   | No file  | `95607b65fe5a`  |
| 1026   | No file  | `95607b65fe5a`  |
| 1016   | No file  | `95607b65fe5a`  |
| 1009   | No file  | `95607b65fe5a`  |
| 1005   | No file  | `95607b65fe5a`  |
| 1000   | No file  | `95607b65fe5a`  |
| 998    | No file  | `95607b65fe5a`  |
| 990    | No file  | `95607b65fe5a`  |
| 979    | No file  | `95607b65fe5a`  |
| 972    | No file  | `95607b65fe5a`  |
| 963    | No file  | `95607b65fe5a`  |
| 955    | No file  | `95607b65fe5a`  |
| 946    | No file  | `95607b65fe5a`  |
| 938    | No file  | `95607b65fe5a`  |
| 927    | No file  | `95607b65fe5a`  |
| 911    | No file  | `95607b65fe5a`  |
| 904    | No file  | `95607b65fe5a`  |
| 899    | No file  | `95607b65fe5a`  |
| 894    | No file  | `95607b65fe5a`  |
| 885    | No file  | `95607b65fe5a`  |
| 879    | No file  | `95607b65fe5a`  |
| 872    | No file  | `95607b65fe5a`  |
| 864    | No file  | `95607b65fe5a`  |
| 855    | No file  | `95607b65fe5a`  |
| 853    | No file  | `95607b65fe5a`  |
| 845    | No file  | `95607b65fe5a`  |
| 837    | No file  | `95607b65fe5a`  |
| 829    | No file  | `95607b65fe5a`  |
| 822    | No file  | `95607b65fe5a`  |
| 814    | No file  | `95607b65fe5a`  |
| 805    | No file  | `95607b65fe5a`  |
| 794    | No file  | `95607b65fe5a`  |
| 787    | No file  | `95607b65fe5a`  |
| 780    | No file  | `95607b65fe5a`  |
| 771    | No file  | `95607b65fe5a`  |
| 760    | No file  | `95607b65fe5a`  |
| 748    | No file  | `95607b65fe5a`  |
| 741    | No file  | `95607b65fe5a`  |
| 736    | No file  | `95607b65fe5a`  |
| 731    | No file  | `95607b65fe5a`  |
| 723    | No file  | `95607b65fe5a`  |
| 711    | No file  | `95607b65fe5a`  |
| 707    | No file  | `95607b65fe5a`  |
| 697    | No file  | `95607b65fe5a`  |
| 689    | No file  | `95607b65fe5a`  |
| 683    | No file  | `95607b65fe5a`  |
| 678    | No file  | `95607b65fe5a`  |
| 670    | No file  | `95607b65fe5a`  |
| 661    | No file  | `95607b65fe5a`  |
| 656    | No file  | `95607b65fe5a`  |
| 652    | No file  | `95607b65fe5a`  |
| 643    | No file  | `95607b65fe5a`  |
| 637    | No file  | `95607b65fe5a`  |
| 630    | No file  | `95607b65fe5a`  |
| 627    | No file  | `95607b65fe5a`  |
| 621    | No file  | `95607b65fe5a`  |
| 617    | No file  | `95607b65fe5a`  |
| 615    | No file  | `95607b65fe5a`  |
| 606    | No file  | `95607b65fe5a`  |
| 599    | No file  | `95607b65fe5a`  |
| 592    | No file  | `95607b65fe5a`  |
| 586    | No file  | `95607b65fe5a`  |
| 577    | No file  | `95607b65fe5a`  |
| 569    | No file  | `95607b65fe5a`  |
| 561    | No file  | `95607b65fe5a`  |
| 554    | No file  | `95607b65fe5a`  |
| 542    | No file  | `95607b65fe5a`  |
| 532    | No file  | `95607b65fe5a`  |
| 531    | No file  | `95607b65fe5a`  |
| 526    | No file  | `95607b65fe5a`  |
| 521    | No file  | `95607b65fe5a`  |
| 517    | No file  | `95607b65fe5a`  |
| 510    | No file  | `95607b65fe5a`  |
| 508    | No file  | `95607b65fe5a`  |
| 504    | No file  | `95607b65fe5a`  |
| 497    | No file  | `95607b65fe5a`  |
| 491    | No file  | `95607b65fe5a`  |
| 485    | No file  | `95607b65fe5a`  |
| 478    | No file  | `95607b65fe5a`  |
| 472    | No file  | `95607b65fe5a`  |
| 466    | No file  | `95607b65fe5a`  |
| 457    | No file  | `95607b65fe5a`  |
| 452    | No file  | `95607b65fe5a`  |
| 449    | No file  | `95607b65fe5a`  |
| 435    | No file  | `95607b65fe5a`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                          |
| --------------------- | -------- | ------------------------------------------------------------- |
| `skill.dbss`          | Optional | The rank records, see [`skill.dbss`](../dbss/skill_dbss.md)           |
| `languagedata_en.loc` | Optional | Rank names, LOC type `10`, `str_id1 = skill_key >> 16`        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No magic and no trailer: a u32 group count, then the groups back to back up
to the end of the file.

| Offset  | Type                     | Field       | Notes                                    |
| ------- | ------------------------ | ----------- | ---------------------------------------- |
| `+0x00` | u32                      | group_count | `3514` on client 3458                    |
| `+0x04` | Skill Group[group_count] | groups      | Variable-size groups, see Skill Group    |

### Skill Group (variable: 6 bytes + skill keys)

| Offset  | Type             | Field      | Notes                                                                    |
| ------- | ---------------- | ---------- | ------------------------------------------------------------------------ |
| `+0x00` | u16              | group_no   | Unique; `142` to `15162`, not sorted                                     |
| `+0x02` | u32              | rank_count | Number of keys that follow, including the unlearned entry; up to `21`    |
| `+0x06` | u32[rank_count]  | skill_keys | Rank 0 is always `0` (not learned); the rest are `skill.dbss` keys in rank order |

2,271 groups have a single rank (`rank_count` 2); the longest chains have 20
ranks. Every rank key is a `skill.dbss` key.

## Notes

- The layout comes from bdo-data-extractor and walks exactly to the end of
  the file on client 3458.
- Rank `i` usually lists rank `i + 1` in its `skill.dbss` `next_skill_keys`
  (3,422 of 3,858 consecutive pairs).
