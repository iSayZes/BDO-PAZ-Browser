# `rosewarskillstaticstatus.bss` Format

## Purpose

The Rose War team skills the commander uses from the team skill panel: one
row per `__eRoseWarSkillType_*` value with the skill number for each team.
On client 3474 the file has 7 rows, skill types `1` to `7`, and the two
teams share every skill but Bombard (Powerful Attack), which summons King
Griffon for Kamasylvia and Fugitive Khalk for O'dyllita.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                           | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------------------ | ----- | ------- | --------- |
| 1      | 2545 and later | `rosewarskillstaticstatus.bss` | 76    | 7 Row   | 8         |

| Layout | File                           | Known         | Unknown    |
| ------ | ------------------------------ | ------------- | ---------- |
| 1      | `rosewarskillstaticstatus.bss` | 76 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `bd6af37b0d43`  |
| 3482   | Layout 1 | `bd6af37b0d43`  |
| 3474   | Layout 1 | `bd6af37b0d43`  |
| 3473   | Layout 1 | `bd6af37b0d43`  |
| 3464   | Layout 1 | `bd6af37b0d43`  |
| 3458   | Layout 1 | `bd6af37b0d43`  |
| 3454   | Layout 1 | `bd6af37b0d43`  |
| 3444   | Layout 1 | `bd6af37b0d43`  |
| 3435   | Layout 1 | `bd6af37b0d43`  |
| 3426   | Layout 1 | `bd6af37b0d43`  |
| 3418   | Layout 1 | `bd6af37b0d43`  |
| 3412   | Layout 1 | `bd6af37b0d43`  |
| 3402   | Layout 1 | `bd6af37b0d43`  |
| 3396   | Layout 1 | `bd6af37b0d43`  |
| 3387   | Layout 1 | `bd6af37b0d43`  |
| 3381   | Layout 1 | `bd6af37b0d43`  |
| 3373   | Layout 1 | `bd6af37b0d43`  |
| 3364   | Layout 1 | `bd6af37b0d43`  |
| 3356   | Layout 1 | `bd6af37b0d43`  |
| 3349   | Layout 1 | `bd6af37b0d43`  |
| 3342   | Layout 1 | `bd6af37b0d43`  |
| 3335   | Layout 1 | `bd6af37b0d43`  |
| 3326   | Layout 1 | `bd6af37b0d43`  |
| 3321   | Layout 1 | `bd6af37b0d43`  |
| 3314   | Layout 1 | `bd6af37b0d43`  |
| 3303   | Layout 1 | `bd6af37b0d43`  |
| 3302   | Layout 1 | `bd6af37b0d43`  |
| 3293   | Layout 1 | `bd6af37b0d43`  |
| 3283   | Layout 1 | `bd6af37b0d43`  |
| 3275   | Layout 1 | `bd6af37b0d43`  |
| 3267   | Layout 1 | `bd6af37b0d43`  |
| 3258   | Layout 1 | `bd6af37b0d43`  |
| 3251   | Layout 1 | `bd6af37b0d43`  |
| 3242   | Layout 1 | `bd6af37b0d43`  |
| 3235   | Layout 1 | `bd6af37b0d43`  |
| 3229   | Layout 1 | `bd6af37b0d43`  |
| 3212   | Layout 1 | `bd6af37b0d43`  |
| 3203   | Layout 1 | `bd6af37b0d43`  |
| 3193   | Layout 1 | `bd6af37b0d43`  |
| 3186   | Layout 1 | `bd6af37b0d43`  |
| 3177   | Layout 1 | `bd6af37b0d43`  |
| 3169   | Layout 1 | `bd6af37b0d43`  |
| 3158   | Layout 1 | `bd6af37b0d43`  |
| 3151   | Layout 1 | `bd6af37b0d43`  |
| 3144   | Layout 1 | `bd6af37b0d43`  |
| 3133   | Layout 1 | `bd6af37b0d43`  |
| 3125   | Layout 1 | `bd6af37b0d43`  |
| 3118   | Layout 1 | `bd6af37b0d43`  |
| 3111   | Layout 1 | `bd6af37b0d43`  |
| 3103   | Layout 1 | `bd6af37b0d43`  |
| 3095   | Layout 1 | `bd6af37b0d43`  |
| 3086   | Layout 1 | `bd6af37b0d43`  |
| 3072   | Layout 1 | `bd6af37b0d43`  |
| 3062   | Layout 1 | `bd6af37b0d43`  |
| 3052   | Layout 1 | `bd6af37b0d43`  |
| 3045   | Layout 1 | `bd6af37b0d43`  |
| 3037   | Layout 1 | `bd6af37b0d43`  |
| 3030   | Layout 1 | `bd6af37b0d43`  |
| 3021   | Layout 1 | `bd6af37b0d43`  |
| 3012   | Layout 1 | `bd6af37b0d43`  |
| 3002   | Layout 1 | `bd6af37b0d43`  |
| 2995   | Layout 1 | `bd6af37b0d43`  |
| 2987   | Layout 1 | `bd6af37b0d43`  |
| 2978   | Layout 1 | `bd6af37b0d43`  |
| 2970   | Layout 1 | `bd6af37b0d43`  |
| 2959   | Layout 1 | `bd6af37b0d43`  |
| 2951   | Layout 1 | `bd6af37b0d43`  |
| 2942   | Layout 1 | `bd6af37b0d43`  |
| 2935   | Layout 1 | `bd6af37b0d43`  |
| 2932   | Layout 1 | `bd6af37b0d43`  |
| 2923   | Layout 1 | `bd6af37b0d43`  |
| 2919   | Layout 1 | `bd6af37b0d43`  |
| 2907   | Layout 1 | `bd6af37b0d43`  |
| 2900   | Layout 1 | `bd6af37b0d43`  |
| 2891   | Layout 1 | `bd6af37b0d43`  |
| 2882   | Layout 1 | `bd6af37b0d43`  |
| 2872   | Layout 1 | `bd6af37b0d43`  |
| 2863   | Layout 1 | `bd6af37b0d43`  |
| 2855   | Layout 1 | `bd6af37b0d43`  |
| 2849   | Layout 1 | `bd6af37b0d43`  |
| 2844   | Layout 1 | `bd6af37b0d43`  |
| 2834   | Layout 1 | `bd6af37b0d43`  |
| 2825   | Layout 1 | `bd6af37b0d43`  |
| 2819   | Layout 1 | `bd6af37b0d43`  |
| 2811   | Layout 1 | `bd6af37b0d43`  |
| 2803   | Layout 1 | `bd6af37b0d43`  |
| 2794   | Layout 1 | `bd6af37b0d43`  |
| 2783   | Layout 1 | `bd6af37b0d43`  |
| 2774   | Layout 1 | `bd6af37b0d43`  |
| 2765   | Layout 1 | `bd6af37b0d43`  |
| 2756   | Layout 1 | `bd6af37b0d43`  |
| 2750   | Layout 1 | `bd6af37b0d43`  |
| 2743   | Layout 1 | `bd6af37b0d43`  |
| 2736   | Layout 1 | `bd6af37b0d43`  |
| 2726   | Layout 1 | `bd6af37b0d43`  |
| 2717   | Layout 1 | `bd6af37b0d43`  |
| 2709   | Layout 1 | `bd6af37b0d43`  |
| 2703   | Layout 1 | `bd6af37b0d43`  |
| 2695   | Layout 1 | `bd6af37b0d43`  |
| 2684   | Layout 1 | `bd6af37b0d43`  |
| 2672   | Layout 1 | `bd6af37b0d43`  |
| 2665   | Layout 1 | `bd6af37b0d43`  |
| 2657   | Layout 1 | `bd6af37b0d43`  |
| 2649   | Layout 1 | `bd6af37b0d43`  |
| 2644   | Layout 1 | `bd6af37b0d43`  |
| 2637   | Layout 1 | `bd6af37b0d43`  |
| 2629   | Layout 1 | `bd6af37b0d43`  |
| 2619   | Layout 1 | `bd6af37b0d43`  |
| 2612   | Layout 1 | `bd6af37b0d43`  |
| 2606   | Layout 1 | `bd6af37b0d43`  |
| 2602   | Layout 1 | `bd6af37b0d43`  |
| 2601   | Layout 1 | `bd6af37b0d43`  |
| 2592   | Layout 1 | `bd6af37b0d43`  |
| 2583   | Layout 1 | `bd6af37b0d43`  |
| 2575   | Layout 1 | `bd6af37b0d43`  |
| 2567   | Layout 1 | `bd6af37b0d43`  |
| 2560   | Layout 1 | `bd6af37b0d43`  |
| 2553   | Layout 1 | `bd6af37b0d43`  |
| 2545   | Layout 1 | `bd6af37b0d43`  |
| 2538   | No file  | `bd6af37b0d43`  |
| 2529   | No file  | `bd6af37b0d43`  |
| 2519   | No file  | `bd6af37b0d43`  |
| 2513   | No file  | `bd6af37b0d43`  |
| 2510   | No file  | `bd6af37b0d43`  |
| 2507   | No file  | `bd6af37b0d43`  |
| 2503   | No file  | `bd6af37b0d43`  |
| 2498   | No file  | `bd6af37b0d43`  |
| 2492   | No file  | `bd6af37b0d43`  |
| 2487   | No file  | `bd6af37b0d43`  |
| 2480   | No file  | `bd6af37b0d43`  |
| 2474   | No file  | `bd6af37b0d43`  |
| 2468   | No file  | `bd6af37b0d43`  |
| 2460   | No file  | `bd6af37b0d43`  |
| 2453   | No file  | `bd6af37b0d43`  |
| 2444   | No file  | `bd6af37b0d43`  |
| 2438   | No file  | `bd6af37b0d43`  |
| 2434   | No file  | `bd6af37b0d43`  |
| 2429   | No file  | `bd6af37b0d43`  |
| 2421   | No file  | `bd6af37b0d43`  |
| 2414   | No file  | `bd6af37b0d43`  |
| 2407   | No file  | `bd6af37b0d43`  |
| 2401   | No file  | `bd6af37b0d43`  |
| 2397   | No file  | `bd6af37b0d43`  |
| 2393   | No file  | `bd6af37b0d43`  |
| 2384   | No file  | `bd6af37b0d43`  |
| 2378   | No file  | `bd6af37b0d43`  |
| 2372   | No file  | `bd6af37b0d43`  |
| 2358   | No file  | `bd6af37b0d43`  |
| 2352   | No file  | `bd6af37b0d43`  |
| 2347   | No file  | `bd6af37b0d43`  |
| 2343   | No file  | `bd6af37b0d43`  |
| 2335   | No file  | `bd6af37b0d43`  |
| 2327   | No file  | `bd6af37b0d43`  |
| 2324   | No file  | `bd6af37b0d43`  |
| 2319   | No file  | `bd6af37b0d43`  |
| 2313   | No file  | `bd6af37b0d43`  |
| 2308   | No file  | `bd6af37b0d43`  |
| 2302   | No file  | `bd6af37b0d43`  |
| 2295   | No file  | `bd6af37b0d43`  |
| 2290   | No file  | `bd6af37b0d43`  |
| 2284   | No file  | `bd6af37b0d43`  |
| 2276   | No file  | `bd6af37b0d43`  |
| 2269   | No file  | `bd6af37b0d43`  |
| 2259   | No file  | `bd6af37b0d43`  |
| 2250   | No file  | `bd6af37b0d43`  |
| 2243   | No file  | `bd6af37b0d43`  |
| 2235   | No file  | `bd6af37b0d43`  |
| 2229   | No file  | `bd6af37b0d43`  |
| 2224   | No file  | `bd6af37b0d43`  |
| 2218   | No file  | `bd6af37b0d43`  |
| 2215   | No file  | `bd6af37b0d43`  |
| 2207   | No file  | `bd6af37b0d43`  |
| 2203   | No file  | `bd6af37b0d43`  |
| 2196   | No file  | `bd6af37b0d43`  |
| 2192   | No file  | `bd6af37b0d43`  |
| 2189   | No file  | `bd6af37b0d43`  |
| 2183   | No file  | `bd6af37b0d43`  |
| 2179   | No file  | `bd6af37b0d43`  |
| 2171   | No file  | `bd6af37b0d43`  |
| 2163   | No file  | `bd6af37b0d43`  |
| 2156   | No file  | `bd6af37b0d43`  |
| 2151   | No file  | `bd6af37b0d43`  |
| 2147   | No file  | `bd6af37b0d43`  |
| 2142   | No file  | `bd6af37b0d43`  |
| 2138   | No file  | `bd6af37b0d43`  |
| 2134   | No file  | `bd6af37b0d43`  |
| 2130   | No file  | `bd6af37b0d43`  |
| 2122   | No file  | `bd6af37b0d43`  |
| 2107   | No file  | `bd6af37b0d43`  |
| 2098   | No file  | `bd6af37b0d43`  |
| 2089   | No file  | `bd6af37b0d43`  |
| 2081   | No file  | `bd6af37b0d43`  |
| 2073   | No file  | `bd6af37b0d43`  |
| 2067   | No file  | `bd6af37b0d43`  |
| 2063   | No file  | `bd6af37b0d43`  |
| 2059   | No file  | `bd6af37b0d43`  |
| 2052   | No file  | `bd6af37b0d43`  |
| 2044   | No file  | `bd6af37b0d43`  |
| 2039   | No file  | `bd6af37b0d43`  |
| 2032   | No file  | `bd6af37b0d43`  |
| 2025   | No file  | `bd6af37b0d43`  |
| 2011   | No file  | `bd6af37b0d43`  |
| 2005   | No file  | `bd6af37b0d43`  |
| 2000   | No file  | `bd6af37b0d43`  |
| 1996   | No file  | `bd6af37b0d43`  |
| 1991   | No file  | `bd6af37b0d43`  |
| 1985   | No file  | `bd6af37b0d43`  |
| 1980   | No file  | `bd6af37b0d43`  |
| 1969   | No file  | `bd6af37b0d43`  |
| 1964   | No file  | `bd6af37b0d43`  |
| 1958   | No file  | `bd6af37b0d43`  |
| 1950   | No file  | `bd6af37b0d43`  |
| 1945   | No file  | `bd6af37b0d43`  |
| 1937   | No file  | `bd6af37b0d43`  |
| 1933   | No file  | `bd6af37b0d43`  |
| 1927   | No file  | `bd6af37b0d43`  |
| 1921   | No file  | `bd6af37b0d43`  |
| 1914   | No file  | `bd6af37b0d43`  |
| 1908   | No file  | `bd6af37b0d43`  |
| 1897   | No file  | `bd6af37b0d43`  |
| 1892   | No file  | `bd6af37b0d43`  |
| 1886   | No file  | `bd6af37b0d43`  |
| 1881   | No file  | `bd6af37b0d43`  |
| 1871   | No file  | `bd6af37b0d43`  |
| 1866   | No file  | `bd6af37b0d43`  |
| 1862   | No file  | `bd6af37b0d43`  |
| 1854   | No file  | `bd6af37b0d43`  |
| 1846   | No file  | `bd6af37b0d43`  |
| 1838   | No file  | `bd6af37b0d43`  |
| 1832   | No file  | `bd6af37b0d43`  |
| 1826   | No file  | `bd6af37b0d43`  |
| 1822   | No file  | `bd6af37b0d43`  |
| 1818   | No file  | `bd6af37b0d43`  |
| 1804   | No file  | `bd6af37b0d43`  |
| 1794   | No file  | `bd6af37b0d43`  |
| 1790   | No file  | `bd6af37b0d43`  |
| 1784   | No file  | `bd6af37b0d43`  |
| 1774   | No file  | `bd6af37b0d43`  |
| 1771   | No file  | `bd6af37b0d43`  |
| 1762   | No file  | `bd6af37b0d43`  |
| 1759   | No file  | `bd6af37b0d43`  |
| 1754   | No file  | `bd6af37b0d43`  |
| 1749   | No file  | `bd6af37b0d43`  |
| 1743   | No file  | `bd6af37b0d43`  |
| 1737   | No file  | `bd6af37b0d43`  |
| 1731   | No file  | `bd6af37b0d43`  |
| 1725   | No file  | `bd6af37b0d43`  |
| 1717   | No file  | `bd6af37b0d43`  |
| 1710   | No file  | `bd6af37b0d43`  |
| 1704   | No file  | `bd6af37b0d43`  |
| 1698   | No file  | `bd6af37b0d43`  |
| 1690   | No file  | `bd6af37b0d43`  |
| 1685   | No file  | `bd6af37b0d43`  |
| 1680   | No file  | `bd6af37b0d43`  |
| 1674   | No file  | `bd6af37b0d43`  |
| 1668   | No file  | `bd6af37b0d43`  |
| 1659   | No file  | `bd6af37b0d43`  |
| 1649   | No file  | `bd6af37b0d43`  |
| 1642   | No file  | `bd6af37b0d43`  |
| 1636   | No file  | `bd6af37b0d43`  |
| 1628   | No file  | `bd6af37b0d43`  |
| 1622   | No file  | `bd6af37b0d43`  |
| 1614   | No file  | `bd6af37b0d43`  |
| 1608   | No file  | `bd6af37b0d43`  |
| 1602   | No file  | `bd6af37b0d43`  |
| 1598   | No file  | `bd6af37b0d43`  |
| 1594   | No file  | `bd6af37b0d43`  |
| 1590   | No file  | `bd6af37b0d43`  |
| 1587   | No file  | `bd6af37b0d43`  |
| 1584   | No file  | `bd6af37b0d43`  |
| 1579   | No file  | `bd6af37b0d43`  |
| 1572   | No file  | `bd6af37b0d43`  |
| 1565   | No file  | `bd6af37b0d43`  |
| 1559   | No file  | `bd6af37b0d43`  |
| 1554   | No file  | `bd6af37b0d43`  |
| 1547   | No file  | `bd6af37b0d43`  |
| 1537   | No file  | `bd6af37b0d43`  |
| 1529   | No file  | `bd6af37b0d43`  |
| 1524   | No file  | `bd6af37b0d43`  |
| 1519   | No file  | `bd6af37b0d43`  |
| 1509   | No file  | `bd6af37b0d43`  |
| 1506   | No file  | `bd6af37b0d43`  |
| 1504   | No file  | `bd6af37b0d43`  |
| 1500   | No file  | `bd6af37b0d43`  |
| 1493   | No file  | `bd6af37b0d43`  |
| 1489   | No file  | `bd6af37b0d43`  |
| 1485   | No file  | `bd6af37b0d43`  |
| 1481   | No file  | `bd6af37b0d43`  |
| 1474   | No file  | `bd6af37b0d43`  |
| 1466   | No file  | `bd6af37b0d43`  |
| 1462   | No file  | `bd6af37b0d43`  |
| 1459   | No file  | `bd6af37b0d43`  |
| 1453   | No file  | `bd6af37b0d43`  |
| 1450   | No file  | `bd6af37b0d43`  |
| 1445   | No file  | `bd6af37b0d43`  |
| 1439   | No file  | `bd6af37b0d43`  |
| 1433   | No file  | `bd6af37b0d43`  |
| 1430   | No file  | `bd6af37b0d43`  |
| 1426   | No file  | `bd6af37b0d43`  |
| 1421   | No file  | `bd6af37b0d43`  |
| 1417   | No file  | `bd6af37b0d43`  |
| 1416   | No file  | `bd6af37b0d43`  |
| 1409   | No file  | `bd6af37b0d43`  |
| 1405   | No file  | `bd6af37b0d43`  |
| 1401   | No file  | `bd6af37b0d43`  |
| 1396   | No file  | `bd6af37b0d43`  |
| 1391   | No file  | `bd6af37b0d43`  |
| 1390   | No file  | `bd6af37b0d43`  |
| 1386   | No file  | `bd6af37b0d43`  |
| 1381   | No file  | `bd6af37b0d43`  |
| 1379   | No file  | `bd6af37b0d43`  |
| 1372   | No file  | `bd6af37b0d43`  |
| 1366   | No file  | `bd6af37b0d43`  |
| 1364   | No file  | `bd6af37b0d43`  |
| 1363   | No file  | `bd6af37b0d43`  |
| 1360   | No file  | `bd6af37b0d43`  |
| 1358   | No file  | `bd6af37b0d43`  |
| 1355   | No file  | `bd6af37b0d43`  |
| 1351   | No file  | `bd6af37b0d43`  |
| 1348   | No file  | `bd6af37b0d43`  |
| 1346   | No file  | `bd6af37b0d43`  |
| 1341   | No file  | `bd6af37b0d43`  |
| 1340   | No file  | `bd6af37b0d43`  |
| 1338   | No file  | `bd6af37b0d43`  |
| 1335   | No file  | `bd6af37b0d43`  |
| 1333   | No file  | `bd6af37b0d43`  |
| 1329   | No file  | `bd6af37b0d43`  |
| 1327   | No file  | `bd6af37b0d43`  |
| 1324   | No file  | `bd6af37b0d43`  |
| 1321   | No file  | `bd6af37b0d43`  |
| 1319   | No file  | `bd6af37b0d43`  |
| 1318   | No file  | `bd6af37b0d43`  |
| 1316   | No file  | `bd6af37b0d43`  |
| 1313   | No file  | `bd6af37b0d43`  |
| 1311   | No file  | `bd6af37b0d43`  |
| 1309   | No file  | `bd6af37b0d43`  |
| 1304   | No file  | `bd6af37b0d43`  |
| 1292   | No file  | `bd6af37b0d43`  |
| 1286   | No file  | `bd6af37b0d43`  |
| 1280   | No file  | `bd6af37b0d43`  |
| 1276   | No file  | `bd6af37b0d43`  |
| 1267   | No file  | `bd6af37b0d43`  |
| 1261   | No file  | `bd6af37b0d43`  |
| 1256   | No file  | `bd6af37b0d43`  |
| 1250   | No file  | `bd6af37b0d43`  |
| 1246   | No file  | `bd6af37b0d43`  |
| 1239   | No file  | `bd6af37b0d43`  |
| 1230   | No file  | `bd6af37b0d43`  |
| 1226   | No file  | `bd6af37b0d43`  |
| 1220   | No file  | `bd6af37b0d43`  |
| 1217   | No file  | `bd6af37b0d43`  |
| 1211   | No file  | `bd6af37b0d43`  |
| 1210   | No file  | `bd6af37b0d43`  |
| 1208   | No file  | `bd6af37b0d43`  |
| 1203   | No file  | `bd6af37b0d43`  |
| 1197   | No file  | `bd6af37b0d43`  |
| 1194   | No file  | `bd6af37b0d43`  |
| 1192   | No file  | `bd6af37b0d43`  |
| 1187   | No file  | `bd6af37b0d43`  |
| 1183   | No file  | `bd6af37b0d43`  |
| 1177   | No file  | `bd6af37b0d43`  |
| 1173   | No file  | `bd6af37b0d43`  |
| 1167   | No file  | `bd6af37b0d43`  |
| 1164   | No file  | `bd6af37b0d43`  |
| 1156   | No file  | `bd6af37b0d43`  |
| 1149   | No file  | `bd6af37b0d43`  |
| 1144   | No file  | `bd6af37b0d43`  |
| 1137   | No file  | `bd6af37b0d43`  |
| 1132   | No file  | `bd6af37b0d43`  |
| 1127   | No file  | `bd6af37b0d43`  |
| 1122   | No file  | `bd6af37b0d43`  |
| 1118   | No file  | `bd6af37b0d43`  |
| 1114   | No file  | `bd6af37b0d43`  |
| 1109   | No file  | `bd6af37b0d43`  |
| 1102   | No file  | `bd6af37b0d43`  |
| 1096   | No file  | `bd6af37b0d43`  |
| 1088   | No file  | `bd6af37b0d43`  |
| 1081   | No file  | `bd6af37b0d43`  |
| 1076   | No file  | `bd6af37b0d43`  |
| 1069   | No file  | `bd6af37b0d43`  |
| 1064   | No file  | `bd6af37b0d43`  |
| 1058   | No file  | `bd6af37b0d43`  |
| 1051   | No file  | `bd6af37b0d43`  |
| 1044   | No file  | `bd6af37b0d43`  |
| 1036   | No file  | `bd6af37b0d43`  |
| 1026   | No file  | `bd6af37b0d43`  |
| 1016   | No file  | `bd6af37b0d43`  |
| 1009   | No file  | `bd6af37b0d43`  |
| 1005   | No file  | `bd6af37b0d43`  |
| 1000   | No file  | `bd6af37b0d43`  |
| 998    | No file  | `bd6af37b0d43`  |
| 990    | No file  | `bd6af37b0d43`  |
| 979    | No file  | `bd6af37b0d43`  |
| 972    | No file  | `bd6af37b0d43`  |
| 963    | No file  | `bd6af37b0d43`  |
| 955    | No file  | `bd6af37b0d43`  |
| 946    | No file  | `bd6af37b0d43`  |
| 938    | No file  | `bd6af37b0d43`  |
| 927    | No file  | `bd6af37b0d43`  |
| 911    | No file  | `bd6af37b0d43`  |
| 904    | No file  | `bd6af37b0d43`  |
| 899    | No file  | `bd6af37b0d43`  |
| 894    | No file  | `bd6af37b0d43`  |
| 885    | No file  | `bd6af37b0d43`  |
| 879    | No file  | `bd6af37b0d43`  |
| 872    | No file  | `bd6af37b0d43`  |
| 864    | No file  | `bd6af37b0d43`  |
| 855    | No file  | `bd6af37b0d43`  |
| 853    | No file  | `bd6af37b0d43`  |
| 845    | No file  | `bd6af37b0d43`  |
| 837    | No file  | `bd6af37b0d43`  |
| 829    | No file  | `bd6af37b0d43`  |
| 822    | No file  | `bd6af37b0d43`  |
| 814    | No file  | `bd6af37b0d43`  |
| 805    | No file  | `bd6af37b0d43`  |
| 794    | No file  | `bd6af37b0d43`  |
| 787    | No file  | `bd6af37b0d43`  |
| 780    | No file  | `bd6af37b0d43`  |
| 771    | No file  | `bd6af37b0d43`  |
| 760    | No file  | `bd6af37b0d43`  |
| 748    | No file  | `bd6af37b0d43`  |
| 741    | No file  | `bd6af37b0d43`  |
| 736    | No file  | `bd6af37b0d43`  |
| 731    | No file  | `bd6af37b0d43`  |
| 723    | No file  | `bd6af37b0d43`  |
| 711    | No file  | `bd6af37b0d43`  |
| 707    | No file  | `bd6af37b0d43`  |
| 697    | No file  | `bd6af37b0d43`  |
| 689    | No file  | `bd6af37b0d43`  |
| 683    | No file  | `bd6af37b0d43`  |
| 678    | No file  | `bd6af37b0d43`  |
| 670    | No file  | `bd6af37b0d43`  |
| 661    | No file  | `bd6af37b0d43`  |
| 656    | No file  | `bd6af37b0d43`  |
| 652    | No file  | `bd6af37b0d43`  |
| 643    | No file  | `bd6af37b0d43`  |
| 637    | No file  | `bd6af37b0d43`  |
| 630    | No file  | `bd6af37b0d43`  |
| 627    | No file  | `bd6af37b0d43`  |
| 621    | No file  | `bd6af37b0d43`  |
| 617    | No file  | `bd6af37b0d43`  |
| 615    | No file  | `bd6af37b0d43`  |
| 606    | No file  | `bd6af37b0d43`  |
| 599    | No file  | `bd6af37b0d43`  |
| 592    | No file  | `bd6af37b0d43`  |
| 586    | No file  | `bd6af37b0d43`  |
| 577    | No file  | `bd6af37b0d43`  |
| 569    | No file  | `bd6af37b0d43`  |
| 561    | No file  | `bd6af37b0d43`  |
| 554    | No file  | `bd6af37b0d43`  |
| 542    | No file  | `bd6af37b0d43`  |
| 532    | No file  | `bd6af37b0d43`  |
| 531    | No file  | `bd6af37b0d43`  |
| 526    | No file  | `bd6af37b0d43`  |
| 521    | No file  | `bd6af37b0d43`  |
| 517    | No file  | `bd6af37b0d43`  |
| 510    | No file  | `bd6af37b0d43`  |
| 508    | No file  | `bd6af37b0d43`  |
| 504    | No file  | `bd6af37b0d43`  |
| 497    | No file  | `bd6af37b0d43`  |
| 491    | No file  | `bd6af37b0d43`  |
| 485    | No file  | `bd6af37b0d43`  |
| 478    | No file  | `bd6af37b0d43`  |
| 472    | No file  | `bd6af37b0d43`  |
| 466    | No file  | `bd6af37b0d43`  |
| 457    | No file  | `bd6af37b0d43`  |
| 452    | No file  | `bd6af37b0d43`  |
| 449    | No file  | `bd6af37b0d43`  |
| 435    | No file  | `bd6af37b0d43`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Skill names, LOC type 10     |

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

