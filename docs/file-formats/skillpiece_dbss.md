# `skillpiece.dbss` Format

## Purpose

Set effect tiers. A record belongs to one set skill: each equipped piece of
the set applies a [`buff.dbss`](buff_dbss.md) type 48 buff that adds points
to that skill, and once the points reach a tier's threshold the skill runs at
the tier's level. A tier also carries the Korean tooltip text: the set title,
the threshold label and the bonus lines.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                    | Bytes  | Records              | Row bytes                 |
| ------ | -------------- | ------- | ----------------------- | ------ | -------------------- | ------------------------- |
| 1      | 1346 and later | 3483    | `skillpiece.dbss`       | 31,628 | 168 Tier, 100 Record | 30 to 534, 180 on average |
| 1      | 1346 and later | 3483    | `skillpieceoffset.dbss` | 1,004  | 100 Index Row        | 10                        |

| Layout | File                    | Known            | Unknown      |
| ------ | ----------------------- | ---------------- | ------------ |
| 1      | `skillpiece.dbss`       | 31,228 B (98.7%) | 400 B (1.3%) |
| 1      | `skillpieceoffset.dbss` | 1,004 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `356a73f483d6`  |
| 3482   | Layout 1             | `356a73f483d6`  |
| 3474   | Layout 1             | `356a73f483d6`  |
| 3473   | Layout 1             | `356a73f483d6`  |
| 3464   | Layout 1             | `356a73f483d6`  |
| 3458   | Layout 1             | `356a73f483d6`  |
| 3454   | Layout 1             | `356a73f483d6`  |
| 3444   | Layout 1             | `356a73f483d6`  |
| 3435   | Layout 1             | `356a73f483d6`  |
| 3426   | Layout 1             | `356a73f483d6`  |
| 3418   | Layout 1             | `356a73f483d6`  |
| 3412   | Layout 1             | `356a73f483d6`  |
| 3402   | Layout 1             | `356a73f483d6`  |
| 3396   | Layout 1             | `356a73f483d6`  |
| 3387   | Layout 1             | `356a73f483d6`  |
| 3381   | Layout 1             | `356a73f483d6`  |
| 3373   | Layout 1             | `356a73f483d6`  |
| 3364   | Layout 1             | `356a73f483d6`  |
| 3356   | Layout 1             | `356a73f483d6`  |
| 3349   | Layout 1             | `356a73f483d6`  |
| 3342   | Layout 1             | `356a73f483d6`  |
| 3335   | Layout 1             | `356a73f483d6`  |
| 3326   | Layout 1             | `356a73f483d6`  |
| 3321   | Layout 1             | `356a73f483d6`  |
| 3314   | Layout 1             | `356a73f483d6`  |
| 3303   | Layout 1             | `356a73f483d6`  |
| 3302   | Layout 1             | `356a73f483d6`  |
| 3293   | Layout 1             | `356a73f483d6`  |
| 3283   | Layout 1             | `356a73f483d6`  |
| 3275   | Layout 1             | `356a73f483d6`  |
| 3267   | Layout 1             | `356a73f483d6`  |
| 3258   | Layout 1             | `356a73f483d6`  |
| 3251   | Layout 1             | `356a73f483d6`  |
| 3242   | Layout 1             | `356a73f483d6`  |
| 3235   | Layout 1             | `356a73f483d6`  |
| 3229   | Layout 1             | `356a73f483d6`  |
| 3212   | Layout 1             | `356a73f483d6`  |
| 3203   | Layout 1             | `356a73f483d6`  |
| 3193   | Layout 1             | `356a73f483d6`  |
| 3186   | Layout 1             | `356a73f483d6`  |
| 3177   | Layout 1             | `356a73f483d6`  |
| 3169   | Layout 1             | `356a73f483d6`  |
| 3158   | Layout 1             | `356a73f483d6`  |
| 3151   | Layout 1             | `356a73f483d6`  |
| 3144   | Layout 1             | `356a73f483d6`  |
| 3133   | Layout 1             | `356a73f483d6`  |
| 3125   | Layout 1             | `356a73f483d6`  |
| 3118   | Layout 1             | `356a73f483d6`  |
| 3111   | Layout 1             | `356a73f483d6`  |
| 3103   | Layout 1             | `356a73f483d6`  |
| 3095   | Layout 1             | `356a73f483d6`  |
| 3086   | Layout 1             | `356a73f483d6`  |
| 3072   | Layout 1             | `356a73f483d6`  |
| 3062   | Layout 1             | `356a73f483d6`  |
| 3052   | Layout 1             | `356a73f483d6`  |
| 3045   | Layout 1             | `356a73f483d6`  |
| 3037   | Layout 1             | `356a73f483d6`  |
| 3030   | Layout 1             | `356a73f483d6`  |
| 3021   | Layout 1             | `356a73f483d6`  |
| 3012   | Layout 1             | `356a73f483d6`  |
| 3002   | Layout 1             | `356a73f483d6`  |
| 2995   | Layout 1             | `356a73f483d6`  |
| 2987   | Layout 1             | `356a73f483d6`  |
| 2978   | Layout 1             | `356a73f483d6`  |
| 2970   | Layout 1             | `356a73f483d6`  |
| 2959   | Layout 1             | `356a73f483d6`  |
| 2951   | Layout 1             | `356a73f483d6`  |
| 2942   | Layout 1             | `356a73f483d6`  |
| 2935   | Layout 1             | `356a73f483d6`  |
| 2932   | Layout 1             | `356a73f483d6`  |
| 2923   | Layout 1             | `356a73f483d6`  |
| 2919   | Layout 1             | `356a73f483d6`  |
| 2907   | Layout 1             | `356a73f483d6`  |
| 2900   | Layout 1             | `356a73f483d6`  |
| 2891   | Layout 1             | `356a73f483d6`  |
| 2882   | Layout 1             | `356a73f483d6`  |
| 2872   | Layout 1             | `356a73f483d6`  |
| 2863   | Layout 1             | `356a73f483d6`  |
| 2855   | Layout 1             | `356a73f483d6`  |
| 2849   | Layout 1             | `356a73f483d6`  |
| 2844   | Layout 1             | `356a73f483d6`  |
| 2834   | Layout 1             | `356a73f483d6`  |
| 2825   | Layout 1             | `356a73f483d6`  |
| 2819   | Layout 1             | `356a73f483d6`  |
| 2811   | Layout 1             | `356a73f483d6`  |
| 2803   | Layout 1             | `356a73f483d6`  |
| 2794   | Layout 1             | `356a73f483d6`  |
| 2783   | Layout 1             | `356a73f483d6`  |
| 2774   | Layout 1             | `356a73f483d6`  |
| 2765   | Layout 1             | `356a73f483d6`  |
| 2756   | Layout 1             | `356a73f483d6`  |
| 2750   | Layout 1             | `356a73f483d6`  |
| 2743   | Layout 1             | `356a73f483d6`  |
| 2736   | Layout 1             | `356a73f483d6`  |
| 2726   | Layout 1             | `356a73f483d6`  |
| 2717   | Layout 1             | `356a73f483d6`  |
| 2709   | Layout 1             | `356a73f483d6`  |
| 2703   | Layout 1             | `356a73f483d6`  |
| 2695   | Layout 1             | `356a73f483d6`  |
| 2684   | Layout 1             | `356a73f483d6`  |
| 2672   | Layout 1             | `356a73f483d6`  |
| 2665   | Layout 1             | `356a73f483d6`  |
| 2657   | Layout 1             | `356a73f483d6`  |
| 2649   | Layout 1             | `356a73f483d6`  |
| 2644   | Layout 1             | `356a73f483d6`  |
| 2637   | Layout 1             | `356a73f483d6`  |
| 2629   | Layout 1             | `356a73f483d6`  |
| 2619   | Layout 1             | `356a73f483d6`  |
| 2612   | Layout 1             | `356a73f483d6`  |
| 2606   | Layout 1             | `356a73f483d6`  |
| 2602   | Layout 1             | `356a73f483d6`  |
| 2601   | Layout 1             | `356a73f483d6`  |
| 2592   | Layout 1             | `356a73f483d6`  |
| 2583   | Layout 1             | `356a73f483d6`  |
| 2575   | Layout 1             | `356a73f483d6`  |
| 2567   | Layout 1             | `356a73f483d6`  |
| 2560   | Layout 1             | `356a73f483d6`  |
| 2553   | Layout 1             | `356a73f483d6`  |
| 2545   | Layout 1             | `356a73f483d6`  |
| 2538   | Layout 1             | `356a73f483d6`  |
| 2529   | Layout 1             | `356a73f483d6`  |
| 2519   | Layout 1             | `356a73f483d6`  |
| 2513   | Layout 1             | `356a73f483d6`  |
| 2510   | Layout 1             | `356a73f483d6`  |
| 2507   | Layout 1             | `356a73f483d6`  |
| 2503   | Layout 1             | `356a73f483d6`  |
| 2498   | Layout 1             | `356a73f483d6`  |
| 2492   | Layout 1             | `356a73f483d6`  |
| 2487   | Layout 1             | `356a73f483d6`  |
| 2480   | Layout 1             | `356a73f483d6`  |
| 2474   | Layout 1             | `356a73f483d6`  |
| 2468   | Layout 1             | `356a73f483d6`  |
| 2460   | Layout 1             | `356a73f483d6`  |
| 2453   | Layout 1             | `356a73f483d6`  |
| 2444   | Layout 1             | `356a73f483d6`  |
| 2438   | Layout 1             | `356a73f483d6`  |
| 2434   | Layout 1             | `356a73f483d6`  |
| 2429   | Layout 1             | `356a73f483d6`  |
| 2421   | Layout 1             | `356a73f483d6`  |
| 2414   | Layout 1             | `356a73f483d6`  |
| 2407   | Layout 1             | `356a73f483d6`  |
| 2401   | Layout 1             | `356a73f483d6`  |
| 2397   | Layout 1             | `356a73f483d6`  |
| 2393   | Layout 1             | `356a73f483d6`  |
| 2384   | Layout 1             | `356a73f483d6`  |
| 2378   | Layout 1             | `356a73f483d6`  |
| 2372   | Layout 1             | `356a73f483d6`  |
| 2358   | Layout 1             | `356a73f483d6`  |
| 2352   | Layout 1             | `356a73f483d6`  |
| 2347   | Layout 1             | `356a73f483d6`  |
| 2343   | Layout 1             | `356a73f483d6`  |
| 2335   | Layout 1             | `356a73f483d6`  |
| 2327   | Layout 1             | `356a73f483d6`  |
| 2324   | Layout 1             | `356a73f483d6`  |
| 2319   | Layout 1             | `356a73f483d6`  |
| 2313   | Layout 1             | `356a73f483d6`  |
| 2308   | Layout 1             | `356a73f483d6`  |
| 2302   | Layout 1             | `356a73f483d6`  |
| 2295   | Layout 1             | `356a73f483d6`  |
| 2290   | Layout 1             | `356a73f483d6`  |
| 2284   | Layout 1             | `356a73f483d6`  |
| 2276   | Layout 1             | `356a73f483d6`  |
| 2269   | Layout 1             | `356a73f483d6`  |
| 2259   | Layout 1             | `356a73f483d6`  |
| 2250   | Layout 1             | `356a73f483d6`  |
| 2243   | Layout 1             | `356a73f483d6`  |
| 2235   | Layout 1             | `356a73f483d6`  |
| 2229   | Layout 1             | `356a73f483d6`  |
| 2224   | Layout 1             | `356a73f483d6`  |
| 2218   | Layout 1             | `356a73f483d6`  |
| 2215   | Layout 1             | `356a73f483d6`  |
| 2207   | Layout 1             | `356a73f483d6`  |
| 2203   | Layout 1             | `356a73f483d6`  |
| 2196   | Layout 1             | `356a73f483d6`  |
| 2192   | Layout 1             | `356a73f483d6`  |
| 2189   | Layout 1             | `356a73f483d6`  |
| 2183   | Layout 1             | `356a73f483d6`  |
| 2179   | Layout 1             | `356a73f483d6`  |
| 2171   | Layout 1             | `356a73f483d6`  |
| 2163   | Layout 1             | `356a73f483d6`  |
| 2156   | Layout 1             | `356a73f483d6`  |
| 2151   | Layout 1             | `356a73f483d6`  |
| 2147   | Layout 1             | `356a73f483d6`  |
| 2142   | Layout 1             | `356a73f483d6`  |
| 2138   | Layout 1             | `356a73f483d6`  |
| 2134   | Layout 1             | `356a73f483d6`  |
| 2130   | Layout 1             | `356a73f483d6`  |
| 2122   | Layout 1             | `356a73f483d6`  |
| 2107   | Layout 1             | `356a73f483d6`  |
| 2098   | Layout 1             | `356a73f483d6`  |
| 2089   | Layout 1             | `356a73f483d6`  |
| 2081   | Layout 1             | `356a73f483d6`  |
| 2073   | Layout 1             | `356a73f483d6`  |
| 2067   | Layout 1             | `356a73f483d6`  |
| 2063   | Layout 1             | `356a73f483d6`  |
| 2059   | Layout 1             | `356a73f483d6`  |
| 2052   | Layout 1             | `356a73f483d6`  |
| 2044   | Layout 1             | `356a73f483d6`  |
| 2039   | Layout 1             | `356a73f483d6`  |
| 2032   | Layout 1             | `356a73f483d6`  |
| 2025   | Layout 1             | `356a73f483d6`  |
| 2011   | Layout 1             | `356a73f483d6`  |
| 2005   | Layout 1             | `356a73f483d6`  |
| 2000   | Layout 1             | `356a73f483d6`  |
| 1996   | Layout 1             | `356a73f483d6`  |
| 1991   | Layout 1             | `356a73f483d6`  |
| 1985   | Layout 1             | `356a73f483d6`  |
| 1980   | Layout 1             | `356a73f483d6`  |
| 1969   | Layout 1             | `356a73f483d6`  |
| 1964   | Layout 1             | `356a73f483d6`  |
| 1958   | Layout 1             | `356a73f483d6`  |
| 1950   | Layout 1             | `356a73f483d6`  |
| 1945   | Layout 1             | `356a73f483d6`  |
| 1937   | Layout 1             | `356a73f483d6`  |
| 1933   | Layout 1             | `356a73f483d6`  |
| 1927   | Layout 1             | `356a73f483d6`  |
| 1921   | Layout 1             | `356a73f483d6`  |
| 1914   | Layout 1             | `356a73f483d6`  |
| 1908   | Layout 1             | `356a73f483d6`  |
| 1897   | Layout 1             | `356a73f483d6`  |
| 1892   | Layout 1             | `356a73f483d6`  |
| 1886   | Layout 1             | `356a73f483d6`  |
| 1881   | Layout 1             | `356a73f483d6`  |
| 1871   | Layout 1             | `356a73f483d6`  |
| 1866   | Layout 1             | `356a73f483d6`  |
| 1862   | Layout 1             | `356a73f483d6`  |
| 1854   | Layout 1             | `356a73f483d6`  |
| 1846   | Layout 1             | `356a73f483d6`  |
| 1838   | Layout 1             | `356a73f483d6`  |
| 1832   | Layout 1             | `356a73f483d6`  |
| 1826   | Layout 1             | `356a73f483d6`  |
| 1822   | Layout 1             | `356a73f483d6`  |
| 1818   | Layout 1             | `356a73f483d6`  |
| 1804   | Layout 1             | `356a73f483d6`  |
| 1794   | Layout 1             | `356a73f483d6`  |
| 1790   | Layout 1             | `356a73f483d6`  |
| 1784   | Layout 1             | `356a73f483d6`  |
| 1774   | Layout 1             | `356a73f483d6`  |
| 1771   | Layout 1             | `356a73f483d6`  |
| 1762   | Layout 1             | `356a73f483d6`  |
| 1759   | Layout 1             | `356a73f483d6`  |
| 1754   | Layout 1             | `356a73f483d6`  |
| 1749   | Layout 1             | `356a73f483d6`  |
| 1743   | Layout 1             | `356a73f483d6`  |
| 1737   | Layout 1             | `356a73f483d6`  |
| 1731   | Layout 1             | `356a73f483d6`  |
| 1725   | Layout 1             | `356a73f483d6`  |
| 1717   | Layout 1             | `356a73f483d6`  |
| 1710   | Layout 1             | `356a73f483d6`  |
| 1704   | Layout 1             | `356a73f483d6`  |
| 1698   | Layout 1             | `356a73f483d6`  |
| 1690   | Layout 1             | `356a73f483d6`  |
| 1685   | Layout 1             | `356a73f483d6`  |
| 1680   | Layout 1             | `356a73f483d6`  |
| 1674   | Layout 1             | `356a73f483d6`  |
| 1668   | Layout 1             | `356a73f483d6`  |
| 1659   | Layout 1             | `356a73f483d6`  |
| 1649   | Layout 1             | `356a73f483d6`  |
| 1642   | Layout 1             | `356a73f483d6`  |
| 1636   | Layout 1             | `356a73f483d6`  |
| 1628   | Layout 1             | `356a73f483d6`  |
| 1622   | Layout 1             | `356a73f483d6`  |
| 1614   | Layout 1             | `356a73f483d6`  |
| 1608   | Layout 1             | `356a73f483d6`  |
| 1602   | Layout 1             | `356a73f483d6`  |
| 1598   | Layout 1             | `356a73f483d6`  |
| 1594   | Layout 1             | `356a73f483d6`  |
| 1590   | Layout 1             | `356a73f483d6`  |
| 1587   | Layout 1             | `356a73f483d6`  |
| 1584   | Layout 1             | `356a73f483d6`  |
| 1579   | Layout 1             | `356a73f483d6`  |
| 1572   | Layout 1             | `356a73f483d6`  |
| 1565   | Layout 1             | `356a73f483d6`  |
| 1559   | Layout 1             | `356a73f483d6`  |
| 1554   | Layout 1             | `356a73f483d6`  |
| 1547   | Layout 1             | `356a73f483d6`  |
| 1537   | Layout 1             | `356a73f483d6`  |
| 1529   | Layout 1             | `356a73f483d6`  |
| 1524   | Layout 1             | `356a73f483d6`  |
| 1519   | Layout 1             | `356a73f483d6`  |
| 1509   | Layout 1             | `356a73f483d6`  |
| 1506   | Layout 1             | `356a73f483d6`  |
| 1504   | Layout 1             | `356a73f483d6`  |
| 1500   | Layout 1             | `356a73f483d6`  |
| 1493   | Layout 1             | `356a73f483d6`  |
| 1489   | Layout 1             | `356a73f483d6`  |
| 1485   | Layout 1             | `356a73f483d6`  |
| 1481   | Layout 1             | `356a73f483d6`  |
| 1474   | Layout 1             | `356a73f483d6`  |
| 1466   | Layout 1             | `356a73f483d6`  |
| 1462   | Layout 1             | `356a73f483d6`  |
| 1459   | Layout 1             | `356a73f483d6`  |
| 1453   | Layout 1             | `356a73f483d6`  |
| 1450   | Layout 1             | `356a73f483d6`  |
| 1445   | Layout 1             | `356a73f483d6`  |
| 1439   | Layout 1             | `356a73f483d6`  |
| 1433   | Layout 1             | `356a73f483d6`  |
| 1430   | Layout 1             | `356a73f483d6`  |
| 1426   | Layout 1             | `356a73f483d6`  |
| 1421   | Layout 1             | `356a73f483d6`  |
| 1417   | Layout 1             | `356a73f483d6`  |
| 1416   | Layout 1             | `356a73f483d6`  |
| 1409   | Layout 1             | `356a73f483d6`  |
| 1405   | Layout 1             | `356a73f483d6`  |
| 1401   | Layout 1             | `356a73f483d6`  |
| 1396   | Layout 1             | `356a73f483d6`  |
| 1391   | Layout 1             | `356a73f483d6`  |
| 1390   | Layout 1             | `356a73f483d6`  |
| 1386   | Layout 1             | `356a73f483d6`  |
| 1381   | Layout 1             | `356a73f483d6`  |
| 1379   | Layout 1             | `356a73f483d6`  |
| 1372   | Layout 1             | `356a73f483d6`  |
| 1366   | Layout 1             | `356a73f483d6`  |
| 1364   | Layout 1             | `356a73f483d6`  |
| 1363   | Layout 1             | `356a73f483d6`  |
| 1360   | Layout 1             | `356a73f483d6`  |
| 1358   | Layout 1             | `356a73f483d6`  |
| 1355   | Layout 1             | `356a73f483d6`  |
| 1351   | Layout 1             | `356a73f483d6`  |
| 1348   | Layout 1             | `356a73f483d6`  |
| 1346   | Layout 1             | `356a73f483d6`  |
| 1341   | No documented layout | `356a73f483d6`  |
| 1340   | No documented layout | `356a73f483d6`  |
| 1338   | No documented layout | `356a73f483d6`  |
| 1335   | No documented layout | `356a73f483d6`  |
| 1333   | No documented layout | `356a73f483d6`  |
| 1329   | No documented layout | `356a73f483d6`  |
| 1327   | No documented layout | `356a73f483d6`  |
| 1324   | No documented layout | `356a73f483d6`  |
| 1321   | No documented layout | `356a73f483d6`  |
| 1319   | No documented layout | `356a73f483d6`  |
| 1318   | No documented layout | `356a73f483d6`  |
| 1316   | No documented layout | `356a73f483d6`  |
| 1313   | No documented layout | `356a73f483d6`  |
| 1311   | No documented layout | `356a73f483d6`  |
| 1309   | No documented layout | `356a73f483d6`  |
| 1304   | No documented layout | `356a73f483d6`  |
| 1292   | No documented layout | `356a73f483d6`  |
| 1286   | No documented layout | `356a73f483d6`  |
| 1280   | No documented layout | `356a73f483d6`  |
| 1276   | No documented layout | `356a73f483d6`  |
| 1267   | No documented layout | `356a73f483d6`  |
| 1261   | No file              | `356a73f483d6`  |
| 1256   | No file              | `356a73f483d6`  |
| 1250   | No file              | `356a73f483d6`  |
| 1246   | No file              | `356a73f483d6`  |
| 1239   | No file              | `356a73f483d6`  |
| 1230   | No file              | `356a73f483d6`  |
| 1226   | No file              | `356a73f483d6`  |
| 1220   | No file              | `356a73f483d6`  |
| 1217   | No file              | `356a73f483d6`  |
| 1211   | No file              | `356a73f483d6`  |
| 1210   | No file              | `356a73f483d6`  |
| 1208   | No file              | `356a73f483d6`  |
| 1203   | No file              | `356a73f483d6`  |
| 1197   | No file              | `356a73f483d6`  |
| 1194   | No file              | `356a73f483d6`  |
| 1192   | No file              | `356a73f483d6`  |
| 1187   | No file              | `356a73f483d6`  |
| 1183   | No file              | `356a73f483d6`  |
| 1177   | No file              | `356a73f483d6`  |
| 1173   | No file              | `356a73f483d6`  |
| 1167   | No file              | `356a73f483d6`  |
| 1164   | No file              | `356a73f483d6`  |
| 1156   | No file              | `356a73f483d6`  |
| 1149   | No file              | `356a73f483d6`  |
| 1144   | No file              | `356a73f483d6`  |
| 1137   | No file              | `356a73f483d6`  |
| 1132   | No file              | `356a73f483d6`  |
| 1127   | No file              | `356a73f483d6`  |
| 1122   | No file              | `356a73f483d6`  |
| 1118   | No file              | `356a73f483d6`  |
| 1114   | No file              | `356a73f483d6`  |
| 1109   | No file              | `356a73f483d6`  |
| 1102   | No file              | `356a73f483d6`  |
| 1096   | No file              | `356a73f483d6`  |
| 1088   | No file              | `356a73f483d6`  |
| 1081   | No file              | `356a73f483d6`  |
| 1076   | No file              | `356a73f483d6`  |
| 1069   | No file              | `356a73f483d6`  |
| 1064   | No file              | `356a73f483d6`  |
| 1058   | No file              | `356a73f483d6`  |
| 1051   | No file              | `356a73f483d6`  |
| 1044   | No file              | `356a73f483d6`  |
| 1036   | No file              | `356a73f483d6`  |
| 1026   | No file              | `356a73f483d6`  |
| 1016   | No file              | `356a73f483d6`  |
| 1009   | No file              | `356a73f483d6`  |
| 1005   | No file              | `356a73f483d6`  |
| 1000   | No file              | `356a73f483d6`  |
| 998    | No file              | `356a73f483d6`  |
| 990    | No file              | `356a73f483d6`  |
| 979    | No file              | `356a73f483d6`  |
| 972    | No file              | `356a73f483d6`  |
| 963    | No file              | `356a73f483d6`  |
| 955    | No file              | `356a73f483d6`  |
| 946    | No file              | `356a73f483d6`  |
| 938    | No file              | `356a73f483d6`  |
| 927    | No file              | `356a73f483d6`  |
| 911    | No file              | `356a73f483d6`  |
| 904    | No file              | `356a73f483d6`  |
| 899    | No file              | `356a73f483d6`  |
| 894    | No file              | `356a73f483d6`  |
| 885    | No file              | `356a73f483d6`  |
| 879    | No file              | `356a73f483d6`  |
| 872    | No file              | `356a73f483d6`  |
| 864    | No file              | `356a73f483d6`  |
| 855    | No file              | `356a73f483d6`  |
| 853    | No file              | `356a73f483d6`  |
| 845    | No file              | `356a73f483d6`  |
| 837    | No file              | `356a73f483d6`  |
| 829    | No file              | `356a73f483d6`  |
| 822    | No file              | `356a73f483d6`  |
| 814    | No file              | `356a73f483d6`  |
| 805    | No file              | `356a73f483d6`  |
| 794    | No file              | `356a73f483d6`  |
| 787    | No file              | `356a73f483d6`  |
| 780    | No file              | `356a73f483d6`  |
| 771    | No file              | `356a73f483d6`  |
| 760    | No file              | `356a73f483d6`  |
| 748    | No file              | `356a73f483d6`  |
| 741    | No file              | `356a73f483d6`  |
| 736    | No file              | `356a73f483d6`  |
| 731    | No file              | `356a73f483d6`  |
| 723    | No file              | `356a73f483d6`  |
| 711    | No file              | `356a73f483d6`  |
| 707    | No file              | `356a73f483d6`  |
| 697    | No file              | `356a73f483d6`  |
| 689    | No file              | `356a73f483d6`  |
| 683    | No file              | `356a73f483d6`  |
| 678    | No file              | `356a73f483d6`  |
| 670    | No file              | `356a73f483d6`  |
| 661    | No file              | `356a73f483d6`  |
| 656    | No file              | `356a73f483d6`  |
| 652    | No file              | `356a73f483d6`  |
| 643    | No file              | `356a73f483d6`  |
| 637    | No file              | `356a73f483d6`  |
| 630    | No file              | `356a73f483d6`  |
| 627    | No file              | `356a73f483d6`  |
| 621    | No file              | `356a73f483d6`  |
| 617    | No file              | `356a73f483d6`  |
| 615    | No file              | `356a73f483d6`  |
| 606    | No file              | `356a73f483d6`  |
| 599    | No file              | `356a73f483d6`  |
| 592    | No file              | `356a73f483d6`  |
| 586    | No file              | `356a73f483d6`  |
| 577    | No file              | `356a73f483d6`  |
| 569    | No file              | `356a73f483d6`  |
| 561    | No file              | `356a73f483d6`  |
| 554    | No file              | `356a73f483d6`  |
| 542    | No file              | `356a73f483d6`  |
| 532    | No file              | `356a73f483d6`  |
| 531    | No file              | `356a73f483d6`  |
| 526    | No file              | `356a73f483d6`  |
| 521    | No file              | `356a73f483d6`  |
| 517    | No file              | `356a73f483d6`  |
| 510    | No file              | `356a73f483d6`  |
| 508    | No file              | `356a73f483d6`  |
| 504    | No file              | `356a73f483d6`  |
| 497    | No file              | `356a73f483d6`  |
| 491    | No file              | `356a73f483d6`  |
| 485    | No file              | `356a73f483d6`  |
| 478    | No file              | `356a73f483d6`  |
| 472    | No file              | `356a73f483d6`  |
| 466    | No file              | `356a73f483d6`  |
| 457    | No file              | `356a73f483d6`  |
| 452    | No file              | `356a73f483d6`  |
| 449    | No file              | `356a73f483d6`  |
| 435    | No file              | `356a73f483d6`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                               |
| --------------------- | -------- | ------------------------------------------------------------------ |
| `languagedata_en.loc` | Optional | Tier text in the user's language, LOC type 52, see [`languagedata_*.loc`](languagedata_loc.md#type-52-item-set-bonus-text-skillpiecedbss); set skill name, LOC type 10 |

