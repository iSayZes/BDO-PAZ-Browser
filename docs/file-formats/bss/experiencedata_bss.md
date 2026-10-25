# `experiencedata.bss` Format

## Purpose

The first-experience triggers of the Black Spirit guide: each row waits
for an event (`WhenShow(1);`, `completeQuest(8000,55);`,
`checkposition(...)`), checks a constant condition (`getLevel()>99;`,
`clearquest`, `getknowledge`), then runs one script: the Black Spirit
appears (`AppearBlackSprit(8000,56)`), a client Lua function runs
(`ShowLua(move_tutorial1)`), a cutscene plays or the Magnus entry starts.
A delete condition retires the row (`ClearQuest(8000,55);`,
`getLevel()>1`). The rows are the `FirstExperience` sheet; the file is
not an EXP table and has no link to [`experience.bss`](experience_bss.md).
It is a PABR table of 17-byte rows whose scripts sit in the string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                 | Bytes   | Records   | Row bytes                 |
| ------ | ------------- | -------------------- | ------- | --------- | ------------------------- |
| 2      | 805 and later | `experiencedata.bss` | 247,896 | 1,608 Row | 17                        |
| 1      | 435 to 794    | `experiencedata.bss` | 88,330  | 502 Row   | 95 to 503, 176 on average |

