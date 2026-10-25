# `dropuimaincategoryinfo.bss` Format

## Purpose

The region tabs of the drop item window (Monster Zone Info): one fixed row
per tab with its territory and tab icon.
[`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md) puts each
hunting ground on a tab through `main_category_key`, and its handler reads
this file for the Region column.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes | Records    | Row bytes |
| ------ | -------------- | ---------------------------- | ----- | ---------- | --------- |
| 1      | 1914 and later | `dropuimaincategoryinfo.bss` | 631   | 13 Tab Row | 10        |

| Layout | File                         | Known          | Unknown    |
| ------ | ---------------------------- | -------------- | ---------- |
| 1      | `dropuimaincategoryinfo.bss` | 631 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `18492e0931b7`  |
| 3482   | Layout 1 | `18492e0931b7`  |
| 3474   | Layout 1 | `18492e0931b7`  |
| 3473   | Layout 1 | `18492e0931b7`  |
| 3464   | Layout 1 | `18492e0931b7`  |
| 3458   | Layout 1 | `18492e0931b7`  |
| 3454   | Layout 1 | `18492e0931b7`  |
| 3444   | Layout 1 | `18492e0931b7`  |
| 3435   | Layout 1 | `18492e0931b7`  |
| 3426   | Layout 1 | `18492e0931b7`  |
| 3418   | Layout 1 | `18492e0931b7`  |
| 3412   | Layout 1 | `18492e0931b7`  |
| 3402   | Layout 1 | `18492e0931b7`  |
| 3396   | Layout 1 | `18492e0931b7`  |
| 3387   | Layout 1 | `18492e0931b7`  |
| 3381   | Layout 1 | `18492e0931b7`  |
| 3373   | Layout 1 | `18492e0931b7`  |
| 3364   | Layout 1 | `18492e0931b7`  |
| 3356   | Layout 1 | `18492e0931b7`  |
| 3349   | Layout 1 | `18492e0931b7`  |
| 3342   | Layout 1 | `18492e0931b7`  |
| 3335   | Layout 1 | `18492e0931b7`  |
| 3326   | Layout 1 | `18492e0931b7`  |
| 3321   | Layout 1 | `18492e0931b7`  |
| 3314   | Layout 1 | `18492e0931b7`  |
| 3303   | Layout 1 | `18492e0931b7`  |
| 3302   | Layout 1 | `18492e0931b7`  |
| 3293   | Layout 1 | `18492e0931b7`  |
| 3283   | Layout 1 | `18492e0931b7`  |
| 3275   | Layout 1 | `18492e0931b7`  |
| 3267   | Layout 1 | `18492e0931b7`  |
| 3258   | Layout 1 | `18492e0931b7`  |
| 3251   | Layout 1 | `18492e0931b7`  |
| 3242   | Layout 1 | `18492e0931b7`  |
| 3235   | Layout 1 | `18492e0931b7`  |
| 3229   | Layout 1 | `18492e0931b7`  |
| 3212   | Layout 1 | `18492e0931b7`  |
| 3203   | Layout 1 | `18492e0931b7`  |
| 3193   | Layout 1 | `18492e0931b7`  |
| 3186   | Layout 1 | `18492e0931b7`  |
| 3177   | Layout 1 | `18492e0931b7`  |
| 3169   | Layout 1 | `18492e0931b7`  |
| 3158   | Layout 1 | `18492e0931b7`  |
| 3151   | Layout 1 | `18492e0931b7`  |
| 3144   | Layout 1 | `18492e0931b7`  |
| 3133   | Layout 1 | `18492e0931b7`  |
| 3125   | Layout 1 | `18492e0931b7`  |
| 3118   | Layout 1 | `18492e0931b7`  |
| 3111   | Layout 1 | `18492e0931b7`  |
| 3103   | Layout 1 | `18492e0931b7`  |
| 3095   | Layout 1 | `18492e0931b7`  |
| 3086   | Layout 1 | `18492e0931b7`  |
| 3072   | Layout 1 | `18492e0931b7`  |
| 3062   | Layout 1 | `18492e0931b7`  |
| 3052   | Layout 1 | `18492e0931b7`  |
| 3045   | Layout 1 | `18492e0931b7`  |
| 3037   | Layout 1 | `18492e0931b7`  |
| 3030   | Layout 1 | `18492e0931b7`  |
| 3021   | Layout 1 | `18492e0931b7`  |
| 3012   | Layout 1 | `18492e0931b7`  |
| 3002   | Layout 1 | `18492e0931b7`  |
| 2995   | Layout 1 | `18492e0931b7`  |
| 2987   | Layout 1 | `18492e0931b7`  |
| 2978   | Layout 1 | `18492e0931b7`  |
| 2970   | Layout 1 | `18492e0931b7`  |
| 2959   | Layout 1 | `18492e0931b7`  |
| 2951   | Layout 1 | `18492e0931b7`  |
| 2942   | Layout 1 | `18492e0931b7`  |
| 2935   | Layout 1 | `18492e0931b7`  |
| 2932   | Layout 1 | `18492e0931b7`  |
| 2923   | Layout 1 | `18492e0931b7`  |
| 2919   | Layout 1 | `18492e0931b7`  |
| 2907   | Layout 1 | `18492e0931b7`  |
| 2900   | Layout 1 | `18492e0931b7`  |
| 2891   | Layout 1 | `18492e0931b7`  |
| 2882   | Layout 1 | `18492e0931b7`  |
| 2872   | Layout 1 | `18492e0931b7`  |
| 2863   | Layout 1 | `18492e0931b7`  |
| 2855   | Layout 1 | `18492e0931b7`  |
| 2849   | Layout 1 | `18492e0931b7`  |
| 2844   | Layout 1 | `18492e0931b7`  |
| 2834   | Layout 1 | `18492e0931b7`  |
| 2825   | Layout 1 | `18492e0931b7`  |
| 2819   | Layout 1 | `18492e0931b7`  |
| 2811   | Layout 1 | `18492e0931b7`  |
| 2803   | Layout 1 | `18492e0931b7`  |
| 2794   | Layout 1 | `18492e0931b7`  |
| 2783   | Layout 1 | `18492e0931b7`  |
| 2774   | Layout 1 | `18492e0931b7`  |
| 2765   | Layout 1 | `18492e0931b7`  |
| 2756   | Layout 1 | `18492e0931b7`  |
| 2750   | Layout 1 | `18492e0931b7`  |
| 2743   | Layout 1 | `18492e0931b7`  |
| 2736   | Layout 1 | `18492e0931b7`  |
| 2726   | Layout 1 | `18492e0931b7`  |
| 2717   | Layout 1 | `18492e0931b7`  |
| 2709   | Layout 1 | `18492e0931b7`  |
| 2703   | Layout 1 | `18492e0931b7`  |
| 2695   | Layout 1 | `18492e0931b7`  |
| 2684   | Layout 1 | `18492e0931b7`  |
| 2672   | Layout 1 | `18492e0931b7`  |
| 2665   | Layout 1 | `18492e0931b7`  |
| 2657   | Layout 1 | `18492e0931b7`  |
| 2649   | Layout 1 | `18492e0931b7`  |
| 2644   | Layout 1 | `18492e0931b7`  |
| 2637   | Layout 1 | `18492e0931b7`  |
| 2629   | Layout 1 | `18492e0931b7`  |
| 2619   | Layout 1 | `18492e0931b7`  |
| 2612   | Layout 1 | `18492e0931b7`  |
| 2606   | Layout 1 | `18492e0931b7`  |
| 2602   | Layout 1 | `18492e0931b7`  |
| 2601   | Layout 1 | `18492e0931b7`  |
| 2592   | Layout 1 | `18492e0931b7`  |
| 2583   | Layout 1 | `18492e0931b7`  |
| 2575   | Layout 1 | `18492e0931b7`  |
| 2567   | Layout 1 | `18492e0931b7`  |
| 2560   | Layout 1 | `18492e0931b7`  |
| 2553   | Layout 1 | `18492e0931b7`  |
| 2545   | Layout 1 | `18492e0931b7`  |
| 2538   | Layout 1 | `18492e0931b7`  |
| 2529   | Layout 1 | `18492e0931b7`  |
| 2519   | Layout 1 | `18492e0931b7`  |
| 2513   | Layout 1 | `18492e0931b7`  |
| 2510   | Layout 1 | `18492e0931b7`  |
| 2507   | Layout 1 | `18492e0931b7`  |
| 2503   | Layout 1 | `18492e0931b7`  |
| 2498   | Layout 1 | `18492e0931b7`  |
| 2492   | Layout 1 | `18492e0931b7`  |
| 2487   | Layout 1 | `18492e0931b7`  |
| 2480   | Layout 1 | `18492e0931b7`  |
| 2474   | Layout 1 | `18492e0931b7`  |
| 2468   | Layout 1 | `18492e0931b7`  |
| 2460   | Layout 1 | `18492e0931b7`  |
| 2453   | Layout 1 | `18492e0931b7`  |
| 2444   | Layout 1 | `18492e0931b7`  |
| 2438   | Layout 1 | `18492e0931b7`  |
| 2434   | Layout 1 | `18492e0931b7`  |
| 2429   | Layout 1 | `18492e0931b7`  |
| 2421   | Layout 1 | `18492e0931b7`  |
| 2414   | Layout 1 | `18492e0931b7`  |
| 2407   | Layout 1 | `18492e0931b7`  |
| 2401   | Layout 1 | `18492e0931b7`  |
| 2397   | Layout 1 | `18492e0931b7`  |
| 2393   | Layout 1 | `18492e0931b7`  |
| 2384   | Layout 1 | `18492e0931b7`  |
| 2378   | Layout 1 | `18492e0931b7`  |
| 2372   | Layout 1 | `18492e0931b7`  |
| 2358   | Layout 1 | `18492e0931b7`  |
| 2352   | Layout 1 | `18492e0931b7`  |
| 2347   | Layout 1 | `18492e0931b7`  |
| 2343   | Layout 1 | `18492e0931b7`  |
| 2335   | Layout 1 | `18492e0931b7`  |
| 2327   | Layout 1 | `18492e0931b7`  |
| 2324   | Layout 1 | `18492e0931b7`  |
| 2319   | Layout 1 | `18492e0931b7`  |
| 2313   | Layout 1 | `18492e0931b7`  |
| 2308   | Layout 1 | `18492e0931b7`  |
| 2302   | Layout 1 | `18492e0931b7`  |
| 2295   | Layout 1 | `18492e0931b7`  |
| 2290   | Layout 1 | `18492e0931b7`  |
| 2284   | Layout 1 | `18492e0931b7`  |
| 2276   | Layout 1 | `18492e0931b7`  |
| 2269   | Layout 1 | `18492e0931b7`  |
| 2259   | Layout 1 | `18492e0931b7`  |
| 2250   | Layout 1 | `18492e0931b7`  |
| 2243   | Layout 1 | `18492e0931b7`  |
| 2235   | Layout 1 | `18492e0931b7`  |
| 2229   | Layout 1 | `18492e0931b7`  |
| 2224   | Layout 1 | `18492e0931b7`  |
| 2218   | Layout 1 | `18492e0931b7`  |
| 2215   | Layout 1 | `18492e0931b7`  |
| 2207   | Layout 1 | `18492e0931b7`  |
| 2203   | Layout 1 | `18492e0931b7`  |
| 2196   | Layout 1 | `18492e0931b7`  |
| 2192   | Layout 1 | `18492e0931b7`  |
| 2189   | Layout 1 | `18492e0931b7`  |
| 2183   | Layout 1 | `18492e0931b7`  |
| 2179   | Layout 1 | `18492e0931b7`  |
| 2171   | Layout 1 | `18492e0931b7`  |
| 2163   | Layout 1 | `18492e0931b7`  |
| 2156   | Layout 1 | `18492e0931b7`  |
| 2151   | Layout 1 | `18492e0931b7`  |
| 2147   | Layout 1 | `18492e0931b7`  |
| 2142   | Layout 1 | `18492e0931b7`  |
| 2138   | Layout 1 | `18492e0931b7`  |
| 2134   | Layout 1 | `18492e0931b7`  |
| 2130   | Layout 1 | `18492e0931b7`  |
| 2122   | Layout 1 | `18492e0931b7`  |
| 2107   | Layout 1 | `18492e0931b7`  |
| 2098   | Layout 1 | `18492e0931b7`  |
| 2089   | Layout 1 | `18492e0931b7`  |
| 2081   | Layout 1 | `18492e0931b7`  |
| 2073   | Layout 1 | `18492e0931b7`  |
| 2067   | Layout 1 | `18492e0931b7`  |
| 2063   | Layout 1 | `18492e0931b7`  |
| 2059   | Layout 1 | `18492e0931b7`  |
| 2052   | Layout 1 | `18492e0931b7`  |
| 2044   | Layout 1 | `18492e0931b7`  |
| 2039   | Layout 1 | `18492e0931b7`  |
| 2032   | Layout 1 | `18492e0931b7`  |
| 2025   | Layout 1 | `18492e0931b7`  |
| 2011   | Layout 1 | `18492e0931b7`  |
| 2005   | Layout 1 | `18492e0931b7`  |
| 2000   | Layout 1 | `18492e0931b7`  |
| 1996   | Layout 1 | `18492e0931b7`  |
| 1991   | Layout 1 | `18492e0931b7`  |
| 1985   | Layout 1 | `18492e0931b7`  |
| 1980   | Layout 1 | `18492e0931b7`  |
| 1969   | Layout 1 | `18492e0931b7`  |
| 1964   | Layout 1 | `18492e0931b7`  |
| 1958   | Layout 1 | `18492e0931b7`  |
| 1950   | Layout 1 | `18492e0931b7`  |
| 1945   | Layout 1 | `18492e0931b7`  |
| 1937   | Layout 1 | `18492e0931b7`  |
| 1933   | Layout 1 | `18492e0931b7`  |
| 1927   | Layout 1 | `18492e0931b7`  |
| 1921   | Layout 1 | `18492e0931b7`  |
| 1914   | Layout 1 | `18492e0931b7`  |
| 1908   | No file  | `18492e0931b7`  |
| 1897   | No file  | `18492e0931b7`  |
| 1892   | No file  | `18492e0931b7`  |
| 1886   | No file  | `18492e0931b7`  |
| 1881   | No file  | `18492e0931b7`  |
| 1871   | No file  | `18492e0931b7`  |
| 1866   | No file  | `18492e0931b7`  |
| 1862   | No file  | `18492e0931b7`  |
| 1854   | No file  | `18492e0931b7`  |
| 1846   | No file  | `18492e0931b7`  |
| 1838   | No file  | `18492e0931b7`  |
| 1832   | No file  | `18492e0931b7`  |
| 1826   | No file  | `18492e0931b7`  |
| 1822   | No file  | `18492e0931b7`  |
| 1818   | No file  | `18492e0931b7`  |
| 1804   | No file  | `18492e0931b7`  |
| 1794   | No file  | `18492e0931b7`  |
| 1790   | No file  | `18492e0931b7`  |
| 1784   | No file  | `18492e0931b7`  |
| 1774   | No file  | `18492e0931b7`  |
| 1771   | No file  | `18492e0931b7`  |
| 1762   | No file  | `18492e0931b7`  |
| 1759   | No file  | `18492e0931b7`  |
| 1754   | No file  | `18492e0931b7`  |
| 1749   | No file  | `18492e0931b7`  |
| 1743   | No file  | `18492e0931b7`  |
| 1737   | No file  | `18492e0931b7`  |
| 1731   | No file  | `18492e0931b7`  |
| 1725   | No file  | `18492e0931b7`  |
| 1717   | No file  | `18492e0931b7`  |
| 1710   | No file  | `18492e0931b7`  |
| 1704   | No file  | `18492e0931b7`  |
| 1698   | No file  | `18492e0931b7`  |
| 1690   | No file  | `18492e0931b7`  |
| 1685   | No file  | `18492e0931b7`  |
| 1680   | No file  | `18492e0931b7`  |
| 1674   | No file  | `18492e0931b7`  |
| 1668   | No file  | `18492e0931b7`  |
| 1659   | No file  | `18492e0931b7`  |
| 1649   | No file  | `18492e0931b7`  |
| 1642   | No file  | `18492e0931b7`  |
| 1636   | No file  | `18492e0931b7`  |
| 1628   | No file  | `18492e0931b7`  |
| 1622   | No file  | `18492e0931b7`  |
| 1614   | No file  | `18492e0931b7`  |
| 1608   | No file  | `18492e0931b7`  |
| 1602   | No file  | `18492e0931b7`  |
| 1598   | No file  | `18492e0931b7`  |
| 1594   | No file  | `18492e0931b7`  |
| 1590   | No file  | `18492e0931b7`  |
| 1587   | No file  | `18492e0931b7`  |
| 1584   | No file  | `18492e0931b7`  |
| 1579   | No file  | `18492e0931b7`  |
| 1572   | No file  | `18492e0931b7`  |
| 1565   | No file  | `18492e0931b7`  |
| 1559   | No file  | `18492e0931b7`  |
| 1554   | No file  | `18492e0931b7`  |
| 1547   | No file  | `18492e0931b7`  |
| 1537   | No file  | `18492e0931b7`  |
| 1529   | No file  | `18492e0931b7`  |
| 1524   | No file  | `18492e0931b7`  |
| 1519   | No file  | `18492e0931b7`  |
| 1509   | No file  | `18492e0931b7`  |
| 1506   | No file  | `18492e0931b7`  |
| 1504   | No file  | `18492e0931b7`  |
| 1500   | No file  | `18492e0931b7`  |
| 1493   | No file  | `18492e0931b7`  |
| 1489   | No file  | `18492e0931b7`  |
| 1485   | No file  | `18492e0931b7`  |
| 1481   | No file  | `18492e0931b7`  |
| 1474   | No file  | `18492e0931b7`  |
| 1466   | No file  | `18492e0931b7`  |
| 1462   | No file  | `18492e0931b7`  |
| 1459   | No file  | `18492e0931b7`  |
| 1453   | No file  | `18492e0931b7`  |
| 1450   | No file  | `18492e0931b7`  |
| 1445   | No file  | `18492e0931b7`  |
| 1439   | No file  | `18492e0931b7`  |
| 1433   | No file  | `18492e0931b7`  |
| 1430   | No file  | `18492e0931b7`  |
| 1426   | No file  | `18492e0931b7`  |
| 1421   | No file  | `18492e0931b7`  |
| 1417   | No file  | `18492e0931b7`  |
| 1416   | No file  | `18492e0931b7`  |
| 1409   | No file  | `18492e0931b7`  |
| 1405   | No file  | `18492e0931b7`  |
| 1401   | No file  | `18492e0931b7`  |
| 1396   | No file  | `18492e0931b7`  |
| 1391   | No file  | `18492e0931b7`  |
| 1390   | No file  | `18492e0931b7`  |
| 1386   | No file  | `18492e0931b7`  |
| 1381   | No file  | `18492e0931b7`  |
| 1379   | No file  | `18492e0931b7`  |
| 1372   | No file  | `18492e0931b7`  |
| 1366   | No file  | `18492e0931b7`  |
| 1364   | No file  | `18492e0931b7`  |
| 1363   | No file  | `18492e0931b7`  |
| 1360   | No file  | `18492e0931b7`  |
| 1358   | No file  | `18492e0931b7`  |
| 1355   | No file  | `18492e0931b7`  |
| 1351   | No file  | `18492e0931b7`  |
| 1348   | No file  | `18492e0931b7`  |
| 1346   | No file  | `18492e0931b7`  |
| 1341   | No file  | `18492e0931b7`  |
| 1340   | No file  | `18492e0931b7`  |
| 1338   | No file  | `18492e0931b7`  |
| 1335   | No file  | `18492e0931b7`  |
| 1333   | No file  | `18492e0931b7`  |
| 1329   | No file  | `18492e0931b7`  |
| 1327   | No file  | `18492e0931b7`  |
| 1324   | No file  | `18492e0931b7`  |
| 1321   | No file  | `18492e0931b7`  |
| 1319   | No file  | `18492e0931b7`  |
| 1318   | No file  | `18492e0931b7`  |
| 1316   | No file  | `18492e0931b7`  |
| 1313   | No file  | `18492e0931b7`  |
| 1311   | No file  | `18492e0931b7`  |
| 1309   | No file  | `18492e0931b7`  |
| 1304   | No file  | `18492e0931b7`  |
| 1292   | No file  | `18492e0931b7`  |
| 1286   | No file  | `18492e0931b7`  |
| 1280   | No file  | `18492e0931b7`  |
| 1276   | No file  | `18492e0931b7`  |
| 1267   | No file  | `18492e0931b7`  |
| 1261   | No file  | `18492e0931b7`  |
| 1256   | No file  | `18492e0931b7`  |
| 1250   | No file  | `18492e0931b7`  |
| 1246   | No file  | `18492e0931b7`  |
| 1239   | No file  | `18492e0931b7`  |
| 1230   | No file  | `18492e0931b7`  |
| 1226   | No file  | `18492e0931b7`  |
| 1220   | No file  | `18492e0931b7`  |
| 1217   | No file  | `18492e0931b7`  |
| 1211   | No file  | `18492e0931b7`  |
| 1210   | No file  | `18492e0931b7`  |
| 1208   | No file  | `18492e0931b7`  |
| 1203   | No file  | `18492e0931b7`  |
| 1197   | No file  | `18492e0931b7`  |
| 1194   | No file  | `18492e0931b7`  |
| 1192   | No file  | `18492e0931b7`  |
| 1187   | No file  | `18492e0931b7`  |
| 1183   | No file  | `18492e0931b7`  |
| 1177   | No file  | `18492e0931b7`  |
| 1173   | No file  | `18492e0931b7`  |
| 1167   | No file  | `18492e0931b7`  |
| 1164   | No file  | `18492e0931b7`  |
| 1156   | No file  | `18492e0931b7`  |
| 1149   | No file  | `18492e0931b7`  |
| 1144   | No file  | `18492e0931b7`  |
| 1137   | No file  | `18492e0931b7`  |
| 1132   | No file  | `18492e0931b7`  |
| 1127   | No file  | `18492e0931b7`  |
| 1122   | No file  | `18492e0931b7`  |
| 1118   | No file  | `18492e0931b7`  |
| 1114   | No file  | `18492e0931b7`  |
| 1109   | No file  | `18492e0931b7`  |
| 1102   | No file  | `18492e0931b7`  |
| 1096   | No file  | `18492e0931b7`  |
| 1088   | No file  | `18492e0931b7`  |
| 1081   | No file  | `18492e0931b7`  |
| 1076   | No file  | `18492e0931b7`  |
| 1069   | No file  | `18492e0931b7`  |
| 1064   | No file  | `18492e0931b7`  |
| 1058   | No file  | `18492e0931b7`  |
| 1051   | No file  | `18492e0931b7`  |
| 1044   | No file  | `18492e0931b7`  |
| 1036   | No file  | `18492e0931b7`  |
| 1026   | No file  | `18492e0931b7`  |
| 1016   | No file  | `18492e0931b7`  |
| 1009   | No file  | `18492e0931b7`  |
| 1005   | No file  | `18492e0931b7`  |
| 1000   | No file  | `18492e0931b7`  |
| 998    | No file  | `18492e0931b7`  |
| 990    | No file  | `18492e0931b7`  |
| 979    | No file  | `18492e0931b7`  |
| 972    | No file  | `18492e0931b7`  |
| 963    | No file  | `18492e0931b7`  |
| 955    | No file  | `18492e0931b7`  |
| 946    | No file  | `18492e0931b7`  |
| 938    | No file  | `18492e0931b7`  |
| 927    | No file  | `18492e0931b7`  |
| 911    | No file  | `18492e0931b7`  |
| 904    | No file  | `18492e0931b7`  |
| 899    | No file  | `18492e0931b7`  |
| 894    | No file  | `18492e0931b7`  |
| 885    | No file  | `18492e0931b7`  |
| 879    | No file  | `18492e0931b7`  |
| 872    | No file  | `18492e0931b7`  |
| 864    | No file  | `18492e0931b7`  |
| 855    | No file  | `18492e0931b7`  |
| 853    | No file  | `18492e0931b7`  |
| 845    | No file  | `18492e0931b7`  |
| 837    | No file  | `18492e0931b7`  |
| 829    | No file  | `18492e0931b7`  |
| 822    | No file  | `18492e0931b7`  |
| 814    | No file  | `18492e0931b7`  |
| 805    | No file  | `18492e0931b7`  |
| 794    | No file  | `18492e0931b7`  |
| 787    | No file  | `18492e0931b7`  |
| 780    | No file  | `18492e0931b7`  |
| 771    | No file  | `18492e0931b7`  |
| 760    | No file  | `18492e0931b7`  |
| 748    | No file  | `18492e0931b7`  |
| 741    | No file  | `18492e0931b7`  |
| 736    | No file  | `18492e0931b7`  |
| 731    | No file  | `18492e0931b7`  |
| 723    | No file  | `18492e0931b7`  |
| 711    | No file  | `18492e0931b7`  |
| 707    | No file  | `18492e0931b7`  |
| 697    | No file  | `18492e0931b7`  |
| 689    | No file  | `18492e0931b7`  |
| 683    | No file  | `18492e0931b7`  |
| 678    | No file  | `18492e0931b7`  |
| 670    | No file  | `18492e0931b7`  |
| 661    | No file  | `18492e0931b7`  |
| 656    | No file  | `18492e0931b7`  |
| 652    | No file  | `18492e0931b7`  |
| 643    | No file  | `18492e0931b7`  |
| 637    | No file  | `18492e0931b7`  |
| 630    | No file  | `18492e0931b7`  |
| 627    | No file  | `18492e0931b7`  |
| 621    | No file  | `18492e0931b7`  |
| 617    | No file  | `18492e0931b7`  |
| 615    | No file  | `18492e0931b7`  |
| 606    | No file  | `18492e0931b7`  |
| 599    | No file  | `18492e0931b7`  |
| 592    | No file  | `18492e0931b7`  |
| 586    | No file  | `18492e0931b7`  |
| 577    | No file  | `18492e0931b7`  |
| 569    | No file  | `18492e0931b7`  |
| 561    | No file  | `18492e0931b7`  |
| 554    | No file  | `18492e0931b7`  |
| 542    | No file  | `18492e0931b7`  |
| 532    | No file  | `18492e0931b7`  |
| 531    | No file  | `18492e0931b7`  |
| 526    | No file  | `18492e0931b7`  |
| 521    | No file  | `18492e0931b7`  |
| 517    | No file  | `18492e0931b7`  |
| 510    | No file  | `18492e0931b7`  |
| 508    | No file  | `18492e0931b7`  |
| 504    | No file  | `18492e0931b7`  |
| 497    | No file  | `18492e0931b7`  |
| 491    | No file  | `18492e0931b7`  |
| 485    | No file  | `18492e0931b7`  |
| 478    | No file  | `18492e0931b7`  |
| 472    | No file  | `18492e0931b7`  |
| 466    | No file  | `18492e0931b7`  |
| 457    | No file  | `18492e0931b7`  |
| 452    | No file  | `18492e0931b7`  |
| 449    | No file  | `18492e0931b7`  |
| 435    | No file  | `18492e0931b7`  |

<!-- versions:end -->

## Companion Files

| File                        | Required | Role                                                    |
| --------------------------- | -------- | ------------------------------------------------------- |
| `languagedata_en.loc`       | Optional | Territory names (12)                                    |
| `texturestring_combine.xml` | Optional | Sprite sheet and rectangle of the tab icon, `<key>_Normal` |

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR block of fixed 10-byte rows, followed by the same counted string table
and 8-byte trailer as [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). The string table holds only the tab icon names.

| Offset              | Type           | Field              | Notes                             |
| ------------------- | -------------- | ------------------ | --------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                      |
| `+0x04`             | u32            | count              | Number of rows; 13 on client 3464 |
| `+0x08`             | Tab Row[count] | rows               | See Tab Row                       |
| `rows+0x00`         | String Table   | string_table       | 13 wide strings, one icon per row |
| `string_table+0x00` | u32            | string_table_start | Where the rows end                |
| `string_table+0x04` | u32            | zero               | Always `0`                        |

### Tab Row (10 bytes)

| Offset  | Type | Field         | Notes                                                           |
| ------- | ---- | ------------- | --------------------------------------------------------------- |
| `+0x00` | u32  | key           | Region tab, 1 to 13; `main_category_key` in the hunting grounds |
| `+0x04` | u16  | territory_key | LOC type 12 `str_id1`; `str_id4` 1 is the tab name              |
| `+0x06` | u32  | icon_ref      | String table index of the tab icon's texture key                |

| Key | Territory | Name                       | Icon                               |
| --- | --------- | -------------------------- | ---------------------------------- |
| 1   | 0         | Balenos                    | `Combine_Etc_DropItem_Icon_Tab_04` |
| 2   | 1         | Serendia                   | `Combine_Etc_DropItem_Icon_Tab_02` |
| 3   | 2         | Calpheon                   | `Combine_Etc_DropItem_Icon_Tab_01` |
| 4   | 3         | Mediah                     | `Combine_Etc_DropItem_Icon_Tab_03` |
| 5   | 4         | Valencia                   | `Combine_Etc_DropItem_Icon_Tab_05` |
| 6   | 6         | Kamasylvia                 | `Combine_Etc_DropItem_Icon_Tab_06` |
| 7   | 7         | Drieghan                   | `Combine_Etc_DropItem_Icon_Tab_07` |
| 8   | 8         | O'dyllita                  | `Combine_Etc_DropItem_Icon_Tab_08` |
| 9   | 9         | Mountain of Eternal Winter | `Combine_Etc_DropItem_Icon_Tab_09` |
| 10  | 11        | Ulukita                    | `Combine_Etc_DropItem_Icon_Tab_11` |
| 11  | 10        | Land of the Morning Light  | `Combine_Etc_DropItem_Icon_Tab_10` |
| 12  | 12        | Outer Edania               | `Combine_Etc_DropItem_Icon_Tab_12` |
| 13  | 13        | Inner Edania               | `Combine_Etc_DropItem_Icon_Tab_16` |

The Great Ocean (territory 5) has no tab, and tabs 10 and 11 swap the
territory order.

The icon is a texture key without the button state: the drop window adds
`_Normal`, `_Over` or `_Click` to it (`panel_window_renewdropitem_all_1.luac`),
and only those three keys are in `texturestring_combine.xml`.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Notes

- LOC type 12 `str_id4` 0 is the territory's own name and can differ from the
  tab name: territories 12 and 13 are both `Alyaelli` there, and `Outer
  Edania` / `Inner Edania` only in `str_id4` 1.
- The [`dropuihuntinggroundinfo.bss`](dropuihuntinggroundinfo_bss.md)
  handler loads this file as an optional companion and keeps only key ->
  territory.