### Row (8 bytes)

| Offset  | Type | Field               | Notes                                                                 |
| ------- | ---- | ------------------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | skill_type          | `__eRoseWarSkillType_*` value; see Skill Types                        |
| `+0x04` | u16  | kamasylvia_skill_no | `skill.dbss` skill number for team `0` (Kamasylvia); LOC type 10 name |
| `+0x06` | u16  | odyllita_skill_no   | Skill number for team `1` (O'dyllita)                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Skill Types

`panel_rosewar_teamskill.luac` (client 3474) lists the skill types in this
order, and the Lua reads each skill with `ToClient_GetRoseWarSkillKey(skillType)`
and `getSkillStaticStatus(skillNo, 1)`. The Lua holds the names only; the
values are the list position from `1`, and each value's skill text (LOC type
10, `str_id4` 1) matches its name:

| `skill_type` | Lua name                                 | Skills on client 3474 | Name (LOC type 10)                       |
| ------------ | ---------------------------------------- | --------------------- | ---------------------------------------- |
| `1`          | `__eRoseWarSkillType_Scan`               | `15280`               | Enhance Vision                           |
| `2`          | `__eRoseWarSkillType_Recall`             | `15281`               | Rally Forces (teleports a platoon)       |
| `3`          | `__eRoseWarSkillType_Bombard`            | `15282`, `15286`      | Powerful Attack (King Griffon, Fugitive Khalk) |
| `4`          | `__eRoseWarSkillType_Summon`             | `15283`               | Summon Ogre                              |
| `5`          | `__eRoseWarSkillType_Conceal`            | `15284`               | Obscure Vision                           |
| `6`          | `__eRoseWarSkillType_Zonya`              | `15285`               | Immobilize Guardians                     |
| `7`          | `__eRoseWarSkillType_FixedResurrection`  | `15287`               | Strategic Revival                        |

