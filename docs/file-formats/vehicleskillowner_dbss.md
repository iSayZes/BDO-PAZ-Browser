# `vehicleskillowner.dbss` Format

## Purpose

Which [vehicleskill.dbss](vehicleskill_dbss.md) skills each servant can
learn: one record per servant character with a list of skill keys, each
with a learn value, an EXP value and a learn flag. On client 3474 the file
has 366 records, every one a `servant.bss` character, with 0 to 37 skills
each (5,620 in all).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes  | Records                 | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ------ | ----------------------- | --------- |
| 2      | 2474 and later | 3483    | `vehicleskillowner.dbss`       | 94,316 | 5,620 Skill, 366 Record | 16        |
| 2      | 2474 and later | 3483    | `vehicleskillowneroffset.dbss` | 3,680  | 366 Offset Row          | 10        |
| 1      | 1346 to 2468   | 2468    | `vehicleskillowner.dbss`       | 62,907 | 4,643 Skill, 318 Record | 13        |
| 1      | 1346 to 2468   | 2468    | `vehicleskillowneroffset.dbss` | 3,200  | 318 Offset Row          | 10        |

| Layout | File                           | Known            | Unknown          |
| ------ | ------------------------------ | ---------------- | ---------------- |
| 2      | `vehicleskillowner.dbss`       | 77,456 B (82.1%) | 16,860 B (17.9%) |
| 2      | `vehicleskillowneroffset.dbss` | 3,680 B (100.0%) | 0 B (0.0%)       |
| 1      | `vehicleskillowner.dbss`       | 48,978 B (77.9%) | 13,929 B (22.1%) |
| 1      | `vehicleskillowneroffset.dbss` | 3,200 B (100.0%) | 0 B (0.0%)       |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `92d18e73062e`  |
| 3482   | Layout 2             | `92d18e73062e`  |
| 3474   | Layout 2             | `92d18e73062e`  |
| 3473   | Layout 2             | `92d18e73062e`  |
| 3464   | Layout 2             | `92d18e73062e`  |
| 3458   | Layout 2             | `92d18e73062e`  |
| 3454   | Layout 2             | `92d18e73062e`  |
| 3444   | Layout 2             | `92d18e73062e`  |
| 3435   | Layout 2             | `92d18e73062e`  |
| 3426   | Layout 2             | `92d18e73062e`  |
| 3418   | Layout 2             | `92d18e73062e`  |
| 3412   | Layout 2             | `92d18e73062e`  |
| 3402   | Layout 2             | `92d18e73062e`  |
| 3396   | Layout 2             | `92d18e73062e`  |
| 3387   | Layout 2             | `92d18e73062e`  |
| 3381   | Layout 2             | `92d18e73062e`  |
| 3373   | Layout 2             | `92d18e73062e`  |
| 3364   | Layout 2             | `92d18e73062e`  |
| 3356   | Layout 2             | `92d18e73062e`  |
| 3349   | Layout 2             | `92d18e73062e`  |
| 3342   | Layout 2             | `92d18e73062e`  |
| 3335   | Layout 2             | `92d18e73062e`  |
| 3326   | Layout 2             | `92d18e73062e`  |
| 3321   | Layout 2             | `92d18e73062e`  |
| 3314   | Layout 2             | `92d18e73062e`  |
| 3303   | Layout 2             | `92d18e73062e`  |
| 3302   | Layout 2             | `92d18e73062e`  |
| 3293   | Layout 2             | `92d18e73062e`  |
| 3283   | Layout 2             | `92d18e73062e`  |
| 3275   | Layout 2             | `92d18e73062e`  |
| 3267   | Layout 2             | `92d18e73062e`  |
| 3258   | Layout 2             | `92d18e73062e`  |
| 3251   | Layout 2             | `92d18e73062e`  |
| 3242   | Layout 2             | `92d18e73062e`  |
| 3235   | Layout 2             | `92d18e73062e`  |
| 3229   | Layout 2             | `92d18e73062e`  |
| 3212   | Layout 2             | `92d18e73062e`  |
| 3203   | Layout 2             | `92d18e73062e`  |
| 3193   | Layout 2             | `92d18e73062e`  |
| 3186   | Layout 2             | `92d18e73062e`  |
| 3177   | Layout 2             | `92d18e73062e`  |
| 3169   | Layout 2             | `92d18e73062e`  |
| 3158   | Layout 2             | `92d18e73062e`  |
| 3151   | Layout 2             | `92d18e73062e`  |
| 3144   | Layout 2             | `92d18e73062e`  |
| 3133   | Layout 2             | `92d18e73062e`  |
| 3125   | Layout 2             | `92d18e73062e`  |
| 3118   | Layout 2             | `92d18e73062e`  |
| 3111   | Layout 2             | `92d18e73062e`  |
| 3103   | Layout 2             | `92d18e73062e`  |
| 3095   | Layout 2             | `92d18e73062e`  |
| 3086   | Layout 2             | `92d18e73062e`  |
| 3072   | Layout 2             | `92d18e73062e`  |
| 3062   | Layout 2             | `92d18e73062e`  |
| 3052   | Layout 2             | `92d18e73062e`  |
| 3045   | Layout 2             | `92d18e73062e`  |
| 3037   | Layout 2             | `92d18e73062e`  |
| 3030   | Layout 2             | `92d18e73062e`  |
| 3021   | Layout 2             | `92d18e73062e`  |
| 3012   | Layout 2             | `92d18e73062e`  |
| 3002   | Layout 2             | `92d18e73062e`  |
| 2995   | Layout 2             | `92d18e73062e`  |
| 2987   | Layout 2             | `92d18e73062e`  |
| 2978   | Layout 2             | `92d18e73062e`  |
| 2970   | Layout 2             | `92d18e73062e`  |
| 2959   | Layout 2             | `92d18e73062e`  |
| 2951   | Layout 2             | `92d18e73062e`  |
| 2942   | Layout 2             | `92d18e73062e`  |
| 2935   | Layout 2             | `92d18e73062e`  |
| 2932   | Layout 2             | `92d18e73062e`  |
| 2923   | Layout 2             | `92d18e73062e`  |
| 2919   | Layout 2             | `92d18e73062e`  |
| 2907   | Layout 2             | `92d18e73062e`  |
| 2900   | Layout 2             | `92d18e73062e`  |
| 2891   | Layout 2             | `92d18e73062e`  |
| 2882   | Layout 2             | `92d18e73062e`  |
| 2872   | Layout 2             | `92d18e73062e`  |
| 2863   | Layout 2             | `92d18e73062e`  |
| 2855   | Layout 2             | `92d18e73062e`  |
| 2849   | Layout 2             | `92d18e73062e`  |
| 2844   | Layout 2             | `92d18e73062e`  |
| 2834   | Layout 2             | `92d18e73062e`  |
| 2825   | Layout 2             | `92d18e73062e`  |
| 2819   | Layout 2             | `92d18e73062e`  |
| 2811   | Layout 2             | `92d18e73062e`  |
| 2803   | Layout 2             | `92d18e73062e`  |
| 2794   | Layout 2             | `92d18e73062e`  |
| 2783   | Layout 2             | `92d18e73062e`  |
| 2774   | Layout 2             | `92d18e73062e`  |
| 2765   | Layout 2             | `92d18e73062e`  |
| 2756   | Layout 2             | `92d18e73062e`  |
| 2750   | Layout 2             | `92d18e73062e`  |
| 2743   | Layout 2             | `92d18e73062e`  |
| 2736   | Layout 2             | `92d18e73062e`  |
| 2726   | Layout 2             | `92d18e73062e`  |
| 2717   | Layout 2             | `92d18e73062e`  |
| 2709   | Layout 2             | `92d18e73062e`  |
| 2703   | Layout 2             | `92d18e73062e`  |
| 2695   | Layout 2             | `92d18e73062e`  |
| 2684   | Layout 2             | `92d18e73062e`  |
| 2672   | Layout 2             | `92d18e73062e`  |
| 2665   | Layout 2             | `92d18e73062e`  |
| 2657   | Layout 2             | `92d18e73062e`  |
| 2649   | Layout 2             | `92d18e73062e`  |
| 2644   | Layout 2             | `92d18e73062e`  |
| 2637   | Layout 2             | `92d18e73062e`  |
| 2629   | Layout 2             | `92d18e73062e`  |
| 2619   | Layout 2             | `92d18e73062e`  |
| 2612   | Layout 2             | `92d18e73062e`  |
| 2606   | Layout 2             | `92d18e73062e`  |
| 2602   | Layout 2             | `92d18e73062e`  |
| 2601   | Layout 2             | `92d18e73062e`  |
| 2592   | Layout 2             | `92d18e73062e`  |
| 2583   | Layout 2             | `92d18e73062e`  |
| 2575   | Layout 2             | `92d18e73062e`  |
| 2567   | Layout 2             | `92d18e73062e`  |
| 2560   | Layout 2             | `92d18e73062e`  |
| 2553   | Layout 2             | `92d18e73062e`  |
| 2545   | Layout 2             | `92d18e73062e`  |
| 2538   | Layout 2             | `92d18e73062e`  |
| 2529   | Layout 2             | `92d18e73062e`  |
| 2519   | Layout 2             | `92d18e73062e`  |
| 2513   | Layout 2             | `92d18e73062e`  |
| 2510   | Layout 2             | `92d18e73062e`  |
| 2507   | Layout 2             | `92d18e73062e`  |
| 2503   | Layout 2             | `92d18e73062e`  |
| 2498   | Layout 2             | `92d18e73062e`  |
| 2492   | Layout 2             | `92d18e73062e`  |
| 2487   | Layout 2             | `92d18e73062e`  |
| 2480   | Layout 2             | `92d18e73062e`  |
| 2474   | Layout 2             | `92d18e73062e`  |
| 2468   | Layout 1             | `92d18e73062e`  |
| 2460   | Layout 1             | `92d18e73062e`  |
| 2453   | Layout 1             | `92d18e73062e`  |
| 2444   | Layout 1             | `92d18e73062e`  |
| 2438   | Layout 1             | `92d18e73062e`  |
| 2434   | Layout 1             | `92d18e73062e`  |
| 2429   | Layout 1             | `92d18e73062e`  |
| 2421   | Layout 1             | `92d18e73062e`  |
| 2414   | Layout 1             | `92d18e73062e`  |
| 2407   | Layout 1             | `92d18e73062e`  |
| 2401   | Layout 1             | `92d18e73062e`  |
| 2397   | Layout 1             | `92d18e73062e`  |
| 2393   | Layout 1             | `92d18e73062e`  |
| 2384   | Layout 1             | `92d18e73062e`  |
| 2378   | Layout 1             | `92d18e73062e`  |
| 2372   | Layout 1             | `92d18e73062e`  |
| 2358   | Layout 1             | `92d18e73062e`  |
| 2352   | Layout 1             | `92d18e73062e`  |
| 2347   | Layout 1             | `92d18e73062e`  |
| 2343   | Layout 1             | `92d18e73062e`  |
| 2335   | Layout 1             | `92d18e73062e`  |
| 2327   | Layout 1             | `92d18e73062e`  |
| 2324   | Layout 1             | `92d18e73062e`  |
| 2319   | Layout 1             | `92d18e73062e`  |
| 2313   | Layout 1             | `92d18e73062e`  |
| 2308   | Layout 1             | `92d18e73062e`  |
| 2302   | Layout 1             | `92d18e73062e`  |
| 2295   | Layout 1             | `92d18e73062e`  |
| 2290   | Layout 1             | `92d18e73062e`  |
| 2284   | Layout 1             | `92d18e73062e`  |
| 2276   | Layout 1             | `92d18e73062e`  |
| 2269   | Layout 1             | `92d18e73062e`  |
| 2259   | Layout 1             | `92d18e73062e`  |
| 2250   | Layout 1             | `92d18e73062e`  |
| 2243   | Layout 1             | `92d18e73062e`  |
| 2235   | Layout 1             | `92d18e73062e`  |
| 2229   | Layout 1             | `92d18e73062e`  |
| 2224   | Layout 1             | `92d18e73062e`  |
| 2218   | Layout 1             | `92d18e73062e`  |
| 2215   | Layout 1             | `92d18e73062e`  |
| 2207   | Layout 1             | `92d18e73062e`  |
| 2203   | Layout 1             | `92d18e73062e`  |
| 2196   | Layout 1             | `92d18e73062e`  |
| 2192   | Layout 1             | `92d18e73062e`  |
| 2189   | Layout 1             | `92d18e73062e`  |
| 2183   | Layout 1             | `92d18e73062e`  |
| 2179   | Layout 1             | `92d18e73062e`  |
| 2171   | Layout 1             | `92d18e73062e`  |
| 2163   | Layout 1             | `92d18e73062e`  |
| 2156   | Layout 1             | `92d18e73062e`  |
| 2151   | Layout 1             | `92d18e73062e`  |
| 2147   | Layout 1             | `92d18e73062e`  |
| 2142   | Layout 1             | `92d18e73062e`  |
| 2138   | Layout 1             | `92d18e73062e`  |
| 2134   | Layout 1             | `92d18e73062e`  |
| 2130   | Layout 1             | `92d18e73062e`  |
| 2122   | Layout 1             | `92d18e73062e`  |
| 2107   | Layout 1             | `92d18e73062e`  |
| 2098   | Layout 1             | `92d18e73062e`  |
| 2089   | Layout 1             | `92d18e73062e`  |
| 2081   | Layout 1             | `92d18e73062e`  |
| 2073   | Layout 1             | `92d18e73062e`  |
| 2067   | Layout 1             | `92d18e73062e`  |
| 2063   | Layout 1             | `92d18e73062e`  |
| 2059   | Layout 1             | `92d18e73062e`  |
| 2052   | Layout 1             | `92d18e73062e`  |
| 2044   | Layout 1             | `92d18e73062e`  |
| 2039   | Layout 1             | `92d18e73062e`  |
| 2032   | Layout 1             | `92d18e73062e`  |
| 2025   | Layout 1             | `92d18e73062e`  |
| 2011   | Layout 1             | `92d18e73062e`  |
| 2005   | Layout 1             | `92d18e73062e`  |
| 2000   | Layout 1             | `92d18e73062e`  |
| 1996   | Layout 1             | `92d18e73062e`  |
| 1991   | Layout 1             | `92d18e73062e`  |
| 1985   | Layout 1             | `92d18e73062e`  |
| 1980   | Layout 1             | `92d18e73062e`  |
| 1969   | Layout 1             | `92d18e73062e`  |
| 1964   | Layout 1             | `92d18e73062e`  |
| 1958   | Layout 1             | `92d18e73062e`  |
| 1950   | Layout 1             | `92d18e73062e`  |
| 1945   | Layout 1             | `92d18e73062e`  |
| 1937   | Layout 1             | `92d18e73062e`  |
| 1933   | Layout 1             | `92d18e73062e`  |
| 1927   | Layout 1             | `92d18e73062e`  |
| 1921   | Layout 1             | `92d18e73062e`  |
| 1914   | Layout 1             | `92d18e73062e`  |
| 1908   | Layout 1             | `92d18e73062e`  |
| 1897   | Layout 1             | `92d18e73062e`  |
| 1892   | Layout 1             | `92d18e73062e`  |
| 1886   | Layout 1             | `92d18e73062e`  |
| 1881   | Layout 1             | `92d18e73062e`  |
| 1871   | Layout 1             | `92d18e73062e`  |
| 1866   | Layout 1             | `92d18e73062e`  |
| 1862   | Layout 1             | `92d18e73062e`  |
| 1854   | Layout 1             | `92d18e73062e`  |
| 1846   | Layout 1             | `92d18e73062e`  |
| 1838   | Layout 1             | `92d18e73062e`  |
| 1832   | Layout 1             | `92d18e73062e`  |
| 1826   | Layout 1             | `92d18e73062e`  |
| 1822   | Layout 1             | `92d18e73062e`  |
| 1818   | Layout 1             | `92d18e73062e`  |
| 1804   | Layout 1             | `92d18e73062e`  |
| 1794   | Layout 1             | `92d18e73062e`  |
| 1790   | Layout 1             | `92d18e73062e`  |
| 1784   | Layout 1             | `92d18e73062e`  |
| 1774   | Layout 1             | `92d18e73062e`  |
| 1771   | Layout 1             | `92d18e73062e`  |
| 1762   | Layout 1             | `92d18e73062e`  |
| 1759   | Layout 1             | `92d18e73062e`  |
| 1754   | Layout 1             | `92d18e73062e`  |
| 1749   | Layout 1             | `92d18e73062e`  |
| 1743   | Layout 1             | `92d18e73062e`  |
| 1737   | Layout 1             | `92d18e73062e`  |
| 1731   | Layout 1             | `92d18e73062e`  |
| 1725   | Layout 1             | `92d18e73062e`  |
| 1717   | Layout 1             | `92d18e73062e`  |
| 1710   | Layout 1             | `92d18e73062e`  |
| 1704   | Layout 1             | `92d18e73062e`  |
| 1698   | Layout 1             | `92d18e73062e`  |
| 1690   | Layout 1             | `92d18e73062e`  |
| 1685   | Layout 1             | `92d18e73062e`  |
| 1680   | Layout 1             | `92d18e73062e`  |
| 1674   | Layout 1             | `92d18e73062e`  |
| 1668   | Layout 1             | `92d18e73062e`  |
| 1659   | Layout 1             | `92d18e73062e`  |
| 1649   | Layout 1             | `92d18e73062e`  |
| 1642   | Layout 1             | `92d18e73062e`  |
| 1636   | Layout 1             | `92d18e73062e`  |
| 1628   | Layout 1             | `92d18e73062e`  |
| 1622   | Layout 1             | `92d18e73062e`  |
| 1614   | Layout 1             | `92d18e73062e`  |
| 1608   | Layout 1             | `92d18e73062e`  |
| 1602   | Layout 1             | `92d18e73062e`  |
| 1598   | Layout 1             | `92d18e73062e`  |
| 1594   | Layout 1             | `92d18e73062e`  |
| 1590   | Layout 1             | `92d18e73062e`  |
| 1587   | Layout 1             | `92d18e73062e`  |
| 1584   | Layout 1             | `92d18e73062e`  |
| 1579   | Layout 1             | `92d18e73062e`  |
| 1572   | Layout 1             | `92d18e73062e`  |
| 1565   | Layout 1             | `92d18e73062e`  |
| 1559   | Layout 1             | `92d18e73062e`  |
| 1554   | Layout 1             | `92d18e73062e`  |
| 1547   | Layout 1             | `92d18e73062e`  |
| 1537   | Layout 1             | `92d18e73062e`  |
| 1529   | Layout 1             | `92d18e73062e`  |
| 1524   | Layout 1             | `92d18e73062e`  |
| 1519   | Layout 1             | `92d18e73062e`  |
| 1509   | Layout 1             | `92d18e73062e`  |
| 1506   | Layout 1             | `92d18e73062e`  |
| 1504   | Layout 1             | `92d18e73062e`  |
| 1500   | Layout 1             | `92d18e73062e`  |
| 1493   | Layout 1             | `92d18e73062e`  |
| 1489   | Layout 1             | `92d18e73062e`  |
| 1485   | Layout 1             | `92d18e73062e`  |
| 1481   | Layout 1             | `92d18e73062e`  |
| 1474   | Layout 1             | `92d18e73062e`  |
| 1466   | Layout 1             | `92d18e73062e`  |
| 1462   | Layout 1             | `92d18e73062e`  |
| 1459   | Layout 1             | `92d18e73062e`  |
| 1453   | Layout 1             | `92d18e73062e`  |
| 1450   | Layout 1             | `92d18e73062e`  |
| 1445   | Layout 1             | `92d18e73062e`  |
| 1439   | Layout 1             | `92d18e73062e`  |
| 1433   | Layout 1             | `92d18e73062e`  |
| 1430   | Layout 1             | `92d18e73062e`  |
| 1426   | Layout 1             | `92d18e73062e`  |
| 1421   | Layout 1             | `92d18e73062e`  |
| 1417   | Layout 1             | `92d18e73062e`  |
| 1416   | Layout 1             | `92d18e73062e`  |
| 1409   | Layout 1             | `92d18e73062e`  |
| 1405   | Layout 1             | `92d18e73062e`  |
| 1401   | Layout 1             | `92d18e73062e`  |
| 1396   | Layout 1             | `92d18e73062e`  |
| 1391   | Layout 1             | `92d18e73062e`  |
| 1390   | Layout 1             | `92d18e73062e`  |
| 1386   | Layout 1             | `92d18e73062e`  |
| 1381   | Layout 1             | `92d18e73062e`  |
| 1379   | Layout 1             | `92d18e73062e`  |
| 1372   | Layout 1             | `92d18e73062e`  |
| 1366   | Layout 1             | `92d18e73062e`  |
| 1364   | Layout 1             | `92d18e73062e`  |
| 1363   | Layout 1             | `92d18e73062e`  |
| 1360   | Layout 1             | `92d18e73062e`  |
| 1358   | Layout 1             | `92d18e73062e`  |
| 1355   | Layout 1             | `92d18e73062e`  |
| 1351   | Layout 1             | `92d18e73062e`  |
| 1348   | Layout 1             | `92d18e73062e`  |
| 1346   | Layout 1             | `92d18e73062e`  |
| 1341   | No documented layout | `92d18e73062e`  |
| 1340   | No documented layout | `92d18e73062e`  |
| 1338   | No documented layout | `92d18e73062e`  |
| 1335   | No documented layout | `92d18e73062e`  |
| 1333   | No documented layout | `92d18e73062e`  |
| 1329   | No documented layout | `92d18e73062e`  |
| 1327   | No documented layout | `92d18e73062e`  |
| 1324   | No documented layout | `92d18e73062e`  |
| 1321   | No documented layout | `92d18e73062e`  |
| 1319   | No documented layout | `92d18e73062e`  |
| 1318   | No documented layout | `92d18e73062e`  |
| 1316   | No documented layout | `92d18e73062e`  |
| 1313   | No documented layout | `92d18e73062e`  |
| 1311   | No documented layout | `92d18e73062e`  |
| 1309   | No documented layout | `92d18e73062e`  |
| 1304   | No documented layout | `92d18e73062e`  |
| 1292   | No documented layout | `92d18e73062e`  |
| 1286   | No documented layout | `92d18e73062e`  |
| 1280   | No file              | `92d18e73062e`  |
| 1276   | No documented layout | `92d18e73062e`  |
| 1267   | No documented layout | `92d18e73062e`  |
| 1261   | No documented layout | `92d18e73062e`  |
| 1256   | No file              | `92d18e73062e`  |
| 1250   | No file              | `92d18e73062e`  |
| 1246   | No file              | `92d18e73062e`  |
| 1239   | No file              | `92d18e73062e`  |
| 1230   | No file              | `92d18e73062e`  |
| 1226   | No file              | `92d18e73062e`  |
| 1220   | No file              | `92d18e73062e`  |
| 1217   | No file              | `92d18e73062e`  |
| 1211   | No file              | `92d18e73062e`  |
| 1210   | No file              | `92d18e73062e`  |
| 1208   | No file              | `92d18e73062e`  |
| 1203   | No file              | `92d18e73062e`  |
| 1197   | No file              | `92d18e73062e`  |
| 1194   | No file              | `92d18e73062e`  |
| 1192   | No file              | `92d18e73062e`  |
| 1187   | No file              | `92d18e73062e`  |
| 1183   | No file              | `92d18e73062e`  |
| 1177   | No file              | `92d18e73062e`  |
| 1173   | No file              | `92d18e73062e`  |
| 1167   | No file              | `92d18e73062e`  |
| 1164   | No file              | `92d18e73062e`  |
| 1156   | No file              | `92d18e73062e`  |
| 1149   | No file              | `92d18e73062e`  |
| 1144   | No file              | `92d18e73062e`  |
| 1137   | No file              | `92d18e73062e`  |
| 1132   | No file              | `92d18e73062e`  |
| 1127   | No file              | `92d18e73062e`  |
| 1122   | No file              | `92d18e73062e`  |
| 1118   | No file              | `92d18e73062e`  |
| 1114   | No file              | `92d18e73062e`  |
| 1109   | No file              | `92d18e73062e`  |
| 1102   | No file              | `92d18e73062e`  |
| 1096   | No file              | `92d18e73062e`  |
| 1088   | No file              | `92d18e73062e`  |
| 1081   | No file              | `92d18e73062e`  |
| 1076   | No file              | `92d18e73062e`  |
| 1069   | No file              | `92d18e73062e`  |
| 1064   | No file              | `92d18e73062e`  |
| 1058   | No file              | `92d18e73062e`  |
| 1051   | No file              | `92d18e73062e`  |
| 1044   | No file              | `92d18e73062e`  |
| 1036   | No file              | `92d18e73062e`  |
| 1026   | No file              | `92d18e73062e`  |
| 1016   | No file              | `92d18e73062e`  |
| 1009   | No file              | `92d18e73062e`  |
| 1005   | No file              | `92d18e73062e`  |
| 1000   | No file              | `92d18e73062e`  |
| 998    | No file              | `92d18e73062e`  |
| 990    | No file              | `92d18e73062e`  |
| 979    | No file              | `92d18e73062e`  |
| 972    | No file              | `92d18e73062e`  |
| 963    | No file              | `92d18e73062e`  |
| 955    | No file              | `92d18e73062e`  |
| 946    | No file              | `92d18e73062e`  |
| 938    | No file              | `92d18e73062e`  |
| 927    | No file              | `92d18e73062e`  |
| 911    | No file              | `92d18e73062e`  |
| 904    | No file              | `92d18e73062e`  |
| 899    | No file              | `92d18e73062e`  |
| 894    | No file              | `92d18e73062e`  |
| 885    | No file              | `92d18e73062e`  |
| 879    | No file              | `92d18e73062e`  |
| 872    | No file              | `92d18e73062e`  |
| 864    | No file              | `92d18e73062e`  |
| 855    | No file              | `92d18e73062e`  |
| 853    | No file              | `92d18e73062e`  |
| 845    | No file              | `92d18e73062e`  |
| 837    | No file              | `92d18e73062e`  |
| 829    | No file              | `92d18e73062e`  |
| 822    | No file              | `92d18e73062e`  |
| 814    | No file              | `92d18e73062e`  |
| 805    | No file              | `92d18e73062e`  |
| 794    | No file              | `92d18e73062e`  |
| 787    | No file              | `92d18e73062e`  |
| 780    | No file              | `92d18e73062e`  |
| 771    | No file              | `92d18e73062e`  |
| 760    | No file              | `92d18e73062e`  |
| 748    | No file              | `92d18e73062e`  |
| 741    | No file              | `92d18e73062e`  |
| 736    | No file              | `92d18e73062e`  |
| 731    | No file              | `92d18e73062e`  |
| 723    | No file              | `92d18e73062e`  |
| 711    | No file              | `92d18e73062e`  |
| 707    | No file              | `92d18e73062e`  |
| 697    | No file              | `92d18e73062e`  |
| 689    | No file              | `92d18e73062e`  |
| 683    | No file              | `92d18e73062e`  |
| 678    | No file              | `92d18e73062e`  |
| 670    | No file              | `92d18e73062e`  |
| 661    | No file              | `92d18e73062e`  |
| 656    | No file              | `92d18e73062e`  |
| 652    | No file              | `92d18e73062e`  |
| 643    | No file              | `92d18e73062e`  |
| 637    | No file              | `92d18e73062e`  |
| 630    | No file              | `92d18e73062e`  |
| 627    | No file              | `92d18e73062e`  |
| 621    | No file              | `92d18e73062e`  |
| 617    | No file              | `92d18e73062e`  |
| 615    | No file              | `92d18e73062e`  |
| 606    | No file              | `92d18e73062e`  |
| 599    | No file              | `92d18e73062e`  |
| 592    | No file              | `92d18e73062e`  |
| 586    | No file              | `92d18e73062e`  |
| 577    | No file              | `92d18e73062e`  |
| 569    | No file              | `92d18e73062e`  |
| 561    | No file              | `92d18e73062e`  |
| 554    | No file              | `92d18e73062e`  |
| 542    | No file              | `92d18e73062e`  |
| 532    | No file              | `92d18e73062e`  |
| 531    | No file              | `92d18e73062e`  |
| 526    | No file              | `92d18e73062e`  |
| 521    | No file              | `92d18e73062e`  |
| 517    | No file              | `92d18e73062e`  |
| 510    | No file              | `92d18e73062e`  |
| 508    | No file              | `92d18e73062e`  |
| 504    | No file              | `92d18e73062e`  |
| 497    | No file              | `92d18e73062e`  |
| 491    | No file              | `92d18e73062e`  |
| 485    | No file              | `92d18e73062e`  |
| 478    | No file              | `92d18e73062e`  |
| 472    | No file              | `92d18e73062e`  |
| 466    | No file              | `92d18e73062e`  |
| 457    | No file              | `92d18e73062e`  |
| 452    | No file              | `92d18e73062e`  |
| 449    | No file              | `92d18e73062e`  |
| 435    | No file              | `92d18e73062e`  |