The handler walks the records from the start of the file and does not read
`skillpieceoffset.dbss` (see below). The buffs of each tier's
[`skill.dbss`](skill_dbss.md) rank come from the `SKILL_BUFFS` lookup index.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                                     |
| ------- | ------------- | ------- | ----------------------------------------- |
| `+0x00` | u32           | count   | Number of records; `100` on client 3464   |
| `+0x04` | Record[count] | records | `count` variable-size records, back to back to the end of the file |

### Record (variable: 14 bytes + tiers)

| Offset       | Type             | Field          | Notes                                                        |
| ------------ | ---------------- | -------------- | ------------------------------------------------------------ |
| `+0x00`      | u16              | key_prefix     | Equals `skill_no`; the index's `data_offset` points past it  |
| `+0x02`      | u16              | skill_no       | The set skill, a `skill.dbss` skill number                   |
| `+0x04`      | u16              | skill_property | `0` in every record (client 3474); see Field Names           |
| `+0x06`      | u32              | tier_count     | Number of tiers; `1` to `13`                                 |
| `+0x0A`      | Tier[tier_count] | tiers          | `tier_count` tiers                                           |
| `tiers+0x00` | u32              | unknown_end    | `0` in every record                                          |

### Tier (variable: 30 bytes + text)

| Offset                | Type  | Field           | Notes                                                       |
| --------------------- | ----- | --------------- | ----------------------------------------------------------- |
| `+0x00`               | u32   | point           | Set points needed; rises from tier to tier; Lua `getPoint()` |
| `+0x04`               | u16   | level           | `skill.dbss` rank of the set skill; `1` to `tier_count` in order |
| `+0x06`               | str16 | group_title_kr  | Set title, `아그리스 세트 효과` ("Agris Set Effect"); the same in every tier of a record; Lua `getGroupTitle()` |
| `group_title_kr+0x00` | str16 | desc_title_kr   | Threshold label: `2부위` ("2 Parts"), `2개` ("x2"), `세트`, `6 포인트`, `목걸이, 허리띠 부위`; Lua `getDescTitle()` |
| `desc_title_kr+0x00`  | str16 | desc_kr         | Bonus lines, values in `<PAColor0xffe9bd23>` tags; Lua `getDesc()` |

