# `effectfilename.bss` Format

## Purpose

The hit and footstep effects the client plays on contact. A PABR file with
no row count: three fixed grids of string-table indices follow the magic.
The attack grids give the effect of a hit per weapon type and armor type,
in ten numbered tables; the special attack grids do the same for a second
set of ten tables; the ground grid gives the effect of each ground type in
five columns, four of them movements (walk, jump, sit, fall). Each cell
names one or more effects as a comma-separated list
(`CO_Hit_Base,fCO_Hit_BloodA(B),...`); an empty string is an empty cell.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                 | Bytes     | Records                                                            | Row bytes               |
| ------ | -------------- | -------------------- | --------- | ------------------------------------------------------------------ | ----------------------- |
| 6      | 1481 and later | `effectfilename.bss` | 2,493,263 | 6,010 Weapon Row, 10 Attack Table, 10 Special Table, 30 Ground Row | 400                     |
| 5      | 1462 to 1474   | `effectfilename.bss` | 867,305   | 2,000 Weapon Row, 10 Attack Table, 10 Special Table, 30 Ground Row | 400                     |
| 4      | 1109 to 1459   | `effectfilename.bss` | 437,449   | 1,000 Weapon Row, 10 Attack Table, 30 Ground Row                   | 400                     |
| 3      | 805 to 829     | `effectfilename.bss` | 50,790    | 100 Weapon Row, 30 Ground Row                                      | 400                     |
| 2      | 531 to 794     | `effectfilename.bss` | 193,704   | 10,150 Effect Text, 100 Weapon Row, 30 Ground Row                  | 8 to 145, 19 on average |
| 1      | 485 to 526     | `effectfilename.bss` | 70,630    | 1,375 Effect Text, 35 Weapon Row, 30 Ground Row                    | 8 to 226, 51 on average |