<!-- versions:end -->

## Companion Files

| File                           | Required | Role                                                    |
| ------------------------------ | -------- | ------------------------------------------------------- |
| `vehicleskillowneroffset.dbss` | Optional | PABR index: character ID to the record's offset and size |
| `vehicleskill.dbss`            | Optional | The skills `skill_key` points at; their Korean names when LOC has none |
| `characterstaticoffset.dbss`   | Optional | Every `characterstatic.dbss` key, so a `character_id` without a row shows as plain text instead of a link |
| `languagedata_en.loc`          | Optional | Servant names (LOC type 6) and skill names (LOC type 8) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                  |
| ------- | ------------- | ------- | -------------------------------------- |
| `+0x00` | u32           | count   | 366 on client 3474                     |
| `+0x04` | Record[count] | records | Back to back, variable size, up to EOF |

### Record (variable: 12 bytes + skills)

| Offset  | Type                | Field            | Notes |
| ------- | ------------------- | ---------------- | ----- |
| `+0x00` | u16                 | character_id     | Servant character, as in `servant.bss` |
| `+0x02` | u16                 | character_id_dup | Equals `character_id` on every record |
| `+0x04` | u32                 | cant_learnable_rate | Weight of "Does not learn" ([Learn Chance](#learn-chance)); 0 on 218 records, up to 1,000,000 on 148 (client 3474) |
| `+0x08` | u32                 | skill_count      | 0 to 37 on client 3474 |
| `+0x0C` | Skill[skill_count]  | skills           | In `skill_key` order |

### Skill (16 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u32  | skill_key  | `vehicleskill.dbss` key, 1 to 106 on client 3474 |
| `+0x04` | u32  | able       | 1,000,000 on 996 of 5,620 entries (client 3474) |
| `+0x08` | u32  | add_exp    | |
| `+0x0C` | u8   | is_learn   | 0 on 153 entries (client 3474) |
| `+0x0D` | u8   | unknown_0d | 2 on every entry (client 3474) |
| `+0x0E` | u16  | unknown_0e | `0` on every entry (clients 1784 and 3474) |

### `vehicleskillowneroffset.dbss`

| Offset              | Type              | Field              | Notes                              |
| ------------------- | ----------------- | ------------------ | ---------------------------------- |
| `+0x00`             | char[4]           | magic              | `PABR`                             |
| `+0x04`             | u32               | count              | Equals the main file's `count`     |
| `+0x08`             | Offset Row[count] | entries            | Not in file order                  |
| `entries+0x00`      | String Table      | string_table       | Present but empty                  |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`  |
| `string_table+0x04` | u32               | zero               | `0`                                |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                       |
| ------- | ---- | ------------ | ----------------------------------------------------------- |
| `+0x00` | u16  | character_id | The record's `character_id`                                 |
| `+0x02` | u32  | offset       | Where the record's `character_id_dup` starts, 2 bytes into the record |
| `+0x06` | u32  | size         | Record size minus 2                                         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Layout 1

Client 1784 has no `cant_learnable_rate` and stores `skill_key` as a u8; it has 288
records and 4,134 skills, keys 1 to 76.

### Record (variable: 8 bytes + skills)

| Offset  | Type                | Field            | Notes |
| ------- | ------------------- | ---------------- | ----- |
| `+0x00` | u16                 | character_id     | |
| `+0x02` | u16                 | character_id_dup | |
| `+0x04` | u32                 | skill_count      | 0 to 27 |
| `+0x08` | Skill[skill_count]  | skills           | In `skill_key` order on 286 of 288 records |

### Skill (13 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u8   | skill_key  | |
| `+0x01` | u32  | able       | |
| `+0x05` | u32  | add_exp    | |
| `+0x09` | u8   | is_learn   | |
| `+0x0A` | u8   | unknown_0d | `0` on every entry |
| `+0x0B` | u16  | unknown_0e | `0` on every entry |

## Learn Chance

The horse growth window (Horse Growth Info, My Horse Info tab) lists a
chance per skill and a "Does not learn" row. The client Lua
(`panel_dialog_servantsimulator_5`) fills that row from
`ToClient_GetHorseSimulateDetailInformationCantLearnableRate()`. With the
window's Total Gain Chance `g`:

```text
chance(skill)   = able × (1 + g) / (cant_learnable_rate + sum of able of the skills not learned yet)
chance(nothing) = 100% - sum of chance(skill)
```

Learned and inherent skills drop out of the sum. On 103 of the 148 records
with a non-zero `cant_learnable_rate` (client 3474), it plus the `able` of
every entry below 1,000,000 is exactly 1,000,000; the formula does not need
that, and holds on a record where the total is 1,061,581 too (9890 below).

Checked on 2026-10-20 (client 3474) with Training Artisan 7, on two tier 6
stallions of the 9915 group (9915, 9952, 9953, 9973, 9978:
`cant_learnable_rate` 536,040, Hind Kick 75,000) at Total Gain Chance
21.7%, and on the tier 8 mare 9890 (`cant_learnable_rate` 379,906, Caution
37,000, Two-seater 9,000) at 31.7%:

| Horse | Learned | Sum | Chance | Does not learn |
| ----- | ------- | --- | ------ | -------------- |
| 9953 (Breed 11), level 8 | Fore Chop, Sprint (inherent) | 924,405 | Hind Kick 9.8739% (shown 9.8739%) | 48.8715% (shown 48.8715%) |
| 9915 (Breed 2), level 4 | Sprint (inherent), Start Accel, Streak Leap | 906,912 | Hind Kick 10.0644% (shown 10.0644%) | 50.2327% (shown 50.2327%) |
| 9890 (Breed 13), level 30 | 18 of 20, S: Instant Accel and Sprint inherent | 425,906 | Caution 11.4413%, Two-seater 2.7830% (shown 11.4413%, 2.783%) | 85.7757% (shown 85.7757%) |

The window's Base Coat line (`bdoservanttitless.bss`) names the breed,
which picks one character of the group. The level 4 horse's window lists
three learned skills; only Streak Leap
(38,064) as the third one gives its shown chances, and Drift, Fore Chop,
High Jump, Quick Stop and Instant Accel then match to the last digit too.

## Field Names

The names follow the `VehicleSkillOwner_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784: one row per `CharacterKey` with
`Able_N`, `AddExp_N` and `IsLearn_N` for skill keys 1 to 76. On client 1784
(288 records, every one in the sheet) the entries match by value:

| Column | Field | Equal (client 1784, 4,134 entries) | Equal (client 3474, 3,899 entries of 279 shared records) |
| ------ | ----- | ---------------------------------- | -------------------------------------------------------- |
| `Able_N` | `able` of the entry with `skill_key` N | 4,112 | 2,529 |
| `AddExp_N` | `add_exp` | 4,134 | 3,197 |
| `IsLearn_N` | `is_learn` | 4,134 | 3,899 |

The 22 client 1784 `able` misses are sheet values with a fraction stored
truncated (`4666.666667` as 4,666). Every record lists each skill whose
`Able_N` is not 0; 23 records also list skills whose `Able_N` is 0. The
client 3474 misses come from changed values: `able` 1,000,000 and `add_exp`
0 where client 1784 has 200,000 and 2,500 (camel 9081, Fore Chop 20 and
Hind Kick 21), and the client Lua gates the
skill-rate display of the breeding simulator behind
`_ContentsGroup_VehicleLearnSkill_Renewal`.

## Open Questions

### Records With No Does-Not-Learn Weight

`cant_learnable_rate` is new on client 3474: 0 on all tier 1 to 5 horses
and on 218 records in all, non-zero on 148, mostly tier 6 to 9 horses. 51
of the 218 start with every skill they list (31619, checked in game, shows
Skill List (27) with all 27 at 100%), but the other 167, among them every
tier 1 to 5 horse, still have skills to learn. With a weight of 0 the
formula gives "Does not learn" 0% and the skills more than 100% in sum, so
the window either shows those horses another way or uses another formula
for them.

### The Constant Byte

`unknown_0d` is 2 on every client 3474 entry and 0 on client 1784.
