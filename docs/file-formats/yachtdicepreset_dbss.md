# `yachtdicepreset.dbss` Format

## Purpose

The dice presets of Yar!: each row is one preset, the five
[`yachtdice.dbss`](yachtdice_dbss.md) dice a player rolls.
[`yachtnpcdiceinfo.bss`](yachtnpcdiceinfo_bss.md) gives each NPC game one
preset by key. `yachtdicepresetoffset.dbss` is the index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes | Records       | Row bytes |
| ------ | -------------- | ---------------------------- | ----- | ------------- | --------- |
| 1      | 1614 and later | `yachtdicepreset.dbss`       | 872   | 31 Row        | 28        |
| 1      | 1614 and later | `yachtdicepresetoffset.dbss` | 376   | 31 Offset Row | 12        |

| Layout | File                         | Known          | Unknown    |
| ------ | ---------------------------- | -------------- | ---------- |
| 1      | `yachtdicepreset.dbss`       | 872 B (100.0%) | 0 B (0.0%) |
| 1      | `yachtdicepresetoffset.dbss` | 376 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `29bbdad01bbb`  |
| 3482   | Layout 1 | `29bbdad01bbb`  |
| 3474   | Layout 1 | `29bbdad01bbb`  |
| 3473   | Layout 1 | `29bbdad01bbb`  |
| 3464   | Layout 1 | `29bbdad01bbb`  |
| 3458   | Layout 1 | `29bbdad01bbb`  |
| 3454   | Layout 1 | `29bbdad01bbb`  |
| 3444   | Layout 1 | `29bbdad01bbb`  |
| 3435   | Layout 1 | `29bbdad01bbb`  |
| 3426   | Layout 1 | `29bbdad01bbb`  |
| 3418   | Layout 1 | `29bbdad01bbb`  |
| 3412   | Layout 1 | `29bbdad01bbb`  |
| 3402   | Layout 1 | `29bbdad01bbb`  |
| 3396   | Layout 1 | `29bbdad01bbb`  |
| 3387   | Layout 1 | `29bbdad01bbb`  |
| 3381   | Layout 1 | `29bbdad01bbb`  |
| 3373   | Layout 1 | `29bbdad01bbb`  |
| 3364   | Layout 1 | `29bbdad01bbb`  |
| 3356   | Layout 1 | `29bbdad01bbb`  |
| 3349   | Layout 1 | `29bbdad01bbb`  |
| 3342   | Layout 1 | `29bbdad01bbb`  |
| 3335   | Layout 1 | `29bbdad01bbb`  |
| 3326   | Layout 1 | `29bbdad01bbb`  |
| 3321   | Layout 1 | `29bbdad01bbb`  |
| 3314   | Layout 1 | `29bbdad01bbb`  |
| 3303   | Layout 1 | `29bbdad01bbb`  |
| 3302   | Layout 1 | `29bbdad01bbb`  |
| 3293   | Layout 1 | `29bbdad01bbb`  |
| 3283   | Layout 1 | `29bbdad01bbb`  |
| 3275   | Layout 1 | `29bbdad01bbb`  |
| 3267   | Layout 1 | `29bbdad01bbb`  |
| 3258   | Layout 1 | `29bbdad01bbb`  |
| 3251   | Layout 1 | `29bbdad01bbb`  |
| 3242   | Layout 1 | `29bbdad01bbb`  |
| 3235   | Layout 1 | `29bbdad01bbb`  |
| 3229   | Layout 1 | `29bbdad01bbb`  |
| 3212   | Layout 1 | `29bbdad01bbb`  |
| 3203   | Layout 1 | `29bbdad01bbb`  |
| 3193   | Layout 1 | `29bbdad01bbb`  |
| 3186   | Layout 1 | `29bbdad01bbb`  |
| 3177   | Layout 1 | `29bbdad01bbb`  |
| 3169   | Layout 1 | `29bbdad01bbb`  |
| 3158   | Layout 1 | `29bbdad01bbb`  |
| 3151   | Layout 1 | `29bbdad01bbb`  |
| 3144   | Layout 1 | `29bbdad01bbb`  |
| 3133   | Layout 1 | `29bbdad01bbb`  |
| 3125   | Layout 1 | `29bbdad01bbb`  |
| 3118   | Layout 1 | `29bbdad01bbb`  |
| 3111   | Layout 1 | `29bbdad01bbb`  |
| 3103   | Layout 1 | `29bbdad01bbb`  |
| 3095   | Layout 1 | `29bbdad01bbb`  |
| 3086   | Layout 1 | `29bbdad01bbb`  |
| 3072   | Layout 1 | `29bbdad01bbb`  |
| 3062   | Layout 1 | `29bbdad01bbb`  |
| 3052   | Layout 1 | `29bbdad01bbb`  |
| 3045   | Layout 1 | `29bbdad01bbb`  |
| 3037   | Layout 1 | `29bbdad01bbb`  |
| 3030   | Layout 1 | `29bbdad01bbb`  |
| 3021   | Layout 1 | `29bbdad01bbb`  |
| 3012   | Layout 1 | `29bbdad01bbb`  |
| 3002   | Layout 1 | `29bbdad01bbb`  |
| 2995   | Layout 1 | `29bbdad01bbb`  |
| 2987   | Layout 1 | `29bbdad01bbb`  |
| 2978   | Layout 1 | `29bbdad01bbb`  |
| 2970   | Layout 1 | `29bbdad01bbb`  |
| 2959   | Layout 1 | `29bbdad01bbb`  |
| 2951   | Layout 1 | `29bbdad01bbb`  |
| 2942   | Layout 1 | `29bbdad01bbb`  |
| 2935   | Layout 1 | `29bbdad01bbb`  |
| 2932   | Layout 1 | `29bbdad01bbb`  |
| 2923   | Layout 1 | `29bbdad01bbb`  |
| 2919   | Layout 1 | `29bbdad01bbb`  |
| 2907   | Layout 1 | `29bbdad01bbb`  |
| 2900   | Layout 1 | `29bbdad01bbb`  |
| 2891   | Layout 1 | `29bbdad01bbb`  |
| 2882   | Layout 1 | `29bbdad01bbb`  |
| 2872   | Layout 1 | `29bbdad01bbb`  |
| 2863   | Layout 1 | `29bbdad01bbb`  |
| 2855   | Layout 1 | `29bbdad01bbb`  |
| 2849   | Layout 1 | `29bbdad01bbb`  |
| 2844   | Layout 1 | `29bbdad01bbb`  |
| 2834   | Layout 1 | `29bbdad01bbb`  |
| 2825   | Layout 1 | `29bbdad01bbb`  |
| 2819   | Layout 1 | `29bbdad01bbb`  |
| 2811   | Layout 1 | `29bbdad01bbb`  |
| 2803   | Layout 1 | `29bbdad01bbb`  |
| 2794   | Layout 1 | `29bbdad01bbb`  |
| 2783   | Layout 1 | `29bbdad01bbb`  |
| 2774   | Layout 1 | `29bbdad01bbb`  |
| 2765   | Layout 1 | `29bbdad01bbb`  |
| 2756   | Layout 1 | `29bbdad01bbb`  |
| 2750   | Layout 1 | `29bbdad01bbb`  |
| 2743   | Layout 1 | `29bbdad01bbb`  |
| 2736   | Layout 1 | `29bbdad01bbb`  |
| 2726   | Layout 1 | `29bbdad01bbb`  |
| 2717   | Layout 1 | `29bbdad01bbb`  |
| 2709   | Layout 1 | `29bbdad01bbb`  |
| 2703   | Layout 1 | `29bbdad01bbb`  |
| 2695   | Layout 1 | `29bbdad01bbb`  |
| 2684   | Layout 1 | `29bbdad01bbb`  |
| 2672   | Layout 1 | `29bbdad01bbb`  |
| 2665   | Layout 1 | `29bbdad01bbb`  |
| 2657   | Layout 1 | `29bbdad01bbb`  |
| 2649   | Layout 1 | `29bbdad01bbb`  |
| 2644   | Layout 1 | `29bbdad01bbb`  |
| 2637   | Layout 1 | `29bbdad01bbb`  |
| 2629   | Layout 1 | `29bbdad01bbb`  |
| 2619   | Layout 1 | `29bbdad01bbb`  |
| 2612   | Layout 1 | `29bbdad01bbb`  |
| 2606   | Layout 1 | `29bbdad01bbb`  |
| 2602   | Layout 1 | `29bbdad01bbb`  |
| 2601   | Layout 1 | `29bbdad01bbb`  |
| 2592   | Layout 1 | `29bbdad01bbb`  |
| 2583   | Layout 1 | `29bbdad01bbb`  |
| 2575   | Layout 1 | `29bbdad01bbb`  |
| 2567   | Layout 1 | `29bbdad01bbb`  |
| 2560   | Layout 1 | `29bbdad01bbb`  |
| 2553   | Layout 1 | `29bbdad01bbb`  |
| 2545   | Layout 1 | `29bbdad01bbb`  |
| 2538   | Layout 1 | `29bbdad01bbb`  |
| 2529   | Layout 1 | `29bbdad01bbb`  |
| 2519   | Layout 1 | `29bbdad01bbb`  |
| 2513   | Layout 1 | `29bbdad01bbb`  |
| 2510   | Layout 1 | `29bbdad01bbb`  |
| 2507   | Layout 1 | `29bbdad01bbb`  |
| 2503   | Layout 1 | `29bbdad01bbb`  |
| 2498   | Layout 1 | `29bbdad01bbb`  |
| 2492   | Layout 1 | `29bbdad01bbb`  |
| 2487   | Layout 1 | `29bbdad01bbb`  |
| 2480   | Layout 1 | `29bbdad01bbb`  |
| 2474   | Layout 1 | `29bbdad01bbb`  |
| 2468   | Layout 1 | `29bbdad01bbb`  |
| 2460   | Layout 1 | `29bbdad01bbb`  |
| 2453   | Layout 1 | `29bbdad01bbb`  |
| 2444   | Layout 1 | `29bbdad01bbb`  |
| 2438   | Layout 1 | `29bbdad01bbb`  |
| 2434   | Layout 1 | `29bbdad01bbb`  |
| 2429   | Layout 1 | `29bbdad01bbb`  |
| 2421   | Layout 1 | `29bbdad01bbb`  |
| 2414   | Layout 1 | `29bbdad01bbb`  |
| 2407   | Layout 1 | `29bbdad01bbb`  |
| 2401   | Layout 1 | `29bbdad01bbb`  |
| 2397   | Layout 1 | `29bbdad01bbb`  |
| 2393   | Layout 1 | `29bbdad01bbb`  |
| 2384   | Layout 1 | `29bbdad01bbb`  |
| 2378   | Layout 1 | `29bbdad01bbb`  |
| 2372   | Layout 1 | `29bbdad01bbb`  |
| 2358   | Layout 1 | `29bbdad01bbb`  |
| 2352   | Layout 1 | `29bbdad01bbb`  |
| 2347   | Layout 1 | `29bbdad01bbb`  |
| 2343   | Layout 1 | `29bbdad01bbb`  |
| 2335   | Layout 1 | `29bbdad01bbb`  |
| 2327   | Layout 1 | `29bbdad01bbb`  |
| 2324   | Layout 1 | `29bbdad01bbb`  |
| 2319   | Layout 1 | `29bbdad01bbb`  |
| 2313   | Layout 1 | `29bbdad01bbb`  |
| 2308   | Layout 1 | `29bbdad01bbb`  |
| 2302   | Layout 1 | `29bbdad01bbb`  |
| 2295   | Layout 1 | `29bbdad01bbb`  |
| 2290   | Layout 1 | `29bbdad01bbb`  |
| 2284   | Layout 1 | `29bbdad01bbb`  |
| 2276   | Layout 1 | `29bbdad01bbb`  |
| 2269   | Layout 1 | `29bbdad01bbb`  |
| 2259   | Layout 1 | `29bbdad01bbb`  |
| 2250   | Layout 1 | `29bbdad01bbb`  |
| 2243   | Layout 1 | `29bbdad01bbb`  |
| 2235   | Layout 1 | `29bbdad01bbb`  |
| 2229   | Layout 1 | `29bbdad01bbb`  |
| 2224   | Layout 1 | `29bbdad01bbb`  |
| 2218   | Layout 1 | `29bbdad01bbb`  |
| 2215   | Layout 1 | `29bbdad01bbb`  |
| 2207   | Layout 1 | `29bbdad01bbb`  |
| 2203   | Layout 1 | `29bbdad01bbb`  |
| 2196   | Layout 1 | `29bbdad01bbb`  |
| 2192   | Layout 1 | `29bbdad01bbb`  |
| 2189   | Layout 1 | `29bbdad01bbb`  |
| 2183   | Layout 1 | `29bbdad01bbb`  |
| 2179   | Layout 1 | `29bbdad01bbb`  |
| 2171   | Layout 1 | `29bbdad01bbb`  |
| 2163   | Layout 1 | `29bbdad01bbb`  |
| 2156   | Layout 1 | `29bbdad01bbb`  |
| 2151   | Layout 1 | `29bbdad01bbb`  |
| 2147   | Layout 1 | `29bbdad01bbb`  |
| 2142   | Layout 1 | `29bbdad01bbb`  |
| 2138   | Layout 1 | `29bbdad01bbb`  |
| 2134   | Layout 1 | `29bbdad01bbb`  |
| 2130   | Layout 1 | `29bbdad01bbb`  |
| 2122   | Layout 1 | `29bbdad01bbb`  |
| 2107   | Layout 1 | `29bbdad01bbb`  |
| 2098   | Layout 1 | `29bbdad01bbb`  |
| 2089   | Layout 1 | `29bbdad01bbb`  |
| 2081   | Layout 1 | `29bbdad01bbb`  |
| 2073   | Layout 1 | `29bbdad01bbb`  |
| 2067   | Layout 1 | `29bbdad01bbb`  |
| 2063   | Layout 1 | `29bbdad01bbb`  |
| 2059   | Layout 1 | `29bbdad01bbb`  |
| 2052   | Layout 1 | `29bbdad01bbb`  |
| 2044   | Layout 1 | `29bbdad01bbb`  |
| 2039   | Layout 1 | `29bbdad01bbb`  |
| 2032   | Layout 1 | `29bbdad01bbb`  |
| 2025   | Layout 1 | `29bbdad01bbb`  |
| 2011   | Layout 1 | `29bbdad01bbb`  |
| 2005   | Layout 1 | `29bbdad01bbb`  |
| 2000   | Layout 1 | `29bbdad01bbb`  |
| 1996   | Layout 1 | `29bbdad01bbb`  |
| 1991   | Layout 1 | `29bbdad01bbb`  |
| 1985   | Layout 1 | `29bbdad01bbb`  |
| 1980   | Layout 1 | `29bbdad01bbb`  |
| 1969   | Layout 1 | `29bbdad01bbb`  |
| 1964   | Layout 1 | `29bbdad01bbb`  |
| 1958   | Layout 1 | `29bbdad01bbb`  |
| 1950   | Layout 1 | `29bbdad01bbb`  |
| 1945   | Layout 1 | `29bbdad01bbb`  |
| 1937   | Layout 1 | `29bbdad01bbb`  |
| 1933   | Layout 1 | `29bbdad01bbb`  |
| 1927   | Layout 1 | `29bbdad01bbb`  |
| 1921   | Layout 1 | `29bbdad01bbb`  |
| 1914   | Layout 1 | `29bbdad01bbb`  |
| 1908   | Layout 1 | `29bbdad01bbb`  |
| 1897   | Layout 1 | `29bbdad01bbb`  |
| 1892   | Layout 1 | `29bbdad01bbb`  |
| 1886   | Layout 1 | `29bbdad01bbb`  |
| 1881   | Layout 1 | `29bbdad01bbb`  |
| 1871   | Layout 1 | `29bbdad01bbb`  |
| 1866   | Layout 1 | `29bbdad01bbb`  |
| 1862   | Layout 1 | `29bbdad01bbb`  |
| 1854   | Layout 1 | `29bbdad01bbb`  |
| 1846   | Layout 1 | `29bbdad01bbb`  |
| 1838   | Layout 1 | `29bbdad01bbb`  |
| 1832   | Layout 1 | `29bbdad01bbb`  |
| 1826   | Layout 1 | `29bbdad01bbb`  |
| 1822   | Layout 1 | `29bbdad01bbb`  |
| 1818   | Layout 1 | `29bbdad01bbb`  |
| 1804   | Layout 1 | `29bbdad01bbb`  |
| 1794   | Layout 1 | `29bbdad01bbb`  |
| 1790   | Layout 1 | `29bbdad01bbb`  |
| 1784   | Layout 1 | `29bbdad01bbb`  |
| 1774   | Layout 1 | `29bbdad01bbb`  |
| 1771   | Layout 1 | `29bbdad01bbb`  |
| 1762   | Layout 1 | `29bbdad01bbb`  |
| 1759   | Layout 1 | `29bbdad01bbb`  |
| 1754   | Layout 1 | `29bbdad01bbb`  |
| 1749   | Layout 1 | `29bbdad01bbb`  |
| 1743   | Layout 1 | `29bbdad01bbb`  |
| 1737   | Layout 1 | `29bbdad01bbb`  |
| 1731   | Layout 1 | `29bbdad01bbb`  |
| 1725   | Layout 1 | `29bbdad01bbb`  |
| 1717   | Layout 1 | `29bbdad01bbb`  |
| 1710   | Layout 1 | `29bbdad01bbb`  |
| 1704   | Layout 1 | `29bbdad01bbb`  |
| 1698   | Layout 1 | `29bbdad01bbb`  |
| 1690   | Layout 1 | `29bbdad01bbb`  |
| 1685   | Layout 1 | `29bbdad01bbb`  |
| 1680   | Layout 1 | `29bbdad01bbb`  |
| 1674   | Layout 1 | `29bbdad01bbb`  |
| 1668   | Layout 1 | `29bbdad01bbb`  |
| 1659   | Layout 1 | `29bbdad01bbb`  |
| 1649   | Layout 1 | `29bbdad01bbb`  |
| 1642   | Layout 1 | `29bbdad01bbb`  |
| 1636   | Layout 1 | `29bbdad01bbb`  |
| 1628   | Layout 1 | `29bbdad01bbb`  |
| 1622   | Layout 1 | `29bbdad01bbb`  |
| 1614   | Layout 1 | `29bbdad01bbb`  |
| 1608   | No file  | `29bbdad01bbb`  |
| 1602   | No file  | `29bbdad01bbb`  |
| 1598   | No file  | `29bbdad01bbb`  |
| 1594   | No file  | `29bbdad01bbb`  |
| 1590   | No file  | `29bbdad01bbb`  |
| 1587   | No file  | `29bbdad01bbb`  |
| 1584   | No file  | `29bbdad01bbb`  |
| 1579   | No file  | `29bbdad01bbb`  |
| 1572   | No file  | `29bbdad01bbb`  |
| 1565   | No file  | `29bbdad01bbb`  |
| 1559   | No file  | `29bbdad01bbb`  |
| 1554   | No file  | `29bbdad01bbb`  |
| 1547   | No file  | `29bbdad01bbb`  |
| 1537   | No file  | `29bbdad01bbb`  |
| 1529   | No file  | `29bbdad01bbb`  |
| 1524   | No file  | `29bbdad01bbb`  |
| 1519   | No file  | `29bbdad01bbb`  |
| 1509   | No file  | `29bbdad01bbb`  |
| 1506   | No file  | `29bbdad01bbb`  |
| 1504   | No file  | `29bbdad01bbb`  |
| 1500   | No file  | `29bbdad01bbb`  |
| 1493   | No file  | `29bbdad01bbb`  |
| 1489   | No file  | `29bbdad01bbb`  |
| 1485   | No file  | `29bbdad01bbb`  |
| 1481   | No file  | `29bbdad01bbb`  |
| 1474   | No file  | `29bbdad01bbb`  |
| 1466   | No file  | `29bbdad01bbb`  |
| 1462   | No file  | `29bbdad01bbb`  |
| 1459   | No file  | `29bbdad01bbb`  |
| 1453   | No file  | `29bbdad01bbb`  |
| 1450   | No file  | `29bbdad01bbb`  |
| 1445   | No file  | `29bbdad01bbb`  |
| 1439   | No file  | `29bbdad01bbb`  |
| 1433   | No file  | `29bbdad01bbb`  |
| 1430   | No file  | `29bbdad01bbb`  |
| 1426   | No file  | `29bbdad01bbb`  |
| 1421   | No file  | `29bbdad01bbb`  |
| 1417   | No file  | `29bbdad01bbb`  |
| 1416   | No file  | `29bbdad01bbb`  |
| 1409   | No file  | `29bbdad01bbb`  |
| 1405   | No file  | `29bbdad01bbb`  |
| 1401   | No file  | `29bbdad01bbb`  |
| 1396   | No file  | `29bbdad01bbb`  |
| 1391   | No file  | `29bbdad01bbb`  |
| 1390   | No file  | `29bbdad01bbb`  |
| 1386   | No file  | `29bbdad01bbb`  |
| 1381   | No file  | `29bbdad01bbb`  |
| 1379   | No file  | `29bbdad01bbb`  |
| 1372   | No file  | `29bbdad01bbb`  |
| 1366   | No file  | `29bbdad01bbb`  |
| 1364   | No file  | `29bbdad01bbb`  |
| 1363   | No file  | `29bbdad01bbb`  |
| 1360   | No file  | `29bbdad01bbb`  |
| 1358   | No file  | `29bbdad01bbb`  |
| 1355   | No file  | `29bbdad01bbb`  |
| 1351   | No file  | `29bbdad01bbb`  |
| 1348   | No file  | `29bbdad01bbb`  |
| 1346   | No file  | `29bbdad01bbb`  |
| 1341   | No file  | `29bbdad01bbb`  |
| 1340   | No file  | `29bbdad01bbb`  |
| 1338   | No file  | `29bbdad01bbb`  |
| 1335   | No file  | `29bbdad01bbb`  |
| 1333   | No file  | `29bbdad01bbb`  |
| 1329   | No file  | `29bbdad01bbb`  |
| 1327   | No file  | `29bbdad01bbb`  |
| 1324   | No file  | `29bbdad01bbb`  |
| 1321   | No file  | `29bbdad01bbb`  |
| 1319   | No file  | `29bbdad01bbb`  |
| 1318   | No file  | `29bbdad01bbb`  |
| 1316   | No file  | `29bbdad01bbb`  |
| 1313   | No file  | `29bbdad01bbb`  |
| 1311   | No file  | `29bbdad01bbb`  |
| 1309   | No file  | `29bbdad01bbb`  |
| 1304   | No file  | `29bbdad01bbb`  |
| 1292   | No file  | `29bbdad01bbb`  |
| 1286   | No file  | `29bbdad01bbb`  |
| 1280   | No file  | `29bbdad01bbb`  |
| 1276   | No file  | `29bbdad01bbb`  |
| 1267   | No file  | `29bbdad01bbb`  |
| 1261   | No file  | `29bbdad01bbb`  |
| 1256   | No file  | `29bbdad01bbb`  |
| 1250   | No file  | `29bbdad01bbb`  |
| 1246   | No file  | `29bbdad01bbb`  |
| 1239   | No file  | `29bbdad01bbb`  |
| 1230   | No file  | `29bbdad01bbb`  |
| 1226   | No file  | `29bbdad01bbb`  |
| 1220   | No file  | `29bbdad01bbb`  |
| 1217   | No file  | `29bbdad01bbb`  |
| 1211   | No file  | `29bbdad01bbb`  |
| 1210   | No file  | `29bbdad01bbb`  |
| 1208   | No file  | `29bbdad01bbb`  |
| 1203   | No file  | `29bbdad01bbb`  |
| 1197   | No file  | `29bbdad01bbb`  |
| 1194   | No file  | `29bbdad01bbb`  |
| 1192   | No file  | `29bbdad01bbb`  |
| 1187   | No file  | `29bbdad01bbb`  |
| 1183   | No file  | `29bbdad01bbb`  |
| 1177   | No file  | `29bbdad01bbb`  |
| 1173   | No file  | `29bbdad01bbb`  |
| 1167   | No file  | `29bbdad01bbb`  |
| 1164   | No file  | `29bbdad01bbb`  |
| 1156   | No file  | `29bbdad01bbb`  |
| 1149   | No file  | `29bbdad01bbb`  |
| 1144   | No file  | `29bbdad01bbb`  |
| 1137   | No file  | `29bbdad01bbb`  |
| 1132   | No file  | `29bbdad01bbb`  |
| 1127   | No file  | `29bbdad01bbb`  |
| 1122   | No file  | `29bbdad01bbb`  |
| 1118   | No file  | `29bbdad01bbb`  |
| 1114   | No file  | `29bbdad01bbb`  |
| 1109   | No file  | `29bbdad01bbb`  |
| 1102   | No file  | `29bbdad01bbb`  |
| 1096   | No file  | `29bbdad01bbb`  |
| 1088   | No file  | `29bbdad01bbb`  |
| 1081   | No file  | `29bbdad01bbb`  |
| 1076   | No file  | `29bbdad01bbb`  |
| 1069   | No file  | `29bbdad01bbb`  |
| 1064   | No file  | `29bbdad01bbb`  |
| 1058   | No file  | `29bbdad01bbb`  |
| 1051   | No file  | `29bbdad01bbb`  |
| 1044   | No file  | `29bbdad01bbb`  |
| 1036   | No file  | `29bbdad01bbb`  |
| 1026   | No file  | `29bbdad01bbb`  |
| 1016   | No file  | `29bbdad01bbb`  |
| 1009   | No file  | `29bbdad01bbb`  |
| 1005   | No file  | `29bbdad01bbb`  |
| 1000   | No file  | `29bbdad01bbb`  |
| 998    | No file  | `29bbdad01bbb`  |
| 990    | No file  | `29bbdad01bbb`  |
| 979    | No file  | `29bbdad01bbb`  |
| 972    | No file  | `29bbdad01bbb`  |
| 963    | No file  | `29bbdad01bbb`  |
| 955    | No file  | `29bbdad01bbb`  |
| 946    | No file  | `29bbdad01bbb`  |
| 938    | No file  | `29bbdad01bbb`  |
| 927    | No file  | `29bbdad01bbb`  |
| 911    | No file  | `29bbdad01bbb`  |
| 904    | No file  | `29bbdad01bbb`  |
| 899    | No file  | `29bbdad01bbb`  |
| 894    | No file  | `29bbdad01bbb`  |
| 885    | No file  | `29bbdad01bbb`  |
| 879    | No file  | `29bbdad01bbb`  |
| 872    | No file  | `29bbdad01bbb`  |
| 864    | No file  | `29bbdad01bbb`  |
| 855    | No file  | `29bbdad01bbb`  |
| 853    | No file  | `29bbdad01bbb`  |
| 845    | No file  | `29bbdad01bbb`  |
| 837    | No file  | `29bbdad01bbb`  |
| 829    | No file  | `29bbdad01bbb`  |
| 822    | No file  | `29bbdad01bbb`  |
| 814    | No file  | `29bbdad01bbb`  |
| 805    | No file  | `29bbdad01bbb`  |
| 794    | No file  | `29bbdad01bbb`  |
| 787    | No file  | `29bbdad01bbb`  |
| 780    | No file  | `29bbdad01bbb`  |
| 771    | No file  | `29bbdad01bbb`  |
| 760    | No file  | `29bbdad01bbb`  |
| 748    | No file  | `29bbdad01bbb`  |
| 741    | No file  | `29bbdad01bbb`  |
| 736    | No file  | `29bbdad01bbb`  |
| 731    | No file  | `29bbdad01bbb`  |
| 723    | No file  | `29bbdad01bbb`  |
| 711    | No file  | `29bbdad01bbb`  |
| 707    | No file  | `29bbdad01bbb`  |
| 697    | No file  | `29bbdad01bbb`  |
| 689    | No file  | `29bbdad01bbb`  |
| 683    | No file  | `29bbdad01bbb`  |
| 678    | No file  | `29bbdad01bbb`  |
| 670    | No file  | `29bbdad01bbb`  |
| 661    | No file  | `29bbdad01bbb`  |
| 656    | No file  | `29bbdad01bbb`  |
| 652    | No file  | `29bbdad01bbb`  |
| 643    | No file  | `29bbdad01bbb`  |
| 637    | No file  | `29bbdad01bbb`  |
| 630    | No file  | `29bbdad01bbb`  |
| 627    | No file  | `29bbdad01bbb`  |
| 621    | No file  | `29bbdad01bbb`  |
| 617    | No file  | `29bbdad01bbb`  |
| 615    | No file  | `29bbdad01bbb`  |
| 606    | No file  | `29bbdad01bbb`  |
| 599    | No file  | `29bbdad01bbb`  |
| 592    | No file  | `29bbdad01bbb`  |
| 586    | No file  | `29bbdad01bbb`  |
| 577    | No file  | `29bbdad01bbb`  |
| 569    | No file  | `29bbdad01bbb`  |
| 561    | No file  | `29bbdad01bbb`  |
| 554    | No file  | `29bbdad01bbb`  |
| 542    | No file  | `29bbdad01bbb`  |
| 532    | No file  | `29bbdad01bbb`  |
| 531    | No file  | `29bbdad01bbb`  |
| 526    | No file  | `29bbdad01bbb`  |
| 521    | No file  | `29bbdad01bbb`  |
| 517    | No file  | `29bbdad01bbb`  |
| 510    | No file  | `29bbdad01bbb`  |
| 508    | No file  | `29bbdad01bbb`  |
| 504    | No file  | `29bbdad01bbb`  |
| 497    | No file  | `29bbdad01bbb`  |
| 491    | No file  | `29bbdad01bbb`  |
| 485    | No file  | `29bbdad01bbb`  |
| 478    | No file  | `29bbdad01bbb`  |
| 472    | No file  | `29bbdad01bbb`  |
| 466    | No file  | `29bbdad01bbb`  |
| 457    | No file  | `29bbdad01bbb`  |
| 452    | No file  | `29bbdad01bbb`  |
| 449    | No file  | `29bbdad01bbb`  |
| 435    | No file  | `29bbdad01bbb`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                                     |
| ---------------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `yachtdicepresetoffset.dbss` | Optional | `key -> (data_offset, data_size)` of every row; the rows have one fixed size and can be walked without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `31` on client 3474          |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (28 bytes)