A string is a u32 character count, a u32 `0` and that many UTF-16LE code
units with no terminator (`_common/record_reader.py` reads it with a u64
count). A line break is stored as the two characters `\n` (99 times on client
3464) or as a real newline (10 times); the parser turns both into a newline
with `decode_inline_text()`. All three strings are empty in every tier of 13 records (client 3464):
the Ancient Magic Crystal activation conditions `50047` to `50055`, the
matching boss weapons `50060` to `50068`, Serenity `50198`, and the Pearl Shop
outfits `44953` and `44954`.

### `skillpieceoffset.dbss`

| Offset  | Type             | Field | Notes                                     |
| ------- | ---------------- | ----- | ----------------------------------------- |
| `+0x00` | u32              | count | Equals the `skillpiece.dbss` count        |
| `+0x04` | Index Row[count] | rows  | `count` 10-byte rows; no magic, no trailer |

### Index Row (10 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u16  | skill_no    | Record key                                               |
| `+0x02` | u32  | data_offset | Record start + 2, past `key_prefix`                      |
| `+0x06` | u32  | data_size   | Record size - 2                                          |

The rows are in neither key nor file order (the first row is `51128`, the
second record). `parse_bare_offset_rows` (`_common/pabr_offset.py`) reads
them, and on client 3464 every row matches the record walked from the start
of the file. `test_every_offset_row_points_past_its_records_key_prefix` in the
handler tests checks this against the installed client.