| Layout | File                 | Known                | Unknown    |
| ------ | -------------------- | -------------------- | ---------- |
| 6      | `effectfilename.bss` | 2,493,263 B (100.0%) | 0 B (0.0%) |
| 5      | `effectfilename.bss` | 867,305 B (100.0%)   | 0 B (0.0%) |
| 4      | `effectfilename.bss` | 437,449 B (100.0%)   | 0 B (0.0%) |
| 3      | `effectfilename.bss` | 50,790 B (100.0%)    | 0 B (0.0%) |
| 2      | `effectfilename.bss` | 193,704 B (100.0%)   | 0 B (0.0%) |
| 1      | `effectfilename.bss` | 70,630 B (100.0%)    | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 6 | `899cfbce7111`  |
| 3482   | Layout 6 | `899cfbce7111`  |
| 3474   | Layout 6 | `899cfbce7111`  |
| 3473   | Layout 6 | `899cfbce7111`  |
| 3464   | Layout 6 | `899cfbce7111`  |
| 3458   | Layout 6 | `899cfbce7111`  |
| 3454   | Layout 6 | `899cfbce7111`  |
| 3444   | Layout 6 | `899cfbce7111`  |
| 3435   | Layout 6 | `899cfbce7111`  |
| 3426   | Layout 6 | `899cfbce7111`  |
| 3418   | Layout 6 | `899cfbce7111`  |
| 3412   | Layout 6 | `899cfbce7111`  |
| 3402   | Layout 6 | `899cfbce7111`  |
| 3396   | Layout 6 | `899cfbce7111`  |
| 3387   | Layout 6 | `899cfbce7111`  |
| 3381   | Layout 6 | `899cfbce7111`  |
| 3373   | Layout 6 | `899cfbce7111`  |
| 3364   | Layout 6 | `899cfbce7111`  |
| 3356   | Layout 6 | `899cfbce7111`  |
| 3349   | Layout 6 | `899cfbce7111`  |
| 3342   | Layout 6 | `899cfbce7111`  |
| 3335   | Layout 6 | `899cfbce7111`  |
| 3326   | Layout 6 | `899cfbce7111`  |
| 3321   | Layout 6 | `899cfbce7111`  |
| 3314   | Layout 6 | `899cfbce7111`  |
| 3303   | Layout 6 | `899cfbce7111`  |
| 3302   | Layout 6 | `899cfbce7111`  |
| 3293   | Layout 6 | `899cfbce7111`  |
| 3283   | Layout 6 | `899cfbce7111`  |
| 3275   | Layout 6 | `899cfbce7111`  |
| 3267   | Layout 6 | `899cfbce7111`  |
| 3258   | Layout 6 | `899cfbce7111`  |
| 3251   | Layout 6 | `899cfbce7111`  |
| 3242   | Layout 6 | `899cfbce7111`  |
| 3235   | Layout 6 | `899cfbce7111`  |
| 3229   | Layout 6 | `899cfbce7111`  |
| 3212   | Layout 6 | `899cfbce7111`  |
| 3203   | Layout 6 | `899cfbce7111`  |
| 3193   | Layout 6 | `899cfbce7111`  |
| 3186   | Layout 6 | `899cfbce7111`  |
| 3177   | Layout 6 | `899cfbce7111`  |
| 3169   | Layout 6 | `899cfbce7111`  |
| 3158   | Layout 6 | `899cfbce7111`  |
| 3151   | Layout 6 | `899cfbce7111`  |
| 3144   | Layout 6 | `899cfbce7111`  |
| 3133   | Layout 6 | `899cfbce7111`  |
| 3125   | Layout 6 | `899cfbce7111`  |
| 3118   | Layout 6 | `899cfbce7111`  |
| 3111   | Layout 6 | `899cfbce7111`  |
| 3103   | Layout 6 | `899cfbce7111`  |
| 3095   | Layout 6 | `899cfbce7111`  |
| 3086   | Layout 6 | `899cfbce7111`  |
| 3072   | Layout 6 | `899cfbce7111`  |
| 3062   | Layout 6 | `899cfbce7111`  |
| 3052   | Layout 6 | `899cfbce7111`  |
| 3045   | Layout 6 | `899cfbce7111`  |
| 3037   | Layout 6 | `899cfbce7111`  |
| 3030   | Layout 6 | `899cfbce7111`  |
| 3021   | Layout 6 | `899cfbce7111`  |
| 3012   | Layout 6 | `899cfbce7111`  |
| 3002   | Layout 6 | `899cfbce7111`  |
| 2995   | Layout 6 | `899cfbce7111`  |
| 2987   | Layout 6 | `899cfbce7111`  |
| 2978   | Layout 6 | `899cfbce7111`  |
| 2970   | Layout 6 | `899cfbce7111`  |
| 2959   | Layout 6 | `899cfbce7111`  |
| 2951   | Layout 6 | `899cfbce7111`  |
| 2942   | Layout 6 | `899cfbce7111`  |
| 2935   | Layout 6 | `899cfbce7111`  |
| 2932   | Layout 6 | `899cfbce7111`  |
| 2923   | Layout 6 | `899cfbce7111`  |
| 2919   | Layout 6 | `899cfbce7111`  |
| 2907   | Layout 6 | `899cfbce7111`  |
| 2900   | Layout 6 | `899cfbce7111`  |
| 2891   | Layout 6 | `899cfbce7111`  |
| 2882   | Layout 6 | `899cfbce7111`  |
| 2872   | Layout 6 | `899cfbce7111`  |
| 2863   | Layout 6 | `899cfbce7111`  |
| 2855   | Layout 6 | `899cfbce7111`  |
| 2849   | Layout 6 | `899cfbce7111`  |
| 2844   | Layout 6 | `899cfbce7111`  |
| 2834   | Layout 6 | `899cfbce7111`  |
| 2825   | Layout 6 | `899cfbce7111`  |
| 2819   | Layout 6 | `899cfbce7111`  |
| 2811   | Layout 6 | `899cfbce7111`  |
| 2803   | Layout 6 | `899cfbce7111`  |
| 2794   | Layout 6 | `899cfbce7111`  |
| 2783   | Layout 6 | `899cfbce7111`  |
| 2774   | Layout 6 | `899cfbce7111`  |
| 2765   | Layout 6 | `899cfbce7111`  |
| 2756   | Layout 6 | `899cfbce7111`  |
| 2750   | Layout 6 | `899cfbce7111`  |
| 2743   | Layout 6 | `899cfbce7111`  |
| 2736   | Layout 6 | `899cfbce7111`  |
| 2726   | Layout 6 | `899cfbce7111`  |
| 2717   | Layout 6 | `899cfbce7111`  |
| 2709   | Layout 6 | `899cfbce7111`  |
| 2703   | Layout 6 | `899cfbce7111`  |
| 2695   | Layout 6 | `899cfbce7111`  |
| 2684   | Layout 6 | `899cfbce7111`  |
| 2672   | Layout 6 | `899cfbce7111`  |
| 2665   | Layout 6 | `899cfbce7111`  |
| 2657   | Layout 6 | `899cfbce7111`  |
| 2649   | Layout 6 | `899cfbce7111`  |
| 2644   | Layout 6 | `899cfbce7111`  |
| 2637   | Layout 6 | `899cfbce7111`  |
| 2629   | Layout 6 | `899cfbce7111`  |
| 2619   | Layout 6 | `899cfbce7111`  |
| 2612   | Layout 6 | `899cfbce7111`  |
| 2606   | Layout 6 | `899cfbce7111`  |
| 2602   | Layout 6 | `899cfbce7111`  |
| 2601   | Layout 6 | `899cfbce7111`  |
| 2592   | Layout 6 | `899cfbce7111`  |
| 2583   | Layout 6 | `899cfbce7111`  |
| 2575   | Layout 6 | `899cfbce7111`  |
| 2567   | Layout 6 | `899cfbce7111`  |
| 2560   | Layout 6 | `899cfbce7111`  |
| 2553   | Layout 6 | `899cfbce7111`  |
| 2545   | Layout 6 | `899cfbce7111`  |
| 2538   | Layout 6 | `899cfbce7111`  |
| 2529   | Layout 6 | `899cfbce7111`  |
| 2519   | Layout 6 | `899cfbce7111`  |
| 2513   | Layout 6 | `899cfbce7111`  |
| 2510   | Layout 6 | `899cfbce7111`  |
| 2507   | Layout 6 | `899cfbce7111`  |
| 2503   | Layout 6 | `899cfbce7111`  |
| 2498   | Layout 6 | `899cfbce7111`  |
| 2492   | Layout 6 | `899cfbce7111`  |
| 2487   | Layout 6 | `899cfbce7111`  |
| 2480   | Layout 6 | `899cfbce7111`  |
| 2474   | Layout 6 | `899cfbce7111`  |
| 2468   | Layout 6 | `899cfbce7111`  |
| 2460   | Layout 6 | `899cfbce7111`  |
| 2453   | Layout 6 | `899cfbce7111`  |
| 2444   | Layout 6 | `899cfbce7111`  |
| 2438   | Layout 6 | `899cfbce7111`  |
| 2434   | Layout 6 | `899cfbce7111`  |
| 2429   | Layout 6 | `899cfbce7111`  |
| 2421   | Layout 6 | `899cfbce7111`  |
| 2414   | Layout 6 | `899cfbce7111`  |
| 2407   | Layout 6 | `899cfbce7111`  |
| 2401   | Layout 6 | `899cfbce7111`  |
| 2397   | Layout 6 | `899cfbce7111`  |
| 2393   | Layout 6 | `899cfbce7111`  |
| 2384   | Layout 6 | `899cfbce7111`  |
| 2378   | Layout 6 | `899cfbce7111`  |
| 2372   | Layout 6 | `899cfbce7111`  |
| 2358   | Layout 6 | `899cfbce7111`  |
| 2352   | Layout 6 | `899cfbce7111`  |
| 2347   | Layout 6 | `899cfbce7111`  |
| 2343   | Layout 6 | `899cfbce7111`  |
| 2335   | Layout 6 | `899cfbce7111`  |
| 2327   | Layout 6 | `899cfbce7111`  |
| 2324   | Layout 6 | `899cfbce7111`  |
| 2319   | Layout 6 | `899cfbce7111`  |
| 2313   | Layout 6 | `899cfbce7111`  |
| 2308   | Layout 6 | `899cfbce7111`  |
| 2302   | Layout 6 | `899cfbce7111`  |
| 2295   | Layout 6 | `899cfbce7111`  |
| 2290   | Layout 6 | `899cfbce7111`  |
| 2284   | Layout 6 | `899cfbce7111`  |
| 2276   | Layout 6 | `899cfbce7111`  |
| 2269   | Layout 6 | `899cfbce7111`  |
| 2259   | Layout 6 | `899cfbce7111`  |
| 2250   | Layout 6 | `899cfbce7111`  |
| 2243   | Layout 6 | `899cfbce7111`  |
| 2235   | Layout 6 | `899cfbce7111`  |
| 2229   | Layout 6 | `899cfbce7111`  |
| 2224   | Layout 6 | `899cfbce7111`  |
| 2218   | Layout 6 | `899cfbce7111`  |
| 2215   | Layout 6 | `899cfbce7111`  |
| 2207   | Layout 6 | `899cfbce7111`  |
| 2203   | Layout 6 | `899cfbce7111`  |
| 2196   | Layout 6 | `899cfbce7111`  |
| 2192   | Layout 6 | `899cfbce7111`  |
| 2189   | Layout 6 | `899cfbce7111`  |
| 2183   | Layout 6 | `899cfbce7111`  |
| 2179   | Layout 6 | `899cfbce7111`  |
| 2171   | Layout 6 | `899cfbce7111`  |
| 2163   | Layout 6 | `899cfbce7111`  |
| 2156   | Layout 6 | `899cfbce7111`  |
| 2151   | Layout 6 | `899cfbce7111`  |
| 2147   | Layout 6 | `899cfbce7111`  |
| 2142   | Layout 6 | `899cfbce7111`  |
| 2138   | Layout 6 | `899cfbce7111`  |
| 2134   | Layout 6 | `899cfbce7111`  |
| 2130   | Layout 6 | `899cfbce7111`  |
| 2122   | Layout 6 | `899cfbce7111`  |
| 2107   | Layout 6 | `899cfbce7111`  |
| 2098   | Layout 6 | `899cfbce7111`  |
| 2089   | Layout 6 | `899cfbce7111`  |
| 2081   | Layout 6 | `899cfbce7111`  |
| 2073   | Layout 6 | `899cfbce7111`  |
| 2067   | Layout 6 | `899cfbce7111`  |
| 2063   | Layout 6 | `899cfbce7111`  |
| 2059   | Layout 6 | `899cfbce7111`  |
| 2052   | Layout 6 | `899cfbce7111`  |
| 2044   | Layout 6 | `899cfbce7111`  |
| 2039   | Layout 6 | `899cfbce7111`  |
| 2032   | Layout 6 | `899cfbce7111`  |
| 2025   | Layout 6 | `899cfbce7111`  |
| 2011   | Layout 6 | `899cfbce7111`  |
| 2005   | Layout 6 | `899cfbce7111`  |
| 2000   | Layout 6 | `899cfbce7111`  |
| 1996   | Layout 6 | `899cfbce7111`  |
| 1991   | Layout 6 | `899cfbce7111`  |
| 1985   | Layout 6 | `899cfbce7111`  |
| 1980   | Layout 6 | `899cfbce7111`  |
| 1969   | Layout 6 | `899cfbce7111`  |
| 1964   | Layout 6 | `899cfbce7111`  |
| 1958   | Layout 6 | `899cfbce7111`  |
| 1950   | Layout 6 | `899cfbce7111`  |
| 1945   | Layout 6 | `899cfbce7111`  |
| 1937   | Layout 6 | `899cfbce7111`  |
| 1933   | Layout 6 | `899cfbce7111`  |
| 1927   | Layout 6 | `899cfbce7111`  |
| 1921   | Layout 6 | `899cfbce7111`  |
| 1914   | Layout 6 | `899cfbce7111`  |
| 1908   | Layout 6 | `899cfbce7111`  |
| 1897   | Layout 6 | `899cfbce7111`  |
| 1892   | Layout 6 | `899cfbce7111`  |
| 1886   | Layout 6 | `899cfbce7111`  |
| 1881   | Layout 6 | `899cfbce7111`  |
| 1871   | Layout 6 | `899cfbce7111`  |
| 1866   | Layout 6 | `899cfbce7111`  |
| 1862   | Layout 6 | `899cfbce7111`  |
| 1854   | Layout 6 | `899cfbce7111`  |
| 1846   | Layout 6 | `899cfbce7111`  |
| 1838   | Layout 6 | `899cfbce7111`  |
| 1832   | Layout 6 | `899cfbce7111`  |
| 1826   | Layout 6 | `899cfbce7111`  |
| 1822   | Layout 6 | `899cfbce7111`  |
| 1818   | Layout 6 | `899cfbce7111`  |
| 1804   | Layout 6 | `899cfbce7111`  |
| 1794   | Layout 6 | `899cfbce7111`  |
| 1790   | Layout 6 | `899cfbce7111`  |
| 1784   | Layout 6 | `899cfbce7111`  |
| 1774   | Layout 6 | `899cfbce7111`  |
| 1771   | Layout 6 | `899cfbce7111`  |
| 1762   | Layout 6 | `899cfbce7111`  |
| 1759   | Layout 6 | `899cfbce7111`  |
| 1754   | Layout 6 | `899cfbce7111`  |
| 1749   | Layout 6 | `899cfbce7111`  |
| 1743   | Layout 6 | `899cfbce7111`  |
| 1737   | Layout 6 | `899cfbce7111`  |
| 1731   | Layout 6 | `899cfbce7111`  |
| 1725   | Layout 6 | `899cfbce7111`  |
| 1717   | Layout 6 | `899cfbce7111`  |
| 1710   | Layout 6 | `899cfbce7111`  |
| 1704   | Layout 6 | `899cfbce7111`  |
| 1698   | Layout 6 | `899cfbce7111`  |
| 1690   | Layout 6 | `899cfbce7111`  |
| 1685   | Layout 6 | `899cfbce7111`  |
| 1680   | Layout 6 | `899cfbce7111`  |
| 1674   | Layout 6 | `899cfbce7111`  |
| 1668   | Layout 6 | `899cfbce7111`  |
| 1659   | Layout 6 | `899cfbce7111`  |
| 1649   | Layout 6 | `899cfbce7111`  |
| 1642   | Layout 6 | `899cfbce7111`  |
| 1636   | Layout 6 | `899cfbce7111`  |
| 1628   | Layout 6 | `899cfbce7111`  |
| 1622   | Layout 6 | `899cfbce7111`  |
| 1614   | Layout 6 | `899cfbce7111`  |
| 1608   | Layout 6 | `899cfbce7111`  |
| 1602   | Layout 6 | `899cfbce7111`  |
| 1598   | Layout 6 | `899cfbce7111`  |
| 1594   | Layout 6 | `899cfbce7111`  |
| 1590   | Layout 6 | `899cfbce7111`  |
| 1587   | Layout 6 | `899cfbce7111`  |
| 1584   | Layout 6 | `899cfbce7111`  |
| 1579   | Layout 6 | `899cfbce7111`  |
| 1572   | Layout 6 | `899cfbce7111`  |
| 1565   | Layout 6 | `899cfbce7111`  |
| 1559   | Layout 6 | `899cfbce7111`  |
| 1554   | Layout 6 | `899cfbce7111`  |
| 1547   | Layout 6 | `899cfbce7111`  |
| 1537   | Layout 6 | `899cfbce7111`  |
| 1529   | Layout 6 | `899cfbce7111`  |
| 1524   | Layout 6 | `899cfbce7111`  |
| 1519   | Layout 6 | `899cfbce7111`  |
| 1509   | Layout 6 | `899cfbce7111`  |
| 1506   | Layout 6 | `899cfbce7111`  |
| 1504   | Layout 6 | `899cfbce7111`  |
| 1500   | Layout 6 | `899cfbce7111`  |
| 1493   | Layout 6 | `899cfbce7111`  |
| 1489   | Layout 6 | `899cfbce7111`  |
| 1485   | Layout 6 | `899cfbce7111`  |
| 1481   | Layout 6 | `899cfbce7111`  |
| 1474   | Layout 5 | `899cfbce7111`  |
| 1466   | Layout 5 | `899cfbce7111`  |
| 1462   | Layout 5 | `899cfbce7111`  |
| 1459   | Layout 4 | `899cfbce7111`  |
| 1453   | Layout 4 | `899cfbce7111`  |
| 1450   | Layout 4 | `899cfbce7111`  |
| 1445   | Layout 4 | `899cfbce7111`  |
| 1439   | Layout 4 | `899cfbce7111`  |
| 1433   | Layout 4 | `899cfbce7111`  |
| 1430   | Layout 4 | `899cfbce7111`  |
| 1426   | Layout 4 | `899cfbce7111`  |
| 1421   | Layout 4 | `899cfbce7111`  |
| 1417   | Layout 4 | `899cfbce7111`  |
| 1416   | Layout 4 | `899cfbce7111`  |
| 1409   | Layout 4 | `899cfbce7111`  |
| 1405   | Layout 4 | `899cfbce7111`  |
| 1401   | Layout 4 | `899cfbce7111`  |
| 1396   | Layout 4 | `899cfbce7111`  |
| 1391   | Layout 4 | `899cfbce7111`  |
| 1390   | Layout 4 | `899cfbce7111`  |
| 1386   | Layout 4 | `899cfbce7111`  |
| 1381   | Layout 4 | `899cfbce7111`  |
| 1379   | Layout 4 | `899cfbce7111`  |
| 1372   | Layout 4 | `899cfbce7111`  |
| 1366   | Layout 4 | `899cfbce7111`  |
| 1364   | Layout 4 | `899cfbce7111`  |
| 1363   | Layout 4 | `899cfbce7111`  |
| 1360   | Layout 4 | `899cfbce7111`  |
| 1358   | Layout 4 | `899cfbce7111`  |
| 1355   | Layout 4 | `899cfbce7111`  |
| 1351   | Layout 4 | `899cfbce7111`  |
| 1348   | Layout 4 | `899cfbce7111`  |
| 1346   | Layout 4 | `899cfbce7111`  |
| 1341   | Layout 4 | `899cfbce7111`  |
| 1340   | Layout 4 | `899cfbce7111`  |
| 1338   | Layout 4 | `899cfbce7111`  |
| 1335   | Layout 4 | `899cfbce7111`  |
| 1333   | Layout 4 | `899cfbce7111`  |
| 1329   | Layout 4 | `899cfbce7111`  |
| 1327   | Layout 4 | `899cfbce7111`  |
| 1324   | Layout 4 | `899cfbce7111`  |
| 1321   | Layout 4 | `899cfbce7111`  |
| 1319   | Layout 4 | `899cfbce7111`  |
| 1318   | Layout 4 | `899cfbce7111`  |
| 1316   | Layout 4 | `899cfbce7111`  |
| 1313   | Layout 4 | `899cfbce7111`  |
| 1311   | Layout 4 | `899cfbce7111`  |
| 1309   | Layout 4 | `899cfbce7111`  |
| 1304   | Layout 4 | `899cfbce7111`  |
| 1292   | Layout 4 | `899cfbce7111`  |
| 1286   | Layout 4 | `899cfbce7111`  |
| 1280   | Layout 4 | `899cfbce7111`  |
| 1276   | Layout 4 | `899cfbce7111`  |
| 1267   | Layout 4 | `899cfbce7111`  |
| 1261   | Layout 4 | `899cfbce7111`  |
| 1256   | Layout 4 | `899cfbce7111`  |
| 1250   | Layout 4 | `899cfbce7111`  |
| 1246   | Layout 4 | `899cfbce7111`  |
| 1239   | Layout 4 | `899cfbce7111`  |
| 1230   | Layout 4 | `899cfbce7111`  |
| 1226   | Layout 4 | `899cfbce7111`  |
| 1220   | Layout 4 | `899cfbce7111`  |
| 1217   | Layout 4 | `899cfbce7111`  |
| 1211   | Layout 4 | `899cfbce7111`  |
| 1210   | Layout 4 | `899cfbce7111`  |
| 1208   | Layout 4 | `899cfbce7111`  |
| 1203   | Layout 4 | `899cfbce7111`  |
| 1197   | Layout 4 | `899cfbce7111`  |
| 1194   | Layout 4 | `899cfbce7111`  |
| 1192   | Layout 4 | `899cfbce7111`  |
| 1187   | Layout 4 | `899cfbce7111`  |
| 1183   | Layout 4 | `899cfbce7111`  |
| 1177   | Layout 4 | `899cfbce7111`  |
| 1173   | Layout 4 | `899cfbce7111`  |
| 1167   | Layout 4 | `899cfbce7111`  |
| 1164   | Layout 4 | `899cfbce7111`  |
| 1156   | Layout 4 | `899cfbce7111`  |
| 1149   | Layout 4 | `899cfbce7111`  |
| 1144   | Layout 4 | `899cfbce7111`  |
| 1137   | Layout 4 | `899cfbce7111`  |
| 1132   | Layout 4 | `899cfbce7111`  |
| 1127   | Layout 4 | `899cfbce7111`  |
| 1122   | Layout 4 | `899cfbce7111`  |
| 1118   | Layout 4 | `899cfbce7111`  |
| 1114   | Layout 4 | `899cfbce7111`  |
| 1109   | Layout 4 | `899cfbce7111`  |
| 1102   | No file  | `899cfbce7111`  |
| 1096   | No file  | `899cfbce7111`  |
| 1088   | No file  | `899cfbce7111`  |
| 1081   | No file  | `899cfbce7111`  |
| 1076   | No file  | `899cfbce7111`  |
| 1069   | No file  | `899cfbce7111`  |
| 1064   | No file  | `899cfbce7111`  |
| 1058   | No file  | `899cfbce7111`  |
| 1051   | No file  | `899cfbce7111`  |
| 1044   | No file  | `899cfbce7111`  |
| 1036   | No file  | `899cfbce7111`  |
| 1026   | No file  | `899cfbce7111`  |
| 1016   | No file  | `899cfbce7111`  |
| 1009   | No file  | `899cfbce7111`  |
| 1005   | No file  | `899cfbce7111`  |
| 1000   | No file  | `899cfbce7111`  |
| 998    | No file  | `899cfbce7111`  |
| 990    | No file  | `899cfbce7111`  |
| 979    | No file  | `899cfbce7111`  |
| 972    | No file  | `899cfbce7111`  |
| 963    | No file  | `899cfbce7111`  |
| 955    | No file  | `899cfbce7111`  |
| 946    | No file  | `899cfbce7111`  |
| 938    | No file  | `899cfbce7111`  |
| 927    | No file  | `899cfbce7111`  |
| 911    | No file  | `899cfbce7111`  |
| 904    | No file  | `899cfbce7111`  |
| 899    | No file  | `899cfbce7111`  |
| 894    | No file  | `899cfbce7111`  |
| 885    | No file  | `899cfbce7111`  |
| 879    | No file  | `899cfbce7111`  |
| 872    | No file  | `899cfbce7111`  |
| 864    | No file  | `899cfbce7111`  |
| 855    | No file  | `899cfbce7111`  |
| 853    | No file  | `899cfbce7111`  |
| 845    | No file  | `899cfbce7111`  |
| 837    | No file  | `899cfbce7111`  |
| 829    | Layout 3 | `899cfbce7111`  |
| 822    | Layout 3 | `899cfbce7111`  |
| 814    | Layout 3 | `899cfbce7111`  |
| 805    | Layout 3 | `899cfbce7111`  |
| 794    | Layout 2 | `899cfbce7111`  |
| 787    | Layout 2 | `899cfbce7111`  |
| 780    | Layout 2 | `899cfbce7111`  |
| 771    | Layout 2 | `899cfbce7111`  |
| 760    | Layout 2 | `899cfbce7111`  |
| 748    | Layout 2 | `899cfbce7111`  |
| 741    | Layout 2 | `899cfbce7111`  |
| 736    | Layout 2 | `899cfbce7111`  |
| 731    | Layout 2 | `899cfbce7111`  |
| 723    | Layout 2 | `899cfbce7111`  |
| 711    | Layout 2 | `899cfbce7111`  |
| 707    | Layout 2 | `899cfbce7111`  |
| 697    | Layout 2 | `899cfbce7111`  |
| 689    | Layout 2 | `899cfbce7111`  |
| 683    | Layout 2 | `899cfbce7111`  |
| 678    | Layout 2 | `899cfbce7111`  |
| 670    | Layout 2 | `899cfbce7111`  |
| 661    | Layout 2 | `899cfbce7111`  |
| 656    | Layout 2 | `899cfbce7111`  |
| 652    | Layout 2 | `899cfbce7111`  |
| 643    | Layout 2 | `899cfbce7111`  |
| 637    | Layout 2 | `899cfbce7111`  |
| 630    | Layout 2 | `899cfbce7111`  |
| 627    | Layout 2 | `899cfbce7111`  |
| 621    | Layout 2 | `899cfbce7111`  |
| 617    | Layout 2 | `899cfbce7111`  |
| 615    | Layout 2 | `899cfbce7111`  |
| 606    | Layout 2 | `899cfbce7111`  |
| 599    | Layout 2 | `899cfbce7111`  |
| 592    | Layout 2 | `899cfbce7111`  |
| 586    | Layout 2 | `899cfbce7111`  |
| 577    | Layout 2 | `899cfbce7111`  |
| 569    | Layout 2 | `899cfbce7111`  |
| 561    | Layout 2 | `899cfbce7111`  |
| 554    | Layout 2 | `899cfbce7111`  |
| 542    | Layout 2 | `899cfbce7111`  |
| 532    | Layout 2 | `899cfbce7111`  |
| 531    | Layout 2 | `899cfbce7111`  |
| 526    | Layout 1 | `899cfbce7111`  |
| 521    | Layout 1 | `899cfbce7111`  |
| 517    | Layout 1 | `899cfbce7111`  |
| 510    | Layout 1 | `899cfbce7111`  |
| 508    | Layout 1 | `899cfbce7111`  |
| 504    | Layout 1 | `899cfbce7111`  |
| 497    | Layout 1 | `899cfbce7111`  |
| 491    | Layout 1 | `899cfbce7111`  |
| 485    | Layout 1 | `899cfbce7111`  |
| 478    | No file  | `899cfbce7111`  |
| 472    | No file  | `899cfbce7111`  |
| 466    | No file  | `899cfbce7111`  |
| 457    | No file  | `899cfbce7111`  |
| 452    | No file  | `899cfbce7111`  |
| 449    | No file  | `899cfbce7111`  |
| 435    | No file  | `899cfbce7111`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 6