| Layout | File                 | Known              | Unknown    |
| ------ | -------------------- | ------------------ | ---------- |
| 2      | `experiencedata.bss` | 247,896 B (100.0%) | 0 B (0.0%) |
| 1      | `experiencedata.bss` | 88,330 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `ef8f618f782b`  |
| 3482   | Layout 2 | `ef8f618f782b`  |
| 3474   | Layout 2 | `ef8f618f782b`  |
| 3473   | Layout 2 | `ef8f618f782b`  |
| 3464   | Layout 2 | `ef8f618f782b`  |
| 3458   | Layout 2 | `ef8f618f782b`  |
| 3454   | Layout 2 | `ef8f618f782b`  |
| 3444   | Layout 2 | `ef8f618f782b`  |
| 3435   | Layout 2 | `ef8f618f782b`  |
| 3426   | Layout 2 | `ef8f618f782b`  |
| 3418   | Layout 2 | `ef8f618f782b`  |
| 3412   | Layout 2 | `ef8f618f782b`  |
| 3402   | Layout 2 | `ef8f618f782b`  |
| 3396   | Layout 2 | `ef8f618f782b`  |
| 3387   | Layout 2 | `ef8f618f782b`  |
| 3381   | Layout 2 | `ef8f618f782b`  |
| 3373   | Layout 2 | `ef8f618f782b`  |
| 3364   | Layout 2 | `ef8f618f782b`  |
| 3356   | Layout 2 | `ef8f618f782b`  |
| 3349   | Layout 2 | `ef8f618f782b`  |
| 3342   | Layout 2 | `ef8f618f782b`  |
| 3335   | Layout 2 | `ef8f618f782b`  |
| 3326   | Layout 2 | `ef8f618f782b`  |
| 3321   | Layout 2 | `ef8f618f782b`  |
| 3314   | Layout 2 | `ef8f618f782b`  |
| 3303   | Layout 2 | `ef8f618f782b`  |
| 3302   | Layout 2 | `ef8f618f782b`  |
| 3293   | Layout 2 | `ef8f618f782b`  |
| 3283   | Layout 2 | `ef8f618f782b`  |
| 3275   | Layout 2 | `ef8f618f782b`  |
| 3267   | Layout 2 | `ef8f618f782b`  |
| 3258   | Layout 2 | `ef8f618f782b`  |
| 3251   | Layout 2 | `ef8f618f782b`  |
| 3242   | Layout 2 | `ef8f618f782b`  |
| 3235   | Layout 2 | `ef8f618f782b`  |
| 3229   | Layout 2 | `ef8f618f782b`  |
| 3212   | Layout 2 | `ef8f618f782b`  |
| 3203   | Layout 2 | `ef8f618f782b`  |
| 3193   | Layout 2 | `ef8f618f782b`  |
| 3186   | Layout 2 | `ef8f618f782b`  |
| 3177   | Layout 2 | `ef8f618f782b`  |
| 3169   | Layout 2 | `ef8f618f782b`  |
| 3158   | Layout 2 | `ef8f618f782b`  |
| 3151   | Layout 2 | `ef8f618f782b`  |
| 3144   | Layout 2 | `ef8f618f782b`  |
| 3133   | Layout 2 | `ef8f618f782b`  |
| 3125   | Layout 2 | `ef8f618f782b`  |
| 3118   | Layout 2 | `ef8f618f782b`  |
| 3111   | Layout 2 | `ef8f618f782b`  |
| 3103   | Layout 2 | `ef8f618f782b`  |
| 3095   | Layout 2 | `ef8f618f782b`  |
| 3086   | Layout 2 | `ef8f618f782b`  |
| 3072   | Layout 2 | `ef8f618f782b`  |
| 3062   | Layout 2 | `ef8f618f782b`  |
| 3052   | Layout 2 | `ef8f618f782b`  |
| 3045   | Layout 2 | `ef8f618f782b`  |
| 3037   | Layout 2 | `ef8f618f782b`  |
| 3030   | Layout 2 | `ef8f618f782b`  |
| 3021   | Layout 2 | `ef8f618f782b`  |
| 3012   | Layout 2 | `ef8f618f782b`  |
| 3002   | Layout 2 | `ef8f618f782b`  |
| 2995   | Layout 2 | `ef8f618f782b`  |
| 2987   | Layout 2 | `ef8f618f782b`  |
| 2978   | Layout 2 | `ef8f618f782b`  |
| 2970   | Layout 2 | `ef8f618f782b`  |
| 2959   | Layout 2 | `ef8f618f782b`  |
| 2951   | Layout 2 | `ef8f618f782b`  |
| 2942   | Layout 2 | `ef8f618f782b`  |
| 2935   | Layout 2 | `ef8f618f782b`  |
| 2932   | Layout 2 | `ef8f618f782b`  |
| 2923   | Layout 2 | `ef8f618f782b`  |
| 2919   | Layout 2 | `ef8f618f782b`  |
| 2907   | Layout 2 | `ef8f618f782b`  |
| 2900   | Layout 2 | `ef8f618f782b`  |
| 2891   | Layout 2 | `ef8f618f782b`  |
| 2882   | Layout 2 | `ef8f618f782b`  |
| 2872   | Layout 2 | `ef8f618f782b`  |
| 2863   | Layout 2 | `ef8f618f782b`  |
| 2855   | Layout 2 | `ef8f618f782b`  |
| 2849   | Layout 2 | `ef8f618f782b`  |
| 2844   | Layout 2 | `ef8f618f782b`  |
| 2834   | Layout 2 | `ef8f618f782b`  |
| 2825   | Layout 2 | `ef8f618f782b`  |
| 2819   | Layout 2 | `ef8f618f782b`  |
| 2811   | Layout 2 | `ef8f618f782b`  |
| 2803   | Layout 2 | `ef8f618f782b`  |
| 2794   | Layout 2 | `ef8f618f782b`  |
| 2783   | Layout 2 | `ef8f618f782b`  |
| 2774   | Layout 2 | `ef8f618f782b`  |
| 2765   | Layout 2 | `ef8f618f782b`  |
| 2756   | Layout 2 | `ef8f618f782b`  |
| 2750   | Layout 2 | `ef8f618f782b`  |
| 2743   | Layout 2 | `ef8f618f782b`  |
| 2736   | Layout 2 | `ef8f618f782b`  |
| 2726   | Layout 2 | `ef8f618f782b`  |
| 2717   | Layout 2 | `ef8f618f782b`  |
| 2709   | Layout 2 | `ef8f618f782b`  |
| 2703   | Layout 2 | `ef8f618f782b`  |
| 2695   | Layout 2 | `ef8f618f782b`  |
| 2684   | Layout 2 | `ef8f618f782b`  |
| 2672   | Layout 2 | `ef8f618f782b`  |
| 2665   | Layout 2 | `ef8f618f782b`  |
| 2657   | Layout 2 | `ef8f618f782b`  |
| 2649   | Layout 2 | `ef8f618f782b`  |
| 2644   | Layout 2 | `ef8f618f782b`  |
| 2637   | Layout 2 | `ef8f618f782b`  |
| 2629   | Layout 2 | `ef8f618f782b`  |
| 2619   | Layout 2 | `ef8f618f782b`  |
| 2612   | Layout 2 | `ef8f618f782b`  |
| 2606   | Layout 2 | `ef8f618f782b`  |
| 2602   | Layout 2 | `ef8f618f782b`  |
| 2601   | Layout 2 | `ef8f618f782b`  |
| 2592   | Layout 2 | `ef8f618f782b`  |
| 2583   | Layout 2 | `ef8f618f782b`  |
| 2575   | Layout 2 | `ef8f618f782b`  |
| 2567   | Layout 2 | `ef8f618f782b`  |
| 2560   | Layout 2 | `ef8f618f782b`  |
| 2553   | Layout 2 | `ef8f618f782b`  |
| 2545   | Layout 2 | `ef8f618f782b`  |
| 2538   | Layout 2 | `ef8f618f782b`  |
| 2529   | Layout 2 | `ef8f618f782b`  |
| 2519   | Layout 2 | `ef8f618f782b`  |
| 2513   | Layout 2 | `ef8f618f782b`  |
| 2510   | Layout 2 | `ef8f618f782b`  |
| 2507   | Layout 2 | `ef8f618f782b`  |
| 2503   | Layout 2 | `ef8f618f782b`  |
| 2498   | Layout 2 | `ef8f618f782b`  |
| 2492   | Layout 2 | `ef8f618f782b`  |
| 2487   | Layout 2 | `ef8f618f782b`  |
| 2480   | Layout 2 | `ef8f618f782b`  |
| 2474   | Layout 2 | `ef8f618f782b`  |
| 2468   | Layout 2 | `ef8f618f782b`  |
| 2460   | Layout 2 | `ef8f618f782b`  |
| 2453   | Layout 2 | `ef8f618f782b`  |
| 2444   | Layout 2 | `ef8f618f782b`  |
| 2438   | Layout 2 | `ef8f618f782b`  |
| 2434   | Layout 2 | `ef8f618f782b`  |
| 2429   | Layout 2 | `ef8f618f782b`  |
| 2421   | Layout 2 | `ef8f618f782b`  |
| 2414   | Layout 2 | `ef8f618f782b`  |
| 2407   | Layout 2 | `ef8f618f782b`  |
| 2401   | Layout 2 | `ef8f618f782b`  |
| 2397   | Layout 2 | `ef8f618f782b`  |
| 2393   | Layout 2 | `ef8f618f782b`  |
| 2384   | Layout 2 | `ef8f618f782b`  |
| 2378   | Layout 2 | `ef8f618f782b`  |
| 2372   | Layout 2 | `ef8f618f782b`  |
| 2358   | Layout 2 | `ef8f618f782b`  |
| 2352   | Layout 2 | `ef8f618f782b`  |
| 2347   | Layout 2 | `ef8f618f782b`  |
| 2343   | Layout 2 | `ef8f618f782b`  |
| 2335   | Layout 2 | `ef8f618f782b`  |
| 2327   | Layout 2 | `ef8f618f782b`  |
| 2324   | Layout 2 | `ef8f618f782b`  |
| 2319   | Layout 2 | `ef8f618f782b`  |
| 2313   | Layout 2 | `ef8f618f782b`  |
| 2308   | Layout 2 | `ef8f618f782b`  |
| 2302   | Layout 2 | `ef8f618f782b`  |
| 2295   | Layout 2 | `ef8f618f782b`  |
| 2290   | Layout 2 | `ef8f618f782b`  |
| 2284   | Layout 2 | `ef8f618f782b`  |
| 2276   | Layout 2 | `ef8f618f782b`  |
| 2269   | Layout 2 | `ef8f618f782b`  |
| 2259   | Layout 2 | `ef8f618f782b`  |
| 2250   | Layout 2 | `ef8f618f782b`  |
| 2243   | Layout 2 | `ef8f618f782b`  |
| 2235   | Layout 2 | `ef8f618f782b`  |
| 2229   | Layout 2 | `ef8f618f782b`  |
| 2224   | Layout 2 | `ef8f618f782b`  |
| 2218   | Layout 2 | `ef8f618f782b`  |
| 2215   | Layout 2 | `ef8f618f782b`  |
| 2207   | Layout 2 | `ef8f618f782b`  |
| 2203   | Layout 2 | `ef8f618f782b`  |
| 2196   | Layout 2 | `ef8f618f782b`  |
| 2192   | Layout 2 | `ef8f618f782b`  |
| 2189   | Layout 2 | `ef8f618f782b`  |
| 2183   | Layout 2 | `ef8f618f782b`  |
| 2179   | Layout 2 | `ef8f618f782b`  |
| 2171   | Layout 2 | `ef8f618f782b`  |
| 2163   | Layout 2 | `ef8f618f782b`  |
| 2156   | Layout 2 | `ef8f618f782b`  |
| 2151   | Layout 2 | `ef8f618f782b`  |
| 2147   | Layout 2 | `ef8f618f782b`  |
| 2142   | Layout 2 | `ef8f618f782b`  |
| 2138   | Layout 2 | `ef8f618f782b`  |
| 2134   | Layout 2 | `ef8f618f782b`  |
| 2130   | Layout 2 | `ef8f618f782b`  |
| 2122   | Layout 2 | `ef8f618f782b`  |
| 2107   | Layout 2 | `ef8f618f782b`  |
| 2098   | Layout 2 | `ef8f618f782b`  |
| 2089   | Layout 2 | `ef8f618f782b`  |
| 2081   | Layout 2 | `ef8f618f782b`  |
| 2073   | Layout 2 | `ef8f618f782b`  |
| 2067   | Layout 2 | `ef8f618f782b`  |
| 2063   | Layout 2 | `ef8f618f782b`  |
| 2059   | Layout 2 | `ef8f618f782b`  |
| 2052   | Layout 2 | `ef8f618f782b`  |
| 2044   | Layout 2 | `ef8f618f782b`  |
| 2039   | Layout 2 | `ef8f618f782b`  |
| 2032   | Layout 2 | `ef8f618f782b`  |
| 2025   | Layout 2 | `ef8f618f782b`  |
| 2011   | Layout 2 | `ef8f618f782b`  |
| 2005   | Layout 2 | `ef8f618f782b`  |
| 2000   | Layout 2 | `ef8f618f782b`  |
| 1996   | Layout 2 | `ef8f618f782b`  |
| 1991   | Layout 2 | `ef8f618f782b`  |
| 1985   | Layout 2 | `ef8f618f782b`  |
| 1980   | Layout 2 | `ef8f618f782b`  |
| 1969   | Layout 2 | `ef8f618f782b`  |
| 1964   | Layout 2 | `ef8f618f782b`  |
| 1958   | Layout 2 | `ef8f618f782b`  |
| 1950   | Layout 2 | `ef8f618f782b`  |
| 1945   | Layout 2 | `ef8f618f782b`  |
| 1937   | Layout 2 | `ef8f618f782b`  |
| 1933   | Layout 2 | `ef8f618f782b`  |
| 1927   | Layout 2 | `ef8f618f782b`  |
| 1921   | Layout 2 | `ef8f618f782b`  |
| 1914   | Layout 2 | `ef8f618f782b`  |
| 1908   | Layout 2 | `ef8f618f782b`  |
| 1897   | Layout 2 | `ef8f618f782b`  |
| 1892   | Layout 2 | `ef8f618f782b`  |
| 1886   | Layout 2 | `ef8f618f782b`  |
| 1881   | Layout 2 | `ef8f618f782b`  |
| 1871   | Layout 2 | `ef8f618f782b`  |
| 1866   | Layout 2 | `ef8f618f782b`  |
| 1862   | Layout 2 | `ef8f618f782b`  |
| 1854   | Layout 2 | `ef8f618f782b`  |
| 1846   | Layout 2 | `ef8f618f782b`  |
| 1838   | Layout 2 | `ef8f618f782b`  |
| 1832   | Layout 2 | `ef8f618f782b`  |
| 1826   | Layout 2 | `ef8f618f782b`  |
| 1822   | Layout 2 | `ef8f618f782b`  |
| 1818   | Layout 2 | `ef8f618f782b`  |
| 1804   | Layout 2 | `ef8f618f782b`  |
| 1794   | Layout 2 | `ef8f618f782b`  |
| 1790   | Layout 2 | `ef8f618f782b`  |
| 1784   | Layout 2 | `ef8f618f782b`  |
| 1774   | Layout 2 | `ef8f618f782b`  |
| 1771   | Layout 2 | `ef8f618f782b`  |
| 1762   | Layout 2 | `ef8f618f782b`  |
| 1759   | Layout 2 | `ef8f618f782b`  |
| 1754   | Layout 2 | `ef8f618f782b`  |
| 1749   | Layout 2 | `ef8f618f782b`  |
| 1743   | Layout 2 | `ef8f618f782b`  |
| 1737   | Layout 2 | `ef8f618f782b`  |
| 1731   | Layout 2 | `ef8f618f782b`  |
| 1725   | Layout 2 | `ef8f618f782b`  |
| 1717   | Layout 2 | `ef8f618f782b`  |
| 1710   | Layout 2 | `ef8f618f782b`  |
| 1704   | Layout 2 | `ef8f618f782b`  |
| 1698   | Layout 2 | `ef8f618f782b`  |
| 1690   | Layout 2 | `ef8f618f782b`  |
| 1685   | Layout 2 | `ef8f618f782b`  |
| 1680   | Layout 2 | `ef8f618f782b`  |
| 1674   | Layout 2 | `ef8f618f782b`  |
| 1668   | Layout 2 | `ef8f618f782b`  |
| 1659   | Layout 2 | `ef8f618f782b`  |
| 1649   | Layout 2 | `ef8f618f782b`  |
| 1642   | Layout 2 | `ef8f618f782b`  |
| 1636   | Layout 2 | `ef8f618f782b`  |
| 1628   | Layout 2 | `ef8f618f782b`  |
| 1622   | Layout 2 | `ef8f618f782b`  |
| 1614   | Layout 2 | `ef8f618f782b`  |
| 1608   | Layout 2 | `ef8f618f782b`  |
| 1602   | Layout 2 | `ef8f618f782b`  |
| 1598   | Layout 2 | `ef8f618f782b`  |
| 1594   | Layout 2 | `ef8f618f782b`  |
| 1590   | Layout 2 | `ef8f618f782b`  |
| 1587   | Layout 2 | `ef8f618f782b`  |
| 1584   | Layout 2 | `ef8f618f782b`  |
| 1579   | Layout 2 | `ef8f618f782b`  |
| 1572   | Layout 2 | `ef8f618f782b`  |
| 1565   | Layout 2 | `ef8f618f782b`  |
| 1559   | Layout 2 | `ef8f618f782b`  |
| 1554   | Layout 2 | `ef8f618f782b`  |
| 1547   | Layout 2 | `ef8f618f782b`  |
| 1537   | Layout 2 | `ef8f618f782b`  |
| 1529   | Layout 2 | `ef8f618f782b`  |
| 1524   | Layout 2 | `ef8f618f782b`  |
| 1519   | Layout 2 | `ef8f618f782b`  |
| 1509   | Layout 2 | `ef8f618f782b`  |
| 1506   | Layout 2 | `ef8f618f782b`  |
| 1504   | Layout 2 | `ef8f618f782b`  |
| 1500   | Layout 2 | `ef8f618f782b`  |
| 1493   | Layout 2 | `ef8f618f782b`  |
| 1489   | Layout 2 | `ef8f618f782b`  |
| 1485   | Layout 2 | `ef8f618f782b`  |
| 1481   | Layout 2 | `ef8f618f782b`  |
| 1474   | Layout 2 | `ef8f618f782b`  |
| 1466   | Layout 2 | `ef8f618f782b`  |
| 1462   | Layout 2 | `ef8f618f782b`  |
| 1459   | Layout 2 | `ef8f618f782b`  |
| 1453   | Layout 2 | `ef8f618f782b`  |
| 1450   | Layout 2 | `ef8f618f782b`  |
| 1445   | Layout 2 | `ef8f618f782b`  |
| 1439   | Layout 2 | `ef8f618f782b`  |
| 1433   | Layout 2 | `ef8f618f782b`  |
| 1430   | Layout 2 | `ef8f618f782b`  |
| 1426   | Layout 2 | `ef8f618f782b`  |
| 1421   | Layout 2 | `ef8f618f782b`  |
| 1417   | Layout 2 | `ef8f618f782b`  |
| 1416   | Layout 2 | `ef8f618f782b`  |
| 1409   | Layout 2 | `ef8f618f782b`  |
| 1405   | Layout 2 | `ef8f618f782b`  |
| 1401   | Layout 2 | `ef8f618f782b`  |
| 1396   | Layout 2 | `ef8f618f782b`  |
| 1391   | Layout 2 | `ef8f618f782b`  |
| 1390   | Layout 2 | `ef8f618f782b`  |
| 1386   | Layout 2 | `ef8f618f782b`  |
| 1381   | Layout 2 | `ef8f618f782b`  |
| 1379   | Layout 2 | `ef8f618f782b`  |
| 1372   | Layout 2 | `ef8f618f782b`  |
| 1366   | Layout 2 | `ef8f618f782b`  |
| 1364   | Layout 2 | `ef8f618f782b`  |
| 1363   | Layout 2 | `ef8f618f782b`  |
| 1360   | Layout 2 | `ef8f618f782b`  |
| 1358   | Layout 2 | `ef8f618f782b`  |
| 1355   | Layout 2 | `ef8f618f782b`  |
| 1351   | Layout 2 | `ef8f618f782b`  |
| 1348   | Layout 2 | `ef8f618f782b`  |
| 1346   | Layout 2 | `ef8f618f782b`  |
| 1341   | Layout 2 | `ef8f618f782b`  |
| 1340   | Layout 2 | `ef8f618f782b`  |
| 1338   | Layout 2 | `ef8f618f782b`  |
| 1335   | Layout 2 | `ef8f618f782b`  |
| 1333   | Layout 2 | `ef8f618f782b`  |
| 1329   | Layout 2 | `ef8f618f782b`  |
| 1327   | Layout 2 | `ef8f618f782b`  |
| 1324   | Layout 2 | `ef8f618f782b`  |
| 1321   | Layout 2 | `ef8f618f782b`  |
| 1319   | Layout 2 | `ef8f618f782b`  |
| 1318   | Layout 2 | `ef8f618f782b`  |
| 1316   | Layout 2 | `ef8f618f782b`  |
| 1313   | Layout 2 | `ef8f618f782b`  |
| 1311   | Layout 2 | `ef8f618f782b`  |
| 1309   | Layout 2 | `ef8f618f782b`  |
| 1304   | Layout 2 | `ef8f618f782b`  |
| 1292   | Layout 2 | `ef8f618f782b`  |
| 1286   | Layout 2 | `ef8f618f782b`  |
| 1280   | Layout 2 | `ef8f618f782b`  |
| 1276   | Layout 2 | `ef8f618f782b`  |
| 1267   | Layout 2 | `ef8f618f782b`  |
| 1261   | Layout 2 | `ef8f618f782b`  |
| 1256   | Layout 2 | `ef8f618f782b`  |
| 1250   | Layout 2 | `ef8f618f782b`  |
| 1246   | Layout 2 | `ef8f618f782b`  |
| 1239   | Layout 2 | `ef8f618f782b`  |
| 1230   | Layout 2 | `ef8f618f782b`  |
| 1226   | Layout 2 | `ef8f618f782b`  |
| 1220   | Layout 2 | `ef8f618f782b`  |
| 1217   | Layout 2 | `ef8f618f782b`  |
| 1211   | Layout 2 | `ef8f618f782b`  |
| 1210   | Layout 2 | `ef8f618f782b`  |
| 1208   | Layout 2 | `ef8f618f782b`  |
| 1203   | Layout 2 | `ef8f618f782b`  |
| 1197   | Layout 2 | `ef8f618f782b`  |
| 1194   | Layout 2 | `ef8f618f782b`  |
| 1192   | Layout 2 | `ef8f618f782b`  |
| 1187   | Layout 2 | `ef8f618f782b`  |
| 1183   | Layout 2 | `ef8f618f782b`  |
| 1177   | Layout 2 | `ef8f618f782b`  |
| 1173   | Layout 2 | `ef8f618f782b`  |
| 1167   | Layout 2 | `ef8f618f782b`  |
| 1164   | Layout 2 | `ef8f618f782b`  |
| 1156   | Layout 2 | `ef8f618f782b`  |
| 1149   | Layout 2 | `ef8f618f782b`  |
| 1144   | Layout 2 | `ef8f618f782b`  |
| 1137   | Layout 2 | `ef8f618f782b`  |
| 1132   | Layout 2 | `ef8f618f782b`  |
| 1127   | Layout 2 | `ef8f618f782b`  |
| 1122   | Layout 2 | `ef8f618f782b`  |
| 1118   | Layout 2 | `ef8f618f782b`  |
| 1114   | Layout 2 | `ef8f618f782b`  |
| 1109   | Layout 2 | `ef8f618f782b`  |
| 1102   | Layout 2 | `ef8f618f782b`  |
| 1096   | Layout 2 | `ef8f618f782b`  |
| 1088   | Layout 2 | `ef8f618f782b`  |
| 1081   | Layout 2 | `ef8f618f782b`  |
| 1076   | Layout 2 | `ef8f618f782b`  |
| 1069   | Layout 2 | `ef8f618f782b`  |
| 1064   | Layout 2 | `ef8f618f782b`  |
| 1058   | Layout 2 | `ef8f618f782b`  |
| 1051   | Layout 2 | `ef8f618f782b`  |
| 1044   | Layout 2 | `ef8f618f782b`  |
| 1036   | Layout 2 | `ef8f618f782b`  |
| 1026   | Layout 2 | `ef8f618f782b`  |
| 1016   | Layout 2 | `ef8f618f782b`  |
| 1009   | Layout 2 | `ef8f618f782b`  |
| 1005   | Layout 2 | `ef8f618f782b`  |
| 1000   | Layout 2 | `ef8f618f782b`  |
| 998    | Layout 2 | `ef8f618f782b`  |
| 990    | Layout 2 | `ef8f618f782b`  |
| 979    | Layout 2 | `ef8f618f782b`  |
| 972    | Layout 2 | `ef8f618f782b`  |
| 963    | Layout 2 | `ef8f618f782b`  |
| 955    | Layout 2 | `ef8f618f782b`  |
| 946    | Layout 2 | `ef8f618f782b`  |
| 938    | Layout 2 | `ef8f618f782b`  |
| 927    | Layout 2 | `ef8f618f782b`  |
| 911    | Layout 2 | `ef8f618f782b`  |
| 904    | Layout 2 | `ef8f618f782b`  |
| 899    | Layout 2 | `ef8f618f782b`  |
| 894    | Layout 2 | `ef8f618f782b`  |
| 885    | Layout 2 | `ef8f618f782b`  |
| 879    | Layout 2 | `ef8f618f782b`  |
| 872    | Layout 2 | `ef8f618f782b`  |
| 864    | Layout 2 | `ef8f618f782b`  |
| 855    | Layout 2 | `ef8f618f782b`  |
| 853    | Layout 2 | `ef8f618f782b`  |
| 845    | Layout 2 | `ef8f618f782b`  |
| 837    | Layout 2 | `ef8f618f782b`  |
| 829    | Layout 2 | `ef8f618f782b`  |
| 822    | Layout 2 | `ef8f618f782b`  |
| 814    | Layout 2 | `ef8f618f782b`  |
| 805    | Layout 2 | `ef8f618f782b`  |
| 794    | Layout 1 | `ef8f618f782b`  |
| 787    | Layout 1 | `ef8f618f782b`  |
| 780    | Layout 1 | `ef8f618f782b`  |
| 771    | Layout 1 | `ef8f618f782b`  |
| 760    | Layout 1 | `ef8f618f782b`  |
| 748    | Layout 1 | `ef8f618f782b`  |
| 741    | Layout 1 | `ef8f618f782b`  |
| 736    | Layout 1 | `ef8f618f782b`  |
| 731    | Layout 1 | `ef8f618f782b`  |
| 723    | Layout 1 | `ef8f618f782b`  |
| 711    | Layout 1 | `ef8f618f782b`  |
| 707    | Layout 1 | `ef8f618f782b`  |
| 697    | Layout 1 | `ef8f618f782b`  |
| 689    | Layout 1 | `ef8f618f782b`  |
| 683    | Layout 1 | `ef8f618f782b`  |
| 678    | Layout 1 | `ef8f618f782b`  |
| 670    | Layout 1 | `ef8f618f782b`  |
| 661    | Layout 1 | `ef8f618f782b`  |
| 656    | Layout 1 | `ef8f618f782b`  |
| 652    | Layout 1 | `ef8f618f782b`  |
| 643    | Layout 1 | `ef8f618f782b`  |
| 637    | Layout 1 | `ef8f618f782b`  |
| 630    | Layout 1 | `ef8f618f782b`  |
| 627    | Layout 1 | `ef8f618f782b`  |
| 621    | Layout 1 | `ef8f618f782b`  |
| 617    | Layout 1 | `ef8f618f782b`  |
| 615    | Layout 1 | `ef8f618f782b`  |
| 606    | Layout 1 | `ef8f618f782b`  |
| 599    | Layout 1 | `ef8f618f782b`  |
| 592    | Layout 1 | `ef8f618f782b`  |
| 586    | Layout 1 | `ef8f618f782b`  |
| 577    | Layout 1 | `ef8f618f782b`  |
| 569    | Layout 1 | `ef8f618f782b`  |
| 561    | Layout 1 | `ef8f618f782b`  |
| 554    | Layout 1 | `ef8f618f782b`  |
| 542    | Layout 1 | `ef8f618f782b`  |
| 532    | Layout 1 | `ef8f618f782b`  |
| 531    | Layout 1 | `ef8f618f782b`  |
| 526    | Layout 1 | `ef8f618f782b`  |
| 521    | Layout 1 | `ef8f618f782b`  |
| 517    | Layout 1 | `ef8f618f782b`  |
| 510    | Layout 1 | `ef8f618f782b`  |
| 508    | Layout 1 | `ef8f618f782b`  |
| 504    | Layout 1 | `ef8f618f782b`  |
| 497    | Layout 1 | `ef8f618f782b`  |
| 491    | Layout 1 | `ef8f618f782b`  |
| 485    | Layout 1 | `ef8f618f782b`  |
| 478    | Layout 1 | `ef8f618f782b`  |
| 472    | Layout 1 | `ef8f618f782b`  |
| 466    | Layout 1 | `ef8f618f782b`  |
| 457    | Layout 1 | `ef8f618f782b`  |
| 452    | Layout 1 | `ef8f618f782b`  |
| 449    | Layout 1 | `ef8f618f782b`  |
| 435    | Layout 1 | `ef8f618f782b`  |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field              | Notes                                         |
| ------------------- | -------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count          | Number of rows                                |
| `+0x08`             | Row[row_count] | rows               | See Row                                       |
| `rows+0x00`         | String Table   | string_table       | See String Table                              |
| `string_table+0x00` | u32            | string_table_start | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero               | `0`                                           |

