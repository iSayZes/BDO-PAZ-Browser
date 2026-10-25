# `displayexchangeitemnpc.dbss` Format

## Purpose

The item exchanges an NPC dialog lists in its exchange window: each row
names an NPC and one of its dialogs, and lists the `itemexchangebynpc.dbss`
keys (need item and count, result item and count) the window shows.
`displayexchangeitemnpcoffset.dbss` is the index into it, keyed by
`dialog_index << 16 | npc_character_key`, the same key
[`detail_dialog.dbss`](detail_dialog_dbss.md) uses for the dialog.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                | Bytes | Records        | Row bytes               |
| ------ | -------------- | ----------------------------------- | ----- | -------------- | ----------------------- |
| 1      | 1346 and later | `displayexchangeitemnpc.dbss`       | 2,944 | 124 Row        | 18 to 60, 24 on average |
| 1      | 1346 and later | `displayexchangeitemnpcoffset.dbss` | 1,492 | 124 Offset Row | 12                      |

| Layout | File                                | Known            | Unknown    |
| ------ | ----------------------------------- | ---------------- | ---------- |
| 1      | `displayexchangeitemnpc.dbss`       | 2,944 B (100.0%) | 0 B (0.0%) |
| 1      | `displayexchangeitemnpcoffset.dbss` | 1,492 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `f044f8f71342`  |
| 3482   | Layout 1             | `f044f8f71342`  |
| 3474   | Layout 1             | `f044f8f71342`  |
| 3473   | Layout 1             | `f044f8f71342`  |
| 3464   | Layout 1             | `f044f8f71342`  |
| 3458   | Layout 1             | `f044f8f71342`  |
| 3454   | Layout 1             | `f044f8f71342`  |
| 3444   | Layout 1             | `f044f8f71342`  |
| 3435   | Layout 1             | `f044f8f71342`  |
| 3426   | Layout 1             | `f044f8f71342`  |
| 3418   | Layout 1             | `f044f8f71342`  |
| 3412   | Layout 1             | `f044f8f71342`  |
| 3402   | Layout 1             | `f044f8f71342`  |
| 3396   | Layout 1             | `f044f8f71342`  |
| 3387   | Layout 1             | `f044f8f71342`  |
| 3381   | Layout 1             | `f044f8f71342`  |
| 3373   | Layout 1             | `f044f8f71342`  |
| 3364   | Layout 1             | `f044f8f71342`  |
| 3356   | Layout 1             | `f044f8f71342`  |
| 3349   | Layout 1             | `f044f8f71342`  |
| 3342   | Layout 1             | `f044f8f71342`  |
| 3335   | Layout 1             | `f044f8f71342`  |
| 3326   | Layout 1             | `f044f8f71342`  |
| 3321   | Layout 1             | `f044f8f71342`  |
| 3314   | Layout 1             | `f044f8f71342`  |
| 3303   | Layout 1             | `f044f8f71342`  |
| 3302   | Layout 1             | `f044f8f71342`  |
| 3293   | Layout 1             | `f044f8f71342`  |
| 3283   | Layout 1             | `f044f8f71342`  |
| 3275   | Layout 1             | `f044f8f71342`  |
| 3267   | Layout 1             | `f044f8f71342`  |
| 3258   | Layout 1             | `f044f8f71342`  |
| 3251   | Layout 1             | `f044f8f71342`  |
| 3242   | Layout 1             | `f044f8f71342`  |
| 3235   | Layout 1             | `f044f8f71342`  |
| 3229   | Layout 1             | `f044f8f71342`  |
| 3212   | Layout 1             | `f044f8f71342`  |
| 3203   | Layout 1             | `f044f8f71342`  |
| 3193   | Layout 1             | `f044f8f71342`  |
| 3186   | Layout 1             | `f044f8f71342`  |
| 3177   | Layout 1             | `f044f8f71342`  |
| 3169   | Layout 1             | `f044f8f71342`  |
| 3158   | Layout 1             | `f044f8f71342`  |
| 3151   | Layout 1             | `f044f8f71342`  |
| 3144   | Layout 1             | `f044f8f71342`  |
| 3133   | Layout 1             | `f044f8f71342`  |
| 3125   | Layout 1             | `f044f8f71342`  |
| 3118   | Layout 1             | `f044f8f71342`  |
| 3111   | Layout 1             | `f044f8f71342`  |
| 3103   | Layout 1             | `f044f8f71342`  |
| 3095   | Layout 1             | `f044f8f71342`  |
| 3086   | Layout 1             | `f044f8f71342`  |
| 3072   | Layout 1             | `f044f8f71342`  |
| 3062   | Layout 1             | `f044f8f71342`  |
| 3052   | Layout 1             | `f044f8f71342`  |
| 3045   | Layout 1             | `f044f8f71342`  |
| 3037   | Layout 1             | `f044f8f71342`  |
| 3030   | Layout 1             | `f044f8f71342`  |
| 3021   | Layout 1             | `f044f8f71342`  |
| 3012   | Layout 1             | `f044f8f71342`  |
| 3002   | Layout 1             | `f044f8f71342`  |
| 2995   | Layout 1             | `f044f8f71342`  |
| 2987   | Layout 1             | `f044f8f71342`  |
| 2978   | Layout 1             | `f044f8f71342`  |
| 2970   | Layout 1             | `f044f8f71342`  |
| 2959   | Layout 1             | `f044f8f71342`  |
| 2951   | Layout 1             | `f044f8f71342`  |
| 2942   | Layout 1             | `f044f8f71342`  |
| 2935   | Layout 1             | `f044f8f71342`  |
| 2932   | Layout 1             | `f044f8f71342`  |
| 2923   | Layout 1             | `f044f8f71342`  |
| 2919   | Layout 1             | `f044f8f71342`  |
| 2907   | Layout 1             | `f044f8f71342`  |
| 2900   | Layout 1             | `f044f8f71342`  |
| 2891   | Layout 1             | `f044f8f71342`  |
| 2882   | Layout 1             | `f044f8f71342`  |
| 2872   | Layout 1             | `f044f8f71342`  |
| 2863   | Layout 1             | `f044f8f71342`  |
| 2855   | Layout 1             | `f044f8f71342`  |
| 2849   | Layout 1             | `f044f8f71342`  |
| 2844   | Layout 1             | `f044f8f71342`  |
| 2834   | Layout 1             | `f044f8f71342`  |
| 2825   | Layout 1             | `f044f8f71342`  |
| 2819   | Layout 1             | `f044f8f71342`  |
| 2811   | Layout 1             | `f044f8f71342`  |
| 2803   | Layout 1             | `f044f8f71342`  |
| 2794   | Layout 1             | `f044f8f71342`  |
| 2783   | Layout 1             | `f044f8f71342`  |
| 2774   | Layout 1             | `f044f8f71342`  |
| 2765   | Layout 1             | `f044f8f71342`  |
| 2756   | Layout 1             | `f044f8f71342`  |
| 2750   | Layout 1             | `f044f8f71342`  |
| 2743   | Layout 1             | `f044f8f71342`  |
| 2736   | Layout 1             | `f044f8f71342`  |
| 2726   | Layout 1             | `f044f8f71342`  |
| 2717   | Layout 1             | `f044f8f71342`  |
| 2709   | Layout 1             | `f044f8f71342`  |
| 2703   | Layout 1             | `f044f8f71342`  |
| 2695   | Layout 1             | `f044f8f71342`  |
| 2684   | Layout 1             | `f044f8f71342`  |
| 2672   | Layout 1             | `f044f8f71342`  |
| 2665   | Layout 1             | `f044f8f71342`  |
| 2657   | Layout 1             | `f044f8f71342`  |
| 2649   | Layout 1             | `f044f8f71342`  |
| 2644   | Layout 1             | `f044f8f71342`  |
| 2637   | Layout 1             | `f044f8f71342`  |
| 2629   | Layout 1             | `f044f8f71342`  |
| 2619   | Layout 1             | `f044f8f71342`  |
| 2612   | Layout 1             | `f044f8f71342`  |
| 2606   | Layout 1             | `f044f8f71342`  |
| 2602   | Layout 1             | `f044f8f71342`  |
| 2601   | Layout 1             | `f044f8f71342`  |
| 2592   | Layout 1             | `f044f8f71342`  |
| 2583   | Layout 1             | `f044f8f71342`  |
| 2575   | Layout 1             | `f044f8f71342`  |
| 2567   | Layout 1             | `f044f8f71342`  |
| 2560   | Layout 1             | `f044f8f71342`  |
| 2553   | Layout 1             | `f044f8f71342`  |
| 2545   | Layout 1             | `f044f8f71342`  |
| 2538   | Layout 1             | `f044f8f71342`  |
| 2529   | Layout 1             | `f044f8f71342`  |
| 2519   | Layout 1             | `f044f8f71342`  |
| 2513   | Layout 1             | `f044f8f71342`  |
| 2510   | Layout 1             | `f044f8f71342`  |
| 2507   | Layout 1             | `f044f8f71342`  |
| 2503   | Layout 1             | `f044f8f71342`  |
| 2498   | Layout 1             | `f044f8f71342`  |
| 2492   | Layout 1             | `f044f8f71342`  |
| 2487   | Layout 1             | `f044f8f71342`  |
| 2480   | Layout 1             | `f044f8f71342`  |
| 2474   | Layout 1             | `f044f8f71342`  |
| 2468   | Layout 1             | `f044f8f71342`  |
| 2460   | Layout 1             | `f044f8f71342`  |
| 2453   | Layout 1             | `f044f8f71342`  |
| 2444   | Layout 1             | `f044f8f71342`  |
| 2438   | Layout 1             | `f044f8f71342`  |
| 2434   | Layout 1             | `f044f8f71342`  |
| 2429   | Layout 1             | `f044f8f71342`  |
| 2421   | Layout 1             | `f044f8f71342`  |
| 2414   | Layout 1             | `f044f8f71342`  |
| 2407   | Layout 1             | `f044f8f71342`  |
| 2401   | Layout 1             | `f044f8f71342`  |
| 2397   | Layout 1             | `f044f8f71342`  |
| 2393   | Layout 1             | `f044f8f71342`  |
| 2384   | Layout 1             | `f044f8f71342`  |
| 2378   | Layout 1             | `f044f8f71342`  |
| 2372   | Layout 1             | `f044f8f71342`  |
| 2358   | Layout 1             | `f044f8f71342`  |
| 2352   | Layout 1             | `f044f8f71342`  |
| 2347   | Layout 1             | `f044f8f71342`  |
| 2343   | Layout 1             | `f044f8f71342`  |
| 2335   | Layout 1             | `f044f8f71342`  |
| 2327   | Layout 1             | `f044f8f71342`  |
| 2324   | Layout 1             | `f044f8f71342`  |
| 2319   | Layout 1             | `f044f8f71342`  |
| 2313   | Layout 1             | `f044f8f71342`  |
| 2308   | Layout 1             | `f044f8f71342`  |
| 2302   | Layout 1             | `f044f8f71342`  |
| 2295   | Layout 1             | `f044f8f71342`  |
| 2290   | Layout 1             | `f044f8f71342`  |
| 2284   | Layout 1             | `f044f8f71342`  |
| 2276   | Layout 1             | `f044f8f71342`  |
| 2269   | Layout 1             | `f044f8f71342`  |
| 2259   | Layout 1             | `f044f8f71342`  |
| 2250   | Layout 1             | `f044f8f71342`  |
| 2243   | Layout 1             | `f044f8f71342`  |
| 2235   | Layout 1             | `f044f8f71342`  |
| 2229   | Layout 1             | `f044f8f71342`  |
| 2224   | Layout 1             | `f044f8f71342`  |
| 2218   | Layout 1             | `f044f8f71342`  |
| 2215   | Layout 1             | `f044f8f71342`  |
| 2207   | Layout 1             | `f044f8f71342`  |
| 2203   | Layout 1             | `f044f8f71342`  |
| 2196   | Layout 1             | `f044f8f71342`  |
| 2192   | Layout 1             | `f044f8f71342`  |
| 2189   | Layout 1             | `f044f8f71342`  |
| 2183   | Layout 1             | `f044f8f71342`  |
| 2179   | Layout 1             | `f044f8f71342`  |
| 2171   | Layout 1             | `f044f8f71342`  |
| 2163   | Layout 1             | `f044f8f71342`  |
| 2156   | Layout 1             | `f044f8f71342`  |
| 2151   | Layout 1             | `f044f8f71342`  |
| 2147   | Layout 1             | `f044f8f71342`  |
| 2142   | Layout 1             | `f044f8f71342`  |
| 2138   | Layout 1             | `f044f8f71342`  |
| 2134   | Layout 1             | `f044f8f71342`  |
| 2130   | Layout 1             | `f044f8f71342`  |
| 2122   | Layout 1             | `f044f8f71342`  |
| 2107   | Layout 1             | `f044f8f71342`  |
| 2098   | Layout 1             | `f044f8f71342`  |
| 2089   | Layout 1             | `f044f8f71342`  |
| 2081   | Layout 1             | `f044f8f71342`  |
| 2073   | Layout 1             | `f044f8f71342`  |
| 2067   | Layout 1             | `f044f8f71342`  |
| 2063   | Layout 1             | `f044f8f71342`  |
| 2059   | Layout 1             | `f044f8f71342`  |
| 2052   | Layout 1             | `f044f8f71342`  |
| 2044   | Layout 1             | `f044f8f71342`  |
| 2039   | Layout 1             | `f044f8f71342`  |
| 2032   | Layout 1             | `f044f8f71342`  |
| 2025   | Layout 1             | `f044f8f71342`  |
| 2011   | Layout 1             | `f044f8f71342`  |
| 2005   | Layout 1             | `f044f8f71342`  |
| 2000   | Layout 1             | `f044f8f71342`  |
| 1996   | Layout 1             | `f044f8f71342`  |
| 1991   | Layout 1             | `f044f8f71342`  |
| 1985   | Layout 1             | `f044f8f71342`  |
| 1980   | Layout 1             | `f044f8f71342`  |
| 1969   | Layout 1             | `f044f8f71342`  |
| 1964   | Layout 1             | `f044f8f71342`  |
| 1958   | Layout 1             | `f044f8f71342`  |
| 1950   | Layout 1             | `f044f8f71342`  |
| 1945   | Layout 1             | `f044f8f71342`  |
| 1937   | Layout 1             | `f044f8f71342`  |
| 1933   | Layout 1             | `f044f8f71342`  |
| 1927   | Layout 1             | `f044f8f71342`  |
| 1921   | Layout 1             | `f044f8f71342`  |
| 1914   | Layout 1             | `f044f8f71342`  |
| 1908   | Layout 1             | `f044f8f71342`  |
| 1897   | Layout 1             | `f044f8f71342`  |
| 1892   | Layout 1             | `f044f8f71342`  |
| 1886   | Layout 1             | `f044f8f71342`  |
| 1881   | Layout 1             | `f044f8f71342`  |
| 1871   | Layout 1             | `f044f8f71342`  |
| 1866   | Layout 1             | `f044f8f71342`  |
| 1862   | Layout 1             | `f044f8f71342`  |
| 1854   | Layout 1             | `f044f8f71342`  |
| 1846   | Layout 1             | `f044f8f71342`  |
| 1838   | Layout 1             | `f044f8f71342`  |
| 1832   | Layout 1             | `f044f8f71342`  |
| 1826   | Layout 1             | `f044f8f71342`  |
| 1822   | Layout 1             | `f044f8f71342`  |
| 1818   | Layout 1             | `f044f8f71342`  |
| 1804   | Layout 1             | `f044f8f71342`  |
| 1794   | Layout 1             | `f044f8f71342`  |
| 1790   | Layout 1             | `f044f8f71342`  |
| 1784   | Layout 1             | `f044f8f71342`  |
| 1774   | Layout 1             | `f044f8f71342`  |
| 1771   | Layout 1             | `f044f8f71342`  |
| 1762   | Layout 1             | `f044f8f71342`  |
| 1759   | Layout 1             | `f044f8f71342`  |
| 1754   | Layout 1             | `f044f8f71342`  |
| 1749   | Layout 1             | `f044f8f71342`  |
| 1743   | Layout 1             | `f044f8f71342`  |
| 1737   | Layout 1             | `f044f8f71342`  |
| 1731   | Layout 1             | `f044f8f71342`  |
| 1725   | Layout 1             | `f044f8f71342`  |
| 1717   | Layout 1             | `f044f8f71342`  |
| 1710   | Layout 1             | `f044f8f71342`  |
| 1704   | Layout 1             | `f044f8f71342`  |
| 1698   | Layout 1             | `f044f8f71342`  |
| 1690   | Layout 1             | `f044f8f71342`  |
| 1685   | Layout 1             | `f044f8f71342`  |
| 1680   | Layout 1             | `f044f8f71342`  |
| 1674   | Layout 1             | `f044f8f71342`  |
| 1668   | Layout 1             | `f044f8f71342`  |
| 1659   | Layout 1             | `f044f8f71342`  |
| 1649   | Layout 1             | `f044f8f71342`  |
| 1642   | Layout 1             | `f044f8f71342`  |
| 1636   | Layout 1             | `f044f8f71342`  |
| 1628   | Layout 1             | `f044f8f71342`  |
| 1622   | Layout 1             | `f044f8f71342`  |
| 1614   | Layout 1             | `f044f8f71342`  |
| 1608   | Layout 1             | `f044f8f71342`  |
| 1602   | Layout 1             | `f044f8f71342`  |
| 1598   | Layout 1             | `f044f8f71342`  |
| 1594   | Layout 1             | `f044f8f71342`  |
| 1590   | Layout 1             | `f044f8f71342`  |
| 1587   | Layout 1             | `f044f8f71342`  |
| 1584   | Layout 1             | `f044f8f71342`  |
| 1579   | Layout 1             | `f044f8f71342`  |
| 1572   | Layout 1             | `f044f8f71342`  |
| 1565   | Layout 1             | `f044f8f71342`  |
| 1559   | Layout 1             | `f044f8f71342`  |
| 1554   | Layout 1             | `f044f8f71342`  |
| 1547   | Layout 1             | `f044f8f71342`  |
| 1537   | Layout 1             | `f044f8f71342`  |
| 1529   | Layout 1             | `f044f8f71342`  |
| 1524   | Layout 1             | `f044f8f71342`  |
| 1519   | Layout 1             | `f044f8f71342`  |
| 1509   | Layout 1             | `f044f8f71342`  |
| 1506   | Layout 1             | `f044f8f71342`  |
| 1504   | Layout 1             | `f044f8f71342`  |
| 1500   | Layout 1             | `f044f8f71342`  |
| 1493   | Layout 1             | `f044f8f71342`  |
| 1489   | Layout 1             | `f044f8f71342`  |
| 1485   | Layout 1             | `f044f8f71342`  |
| 1481   | Layout 1             | `f044f8f71342`  |
| 1474   | Layout 1             | `f044f8f71342`  |
| 1466   | Layout 1             | `f044f8f71342`  |
| 1462   | Layout 1             | `f044f8f71342`  |
| 1459   | Layout 1             | `f044f8f71342`  |
| 1453   | Layout 1             | `f044f8f71342`  |
| 1450   | Layout 1             | `f044f8f71342`  |
| 1445   | Layout 1             | `f044f8f71342`  |
| 1439   | Layout 1             | `f044f8f71342`  |
| 1433   | Layout 1             | `f044f8f71342`  |
| 1430   | Layout 1             | `f044f8f71342`  |
| 1426   | Layout 1             | `f044f8f71342`  |
| 1421   | Layout 1             | `f044f8f71342`  |
| 1417   | Layout 1             | `f044f8f71342`  |
| 1416   | Layout 1             | `f044f8f71342`  |
| 1409   | Layout 1             | `f044f8f71342`  |
| 1405   | Layout 1             | `f044f8f71342`  |
| 1401   | Layout 1             | `f044f8f71342`  |
| 1396   | Layout 1             | `f044f8f71342`  |
| 1391   | Layout 1             | `f044f8f71342`  |
| 1390   | Layout 1             | `f044f8f71342`  |
| 1386   | Layout 1             | `f044f8f71342`  |
| 1381   | Layout 1             | `f044f8f71342`  |
| 1379   | Layout 1             | `f044f8f71342`  |
| 1372   | Layout 1             | `f044f8f71342`  |
| 1366   | Layout 1             | `f044f8f71342`  |
| 1364   | Layout 1             | `f044f8f71342`  |
| 1363   | Layout 1             | `f044f8f71342`  |
| 1360   | Layout 1             | `f044f8f71342`  |
| 1358   | Layout 1             | `f044f8f71342`  |
| 1355   | Layout 1             | `f044f8f71342`  |
| 1351   | Layout 1             | `f044f8f71342`  |
| 1348   | Layout 1             | `f044f8f71342`  |
| 1346   | Layout 1             | `f044f8f71342`  |
| 1341   | No documented layout | `f044f8f71342`  |
| 1340   | No documented layout | `f044f8f71342`  |
| 1338   | No documented layout | `f044f8f71342`  |
| 1335   | No documented layout | `f044f8f71342`  |
| 1333   | No documented layout | `f044f8f71342`  |
| 1329   | No documented layout | `f044f8f71342`  |
| 1327   | No documented layout | `f044f8f71342`  |
| 1324   | No documented layout | `f044f8f71342`  |
| 1321   | No documented layout | `f044f8f71342`  |
| 1319   | No documented layout | `f044f8f71342`  |
| 1318   | No documented layout | `f044f8f71342`  |
| 1316   | No documented layout | `f044f8f71342`  |
| 1313   | No documented layout | `f044f8f71342`  |
| 1311   | No documented layout | `f044f8f71342`  |
| 1309   | No documented layout | `f044f8f71342`  |
| 1304   | No documented layout | `f044f8f71342`  |
| 1292   | No documented layout | `f044f8f71342`  |
| 1286   | No documented layout | `f044f8f71342`  |
| 1280   | No documented layout | `f044f8f71342`  |
| 1276   | No documented layout | `f044f8f71342`  |
| 1267   | No file              | `f044f8f71342`  |
| 1261   | No file              | `f044f8f71342`  |
| 1256   | No file              | `f044f8f71342`  |
| 1250   | No file              | `f044f8f71342`  |
| 1246   | No file              | `f044f8f71342`  |
| 1239   | No file              | `f044f8f71342`  |
| 1230   | No file              | `f044f8f71342`  |
| 1226   | No file              | `f044f8f71342`  |
| 1220   | No file              | `f044f8f71342`  |
| 1217   | No file              | `f044f8f71342`  |
| 1211   | No file              | `f044f8f71342`  |
| 1210   | No file              | `f044f8f71342`  |
| 1208   | No file              | `f044f8f71342`  |
| 1203   | No file              | `f044f8f71342`  |
| 1197   | No file              | `f044f8f71342`  |
| 1194   | No file              | `f044f8f71342`  |
| 1192   | No file              | `f044f8f71342`  |
| 1187   | No file              | `f044f8f71342`  |
| 1183   | No file              | `f044f8f71342`  |
| 1177   | No file              | `f044f8f71342`  |
| 1173   | No file              | `f044f8f71342`  |
| 1167   | No file              | `f044f8f71342`  |
| 1164   | No file              | `f044f8f71342`  |
| 1156   | No file              | `f044f8f71342`  |
| 1149   | No file              | `f044f8f71342`  |
| 1144   | No file              | `f044f8f71342`  |
| 1137   | No file              | `f044f8f71342`  |
| 1132   | No file              | `f044f8f71342`  |
| 1127   | No file              | `f044f8f71342`  |
| 1122   | No file              | `f044f8f71342`  |
| 1118   | No file              | `f044f8f71342`  |
| 1114   | No file              | `f044f8f71342`  |
| 1109   | No file              | `f044f8f71342`  |
| 1102   | No file              | `f044f8f71342`  |
| 1096   | No file              | `f044f8f71342`  |
| 1088   | No file              | `f044f8f71342`  |
| 1081   | No file              | `f044f8f71342`  |
| 1076   | No file              | `f044f8f71342`  |
| 1069   | No file              | `f044f8f71342`  |
| 1064   | No file              | `f044f8f71342`  |
| 1058   | No file              | `f044f8f71342`  |
| 1051   | No file              | `f044f8f71342`  |
| 1044   | No file              | `f044f8f71342`  |
| 1036   | No file              | `f044f8f71342`  |
| 1026   | No file              | `f044f8f71342`  |
| 1016   | No file              | `f044f8f71342`  |
| 1009   | No file              | `f044f8f71342`  |
| 1005   | No file              | `f044f8f71342`  |
| 1000   | No file              | `f044f8f71342`  |
| 998    | No file              | `f044f8f71342`  |
| 990    | No file              | `f044f8f71342`  |
| 979    | No file              | `f044f8f71342`  |
| 972    | No file              | `f044f8f71342`  |
| 963    | No file              | `f044f8f71342`  |
| 955    | No file              | `f044f8f71342`  |
| 946    | No file              | `f044f8f71342`  |
| 938    | No file              | `f044f8f71342`  |
| 927    | No file              | `f044f8f71342`  |
| 911    | No file              | `f044f8f71342`  |
| 904    | No file              | `f044f8f71342`  |
| 899    | No file              | `f044f8f71342`  |
| 894    | No file              | `f044f8f71342`  |
| 885    | No file              | `f044f8f71342`  |
| 879    | No file              | `f044f8f71342`  |
| 872    | No file              | `f044f8f71342`  |
| 864    | No file              | `f044f8f71342`  |
| 855    | No file              | `f044f8f71342`  |
| 853    | No file              | `f044f8f71342`  |
| 845    | No file              | `f044f8f71342`  |
| 837    | No file              | `f044f8f71342`  |
| 829    | No file              | `f044f8f71342`  |
| 822    | No file              | `f044f8f71342`  |
| 814    | No file              | `f044f8f71342`  |
| 805    | No file              | `f044f8f71342`  |
| 794    | No file              | `f044f8f71342`  |
| 787    | No file              | `f044f8f71342`  |
| 780    | No file              | `f044f8f71342`  |
| 771    | No file              | `f044f8f71342`  |
| 760    | No file              | `f044f8f71342`  |
| 748    | No file              | `f044f8f71342`  |
| 741    | No file              | `f044f8f71342`  |
| 736    | No file              | `f044f8f71342`  |
| 731    | No file              | `f044f8f71342`  |
| 723    | No file              | `f044f8f71342`  |
| 711    | No file              | `f044f8f71342`  |
| 707    | No file              | `f044f8f71342`  |
| 697    | No file              | `f044f8f71342`  |
| 689    | No file              | `f044f8f71342`  |
| 683    | No file              | `f044f8f71342`  |
| 678    | No file              | `f044f8f71342`  |
| 670    | No file              | `f044f8f71342`  |
| 661    | No file              | `f044f8f71342`  |
| 656    | No file              | `f044f8f71342`  |
| 652    | No file              | `f044f8f71342`  |
| 643    | No file              | `f044f8f71342`  |
| 637    | No file              | `f044f8f71342`  |
| 630    | No file              | `f044f8f71342`  |
| 627    | No file              | `f044f8f71342`  |
| 621    | No file              | `f044f8f71342`  |
| 617    | No file              | `f044f8f71342`  |
| 615    | No file              | `f044f8f71342`  |
| 606    | No file              | `f044f8f71342`  |
| 599    | No file              | `f044f8f71342`  |
| 592    | No file              | `f044f8f71342`  |
| 586    | No file              | `f044f8f71342`  |
| 577    | No file              | `f044f8f71342`  |
| 569    | No file              | `f044f8f71342`  |
| 561    | No file              | `f044f8f71342`  |
| 554    | No file              | `f044f8f71342`  |
| 542    | No file              | `f044f8f71342`  |
| 532    | No file              | `f044f8f71342`  |
| 531    | No file              | `f044f8f71342`  |
| 526    | No file              | `f044f8f71342`  |
| 521    | No file              | `f044f8f71342`  |
| 517    | No file              | `f044f8f71342`  |
| 510    | No file              | `f044f8f71342`  |
| 508    | No file              | `f044f8f71342`  |
| 504    | No file              | `f044f8f71342`  |
| 497    | No file              | `f044f8f71342`  |
| 491    | No file              | `f044f8f71342`  |
| 485    | No file              | `f044f8f71342`  |
| 478    | No file              | `f044f8f71342`  |
| 472    | No file              | `f044f8f71342`  |
| 466    | No file              | `f044f8f71342`  |
| 457    | No file              | `f044f8f71342`  |
| 452    | No file              | `f044f8f71342`  |
| 449    | No file              | `f044f8f71342`  |
| 435    | No file              | `f044f8f71342`  |