### File Layout

| Offset              | Type              | Field                 | Notes                                                        |
| ------------------- | ----------------- | --------------------- | ------------------------------------------------------------ |
| `+0x00`             | char[4]           | magic                 | ASCII `PABR`; no row count follows                           |
| `+0x04`             | Attack Table[10]  | attack_tables         | See Attack Table; table N is the `AttackEffect_Table_N` sheet |
| `+0x61A84`          | Special Table[10] | special_attack_tables | See Special Table; table N is the `Special_AttackEffect_Table_N` sheet |
| `+0x24AEA4`         | Ground Row[30]    | ground_rows           | See Ground Row; row N is ground type N                       |
| `+0x24B0FC`         | String Table      | string_table          | See String Table                                             |
| `string_table+0x00` | u32               | table_start           | Offset of the string table, `0x24B0FC`                       |
| `string_table+0x04` | u32               | zero                  | Always `0`                                                   |

### Attack Table (40,000 bytes)

| Offset  | Type            | Field       | Notes                                   |
| ------- | --------------- | ----------- | --------------------------------------- |
| `+0x00` | Weapon Row[100] | weapon_rows | Row N is weapon type N, see Weapon Types |

### Special Table (200,400 bytes)

| Offset  | Type            | Field       | Notes                                                                   |
| ------- | --------------- | ----------- | ----------------------------------------------------------------------- |
| `+0x00` | Weapon Row[501] | weapon_rows | Row N is the sheet's column N; only rows `0` to `2` are filled (client 3483) |