### Row (17 bytes)

| Offset  | Type | Field            | Notes                                                                                              |
| ------- | ---- | ---------------- | -------------------------------------------------------------------------------------------------- |
| `+0x00` | u32  | once_condition   | Index into `strings`: the event the row waits for (`WhenShow(2);AcceptQuest(1021,1)`); never empty |
| `+0x04` | u32  | constant_condition  | Index into `strings`: a condition that must also hold (`getLevel()>99;`); empty on 1,297 rows of client 3482 |
| `+0x08` | u32  | execute          | Index into `strings`: the script run when both hold (`AppearBlackSprit(8000,56)`); never empty     |
| `+0x0C` | u8   | repeat           | `0` or `1`                                                                                         |
| `+0x0D` | u32  | delete_condition | Index into `strings`: the condition that retires the row (`ClearQuest(8000,55);`)                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                    |
| ------- | ------------------ | ------------ | ------------------------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings                                                        |
| `+0x04` | pstr[string_count] | strings      | UTF-8 scripts; one empty string serves every empty `constant_condition`    |

## Layout 1

No PABR head and no string table: a u32 row count, then rows that hold
each script inline as UTF-16LE text.

### File Layout

| Offset  | Type           | Field     | Notes          |
| ------- | -------------- | --------- | -------------- |
| `+0x00` | u32            | row_count | Number of rows |
| `+0x04` | Row[row_count] | rows      | See Row        |