<!-- versions:end -->

## Companion Files

| File                                | Required | Role                                                     |
| ----------------------------------- | -------- | -------------------------------------------------------- |
| `displayexchangeitemnpcoffset.dbss` | Optional | `dialog_key -> (data_offset, data_size)` index; the rows carry their own counts and can be walked without it |
| `characterstaticoffset.dbss`        | Optional | Every `characterstatic.dbss` key, so an NPC key without a row shows as plain text instead of a link |
| [`itemexchangebynpc.dbss`](itemexchangebynpc_dbss.md) | Optional | The need and result item and count of each listed key |
| `languagedata_en.loc`               | Optional | NPC name (type `6`) and the name the NPC shows in the dialog (type `38`, keyed `npc_character_key`, `dialog_index`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `124` on client 3474         |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 16 bytes + exchange keys)

| Offset                    | Type                     | Field                 | Notes                                                        |
| ------------------------- | ------------------------ | --------------------- | ------------------------------------------------------------ |
| `+0x00`                   | u16                      | npc_character_key     | NPC, a `characterstatic.dbss` key                            |
| `+0x02`                   | u16                      | dialog_index          | The NPC's dialog; with `npc_character_key` the `detail_dialog.dbss` key `dialog_index << 16 \| npc_character_key`, unique per row |
| `+0x04`                   | u64                      | item_exchange_count   | Number of `item_exchange_keys`; `1` to `22`, never `0` (client 3474) |
| `+0x0C`                   | u16[item_exchange_count] | item_exchange_keys    | `itemexchangebynpc.dbss` keys in window order, not sorted    |
| `item_exchange_keys+0x00` | u16                      | npc_character_key_dup | Equal to `npc_character_key` in every row                    |
| `item_exchange_keys+0x02` | u16                      | dialog_index_dup      | Equal to `dialog_index` in every row                         |

