# `olviaacademypassstaticstatusmanager.bss` Format

## Purpose

The steps of the nine Olvia Academy Pass tabs
(`panel_window_olviaacademy_pass_all*.luac`). Per tab the file holds a step
count and per step the base quest and the pass quest, both packed quest IDs
`(quest_id << 16) | quest_chain_id` of
[`olviaacademypassquestlist.bss`](olviaacademyquestlist_bss.md). The tabs
have no key and no count: they follow the PABR magic one after the other, in
the order of the `__eOlviaAcademyPassType_*` values, up to the string table.
The curricula of the same academy are in
[`olviaacademycurriculumss.bss`](olviaacademycurriculumss_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                      | Bytes | Records         | Row bytes |
| ------ | -------------- | ----------------------------------------- | ----- | --------------- | --------- |
| 1      | 3186 and later | `olviaacademypassstaticstatusmanager.bss` | 772   | 90 Step, 9 Pass | 8         |

| Layout | File                                      | Known          | Unknown    |
| ------ | ----------------------------------------- | -------------- | ---------- |
| 1      | `olviaacademypassstaticstatusmanager.bss` | 772 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `1cff14b0ab14`  |
| 3482   | Layout 1 | `1cff14b0ab14`  |
| 3474   | Layout 1 | `1cff14b0ab14`  |
| 3473   | Layout 1 | `1cff14b0ab14`  |
| 3464   | Layout 1 | `1cff14b0ab14`  |
| 3458   | Layout 1 | `1cff14b0ab14`  |
| 3454   | Layout 1 | `1cff14b0ab14`  |
| 3444   | Layout 1 | `1cff14b0ab14`  |
| 3435   | Layout 1 | `1cff14b0ab14`  |
| 3426   | Layout 1 | `1cff14b0ab14`  |
| 3418   | Layout 1 | `1cff14b0ab14`  |
| 3412   | Layout 1 | `1cff14b0ab14`  |
| 3402   | Layout 1 | `1cff14b0ab14`  |
| 3396   | Layout 1 | `1cff14b0ab14`  |
| 3387   | Layout 1 | `1cff14b0ab14`  |
| 3381   | Layout 1 | `1cff14b0ab14`  |
| 3373   | Layout 1 | `1cff14b0ab14`  |
| 3364   | Layout 1 | `1cff14b0ab14`  |
| 3356   | Layout 1 | `1cff14b0ab14`  |
| 3349   | Layout 1 | `1cff14b0ab14`  |
| 3342   | Layout 1 | `1cff14b0ab14`  |
| 3335   | Layout 1 | `1cff14b0ab14`  |
| 3326   | Layout 1 | `1cff14b0ab14`  |
| 3321   | Layout 1 | `1cff14b0ab14`  |
| 3314   | Layout 1 | `1cff14b0ab14`  |
| 3303   | Layout 1 | `1cff14b0ab14`  |
| 3302   | Layout 1 | `1cff14b0ab14`  |
| 3293   | Layout 1 | `1cff14b0ab14`  |
| 3283   | Layout 1 | `1cff14b0ab14`  |
| 3275   | Layout 1 | `1cff14b0ab14`  |
| 3267   | Layout 1 | `1cff14b0ab14`  |
| 3258   | Layout 1 | `1cff14b0ab14`  |
| 3251   | Layout 1 | `1cff14b0ab14`  |
| 3242   | Layout 1 | `1cff14b0ab14`  |
| 3235   | Layout 1 | `1cff14b0ab14`  |
| 3229   | Layout 1 | `1cff14b0ab14`  |
| 3212   | Layout 1 | `1cff14b0ab14`  |
| 3203   | Layout 1 | `1cff14b0ab14`  |
| 3193   | Layout 1 | `1cff14b0ab14`  |
| 3186   | Layout 1 | `1cff14b0ab14`  |
| 3177   | No file  | `1cff14b0ab14`  |
| 3169   | No file  | `1cff14b0ab14`  |
| 3158   | No file  | `1cff14b0ab14`  |
| 3151   | No file  | `1cff14b0ab14`  |
| 3144   | No file  | `1cff14b0ab14`  |
| 3133   | No file  | `1cff14b0ab14`  |
| 3125   | No file  | `1cff14b0ab14`  |
| 3118   | No file  | `1cff14b0ab14`  |
| 3111   | No file  | `1cff14b0ab14`  |
| 3103   | No file  | `1cff14b0ab14`  |
| 3095   | No file  | `1cff14b0ab14`  |
| 3086   | No file  | `1cff14b0ab14`  |
| 3072   | No file  | `1cff14b0ab14`  |
| 3062   | No file  | `1cff14b0ab14`  |
| 3052   | No file  | `1cff14b0ab14`  |
| 3045   | No file  | `1cff14b0ab14`  |
| 3037   | No file  | `1cff14b0ab14`  |
| 3030   | No file  | `1cff14b0ab14`  |
| 3021   | No file  | `1cff14b0ab14`  |
| 3012   | No file  | `1cff14b0ab14`  |
| 3002   | No file  | `1cff14b0ab14`  |
| 2995   | No file  | `1cff14b0ab14`  |
| 2987   | No file  | `1cff14b0ab14`  |
| 2978   | No file  | `1cff14b0ab14`  |
| 2970   | No file  | `1cff14b0ab14`  |
| 2959   | No file  | `1cff14b0ab14`  |
| 2951   | No file  | `1cff14b0ab14`  |
| 2942   | No file  | `1cff14b0ab14`  |
| 2935   | No file  | `1cff14b0ab14`  |
| 2932   | No file  | `1cff14b0ab14`  |
| 2923   | No file  | `1cff14b0ab14`  |
| 2919   | No file  | `1cff14b0ab14`  |
| 2907   | No file  | `1cff14b0ab14`  |
| 2900   | No file  | `1cff14b0ab14`  |
| 2891   | No file  | `1cff14b0ab14`  |
| 2882   | No file  | `1cff14b0ab14`  |
| 2872   | No file  | `1cff14b0ab14`  |
| 2863   | No file  | `1cff14b0ab14`  |
| 2855   | No file  | `1cff14b0ab14`  |
| 2849   | No file  | `1cff14b0ab14`  |
| 2844   | No file  | `1cff14b0ab14`  |
| 2834   | No file  | `1cff14b0ab14`  |
| 2825   | No file  | `1cff14b0ab14`  |
| 2819   | No file  | `1cff14b0ab14`  |
| 2811   | No file  | `1cff14b0ab14`  |
| 2803   | No file  | `1cff14b0ab14`  |
| 2794   | No file  | `1cff14b0ab14`  |
| 2783   | No file  | `1cff14b0ab14`  |
| 2774   | No file  | `1cff14b0ab14`  |
| 2765   | No file  | `1cff14b0ab14`  |
| 2756   | No file  | `1cff14b0ab14`  |
| 2750   | No file  | `1cff14b0ab14`  |
| 2743   | No file  | `1cff14b0ab14`  |
| 2736   | No file  | `1cff14b0ab14`  |
| 2726   | No file  | `1cff14b0ab14`  |
| 2717   | No file  | `1cff14b0ab14`  |
| 2709   | No file  | `1cff14b0ab14`  |
| 2703   | No file  | `1cff14b0ab14`  |
| 2695   | No file  | `1cff14b0ab14`  |
| 2684   | No file  | `1cff14b0ab14`  |
| 2672   | No file  | `1cff14b0ab14`  |
| 2665   | No file  | `1cff14b0ab14`  |
| 2657   | No file  | `1cff14b0ab14`  |
| 2649   | No file  | `1cff14b0ab14`  |
| 2644   | No file  | `1cff14b0ab14`  |
| 2637   | No file  | `1cff14b0ab14`  |
| 2629   | No file  | `1cff14b0ab14`  |
| 2619   | No file  | `1cff14b0ab14`  |
| 2612   | No file  | `1cff14b0ab14`  |
| 2606   | No file  | `1cff14b0ab14`  |
| 2602   | No file  | `1cff14b0ab14`  |
| 2601   | No file  | `1cff14b0ab14`  |
| 2592   | No file  | `1cff14b0ab14`  |
| 2583   | No file  | `1cff14b0ab14`  |
| 2575   | No file  | `1cff14b0ab14`  |
| 2567   | No file  | `1cff14b0ab14`  |
| 2560   | No file  | `1cff14b0ab14`  |
| 2553   | No file  | `1cff14b0ab14`  |
| 2545   | No file  | `1cff14b0ab14`  |
| 2538   | No file  | `1cff14b0ab14`  |
| 2529   | No file  | `1cff14b0ab14`  |
| 2519   | No file  | `1cff14b0ab14`  |
| 2513   | No file  | `1cff14b0ab14`  |
| 2510   | No file  | `1cff14b0ab14`  |
| 2507   | No file  | `1cff14b0ab14`  |
| 2503   | No file  | `1cff14b0ab14`  |
| 2498   | No file  | `1cff14b0ab14`  |
| 2492   | No file  | `1cff14b0ab14`  |
| 2487   | No file  | `1cff14b0ab14`  |
| 2480   | No file  | `1cff14b0ab14`  |
| 2474   | No file  | `1cff14b0ab14`  |
| 2468   | No file  | `1cff14b0ab14`  |
| 2460   | No file  | `1cff14b0ab14`  |
| 2453   | No file  | `1cff14b0ab14`  |
| 2444   | No file  | `1cff14b0ab14`  |
| 2438   | No file  | `1cff14b0ab14`  |
| 2434   | No file  | `1cff14b0ab14`  |
| 2429   | No file  | `1cff14b0ab14`  |
| 2421   | No file  | `1cff14b0ab14`  |
| 2414   | No file  | `1cff14b0ab14`  |
| 2407   | No file  | `1cff14b0ab14`  |
| 2401   | No file  | `1cff14b0ab14`  |
| 2397   | No file  | `1cff14b0ab14`  |
| 2393   | No file  | `1cff14b0ab14`  |
| 2384   | No file  | `1cff14b0ab14`  |
| 2378   | No file  | `1cff14b0ab14`  |
| 2372   | No file  | `1cff14b0ab14`  |
| 2358   | No file  | `1cff14b0ab14`  |
| 2352   | No file  | `1cff14b0ab14`  |
| 2347   | No file  | `1cff14b0ab14`  |
| 2343   | No file  | `1cff14b0ab14`  |
| 2335   | No file  | `1cff14b0ab14`  |
| 2327   | No file  | `1cff14b0ab14`  |
| 2324   | No file  | `1cff14b0ab14`  |
| 2319   | No file  | `1cff14b0ab14`  |
| 2313   | No file  | `1cff14b0ab14`  |
| 2308   | No file  | `1cff14b0ab14`  |
| 2302   | No file  | `1cff14b0ab14`  |
| 2295   | No file  | `1cff14b0ab14`  |
| 2290   | No file  | `1cff14b0ab14`  |
| 2284   | No file  | `1cff14b0ab14`  |
| 2276   | No file  | `1cff14b0ab14`  |
| 2269   | No file  | `1cff14b0ab14`  |
| 2259   | No file  | `1cff14b0ab14`  |
| 2250   | No file  | `1cff14b0ab14`  |
| 2243   | No file  | `1cff14b0ab14`  |
| 2235   | No file  | `1cff14b0ab14`  |
| 2229   | No file  | `1cff14b0ab14`  |
| 2224   | No file  | `1cff14b0ab14`  |
| 2218   | No file  | `1cff14b0ab14`  |
| 2215   | No file  | `1cff14b0ab14`  |
| 2207   | No file  | `1cff14b0ab14`  |
| 2203   | No file  | `1cff14b0ab14`  |
| 2196   | No file  | `1cff14b0ab14`  |
| 2192   | No file  | `1cff14b0ab14`  |
| 2189   | No file  | `1cff14b0ab14`  |
| 2183   | No file  | `1cff14b0ab14`  |
| 2179   | No file  | `1cff14b0ab14`  |
| 2171   | No file  | `1cff14b0ab14`  |
| 2163   | No file  | `1cff14b0ab14`  |
| 2156   | No file  | `1cff14b0ab14`  |
| 2151   | No file  | `1cff14b0ab14`  |
| 2147   | No file  | `1cff14b0ab14`  |
| 2142   | No file  | `1cff14b0ab14`  |
| 2138   | No file  | `1cff14b0ab14`  |
| 2134   | No file  | `1cff14b0ab14`  |
| 2130   | No file  | `1cff14b0ab14`  |
| 2122   | No file  | `1cff14b0ab14`  |
| 2107   | No file  | `1cff14b0ab14`  |
| 2098   | No file  | `1cff14b0ab14`  |
| 2089   | No file  | `1cff14b0ab14`  |
| 2081   | No file  | `1cff14b0ab14`  |
| 2073   | No file  | `1cff14b0ab14`  |
| 2067   | No file  | `1cff14b0ab14`  |
| 2063   | No file  | `1cff14b0ab14`  |
| 2059   | No file  | `1cff14b0ab14`  |
| 2052   | No file  | `1cff14b0ab14`  |
| 2044   | No file  | `1cff14b0ab14`  |
| 2039   | No file  | `1cff14b0ab14`  |
| 2032   | No file  | `1cff14b0ab14`  |
| 2025   | No file  | `1cff14b0ab14`  |
| 2011   | No file  | `1cff14b0ab14`  |
| 2005   | No file  | `1cff14b0ab14`  |
| 2000   | No file  | `1cff14b0ab14`  |
| 1996   | No file  | `1cff14b0ab14`  |
| 1991   | No file  | `1cff14b0ab14`  |
| 1985   | No file  | `1cff14b0ab14`  |
| 1980   | No file  | `1cff14b0ab14`  |
| 1969   | No file  | `1cff14b0ab14`  |
| 1964   | No file  | `1cff14b0ab14`  |
| 1958   | No file  | `1cff14b0ab14`  |
| 1950   | No file  | `1cff14b0ab14`  |
| 1945   | No file  | `1cff14b0ab14`  |
| 1937   | No file  | `1cff14b0ab14`  |
| 1933   | No file  | `1cff14b0ab14`  |
| 1927   | No file  | `1cff14b0ab14`  |
| 1921   | No file  | `1cff14b0ab14`  |
| 1914   | No file  | `1cff14b0ab14`  |
| 1908   | No file  | `1cff14b0ab14`  |
| 1897   | No file  | `1cff14b0ab14`  |
| 1892   | No file  | `1cff14b0ab14`  |
| 1886   | No file  | `1cff14b0ab14`  |
| 1881   | No file  | `1cff14b0ab14`  |
| 1871   | No file  | `1cff14b0ab14`  |
| 1866   | No file  | `1cff14b0ab14`  |
| 1862   | No file  | `1cff14b0ab14`  |
| 1854   | No file  | `1cff14b0ab14`  |
| 1846   | No file  | `1cff14b0ab14`  |
| 1838   | No file  | `1cff14b0ab14`  |
| 1832   | No file  | `1cff14b0ab14`  |
| 1826   | No file  | `1cff14b0ab14`  |
| 1822   | No file  | `1cff14b0ab14`  |
| 1818   | No file  | `1cff14b0ab14`  |
| 1804   | No file  | `1cff14b0ab14`  |
| 1794   | No file  | `1cff14b0ab14`  |
| 1790   | No file  | `1cff14b0ab14`  |
| 1784   | No file  | `1cff14b0ab14`  |
| 1774   | No file  | `1cff14b0ab14`  |
| 1771   | No file  | `1cff14b0ab14`  |
| 1762   | No file  | `1cff14b0ab14`  |
| 1759   | No file  | `1cff14b0ab14`  |
| 1754   | No file  | `1cff14b0ab14`  |
| 1749   | No file  | `1cff14b0ab14`  |
| 1743   | No file  | `1cff14b0ab14`  |
| 1737   | No file  | `1cff14b0ab14`  |
| 1731   | No file  | `1cff14b0ab14`  |
| 1725   | No file  | `1cff14b0ab14`  |
| 1717   | No file  | `1cff14b0ab14`  |
| 1710   | No file  | `1cff14b0ab14`  |
| 1704   | No file  | `1cff14b0ab14`  |
| 1698   | No file  | `1cff14b0ab14`  |
| 1690   | No file  | `1cff14b0ab14`  |
| 1685   | No file  | `1cff14b0ab14`  |
| 1680   | No file  | `1cff14b0ab14`  |
| 1674   | No file  | `1cff14b0ab14`  |
| 1668   | No file  | `1cff14b0ab14`  |
| 1659   | No file  | `1cff14b0ab14`  |
| 1649   | No file  | `1cff14b0ab14`  |
| 1642   | No file  | `1cff14b0ab14`  |
| 1636   | No file  | `1cff14b0ab14`  |
| 1628   | No file  | `1cff14b0ab14`  |
| 1622   | No file  | `1cff14b0ab14`  |
| 1614   | No file  | `1cff14b0ab14`  |
| 1608   | No file  | `1cff14b0ab14`  |
| 1602   | No file  | `1cff14b0ab14`  |
| 1598   | No file  | `1cff14b0ab14`  |
| 1594   | No file  | `1cff14b0ab14`  |
| 1590   | No file  | `1cff14b0ab14`  |
| 1587   | No file  | `1cff14b0ab14`  |
| 1584   | No file  | `1cff14b0ab14`  |
| 1579   | No file  | `1cff14b0ab14`  |
| 1572   | No file  | `1cff14b0ab14`  |
| 1565   | No file  | `1cff14b0ab14`  |
| 1559   | No file  | `1cff14b0ab14`  |
| 1554   | No file  | `1cff14b0ab14`  |
| 1547   | No file  | `1cff14b0ab14`  |
| 1537   | No file  | `1cff14b0ab14`  |
| 1529   | No file  | `1cff14b0ab14`  |
| 1524   | No file  | `1cff14b0ab14`  |
| 1519   | No file  | `1cff14b0ab14`  |
| 1509   | No file  | `1cff14b0ab14`  |
| 1506   | No file  | `1cff14b0ab14`  |
| 1504   | No file  | `1cff14b0ab14`  |
| 1500   | No file  | `1cff14b0ab14`  |
| 1493   | No file  | `1cff14b0ab14`  |
| 1489   | No file  | `1cff14b0ab14`  |
| 1485   | No file  | `1cff14b0ab14`  |
| 1481   | No file  | `1cff14b0ab14`  |
| 1474   | No file  | `1cff14b0ab14`  |
| 1466   | No file  | `1cff14b0ab14`  |
| 1462   | No file  | `1cff14b0ab14`  |
| 1459   | No file  | `1cff14b0ab14`  |
| 1453   | No file  | `1cff14b0ab14`  |
| 1450   | No file  | `1cff14b0ab14`  |
| 1445   | No file  | `1cff14b0ab14`  |
| 1439   | No file  | `1cff14b0ab14`  |
| 1433   | No file  | `1cff14b0ab14`  |
| 1430   | No file  | `1cff14b0ab14`  |
| 1426   | No file  | `1cff14b0ab14`  |
| 1421   | No file  | `1cff14b0ab14`  |
| 1417   | No file  | `1cff14b0ab14`  |
| 1416   | No file  | `1cff14b0ab14`  |
| 1409   | No file  | `1cff14b0ab14`  |
| 1405   | No file  | `1cff14b0ab14`  |
| 1401   | No file  | `1cff14b0ab14`  |
| 1396   | No file  | `1cff14b0ab14`  |
| 1391   | No file  | `1cff14b0ab14`  |
| 1390   | No file  | `1cff14b0ab14`  |
| 1386   | No file  | `1cff14b0ab14`  |
| 1381   | No file  | `1cff14b0ab14`  |
| 1379   | No file  | `1cff14b0ab14`  |
| 1372   | No file  | `1cff14b0ab14`  |
| 1366   | No file  | `1cff14b0ab14`  |
| 1364   | No file  | `1cff14b0ab14`  |
| 1363   | No file  | `1cff14b0ab14`  |
| 1360   | No file  | `1cff14b0ab14`  |
| 1358   | No file  | `1cff14b0ab14`  |
| 1355   | No file  | `1cff14b0ab14`  |
| 1351   | No file  | `1cff14b0ab14`  |
| 1348   | No file  | `1cff14b0ab14`  |
| 1346   | No file  | `1cff14b0ab14`  |
| 1341   | No file  | `1cff14b0ab14`  |
| 1340   | No file  | `1cff14b0ab14`  |
| 1338   | No file  | `1cff14b0ab14`  |
| 1335   | No file  | `1cff14b0ab14`  |
| 1333   | No file  | `1cff14b0ab14`  |
| 1329   | No file  | `1cff14b0ab14`  |
| 1327   | No file  | `1cff14b0ab14`  |
| 1324   | No file  | `1cff14b0ab14`  |
| 1321   | No file  | `1cff14b0ab14`  |
| 1319   | No file  | `1cff14b0ab14`  |
| 1318   | No file  | `1cff14b0ab14`  |
| 1316   | No file  | `1cff14b0ab14`  |
| 1313   | No file  | `1cff14b0ab14`  |
| 1311   | No file  | `1cff14b0ab14`  |
| 1309   | No file  | `1cff14b0ab14`  |
| 1304   | No file  | `1cff14b0ab14`  |
| 1292   | No file  | `1cff14b0ab14`  |
| 1286   | No file  | `1cff14b0ab14`  |
| 1280   | No file  | `1cff14b0ab14`  |
| 1276   | No file  | `1cff14b0ab14`  |
| 1267   | No file  | `1cff14b0ab14`  |
| 1261   | No file  | `1cff14b0ab14`  |
| 1256   | No file  | `1cff14b0ab14`  |
| 1250   | No file  | `1cff14b0ab14`  |
| 1246   | No file  | `1cff14b0ab14`  |
| 1239   | No file  | `1cff14b0ab14`  |
| 1230   | No file  | `1cff14b0ab14`  |
| 1226   | No file  | `1cff14b0ab14`  |
| 1220   | No file  | `1cff14b0ab14`  |
| 1217   | No file  | `1cff14b0ab14`  |
| 1211   | No file  | `1cff14b0ab14`  |
| 1210   | No file  | `1cff14b0ab14`  |
| 1208   | No file  | `1cff14b0ab14`  |
| 1203   | No file  | `1cff14b0ab14`  |
| 1197   | No file  | `1cff14b0ab14`  |
| 1194   | No file  | `1cff14b0ab14`  |
| 1192   | No file  | `1cff14b0ab14`  |
| 1187   | No file  | `1cff14b0ab14`  |
| 1183   | No file  | `1cff14b0ab14`  |
| 1177   | No file  | `1cff14b0ab14`  |
| 1173   | No file  | `1cff14b0ab14`  |
| 1167   | No file  | `1cff14b0ab14`  |
| 1164   | No file  | `1cff14b0ab14`  |
| 1156   | No file  | `1cff14b0ab14`  |
| 1149   | No file  | `1cff14b0ab14`  |
| 1144   | No file  | `1cff14b0ab14`  |
| 1137   | No file  | `1cff14b0ab14`  |
| 1132   | No file  | `1cff14b0ab14`  |
| 1127   | No file  | `1cff14b0ab14`  |
| 1122   | No file  | `1cff14b0ab14`  |
| 1118   | No file  | `1cff14b0ab14`  |
| 1114   | No file  | `1cff14b0ab14`  |
| 1109   | No file  | `1cff14b0ab14`  |
| 1102   | No file  | `1cff14b0ab14`  |
| 1096   | No file  | `1cff14b0ab14`  |
| 1088   | No file  | `1cff14b0ab14`  |
| 1081   | No file  | `1cff14b0ab14`  |
| 1076   | No file  | `1cff14b0ab14`  |
| 1069   | No file  | `1cff14b0ab14`  |
| 1064   | No file  | `1cff14b0ab14`  |
| 1058   | No file  | `1cff14b0ab14`  |
| 1051   | No file  | `1cff14b0ab14`  |
| 1044   | No file  | `1cff14b0ab14`  |
| 1036   | No file  | `1cff14b0ab14`  |
| 1026   | No file  | `1cff14b0ab14`  |
| 1016   | No file  | `1cff14b0ab14`  |
| 1009   | No file  | `1cff14b0ab14`  |
| 1005   | No file  | `1cff14b0ab14`  |
| 1000   | No file  | `1cff14b0ab14`  |
| 998    | No file  | `1cff14b0ab14`  |
| 990    | No file  | `1cff14b0ab14`  |
| 979    | No file  | `1cff14b0ab14`  |
| 972    | No file  | `1cff14b0ab14`  |
| 963    | No file  | `1cff14b0ab14`  |
| 955    | No file  | `1cff14b0ab14`  |
| 946    | No file  | `1cff14b0ab14`  |
| 938    | No file  | `1cff14b0ab14`  |
| 927    | No file  | `1cff14b0ab14`  |
| 911    | No file  | `1cff14b0ab14`  |
| 904    | No file  | `1cff14b0ab14`  |
| 899    | No file  | `1cff14b0ab14`  |
| 894    | No file  | `1cff14b0ab14`  |
| 885    | No file  | `1cff14b0ab14`  |
| 879    | No file  | `1cff14b0ab14`  |
| 872    | No file  | `1cff14b0ab14`  |
| 864    | No file  | `1cff14b0ab14`  |
| 855    | No file  | `1cff14b0ab14`  |
| 853    | No file  | `1cff14b0ab14`  |
| 845    | No file  | `1cff14b0ab14`  |
| 837    | No file  | `1cff14b0ab14`  |
| 829    | No file  | `1cff14b0ab14`  |
| 822    | No file  | `1cff14b0ab14`  |
| 814    | No file  | `1cff14b0ab14`  |
| 805    | No file  | `1cff14b0ab14`  |
| 794    | No file  | `1cff14b0ab14`  |
| 787    | No file  | `1cff14b0ab14`  |
| 780    | No file  | `1cff14b0ab14`  |
| 771    | No file  | `1cff14b0ab14`  |
| 760    | No file  | `1cff14b0ab14`  |
| 748    | No file  | `1cff14b0ab14`  |
| 741    | No file  | `1cff14b0ab14`  |
| 736    | No file  | `1cff14b0ab14`  |
| 731    | No file  | `1cff14b0ab14`  |
| 723    | No file  | `1cff14b0ab14`  |
| 711    | No file  | `1cff14b0ab14`  |
| 707    | No file  | `1cff14b0ab14`  |
| 697    | No file  | `1cff14b0ab14`  |
| 689    | No file  | `1cff14b0ab14`  |
| 683    | No file  | `1cff14b0ab14`  |
| 678    | No file  | `1cff14b0ab14`  |
| 670    | No file  | `1cff14b0ab14`  |
| 661    | No file  | `1cff14b0ab14`  |
| 656    | No file  | `1cff14b0ab14`  |
| 652    | No file  | `1cff14b0ab14`  |
| 643    | No file  | `1cff14b0ab14`  |
| 637    | No file  | `1cff14b0ab14`  |
| 630    | No file  | `1cff14b0ab14`  |
| 627    | No file  | `1cff14b0ab14`  |
| 621    | No file  | `1cff14b0ab14`  |
| 617    | No file  | `1cff14b0ab14`  |
| 615    | No file  | `1cff14b0ab14`  |
| 606    | No file  | `1cff14b0ab14`  |
| 599    | No file  | `1cff14b0ab14`  |
| 592    | No file  | `1cff14b0ab14`  |
| 586    | No file  | `1cff14b0ab14`  |
| 577    | No file  | `1cff14b0ab14`  |
| 569    | No file  | `1cff14b0ab14`  |
| 561    | No file  | `1cff14b0ab14`  |
| 554    | No file  | `1cff14b0ab14`  |
| 542    | No file  | `1cff14b0ab14`  |
| 532    | No file  | `1cff14b0ab14`  |
| 531    | No file  | `1cff14b0ab14`  |
| 526    | No file  | `1cff14b0ab14`  |
| 521    | No file  | `1cff14b0ab14`  |
| 517    | No file  | `1cff14b0ab14`  |
| 510    | No file  | `1cff14b0ab14`  |
| 508    | No file  | `1cff14b0ab14`  |
| 504    | No file  | `1cff14b0ab14`  |
| 497    | No file  | `1cff14b0ab14`  |
| 491    | No file  | `1cff14b0ab14`  |
| 485    | No file  | `1cff14b0ab14`  |
| 478    | No file  | `1cff14b0ab14`  |
| 472    | No file  | `1cff14b0ab14`  |
| 466    | No file  | `1cff14b0ab14`  |
| 457    | No file  | `1cff14b0ab14`  |
| 452    | No file  | `1cff14b0ab14`  |
| 449    | No file  | `1cff14b0ab14`  |
| 435    | No file  | `1cff14b0ab14`  |

<!-- versions:end -->

## Companion Files

None. The handler names each quest with its LOC type 18 title from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                | Field        | Notes                                                       |
| ------------------- | ------------------- | ------------ | ----------------------------------------------------------- |
| `+0x00`             | char[4]             | magic        | ASCII `PABR`                                                |
| `+0x04`             | Pass[..table_start] | passes       | One per pass type, `__eOlviaAcademyPassType_Collect` first; see Pass Types |
| `passes+0x00`       | String Table        | string_table | See String Table                                            |
| `EOF-0x08`          | u32                 | table_start  | Offset of the string table, where `passes` ends             |
| `EOF-0x04`          | u32                 | zero         | Always `0`                                                  |

### Pass (variable: 4 bytes + steps)

| Offset  | Type             | Field     | Notes                                                       |
| ------- | ---------------- | --------- | ----------------------------------------------------------- |
| `+0x00` | u32              | pass_size | `ToClient_GetOlviaAcademyPassSize(passType)`; `10` on every pass (client 3482) |
| `+0x04` | Step[pass_size]  | steps     | `questIndex` from `0`                                       |

### Step (8 bytes)

| Offset  | Type | Field      | Notes                                                               |
| ------- | ---- | ---------- | ------------------------------------------------------------------- |
| `+0x00` | u32  | base_quest | `ToClient_GetOlviaAcademyQuest(passType, questIndex, __eOlviaAcademyPassQuestType_Base)`; packed quest ID |
| `+0x04` | u32  | pass_quest | The same with `__eOlviaAcademyPassQuestType_Pass`; packed quest ID  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3482     |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                   |

## Pass Types

`panel_window_olviaacademy_pass_all_1.luac` walks the passes with
`for passType = __eOlviaAcademyPassType_Collect, __eOlviaAcademyPassType_Count - 1`,
and `panel_window_olviaacademy_pass_all.luac` lists the nine values in this
order. On client 3482 every step of pass `n` (from `0`) is chain 2324 with
`base_quest` at sub ID `(n + 1) * 100 + 2 * questIndex + 1` and
`pass_quest` at the next sub ID, so the file order is the value order:

| Pass | Pass type (Lua)                    | Base quests (sub IDs)  | Title          |
| ---- | ---------------------------------- | ---------------------- | -------------- |
| 0    | `__eOlviaAcademyPassType_Collect`  | 101, 103, ... 119      | Gathering Time! `n`. |
| 1    | `__eOlviaAcademyPassType_Fish`     | 201, 203, ... 219      | Hands-On Fishing! `n`. |
| 2    | `__eOlviaAcademyPassType_Hunt`     | 301, 303, ... 319      | Happy Hunting! `n`. |
| 3    | `__eOlviaAcademyPassType_Cook`     | 401, 403, ... 419      | Win Them Over with Cooking! `n`. |
| 4    | `__eOlviaAcademyPassType_Alchemy`  | 501, 503, ... 519      | Hands-On Alchemy! `n`. |
| 5    | `__eOlviaAcademyPassType_Work`     | 601, 603, ... 619      | Processing in Progress! `n`. |
| 6    | `__eOlviaAcademyPassType_Train`    | 701, 703, ... 719      | Hands-On Training! `n`. |
| 7    | `__eOlviaAcademyPassType_Farm`     | 801, 803, ... 819      | Fantastic Farming! `n`. |
| 8    | `__eOlviaAcademyPassType_Ship`     | 901, 903, ... 919      | Hands-On Sailing! `n`. |

## Field Names

No reference source has the file: it first appears on client 3186
(absent on client 3177), and a private server's `DataSheets.bexcel` on
client 1784 has no sheet with `Olvia` or `Academy` in its name. The
names come from the client Lua of client 3482:
`panel_window_olviaacademy_pass_all_1.luac` reads `passSize` from
`ToClient_GetOlviaAcademyPassSize(passType)` and asks for each step with
`ToClient_GetOlviaAcademyQuest(passType, questIndex, __eOlviaAcademyPassQuestType_Base)`
and `..._Pass`. The base quest of every step is the quest whose title the
tab shows, the pass quest is that title with `(Olvia Academy Pass)`, whose
reward stays locked while `ToClient_HasOlviaAcademyPass(passType)` is false.

## Notes

- Decompressed size on client 3482: `772` bytes, 9 passes of 10 steps.
- The 180 quests of the 90 steps are exactly the quests of
  `olviaacademypassquestlist.bss` (client 3482), whose file order is not
  the step order.
- On every step `pass_quest` is `base_quest` plus `1 << 16`: the same chain,
  the next sub ID.
- The handler shows one row per step with its pass type, `questIndex + 1`
  as the step number and both quests with their titles; each quest links to
  its row in `olviaacademypassquestlist.bss`, and the pass quest list view
  links each quest back to its step.

## Open Questions

### A Pass With No Steps

The passes have no key: the reading takes the pass type from the position
in the file. Whether a pass type with no steps keeps a block with a
`pass_size` of `0`, so that every later pass keeps its position, is open;
every pass on client 3482 has 10 steps.