## Field Names

The record is the `PointSkill_Table` sheet of a private server on client
1784 (`SkillNo`, `SkillProperty`, `Point`, `SkillLevel`, `GroupNo`,
`GroupTitle`, `Title`, `Description`). That server's dump
(`Instance_dumpFull.exe`) reads the client record from `+0x02` (row reader
at VA `0x140c85c00`) as a u16 into `SkillPieceStaticStatus` `+0x00`, a u16
into `+0x02`, the tier count and tiers, then a u32 into `+0x28`. The sheet
loader writes `SkillNo` to `+0x00` and `SkillProperty` to `+0x02` (VA
`0x140c866f6` and `0x140c866fa`), so `skill_no` is a u16 and the next u16 is
`skill_property`. Each tier's `Point` and `SkillLevel` are `point` and
`level`, and its three texts are `GroupTitle`, `Title` and `Description`.

The private server's own file holds 269 of the sheet's 270 set skills; a
sheet `SkillNo` above 65,535 (79223 to 79403) is stored as its low 16
bits (13687 to 13867). `SkillProperty` is `0` on all 315 sheet rows and
`skill_property` on every record of that file and of client 3474. The
struct starts it at `5` before the sheet sets it, and one dump function
uses it as an index into a u32 array; what the values mean is open.