### Weapon Row (400 bytes)

| Offset  | Type     | Field       | Notes                                                                      |
| ------- | -------- | ----------- | -------------------------------------------------------------------------- |
| `+0x00` | u32[100] | effect_refs | String table index of the effect list per armor type, see Armor Types; `0` to `50` are filled, `51` to `99` point at the empty string (client 3483) |

### Ground Row (20 bytes)

| Offset  | Type   | Field       | Notes                                                              |
| ------- | ------ | ----------- | ------------------------------------------------------------------ |
| `+0x00` | u32[5] | effect_refs | String table index of the effect list per column, see Ground Columns |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                         |
| ------- | ------------------ | ------------ | ----------------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `926` on client 3483                                       |
| `+0x04` | pstr[string_count] | strings      | UTF-8 effect lists in first-use order, every one referenced, one empty string |

## Layout 5

### File Layout

| Offset              | Type              | Field                 | Notes                                                        |
| ------------------- | ----------------- | --------------------- | ------------------------------------------------------------ |
| `+0x00`             | char[4]           | magic                 | ASCII `PABR`; no row count follows                           |
| `+0x04`             | Attack Table[10]  | attack_tables         | See Attack Table                                             |
| `+0x61A84`          | Special Table[10] | special_attack_tables | See Special Table                                            |
| `+0xC3504`          | Ground Row[30]    | ground_rows           | See Ground Row                                               |
| `+0xC375C`          | String Table      | string_table          | See String Table                                             |
| `string_table+0x00` | u32               | table_start           | Offset of the string table, `0xC375C`                        |
| `string_table+0x04` | u32               | zero                  | Always `0`                                                   |