| Offset  | Type   | Field               | Notes                                                      |
| ------- | ------ | ------------------- | ---------------------------------------------------------- |
| `+0x00` | u32    | dice_preset_key     | Preset key; unique per row                                 |
| `+0x04` | u32    | dice_preset_key_dup | Equal to `dice_preset_key` in every row; the offset file points here |
| `+0x08` | u32[5] | dice_keys           | Keys of `yachtdice.dbss`, one per die, in sheet order      |

The rows run from key 15 down to 1, then from 31 down to 16 (clients 1784
and 3474).

### `yachtdicepresetoffset.dbss`

| Offset  | Type              | Field | Notes                                   |
| ------- | ----------------- | ----- | --------------------------------------- |
| `+0x00` | u32               | count | Equals the `yachtdicepreset.dbss` count |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row    |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                    |
| ------- | ---- | ----------- | -------------------------------------------------------- |
| `+0x00` | u32  | key         | Key of the row it points at                              |
| `+0x04` | u32  | data_offset | Row start + 4, at `dice_preset_key_dup`                  |
| `+0x08` | u32  | data_size   | The row without its leading key: `24`                    |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The
index rows are in file order, and every index row points at the row with
its key (clients 1784 and 3474).

## Presets

On client 3474 presets 1 to 24 each hold one die of a single symbol (dice
1 to 4), one die of mixed symbols (dice 6 to 11) and three odd or even dice
(12 to 15). Preset 25 holds the mixed dice 6 to 10, 26 the dice 1 to 5,
and 27 to 31 mixes of the others. The NPC games of `yachtnpcdiceinfo.bss`
use presets 1, 25, 26 and 31.

## Field Names

The `DicePreset` sheet of a private server's `datasheet_minigame.xlsm` on
client 1784 has the columns `PresetIndex` (`dice_preset_key`) and
`DiceList` (`dice_keys`, one comma-separated list). Its 31 rows match the
31 rows of clients 1784 and 3474, dice order included. The note column
`#참고` names each preset by its symbol, eye and odd or even dice
(`해,1,홀수`: sun, 1, odd). The file writes the key twice: once as the
index key, once inside the row.

## Notes

- Clients 1784 and 3474 ship the same `yachtdicepreset.dbss` and
  `yachtdicepresetoffset.dbss`, byte for byte.