### Row (variable: 33 bytes + script text)

| Offset                 | Type  | Field              | Notes                                           |
| ---------------------- | ----- | ------------------ | ----------------------------------------------- |
| `+0x00`                | str16 | once_condition     | As in Layout 2, as text                         |
| `once_condition+0x00`  | str16 | constant_condition | As in Layout 2, as text; count `0` when empty   |
| `constant_condition+0x00` | str16 | execute         | As in Layout 2, as text                         |
| `execute+0x00`         | u8    | repeat             | As in Layout 2                                  |
| `execute+0x01`         | str16 | delete_condition   | As in Layout 2, as text                         |

## Scripts

Calls are joined by `;`, and a `!` in front of a call negates it. Counts
are rows using each call, client 3482 (1,608 rows, 3,996 strings).

| Field              | Calls (rows)                                                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `once_condition`   | `completequest` (1,129), `acceptquest` (238), `whenshow` (190), `checkposition` (123), `checkclearquest` (94), `checkinstancefieldmapkey` (31), `endcutscene` (14), `luaevent` (1) |
| `constant_condition`  | `clearquest` (148), `getknowledge` (86), `progressquest` (73), `checkclass` (34), `checkfieldtype` (26), `iscontentsgroupopen` (21), `getlevel` (16), `checkquestcondition` (15), `checkusertype` (2), `checkseasoncharacter` (1); empty on 1,297 rows |
| `execute`          | `AppearBlackSprit` (1,178), `ShowLua` (307), `AbyssOne` with `SetDummyActorActionKey` (111), `cutscene` (12)                                     |
| `delete_condition` | `clearquest` (1,468), `getlevel` (137), `getknowledge` (2)                                                                                       |

