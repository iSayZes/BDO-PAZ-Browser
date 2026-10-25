# `abyssoneaudioinfo.bss` Format

## Purpose

The background music and ambience of the Abyss One (The Magnus) fields: per
`fieldinfo.bss` field (`A1_001` to `A1_065`) the four Wwise `BGM` states
it plays and its ambience index, the same pair of values
[`audioinfo.bss`](audioinfo_bss.md) holds per area colour of the world.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ----------------------- | ----- | ------- | --------- |
| 1      | 2000 and later | `abyssoneaudioinfo.bss` | 1,988 | 49 Row  | 22        |

| Layout | File                    | Known            | Unknown    |
| ------ | ----------------------- | ---------------- | ---------- |
| 1      | `abyssoneaudioinfo.bss` | 1,988 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `4bea84d3448f`  |
| 3482   | Layout 1 | `4bea84d3448f`  |
| 3474   | Layout 1 | `4bea84d3448f`  |
| 3473   | Layout 1 | `4bea84d3448f`  |
| 3464   | Layout 1 | `4bea84d3448f`  |
| 3458   | Layout 1 | `4bea84d3448f`  |
| 3454   | Layout 1 | `4bea84d3448f`  |
| 3444   | Layout 1 | `4bea84d3448f`  |
| 3435   | Layout 1 | `4bea84d3448f`  |
| 3426   | Layout 1 | `4bea84d3448f`  |
| 3418   | Layout 1 | `4bea84d3448f`  |
| 3412   | Layout 1 | `4bea84d3448f`  |
| 3402   | Layout 1 | `4bea84d3448f`  |
| 3396   | Layout 1 | `4bea84d3448f`  |
| 3387   | Layout 1 | `4bea84d3448f`  |
| 3381   | Layout 1 | `4bea84d3448f`  |
| 3373   | Layout 1 | `4bea84d3448f`  |
| 3364   | Layout 1 | `4bea84d3448f`  |
| 3356   | Layout 1 | `4bea84d3448f`  |
| 3349   | Layout 1 | `4bea84d3448f`  |
| 3342   | Layout 1 | `4bea84d3448f`  |
| 3335   | Layout 1 | `4bea84d3448f`  |
| 3326   | Layout 1 | `4bea84d3448f`  |
| 3321   | Layout 1 | `4bea84d3448f`  |
| 3314   | Layout 1 | `4bea84d3448f`  |
| 3303   | Layout 1 | `4bea84d3448f`  |
| 3302   | Layout 1 | `4bea84d3448f`  |
| 3293   | Layout 1 | `4bea84d3448f`  |
| 3283   | Layout 1 | `4bea84d3448f`  |
| 3275   | Layout 1 | `4bea84d3448f`  |
| 3267   | Layout 1 | `4bea84d3448f`  |
| 3258   | Layout 1 | `4bea84d3448f`  |
| 3251   | Layout 1 | `4bea84d3448f`  |
| 3242   | Layout 1 | `4bea84d3448f`  |
| 3235   | Layout 1 | `4bea84d3448f`  |
| 3229   | Layout 1 | `4bea84d3448f`  |
| 3212   | Layout 1 | `4bea84d3448f`  |
| 3203   | Layout 1 | `4bea84d3448f`  |
| 3193   | Layout 1 | `4bea84d3448f`  |
| 3186   | Layout 1 | `4bea84d3448f`  |
| 3177   | Layout 1 | `4bea84d3448f`  |
| 3169   | Layout 1 | `4bea84d3448f`  |
| 3158   | Layout 1 | `4bea84d3448f`  |
| 3151   | Layout 1 | `4bea84d3448f`  |
| 3144   | Layout 1 | `4bea84d3448f`  |
| 3133   | Layout 1 | `4bea84d3448f`  |
| 3125   | Layout 1 | `4bea84d3448f`  |
| 3118   | Layout 1 | `4bea84d3448f`  |
| 3111   | Layout 1 | `4bea84d3448f`  |
| 3103   | Layout 1 | `4bea84d3448f`  |
| 3095   | Layout 1 | `4bea84d3448f`  |
| 3086   | Layout 1 | `4bea84d3448f`  |
| 3072   | Layout 1 | `4bea84d3448f`  |
| 3062   | Layout 1 | `4bea84d3448f`  |
| 3052   | Layout 1 | `4bea84d3448f`  |
| 3045   | Layout 1 | `4bea84d3448f`  |
| 3037   | Layout 1 | `4bea84d3448f`  |
| 3030   | Layout 1 | `4bea84d3448f`  |
| 3021   | Layout 1 | `4bea84d3448f`  |
| 3012   | Layout 1 | `4bea84d3448f`  |
| 3002   | Layout 1 | `4bea84d3448f`  |
| 2995   | Layout 1 | `4bea84d3448f`  |
| 2987   | Layout 1 | `4bea84d3448f`  |
| 2978   | Layout 1 | `4bea84d3448f`  |
| 2970   | Layout 1 | `4bea84d3448f`  |
| 2959   | Layout 1 | `4bea84d3448f`  |
| 2951   | Layout 1 | `4bea84d3448f`  |
| 2942   | Layout 1 | `4bea84d3448f`  |
| 2935   | Layout 1 | `4bea84d3448f`  |
| 2932   | Layout 1 | `4bea84d3448f`  |
| 2923   | Layout 1 | `4bea84d3448f`  |
| 2919   | Layout 1 | `4bea84d3448f`  |
| 2907   | Layout 1 | `4bea84d3448f`  |
| 2900   | Layout 1 | `4bea84d3448f`  |
| 2891   | Layout 1 | `4bea84d3448f`  |
| 2882   | Layout 1 | `4bea84d3448f`  |
| 2872   | Layout 1 | `4bea84d3448f`  |
| 2863   | Layout 1 | `4bea84d3448f`  |
| 2855   | Layout 1 | `4bea84d3448f`  |
| 2849   | Layout 1 | `4bea84d3448f`  |
| 2844   | Layout 1 | `4bea84d3448f`  |
| 2834   | Layout 1 | `4bea84d3448f`  |
| 2825   | Layout 1 | `4bea84d3448f`  |
| 2819   | Layout 1 | `4bea84d3448f`  |
| 2811   | Layout 1 | `4bea84d3448f`  |
| 2803   | Layout 1 | `4bea84d3448f`  |
| 2794   | Layout 1 | `4bea84d3448f`  |
| 2783   | Layout 1 | `4bea84d3448f`  |
| 2774   | Layout 1 | `4bea84d3448f`  |
| 2765   | Layout 1 | `4bea84d3448f`  |
| 2756   | Layout 1 | `4bea84d3448f`  |
| 2750   | Layout 1 | `4bea84d3448f`  |
| 2743   | Layout 1 | `4bea84d3448f`  |
| 2736   | Layout 1 | `4bea84d3448f`  |
| 2726   | Layout 1 | `4bea84d3448f`  |
| 2717   | Layout 1 | `4bea84d3448f`  |
| 2709   | Layout 1 | `4bea84d3448f`  |
| 2703   | Layout 1 | `4bea84d3448f`  |
| 2695   | Layout 1 | `4bea84d3448f`  |
| 2684   | Layout 1 | `4bea84d3448f`  |
| 2672   | Layout 1 | `4bea84d3448f`  |
| 2665   | Layout 1 | `4bea84d3448f`  |
| 2657   | Layout 1 | `4bea84d3448f`  |
| 2649   | Layout 1 | `4bea84d3448f`  |
| 2644   | Layout 1 | `4bea84d3448f`  |
| 2637   | Layout 1 | `4bea84d3448f`  |
| 2629   | Layout 1 | `4bea84d3448f`  |
| 2619   | Layout 1 | `4bea84d3448f`  |
| 2612   | Layout 1 | `4bea84d3448f`  |
| 2606   | Layout 1 | `4bea84d3448f`  |
| 2602   | Layout 1 | `4bea84d3448f`  |
| 2601   | Layout 1 | `4bea84d3448f`  |
| 2592   | Layout 1 | `4bea84d3448f`  |
| 2583   | Layout 1 | `4bea84d3448f`  |
| 2575   | Layout 1 | `4bea84d3448f`  |
| 2567   | Layout 1 | `4bea84d3448f`  |
| 2560   | Layout 1 | `4bea84d3448f`  |
| 2553   | Layout 1 | `4bea84d3448f`  |
| 2545   | Layout 1 | `4bea84d3448f`  |
| 2538   | Layout 1 | `4bea84d3448f`  |
| 2529   | Layout 1 | `4bea84d3448f`  |
| 2519   | Layout 1 | `4bea84d3448f`  |
| 2513   | Layout 1 | `4bea84d3448f`  |
| 2510   | Layout 1 | `4bea84d3448f`  |
| 2507   | Layout 1 | `4bea84d3448f`  |
| 2503   | Layout 1 | `4bea84d3448f`  |
| 2498   | Layout 1 | `4bea84d3448f`  |
| 2492   | Layout 1 | `4bea84d3448f`  |
| 2487   | Layout 1 | `4bea84d3448f`  |
| 2480   | Layout 1 | `4bea84d3448f`  |
| 2474   | Layout 1 | `4bea84d3448f`  |
| 2468   | Layout 1 | `4bea84d3448f`  |
| 2460   | Layout 1 | `4bea84d3448f`  |
| 2453   | Layout 1 | `4bea84d3448f`  |
| 2444   | Layout 1 | `4bea84d3448f`  |
| 2438   | Layout 1 | `4bea84d3448f`  |
| 2434   | Layout 1 | `4bea84d3448f`  |
| 2429   | Layout 1 | `4bea84d3448f`  |
| 2421   | Layout 1 | `4bea84d3448f`  |
| 2414   | Layout 1 | `4bea84d3448f`  |
| 2407   | Layout 1 | `4bea84d3448f`  |
| 2401   | Layout 1 | `4bea84d3448f`  |
| 2397   | Layout 1 | `4bea84d3448f`  |
| 2393   | Layout 1 | `4bea84d3448f`  |
| 2384   | Layout 1 | `4bea84d3448f`  |
| 2378   | Layout 1 | `4bea84d3448f`  |
| 2372   | Layout 1 | `4bea84d3448f`  |
| 2358   | Layout 1 | `4bea84d3448f`  |
| 2352   | Layout 1 | `4bea84d3448f`  |
| 2347   | Layout 1 | `4bea84d3448f`  |
| 2343   | Layout 1 | `4bea84d3448f`  |
| 2335   | Layout 1 | `4bea84d3448f`  |
| 2327   | Layout 1 | `4bea84d3448f`  |
| 2324   | Layout 1 | `4bea84d3448f`  |
| 2319   | Layout 1 | `4bea84d3448f`  |
| 2313   | Layout 1 | `4bea84d3448f`  |
| 2308   | Layout 1 | `4bea84d3448f`  |
| 2302   | Layout 1 | `4bea84d3448f`  |
| 2295   | Layout 1 | `4bea84d3448f`  |
| 2290   | Layout 1 | `4bea84d3448f`  |
| 2284   | Layout 1 | `4bea84d3448f`  |
| 2276   | Layout 1 | `4bea84d3448f`  |
| 2269   | Layout 1 | `4bea84d3448f`  |
| 2259   | Layout 1 | `4bea84d3448f`  |
| 2250   | Layout 1 | `4bea84d3448f`  |
| 2243   | Layout 1 | `4bea84d3448f`  |
| 2235   | Layout 1 | `4bea84d3448f`  |
| 2229   | Layout 1 | `4bea84d3448f`  |
| 2224   | Layout 1 | `4bea84d3448f`  |
| 2218   | Layout 1 | `4bea84d3448f`  |
| 2215   | Layout 1 | `4bea84d3448f`  |
| 2207   | Layout 1 | `4bea84d3448f`  |
| 2203   | Layout 1 | `4bea84d3448f`  |
| 2196   | Layout 1 | `4bea84d3448f`  |
| 2192   | Layout 1 | `4bea84d3448f`  |
| 2189   | Layout 1 | `4bea84d3448f`  |
| 2183   | Layout 1 | `4bea84d3448f`  |
| 2179   | Layout 1 | `4bea84d3448f`  |
| 2171   | Layout 1 | `4bea84d3448f`  |
| 2163   | Layout 1 | `4bea84d3448f`  |
| 2156   | Layout 1 | `4bea84d3448f`  |
| 2151   | Layout 1 | `4bea84d3448f`  |
| 2147   | Layout 1 | `4bea84d3448f`  |
| 2142   | Layout 1 | `4bea84d3448f`  |
| 2138   | Layout 1 | `4bea84d3448f`  |
| 2134   | Layout 1 | `4bea84d3448f`  |
| 2130   | Layout 1 | `4bea84d3448f`  |
| 2122   | Layout 1 | `4bea84d3448f`  |
| 2107   | Layout 1 | `4bea84d3448f`  |
| 2098   | Layout 1 | `4bea84d3448f`  |
| 2089   | Layout 1 | `4bea84d3448f`  |
| 2081   | Layout 1 | `4bea84d3448f`  |
| 2073   | Layout 1 | `4bea84d3448f`  |
| 2067   | Layout 1 | `4bea84d3448f`  |
| 2063   | Layout 1 | `4bea84d3448f`  |
| 2059   | Layout 1 | `4bea84d3448f`  |
| 2052   | Layout 1 | `4bea84d3448f`  |
| 2044   | Layout 1 | `4bea84d3448f`  |
| 2039   | Layout 1 | `4bea84d3448f`  |
| 2032   | Layout 1 | `4bea84d3448f`  |
| 2025   | Layout 1 | `4bea84d3448f`  |
| 2011   | Layout 1 | `4bea84d3448f`  |
| 2005   | Layout 1 | `4bea84d3448f`  |
| 2000   | Layout 1 | `4bea84d3448f`  |
| 1996   | No file  | `4bea84d3448f`  |
| 1991   | No file  | `4bea84d3448f`  |
| 1985   | No file  | `4bea84d3448f`  |
| 1980   | No file  | `4bea84d3448f`  |
| 1969   | No file  | `4bea84d3448f`  |
| 1964   | No file  | `4bea84d3448f`  |
| 1958   | No file  | `4bea84d3448f`  |
| 1950   | No file  | `4bea84d3448f`  |
| 1945   | No file  | `4bea84d3448f`  |
| 1937   | No file  | `4bea84d3448f`  |
| 1933   | No file  | `4bea84d3448f`  |
| 1927   | No file  | `4bea84d3448f`  |
| 1921   | No file  | `4bea84d3448f`  |
| 1914   | No file  | `4bea84d3448f`  |
| 1908   | No file  | `4bea84d3448f`  |
| 1897   | No file  | `4bea84d3448f`  |
| 1892   | No file  | `4bea84d3448f`  |
| 1886   | No file  | `4bea84d3448f`  |
| 1881   | No file  | `4bea84d3448f`  |
| 1871   | No file  | `4bea84d3448f`  |
| 1866   | No file  | `4bea84d3448f`  |
| 1862   | No file  | `4bea84d3448f`  |
| 1854   | No file  | `4bea84d3448f`  |
| 1846   | No file  | `4bea84d3448f`  |
| 1838   | No file  | `4bea84d3448f`  |
| 1832   | No file  | `4bea84d3448f`  |
| 1826   | No file  | `4bea84d3448f`  |
| 1822   | No file  | `4bea84d3448f`  |
| 1818   | No file  | `4bea84d3448f`  |
| 1804   | No file  | `4bea84d3448f`  |
| 1794   | No file  | `4bea84d3448f`  |
| 1790   | No file  | `4bea84d3448f`  |
| 1784   | No file  | `4bea84d3448f`  |
| 1774   | No file  | `4bea84d3448f`  |
| 1771   | No file  | `4bea84d3448f`  |
| 1762   | No file  | `4bea84d3448f`  |
| 1759   | No file  | `4bea84d3448f`  |
| 1754   | No file  | `4bea84d3448f`  |
| 1749   | No file  | `4bea84d3448f`  |
| 1743   | No file  | `4bea84d3448f`  |
| 1737   | No file  | `4bea84d3448f`  |
| 1731   | No file  | `4bea84d3448f`  |
| 1725   | No file  | `4bea84d3448f`  |
| 1717   | No file  | `4bea84d3448f`  |
| 1710   | No file  | `4bea84d3448f`  |
| 1704   | No file  | `4bea84d3448f`  |
| 1698   | No file  | `4bea84d3448f`  |
| 1690   | No file  | `4bea84d3448f`  |
| 1685   | No file  | `4bea84d3448f`  |
| 1680   | No file  | `4bea84d3448f`  |
| 1674   | No file  | `4bea84d3448f`  |
| 1668   | No file  | `4bea84d3448f`  |
| 1659   | No file  | `4bea84d3448f`  |
| 1649   | No file  | `4bea84d3448f`  |
| 1642   | No file  | `4bea84d3448f`  |
| 1636   | No file  | `4bea84d3448f`  |
| 1628   | No file  | `4bea84d3448f`  |
| 1622   | No file  | `4bea84d3448f`  |
| 1614   | No file  | `4bea84d3448f`  |
| 1608   | No file  | `4bea84d3448f`  |
| 1602   | No file  | `4bea84d3448f`  |
| 1598   | No file  | `4bea84d3448f`  |
| 1594   | No file  | `4bea84d3448f`  |
| 1590   | No file  | `4bea84d3448f`  |
| 1587   | No file  | `4bea84d3448f`  |
| 1584   | No file  | `4bea84d3448f`  |
| 1579   | No file  | `4bea84d3448f`  |
| 1572   | No file  | `4bea84d3448f`  |
| 1565   | No file  | `4bea84d3448f`  |
| 1559   | No file  | `4bea84d3448f`  |
| 1554   | No file  | `4bea84d3448f`  |
| 1547   | No file  | `4bea84d3448f`  |
| 1537   | No file  | `4bea84d3448f`  |
| 1529   | No file  | `4bea84d3448f`  |
| 1524   | No file  | `4bea84d3448f`  |
| 1519   | No file  | `4bea84d3448f`  |
| 1509   | No file  | `4bea84d3448f`  |
| 1506   | No file  | `4bea84d3448f`  |
| 1504   | No file  | `4bea84d3448f`  |
| 1500   | No file  | `4bea84d3448f`  |
| 1493   | No file  | `4bea84d3448f`  |
| 1489   | No file  | `4bea84d3448f`  |
| 1485   | No file  | `4bea84d3448f`  |
| 1481   | No file  | `4bea84d3448f`  |
| 1474   | No file  | `4bea84d3448f`  |
| 1466   | No file  | `4bea84d3448f`  |
| 1462   | No file  | `4bea84d3448f`  |
| 1459   | No file  | `4bea84d3448f`  |
| 1453   | No file  | `4bea84d3448f`  |
| 1450   | No file  | `4bea84d3448f`  |
| 1445   | No file  | `4bea84d3448f`  |
| 1439   | No file  | `4bea84d3448f`  |
| 1433   | No file  | `4bea84d3448f`  |
| 1430   | No file  | `4bea84d3448f`  |
| 1426   | No file  | `4bea84d3448f`  |
| 1421   | No file  | `4bea84d3448f`  |
| 1417   | No file  | `4bea84d3448f`  |
| 1416   | No file  | `4bea84d3448f`  |
| 1409   | No file  | `4bea84d3448f`  |
| 1405   | No file  | `4bea84d3448f`  |
| 1401   | No file  | `4bea84d3448f`  |
| 1396   | No file  | `4bea84d3448f`  |
| 1391   | No file  | `4bea84d3448f`  |
| 1390   | No file  | `4bea84d3448f`  |
| 1386   | No file  | `4bea84d3448f`  |
| 1381   | No file  | `4bea84d3448f`  |
| 1379   | No file  | `4bea84d3448f`  |
| 1372   | No file  | `4bea84d3448f`  |
| 1366   | No file  | `4bea84d3448f`  |
| 1364   | No file  | `4bea84d3448f`  |
| 1363   | No file  | `4bea84d3448f`  |
| 1360   | No file  | `4bea84d3448f`  |
| 1358   | No file  | `4bea84d3448f`  |
| 1355   | No file  | `4bea84d3448f`  |
| 1351   | No file  | `4bea84d3448f`  |
| 1348   | No file  | `4bea84d3448f`  |
| 1346   | No file  | `4bea84d3448f`  |
| 1341   | No file  | `4bea84d3448f`  |
| 1340   | No file  | `4bea84d3448f`  |
| 1338   | No file  | `4bea84d3448f`  |
| 1335   | No file  | `4bea84d3448f`  |
| 1333   | No file  | `4bea84d3448f`  |
| 1329   | No file  | `4bea84d3448f`  |
| 1327   | No file  | `4bea84d3448f`  |
| 1324   | No file  | `4bea84d3448f`  |
| 1321   | No file  | `4bea84d3448f`  |
| 1319   | No file  | `4bea84d3448f`  |
| 1318   | No file  | `4bea84d3448f`  |
| 1316   | No file  | `4bea84d3448f`  |
| 1313   | No file  | `4bea84d3448f`  |
| 1311   | No file  | `4bea84d3448f`  |
| 1309   | No file  | `4bea84d3448f`  |
| 1304   | No file  | `4bea84d3448f`  |
| 1292   | No file  | `4bea84d3448f`  |
| 1286   | No file  | `4bea84d3448f`  |
| 1280   | No file  | `4bea84d3448f`  |
| 1276   | No file  | `4bea84d3448f`  |
| 1267   | No file  | `4bea84d3448f`  |
| 1261   | No file  | `4bea84d3448f`  |
| 1256   | No file  | `4bea84d3448f`  |
| 1250   | No file  | `4bea84d3448f`  |
| 1246   | No file  | `4bea84d3448f`  |
| 1239   | No file  | `4bea84d3448f`  |
| 1230   | No file  | `4bea84d3448f`  |
| 1226   | No file  | `4bea84d3448f`  |
| 1220   | No file  | `4bea84d3448f`  |
| 1217   | No file  | `4bea84d3448f`  |
| 1211   | No file  | `4bea84d3448f`  |
| 1210   | No file  | `4bea84d3448f`  |
| 1208   | No file  | `4bea84d3448f`  |
| 1203   | No file  | `4bea84d3448f`  |
| 1197   | No file  | `4bea84d3448f`  |
| 1194   | No file  | `4bea84d3448f`  |
| 1192   | No file  | `4bea84d3448f`  |
| 1187   | No file  | `4bea84d3448f`  |
| 1183   | No file  | `4bea84d3448f`  |
| 1177   | No file  | `4bea84d3448f`  |
| 1173   | No file  | `4bea84d3448f`  |
| 1167   | No file  | `4bea84d3448f`  |
| 1164   | No file  | `4bea84d3448f`  |
| 1156   | No file  | `4bea84d3448f`  |
| 1149   | No file  | `4bea84d3448f`  |
| 1144   | No file  | `4bea84d3448f`  |
| 1137   | No file  | `4bea84d3448f`  |
| 1132   | No file  | `4bea84d3448f`  |
| 1127   | No file  | `4bea84d3448f`  |
| 1122   | No file  | `4bea84d3448f`  |
| 1118   | No file  | `4bea84d3448f`  |
| 1114   | No file  | `4bea84d3448f`  |
| 1109   | No file  | `4bea84d3448f`  |
| 1102   | No file  | `4bea84d3448f`  |
| 1096   | No file  | `4bea84d3448f`  |
| 1088   | No file  | `4bea84d3448f`  |
| 1081   | No file  | `4bea84d3448f`  |
| 1076   | No file  | `4bea84d3448f`  |
| 1069   | No file  | `4bea84d3448f`  |
| 1064   | No file  | `4bea84d3448f`  |
| 1058   | No file  | `4bea84d3448f`  |
| 1051   | No file  | `4bea84d3448f`  |
| 1044   | No file  | `4bea84d3448f`  |
| 1036   | No file  | `4bea84d3448f`  |
| 1026   | No file  | `4bea84d3448f`  |
| 1016   | No file  | `4bea84d3448f`  |
| 1009   | No file  | `4bea84d3448f`  |
| 1005   | No file  | `4bea84d3448f`  |
| 1000   | No file  | `4bea84d3448f`  |
| 998    | No file  | `4bea84d3448f`  |
| 990    | No file  | `4bea84d3448f`  |
| 979    | No file  | `4bea84d3448f`  |
| 972    | No file  | `4bea84d3448f`  |
| 963    | No file  | `4bea84d3448f`  |
| 955    | No file  | `4bea84d3448f`  |
| 946    | No file  | `4bea84d3448f`  |
| 938    | No file  | `4bea84d3448f`  |
| 927    | No file  | `4bea84d3448f`  |
| 911    | No file  | `4bea84d3448f`  |
| 904    | No file  | `4bea84d3448f`  |
| 899    | No file  | `4bea84d3448f`  |
| 894    | No file  | `4bea84d3448f`  |
| 885    | No file  | `4bea84d3448f`  |
| 879    | No file  | `4bea84d3448f`  |
| 872    | No file  | `4bea84d3448f`  |
| 864    | No file  | `4bea84d3448f`  |
| 855    | No file  | `4bea84d3448f`  |
| 853    | No file  | `4bea84d3448f`  |
| 845    | No file  | `4bea84d3448f`  |
| 837    | No file  | `4bea84d3448f`  |
| 829    | No file  | `4bea84d3448f`  |
| 822    | No file  | `4bea84d3448f`  |
| 814    | No file  | `4bea84d3448f`  |
| 805    | No file  | `4bea84d3448f`  |
| 794    | No file  | `4bea84d3448f`  |
| 787    | No file  | `4bea84d3448f`  |
| 780    | No file  | `4bea84d3448f`  |
| 771    | No file  | `4bea84d3448f`  |
| 760    | No file  | `4bea84d3448f`  |
| 748    | No file  | `4bea84d3448f`  |
| 741    | No file  | `4bea84d3448f`  |
| 736    | No file  | `4bea84d3448f`  |
| 731    | No file  | `4bea84d3448f`  |
| 723    | No file  | `4bea84d3448f`  |
| 711    | No file  | `4bea84d3448f`  |
| 707    | No file  | `4bea84d3448f`  |
| 697    | No file  | `4bea84d3448f`  |
| 689    | No file  | `4bea84d3448f`  |
| 683    | No file  | `4bea84d3448f`  |
| 678    | No file  | `4bea84d3448f`  |
| 670    | No file  | `4bea84d3448f`  |
| 661    | No file  | `4bea84d3448f`  |
| 656    | No file  | `4bea84d3448f`  |
| 652    | No file  | `4bea84d3448f`  |
| 643    | No file  | `4bea84d3448f`  |
| 637    | No file  | `4bea84d3448f`  |
| 630    | No file  | `4bea84d3448f`  |
| 627    | No file  | `4bea84d3448f`  |
| 621    | No file  | `4bea84d3448f`  |
| 617    | No file  | `4bea84d3448f`  |
| 615    | No file  | `4bea84d3448f`  |
| 606    | No file  | `4bea84d3448f`  |
| 599    | No file  | `4bea84d3448f`  |
| 592    | No file  | `4bea84d3448f`  |
| 586    | No file  | `4bea84d3448f`  |
| 577    | No file  | `4bea84d3448f`  |
| 569    | No file  | `4bea84d3448f`  |
| 561    | No file  | `4bea84d3448f`  |
| 554    | No file  | `4bea84d3448f`  |
| 542    | No file  | `4bea84d3448f`  |
| 532    | No file  | `4bea84d3448f`  |
| 531    | No file  | `4bea84d3448f`  |
| 526    | No file  | `4bea84d3448f`  |
| 521    | No file  | `4bea84d3448f`  |
| 517    | No file  | `4bea84d3448f`  |
| 510    | No file  | `4bea84d3448f`  |
| 508    | No file  | `4bea84d3448f`  |
| 504    | No file  | `4bea84d3448f`  |
| 497    | No file  | `4bea84d3448f`  |
| 491    | No file  | `4bea84d3448f`  |
| 485    | No file  | `4bea84d3448f`  |
| 478    | No file  | `4bea84d3448f`  |
| 472    | No file  | `4bea84d3448f`  |
| 466    | No file  | `4bea84d3448f`  |
| 457    | No file  | `4bea84d3448f`  |
| 452    | No file  | `4bea84d3448f`  |
| 449    | No file  | `4bea84d3448f`  |
| 435    | No file  | `4bea84d3448f`  |