### Special Table (40,000 bytes)

| Offset  | Type            | Field       | Notes                                                    |
| ------- | --------------- | ----------- | -------------------------------------------------------- |
| `+0x00` | Weapon Row[100] | weapon_rows | Row N is the sheet's column N, rows `0` to `2` filled    |

## Layout 4

### File Layout

| Offset              | Type             | Field         | Notes                                 |
| ------------------- | ---------------- | ------------- | ------------------------------------- |
| `+0x00`             | char[4]          | magic         | ASCII `PABR`; no row count follows    |
| `+0x04`             | Attack Table[10] | attack_tables | See Attack Table                      |
| `+0x61A84`          | Ground Row[30]   | ground_rows   | See Ground Row                        |
| `+0x61CDC`          | String Table     | string_table  | See String Table                      |
| `string_table+0x00` | u32              | table_start   | Offset of the string table, `0x61CDC` |
| `string_table+0x04` | u32              | zero          | Always `0`                            |

## Layout 3

### File Layout

| Offset              | Type            | Field         | Notes                                 |
| ------------------- | --------------- | ------------- | ------------------------------------- |
| `+0x00`             | char[4]         | magic         | ASCII `PABR`; no row count follows    |
| `+0x04`             | Attack Table[1] | attack_tables | One table, see Attack Table           |
| `+0x9C44`           | Ground Row[30]  | ground_rows   | See Ground Row                        |
| `+0x9E9C`           | String Table    | string_table  | See String Table                      |
| `string_table+0x00` | u32             | table_start   | Offset of the string table, `0x9E9C`  |
| `string_table+0x04` | u32             | zero          | Always `0`                            |