`WhenShow(n)` takes `2` on 176 rows, `1` on 12 and `3` on 2. The 12
`cutscene(CS_Velia_00_<class>_Start_0001.pas)` rows are the opening
cutscenes, one per class code (`PHM`, `PHW`, `PGM` and 9 more). 14
`EndCutScene` rows follow them, one per file and two more for
`CS_Velia_00_PNW_Start_0002.pas` and `CS_Velia_00_PNM_Start_0002.pas`;
each runs `ShowLua(move_tutorial1)`. `repeat` is `1` on 1,321 rows and
`0` on 287.

## Field Names

`once_condition`, `constant_condition`, `execute`, `repeat` and
`delete_condition` are the `OnceCondition`, `ConstCondition`, `Execute`,
`Repeat` and `DeleteCondition` columns of the `FirstExperience` sheet of
a private server's `DataSheets.bexcel` on client 1784, in that order. The
sheet's 1,039 rows match the 1,039 rows of that client's
`experiencedata.bss` in every column and in file order. The client's
`ShowableFirstExperience()` (`panel_intromovie.luac`) turns the
first-experience checks off while the intro video plays.

## Notes

- Up to client 794 the file sits at
  `gamecommondata/binary/en/experiencedata.bss` with the scripts inline
  (Layout 1); client 805 has the PABR file of Layout 2.
- 22 of the 37 `ShowLua` names are `funcText` cases of `executeLuaFunc()`
  in `tutorialmain.luac` (`move_tutorial1`, `closeDialog`, `manufacture`);
  the other 15 (`attack_tutorial`, `callSpirit`, `MorningLandStart` among
  them) are not, so the client handles them somewhere else.
- The rows have no key; the handler numbers them by their place in the
  file.

## Open Questions

### What `repeat` Does

The sheet column is `Repeat`, and `1` on 1,321 rows of client 3482. Every
row has a `delete_condition`, so `1` may let a row fire again until that
condition holds and `0` fire once, but no Lua reads the field to confirm
it.
