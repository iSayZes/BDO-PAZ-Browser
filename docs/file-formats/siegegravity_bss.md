# `siegegravity.bss` Format

## Purpose

One world position and an f32 per Conquest War territory: rows of a u16
territory key, three f32 coordinates and an unnamed f32. On client 3482
the three rows are Calpheon (`2`), Mediah (`3`) and Valencia (`4`), and
each position lies in that territory's castle. What the client does with
the point is open (see Open Questions).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File               | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ------------------ | ----- | ------- | --------- |
| 1      | 2583 and later | 3483    | `siegegravity.bss` | 74    | 3 Row   | 18        |

| Layout | File               | Known        | Unknown      |
| ------ | ------------------ | ------------ | ------------ |
| 1      | `siegegravity.bss` | 62 B (83.8%) | 12 B (16.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `c97462b2546b`  |
| 3482   | Layout 1 | `c97462b2546b`  |
| 3474   | Layout 1 | `c97462b2546b`  |
| 3473   | Layout 1 | `c97462b2546b`  |
| 3464   | Layout 1 | `c97462b2546b`  |
| 3458   | Layout 1 | `c97462b2546b`  |
| 3454   | Layout 1 | `c97462b2546b`  |
| 3444   | Layout 1 | `c97462b2546b`  |
| 3435   | Layout 1 | `c97462b2546b`  |
| 3426   | Layout 1 | `c97462b2546b`  |
| 3418   | Layout 1 | `c97462b2546b`  |
| 3412   | Layout 1 | `c97462b2546b`  |
| 3402   | Layout 1 | `c97462b2546b`  |
| 3396   | Layout 1 | `c97462b2546b`  |
| 3387   | Layout 1 | `c97462b2546b`  |
| 3381   | Layout 1 | `c97462b2546b`  |
| 3373   | Layout 1 | `c97462b2546b`  |
| 3364   | Layout 1 | `c97462b2546b`  |
| 3356   | Layout 1 | `c97462b2546b`  |
| 3349   | Layout 1 | `c97462b2546b`  |
| 3342   | Layout 1 | `c97462b2546b`  |
| 3335   | Layout 1 | `c97462b2546b`  |
| 3326   | Layout 1 | `c97462b2546b`  |
| 3321   | Layout 1 | `c97462b2546b`  |
| 3314   | Layout 1 | `c97462b2546b`  |
| 3303   | Layout 1 | `c97462b2546b`  |
| 3302   | Layout 1 | `c97462b2546b`  |
| 3293   | Layout 1 | `c97462b2546b`  |
| 3283   | Layout 1 | `c97462b2546b`  |
| 3275   | Layout 1 | `c97462b2546b`  |
| 3267   | Layout 1 | `c97462b2546b`  |
| 3258   | Layout 1 | `c97462b2546b`  |
| 3251   | Layout 1 | `c97462b2546b`  |
| 3242   | Layout 1 | `c97462b2546b`  |
| 3235   | Layout 1 | `c97462b2546b`  |
| 3229   | Layout 1 | `c97462b2546b`  |
| 3212   | Layout 1 | `c97462b2546b`  |
| 3203   | Layout 1 | `c97462b2546b`  |
| 3193   | Layout 1 | `c97462b2546b`  |
| 3186   | Layout 1 | `c97462b2546b`  |
| 3177   | Layout 1 | `c97462b2546b`  |
| 3169   | Layout 1 | `c97462b2546b`  |
| 3158   | Layout 1 | `c97462b2546b`  |
| 3151   | Layout 1 | `c97462b2546b`  |
| 3144   | Layout 1 | `c97462b2546b`  |
| 3133   | Layout 1 | `c97462b2546b`  |
| 3125   | Layout 1 | `c97462b2546b`  |
| 3118   | Layout 1 | `c97462b2546b`  |
| 3111   | Layout 1 | `c97462b2546b`  |
| 3103   | Layout 1 | `c97462b2546b`  |
| 3095   | Layout 1 | `c97462b2546b`  |
| 3086   | Layout 1 | `c97462b2546b`  |
| 3072   | Layout 1 | `c97462b2546b`  |
| 3062   | Layout 1 | `c97462b2546b`  |
| 3052   | Layout 1 | `c97462b2546b`  |
| 3045   | Layout 1 | `c97462b2546b`  |
| 3037   | Layout 1 | `c97462b2546b`  |
| 3030   | Layout 1 | `c97462b2546b`  |
| 3021   | Layout 1 | `c97462b2546b`  |
| 3012   | Layout 1 | `c97462b2546b`  |
| 3002   | Layout 1 | `c97462b2546b`  |
| 2995   | Layout 1 | `c97462b2546b`  |
| 2987   | Layout 1 | `c97462b2546b`  |
| 2978   | Layout 1 | `c97462b2546b`  |
| 2970   | Layout 1 | `c97462b2546b`  |
| 2959   | Layout 1 | `c97462b2546b`  |
| 2951   | Layout 1 | `c97462b2546b`  |
| 2942   | Layout 1 | `c97462b2546b`  |
| 2935   | Layout 1 | `c97462b2546b`  |
| 2932   | Layout 1 | `c97462b2546b`  |
| 2923   | Layout 1 | `c97462b2546b`  |
| 2919   | Layout 1 | `c97462b2546b`  |
| 2907   | Layout 1 | `c97462b2546b`  |
| 2900   | Layout 1 | `c97462b2546b`  |
| 2891   | Layout 1 | `c97462b2546b`  |
| 2882   | Layout 1 | `c97462b2546b`  |
| 2872   | Layout 1 | `c97462b2546b`  |
| 2863   | Layout 1 | `c97462b2546b`  |
| 2855   | Layout 1 | `c97462b2546b`  |
| 2849   | Layout 1 | `c97462b2546b`  |
| 2844   | Layout 1 | `c97462b2546b`  |
| 2834   | Layout 1 | `c97462b2546b`  |
| 2825   | Layout 1 | `c97462b2546b`  |
| 2819   | Layout 1 | `c97462b2546b`  |
| 2811   | Layout 1 | `c97462b2546b`  |
| 2803   | Layout 1 | `c97462b2546b`  |
| 2794   | Layout 1 | `c97462b2546b`  |
| 2783   | Layout 1 | `c97462b2546b`  |
| 2774   | Layout 1 | `c97462b2546b`  |
| 2765   | Layout 1 | `c97462b2546b`  |
| 2756   | Layout 1 | `c97462b2546b`  |
| 2750   | Layout 1 | `c97462b2546b`  |
| 2743   | Layout 1 | `c97462b2546b`  |
| 2736   | Layout 1 | `c97462b2546b`  |
| 2726   | Layout 1 | `c97462b2546b`  |
| 2717   | Layout 1 | `c97462b2546b`  |
| 2709   | Layout 1 | `c97462b2546b`  |
| 2703   | Layout 1 | `c97462b2546b`  |
| 2695   | Layout 1 | `c97462b2546b`  |
| 2684   | Layout 1 | `c97462b2546b`  |
| 2672   | Layout 1 | `c97462b2546b`  |
| 2665   | Layout 1 | `c97462b2546b`  |
| 2657   | Layout 1 | `c97462b2546b`  |
| 2649   | Layout 1 | `c97462b2546b`  |
| 2644   | Layout 1 | `c97462b2546b`  |
| 2637   | Layout 1 | `c97462b2546b`  |
| 2629   | Layout 1 | `c97462b2546b`  |
| 2619   | Layout 1 | `c97462b2546b`  |
| 2612   | Layout 1 | `c97462b2546b`  |
| 2606   | Layout 1 | `c97462b2546b`  |
| 2602   | Layout 1 | `c97462b2546b`  |
| 2601   | Layout 1 | `c97462b2546b`  |
| 2592   | Layout 1 | `c97462b2546b`  |
| 2583   | Layout 1 | `c97462b2546b`  |
| 2575   | No file  | `c97462b2546b`  |
| 2567   | No file  | `c97462b2546b`  |
| 2560   | No file  | `c97462b2546b`  |
| 2553   | No file  | `c97462b2546b`  |
| 2545   | No file  | `c97462b2546b`  |
| 2538   | No file  | `c97462b2546b`  |
| 2529   | No file  | `c97462b2546b`  |
| 2519   | No file  | `c97462b2546b`  |
| 2513   | No file  | `c97462b2546b`  |
| 2510   | No file  | `c97462b2546b`  |
| 2507   | No file  | `c97462b2546b`  |
| 2503   | No file  | `c97462b2546b`  |
| 2498   | No file  | `c97462b2546b`  |
| 2492   | No file  | `c97462b2546b`  |
| 2487   | No file  | `c97462b2546b`  |
| 2480   | No file  | `c97462b2546b`  |
| 2474   | No file  | `c97462b2546b`  |
| 2468   | No file  | `c97462b2546b`  |
| 2460   | No file  | `c97462b2546b`  |
| 2453   | No file  | `c97462b2546b`  |
| 2444   | No file  | `c97462b2546b`  |
| 2438   | No file  | `c97462b2546b`  |
| 2434   | No file  | `c97462b2546b`  |
| 2429   | No file  | `c97462b2546b`  |
| 2421   | No file  | `c97462b2546b`  |
| 2414   | No file  | `c97462b2546b`  |
| 2407   | No file  | `c97462b2546b`  |
| 2401   | No file  | `c97462b2546b`  |
| 2397   | No file  | `c97462b2546b`  |
| 2393   | No file  | `c97462b2546b`  |
| 2384   | No file  | `c97462b2546b`  |
| 2378   | No file  | `c97462b2546b`  |
| 2372   | No file  | `c97462b2546b`  |
| 2358   | No file  | `c97462b2546b`  |
| 2352   | No file  | `c97462b2546b`  |
| 2347   | No file  | `c97462b2546b`  |
| 2343   | No file  | `c97462b2546b`  |
| 2335   | No file  | `c97462b2546b`  |
| 2327   | No file  | `c97462b2546b`  |
| 2324   | No file  | `c97462b2546b`  |
| 2319   | No file  | `c97462b2546b`  |
| 2313   | No file  | `c97462b2546b`  |
| 2308   | No file  | `c97462b2546b`  |
| 2302   | No file  | `c97462b2546b`  |
| 2295   | No file  | `c97462b2546b`  |
| 2290   | No file  | `c97462b2546b`  |
| 2284   | No file  | `c97462b2546b`  |
| 2276   | No file  | `c97462b2546b`  |
| 2269   | No file  | `c97462b2546b`  |
| 2259   | No file  | `c97462b2546b`  |
| 2250   | No file  | `c97462b2546b`  |
| 2243   | No file  | `c97462b2546b`  |
| 2235   | No file  | `c97462b2546b`  |
| 2229   | No file  | `c97462b2546b`  |
| 2224   | No file  | `c97462b2546b`  |
| 2218   | No file  | `c97462b2546b`  |
| 2215   | No file  | `c97462b2546b`  |
| 2207   | No file  | `c97462b2546b`  |
| 2203   | No file  | `c97462b2546b`  |
| 2196   | No file  | `c97462b2546b`  |
| 2192   | No file  | `c97462b2546b`  |
| 2189   | No file  | `c97462b2546b`  |
| 2183   | No file  | `c97462b2546b`  |
| 2179   | No file  | `c97462b2546b`  |
| 2171   | No file  | `c97462b2546b`  |
| 2163   | No file  | `c97462b2546b`  |
| 2156   | No file  | `c97462b2546b`  |
| 2151   | No file  | `c97462b2546b`  |
| 2147   | No file  | `c97462b2546b`  |
| 2142   | No file  | `c97462b2546b`  |
| 2138   | No file  | `c97462b2546b`  |
| 2134   | No file  | `c97462b2546b`  |
| 2130   | No file  | `c97462b2546b`  |
| 2122   | No file  | `c97462b2546b`  |
| 2107   | No file  | `c97462b2546b`  |
| 2098   | No file  | `c97462b2546b`  |
| 2089   | No file  | `c97462b2546b`  |
| 2081   | No file  | `c97462b2546b`  |
| 2073   | No file  | `c97462b2546b`  |
| 2067   | No file  | `c97462b2546b`  |
| 2063   | No file  | `c97462b2546b`  |
| 2059   | No file  | `c97462b2546b`  |
| 2052   | No file  | `c97462b2546b`  |
| 2044   | No file  | `c97462b2546b`  |
| 2039   | No file  | `c97462b2546b`  |
| 2032   | No file  | `c97462b2546b`  |
| 2025   | No file  | `c97462b2546b`  |
| 2011   | No file  | `c97462b2546b`  |
| 2005   | No file  | `c97462b2546b`  |
| 2000   | No file  | `c97462b2546b`  |
| 1996   | No file  | `c97462b2546b`  |
| 1991   | No file  | `c97462b2546b`  |
| 1985   | No file  | `c97462b2546b`  |
| 1980   | No file  | `c97462b2546b`  |
| 1969   | No file  | `c97462b2546b`  |
| 1964   | No file  | `c97462b2546b`  |
| 1958   | No file  | `c97462b2546b`  |
| 1950   | No file  | `c97462b2546b`  |
| 1945   | No file  | `c97462b2546b`  |
| 1937   | No file  | `c97462b2546b`  |
| 1933   | No file  | `c97462b2546b`  |
| 1927   | No file  | `c97462b2546b`  |
| 1921   | No file  | `c97462b2546b`  |
| 1914   | No file  | `c97462b2546b`  |
| 1908   | No file  | `c97462b2546b`  |
| 1897   | No file  | `c97462b2546b`  |
| 1892   | No file  | `c97462b2546b`  |
| 1886   | No file  | `c97462b2546b`  |
| 1881   | No file  | `c97462b2546b`  |
| 1871   | No file  | `c97462b2546b`  |
| 1866   | No file  | `c97462b2546b`  |
| 1862   | No file  | `c97462b2546b`  |
| 1854   | No file  | `c97462b2546b`  |
| 1846   | No file  | `c97462b2546b`  |
| 1838   | No file  | `c97462b2546b`  |
| 1832   | No file  | `c97462b2546b`  |
| 1826   | No file  | `c97462b2546b`  |
| 1822   | No file  | `c97462b2546b`  |
| 1818   | No file  | `c97462b2546b`  |
| 1804   | No file  | `c97462b2546b`  |
| 1794   | No file  | `c97462b2546b`  |
| 1790   | No file  | `c97462b2546b`  |
| 1784   | No file  | `c97462b2546b`  |
| 1774   | No file  | `c97462b2546b`  |
| 1771   | No file  | `c97462b2546b`  |
| 1762   | No file  | `c97462b2546b`  |
| 1759   | No file  | `c97462b2546b`  |
| 1754   | No file  | `c97462b2546b`  |
| 1749   | No file  | `c97462b2546b`  |
| 1743   | No file  | `c97462b2546b`  |
| 1737   | No file  | `c97462b2546b`  |
| 1731   | No file  | `c97462b2546b`  |
| 1725   | No file  | `c97462b2546b`  |
| 1717   | No file  | `c97462b2546b`  |
| 1710   | No file  | `c97462b2546b`  |
| 1704   | No file  | `c97462b2546b`  |
| 1698   | No file  | `c97462b2546b`  |
| 1690   | No file  | `c97462b2546b`  |
| 1685   | No file  | `c97462b2546b`  |
| 1680   | No file  | `c97462b2546b`  |
| 1674   | No file  | `c97462b2546b`  |
| 1668   | No file  | `c97462b2546b`  |
| 1659   | No file  | `c97462b2546b`  |
| 1649   | No file  | `c97462b2546b`  |
| 1642   | No file  | `c97462b2546b`  |
| 1636   | No file  | `c97462b2546b`  |
| 1628   | No file  | `c97462b2546b`  |
| 1622   | No file  | `c97462b2546b`  |
| 1614   | No file  | `c97462b2546b`  |
| 1608   | No file  | `c97462b2546b`  |
| 1602   | No file  | `c97462b2546b`  |
| 1598   | No file  | `c97462b2546b`  |
| 1594   | No file  | `c97462b2546b`  |
| 1590   | No file  | `c97462b2546b`  |
| 1587   | No file  | `c97462b2546b`  |
| 1584   | No file  | `c97462b2546b`  |
| 1579   | No file  | `c97462b2546b`  |
| 1572   | No file  | `c97462b2546b`  |
| 1565   | No file  | `c97462b2546b`  |
| 1559   | No file  | `c97462b2546b`  |
| 1554   | No file  | `c97462b2546b`  |
| 1547   | No file  | `c97462b2546b`  |
| 1537   | No file  | `c97462b2546b`  |
| 1529   | No file  | `c97462b2546b`  |
| 1524   | No file  | `c97462b2546b`  |
| 1519   | No file  | `c97462b2546b`  |
| 1509   | No file  | `c97462b2546b`  |
| 1506   | No file  | `c97462b2546b`  |
| 1504   | No file  | `c97462b2546b`  |
| 1500   | No file  | `c97462b2546b`  |
| 1493   | No file  | `c97462b2546b`  |
| 1489   | No file  | `c97462b2546b`  |
| 1485   | No file  | `c97462b2546b`  |
| 1481   | No file  | `c97462b2546b`  |
| 1474   | No file  | `c97462b2546b`  |
| 1466   | No file  | `c97462b2546b`  |
| 1462   | No file  | `c97462b2546b`  |
| 1459   | No file  | `c97462b2546b`  |
| 1453   | No file  | `c97462b2546b`  |
| 1450   | No file  | `c97462b2546b`  |
| 1445   | No file  | `c97462b2546b`  |
| 1439   | No file  | `c97462b2546b`  |
| 1433   | No file  | `c97462b2546b`  |
| 1430   | No file  | `c97462b2546b`  |
| 1426   | No file  | `c97462b2546b`  |
| 1421   | No file  | `c97462b2546b`  |
| 1417   | No file  | `c97462b2546b`  |
| 1416   | No file  | `c97462b2546b`  |
| 1409   | No file  | `c97462b2546b`  |
| 1405   | No file  | `c97462b2546b`  |
| 1401   | No file  | `c97462b2546b`  |
| 1396   | No file  | `c97462b2546b`  |
| 1391   | No file  | `c97462b2546b`  |
| 1390   | No file  | `c97462b2546b`  |
| 1386   | No file  | `c97462b2546b`  |
| 1381   | No file  | `c97462b2546b`  |
| 1379   | No file  | `c97462b2546b`  |
| 1372   | No file  | `c97462b2546b`  |
| 1366   | No file  | `c97462b2546b`  |
| 1364   | No file  | `c97462b2546b`  |
| 1363   | No file  | `c97462b2546b`  |
| 1360   | No file  | `c97462b2546b`  |
| 1358   | No file  | `c97462b2546b`  |
| 1355   | No file  | `c97462b2546b`  |
| 1351   | No file  | `c97462b2546b`  |
| 1348   | No file  | `c97462b2546b`  |
| 1346   | No file  | `c97462b2546b`  |
| 1341   | No file  | `c97462b2546b`  |
| 1340   | No file  | `c97462b2546b`  |
| 1338   | No file  | `c97462b2546b`  |
| 1335   | No file  | `c97462b2546b`  |
| 1333   | No file  | `c97462b2546b`  |
| 1329   | No file  | `c97462b2546b`  |
| 1327   | No file  | `c97462b2546b`  |
| 1324   | No file  | `c97462b2546b`  |
| 1321   | No file  | `c97462b2546b`  |
| 1319   | No file  | `c97462b2546b`  |
| 1318   | No file  | `c97462b2546b`  |
| 1316   | No file  | `c97462b2546b`  |
| 1313   | No file  | `c97462b2546b`  |
| 1311   | No file  | `c97462b2546b`  |
| 1309   | No file  | `c97462b2546b`  |
| 1304   | No file  | `c97462b2546b`  |
| 1292   | No file  | `c97462b2546b`  |
| 1286   | No file  | `c97462b2546b`  |
| 1280   | No file  | `c97462b2546b`  |
| 1276   | No file  | `c97462b2546b`  |
| 1267   | No file  | `c97462b2546b`  |
| 1261   | No file  | `c97462b2546b`  |
| 1256   | No file  | `c97462b2546b`  |
| 1250   | No file  | `c97462b2546b`  |
| 1246   | No file  | `c97462b2546b`  |
| 1239   | No file  | `c97462b2546b`  |
| 1230   | No file  | `c97462b2546b`  |
| 1226   | No file  | `c97462b2546b`  |
| 1220   | No file  | `c97462b2546b`  |
| 1217   | No file  | `c97462b2546b`  |
| 1211   | No file  | `c97462b2546b`  |
| 1210   | No file  | `c97462b2546b`  |
| 1208   | No file  | `c97462b2546b`  |
| 1203   | No file  | `c97462b2546b`  |
| 1197   | No file  | `c97462b2546b`  |
| 1194   | No file  | `c97462b2546b`  |
| 1192   | No file  | `c97462b2546b`  |
| 1187   | No file  | `c97462b2546b`  |
| 1183   | No file  | `c97462b2546b`  |
| 1177   | No file  | `c97462b2546b`  |
| 1173   | No file  | `c97462b2546b`  |
| 1167   | No file  | `c97462b2546b`  |
| 1164   | No file  | `c97462b2546b`  |
| 1156   | No file  | `c97462b2546b`  |
| 1149   | No file  | `c97462b2546b`  |
| 1144   | No file  | `c97462b2546b`  |
| 1137   | No file  | `c97462b2546b`  |
| 1132   | No file  | `c97462b2546b`  |
| 1127   | No file  | `c97462b2546b`  |
| 1122   | No file  | `c97462b2546b`  |
| 1118   | No file  | `c97462b2546b`  |
| 1114   | No file  | `c97462b2546b`  |
| 1109   | No file  | `c97462b2546b`  |
| 1102   | No file  | `c97462b2546b`  |
| 1096   | No file  | `c97462b2546b`  |
| 1088   | No file  | `c97462b2546b`  |
| 1081   | No file  | `c97462b2546b`  |
| 1076   | No file  | `c97462b2546b`  |
| 1069   | No file  | `c97462b2546b`  |
| 1064   | No file  | `c97462b2546b`  |
| 1058   | No file  | `c97462b2546b`  |
| 1051   | No file  | `c97462b2546b`  |
| 1044   | No file  | `c97462b2546b`  |
| 1036   | No file  | `c97462b2546b`  |
| 1026   | No file  | `c97462b2546b`  |
| 1016   | No file  | `c97462b2546b`  |
| 1009   | No file  | `c97462b2546b`  |
| 1005   | No file  | `c97462b2546b`  |
| 1000   | No file  | `c97462b2546b`  |
| 998    | No file  | `c97462b2546b`  |
| 990    | No file  | `c97462b2546b`  |
| 979    | No file  | `c97462b2546b`  |
| 972    | No file  | `c97462b2546b`  |
| 963    | No file  | `c97462b2546b`  |
| 955    | No file  | `c97462b2546b`  |
| 946    | No file  | `c97462b2546b`  |
| 938    | No file  | `c97462b2546b`  |
| 927    | No file  | `c97462b2546b`  |
| 911    | No file  | `c97462b2546b`  |
| 904    | No file  | `c97462b2546b`  |
| 899    | No file  | `c97462b2546b`  |
| 894    | No file  | `c97462b2546b`  |
| 885    | No file  | `c97462b2546b`  |
| 879    | No file  | `c97462b2546b`  |
| 872    | No file  | `c97462b2546b`  |
| 864    | No file  | `c97462b2546b`  |
| 855    | No file  | `c97462b2546b`  |
| 853    | No file  | `c97462b2546b`  |
| 845    | No file  | `c97462b2546b`  |
| 837    | No file  | `c97462b2546b`  |
| 829    | No file  | `c97462b2546b`  |
| 822    | No file  | `c97462b2546b`  |
| 814    | No file  | `c97462b2546b`  |
| 805    | No file  | `c97462b2546b`  |
| 794    | No file  | `c97462b2546b`  |
| 787    | No file  | `c97462b2546b`  |
| 780    | No file  | `c97462b2546b`  |
| 771    | No file  | `c97462b2546b`  |
| 760    | No file  | `c97462b2546b`  |
| 748    | No file  | `c97462b2546b`  |
| 741    | No file  | `c97462b2546b`  |
| 736    | No file  | `c97462b2546b`  |
| 731    | No file  | `c97462b2546b`  |
| 723    | No file  | `c97462b2546b`  |
| 711    | No file  | `c97462b2546b`  |
| 707    | No file  | `c97462b2546b`  |
| 697    | No file  | `c97462b2546b`  |
| 689    | No file  | `c97462b2546b`  |
| 683    | No file  | `c97462b2546b`  |
| 678    | No file  | `c97462b2546b`  |
| 670    | No file  | `c97462b2546b`  |
| 661    | No file  | `c97462b2546b`  |
| 656    | No file  | `c97462b2546b`  |
| 652    | No file  | `c97462b2546b`  |
| 643    | No file  | `c97462b2546b`  |
| 637    | No file  | `c97462b2546b`  |
| 630    | No file  | `c97462b2546b`  |
| 627    | No file  | `c97462b2546b`  |
| 621    | No file  | `c97462b2546b`  |
| 617    | No file  | `c97462b2546b`  |
| 615    | No file  | `c97462b2546b`  |
| 606    | No file  | `c97462b2546b`  |
| 599    | No file  | `c97462b2546b`  |
| 592    | No file  | `c97462b2546b`  |
| 586    | No file  | `c97462b2546b`  |
| 577    | No file  | `c97462b2546b`  |
| 569    | No file  | `c97462b2546b`  |
| 561    | No file  | `c97462b2546b`  |
| 554    | No file  | `c97462b2546b`  |
| 542    | No file  | `c97462b2546b`  |
| 532    | No file  | `c97462b2546b`  |
| 531    | No file  | `c97462b2546b`  |
| 526    | No file  | `c97462b2546b`  |
| 521    | No file  | `c97462b2546b`  |
| 517    | No file  | `c97462b2546b`  |
| 510    | No file  | `c97462b2546b`  |
| 508    | No file  | `c97462b2546b`  |
| 504    | No file  | `c97462b2546b`  |
| 497    | No file  | `c97462b2546b`  |
| 491    | No file  | `c97462b2546b`  |
| 485    | No file  | `c97462b2546b`  |
| 478    | No file  | `c97462b2546b`  |
| 472    | No file  | `c97462b2546b`  |
| 466    | No file  | `c97462b2546b`  |
| 457    | No file  | `c97462b2546b`  |
| 452    | No file  | `c97462b2546b`  |
| 449    | No file  | `c97462b2546b`  |
| 435    | No file  | `c97462b2546b`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                          |
| --------------------- | -------- | ----------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12  |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows                                |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (18 bytes)

| Offset  | Type | Field         | Notes                                                                 |
| ------- | ---- | ------------- | --------------------------------------------------------------------- |
| `+0x00` | u16  | territory_key | `territoryinfo.bss` key (LOC type 12); one row each                   |
| `+0x02` | f32  | position_x    | World X                                                               |
| `+0x06` | f32  | position_y    | World Y (height)                                                      |
| `+0x0A` | f32  | position_z    | World Z                                                               |
| `+0x0E` | f32  | unknown_0e    | `13500` to `18000` on client 3482, a round number per row             |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Rows

Client 3482, in file order.

| `territory_key` | Territory | `position_x` | `position_y` | `position_z` | `unknown_0e` |
| --------------- | --------- | ------------ | ------------ | ------------ | ------------ |
| 4               | Valencia  | 1160597      | 18668        | 299213       | 18000        |
| 3               | Mediah    | 310370       | -3626        | 53438        | 15000        |
| 2               | Calpheon  | -354348      | 3293         | -59848       | 13500        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 holds
these rows, and client 1784 does not ship the file. The territory keys
are the three Conquest War territories of `siegegovernorcarriagespawn.bss`
(`MajorSiegeRegion`). The three coordinates are a world position: each
lies within about 1,000 units of the four castle gate positions the
`SiegeCastleTeleportPos` sheet (client 1784) gives for the same territory
key, e.g. Calpheon `-348487` to `-354847` (X) and `-55022` to `-61718`
(Z).

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/siegeobject_tables.py`:
  the territory with its name and the position.

## Open Questions

### What the Gravity Point Is

No client Lua of client 3482 names `siegegravity` or a getter for it. The
Lua has the event `FromClient_DestroyedSiegeGravityMagician`
(`panel_warinfomessage.luac`), whose message
`LUA_WARINFOMESSAGE_NOTIFYKINGORLORDTENTCHANGE_DESTROYGRAVITY_MAIN` reads
"All Dekrogda relics have been destroyed, undoing the barrier." The rows
may be the centre of that barrier at each castle, with `unknown_0e` its
radius (13,500 to 18,000 units); nothing in the client data ties the two
together yet.