## Layout 2

### File Layout

| Offset               | Type            | Field         | Notes                                              |
| -------------------- | --------------- | ------------- | -------------------------------------------------- |
| `+0x00`              | Attack Table[1] | attack_tables | One table of inline texts; no PABR magic           |
| `attack_tables+0x00` | Ground Row[30]  | ground_rows   | See Ground Row; the file ends after the last row   |

### Attack Table (variable: 0 bytes + 100 rows)

| Offset  | Type            | Field       | Notes                                   |
| ------- | --------------- | ----------- | --------------------------------------- |
| `+0x00` | Weapon Row[100] | weapon_rows | Row N is weapon type N, see Weapon Types |

### Weapon Row (variable: 0 bytes + 100 texts)

| Offset  | Type             | Field   | Notes                                       |
| ------- | ---------------- | ------- | ------------------------------------------- |
| `+0x00` | Effect Text[100] | effects | One effect list per armor type              |

### Ground Row (variable: 0 bytes + 5 texts)

| Offset  | Type           | Field   | Notes                              |
| ------- | -------------- | ------- | ---------------------------------- |
| `+0x00` | Effect Text[5] | effects | One effect list per column         |

### Effect Text (variable: 8 bytes + text)

| Offset  | Type | Field  | Notes                                      |
| ------- | ---- | ------ | ------------------------------------------ |
| `+0x00` | str8 | effect | The effect list; a count of `0` is empty   |