`unknown_end` has no sheet column. The sheet loader sets `+0x28` to `0`,
the reader loads it from the file, and none of the five callers of the
record getter reads it. It is `0` on every record of both clients.

## Notes

- The set effect tooltip Lua (`panel_equiment_seteffecttooltip`) reads one
  entry per tier from `ToClient_GetSkillPieceInfo()` through `getSkillNo()`,
  `getPoint()`, `getGroupTitle()`, `getDescTitle()`, `getDesc()` and
  `getApply()`. The field names here follow those getters. `getApply()` is
  whether the character has the tier active: the Lua stores it as `isApplied`
  and keeps the highest `point` among applied tiers. A stored `level`, `1` or
  more, would mark every tier as applied.
- `level` is the skill rank: all 168 tiers (client 3464) have a
  `skill.dbss` rank `skill_no << 16 | level`, and no record's skill has a rank
  past its last tier. The ranks carry the buffs; the strings here are only the
  tooltip. No getter in the tooltip Lua returns it.
- `point` is the threshold, not a piece count. The type 48 buff of a piece
  adds `param_2` points: `1` on 107 of the 123 buffs (client 3464), `2` to
  `4` on buffs of 7 set skills, most of them Pearl Shop outfits (`59184`
  takes `1` to `4` and one `-4`), and `10` on the one buff of `50049`. A
  label such as `세트` or `6 포인트` stands for a points total. 99 of the 100
  keys are the `param_1` of at least one type 48 buff; `50589` ("[Set] Black
  Eye Skill Activation Requirements") is not. The items that apply those
  buffs are the set's pieces.
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  reads the same layout (`internal/tables/skillpiece.go`) with two other
  readings: `pieces` for `point`, the equipped-piece threshold, and `apply` for
  `level`, "the tier ordinal exposed by Lua as `getApply()`". The tooltip Lua
  above uses `getApply()` as the active flag, and the outfit pieces of `59184`
  add up to `4` points each.
- LOC type 52 keys a tier by `str_id1 = skill_no` and `str_id2 = level`. On
  client 3464 the 87 records with Korean text have LOC rows for every tier, and
  the 13 records without text have none. `56050` has LOC rows for levels 3 and
  4 (`x8`, `x10`) that its record and `skill.dbss` lack.
- The English text can differ from the Korean values: `59184` reads `Combat
  EXP +10%` in LOC and `+50%` in `desc_kr`.

## Open Questions

### `unknown_end`

The u32 after the tiers is `0` in all 100 records (client 3474) and in all
269 of client 1784. No sheet column fills it and no code in the client 1784
server dump reads it (Field Names). No field elsewhere points at it.

### Black Eye set points

`50589` has a record (3 points, level 1, `검은눈 효과`) but no type 48 buff
adds points to it, so it is open how the Black Eye pieces count toward it.
