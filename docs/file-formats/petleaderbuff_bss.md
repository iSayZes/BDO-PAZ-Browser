# `petleaderbuff.bss` Format

## Purpose

The alpha pet bonus per pet tier: how much an alpha pet ("Pack Leader")
cuts the loot cooldown of every active pet. The client reads it through
`ToClient_getPetLeaderBuff(tier)`. On client 3474 the file holds one entry,
tier `4` (Tier 5 in the game) with `150000`, which reads as 15% on the
client's 1,000,000 = 100% rate scale (see Notes). The file has
no PABR magic and no trailer.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------- | --------- |
| 1      | 1927 and later | 3483    | `petleaderbuff.bss` | 10    | 1 Entry | 6         |

| Layout | File                | Known       | Unknown     |
| ------ | ------------------- | ----------- | ----------- |
| 1      | `petleaderbuff.bss` | 9 B (90.0%) | 1 B (10.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a2cd64eacb51`  |
| 3482   | Layout 1 | `a2cd64eacb51`  |
| 3474   | Layout 1 | `a2cd64eacb51`  |
| 3473   | Layout 1 | `a2cd64eacb51`  |
| 3464   | Layout 1 | `a2cd64eacb51`  |
| 3458   | Layout 1 | `a2cd64eacb51`  |
| 3454   | Layout 1 | `a2cd64eacb51`  |
| 3444   | Layout 1 | `a2cd64eacb51`  |
| 3435   | Layout 1 | `a2cd64eacb51`  |
| 3426   | Layout 1 | `a2cd64eacb51`  |
| 3418   | Layout 1 | `a2cd64eacb51`  |
| 3412   | Layout 1 | `a2cd64eacb51`  |
| 3402   | Layout 1 | `a2cd64eacb51`  |
| 3396   | Layout 1 | `a2cd64eacb51`  |
| 3387   | Layout 1 | `a2cd64eacb51`  |
| 3381   | Layout 1 | `a2cd64eacb51`  |
| 3373   | Layout 1 | `a2cd64eacb51`  |
| 3364   | Layout 1 | `a2cd64eacb51`  |
| 3356   | Layout 1 | `a2cd64eacb51`  |
| 3349   | Layout 1 | `a2cd64eacb51`  |
| 3342   | Layout 1 | `a2cd64eacb51`  |
| 3335   | Layout 1 | `a2cd64eacb51`  |
| 3326   | Layout 1 | `a2cd64eacb51`  |
| 3321   | Layout 1 | `a2cd64eacb51`  |
| 3314   | Layout 1 | `a2cd64eacb51`  |
| 3303   | Layout 1 | `a2cd64eacb51`  |
| 3302   | Layout 1 | `a2cd64eacb51`  |
| 3293   | Layout 1 | `a2cd64eacb51`  |
| 3283   | Layout 1 | `a2cd64eacb51`  |
| 3275   | Layout 1 | `a2cd64eacb51`  |
| 3267   | Layout 1 | `a2cd64eacb51`  |
| 3258   | Layout 1 | `a2cd64eacb51`  |
| 3251   | Layout 1 | `a2cd64eacb51`  |
| 3242   | Layout 1 | `a2cd64eacb51`  |
| 3235   | Layout 1 | `a2cd64eacb51`  |
| 3229   | Layout 1 | `a2cd64eacb51`  |
| 3212   | Layout 1 | `a2cd64eacb51`  |
| 3203   | Layout 1 | `a2cd64eacb51`  |
| 3193   | Layout 1 | `a2cd64eacb51`  |
| 3186   | Layout 1 | `a2cd64eacb51`  |
| 3177   | Layout 1 | `a2cd64eacb51`  |
| 3169   | Layout 1 | `a2cd64eacb51`  |
| 3158   | Layout 1 | `a2cd64eacb51`  |
| 3151   | Layout 1 | `a2cd64eacb51`  |
| 3144   | Layout 1 | `a2cd64eacb51`  |
| 3133   | Layout 1 | `a2cd64eacb51`  |
| 3125   | Layout 1 | `a2cd64eacb51`  |
| 3118   | Layout 1 | `a2cd64eacb51`  |
| 3111   | Layout 1 | `a2cd64eacb51`  |
| 3103   | Layout 1 | `a2cd64eacb51`  |
| 3095   | Layout 1 | `a2cd64eacb51`  |
| 3086   | Layout 1 | `a2cd64eacb51`  |
| 3072   | Layout 1 | `a2cd64eacb51`  |
| 3062   | Layout 1 | `a2cd64eacb51`  |
| 3052   | Layout 1 | `a2cd64eacb51`  |
| 3045   | Layout 1 | `a2cd64eacb51`  |
| 3037   | Layout 1 | `a2cd64eacb51`  |
| 3030   | Layout 1 | `a2cd64eacb51`  |
| 3021   | Layout 1 | `a2cd64eacb51`  |
| 3012   | Layout 1 | `a2cd64eacb51`  |
| 3002   | Layout 1 | `a2cd64eacb51`  |
| 2995   | Layout 1 | `a2cd64eacb51`  |
| 2987   | Layout 1 | `a2cd64eacb51`  |
| 2978   | Layout 1 | `a2cd64eacb51`  |
| 2970   | Layout 1 | `a2cd64eacb51`  |
| 2959   | Layout 1 | `a2cd64eacb51`  |
| 2951   | Layout 1 | `a2cd64eacb51`  |
| 2942   | Layout 1 | `a2cd64eacb51`  |
| 2935   | Layout 1 | `a2cd64eacb51`  |
| 2932   | Layout 1 | `a2cd64eacb51`  |
| 2923   | Layout 1 | `a2cd64eacb51`  |
| 2919   | Layout 1 | `a2cd64eacb51`  |
| 2907   | Layout 1 | `a2cd64eacb51`  |
| 2900   | Layout 1 | `a2cd64eacb51`  |
| 2891   | Layout 1 | `a2cd64eacb51`  |
| 2882   | Layout 1 | `a2cd64eacb51`  |
| 2872   | Layout 1 | `a2cd64eacb51`  |
| 2863   | Layout 1 | `a2cd64eacb51`  |
| 2855   | Layout 1 | `a2cd64eacb51`  |
| 2849   | Layout 1 | `a2cd64eacb51`  |
| 2844   | Layout 1 | `a2cd64eacb51`  |
| 2834   | Layout 1 | `a2cd64eacb51`  |
| 2825   | Layout 1 | `a2cd64eacb51`  |
| 2819   | Layout 1 | `a2cd64eacb51`  |
| 2811   | Layout 1 | `a2cd64eacb51`  |
| 2803   | Layout 1 | `a2cd64eacb51`  |
| 2794   | Layout 1 | `a2cd64eacb51`  |
| 2783   | Layout 1 | `a2cd64eacb51`  |
| 2774   | Layout 1 | `a2cd64eacb51`  |
| 2765   | Layout 1 | `a2cd64eacb51`  |
| 2756   | Layout 1 | `a2cd64eacb51`  |
| 2750   | Layout 1 | `a2cd64eacb51`  |
| 2743   | Layout 1 | `a2cd64eacb51`  |
| 2736   | Layout 1 | `a2cd64eacb51`  |
| 2726   | Layout 1 | `a2cd64eacb51`  |
| 2717   | Layout 1 | `a2cd64eacb51`  |
| 2709   | Layout 1 | `a2cd64eacb51`  |
| 2703   | Layout 1 | `a2cd64eacb51`  |
| 2695   | Layout 1 | `a2cd64eacb51`  |
| 2684   | Layout 1 | `a2cd64eacb51`  |
| 2672   | Layout 1 | `a2cd64eacb51`  |
| 2665   | Layout 1 | `a2cd64eacb51`  |
| 2657   | Layout 1 | `a2cd64eacb51`  |
| 2649   | Layout 1 | `a2cd64eacb51`  |
| 2644   | Layout 1 | `a2cd64eacb51`  |
| 2637   | Layout 1 | `a2cd64eacb51`  |
| 2629   | Layout 1 | `a2cd64eacb51`  |
| 2619   | Layout 1 | `a2cd64eacb51`  |
| 2612   | Layout 1 | `a2cd64eacb51`  |
| 2606   | Layout 1 | `a2cd64eacb51`  |
| 2602   | Layout 1 | `a2cd64eacb51`  |
| 2601   | Layout 1 | `a2cd64eacb51`  |
| 2592   | Layout 1 | `a2cd64eacb51`  |
| 2583   | Layout 1 | `a2cd64eacb51`  |
| 2575   | Layout 1 | `a2cd64eacb51`  |
| 2567   | Layout 1 | `a2cd64eacb51`  |
| 2560   | Layout 1 | `a2cd64eacb51`  |
| 2553   | Layout 1 | `a2cd64eacb51`  |
| 2545   | Layout 1 | `a2cd64eacb51`  |
| 2538   | Layout 1 | `a2cd64eacb51`  |
| 2529   | Layout 1 | `a2cd64eacb51`  |
| 2519   | Layout 1 | `a2cd64eacb51`  |
| 2513   | Layout 1 | `a2cd64eacb51`  |
| 2510   | Layout 1 | `a2cd64eacb51`  |
| 2507   | Layout 1 | `a2cd64eacb51`  |
| 2503   | Layout 1 | `a2cd64eacb51`  |
| 2498   | Layout 1 | `a2cd64eacb51`  |
| 2492   | Layout 1 | `a2cd64eacb51`  |
| 2487   | Layout 1 | `a2cd64eacb51`  |
| 2480   | Layout 1 | `a2cd64eacb51`  |
| 2474   | Layout 1 | `a2cd64eacb51`  |
| 2468   | Layout 1 | `a2cd64eacb51`  |
| 2460   | Layout 1 | `a2cd64eacb51`  |
| 2453   | Layout 1 | `a2cd64eacb51`  |
| 2444   | Layout 1 | `a2cd64eacb51`  |
| 2438   | Layout 1 | `a2cd64eacb51`  |
| 2434   | Layout 1 | `a2cd64eacb51`  |
| 2429   | Layout 1 | `a2cd64eacb51`  |
| 2421   | Layout 1 | `a2cd64eacb51`  |
| 2414   | Layout 1 | `a2cd64eacb51`  |
| 2407   | Layout 1 | `a2cd64eacb51`  |
| 2401   | Layout 1 | `a2cd64eacb51`  |
| 2397   | Layout 1 | `a2cd64eacb51`  |
| 2393   | Layout 1 | `a2cd64eacb51`  |
| 2384   | Layout 1 | `a2cd64eacb51`  |
| 2378   | Layout 1 | `a2cd64eacb51`  |
| 2372   | Layout 1 | `a2cd64eacb51`  |
| 2358   | Layout 1 | `a2cd64eacb51`  |
| 2352   | Layout 1 | `a2cd64eacb51`  |
| 2347   | Layout 1 | `a2cd64eacb51`  |
| 2343   | Layout 1 | `a2cd64eacb51`  |
| 2335   | Layout 1 | `a2cd64eacb51`  |
| 2327   | Layout 1 | `a2cd64eacb51`  |
| 2324   | Layout 1 | `a2cd64eacb51`  |
| 2319   | Layout 1 | `a2cd64eacb51`  |
| 2313   | Layout 1 | `a2cd64eacb51`  |
| 2308   | Layout 1 | `a2cd64eacb51`  |
| 2302   | Layout 1 | `a2cd64eacb51`  |
| 2295   | Layout 1 | `a2cd64eacb51`  |
| 2290   | Layout 1 | `a2cd64eacb51`  |
| 2284   | Layout 1 | `a2cd64eacb51`  |
| 2276   | Layout 1 | `a2cd64eacb51`  |
| 2269   | Layout 1 | `a2cd64eacb51`  |
| 2259   | Layout 1 | `a2cd64eacb51`  |
| 2250   | Layout 1 | `a2cd64eacb51`  |
| 2243   | Layout 1 | `a2cd64eacb51`  |
| 2235   | Layout 1 | `a2cd64eacb51`  |
| 2229   | Layout 1 | `a2cd64eacb51`  |
| 2224   | Layout 1 | `a2cd64eacb51`  |
| 2218   | Layout 1 | `a2cd64eacb51`  |
| 2215   | Layout 1 | `a2cd64eacb51`  |
| 2207   | Layout 1 | `a2cd64eacb51`  |
| 2203   | Layout 1 | `a2cd64eacb51`  |
| 2196   | Layout 1 | `a2cd64eacb51`  |
| 2192   | Layout 1 | `a2cd64eacb51`  |
| 2189   | Layout 1 | `a2cd64eacb51`  |
| 2183   | Layout 1 | `a2cd64eacb51`  |
| 2179   | Layout 1 | `a2cd64eacb51`  |
| 2171   | Layout 1 | `a2cd64eacb51`  |
| 2163   | Layout 1 | `a2cd64eacb51`  |
| 2156   | Layout 1 | `a2cd64eacb51`  |
| 2151   | Layout 1 | `a2cd64eacb51`  |
| 2147   | Layout 1 | `a2cd64eacb51`  |
| 2142   | Layout 1 | `a2cd64eacb51`  |
| 2138   | Layout 1 | `a2cd64eacb51`  |
| 2134   | Layout 1 | `a2cd64eacb51`  |
| 2130   | Layout 1 | `a2cd64eacb51`  |
| 2122   | Layout 1 | `a2cd64eacb51`  |
| 2107   | Layout 1 | `a2cd64eacb51`  |
| 2098   | Layout 1 | `a2cd64eacb51`  |
| 2089   | Layout 1 | `a2cd64eacb51`  |
| 2081   | Layout 1 | `a2cd64eacb51`  |
| 2073   | Layout 1 | `a2cd64eacb51`  |
| 2067   | Layout 1 | `a2cd64eacb51`  |
| 2063   | Layout 1 | `a2cd64eacb51`  |
| 2059   | Layout 1 | `a2cd64eacb51`  |
| 2052   | Layout 1 | `a2cd64eacb51`  |
| 2044   | Layout 1 | `a2cd64eacb51`  |
| 2039   | Layout 1 | `a2cd64eacb51`  |
| 2032   | Layout 1 | `a2cd64eacb51`  |
| 2025   | Layout 1 | `a2cd64eacb51`  |
| 2011   | Layout 1 | `a2cd64eacb51`  |
| 2005   | Layout 1 | `a2cd64eacb51`  |
| 2000   | Layout 1 | `a2cd64eacb51`  |
| 1996   | Layout 1 | `a2cd64eacb51`  |
| 1991   | Layout 1 | `a2cd64eacb51`  |
| 1985   | Layout 1 | `a2cd64eacb51`  |
| 1980   | Layout 1 | `a2cd64eacb51`  |
| 1969   | Layout 1 | `a2cd64eacb51`  |
| 1964   | Layout 1 | `a2cd64eacb51`  |
| 1958   | Layout 1 | `a2cd64eacb51`  |
| 1950   | Layout 1 | `a2cd64eacb51`  |
| 1945   | Layout 1 | `a2cd64eacb51`  |
| 1937   | Layout 1 | `a2cd64eacb51`  |
| 1933   | Layout 1 | `a2cd64eacb51`  |
| 1927   | Layout 1 | `a2cd64eacb51`  |
| 1921   | No file  | `a2cd64eacb51`  |
| 1914   | No file  | `a2cd64eacb51`  |
| 1908   | No file  | `a2cd64eacb51`  |
| 1897   | No file  | `a2cd64eacb51`  |
| 1892   | No file  | `a2cd64eacb51`  |
| 1886   | No file  | `a2cd64eacb51`  |
| 1881   | No file  | `a2cd64eacb51`  |
| 1871   | No file  | `a2cd64eacb51`  |
| 1866   | No file  | `a2cd64eacb51`  |
| 1862   | No file  | `a2cd64eacb51`  |
| 1854   | No file  | `a2cd64eacb51`  |
| 1846   | No file  | `a2cd64eacb51`  |
| 1838   | No file  | `a2cd64eacb51`  |
| 1832   | No file  | `a2cd64eacb51`  |
| 1826   | No file  | `a2cd64eacb51`  |
| 1822   | No file  | `a2cd64eacb51`  |
| 1818   | No file  | `a2cd64eacb51`  |
| 1804   | No file  | `a2cd64eacb51`  |
| 1794   | No file  | `a2cd64eacb51`  |
| 1790   | No file  | `a2cd64eacb51`  |
| 1784   | No file  | `a2cd64eacb51`  |
| 1774   | No file  | `a2cd64eacb51`  |
| 1771   | No file  | `a2cd64eacb51`  |
| 1762   | No file  | `a2cd64eacb51`  |
| 1759   | No file  | `a2cd64eacb51`  |
| 1754   | No file  | `a2cd64eacb51`  |
| 1749   | No file  | `a2cd64eacb51`  |
| 1743   | No file  | `a2cd64eacb51`  |
| 1737   | No file  | `a2cd64eacb51`  |
| 1731   | No file  | `a2cd64eacb51`  |
| 1725   | No file  | `a2cd64eacb51`  |
| 1717   | No file  | `a2cd64eacb51`  |
| 1710   | No file  | `a2cd64eacb51`  |
| 1704   | No file  | `a2cd64eacb51`  |
| 1698   | No file  | `a2cd64eacb51`  |
| 1690   | No file  | `a2cd64eacb51`  |
| 1685   | No file  | `a2cd64eacb51`  |
| 1680   | No file  | `a2cd64eacb51`  |
| 1674   | No file  | `a2cd64eacb51`  |
| 1668   | No file  | `a2cd64eacb51`  |
| 1659   | No file  | `a2cd64eacb51`  |
| 1649   | No file  | `a2cd64eacb51`  |
| 1642   | No file  | `a2cd64eacb51`  |
| 1636   | No file  | `a2cd64eacb51`  |
| 1628   | No file  | `a2cd64eacb51`  |
| 1622   | No file  | `a2cd64eacb51`  |
| 1614   | No file  | `a2cd64eacb51`  |
| 1608   | No file  | `a2cd64eacb51`  |
| 1602   | No file  | `a2cd64eacb51`  |
| 1598   | No file  | `a2cd64eacb51`  |
| 1594   | No file  | `a2cd64eacb51`  |
| 1590   | No file  | `a2cd64eacb51`  |
| 1587   | No file  | `a2cd64eacb51`  |
| 1584   | No file  | `a2cd64eacb51`  |
| 1579   | No file  | `a2cd64eacb51`  |
| 1572   | No file  | `a2cd64eacb51`  |
| 1565   | No file  | `a2cd64eacb51`  |
| 1559   | No file  | `a2cd64eacb51`  |
| 1554   | No file  | `a2cd64eacb51`  |
| 1547   | No file  | `a2cd64eacb51`  |
| 1537   | No file  | `a2cd64eacb51`  |
| 1529   | No file  | `a2cd64eacb51`  |
| 1524   | No file  | `a2cd64eacb51`  |
| 1519   | No file  | `a2cd64eacb51`  |
| 1509   | No file  | `a2cd64eacb51`  |
| 1506   | No file  | `a2cd64eacb51`  |
| 1504   | No file  | `a2cd64eacb51`  |
| 1500   | No file  | `a2cd64eacb51`  |
| 1493   | No file  | `a2cd64eacb51`  |
| 1489   | No file  | `a2cd64eacb51`  |
| 1485   | No file  | `a2cd64eacb51`  |
| 1481   | No file  | `a2cd64eacb51`  |
| 1474   | No file  | `a2cd64eacb51`  |
| 1466   | No file  | `a2cd64eacb51`  |
| 1462   | No file  | `a2cd64eacb51`  |
| 1459   | No file  | `a2cd64eacb51`  |
| 1453   | No file  | `a2cd64eacb51`  |
| 1450   | No file  | `a2cd64eacb51`  |
| 1445   | No file  | `a2cd64eacb51`  |
| 1439   | No file  | `a2cd64eacb51`  |
| 1433   | No file  | `a2cd64eacb51`  |
| 1430   | No file  | `a2cd64eacb51`  |
| 1426   | No file  | `a2cd64eacb51`  |
| 1421   | No file  | `a2cd64eacb51`  |
| 1417   | No file  | `a2cd64eacb51`  |
| 1416   | No file  | `a2cd64eacb51`  |
| 1409   | No file  | `a2cd64eacb51`  |
| 1405   | No file  | `a2cd64eacb51`  |
| 1401   | No file  | `a2cd64eacb51`  |
| 1396   | No file  | `a2cd64eacb51`  |
| 1391   | No file  | `a2cd64eacb51`  |
| 1390   | No file  | `a2cd64eacb51`  |
| 1386   | No file  | `a2cd64eacb51`  |
| 1381   | No file  | `a2cd64eacb51`  |
| 1379   | No file  | `a2cd64eacb51`  |
| 1372   | No file  | `a2cd64eacb51`  |
| 1366   | No file  | `a2cd64eacb51`  |
| 1364   | No file  | `a2cd64eacb51`  |
| 1363   | No file  | `a2cd64eacb51`  |
| 1360   | No file  | `a2cd64eacb51`  |
| 1358   | No file  | `a2cd64eacb51`  |
| 1355   | No file  | `a2cd64eacb51`  |
| 1351   | No file  | `a2cd64eacb51`  |
| 1348   | No file  | `a2cd64eacb51`  |
| 1346   | No file  | `a2cd64eacb51`  |
| 1341   | No file  | `a2cd64eacb51`  |
| 1340   | No file  | `a2cd64eacb51`  |
| 1338   | No file  | `a2cd64eacb51`  |
| 1335   | No file  | `a2cd64eacb51`  |
| 1333   | No file  | `a2cd64eacb51`  |
| 1329   | No file  | `a2cd64eacb51`  |
| 1327   | No file  | `a2cd64eacb51`  |
| 1324   | No file  | `a2cd64eacb51`  |
| 1321   | No file  | `a2cd64eacb51`  |
| 1319   | No file  | `a2cd64eacb51`  |
| 1318   | No file  | `a2cd64eacb51`  |
| 1316   | No file  | `a2cd64eacb51`  |
| 1313   | No file  | `a2cd64eacb51`  |
| 1311   | No file  | `a2cd64eacb51`  |
| 1309   | No file  | `a2cd64eacb51`  |
| 1304   | No file  | `a2cd64eacb51`  |
| 1292   | No file  | `a2cd64eacb51`  |
| 1286   | No file  | `a2cd64eacb51`  |
| 1280   | No file  | `a2cd64eacb51`  |
| 1276   | No file  | `a2cd64eacb51`  |
| 1267   | No file  | `a2cd64eacb51`  |
| 1261   | No file  | `a2cd64eacb51`  |
| 1256   | No file  | `a2cd64eacb51`  |
| 1250   | No file  | `a2cd64eacb51`  |
| 1246   | No file  | `a2cd64eacb51`  |
| 1239   | No file  | `a2cd64eacb51`  |
| 1230   | No file  | `a2cd64eacb51`  |
| 1226   | No file  | `a2cd64eacb51`  |
| 1220   | No file  | `a2cd64eacb51`  |
| 1217   | No file  | `a2cd64eacb51`  |
| 1211   | No file  | `a2cd64eacb51`  |
| 1210   | No file  | `a2cd64eacb51`  |
| 1208   | No file  | `a2cd64eacb51`  |
| 1203   | No file  | `a2cd64eacb51`  |
| 1197   | No file  | `a2cd64eacb51`  |
| 1194   | No file  | `a2cd64eacb51`  |
| 1192   | No file  | `a2cd64eacb51`  |
| 1187   | No file  | `a2cd64eacb51`  |
| 1183   | No file  | `a2cd64eacb51`  |
| 1177   | No file  | `a2cd64eacb51`  |
| 1173   | No file  | `a2cd64eacb51`  |
| 1167   | No file  | `a2cd64eacb51`  |
| 1164   | No file  | `a2cd64eacb51`  |
| 1156   | No file  | `a2cd64eacb51`  |
| 1149   | No file  | `a2cd64eacb51`  |
| 1144   | No file  | `a2cd64eacb51`  |
| 1137   | No file  | `a2cd64eacb51`  |
| 1132   | No file  | `a2cd64eacb51`  |
| 1127   | No file  | `a2cd64eacb51`  |
| 1122   | No file  | `a2cd64eacb51`  |
| 1118   | No file  | `a2cd64eacb51`  |
| 1114   | No file  | `a2cd64eacb51`  |
| 1109   | No file  | `a2cd64eacb51`  |
| 1102   | No file  | `a2cd64eacb51`  |
| 1096   | No file  | `a2cd64eacb51`  |
| 1088   | No file  | `a2cd64eacb51`  |
| 1081   | No file  | `a2cd64eacb51`  |
| 1076   | No file  | `a2cd64eacb51`  |
| 1069   | No file  | `a2cd64eacb51`  |
| 1064   | No file  | `a2cd64eacb51`  |
| 1058   | No file  | `a2cd64eacb51`  |
| 1051   | No file  | `a2cd64eacb51`  |
| 1044   | No file  | `a2cd64eacb51`  |
| 1036   | No file  | `a2cd64eacb51`  |
| 1026   | No file  | `a2cd64eacb51`  |
| 1016   | No file  | `a2cd64eacb51`  |
| 1009   | No file  | `a2cd64eacb51`  |
| 1005   | No file  | `a2cd64eacb51`  |
| 1000   | No file  | `a2cd64eacb51`  |
| 998    | No file  | `a2cd64eacb51`  |
| 990    | No file  | `a2cd64eacb51`  |
| 979    | No file  | `a2cd64eacb51`  |
| 972    | No file  | `a2cd64eacb51`  |
| 963    | No file  | `a2cd64eacb51`  |
| 955    | No file  | `a2cd64eacb51`  |
| 946    | No file  | `a2cd64eacb51`  |
| 938    | No file  | `a2cd64eacb51`  |
| 927    | No file  | `a2cd64eacb51`  |
| 911    | No file  | `a2cd64eacb51`  |
| 904    | No file  | `a2cd64eacb51`  |
| 899    | No file  | `a2cd64eacb51`  |
| 894    | No file  | `a2cd64eacb51`  |
| 885    | No file  | `a2cd64eacb51`  |
| 879    | No file  | `a2cd64eacb51`  |
| 872    | No file  | `a2cd64eacb51`  |
| 864    | No file  | `a2cd64eacb51`  |
| 855    | No file  | `a2cd64eacb51`  |
| 853    | No file  | `a2cd64eacb51`  |
| 845    | No file  | `a2cd64eacb51`  |
| 837    | No file  | `a2cd64eacb51`  |
| 829    | No file  | `a2cd64eacb51`  |
| 822    | No file  | `a2cd64eacb51`  |
| 814    | No file  | `a2cd64eacb51`  |
| 805    | No file  | `a2cd64eacb51`  |
| 794    | No file  | `a2cd64eacb51`  |
| 787    | No file  | `a2cd64eacb51`  |
| 780    | No file  | `a2cd64eacb51`  |
| 771    | No file  | `a2cd64eacb51`  |
| 760    | No file  | `a2cd64eacb51`  |
| 748    | No file  | `a2cd64eacb51`  |
| 741    | No file  | `a2cd64eacb51`  |
| 736    | No file  | `a2cd64eacb51`  |
| 731    | No file  | `a2cd64eacb51`  |
| 723    | No file  | `a2cd64eacb51`  |
| 711    | No file  | `a2cd64eacb51`  |
| 707    | No file  | `a2cd64eacb51`  |
| 697    | No file  | `a2cd64eacb51`  |
| 689    | No file  | `a2cd64eacb51`  |
| 683    | No file  | `a2cd64eacb51`  |
| 678    | No file  | `a2cd64eacb51`  |
| 670    | No file  | `a2cd64eacb51`  |
| 661    | No file  | `a2cd64eacb51`  |
| 656    | No file  | `a2cd64eacb51`  |
| 652    | No file  | `a2cd64eacb51`  |
| 643    | No file  | `a2cd64eacb51`  |
| 637    | No file  | `a2cd64eacb51`  |
| 630    | No file  | `a2cd64eacb51`  |
| 627    | No file  | `a2cd64eacb51`  |
| 621    | No file  | `a2cd64eacb51`  |
| 617    | No file  | `a2cd64eacb51`  |
| 615    | No file  | `a2cd64eacb51`  |
| 606    | No file  | `a2cd64eacb51`  |
| 599    | No file  | `a2cd64eacb51`  |
| 592    | No file  | `a2cd64eacb51`  |
| 586    | No file  | `a2cd64eacb51`  |
| 577    | No file  | `a2cd64eacb51`  |
| 569    | No file  | `a2cd64eacb51`  |
| 561    | No file  | `a2cd64eacb51`  |
| 554    | No file  | `a2cd64eacb51`  |
| 542    | No file  | `a2cd64eacb51`  |
| 532    | No file  | `a2cd64eacb51`  |
| 531    | No file  | `a2cd64eacb51`  |
| 526    | No file  | `a2cd64eacb51`  |
| 521    | No file  | `a2cd64eacb51`  |
| 517    | No file  | `a2cd64eacb51`  |
| 510    | No file  | `a2cd64eacb51`  |
| 508    | No file  | `a2cd64eacb51`  |
| 504    | No file  | `a2cd64eacb51`  |
| 497    | No file  | `a2cd64eacb51`  |
| 491    | No file  | `a2cd64eacb51`  |
| 485    | No file  | `a2cd64eacb51`  |
| 478    | No file  | `a2cd64eacb51`  |
| 472    | No file  | `a2cd64eacb51`  |
| 466    | No file  | `a2cd64eacb51`  |
| 457    | No file  | `a2cd64eacb51`  |
| 452    | No file  | `a2cd64eacb51`  |
| 449    | No file  | `a2cd64eacb51`  |
| 435    | No file  | `a2cd64eacb51`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type         | Field   | Notes                                  |
| ------- | ------------ | ------- | -------------------------------------- |
| `+0x00` | u32          | count   | Number of entries; `1` on client 3474  |
| `+0x04` | Entry[count] | entries | See Entry                              |

### Entry (6 bytes)

| Offset  | Type | Field            | Notes                                                                 |
| ------- | ---- | ---------------- | --------------------------------------------------------------------- |
| `+0x00` | u8   | pet_tier         | Map key: the pet tier as `tier` of [`pet.dbss`](pet_dbss.md) stores it, from 0; `4` is Tier 5 |
| `+0x01` | u8   | unknown_01       | `4` on the only entry, equal to `pet_tier`                            |
| `+0x02` | u32  | leader_buff_rate | Loot cooldown cut for active pets; 1,000,000 = 100%, `150000` (15%) on client 3474 |

## Field Names

No reference source has the table: the file is in the client 2107 archive
but not in the client 1784 one, and a private server's `DataSheets.bexcel`
and `.xlsm` sheets on client 1784 have no sheet or column with `Leader` in
its name. The names come from the client Lua of client 3474:

- `panel_dialog_petleader_all_1.luac` and `panel_window_petlist_all_1.luac`
  call `ToClient_getPetLeaderBuff(petStaticStatus:getPetTier())` and fill the
  result into the resource string `PANEL_WINDOW_PETLEADER_SKILL_DESC`,
  "Pack Leader: Loot cooldown -{percent}% for active pets" (Korean
  `우리들의 골목대장 : 찾은 반려동물 모두의 줍기 재사용 대기시간 감소 ({percent}%)`).
  The Lua names the value `leaderBuffPercent`.
- `getPetTier()` is the stored tier: both scripts add 1 for display
  (`petTier = petStaticStatus:getPetTier() + 1`), and the training window
  asks for the tier the Tier 4 pet trains into. `pet_tier` `4` is therefore Tier 5,
  the only tier that can be appointed alpha (`LUA_PETLEADER_TOOLTIP_DESC`:
  "Appoints one Tier 5 pet as the alpha").

The Lua does not show which of the two equal bytes the client looks the tier
up by; see Open Questions.

## Notes

- Raw bytes on client 3474: `01 00 00 00 04 04 F0 49 02 00`. Clients 2107,
  2519, 3002 and 3251 ship the same ten bytes.
- `global_contentsoptions.luac` sets
  `_ContentsGroup_PetLeader = ToClient_IsContentsGroupOpen("1832")`. Both
  pet leader windows return early when it is off.
- The installed `BlackDesert64.exe` (client 3474) holds no `PetLeader` or
  `leaderbuff` text as ASCII or UTF-16, so it does not show the loader.
- No buff key is stored: the bonus is a rate, not a `buff.dbss` reference.
- The item the Tier 5 training uses is in [`petupgrade.bss`](petupgrade_bss.md).
- In game on client 3474, the Tier 5 Pet Training window shows "Pack
  Leader: Loot cooldown -15% for active pets" under Tier 5 Pet Effects,
  which is `150000` on the 1,000,000 = 100% scale.
- The handler for the option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/tables.py`, framed
  `Framing.BARE`. The Loot Cooldown cell shows `leader_buff_rate` as that
  cut (`-15%`); the record keeps the stored value.

## Open Questions

### Second Tier Byte

`unknown_01` equals `pet_tier` on the only entry. `plantupgradeparam.bss`
stores its map key again as the first member of the value (`param_key`),
which would make this byte a copy of the tier. With one entry the file
cannot tell a copy from a separate field that happens to hold `4`.