## Layout 1

### Attack Table (variable: 0 bytes + 35 rows)

| Offset  | Type           | Field       | Notes                                   |
| ------- | -------------- | ----------- | --------------------------------------- |
| `+0x00` | Weapon Row[35] | weapon_rows | Row N is weapon type N, see Weapon Types |

### Weapon Row (variable: 0 bytes + 35 texts)

| Offset  | Type            | Field   | Notes                          |
| ------- | --------------- | ------- | ------------------------------ |
| `+0x00` | Effect Text[35] | effects | One effect list per armor type |

## Tables

A cell sits at `attack_tables[table].weapon_rows[weapon].effect_refs[armor]`,
the order of the sheets' columns and rows turned around: each sheet lists
armor types down and weapon types across. On client 3483 the filled cells
are these:

| Grid                          | Table | Rows filled              | Columns filled |
| ----------------------------- | ----- | ------------------------ | -------------- |
| `attack_tables`               | `0`   | `0` to `68`              | `0` to `50`    |
| `attack_tables`               | `2`   | 64 of `0` to `68`        | `0` to `50`    |
| `attack_tables`               | `5`   | 64 of `0` to `68`        | `0` to `50`    |
| `special_attack_tables`       | `0`   | `0` to `2`               | `0` to `50`    |
| `special_attack_tables`       | `2`   | `0` to `2`               | `0` to `50`    |
| `special_attack_tables`       | `5`   | `0` to `2`               | `0` to `50`    |
| `ground_rows`                 | -     | 10 of `0` to `29`        | `0` to `3`     |

Tables `2` and `5` hold the same effects as table `0` with other base
effects: `fCO_Hit_Base_Under` in table `2` and `fCO_Hit_Base_Center` in
table `5` where table `0` has `fCO_Hit_Base`. The special rows `0`, `1` and
`2` add `fP_PHM_ChargeWeapon_Fire_*`, `_Ice_*` and `_Elec_*` to the hit
effects.

## Weapon Types

The developer comments on the weapon columns of the `AttackEffect_Table`
sheet in a private server's `DataSheet_EffectDataTable.xlsm` on client
1784 name types `0` to `50`. Client 3483 fills rows `51` to `68` too; no
source names them.

| Type | Weapon                                    | Type | Weapon                                        |
| ---- | ----------------------------------------- | ---- | --------------------------------------------- |
| 0    | Basic attack (animals and the like)       | 26   | Magic attack hit sound                        |
| 1    | Bare hands                                | 27   | Whirlwind hit sound                           |
| 2    | Dagger                                    | 28   | Iron Buster, fire                             |
| 3    | Longsword                                 | 29   | Kamasylven Sword (Ranger), Sura Katana (Ninja) |
| 4    | Very large sword (bosses)                 | 30   | Celestial Bo Staff (Tamer)                    |
| 5    | Wooden sword, wooden blunt weapon         | 31   | Lancia (Valkyrie)                             |
| 6    | Stone blunt weapon                        | 32   | Crescent Blade (Musa)                         |
| 7    | Iron blunt weapon                         | 33   | Kerispear (Maehwa)                            |
| 8    | Bow                                       | 34   | Ship cannon hit sound                         |
| 9    | Unused                                    | 35   | Iron Buster, plain (Striker and Mystic summons) |
| 10   | Spears                                    | 36   | Lahn weapon                                   |
| 11   | Shabby wooden shield                      | 37   | Gun                                           |
| 12   | Wood and leather shield                   | 38   | Shai weapon                                   |
| 13   | Common shield                             | 39   | Shai kick                                     |
| 14   | Enchant arm                               | 40   | Shai bare hands                               |
| 15   | Kick, stronger than the basic attack      | 41   | Guardian polearm                              |
| 16   | Scratching claw (animals)                 | 42   | Not used                                      |
| 17   | Unused                                    | 43   | Not used                                      |
| 18   | Axe                                       | 44   | Not used                                      |
| 19   | Boss monster fist or headbutt             | 45   | Not used                                      |
| 20   | Poison, chemical attack                   | 46   | Hashashin main weapon                         |
| 21   | Scythe (Sorceress), Sah Chakram (Kunoichi) | 47   | Hashashin awakening weapon                    |
| 22   | Iron Buster (Berserker)                   | 48   | Nova mace                                     |
| 23   | Gardbrace (Striker), Cestus (Mystic)      | 49   | Nova shield                                   |
| 24   | Stone shield                              | 50   | Sage magic attack hit                         |
| 25   | Magic attack hit sound                    |      |                                               |

## Armor Types

The developer comments on the armor rows of the same sheet name types `0`
to `50`. Types `32` to `44` repeat earlier types for medium-sized targets;
`28` to `31` are named and boss targets with a body height of 550 or more,
Bell and the hunting monsters left out.