## Field Names

The Rose War is newer than client 1784, so no sheet of a private server's
`DataSheets.bexcel` on that client covers it; the names come from the client
Lua and LOC. Both skill numbers resolve to LOC type 10 skill names. The team
split follows the Bombard row: `15282` summons King Griffon, which LOC places
in the Ash Forest of Kamasylvia (item `42545`), and `15286` summons Fugitive
Khalk, and the Khalk attack alongside the Ahib in the Ahib Conflict Zone
quests (LOC type 18 `7200`, `7211`). Team `0` is Kamasylvia and team `1`
O'dyllita in [`rosewarteamnostaticstatus.bss`](rosewarteamnostaticstatus_bss.md).

## Notes

- Raw bytes on clients 3002 to 3474:
  `50 41 42 52 07 00 00 00 01 00 00 00 B0 3B B0 3B 02 00 00 00 B1 3B B1 3B 03 00 00 00 B2 3B B6 3B 04 00 00 00 B3 3B B3 3B 05 00 00 00 B4 3B B4 3B 06 00 00 00 B5 3B B5 3B 07 00 00 00 B7 3B B7 3B 00 00 00 00 40 00 00 00 00 00 00 00`
  (76 bytes). The file is not in the archives of client 1784.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews this
  file with the shared layout table in `_bss/pabr_values/rosewar_tables.py`,
  with the skill type's Lua name and both skill names.