<!-- versions:end -->

## Companion Files

None. The handler names the field through the `fieldinfo.bss` field name
lookup.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of fields                              |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (22 bytes)

| Offset  | Type   | Field               | Notes                                                                                   |
| ------- | ------ | ------------------- | --------------------------------------------------------------------------------------- |
| `+0x00` | u16    | field_no            | A `fieldinfo.bss` field (`4001` `A1_001`); each key once, in no order                   |
| `+0x02` | u32[4] | bgm_states          | Indexes into `strings`: four Wwise `BGM` states; the four are one string on every row of client 3482 |
| `+0x12` | u32    | bank_no_environment | Ambience: the Wwise `ENV_INDEX_<n>` state (`201` to `208`, `12`, `13`, `43`, `0`)       |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                            |
| ------- | ------------------ | ------------ | ---------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                |
| `+0x04` | pstr[string_count] | strings      | State names, UTF-8 (`W11_AbyssOne_Quest_Idx062`, `W02_Ocean_Empty`); a string several rows use is stored once |

## Field Names

No sheet of the client 1784 `DataSheets.bexcel` and no table of the client
519 server data holds the file; client 2011 is the first test client that
has it. The names follow [`audioinfo.bss`](audioinfo_bss.md), whose Row
ends in the same four state indexes and ambience value:

- `field_no`: 49 of 49 keys are `fieldinfo.bss` fields, all named `A1_`
  (client 3482).
- `bgm_states`: 21 of the 34 strings are states of the `BGM` state group
  in `sound2022/wwise_ids.h`; the 13 `W<nn>_Ocean_Empty` names are in no
  state group (client 3482).
- `bank_no_environment`: 49 of 49 values are `ENV_INDEX_<n>` states of
  the same header (client 3482).

## Open Questions

### Ocean Empty States

The 13 `W<nn>_Ocean_Empty` names are not `BGM` states in
`sound2022/wwise_ids.h`. The client may fall back to silence for an
unknown state, which would make these fields play no music.