| Type | Armor                                         | Type | Armor                                  |
| ---- | --------------------------------------------- | ---- | -------------------------------------- |
| 0    | Common animals                                | 26   | Wooden cart (temporary): blood splashes but does not stain |
| 1    | Clothing, armor: cloth                        | 27   | Wooden cart (temporary), as `26`       |
| 2    | Clothing, armor: leather                      | 28   | Named or boss animal body, large       |
| 3    | Horse footsteps only, not for hits            | 29   | Named or boss metal, large             |
| 4    | Clothing, armor: plate mail                   | 30   | Named or boss stone, large             |
| 5    | Clothing, armor: chain mail                   | 31   | Named or boss wood, large              |
| 6    | Monster: wood without leaves (with leaves: `14`) | 32   | Medium: common animals              |
| 7    | Monster: stone                                | 33   | Medium: cloth                          |
| 8    | Monster: insect                               | 34   | Medium: leather                        |
| 9    | Monster: skeleton, bone                       | 35   | Medium: plate mail                     |
| 10   | Monster: slime, liquid                        | 36   | Medium: chain mail                     |
| 11   | Monster: glass, translucent solid             | 37   | Medium: wood without leaves            |
| 12   | Monster: ceramic, brick                       | 38   | Medium: stone                          |
| 13   | Monster: metal body (apart from metal armor)  | 39   | Medium: insect                         |
| 14   | Monster: plant                                | 40   | Medium: skeleton, bone                 |
| 15   | Monster: named or boss animal body            | 41   | Medium: slime, liquid                  |
| 16   | Monster: named or boss metal                  | 42   | Medium: ceramic, brick                 |
| 17   | Monster: named or boss stone                  | 43   | Medium: metal body                     |
| 18   | Shield: wooden shield only                    | 44   | Medium: plant                          |
| 19   | Shield: wood and leather                      | 45   | Monster: wood without leaves, armor    |
| 20   | Shield: metal                                 | 46   | Clothing, armor: cloth                 |
| 21   | Elephant footsteps only                       | 47   | Clothing, armor: leather               |
| 22   | Shield: stone shield only                     | 48   | Clothing, armor: plate mail            |
| 23   | Monster: reptile, amphibian                   | 49   | Clothing, armor: chain mail            |
| 24   | Monster: small animal, half a character's size | 50   | Clothing: cloth (no blood in table `0`) |
| 25   | Monster: straw scarecrow and the like         |      |                                        |

## Ground Columns

The comments on the `GroundEffect_Table` sheet name the ground types `0` to
`18` and the columns `0` to `3`. Column `4` has no comment and is empty on
clients 1784 and 3483.

| Column | Movement                              |
| ------ | ------------------------------------- |
| 0      | Walk, small ripple                    |
| 1      | Jump, large ripple                    |
| 2      | Sit, quiet ripple                     |
| 3      | Fall (knockdown), the largest ripple  |

| Type | Ground                         | Type | Ground                |
| ---- | ------------------------------ | ---- | --------------------- |
| 0    | Dirt                           | 10   | Snow                  |
| 1    | Lawn, grass                    | 11   | Ice                   |
| 2    | Stone, rock, concrete          | 12   | Carpet                |
| 3    | Gravel mixed with sand         | 13   | Thick iron floor      |
| 4    | Mud                            | 14   | Thin iron floor       |
| 5    | Beach and desert sand          | 15   | Broken glass          |
| 6    | Fallen leaves, forest          | 16   | Ceramic, pottery      |
| 7    | Thick wood                     | 17   | Beach sand            |
| 8    | Thin wood                      | 18   | Shallow water         |
| 9    | Deep water                     |      |                       |

## Field Names

The grids are seven sheets of a private server's `DataSheets.bexcel` on
client 1784: `AttackEffect_Table`, `AttackEffect_Table_2` and
`AttackEffect_Table_5` are attack tables `0`, `2` and `5`;
`Special_AttackEffect_Table`, `_2` and `_5` are special tables `0`, `2`
and `5`; `GroundEffect_Table` is `ground_rows`. The client 1784 file
matches every cell of the seven sheets (6 x 2,601 attack cells, 3 x 153
special cells, 95 ground cells; a `<null>` cell is the empty string).
The 2016 client names
the two grids it had `_attackEffectFileNameArray` (35 x 35) and
`_groundEffectFileNameArray` (30 x 5) of `gc::EffectFileNameManager`.

## Notes

- A special table's rows start at `N x 501` rows into `special_attack_tables`:
  the sheets put special table `2` at row 1,002 and `5` at row 2,505, so
  each special table is 501 rows of 100 cells, 10 x 501 x 100 refs in all.
- Most cells point at the empty string: on client 3483 10,531 of the
  601,150 refs name an effect. `CO_Empty` is a named placeholder the sheets
  use for some weapon and armor pairs (1,425 refs on client 3483); it is a
  separate string from the empty one.
- An effect name carries a one-letter prefix (`f`, `v`) and suffixes in
  brackets: `(B)`, `(v1)` and `(b0.36~0.0~0.0~190~9.0)` on the blood decals,
  whose first three numbers read as a red, green and blue colour (`0.0~0.26~0.0`
  on green blood). What the prefixes and the other suffixes switch is not
  in this file.
- The grids grew in steps: Layout 1 stores one attack table of 35 x 35
  cells and the ground grid as inline `str8` texts with no PABR magic and
  no string table, the shape of the 2016 `gc::EffectFileNameManager`;
  Layout 2 widens the table to 100 x 100, Layout 3 moves the texts into a
  string table, Layout 4 has ten attack tables, Layout 5 adds ten special
  tables of 100 rows and Layout 6 widens them to 501 rows.
- Clients 1000 to 1102 name the file `#na#effectfilename.bss` (one attack
  table on client 1000), which the doc check does not read.

## Open Questions

### What the Attack Table Number Is

Tables `0`, `2` and `5` are filled in both grids, with base effects
`fCO_Hit_Base`, `fCO_Hit_Base_Under` and `fCO_Hit_Base_Center`. The number
may be an attack or hit kind (a knockback, a hit from below), but no source
names the ten slots.

### What a Special Table Row Is

The special sheets have three columns headed `0` to `2` whose effects add a
fire, ice and lightning charge effect (`fP_PHM_ChargeWeapon_*`); their
column comments are copies of the weapon comments of the attack sheet. Why
a special table has 501 rows and what picks a row is open.