The rows are not sorted by key.

### `displayexchangeitemnpcoffset.dbss`

| Offset  | Type              | Field | Notes                                           |
| ------- | ----------------- | ----- | ----------------------------------------------- |
| `+0x00` | u32               | count | Equals the `displayexchangeitemnpc.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row            |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                      |
| ------- | ---- | ----------- | ---------------------------------------------------------- |
| `+0x00` | u32  | dialog_key  | `dialog_index << 16 \| npc_character_key` of the row       |
| `+0x04` | u32  | data_offset | Row start + 4, at `item_exchange_count`                    |
| `+0x08` | u32  | data_size   | Row size - 4: `16 + 2 * item_exchange_count - 4`           |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3474 every index row points
at the row with its key.

## Field Names

The row is the 2016 `gc::DisplayExchangeItemNpcStaticStatus`:
`_itemExchangeByNpcList` (a `pa_vector` of u16 `gc::KeyType`),
`_npcCharacterKey` (u16) and `_dialogIndex` (a u32 in memory, two bytes in
the file). The file writes the key pair before the list as the index key and
again after it. The 2016 `ge::wrapper::DisplayExchangeItemNpcStaticStatusWrapper`
holds a `gc::ItemExchangeByNpcStaticStatus` per list entry, whose
`_itemExchangeByNpcKey` is the u16 key of `itemexchangebynpc.dbss`.

The values match the `DisplayExchangeItemNpc` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `NPC` and `DialogIndex`:

| Field              | Column            | Same value (client 1784) | Same value (client 3474) |
| ------------------ | ----------------- | ------------------------ | ------------------------ |
| npc_character_key  | `NPC`             | 124 of 124 rows          | 124 of 124 rows          |
| dialog_index       | `DialogIndex`     | 124 of 124               | 124 of 124               |
| item_exchange_keys | `SetItemExchange` | 124 of 124               | 114 of 124               |

The 10 rows that differ on client 3474 drop keys from the sheet's list and
add none: `1` (Freharau `41081`), `3` (Andria `43002`, Mansha `50459`,
Thyshelle Arms `44106`), `56` (Gula `44307`) and `238`, `239` (Duncan
`40744`, dialogs `1` to `5`).

## Notes

- The exchange window Lua (`panel_dialog_exchange_item.luac`) reads the row
  of the open dialog through `getCurrentDisplayExchangeWrapper()`, walks
  `getItemExchangeByNpcListSize()` entries and skips an entry whose
  `getItemExchangeByNpcStaticStatusWrapperAtIndex()` is `nil`. Each shown
  entry gives the need item and `getNeedItemCount_s64()`, the result item
  and `getToItemCount_s64()`.
- On client 3474, 124 rows list 478 keys, 216 of them distinct, from `2` to
  `261`, for 81 NPCs. 80 rows are dialog `1`; Villa Keeper `45351` and Villa
  Butler `45345` have dialogs `1` to `17`, Duncan `40744` and EUROPA Event NPC
  `35633` dialogs `1` to `5` or `7`. Villager `637` dialog `750` (dialog name
  Combatant) is the one dialog index above `17`.
- 12 of the 216 keys have no `itemexchangebynpc.dbss` row on client 3474
  (`2`, `5`, `12`, `24`, `28`, `55`, `166`, `167`, `169`, `170`, `171`,
  `172`); on client 1784 4 of 221 have none (`1`, `2`, `5`, `12`). On client
  3474 every key of five rows has no row: Taphtar `45121` (`55`), Freharau
  `41081` (`2`), Crucio Domongatt `41014` dialog `1` and Dominic Erne
  `42109` dialogs `1` and `2` (`5`, `12`).
- None of the four NPCs of those rows has an exchange button in its main
  dialog (dialog `1`) on client 3474, checked in game: Freharau shows Shop
  and Conversation, Crucio Domongatt Conversation and Lord Information,
  Dominic Erne Conversation and Give Gift, and Taphtar Quest, Trade and
  Conversation. A row whose keys all lack an `itemexchangebynpc.dbss` row
  adds no exchange button. Dominic Erne's dialog `2` (`detail_dialog.dbss`
  key `173181`, option "[Return] Dominic Erne's Carnage Axe") was not seen.
- Taphtar's dialog `1` (`detail_dialog.dbss` key `110657`) also has the
  button type `ExceptExchange` and four `[EXC]` options (Shakatu's Rarity
  Box, Memory Fragment x20, Advice of Valks (+50), Shakatu's Luxury Box).
  They are `detail_dialog.dbss` options, separate from the key `55` this
  table lists for him, and did not show on his main dialog.
- On client 3474, 121 of the 124 rows have a `detail_dialog.dbss` record
  for their dialog key; Anahi `45147`, Hetario `59227` and Pacuna `59228`
  (dialog `1`) have none.
